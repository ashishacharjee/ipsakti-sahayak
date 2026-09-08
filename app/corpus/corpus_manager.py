"""
Corpus Manager for IP-SAKTI Sahayak
Provides indexed lookups, filtering by jurisdiction, and access to verified provisions.
"""

from typing import List, Dict, Optional, Any
from app.corpus.provisions_data import PROVISIONS
from app.models.schemas import LegalSourceReference

class CorpusManager:
    def __init__(self):
        self._provisions: List[Dict[str, Any]] = PROVISIONS
        self._by_id: Dict[str, Dict[str, Any]] = {p["id"]: p for p in PROVISIONS}

    def get_all_provisions(self) -> List[Dict[str, Any]]:
        return self._provisions

    def get_by_id(self, provision_id: str) -> Optional[Dict[str, Any]]:
        return self._by_id.get(provision_id)

    def get_by_jurisdiction(self, jurisdiction: str) -> List[Dict[str, Any]]:
        """Filter provisions by jurisdiction ('India' or 'International')."""
        norm = jurisdiction.strip().lower()
        if norm in ["india", "national"]:
            return [p for p in self._provisions if p["jurisdiction"] == "India"]
        elif norm in ["international", "global", "foreign"]:
            return [p for p in self._provisions if p["jurisdiction"] == "International"]
        return self._provisions

    def get_by_category(self, category_tag: str) -> List[Dict[str, Any]]:
        """Filter provisions applicable to a regulatory category or tag."""
        results = []
        for p in self._provisions:
            tags = p.get("category_tags", [])
            if any(category_tag.lower() in t.lower() or t == "All Categories" for t in tags):
                results.append(p)
        return results

    def to_source_reference(self, p: Dict[str, Any]) -> LegalSourceReference:
        return LegalSourceReference(
            provision_id=p["id"],
            statute_name=p["statute"],
            section_or_rule=p["section"],
            year_and_amendment=p["year"],
            authority_type=p["authority_type"],
            jurisdiction=p["jurisdiction"],
            key_excerpt=p["content"],
            applicability_note=p["legal_implication"],
            official_source_url=p["official_url"]
        )

    def get_references_by_ids(self, ids: List[str]) -> List[LegalSourceReference]:
        refs = []
        for pid in ids:
            p = self.get_by_id(pid)
            if p:
                refs.append(self.to_source_reference(p))
        return refs

corpus_manager = CorpusManager()
