"""
BM25 and Semantic Retrieval Service for IP-SAKTI Sahayak
Problem Statement 26045 - SIH 2026

Retrieves verified legal provisions matching user queries and classification states,
partitioned by jurisdiction (India vs International).
"""

import re
from typing import List, Dict, Any, Tuple
from rank_bm25 import BM25Okapi
from app.corpus.corpus_manager import corpus_manager

class LegalRetrievalService:
    def __init__(self):
        self._provisions = corpus_manager.get_all_provisions()
        self._tokenized_corpus = [
            self._tokenize(
                f"{p['title']} {p['statute']} {p['section']} {p['content']} {p['legal_implication']} {' '.join(p.get('category_tags', []))}"
            )
            for p in self._provisions
        ]
        self._bm25 = BM25Okapi(self._tokenized_corpus)

    def _tokenize(self, text: str) -> List[str]:
        cleaned = re.sub(r"[^\w\s]", " ", text.lower())
        return [w for w in cleaned.split() if len(w) > 2]

    def search(
        self,
        query: str,
        category_tag: str = "",
        jurisdiction: str = "both",
        top_k: int = 5
    ) -> List[Dict[str, Any]]:
        """
        Retrieves relevant legal provisions using BM25 with statutory category boosting.
        """
        tokenized_query = self._tokenize(query)
        if not tokenized_query:
            # Fallback to category provisions
            return corpus_manager.get_by_category(category_tag)[:top_k]

        doc_scores = self._bm25.get_scores(tokenized_query)
        
        # Apply metadata and category boosters
        scored_docs: List[Tuple[float, Dict[str, Any]]] = []
        for idx, score in enumerate(doc_scores):
            p = self._provisions[idx]
            boosted_score = float(score)

            # Category boost
            if category_tag and any(category_tag.lower() in t.lower() or t == "All Categories" for t in p.get("category_tags", [])):
                boosted_score += 3.0

            # Jurisdiction filter
            jur = jurisdiction.strip().lower()
            if jur in ["india", "national"] and p.get("jurisdiction") != "India":
                boosted_score -= 10.0
            elif jur in ["international", "global"] and p.get("jurisdiction") != "International":
                boosted_score -= 10.0

            if boosted_score > 0.1:
                scored_docs.append((boosted_score, p))

        # Sort descending
        scored_docs.sort(key=lambda x: x[0], reverse=True)
        return [doc for _, doc in scored_docs[:top_k]]

    def retrieve_dual_jurisdiction(
        self,
        query: str,
        category_tag: str = "",
        top_k_each: int = 4
    ) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
        """
        Retrieves provisions for National (India) and International layers concurrently,
        keeping them strictly segregated.
        """
        india_docs = self.search(query, category_tag=category_tag, jurisdiction="India", top_k=top_k_each)
        intl_docs = self.search(query, category_tag=category_tag, jurisdiction="International", top_k=top_k_each)
        
        # Ensure default foundational provisions if query is narrow
        if not india_docs:
            india_docs = corpus_manager.get_by_jurisdiction("India")[:top_k_each]
        if not intl_docs:
            intl_docs = corpus_manager.get_by_jurisdiction("International")[:top_k_each]

        return india_docs, intl_docs

legal_retrieval = LegalRetrievalService()
