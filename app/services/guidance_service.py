"""
Integrated Guidance Service for IP-SAKTI Sahayak
Problem Statement 26045 - SIH 2026

Orchestrates classification, ABS check, dual-jurisdiction retrieval,
evidence scoring, safe abstention, and review brief compilation.
"""

from typing import Dict, Any, List, Optional
from app.models.schemas import (
    ClassificationRequest,
    ClassificationResult,
    ABSCheckRequest,
    ABSCheckResult,
    DualJurisdictionGuidance,
    EvidenceScoreBreakdown,
    LegalSourceReference,
    ConfidenceLevel,
    ReviewBriefRequest,
    ReviewBriefResponse,
    ClaimType,
    ExtractionClinicalLevel
)
from app.rules.classification_engine import classification_engine
from app.rules.abs_gate import abs_gate
from app.services.retrieval import legal_retrieval
from app.services.evidence_scorer import evidence_engine
from app.services.review_brief import review_brief_service
from app.corpus.corpus_manager import corpus_manager

MANDATORY_DISCLAIMER = (
    "DISCLAIMER: IP-SAKTI Sahayak provides statutory and regulatory informational guidance based on verified "
    "legal corpora (D&C Act, Patents Act, Biological Diversity Act 2023/2024, NDCT Rules, and International Treaties). "
    "This tool DOES NOT provide formal legal advice, patent prosecution services, or judicial certification. "
    "All decisions regarding patent filing and regulatory submissions should be confirmed with a registered Patent Agent, "
    "Advocate, or the official Ayush IP Facilitation Cell."
)

