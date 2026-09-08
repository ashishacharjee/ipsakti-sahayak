"""
Comprehensive Automated Test Suite for IP-SAKTI Sahayak
Problem Statement 26045 - SIH 2026
Team: Coders of GNIT

Includes all 29 Reachability & Logic verification tests:
- 6 Reachability tests for all 6 Classification Categories
- 4 Reachability tests for all 4 ABS Applicant Tracks
- Boundary, Novelty, and Exclusion routing tests
- 100-Point Evidence Strength Engine & Hard Gates tests
- TKDL Search Bridge & IPC mapping tests
- Dual Jurisdiction Segregation & Hague/GRATK tests
- Review Brief assembly tests
"""

import pytest
from app.models.schemas import (
    ClassificationRequest,
    RegulatoryCategory,
    IntendedUse,
    FormulationBasis,
    ClaimType,
    ExtractionClinicalLevel,
    ApplicantType,
    ABSCheckRequest,
    TKDLQueryRequest,
    ReviewBriefRequest
)
from app.rules.classification_engine import classification_engine
from app.rules.abs_gate import abs_gate
from app.services.evidence_scorer import evidence_engine
from app.services.tkdl_bridge import tkdl_bridge
from app.services.guidance_service import guidance_service
from app.services.review_brief import review_brief_service
from app.corpus.corpus_manager import corpus_manager

# ====================================================================
# PART 1: 6 CLASSIFICATION LEAF REACHABILITY TESTS
# ====================================================================

def test_reachability_classical_category():
    """Test 1: Classical / Generic Ayurvedic Medicine (D&C Act §3(a))"""
    req = ClassificationRequest(
        product_name="Chyawanprash Awaleha",
        intended_use=IntendedUse.THERAPEUTIC,
        formulation_basis=FormulationBasis.FIRST_SCHEDULE_EXACT,
        claim_type=ClaimType.CLASSICAL_INDICATION,
        extraction_clinical=ExtractionClinicalLevel.TRADITIONAL_AQUEOUS
    )
    res = classification_engine.classify(req)
    assert res.category == RegulatoryCategory.CLASSICAL
    assert res.category_id == "CLASSICAL"
    assert "Section 3(a)" in res.statutory_citation
    assert "Section 3(p)" in res.ip_posture

def test_reachability_patent_proprietary_category():
    """Test 2: Patent or Proprietary Ayurvedic Medicine (D&C Act §3(h))"""
    req = ClassificationRequest(
        product_name="Modified Ashwagandha & Shatavari Capsule",
        intended_use=IntendedUse.THERAPEUTIC,
        formulation_basis=FormulationBasis.FIRST_SCHEDULE_MODIFIED,
        claim_type=ClaimType.CLASSICAL_INDICATION,
        extraction_clinical=ExtractionClinicalLevel.HYDRO_ETHANOLIC
    )
    res = classification_engine.classify(req)
    assert res.category == RegulatoryCategory.PATENT_PROPRIETARY
    assert res.category_id == "PATENT_PROPRIETARY"
    assert "Section 3(h)" in res.statutory_citation
    assert "Rule 158-B" in res.statutory_citation

def test_reachability_new_drug_category():
    """Test 3: New Drug / Non-Classical Ayurvedic Drug (NDCT Rules 2019 Rule 2(w))"""
    req = ClassificationRequest(
        product_name="Ayur-Glycemia for Type-2 Diabetes Mellitus",
        intended_use=IntendedUse.THERAPEUTIC,
        formulation_basis=FormulationBasis.FIRST_SCHEDULE_MODIFIED,
        claim_type=ClaimType.NEW_THERAPEUTIC_CLAIM,
        extraction_clinical=ExtractionClinicalLevel.CLINICAL_EVALUATION
    )
    res = classification_engine.classify(req)
    assert res.category == RegulatoryCategory.NEW_DRUG
    assert res.category_id == "NEW_DRUG"
    assert "Rule 2(w)" in res.statutory_citation

