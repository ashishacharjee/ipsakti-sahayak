"""
Evidence Strength Engine for IP-SAKTI Sahayak
Problem Statement 26045 - SIH 2026

Calculates a 100-point retrieval-grounded evidence score based on:
1. Source Agreement (Max 35 pts)
2. Authority (Max 20 pts)
3. Currency (Max 20 pts)
4. Jurisdiction (Max 15 pts)
5. Classification (Max 10 pts)

Includes hard gates for stale sources, legal contradictions, and borderline classifications.
"""

from typing import List, Dict, Any, Optional
from app.models.schemas import EvidenceScoreBreakdown, ConfidenceLevel

class EvidenceStrengthEngine:
    """
    Computes objective mathematical evidence strength.
    Never an LLM self-reported hallucinated confidence score.
    """

    def calculate_score(
        self,
        retrieved_provisions: List[Dict[str, Any]],
        category_id: str,
        jurisdiction_requested: str,
        has_contradiction: bool = False,
        has_stale_source: bool = False,
        is_borderline: bool = False
    ) -> EvidenceScoreBreakdown:
        
        num_sources = len(retrieved_provisions)

        # 1. Source Agreement (Max 35 points)
        if num_sources >= 4:
            agreement_score = 35.0
        elif num_sources == 3:
            agreement_score = 30.0
        elif num_sources == 2:
            agreement_score = 25.0
        elif num_sources == 1:
            agreement_score = 15.0
        else:
            agreement_score = 0.0

        # 2. Statutory Authority (Max 20 points)
        max_authority = 0
        for p in retrieved_provisions:
            weight = p.get("authority_weight", 12)
            if weight > max_authority:
                max_authority = weight
        authority_score = float(min(max_authority, 20)) if num_sources > 0 else 0.0

        # 3. Currency (Max 20 points)
        active_count = sum(1 for p in retrieved_provisions if p.get("is_active", True))
        recent_count = sum(1 for p in retrieved_provisions if "2023" in str(p.get("year", "")) or "2024" in str(p.get("year", "")))
        
        if num_sources > 0:
            if (active_count / num_sources) >= 0.8:
                if recent_count >= 1:
                    currency_score = 20.0
                else:
                    currency_score = 15.0
            else:
                currency_score = 10.0
        else:
            currency_score = 0.0

        # 4. Jurisdiction Match (Max 15 points)
        if num_sources == 0:
            jurisdiction_score = 0.0
        else:
            jur_norm = jurisdiction_requested.strip().lower() if jurisdiction_requested else ""
            has_in = any(str(p.get("jurisdiction", "")).lower() in ["india", "national"] for p in retrieved_provisions)
            has_intl = any(str(p.get("jurisdiction", "")).lower() in ["international", "wipo", "foreign"] for p in retrieved_provisions)
            
            if jur_norm in ["both", "dual"]:
                jurisdiction_score = 15.0 if (has_in and has_intl) else (10.0 if (has_in or has_intl) else 0.0)
            elif jur_norm in ["india", "national"]:
                jurisdiction_score = 15.0 if has_in else (5.0 if has_intl else 0.0)
            else:
                jurisdiction_score = 15.0 if has_intl else (5.0 if has_in else 0.0)

        # 5. Classification Certainty (Max 10 points)
        valid_categories = ["CLASSICAL", "PATENT_PROPRIETARY", "NEW_DRUG", "PHYTOPHARMACEUTICAL", "NUTRACEUTICAL", "COSMETIC"]
        if category_id and str(category_id).upper() in valid_categories:
            classification_certainty = 10.0
        elif category_id and str(category_id).upper() != "UNKNOWN":
            classification_certainty = 5.0
        else:
            classification_certainty = 0.0

        # Check Hard Gates
        hard_gate_triggered = False
        hard_gate_reason = None

        if num_sources == 0:
            hard_gate_triggered = True
            hard_gate_reason = "Hard Gate Triggered: No statutory provisions or precedents found."
        elif has_stale_source:
            hard_gate_triggered = True
            hard_gate_reason = "Hard Gate Triggered: Stale or superseded statutory provision detected."
        elif has_contradiction:
            hard_gate_triggered = True
            hard_gate_reason = "Hard Gate Triggered: Statutory contradiction or conflicting therapeutic claims detected."
        elif is_borderline:
            hard_gate_triggered = True
            hard_gate_reason = "Hard Gate Triggered: Borderline classification requiring empirical clinical verification."
        
        # Penalize score for missing categories even if no hard gate
        total_score = agreement_score + authority_score + currency_score + jurisdiction_score + classification_certainty
        
        # Apply Hard Gate Cap
        if hard_gate_triggered:
            total_score = min(total_score, 48.0)

        # Ensure bounds [0, 100]
        total_score = round(max(0.0, min(100.0, total_score)), 1)

        # Confidence categorization
        if total_score >= 80.0 and not hard_gate_triggered:
            confidence_level = ConfidenceLevel.HIGH
        elif total_score >= 55.0 and not hard_gate_triggered:
            confidence_level = ConfidenceLevel.MODERATE
        else:
            confidence_level = ConfidenceLevel.LOW

        return EvidenceScoreBreakdown(
            source_agreement=agreement_score,
            source_authority=authority_score,
            currency_score=currency_score,
            jurisdiction_match=jurisdiction_score,
            classification_certainty=classification_certainty,
            total_score=total_score,
            confidence_level=confidence_level,
            hard_gate_triggered=hard_gate_triggered,
            hard_gate_reason=hard_gate_reason
        )

evidence_engine = EvidenceStrengthEngine()
