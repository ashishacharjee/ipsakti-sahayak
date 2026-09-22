"""
Data models and schemas for IP-SAKTI Sahayak
Problem Statement 26045 - Smart India Hackathon 2026
"""

from enum import Enum
from typing import List, Dict, Optional, Any
from pydantic import BaseModel, Field


class RegulatoryCategory(str, Enum):
    CLASSICAL = "Classical / Generic Ayurvedic Medicine"
    PATENT_PROPRIETARY = "Patent or Proprietary Ayurvedic Medicine (P&P)"
    NEW_DRUG = "New Drug / Non-Classical Ayurvedic Drug"
    PHYTOPHARMACEUTICAL = "Phytopharmaceutical Drug"
    NUTRACEUTICAL = "Ayurveda-Aahar / Nutraceutical"
    COSMETIC = "Ayurvedic Cosmetic"


class ApplicantType(str, Enum):
    FOREIGN_ENTITY = "Foreign Entity / NRI / Foreign Participation (Sec 3 BDA)"
    INDIAN_COMMERCIAL = "Indian Commercial Entity / Company / LLP (Sec 7 BDA)"
    AYUSH_PRACTITIONER = "Registered AYUSH Practitioner / Vaidya / Hakim (Exempted)"
    CULTIVATOR_COMMUNITY = "Local Grower / Cultivator / Community (Exempted)"


class IntendedUse(str, Enum):
    THERAPEUTIC = "Therapeutic / Medicinal Treatment or Cure"
    DIETARY_WELLNESS = "Dietary / General Health & Nutritional Support"
    TOPICAL_BEAUTY = "Topical Cleansing / Beautification / Skin Care"


class FormulationBasis(str, Enum):
    FIRST_SCHEDULE_EXACT = "First-Schedule Authoritative Text Formulation (Identical composition & method)"
    FIRST_SCHEDULE_MODIFIED = "First-Schedule Ingredients in Modified Ratio or Modern Dosage Form (Tablet/Capsule/Syrup)"
    PURIFIED_FRACTION = "Purified and Standardized Bioactive Fraction (≥4 active markers)"
    NOVEL_HERB_COMBINATION = "Novel / Unlisted Botanical Combination or Synthetic Admixture"


class ClaimType(str, Enum):
    CLASSICAL_INDICATION = "Classical Ayurvedic Indication (as described in authoritative scriptures)"
    NEW_THERAPEUTIC_CLAIM = "New Therapeutic Indication / Modern Disease Claim (e.g., Cancer, Diabetes, Alzheimer's)"
    GENERAL_WELLNESS = "General Health, Digestion, Immunity, or Vitality (Non-therapeutic)"
    COSMETIC_APPEARANCE = "External Cleansing, Glow, Moisturizing, Fragrance"


class ExtractionClinicalLevel(str, Enum):
    TRADITIONAL_AQUEOUS = "Traditional Aqueous / Kwath / Asava / Bhasma Method"
    HYDRO_ETHANOLIC = "Standard Hydro-ethanolic / Solvent Extraction"
    PURIFIED_CHROMATOGRAPHY = "Purified Bioactive Fraction with HPLC/HPTLC Fingerprint"
    CLINICAL_EVALUATION = "Phase I/II/III Clinical Safety & Efficacy Trials Undertaken"
    NONE_FOOD_GRADE = "Food Grade / Topical Formulation only"


class ClassificationRequest(BaseModel):
    intended_use: IntendedUse
    formulation_basis: FormulationBasis
    claim_type: ClaimType
    extraction_clinical: ExtractionClinicalLevel
    product_name: Optional[str] = "Ayurvedic Formulation"
    ingredients: Optional[List[str]] = Field(default_factory=list)
    description: Optional[str] = ""


class ClassificationResult(BaseModel):
    category: RegulatoryCategory
    category_id: str
    governing_statute: str
    statutory_citation: str
    description: str
    ip_posture: str
    patentability_verdict: str
    abs_posture: str
    regulatory_requirements: List[str]
    potential_hurdles: List[str]
    rule_path_traversed: List[str]