def test_reachability_phytopharmaceutical_category():
    """Test 4: Phytopharmaceutical Drug (NDCT Rules 2019 Rule 2(aa))"""
    req = ClassificationRequest(
        product_name="Standardized Boswellic Acids Fraction",
        intended_use=IntendedUse.THERAPEUTIC,
        formulation_basis=FormulationBasis.PURIFIED_FRACTION,
        claim_type=ClaimType.CLASSICAL_INDICATION,
        extraction_clinical=ExtractionClinicalLevel.PURIFIED_CHROMATOGRAPHY
    )
    res = classification_engine.classify(req)
    assert res.category == RegulatoryCategory.PHYTOPHARMACEUTICAL
    assert res.category_id == "PHYTOPHARMACEUTICAL"
    assert "Rule 2(aa)" in res.statutory_citation
    assert "minimum four bioactive" in res.description

def test_reachability_ayurveda_aahar_nutraceutical():
    """Test 5: Ayurveda-Aahar / Nutraceutical (FSSAI Regulations 2022)"""
    req = ClassificationRequest(
        product_name="Ayurvedic Daily Digestive Granules",
        intended_use=IntendedUse.DIETARY_WELLNESS,
        formulation_basis=FormulationBasis.FIRST_SCHEDULE_EXACT,
        claim_type=ClaimType.GENERAL_WELLNESS,
        extraction_clinical=ExtractionClinicalLevel.NONE_FOOD_GRADE
    )
    res = classification_engine.classify(req)
    assert res.category == RegulatoryCategory.NUTRACEUTICAL
    assert res.category_id == "NUTRACEUTICAL"
    assert "Ayurveda Aahar" in res.governing_statute

def test_reachability_cosmetic_category():
    """Test 6: Ayurvedic Cosmetic (D&C Act §3(aaa) & Cosmetics Rules 2020)"""
    req = ClassificationRequest(
        product_name="Kumkumadi Tailam Glow Facial Oil",
        intended_use=IntendedUse.TOPICAL_BEAUTY,
        formulation_basis=FormulationBasis.FIRST_SCHEDULE_MODIFIED,
        claim_type=ClaimType.COSMETIC_APPEARANCE,
        extraction_clinical=ExtractionClinicalLevel.NONE_FOOD_GRADE
    )
    res = classification_engine.classify(req)
    assert res.category == RegulatoryCategory.COSMETIC
    assert res.category_id == "COSMETIC"
    assert "Section 3(aaa)" in res.statutory_citation

# ====================================================================
# PART 2: 4 ABS APPLICANT TRACK REACHABILITY TESTS
# ====================================================================

def test_reachability_abs_foreign_entity():
    """Test 7: Foreign Entity Track (Strict Section 3 & Section 6 NBA Approval)"""
    req = ABSCheckRequest(
        applicant_type=ApplicantType.FOREIGN_ENTITY,
        is_commercial_utilization=True,
        filing_ipr_outside_india=True,
        filing_ipr_in_india=False
    )
    res = abs_gate.evaluate(req)
    assert res.requires_nba_approval is True
    assert res.is_exempted is False
    assert "Form I" in res.mandated_forms[0]
    assert "Form III" in res.mandated_forms[1]
    assert "BEFORE FILING" in res.guidance_notes

def test_reachability_abs_indian_commercial_entity():
    """Test 8: Indian Commercial Entity Track (Section 7 SBB Intimation & Sec 6 NBA)"""
    req = ABSCheckRequest(
        applicant_type=ApplicantType.INDIAN_COMMERCIAL,
        is_commercial_utilization=True,
        filing_ipr_in_india=True,
        filing_ipr_outside_india=False
    )
    res = abs_gate.evaluate(req)
    assert res.requires_sbb_intimation is True
    assert res.requires_nba_approval is True
    assert res.is_exempted is False
    assert "Section 7" in res.statutory_provisions[0]

def test_reachability_abs_ayush_practitioner_exemption():
    """Test 9: Registered AYUSH Practitioner Exemption Track (2023 Amendment)"""
    req = ABSCheckRequest(
        applicant_type=ApplicantType.AYUSH_PRACTITIONER,
        is_commercial_utilization=True,
        filing_ipr_in_india=False,
        filing_ipr_outside_india=False
    )
    res = abs_gate.evaluate(req)
    assert res.is_exempted is True
    assert res.requires_sbb_intimation is False
    assert "Biological Diversity (Amendment) Act, 2023" in res.exemption_basis

