import re
from app.models.schemas import (
    ClassificationRequest,
    ABSCheckRequest,
    IntendedUse,
    FormulationBasis,
    ClaimType,
    ExtractionClinicalLevel,
    ApplicantType
)

class QueryParser:
    """
    Intelligently parses the user's free-text formulation query to dynamically infer
    the correct regulatory classification enums, bypassing hardcoded frontend defaults.
    """

    def parse_query_to_overrides(
        self, 
        query: str, 
        classification: ClassificationRequest, 
        abs_check: ABSCheckRequest
    ):
        q = query.lower()

        # ----------------------------------------------------
        # 1. Infer Intended Use & Claim Type
        # ----------------------------------------------------
        # Cosmetic / Topical
        if any(w in q for w in ["cosmetic", "glow", "skin", "hair", "cleansing", "shampoo", "cream", "lotion", "beauty"]):
            classification.intended_use = IntendedUse.TOPICAL_BEAUTY
            classification.claim_type = ClaimType.COSMETIC_APPEARANCE
        # Dietary / Nutraceutical
        elif any(w in q for w in ["diet", "supplement", "nutrition", "wellness", "immunity", "energy", "vitality", "drink", "aahar"]):
            classification.intended_use = IntendedUse.DIETARY_WELLNESS
            classification.claim_type = ClaimType.GENERAL_WELLNESS
        # Modern Therapeutic Claims (New Drug / Patentable)
        elif any(w in q for w in ["cancer", "diabetes", "alzheimer", "tumor", "covid", "cure", "disease", "syndrome", "clinical"]):
            classification.intended_use = IntendedUse.THERAPEUTIC
            classification.claim_type = ClaimType.NEW_THERAPEUTIC_CLAIM
        else:
            # Default to classical therapeutic if no modern/cosmetic keywords are found
            classification.intended_use = IntendedUse.THERAPEUTIC
            classification.claim_type = ClaimType.CLASSICAL_INDICATION

        # ----------------------------------------------------
        # 2. Infer Formulation Basis (Crucial for Sec 3(p) vs 3(e) vs Novel)
        # ----------------------------------------------------
        if any(w in q for w in ["fraction", "purified", "standardized", "marker", "bioactive", "hplc", "chromatography", "nano"]):
            classification.formulation_basis = FormulationBasis.PURIFIED_FRACTION
        elif any(w in q for w in ["novel", "synthetic", "admixture", "new combination", "inventive", "synergy", "synergistic"]):
            classification.formulation_basis = FormulationBasis.NOVEL_HERB_COMBINATION
        elif any(w in q for w in ["tablet", "capsule", "syrup", "modified", "ratio", "modern form", "suspension", "gel"]):
            classification.formulation_basis = FormulationBasis.FIRST_SCHEDULE_MODIFIED
        else:
            # If they explicitly mention classical texts or exact traditional terms
            if any(w in q for w in ["samhita", "classical", "exact", "traditional recipe", "bhasma", "kwath", "churna"]):
                classification.formulation_basis = FormulationBasis.FIRST_SCHEDULE_EXACT
            else:
                pass # Keep frontend defaults

        # ----------------------------------------------------
        # 3. Infer Extraction / Clinical Level
        # ----------------------------------------------------
        if any(w in q for w in ["hplc", "hptlc", "chromatography", "fingerprint", "marker", "nano"]):
            classification.extraction_clinical = ExtractionClinicalLevel.PURIFIED_CHROMATOGRAPHY
        elif any(w in q for w in ["clinical", "trial", "phase", "tested", "efficacy study", "human study"]):
            classification.extraction_clinical = ExtractionClinicalLevel.CLINICAL_EVALUATION
        elif any(w in q for w in ["hydro-ethanolic", "ethanolic", "solvent", "alcohol extract"]):
            classification.extraction_clinical = ExtractionClinicalLevel.HYDRO_ETHANOLIC
        elif any(w in q for w in ["aqueous", "water", "decoction", "kwath", "asava", "traditional"]):
            classification.extraction_clinical = ExtractionClinicalLevel.TRADITIONAL_AQUEOUS
        elif classification.intended_use in [IntendedUse.DIETARY_WELLNESS, IntendedUse.TOPICAL_BEAUTY]:
            classification.extraction_clinical = ExtractionClinicalLevel.NONE_FOOD_GRADE

        # ----------------------------------------------------
        # 4. Infer ABS Applicant Type
        # ----------------------------------------------------
        if any(w in q for w in ["foreign", "nri", "international", "usa", "uk", "overseas"]):
            abs_check.applicant_type = ApplicantType.FOREIGN_ENTITY
            abs_check.filing_ipr_outside_india = True
        elif any(w in q for w in ["vaidya", "hakim", "practitioner", "doctor"]):
            abs_check.applicant_type = ApplicantType.AYUSH_PRACTITIONER
            abs_check.is_commercial_utilization = False
        elif any(w in q for w in ["cultivator", "grower", "community", "farmer", "local"]):
            abs_check.applicant_type = ApplicantType.CULTIVATOR_COMMUNITY
            abs_check.is_commercial_utilization = False
        else:
            abs_check.applicant_type = ApplicantType.INDIAN_COMMERCIAL
            abs_check.is_commercial_utilization = True

        return classification, abs_check

query_parser = QueryParser()
