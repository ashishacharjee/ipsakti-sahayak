"""
IP-SAKTI Sahayak - FastAPI Application
Problem Statement 26045 - Smart India Hackathon 2026
Team: Coders of GNIT
Theme: MedTech / BioTech / HealthTech
Ministry of Ayush / All India Institute of Ayurveda
"""

import time
import uuid
from typing import List, Optional, Dict, Any
from fastapi import FastAPI, Query, HTTPException, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
import os

from app.models.schemas import (
    ClassificationRequest,
    ClassificationResult,
    ABSCheckRequest,
    ABSCheckResult,
    DualJurisdictionGuidance,
    FullGuidanceRequest,
    ApplicantType,
    TKDLQueryRequest,
    TKDLQueryResponse,
    ReviewBriefRequest,
    ReviewBriefResponse,
    LegalSourceReference
)
from app.rules.classification_engine import classification_engine
from app.rules.abs_gate import abs_gate
from app.services.guidance_service import guidance_service
from app.services.tkdl_bridge import tkdl_bridge
from app.services.review_brief import review_brief_service
from app.corpus.corpus_manager import corpus_manager
from app.i18n.localization import localization_service

app = FastAPI(
    title="IP-SAKTI Sahayak API",
    description="Multilingual, RAG-grounded deterministic AI assistant for Ayurveda IPR and regulatory guidance.",
    version="1.0.0"
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Audit log storage (DPDP Act 2023 compliant: ephemeral / anonymized metadata)
AUDIT_LOGS: List[Dict[str, Any]] = []

@app.middleware("http")
async def add_security_and_audit_headers(request: Request, call_next):
    start_time = time.time()
    response: Response = await call_next(request)
    duration = time.time() - start_time
    
    # DPDP and Security Headers
    response.headers["X-Privacy-Standard"] = "DPDP-Act-2023-Aligned"
    response.headers["X-Audit-Trace"] = str(uuid.uuid4().hex[:8])
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "SAMEORIGIN"
    
    # Record non-static audit event
    if request.url.path.startswith("/api/"):
        AUDIT_LOGS.append({
            "trace_id": response.headers["X-Audit-Trace"],
            "path": request.url.path,
            "method": request.method,
            "status_code": response.status_code,
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "duration_ms": round(duration * 1000, 2)
        })
        if len(AUDIT_LOGS) > 200:
            AUDIT_LOGS.pop(0)

    return response

# Serve Frontend Root
STATIC_DIR = os.path.join(os.path.dirname(__file__), "static")

@app.get("/")
async def read_index():
    index_file = os.path.join(STATIC_DIR, "index.html")
    if os.path.exists(index_file):
        return FileResponse(index_file)
    return {"message": "IP-SAKTI Sahayak API is running. Static frontend not yet compiled."}

# Endpoints

@app.post("/api/classify", response_model=ClassificationResult)
async def classify_product(req: ClassificationRequest):
    """
    Deterministic rule engine sorting product into 1 of 6 legal categories in max 4 steps.
    Zero hallucination — LLM never rules.
    """
    return classification_engine.classify(req)

@app.post("/api/abs-check", response_model=ABSCheckResult)
async def check_abs(req: ABSCheckRequest):
    """
    Independent parallel ABS check under Biological Diversity Act 2002/2023.
    Evaluates 3-tier applicant logic (Foreign, Indian Commercial, AYUSH Practitioner, Cultivator).
    """
    return abs_gate.evaluate(req)

@app.post("/api/guidance", response_model=DualJurisdictionGuidance)
async def generate_guidance(payload: FullGuidanceRequest):
    """
    End-to-end assessment:
    Runs classification, ABS gate, dual-jurisdiction retrieval, 100-pt evidence scoring,
    and safe abstention evaluation.
    """
    abs_req = payload.abs_check or ABSCheckRequest(
        applicant_type=ApplicantType.INDIAN_COMMERCIAL
    )
    return guidance_service.process_guidance(
        classification_req=payload.classification,
        abs_req=abs_req,
        free_text_query=payload.query,
        jurisdiction_mode=payload.jurisdiction
    )

@app.post("/api/tkdl-query", response_model=TKDLQueryResponse)
async def generate_tkdl_query(req: TKDLQueryRequest):
    """
    TKDL Search Bridge: Transforms formulation into structured TKRC codes,
    IPC classes, and boolean prior-art search queries.
    """
    return tkdl_bridge.build_query(req)

@app.post("/api/review-brief", response_model=ReviewBriefResponse)
async def create_review_brief(req: ReviewBriefRequest):
    """
    Generates structured, facilitator-ready brief for human IP examiners and AYUSH reviewers.
    """
    # Retrieve cited provisions
    provisions = corpus_manager.get_all_provisions()[:5]
    refs = [corpus_manager.to_source_reference(p) for p in provisions]
    return review_brief_service.generate_brief(req, cited_authorities=refs)

@app.get("/api/corpus")
async def get_corpus(
    jurisdiction: Optional[str] = None,
    category: Optional[str] = None
):
    """
    Browseable curated statutory corpus with 25+ verified legal provisions.
    """
    if jurisdiction:
        return corpus_manager.get_by_jurisdiction(jurisdiction)
    if category:
        return corpus_manager.get_by_category(category)
    return corpus_manager.get_all_provisions()

@app.get("/api/corpus/{provision_id}")
async def get_provision(provision_id: str):
    p = corpus_manager.get_by_id(provision_id)
    if not p:
        raise HTTPException(status_code=404, detail=f"Provision '{provision_id}' not found.")
    return p

@app.get("/api/i18n/{lang}")
async def get_i18n_strings(lang: str = "en"):
    """
    Bilingual UI labels and prompts (en / hi).
    """
    return localization_service.get_all(lang)

@app.get("/api/audit-trail")
async def get_audit_trail():
    """
    Returns anonymous DPDP-compliant execution log trail.
    """
    return {
        "standard": "DPDP Act 2023 - Ephemeral Traceability",
        "total_events": len(AUDIT_LOGS),
        "events": AUDIT_LOGS[-50:]
    }

# Mount static directory for CSS/JS
if os.path.exists(STATIC_DIR):
    app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