def test_reachability_abs_cultivator_grower_exemption():
    """Test 10: Local Cultivator & Grower Exemption Track (2023 Amendment)"""
    req = ABSCheckRequest(
        applicant_type=ApplicantType.CULTIVATOR_COMMUNITY,
        is_commercial_utilization=True,
        filing_ipr_in_india=False,
        filing_ipr_outside_india=False
    )
    res = abs_gate.evaluate(req)
    assert res.is_exempted is True
    assert res.requires_sbb_intimation is False
    assert "growers and cultivators" in res.exemption_basis

# ====================================================================
# PART 3: NOVELTY & BOUNDARY ROUTING TESTS (FROM PPT SLIDES 2 & 6)
# ====================================================================

def test_novelty_new_claim_on_classical_formula_routes_to_new_drug():
    """
    Test 11: Novelty 1 from Slide 2:
    'New claim on a classical formula -> routed to New Drug, not buried under a 3(p)-barred leaf'
    """
    req = ClassificationRequest(
        product_name="Classical Pippali Churna for Neuro-protection",
        intended_use=IntendedUse.THERAPEUTIC,
        formulation_basis=FormulationBasis.FIRST_SCHEDULE_EXACT,
        claim_type=ClaimType.NEW_THERAPEUTIC_CLAIM,  # New claim!
        extraction_clinical=ExtractionClinicalLevel.CLINICAL_EVALUATION
    )
    res = classification_engine.classify(req)
    assert res.category == RegulatoryCategory.NEW_DRUG
    assert "Rule 2(w)" in res.statutory_citation
    assert "Not buried under 3(p)" in "".join(res.rule_path_traversed)

def test_boundary_cosmetic_with_disease_cure_claim_redirects_to_drug():
    """
    Test 12: Topical product making disease claim cannot remain cosmetic under §3(aaa).
    """
    req = ClassificationRequest(
        product_name="Topical Eczema Cure Cream",
        intended_use=IntendedUse.TOPICAL_BEAUTY,
        formulation_basis=FormulationBasis.FIRST_SCHEDULE_MODIFIED,
        claim_type=ClaimType.NEW_THERAPEUTIC_CLAIM,  # Therapeutic disease claim!
        extraction_clinical=ExtractionClinicalLevel.HYDRO_ETHANOLIC
    )
    res = classification_engine.classify(req)
    assert res.category != RegulatoryCategory.COSMETIC
    assert res.category == RegulatoryCategory.NEW_DRUG

def test_boundary_food_supplement_with_disease_claim_redirects_to_drug():
    """
    Test 13: Dietary product claiming diabetes cure cannot remain Ayurveda-Aahar.
    """
    req = ClassificationRequest(
        product_name="Herbal Tea for Diabetes Cure",
        intended_use=IntendedUse.DIETARY_WELLNESS,
        formulation_basis=FormulationBasis.FIRST_SCHEDULE_MODIFIED,
        claim_type=ClaimType.NEW_THERAPEUTIC_CLAIM,
        extraction_clinical=ExtractionClinicalLevel.HYDRO_ETHANOLIC
    )
    res = classification_engine.classify(req)
    assert res.category != RegulatoryCategory.NUTRACEUTICAL
    assert res.category == RegulatoryCategory.NEW_DRUG

def test_novelty_section_3h_exclusion_clause():
    """
    Test 14: Slide 6 bug fix: Identical classical formulation cannot be licensed as P&P.
    """
    req = ClassificationRequest(
        product_name="Triphala Churna classical exact",
        intended_use=IntendedUse.THERAPEUTIC,
        formulation_basis=FormulationBasis.FIRST_SCHEDULE_EXACT,
        claim_type=ClaimType.CLASSICAL_INDICATION,
        extraction_clinical=ExtractionClinicalLevel.TRADITIONAL_AQUEOUS
    )
    res = classification_engine.classify(req)
    assert res.category == RegulatoryCategory.CLASSICAL
    assert res.category != RegulatoryCategory.PATENT_PROPRIETARY