class IntegratedGuidanceService:
    def process_guidance(
        self,
        classification_req: ClassificationRequest,
        abs_req: ABSCheckRequest,
        free_text_query: Optional[str] = None,
        jurisdiction_mode: str = "dual"
    ) -> DualJurisdictionGuidance:
        
        # 1. Deterministic Classification
        classif_result = classification_engine.classify(classification_req)

        # 2. Independent ABS Evaluation
        abs_result = abs_gate.evaluate(abs_req)

        # 3. Dual Jurisdiction Retrieval
        query_text = (
            f"{classification_req.product_name} {free_text_query or ''} "
            f"{classif_result.category.value} {classification_req.claim_type.value} "
            f"{' '.join(classification_req.ingredients or [])}"
        ).strip()

        india_provisions, intl_provisions = legal_retrieval.retrieve_dual_jurisdiction(
            query=query_text,
            category_tag=classif_result.category.value,
            top_k_each=4
        )

        all_retrieved = india_provisions + intl_provisions

        # Detect potential contradiction or borderline flags (Slide 4 Hard Gates)
        has_contradiction = False
        is_borderline = False

        # 1. Flag borderline: New therapeutic claim on herbal formula without clinical safety & efficacy proof
        if (classification_req.claim_type == ClaimType.NEW_THERAPEUTIC_CLAIM and 
            classification_req.extraction_clinical != ExtractionClinicalLevel.CLINICAL_EVALUATION):
            is_borderline = True

        # 2. Flag contradiction: Claiming prohibited disease cure without clinical trials (DMRA 1954 violation risk)
        combined_text = f"{classification_req.product_name} {free_text_query or ''} {classification_req.description or ''}".lower()
        if any(term in combined_text for term in ["cancer cure", "diabetes cure", "blindness cure", "epilepsy cure"]):
            if classification_req.extraction_clinical != ExtractionClinicalLevel.CLINICAL_EVALUATION:
                has_contradiction = True

        # 4. Evidence Strength Calculation (100-pt engine)
        score_breakdown = evidence_engine.calculate_score(
            retrieved_provisions=all_retrieved,
            category_id=classif_result.category_id,
            jurisdiction_requested=jurisdiction_mode,
            has_contradiction=has_contradiction,
            has_stale_source=False,
            is_borderline=is_borderline
        )

        # Convert provisions to LegalSourceReference
        cited_references: List[LegalSourceReference] = []
        seen_ids = set()
        for p in all_retrieved:
            if p["id"] not in seen_ids:
                seen_ids.add(p["id"])
                cited_references.append(corpus_manager.to_source_reference(p))

        # 5. Formulate National (India) Guidance Layer
        national_layer = self._assemble_national_layer(classif_result, abs_result, india_provisions)

        # 6. Formulate International Guidance Layer
        intl_layer = self._assemble_international_layer(classif_result, abs_result, intl_provisions)

        # Safe Abstention logic: If score < 75 or hard gate triggered, abstain from definitive advice
        safe_abstention = score_breakdown.total_score < 75.0 or score_breakdown.hard_gate_triggered
        abstention_reason = None
        if safe_abstention:
            if score_breakdown.hard_gate_triggered:
                abstention_reason = (
                    f"Safe Abstention Active: {score_breakdown.hard_gate_reason} "
                    f"Automatic Facilitator Review Brief generated for human expert review."
                )
            else:
                abstention_reason = (
                    f"Safe Abstention Active: Evidence strength score ({score_breakdown.total_score}/100) is below "
                    f"the 75-point statutory confidence threshold. Groundwork has been compiled into a Facilitator Review Brief."
                )

        return DualJurisdictionGuidance(
            national_guidance=national_layer,
            international_guidance=intl_layer,
            evidence_score=score_breakdown,
            cited_provisions=cited_references,
            safe_abstention=safe_abstention,
            abstention_reason=abstention_reason,
            mandatory_disclaimer=MANDATORY_DISCLAIMER
        )

    def _assemble_national_layer(
        self,
        classif: ClassificationResult,
        abs_res: ABSCheckResult,
        provisions: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        return {
            "jurisdiction": "India (National)",
            "classification_category": classif.category.value,
            "governing_statute": classif.governing_statute,
            "statutory_citation": classif.statutory_citation,
            "ip_patentability_assessment": classif.patentability_verdict,
            "ip_strategy": classif.ip_posture,
            "statutory_bars_evaluated": [
                "Patents Act 1970 Section 3(p) (§3(p)) - Traditional Knowledge Bar (TKDL checked)",
                "Patents Act 1970 Section 3(e) (§3(e)) - Mere Admixture Bar (Synergistic efficacy requirement)",
                "Patents Act 1970 Section 10(4) (§10(4)) - Mandatory Disclosure of Indian Bioresource Origin"
            ],
            "abs_compliance_status": {
                "applicant_track": abs_res.applicant_track,
                "is_exempted": abs_res.is_exempted,
                "exemption_basis": abs_res.exemption_basis,
                "mandated_forms": abs_res.mandated_forms,
                "action_required": (
                    "No ABS royalty required under 2023 statutory exemption." 
                    if abs_res.is_exempted 
                    else f"File {', '.join(abs_res.mandated_forms)} before commercial utilization/IPR filing."
                ),
                "penalties": abs_res.penal_provisions
            },
            "regulatory_pathway": classif.regulatory_requirements,
            "critical_traps": classif.potential_hurdles,
            "key_provisions_cited": [p["section"] + " (" + p["statute"] + ")" for p in provisions]
        }

    def _assemble_international_layer(
        self,
        classif: ClassificationResult,
        abs_res: ABSCheckResult,
        provisions: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        return {
            "jurisdiction": "International (WIPO / PCT / Treaties / Export Regimes)",
            "wipo_gratk_treaty_status": {
                "treaty_name": "WIPO Treaty on IP, Genetic Resources & Associated Traditional Knowledge (2024)",
                "status": "Adopted May 24, 2024; Awaiting 15 ratifications to enter into force (Honest status)",
                "impact": "Mandatory patent disclosure of country of origin of genetic resources and indigenous traditional knowledge upon entry into force."
            },
            "nagoya_protocol_abs": {
                "treaty": "Nagoya Protocol on ABS (CBD)",
                "requirement": "International user checkpoints mandate Internationally Recognized Certificate of Compliance (IRCC) via Indian NBA for cross-border transfer."
            },
            "patent_filing_channels": {
                "pct_system": "WIPO PCT provides 30/31-month national phase entry in 155+ states.",
                "nba_foreign_filing_rule": "CRITICAL: Under Section 6 BDA, NBA approval must be obtained BEFORE filing a patent outside India!"
            },
            "trademark_and_design": {
                "madrid_system": "India is a member; file single international trademark application via Indian IP Office (Classes 3, 5, 30).",
                "hague_agreement_alert": "FACTUAL DISTINCTION: India is NOT a member of the Hague Agreement. Bottle & packaging designs cannot be filed via Hague designating India; must file directly with Kolkata Patent Office under Indian Designs Act 2000."
            },
            "export_market_regulatory_access": {
                "united_states": "US FDA Botanical Drug Guidance (prescription IND/NDA pathway) vs DSHEA (dietary supplement, strictly structure/function claims only).",
                "european_union": "EU Directive 2004/24/EC (THMPD) requires proof of 30 years continuous use, including 15 years within the EU."
            },
            "microbial_deposit": "Budapest Treaty: MTCC Chandigarh / NCMR Pune for Ayurvedic fermented cultures (Asavas/Arishtas)."
        }

guidance_service = IntegratedGuidanceService()
