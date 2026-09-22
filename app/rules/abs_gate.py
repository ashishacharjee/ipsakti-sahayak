"""
Access and Benefit-Sharing (ABS) Gate for IP-SAKTI Sahayak
Problem Statement 26045 - SIH 2026

Independent parallel check evaluating legal duties under:
- Biological Diversity Act, 2002 (as amended by BD (Amendment) Act, 2023)
- Biological Diversity Rules, 2024
- Section 6 & Section 10(4) of The Patents Act, 1970
- Nagoya Protocol on Access and Benefit Sharing
"""

from typing import List
from app.models.schemas import (
    ABSCheckRequest,
    ABSCheckResult,
    ApplicantType
)

class ABSGate:
    """
    Evaluates ABS obligations with 3-tier applicant-aware logic:
    Track 1: Foreign entities / Non-residents / Foreign-invested entities (BDA §3 & §6)
    Track 2: Indian commercial companies / LLPs (BDA §7 & §6)
    Track 3: Exempted registered AYUSH practitioners and local cultivators (BDA 2023 Amdt)
    """

    def evaluate(self, req: ABSCheckRequest) -> ABSCheckResult:
        provisions: List[str] = []
        mandated_forms: List[str] = []
        is_exempted = False
        exemption_basis = None
        requires_nba = False
        requires_sbb = False
        benefit_sharing = False
        guidance = []
        penalties = ""

        # TRACK 1: Exempted Registered AYUSH Practitioner
        if req.applicant_type == ApplicantType.AYUSH_PRACTITIONER:
            is_exempted = True
            exemption_basis = (
                "Section 7 Proviso & Section 3(2) of Biological Diversity (Amendment) Act, 2023: "
                "Explicitly exempts registered AYUSH practitioners (Vaidyas, Hakims, Siddha & Sowa-Rigpa practitioners) "
                "practicing indigenous systems of medicine from prior intimation to SBB and ABS benefit-sharing levies."
            )
            provisions.extend([
                "Biological Diversity (Amendment) Act 2023, Section 7 Proviso",
                "Biological Diversity Rules 2024, Rule 14"
            ])
            guidance.append("No SBB intimation or ABS royalty payment is required for routine patient dispensation or classical formulations.")
            if req.filing_ipr_in_india or req.filing_ipr_outside_india:
                requires_nba = True
                guidance.append(
                    "IMPORTANT NOTE: If applying for a commercial patent or IPR based on biological resources, "
                    "Section 6 of the BD Act still requires NBA approval (Form III) prior to patent grant."
                )
                mandated_forms.append("Form III (Application for seeking prior approval of NBA for applying for IPR)")
            penalties = "Practitioners are fully protected from Section 7 non-compliance notices under the 2023 statutory exemption."

            return ABSCheckResult(
                applicant_type=req.applicant_type,
                applicant_track="AYUSH Registered Practitioner Track (Exempted)",
                requires_nba_approval=requires_nba,
                requires_sbb_intimation=False,
                is_exempted=is_exempted,
                exemption_basis=exemption_basis,
                statutory_provisions=provisions,
                mandated_forms=mandated_forms,
                benefit_sharing_applicable=benefit_sharing,
                guidance_notes=" ".join(guidance),
                penal_provisions=penalties
            )

        # TRACK 2: Exempted Local Grower / Cultivator / Farmer
        if req.applicant_type == ApplicantType.CULTIVATOR_COMMUNITY:
            is_exempted = True
            exemption_basis = (
                "Section 7 Proviso of Biological Diversity (Amendment) Act, 2023: "
                "Explicitly exempts local people and communities of the area, including growers and cultivators of "
                "biodiversity, from prior intimation to State Biodiversity Board (SBB) for obtaining biological resources."
            )
            provisions.extend([
                "Biological Diversity (Amendment) Act 2023, Section 7 Proviso & Section 40",
                "Biological Diversity Rules 2024"
            ])
            guidance.append(
                "Growers and cultivators selling farmed Ayurvedic medicinal plants (e.g. Ashwagandha, Shatavari, Tulsi) "
                "are exempt from ABS levy. Maintain a Certificate of Origin from local agricultural / horticulture authority."
            )
            if req.filing_ipr_in_india or req.filing_ipr_outside_india:
                requires_nba = True
                mandated_forms.append("Form III (Application to NBA for IPR Approval)")
                guidance.append("If filing a patent on an extracted formulation or process, Section 6 NBA approval is mandated.")
            penalties = "Cultivator activities are exempt from civil ABS penalty mechanisms under amended Section 7."

            return ABSCheckResult(
                applicant_type=req.applicant_type,
                applicant_track="Local Cultivator & Grower Track (Exempted)",
                requires_nba_approval=requires_nba,
                requires_sbb_intimation=False,
                is_exempted=is_exempted,
                exemption_basis=exemption_basis,
                statutory_provisions=provisions,
                mandated_forms=mandated_forms,
                benefit_sharing_applicable=benefit_sharing,
                guidance_notes=" ".join(guidance),
                penal_provisions=penalties
            )

        # TRACK 3: Foreign Entity / Non-Resident / Foreign Ownership Participation
        if req.applicant_type == ApplicantType.FOREIGN_ENTITY:
            requires_nba = True
            requires_sbb = False  # Foreign entities deal directly with NBA, not SBB!
            benefit_sharing = True
            provisions.extend([
                "Biological Diversity Act 2002 (as amended 2023), Section 3",
                "Biological Diversity Act 2002 (as amended 2023), Section 6",
                "Biological Diversity Rules 2024, Form I & Form III Schedules",
                "Patents Act 1970, Section 10(4)(d)(ii)"
            ])
            mandated_forms.append("Form I (Application for access to biological resources occurring in India)")
            if req.filing_ipr_in_india or req.filing_ipr_outside_india:
                mandated_forms.append("Form III (Application for approval of NBA for applying for IPR)")

            guidance.append(
                "STRICT RESTRICTION: Non-Indian entities, foreign individuals, or Indian entities with any foreign equity/management "
                "CANNOT access or obtain Indian biological resources without prior written approval of the National Biodiversity Authority (Form I)."
            )
            if req.filing_ipr_outside_india:
                guidance.append(
                    "CRITICAL: If filing IPR outside India (e.g. USPTO, EPO, PCT), NBA approval must be obtained BEFORE FILING. "
                    "Filing abroad prior to NBA clearance is a statutory violation."
                )
            else:
                guidance.append(
                    "For patent applications within India, NBA approval must be obtained and submitted to the Indian Patent Office "
                    "prior to the grant of the patent."
                )
            guidance.append(
                "Benefit-sharing agreement is mandatory. Standard ABS rates under 2024 Rules range from 0.1% to 0.5% of ex-factory sale price, "
                "or negotiated upfront fees and royalties."
            )
            penalties = (
                "Section 55A (amended 2023): Civil penalty by Adjudicating Officer ranging from Rs. 1 Lakh up to Rs. 50 Lakhs, "
                "with an additional penalty up to Rs. 1 Crore in case of continuing contravention. "
                "Under Patents Act Section 64(1)(p), failure to comply is a ground for revocation of patent."
            )

            return ABSCheckResult(
                applicant_type=req.applicant_type,
                applicant_track="Foreign Entity / Foreign Participation Track (Strict Section 3/6 NBA)",
                requires_nba_approval=requires_nba,
                requires_sbb_intimation=requires_sbb,
                is_exempted=False,
                exemption_basis=None,
                statutory_provisions=provisions,
                mandated_forms=mandated_forms,
                benefit_sharing_applicable=benefit_sharing,
                guidance_notes=" ".join(guidance),
                penal_provisions=penalties
            )

        # TRACK 4: Indian Commercial Entity / Corporate / LLP
        requires_sbb = True
        benefit_sharing = req.is_commercial_utilization
        provisions.extend([
            "Biological Diversity Act 2002 (as amended 2023), Section 7",
            "Biological Diversity Act 2002 (as amended 2023), Section 6",
            "Biological Diversity Rules 2024, Form I (SBB) & Form III (NBA)",
            "Patents Act 1970, Section 10(4)(d)(ii)"
        ])
        mandated_forms.append("Form I (State Biodiversity Board - Prior Intimation for Commercial Utilization)")

        guidance.append(
            "Indian commercial enterprises sourcing wild or unprocessed Indian bioresources must give prior intimation "
            "to the State Biodiversity Board (SBB) of the state where materials are procured."
        )

        if req.filing_ipr_in_india or req.filing_ipr_outside_india:
            requires_nba = True
            mandated_forms.append("Form III (NBA Prior Approval for IPR Application)")
            if req.filing_ipr_outside_india:
                guidance.append(
                    "Filing patent outside India (PCT / Direct Foreign Phase) requires PRIOR NBA APPROVAL before filing abroad."
                )
            else:
                guidance.append(
                    "Filing patent in India: Section 6 approval must be obtained prior to the grant/sealing of the patent."
                )

        if benefit_sharing:
            guidance.append(
                "Fair and Equitable Benefit Sharing (ABS) applies under 2024 Rules based on annual gross ex-factory turnover: "
                "0.1% (turnover up to 1 Cr), 0.2% (1-3 Cr), 0.5% (above 3 Cr)."
            )

        penalties = (
            "Section 55A: Non-intimation or failure to comply attracts penalty up to Rs. 50 Lakhs determined by Adjudicating Officer. "
            "Patent applications face pre-grant opposition under Section 25(1)(j) for lack of disclosure of biological origin."
        )

        return ABSCheckResult(
            applicant_type=req.applicant_type,
            applicant_track="Indian Commercial Entity Track (Section 7 SBB & Section 6 NBA)",
            requires_nba_approval=requires_nba,
            requires_sbb_intimation=requires_sbb,
            is_exempted=False,
            exemption_basis=None,
            statutory_provisions=provisions,
            mandated_forms=mandated_forms,
            benefit_sharing_applicable=benefit_sharing,
            guidance_notes=" ".join(guidance),
            penal_provisions=penalties
        )

abs_gate = ABSGate()