def test_phytopharmaceutical_requires_marker_compounds():
    """
    Test 15: Phytopharmaceutical definition requires minimum four markers.
    """
    req = ClassificationRequest(
        product_name="Withania Somnifera Fraction",
        intended_use=IntendedUse.THERAPEUTIC,
        formulation_basis=FormulationBasis.PURIFIED_FRACTION,
        claim_type=ClaimType.CLASSICAL_INDICATION,
        extraction_clinical=ExtractionClinicalLevel.PURIFIED_CHROMATOGRAPHY
    )
    res = classification_engine.classify(req)
    assert res.category == RegulatoryCategory.PHYTOPHARMACEUTICAL
    assert "Rule 2(aa)" in res.statutory_citation

# ====================================================================
# PART 4: 100-POINT EVIDENCE STRENGTH ENGINE & HARD GATES
# ====================================================================

def test_evidence_strength_high_confidence():
    """Test 16: High Evidence Strength (>= 75/100) with multiple concordant sources"""
    provisions = corpus_manager.get_by_category("Classical / Generic Ayurvedic Medicine")
    score = evidence_engine.calculate_score(
        retrieved_provisions=provisions,
        category_id="CLASSICAL",
        jurisdiction_requested="India"
    )
    assert score.total_score >= 75.0
    assert score.confidence_level.value.startswith("HIGH")
    assert score.hard_gate_triggered is False

def test_evidence_strength_hard_gate_stale_source():
    """Test 17: Hard Gate: Stale or superseded source caps score to < 50"""
    provisions = corpus_manager.get_all_provisions()[:4]
    score = evidence_engine.calculate_score(
        retrieved_provisions=provisions,
        category_id="CLASSICAL",
        jurisdiction_requested="India",
        has_stale_source=True
    )
    assert score.hard_gate_triggered is True
    assert score.total_score <= 48.0
    assert score.confidence_level.value.startswith("LOW")
    assert "Stale or superseded" in score.hard_gate_reason

def test_evidence_strength_hard_gate_contradiction():
    """Test 18: Hard Gate: Contradiction in claims caps score to < 50"""
    provisions = corpus_manager.get_all_provisions()[:4]
    score = evidence_engine.calculate_score(
        retrieved_provisions=provisions,
        category_id="PATENT_PROPRIETARY",
        jurisdiction_requested="India",
        has_contradiction=True
    )
    assert score.hard_gate_triggered is True
    assert score.total_score <= 48.0
    assert "contradiction" in score.hard_gate_reason.lower()

def test_evidence_strength_hard_gate_borderline():
    """Test 19: Hard Gate: Borderline classification triggers safe abstention"""
    provisions = corpus_manager.get_all_provisions()[:3]
    score = evidence_engine.calculate_score(
        retrieved_provisions=provisions,
        category_id="PATENT_PROPRIETARY",
        jurisdiction_requested="India",
        is_borderline=True
    )
    assert score.hard_gate_triggered is True
    assert score.total_score <= 48.0

def test_evidence_strength_authority_weighting():
    """Test 20: Statute (20 pts) weights higher than lower instruments"""
    statute_prov = [corpus_manager.get_by_id("DCA_3A")]
    guideline_prov = [corpus_manager.get_by_id("US_FDA_BOTANICAL")]
    
    score_statute = evidence_engine.calculate_score(statute_prov, "CLASSICAL", "India")
    score_guide = evidence_engine.calculate_score(guideline_prov, "NEW_DRUG", "International")
    
    assert score_statute.source_authority == 20.0
    assert score_guide.source_authority == 14.0

def test_evidence_strength_currency_boost():
    """Test 21: Sources reflecting 2023/2024 legislative updates receive full currency score"""
    provisions = [
        corpus_manager.get_by_id("BDA_2023_EXEMPTIONS"),
        corpus_manager.get_by_id("PAT_RULES_2024")
    ]
    score = evidence_engine.calculate_score(provisions, "CLASSICAL", "India")
    assert score.currency_score == 20.0

