"""
API Endpoints Integration Test Suite for IP-SAKTI Sahayak
Problem Statement 26045 - SIH 2026
"""

import pytest
from starlette.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_api_health_and_index():
    response = client.get("/")
    assert response.status_code == 200

def test_api_classify_endpoint():
    payload = {
        "intended_use": "Therapeutic / Medicinal Treatment or Cure",
        "formulation_basis": "First-Schedule Authoritative Text Formulation (Identical composition & method)",
        "claim_type": "Classical Ayurvedic Indication (as described in authoritative scriptures)",
        "extraction_clinical": "Traditional Aqueous / Kwath / Asava / Bhasma Method",
        "product_name": "Classical Maha Sudarshan Churna"
    }
    response = client.post("/api/classify", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["category_id"] == "CLASSICAL"
    assert "Section 3(a)" in data["statutory_citation"]

def test_api_abs_check_endpoint():
    payload = {
        "applicant_type": "Registered AYUSH Practitioner / Vaidya / Hakim (Exempted)",
        "is_commercial_utilization": True,
        "filing_ipr_in_india": False,
        "filing_ipr_outside_india": False
    }
    response = client.post("/api/abs-check", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["is_exempted"] is True
    assert "Biological Diversity (Amendment) Act, 2023" in data["exemption_basis"]

def test_api_guidance_endpoint():
    c_req = {
        "intended_use": "Therapeutic / Medicinal Treatment or Cure",
        "formulation_basis": "First-Schedule Ingredients in Modified Ratio or Modern Dosage Form (Tablet/Capsule/Syrup)",
        "claim_type": "Classical Ayurvedic Indication (as described in authoritative scriptures)",
        "extraction_clinical": "Standard Hydro-ethanolic / Solvent Extraction",
        "product_name": "Ashwagandha High Potency Extract"
    }
    payload = {
        "classification": c_req,
        "jurisdiction": "dual"
    }
    response = client.post("/api/guidance", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "national_guidance" in data
    assert "international_guidance" in data
    assert "evidence_score" in data
    assert data["evidence_score"]["total_score"] > 0
    assert len(data["cited_provisions"]) > 0

def test_api_tkdl_query_endpoint():
    payload = {
        "formulation_name": "Ashwagandha and Turmeric Synergy",
        "sanskrit_or_botanical_terms": ["Ashwagandha", "Haridra"],
        "therapeutic_target": "Anti-inflammatory and Joint Mobility"
    }
    response = client.post("/api/tkdl-query", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert len(data["identified_botanicals"]) >= 2
    assert any("Withania somnifera" in b["botanical_name"] for b in data["identified_botanicals"])
    assert any("Curcuma longa" in b["botanical_name"] for b in data["identified_botanicals"])
    assert "Honest Bridge Notice" in data["disclaimer"]

def test_api_corpus_endpoints():
    response = client.get("/api/corpus")
    assert response.status_code == 200
    provisions = response.json()
    assert len(provisions) >= 25

    single_resp = client.get("/api/corpus/DCA_3H")
    assert single_resp.status_code == 200
    assert single_resp.json()["section"] == "Section 3(h)"

def test_api_i18n_endpoint():
    hi_resp = client.get("/api/i18n/hi")
    assert hi_resp.status_code == 200
    assert "आईपी-शक्ति सहायक" in hi_resp.json()["title"]

def test_api_audit_trail_endpoint():
    resp = client.get("/api/audit-trail")
    assert resp.status_code == 200
    data = resp.json()
    assert "DPDP Act 2023" in data["standard"]
    assert "events" in data
