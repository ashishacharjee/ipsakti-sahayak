"""
Facilitator Review Brief Service for IP-SAKTI Sahayak
Problem Statement 26045 - SIH 2026

Generates structured, auditable briefs for human IP facilitators, patent examiners,
and AYUSH regulatory officers when uncertainty or hard gates are triggered.
"""

import uuid
from datetime import datetime, timezone
from typing import List, Dict, Any
from app.models.schemas import (
    ReviewBriefRequest,
    ReviewBriefResponse,
    LegalSourceReference
)

class ReviewBriefService:
    def generate_brief(
        self,
        req: ReviewBriefRequest,
        cited_authorities: List[LegalSourceReference]
    ) -> ReviewBriefResponse:
        brief_id = f"SAKTI-BRIEF-{datetime.now(timezone.utc).strftime('%Y%m%d')}-{uuid.uuid4().hex[:6].upper()}"
        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

        # Compile open questions for human resolution
        open_questions: List[str] = []
        if req.classification.category_id == "PATENT_PROPRIETARY":
            open_questions.append(
                "Has the applicant generated comparative in-vitro or in-vivo pharmacological data "
                "proving synergistic bioactivity (super-additive efficacy) between the ingredients to overcome Section 3(e)?"
            )
            open_questions.append(
                "Is the manufacturing method distinct from standard classical decoction/tincture methods (e.g. specialized nano-delivery or CO2 supercritical extraction)?"
            )
        elif req.classification.category_id == "NEW_DRUG":
            open_questions.append(
                "Has CDSCO Investigational New Drug (IND) clearance or Phase II/III clinical trial protocol approval been granted?"
            )
            open_questions.append(
                "Does the specification contain clinical safety proof differentiating this new indication from historical Ayurvedic uses?"
            )
        elif req.classification.category_id == "PHYTOPHARMACEUTICAL":
            open_questions.append(
                "Are all minimum four bioactive or analytical marker compounds quantified with validated HPLC/HPTLC chromatograms as required by NDCT Rule 2(aa)?"
            )
        elif req.classification.category_id == "CLASSICAL":
            open_questions.append(
                "Has the applicant verified that the formula exactly matches one of the 54 First Schedule texts without any unapproved modern synthetic preservatives?"
            )

        if not req.abs_result.is_exempted:
            if req.abs_result.requires_nba_approval:
                open_questions.append(
                    f"Has Form {'I and III' if 'Foreign' in req.abs_result.applicant_track else 'III'} been submitted to the National Biodiversity Authority (NBA) Chennai?"
                )
            if req.abs_result.requires_sbb_intimation:
                open_questions.append(
                    f"Has formal written intimation been acknowledged by the State Biodiversity Board of {req.abs_result.applicant_type}?"
                )

        if req.evidence_score.hard_gate_triggered:
            open_questions.append(
                f"HARD GATE AUDIT: {req.evidence_score.hard_gate_reason} — Human legal facilitator must review statutory currency."
            )

        # Recommended action pathways
        next_steps = [
            f"1. Classification Pathway: Proceed under {req.classification.governing_statute}.",
            f"2. ABS Action: {'No ABS fee required (Statutory Exemption under 2023 Amendment)' if req.abs_result.is_exempted else 'File ' + ', '.join(req.abs_result.mandated_forms)}.",
            f"3. Patent Filing Strategy: {req.classification.patentability_verdict}.",
            "4. Prior-Art Clearance: Run the structured TKRC/IPC query in InPASS and WIPO Patentscope before filing."
        ]

        case_summary = (
            f"Regulatory & IP assessment for '{req.formulation_name}'. "
            f"Deterministically classified as '{req.classification.category.value}' governed by {req.classification.governing_statute}. "
            f"ABS Posture: {req.abs_result.applicant_track}. "
            f"Evidence Strength Score: {req.evidence_score.total_score}/100 ({req.evidence_score.confidence_level.value})."
        )

        escalation_contacts = {
            "facilitation_cell": "Ayush IP & Regulatory Facilitation Cell (Ministry of Ayush / AIIA)",
            "email": "ip-facilitator@aiia.gov.in / helpdesk-nba@gov.in",
            "statutory_authority": "National Biodiversity Authority, TICEL Bio Park, Chennai / Indian Patent Office",
            "hotline": "1800-11-AYUSH (29874)"
        }

        return ReviewBriefResponse(
            brief_id=brief_id,
            generated_at=timestamp,
            case_summary=case_summary,
            classification_summary={
                "category": req.classification.category.value,
                "statute": req.classification.governing_statute,
                "citation": req.classification.statutory_citation,
                "requirements": req.classification.regulatory_requirements,
                "rule_path": req.classification.rule_path_traversed
            },
            abs_summary={
                "track": req.abs_result.applicant_track,
                "is_exempted": req.abs_result.is_exempted,
                "exemption_basis": req.abs_result.exemption_basis,
                "required_forms": req.abs_result.mandated_forms,
                "provisions": req.abs_result.statutory_provisions,
                "notes": req.abs_result.guidance_notes
            },
            ip_patentability_summary={
                "patentability_verdict": req.classification.patentability_verdict,
                "ip_posture": req.classification.ip_posture,
                "potential_hurdles": req.classification.potential_hurdles
            },
            evidence_breakdown=req.evidence_score,
            open_questions_for_human=open_questions,
            cited_authorities=cited_authorities,
            recommended_next_steps=next_steps,
            escalation_contact_info=escalation_contacts
        )

review_brief_service = ReviewBriefService()