# ====================================================================
# PART 5: TKDL SEARCH BRIDGE & QUERY BUILDER
# ====================================================================

def test_tkdl_ashwagandha_query_mapping():
    """Test 22: Ashwagandha maps to Withania somnifera and TKRC AK02-B/112"""
    req = TKDLQueryRequest(
        formulation_name="Ashwagandha Churna",
        sanskrit_or_botanical_terms=["Ashwagandha"],
        therapeutic_target="Adaptogen"
    )
    res = tkdl_bridge.build_query(req)
    assert any("Withania somnifera" in b["botanical_name"] for b in res.identified_botanicals)
    assert any("AK02-B/112" in c for c in res.tkrc_codes)
    assert any("A61K 36/81" in ipc for ipc in res.ipc_classes)
    assert "Withania somnifera" in res.structured_search_query

def test_tkdl_haridra_query_mapping():
    """Test 23: Turmeric / Haridra maps to Curcuma longa and TKRC AK02-B/245"""
    req = TKDLQueryRequest(
        formulation_name="Haridra Khanda",
        sanskrit_or_botanical_terms=["Haridra", "Turmeric"],
        therapeutic_target="Anti-inflammatory"
    )
    res = tkdl_bridge.build_query(req)
    assert any("Curcuma longa" in b["botanical_name"] for b in res.identified_botanicals)
    assert any("AK02-B/245" in c for c in res.tkrc_codes)
    assert any("A61P 29/00" in ipc for ipc in res.ipc_classes)

def test_tkdl_honest_bridge_disclaimer():
    """Test 24: TKDL Bridge contains honest NDA disclaimer (Slide 4 mitigation)"""
    req = TKDLQueryRequest(formulation_name="Triphala")
    res = tkdl_bridge.build_query(req)
    assert "Honest Bridge Notice" in res.disclaimer
    assert "non-disclosure agreements" in res.disclaimer

# ====================================================================
# PART 6: DUAL JURISDICTION SEGREGATION & TREATY ACCURACY
# ====================================================================

def test_dual_jurisdiction_answers_never_blended():
    """Test 25: National and International layers computed concurrently, presented separately"""
    c_req = ClassificationRequest(
        product_name="Ashwagandha Extract",
        intended_use=IntendedUse.THERAPEUTIC,
        formulation_basis=FormulationBasis.FIRST_SCHEDULE_MODIFIED,
        claim_type=ClaimType.CLASSICAL_INDICATION,
        extraction_clinical=ExtractionClinicalLevel.HYDRO_ETHANOLIC
    )
    abs_req = ABSCheckRequest(applicant_type=ApplicantType.INDIAN_COMMERCIAL)
    guidance = guidance_service.process_guidance(c_req, abs_req, jurisdiction_mode="dual")
    
    assert guidance.national_guidance["jurisdiction"] == "India (National)"
    assert "International" in guidance.international_guidance["jurisdiction"]
    assert "Section 3(p)" in guidance.national_guidance["statutory_bars_evaluated"][0]
    assert "wipo_gratk_treaty_status" in guidance.international_guidance

def test_hague_agreement_india_non_membership_alert():
    """Test 26: Slide 6 correction: Highlights that India is NOT a member of Hague Agreement"""
    c_req = ClassificationRequest(
        product_name="Ayurvedic Cosmetic Bottle",
        intended_use=IntendedUse.TOPICAL_BEAUTY,
        formulation_basis=FormulationBasis.FIRST_SCHEDULE_MODIFIED,
        claim_type=ClaimType.COSMETIC_APPEARANCE,
        extraction_clinical=ExtractionClinicalLevel.NONE_FOOD_GRADE
    )
    abs_req = ABSCheckRequest(applicant_type=ApplicantType.INDIAN_COMMERCIAL)
    guidance = guidance_service.process_guidance(c_req, abs_req)
    intl_tm_design = guidance.international_guidance["trademark_and_design"]
    assert "India is NOT a member of the Hague Agreement" in intl_tm_design["hague_agreement_alert"]