class ABSCheckRequest(BaseModel):
    applicant_type: ApplicantType
    is_commercial_utilization: bool = True
    filing_ipr_outside_india: bool = False
    filing_ipr_in_india: bool = True
    accessing_biological_resource: bool = True
    bioresource_name: Optional[str] = "Ayurvedic Biological Material"
    source_state: Optional[str] = "India"


class ABSCheckResult(BaseModel):
    applicant_type: ApplicantType
    applicant_track: str
    requires_nba_approval: bool
    requires_sbb_intimation: bool
    is_exempted: bool
    exemption_basis: Optional[str] = None
    statutory_provisions: List[str]
    mandated_forms: List[str]
    benefit_sharing_applicable: bool
    guidance_notes: str
    penal_provisions: str


class ConfidenceLevel(str, Enum):
    HIGH = "HIGH (>= 75/100)"
    MODERATE = "MODERATE (50-74/100) - Defers to Facilitator"
    LOW = "LOW (< 50/100) - Safe Abstention"


class EvidenceScoreBreakdown(BaseModel):
    source_agreement: float = Field(..., description="Max 35 points: Concordance across official sources")
    source_authority: float = Field(..., description="Max 20 points: Statutory hierarchy weight")
    currency_score: float = Field(..., description="Max 20 points: Recent active law (2023/2024)")
    jurisdiction_match: float = Field(..., description="Max 15 points: Relevance to selected jurisdiction")
    classification_certainty: float = Field(..., description="Max 10 points: Deterministic leaf confidence")
    total_score: float = Field(..., description="Out of 100 points")
    confidence_level: ConfidenceLevel
    hard_gate_triggered: bool = False
    hard_gate_reason: Optional[str] = None


class LegalSourceReference(BaseModel):
    provision_id: str
    statute_name: str
    section_or_rule: str
    year_and_amendment: str
    authority_type: str
    jurisdiction: str
    key_excerpt: str
    applicability_note: str
    official_source_url: str


class DualJurisdictionGuidance(BaseModel):
    national_guidance: Dict[str, Any]
    international_guidance: Dict[str, Any]
    evidence_score: EvidenceScoreBreakdown
    cited_provisions: List[LegalSourceReference]
    safe_abstention: bool
    abstention_reason: Optional[str] = None
    mandatory_disclaimer: str


class FullGuidanceRequest(BaseModel):
    classification: ClassificationRequest
    abs_check: Optional[ABSCheckRequest] = None
    query: Optional[str] = None
    jurisdiction: str = "dual"


class TKDLQueryRequest(BaseModel):
    formulation_name: str
    sanskrit_or_botanical_terms: List[str] = Field(default_factory=list)
    classical_texts: List[str] = Field(default_factory=list)
    therapeutic_target: Optional[str] = None


class TKDLQueryResponse(BaseModel):
    tkrc_codes: List[str]
    ipc_classes: List[str]
    structured_search_query: str
    identified_botanicals: List[Dict[str, str]]
    classical_text_references: List[str]
    disclaimer: str


class ReviewBriefRequest(BaseModel):
    classification: ClassificationResult
    abs_result: ABSCheckResult
    evidence_score: EvidenceScoreBreakdown
    user_query: Optional[str] = None
    formulation_name: Optional[str] = "Ayurvedic Formulation"
    key_ingredients: Optional[List[str]] = Field(default_factory=list)


class ReviewBriefResponse(BaseModel):
    brief_id: str
    generated_at: str
    case_summary: str
    classification_summary: Dict[str, Any]
    abs_summary: Dict[str, Any]
    ip_patentability_summary: Dict[str, Any]
    evidence_breakdown: EvidenceScoreBreakdown
    open_questions_for_human: List[str]
    cited_authorities: List[LegalSourceReference]
    recommended_next_steps: List[str]
    escalation_contact_info: Dict[str, str]
