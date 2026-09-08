# IP-SAKTI Sahayak (Smart India Hackathon 2026)

**Problem Statement ID:** 26045  
**Problem Statement Title:** IP-SAKTI Sahayak — a multilingual, RAG-based (source-cited) AI assistant for Intellectual Property and regulatory guidance in Ayurveda, across national and international regimes.  
**Theme:** MedTech / BioTech / HealthTech  
**Ministry / Department:** Ministry of Ayush • All India Institute of Ayurveda (AIIA)  
**Team:** Coders of GNIT  
**Core Motto:** *“AI Assists. Rules Decide. Evidence Proves — Or Defers to a Human.”*

---

## 🧭 System Overview

IP-SAKTI Sahayak solves the dual challenge facing Indian Ayurvedic innovation: legitimate innovation is under-protected and under-commercialized, while India's traditional knowledge remains exposed to biopiracy abroad.

Unlike opaque black-box LLM chatbots that hallucinate legal advice, IP-SAKTI Sahayak operates on a **zero-hallucination deterministic state machine** where the LLM is scoped strictly for phrasing and parsing, while statutory rules decide the category, retrieval algorithms ground every citation in primary law, and mathematical evidence scoring gates all answers or escalates them to a human facilitator.

```
USER Formulation Description (English / Hindi · Bhashini-ready)
             │
   ┌─────────┴─────────┐
   ▼                   ▼
CLASSIFICATION ENGINE   ABS / TK GATE
(Deterministic Tree)    (3-Tier Applicant Logic)
   │                   │
   └─────────┬─────────┘
             ▼
EVIDENCE RETRIEVAL (Curated 25+ Primary Statutory Corpus)
             ▼
EVIDENCE STRENGTH ENGINE (100-Point Retrieval Formula)
Agreement 35 · Authority 20 · Currency 20 · Jurisdiction 15 · Classification 10
Hard Gates: Stale Source · Contradiction · Borderline Classification
             │
     ┌───────┴────────────────────────┐
     ▼                                ▼
HIGH CONFIDENCE (≥ 75)        MODERATE / LOW (< 75)
Source-Cited Answer           Safe Abstention
Dual-Jurisdiction Views       Facilitator Review Brief
Mandatory Legal Disclaimer    Human Escalation Gateway
```

---

## 💡 Key Architectural Innovations

1. **Deterministic 6-Category Classification (Max 4 Questions):**
   - Classical / Generic Ayurvedic Medicine (D&C Act §3(a))
   - Patent or Proprietary Ayurvedic Medicine (D&C Act §3(h))
   - New Drug / Non-Classical Ayurvedic Drug (NDCT Rules 2019 Rule 2(w))
   - Phytopharmaceutical Drug (NDCT Rules 2019 Rule 2(aa))
   - Ayurveda-Aahar / Nutraceutical (FSSAI Regulations 2022)
   - Ayurvedic Cosmetic (D&C Act §3(aaa) & Cosmetics Rules 2020)
2. **Novel Edge-Case Handling (from Slide 2 & 6):**
   - **Novelty 1:** New claim on a classical formula is routed to *New Drug*, not buried under a Section 3(p)-barred leaf!
   - **Novelty 2:** “Not classical” is still checked against First-Schedule ingredients — never assumed.
   - **Section 3(h) Exclusion Clause:** Prevents identical classical formulations from masquerading as P&P drugs.
3. **Independent 3-Tier ABS Gate (Biological Diversity Act 2002/2023):**
   - **Track 1:** Foreign Entity / NRI / Foreign Participation (Mandatory Sec 3 & Sec 6 NBA Approval before foreign filing/access).
   - **Track 2:** Indian Commercial Entity (Section 7 SBB Intimation + Sec 6 NBA approval before patent grant).
   - **Track 3 (Exempted):** Registered AYUSH Practitioners (Vaidyas/Hakims) & Local Cultivators explicitly exempted under the 2023 Amendment.
4. **Honest TKDL Search Bridge:**
   - Respects legal reality: CSIR-TKDL full database is restricted under NDA to patent examiners. Instead of claiming false live API access, it constructs structured boolean prior-art queries, binomial translations (e.g. *Withania somnifera*), TKRC codes (`AK02-B/112`), and IPC subclasses (`A61K 36/81`) for InPASS and Patentscope.
5. **Dual Jurisdiction Segregation (Never Blended):**
   - India National Regime (Patents Act 1970, 2024 Rules, D&C Act, BD Act 2023).
   - International Regime (WIPO GRATK Treaty 2024 status — adopted but not yet in force; Nagoya Protocol; PCT; Budapest Treaty; Madrid System; and explicit alert that India is **not** a member of the Hague Agreement).
6. **100-Point Evidence Strength Engine & Safe Abstention:**
   - Objective point allocation (Agreement 35, Authority 20, Currency 20, Jurisdiction 15, Classification 10).
   - Hard gates cap score to < 50 on stale sources or borderline claims, triggering Safe Abstention and an automated Facilitator Review Brief.
7. **Facilitator Review Brief Generator:**
   - Pre-assembles metadata, classification rationale, ABS posture, open questions, and contacts for human IP cells (Ministry of Ayush / AIIA).
8. **Bilingual Core & Bhashini-Ready:**
   - Full English and Hindi (हिन्दी) localized UI and API endpoints.

---

## 🚀 Getting Started

### 1. Installation
```powershell
cd C:\Users\nitin\.gemini\antigravity\scratch\ipsakti-sahayak
pip install -r requirements.txt
```

### 2. Run the Automated Test Suite (37 Tests)
```powershell
python -m pytest tests/ -v
```
All 37 reachability, boundary, scoring, and API integration tests pass with 100% success.

### 3. Start the Web Server
```powershell
python -m uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```
Open your browser at:
`http://127.0.0.1:8000`

---

## 📁 Repository Structure

```
ipsakti-sahayak/
├── app/
│   ├── main.py                     # FastAPI server, endpoints, DPDP headers, static mount
│   ├── models/
│   │   └── schemas.py              # Pydantic schemas, enums, payload models
│   ├── rules/
│   │   ├── classification_engine.py# Deterministic 6-category rule engine
│   │   └── abs_gate.py             # 3-tier ABS applicant compliance gate
│   ├── corpus/
│   │   ├── provisions_data.py      # Curated 25+ verified primary statutory provisions
│   │   └── corpus_manager.py       # Indexed lookup, filters, and reference converter
│   ├── services/
│   │   ├── retrieval.py            # BM25 lexical search with statutory weighting
│   │   ├── evidence_scorer.py      # 100-point evidence engine with hard gates
│   │   ├── tkdl_bridge.py          # TKDL prior-art query builder & TKRC mapper
│   │   ├── review_brief.py         # Facilitator review brief compiler
│   │   └── guidance_service.py     # Dual-jurisdiction orchestrator
│   ├── i18n/
│   │   └── localization.py         # English/Hindi translations & Bhashini adapter
│   └── static/
│       ├── index.html              # Responsive web UI with Ayush/SIH styling
│       ├── styles.css              # Custom styling & print layout for review briefs
│       └── app.js                  # Frontend state machine & API connectors
├── tests/
│   ├── test_classification_and_abs.py # 29 reachability & logic tests from PPT
│   └── test_api_endpoints.py       # 8 FastAPI endpoint integration tests
├── requirements.txt
└── README.md
```