def test_wipo_gratk_treaty_ratification_status():
    """Test 27: Slide 6 correction: Confirms WIPO GRATK is adopted but NOT yet in force"""
    gratk_entry = corpus_manager.get_by_id("WIPO_GRATK_2024")
    assert gratk_entry["is_active"] is False
    assert "Awaiting 15 ratifications" in gratk_entry["content"] or "enters into force 3 months after 15" in gratk_entry["content"]

# ====================================================================
# PART 7: FACILITATOR REVIEW BRIEF & ESCALATION
# ====================================================================

def test_facilitator_review_brief_assembly():
    """Test 28: Review brief pre-assembles classification, ABS, and open questions"""
    c_req = ClassificationRequest(
        product_name="Novel Bio-enhanced Ashwagandha",
        intended_use=IntendedUse.THERAPEUTIC,
        formulation_basis=FormulationBasis.FIRST_SCHEDULE_MODIFIED,
        claim_type=ClaimType.CLASSICAL_INDICATION,
        extraction_clinical=ExtractionClinicalLevel.HYDRO_ETHANOLIC
    )
    abs_req = ABSCheckRequest(applicant_type=ApplicantType.INDIAN_COMMERCIAL)
    c_res = classification_engine.classify(c_req)
    abs_res = abs_gate.evaluate(abs_req)
    score = evidence_engine.calculate_score(
        corpus_manager.get_all_provisions()[:3],
        c_res.category_id,
        "India"
    )
    
    brief_req = ReviewBriefRequest(
        classification=c_res,
        abs_result=abs_res,
        evidence_score=score,
        formulation_name="Novel Bio-enhanced Ashwagandha"
    )
    
    brief = review_brief_service.generate_brief(brief_req, cited_authorities=[])
    assert brief.brief_id.startswith("SAKTI-BRIEF-")
    assert len(brief.open_questions_for_human) >= 1
    assert "Ayush IP & Regulatory Facilitation Cell" in brief.escalation_contact_info["facilitation_cell"]

# ====================================================================
# PART 8: REAL WALKTHROUGH FROM SLIDE 5
# ====================================================================

def test_real_walkthrough_slide_5_scenario():
    """
    Test 29: Real Walkthrough Scenario from Slide 5:
    '1. Scenario: Modified-extraction Ashwagandha, classical base — patentable?'
    '2. Classification: First-Schedule only, not identical -> Patent/Proprietary (§3(h))'
    '3. Evidence: 2 independent sources agree -> HIGH'
    '4. Outcome: Patentability assessment + TKDL search, terminology trap flagged'
    """
    c_req = ClassificationRequest(
        product_name="Modified-extraction Ashwagandha Formulation",
        intended_use=IntendedUse.THERAPEUTIC,
        formulation_basis=FormulationBasis.FIRST_SCHEDULE_MODIFIED,
        claim_type=ClaimType.CLASSICAL_INDICATION,
        extraction_clinical=ExtractionClinicalLevel.HYDRO_ETHANOLIC,
        ingredients=["Ashwagandha root"]
    )
    abs_req = ABSCheckRequest(applicant_type=ApplicantType.INDIAN_COMMERCIAL)
    guidance = guidance_service.process_guidance(c_req, abs_req, jurisdiction_mode="dual")
    
    # 1. Classification check
    assert guidance.national_guidance["classification_category"] == RegulatoryCategory.PATENT_PROPRIETARY.value
    assert "Section 3(h)" in guidance.national_guidance["statutory_citation"]
    
    # 2. Evidence Strength check
    assert guidance.evidence_score.total_score >= 75.0
    assert guidance.evidence_score.confidence_level == "HIGH (>= 75/100)"
    
    # 3. Patentability assessment
    assert "Conditional Patentability" in guidance.national_guidance["ip_patentability_assessment"]
    assert any("Section 3(p)" in bar for bar in guidance.national_guidance["statutory_bars_evaluated"])
    
    # 4. Mandatory disclaimer is always present
    assert "DISCLAIMER: IP-SAKTI Sahayak provides statutory and regulatory informational guidance" in guidance.mandatory_disclaimer
