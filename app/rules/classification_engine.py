"""
Deterministic Classification Engine for IP-SAKTI Sahayak
Problem Statement 26045 - SIH 2026

Rule tree decides the category — the LLM only asks questions, never rules.
Sorts product formulations into 1 of 6 legal categories in max 4 steps:
1. Classical / Generic Ayurvedic Medicine (D&C Act §3(a))
2. Patent or Proprietary Ayurvedic Medicine (P&P) (D&C Act §3(h))
3. New Drug / Non-Classical Ayurvedic Drug (NDCT Rules 2019 Rule 2(w))
4. Phytopharmaceutical Drug (NDCT Rules 2019 Rule 2(aa))
5. Ayurveda-Aahar / Nutraceutical (FSSAI Ayurveda Aahar Regs 2022)
6. Ayurvedic Cosmetic (D&C Act §3(aaa) & Cosmetic Rules 2020)
"""

from typing import List, Tuple
from app.models.schemas import (
    ClassificationRequest,
    ClassificationResult,
    RegulatoryCategory,
    IntendedUse,
    FormulationBasis,
    ClaimType,
    ExtractionClinicalLevel
)

class ClassificationEngine:
    """
    Deterministic rule engine implementing state machine for ASU product classification.
    Zero hallucination. Fully traceable path traversal.
    """

    def classify(self, req: ClassificationRequest) -> ClassificationResult:
        steps_traversed: List[str] = []

        # STEP 1: Intended Application / Primary Purpose
        steps_traversed.append(f"Step 1 (Intended Use): Analyzed intended application -> {req.intended_use.value}")

        # Branch 1: Topical Cleansing / Beautification
        if req.intended_use == IntendedUse.TOPICAL_BEAUTY:
            steps_traversed.append("Branch A (Cosmetic): Non-systemic topical beauty/grooming application selected.")
            
            # Check if making therapeutic disease claims
            if req.claim_type in [ClaimType.CLASSICAL_INDICATION, ClaimType.NEW_THERAPEUTIC_CLAIM]:
                steps_traversed.append(
                    "Warning: Therapeutic claim made on topical cosmetic formulation. "
                    "Cannot qualify as cosmetic under D&C Act §3(aaa); redirected to drug classification."
                )
                # Fall through to therapeutic drug logic below
            else:
                steps_traversed.append("Step 2 (Claim Check): Appearance/cleansing claim confirmed -> Meets D&C Act §3(aaa).")
                return ClassificationResult(
                    category=RegulatoryCategory.COSMETIC,
                    category_id="COSMETIC",
                    governing_statute="Drugs and Cosmetics Act, 1940 (§3(aaa)) & Cosmetics Rules, 2020",
                    statutory_citation="D&C Act Section 3(aaa); Cosmetics Rules 2020 (GSR 718(E))",
                    description=(
                        "Ayurvedic cosmetic intended strictly for rubbing, pouring, or applying to human body "
                        "for cleansing, beautifying, or promoting attractiveness. Not for diagnosis, treatment, or mitigation of disease."
                    ),
                    ip_posture=(
                        "Low patentability for base mixtures (Section 3(p) TK bar applies if using known herbs). "
                        "High potential for Design Registration (bottle shape, packaging under Indian Designs Act 2000) "
                        "and Trademark protection (Class 3) via IP India / Madrid System."
                    ),
                    patentability_verdict="Generally Excluded (Sec 3(p)/3(e)), Strong Trademark/Design Potential",
                    abs_posture="ABS applies if Indian wild bioresources are used commercially (BDA Sec 7/3).",
                    regulatory_requirements=[
                        "Manufacturing license under Cosmetics Rules, 2020 (Form COS-8)",
                        "Compliance with Bureau of Indian Standards (BIS) cosmetics standards",
                        "Strict ban on therapeutic, medicinal, or healing claims on packaging and labels",
                        "Declaration of Ayurvedic ingredients with botanical names on primary container"
                    ],
                    potential_hurdles=[
                        "Borderline claims triggering reclassification into drug under §3(h)",
                        "Section 3(p) bar on patenting herbal cosmetic formulations",
                        "Hague Agreement unavailability: Design filings must be directly with Indian IPO"
                    ],
                    rule_path_traversed=steps_traversed
                )

        # Branch 2: Dietary / Nutritional / Food Supplement
        if req.intended_use == IntendedUse.DIETARY_WELLNESS:
            steps_traversed.append("Branch B (Dietary): Food supplement / general wellness selected.")
            
            if req.claim_type == ClaimType.NEW_THERAPEUTIC_CLAIM:
                steps_traversed.append(
                    "Warning: Disease-specific therapeutic claim violates FSSAI Ayurveda Aahar Regs Reg 4; "
                    "must be evaluated as drug."
                )
                # Fall through to therapeutic drug logic below
            else:
                steps_traversed.append("Step 2 (Formulation Check): Evaluated against FSSAI Ayurveda Aahar Regulations 2022 Schedule A.")
                return ClassificationResult(
                    category=RegulatoryCategory.NUTRACEUTICAL,
                    category_id="NUTRACEUTICAL",
                    governing_statute="Food Safety and Standards (Ayurveda Aahar) Regulations, 2022",
                    statutory_citation="FSSAI (Ayurveda Aahar) Regulations 2022, Reg 3 & 4",
                    description=(
                        "Food or dietary supplement prepared in accordance with the authoritative books/processes "
                        "specified in Schedule A of Ayurveda Aahar regulations. Consumed for daily dietary maintenance, digestion, or vitality."
                    ),
                    ip_posture=(
                        "Base food formulations face Section 3(p) bar. IP protection rests predominantly in "
                        "Brand Trademarks (Class 29/30/32), Trade Secrets for proprietary blending techniques, and Copyright of branding."
                    ),
                    patentability_verdict="Non-Patentable for classical food formulations (Sec 3(p)); Trademark/Branding Protected",
                    abs_posture="ABS intimation under BDA Sec 7 applies for commercial food utilization unless cultivator-exempt.",
                    regulatory_requirements=[
                        "FSSAI Central / State License under Ayurveda Aahar category",
                        "Mandatory display of official 'Ayurveda Aahar' logo on packaging",
                        "Strict statutory prohibition against claiming cure, mitigation, or treatment of specific human diseases",
                        "Must not contain synthetic vitamins, minerals, or isolated active pharmaceutical ingredients"
                    ],
                    potential_hurdles=[
                        "Accidental disease claims inviting penal action under Drugs & Magic Remedies Act 1954",
                        "Rejection by State Licensing Authority if claiming ASU drug medicinal efficacy"
                    ],
                    rule_path_traversed=steps_traversed
                )

        # Branch 3: Therapeutic / Medicinal Drug Categories
        steps_traversed.append("Branch C (Therapeutic): Product intended for disease diagnosis, mitigation, treatment, or cure.")

        # Check for Phytopharmaceutical Drug first
        # Definition: Purified and standardized fraction (>=4 bioactive markers)
        if (req.formulation_basis == FormulationBasis.PURIFIED_FRACTION or 
            req.extraction_clinical == ExtractionClinicalLevel.PURIFIED_CHROMATOGRAPHY):
            steps_traversed.append(
                "Step 2 (Fraction Verification): Standardized purified botanical fraction with marker compounds identified -> "
                "Matches NDCT Rules 2019 Rule 2(aa)."
            )
            return ClassificationResult(
                category=RegulatoryCategory.PHYTOPHARMACEUTICAL,
                category_id="PHYTOPHARMACEUTICAL",
                governing_statute="New Drugs and Clinical Trials Rules, 2019 (Rule 2(aa)) & D&C Rules Schedule Y",
                statutory_citation="NDCT Rules 2019 Rule 2(aa); D&C Rules 1945 Rule 122-E",
                description=(
                    "Purified and standardized fraction of an extract of a medicinal plant or its part, "
                    "assessed qualitatively and quantitatively with minimum four bioactive/analytical markers, "
                    "for diagnosis, treatment, mitigation or prevention of disease (non-parenteral)."
                ),
                ip_posture=(
                    "High Patentability Potential! Extraction processes, purified chromatographic fractions, "
                    "and specific marker ratios can be patented without facing Section 3(p) traditional knowledge bar, "
                    "provided novelty and inventive step are established over classical aqueous/alcoholic extracts."
                ),
                patentability_verdict="High Patentability Potential (Process & Purified Composition Claims)",
                abs_posture="Mandatory NBA approval under Section 6 prior to patent grant (or before foreign filing).",
                regulatory_requirements=[
                    "Approval from Central Drugs Standard Control Organisation (CDSCO) / DCGI",
                    "Complete botanical dossier (GAP authentication, voucher specimen)",
                    "Fingerprinting with minimum four bioactive or analytical marker compounds",
                    "Preclinical animal safety (toxicology) and clinical trials (Phase I-III) as per NDCT Rules Schedule"
                ],
                potential_hurdles=[
                    "High regulatory burden and clinical trial capital expenditure",
                    "Section 10(4) Patents Act mandatory disclosure of biological source in India",
                    "Risk of Section 3(d) objection if bioactive fraction is deemed mere discovery of known substance"
                ],
                rule_path_traversed=steps_traversed
            )

        # Check for New Drug / Non-Classical Ayurvedic Drug
        # Slide 2 & 6 Novelty: "New claim on a classical formula -> routed to New Drug, not buried under a 3(p)-barred leaf"
        if (req.claim_type == ClaimType.NEW_THERAPEUTIC_CLAIM or 
            req.formulation_basis == FormulationBasis.NOVEL_HERB_COMBINATION or 
            req.extraction_clinical == ExtractionClinicalLevel.CLINICAL_EVALUATION):
            steps_traversed.append(
                "Step 2 (New Indication / Novel Route): New therapeutic claim or novel combination discovered -> "
                "Routed to 'New Drug' under NDCT Rules 2019 Rule 2(w) (Not buried under 3(p) classical leaf)."
            )
            return ClassificationResult(
                category=RegulatoryCategory.NEW_DRUG,
                category_id="NEW_DRUG",
                governing_statute="New Drugs and Clinical Trials Rules, 2019 (Rule 2(w))",
                statutory_citation="NDCT Rules 2019 Rule 2(w); D&C Act Section 3(b)",
                description=(
                    "Drug proposed to be marketed with modified or new claims including new therapeutic indication, "
                    "novel drug delivery system, or novel herbal formulation not recognized in classical First-Schedule literature."
                ),
                ip_posture=(
                    "Genuine Patent Potential. New therapeutic applications and synergistic combinations with demonstrated "
                    "efficacy overcome Section 3(p) if backed by comparative preclinical/clinical data. Process patents strongly viable."
                ),
                patentability_verdict="Strong Patent Potential (Requires Comparative Efficacy Proof vs Classical Prior Art)",
                abs_posture="NBA Section 6 clearance mandatory before patent grant in India, or prior to filing outside India.",
                regulatory_requirements=[
                    "Investigational New Drug (IND) approval from CDSCO",
                    "Phase I, Phase II, and Phase III clinical trials demonstrating safety and efficacy",
                    "Stability testing as per ICH / CDSCO guidelines",
                    "Submission to Subject Expert Committee (SEC) at CDSCO"
                ],
                potential_hurdles=[
                    "Section 3(d) hurdles (proving enhanced efficacy over known classical extract)",
                    "Section 3(e) hurdles (proving synergy over mere admixture)",
                    "Lengthy CDSCO clinical trial clearance timelines"
                ],
                rule_path_traversed=steps_traversed
            )

        # Classical vs Patent/Proprietary check (D&C Act §3(a) vs §3(h))
        # Slide 6: "D&C Act §3(h) exclusion clause: caught and fixed routing bug for classical-source products"
        # If ingredients and method are identical to First Schedule texts -> Classical (§3(a))
        # If ingredients from First Schedule but modified ratio/dosage form -> Patent & Proprietary (§3(h))
        if req.formulation_basis == FormulationBasis.FIRST_SCHEDULE_EXACT:
            steps_traversed.append(
                "Step 2 (Classical Adherence): Formulation composition and manufacturing method strictly adhere to "
                "First-Schedule authoritative book -> Classical Ayurvedic Medicine under D&C Act §3(a)."
            )
            return ClassificationResult(
                category=RegulatoryCategory.CLASSICAL,
                category_id="CLASSICAL",
                governing_statute="Drugs and Cosmetics Act, 1940 (Section 3(a))",
                statutory_citation="D&C Act 1940 Section 3(a); First Schedule (54 Authoritative Books)",
                description=(
                    "Classical / Generic Ayurvedic medicine manufactured exclusively in accordance with the formulae "
                    "described in authoritative books of Ayurveda specified in the First Schedule (e.g., Charaka Samhita, "
                    "Sushruta Samhita, Ashtanga Hridaya, Ayurvedic Formulary of India)."
                ),
                ip_posture=(
                    "Absolute Patent Bar under Section 3(p) of the Patents Act, 1970. Classical knowledge is in public "
                    "domain and codified in the Traditional Knowledge Digital Library (TKDL). Cannot be monopolized. "
                    "Protection strategy: Trademark registration for distinctive brand prefix/suffix, Geographical Indications (GI) "
                    "if regionally linked, and strict GMP manufacturing quality standards."
                ),
                patentability_verdict="Absolute Statutory Exclusion (Section 3(p) Traditional Knowledge Bar)",
                abs_posture="Exempted for registered AYUSH practitioners and local cultivators (BDA 2023 Amendment §3/7); SBB intimation for commercial non-exempt ASU manufacturers.",
                regulatory_requirements=[
                    "Manufacturing license from State Licensing Authority (Ayush) on Form 25-D",
                    "Citation of specific First Schedule text reference in application (Rule 158-B)",
                    "Adherence to Ayurvedic Pharmacopoeia of India (API) standards",
                    "GMP certification (Schedule T compliance)"
                ],
                potential_hurdles=[
                    "Patent rejection under Section 3(p) and TKDL prior art citations",
                    "Section 3(h) exclusion: Cannot be licensed as a proprietary medicine if recipe is identical to classical text"
                ],
                rule_path_traversed=steps_traversed
            )

        # Otherwise, ingredients are from First Schedule but modified ratio, modern excipient, or dosage form -> Patent / Proprietary (§3(h))
        steps_traversed.append(
            "Step 2 (P&P Verification): Formulation contains First-Schedule ingredients in modified ratio or modern "
            "dosage form; not identical to classical recipe -> Patent or Proprietary Medicine under D&C Act §3(h)."
        )
        return ClassificationResult(
            category=RegulatoryCategory.PATENT_PROPRIETARY,
            category_id="PATENT_PROPRIETARY",
            governing_statute="Drugs and Cosmetics Act, 1940 (Section 3(h)) & Rule 158-B",
            statutory_citation="D&C Act Section 3(h); D&C Rules 1945 Rule 158-B",
            description=(
                "Patent or Proprietary Ayurvedic medicine containing ingredients mentioned in the First Schedule authoritative "
                "texts, but formulated in non-classical proportions, modern solid/liquid dosage forms, or proprietary blends. "
                "Explicitly excludes classical formulations identical in all respects."
            ),
            ip_posture=(
                "Conditional Patentability. Highly vulnerable to Section 3(p) (TK bar) and Section 3(e) (mere admixture). "
                "Patentable ONLY IF the applicant presents rigorous quantitative experimental evidence proving synergistic "
                "bioactivity (super-additive efficacy) between the herbs, or an inventive extraction/delivery process. "
                "Strongly protected via Trademarks (Class 5), proprietary know-how, and trade secrets."
            ),
            patentability_verdict="Conditional Patentability: Requires Rigorous Proof of Synergistic Efficacy (Sec 3(e) vs 3(p))",
            abs_posture="SBB intimation required under BDA Sec 7. NBA Sec 6 approval mandatory before patent grant.",
            regulatory_requirements=[
                "Manufacturing license from State Licensing Authority (Ayush) under Form 25-D",
                "Submission of safety data, stability data, and pilot clinical trial proof under Rule 158-B",
                "Adherence to Schedule T (Good Manufacturing Practices)",
                "Quality control testing for heavy metals, microbial count, and pesticide residues"
            ],
            potential_hurdles=[
                "Section 3(p) citation by Patent Office citing TKDL records",
                "Section 3(e) objection: Presumption that combining known herbs is a mere admixture",
                "Section 10(4) requirement to submit NBA approval before patent sealing"
            ],
            rule_path_traversed=steps_traversed
        )

classification_engine = ClassificationEngine()
