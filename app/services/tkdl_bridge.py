"""
TKDL Search Bridge & Query Builder for IP-SAKTI Sahayak
Problem Statement 26045 - SIH 2026

Transforms plain-language formulation inputs into structured prior-art queries,
Traditional Knowledge Resource Classification (TKRC) codes, and IPC subclasses.
Scoped honestly as an intelligent query-constructing bridge (respecting TKDL's NDA status).
"""

from typing import List, Dict, Optional
from app.models.schemas import TKDLQueryRequest, TKDLQueryResponse

# Botanical database mapping common Ayurvedic herbs to binomial taxonomy & TKRC/IPC codes
BOTANICAL_TAXONOMY: Dict[str, Dict[str, str]] = {
    "ashwagandha": {
        "botanical": "Withania somnifera",
        "family": "Solanaceae",
        "sanskrit": "Aśvagandhā",
        "tkrc": "AK02-B/112 (Withania somnifera root)",
        "ipc": "A61K 36/81",
        "classical_texts": "Charaka Samhita (Chikitsa Sthana 1:2), Bhavaprakasha (Guduchyadi Varga)"
    },
    "turmeric": {
        "botanical": "Curcuma longa",
        "family": "Zingiberaceae",
        "sanskrit": "Haridrā",
        "tkrc": "AK02-B/245 (Curcuma longa rhizome)",
        "ipc": "A61K 36/9066",
        "classical_texts": "Sushruta Samhita (Sutra Sthana 38), Ayurvedic Formulary of India (Part I)"
    },
    "haridra": {
        "botanical": "Curcuma longa",
        "family": "Zingiberaceae",
        "sanskrit": "Haridrā",
        "tkrc": "AK02-B/245 (Curcuma longa rhizome)",
        "ipc": "A61K 36/9066",
        "classical_texts": "Charaka Samhita, Ashtanga Hridaya"
    },
    "tulsi": {
        "botanical": "Ocimum sanctum (Ocimum tenuiflorum)",
        "family": "Lamiaceae",
        "sanskrit": "Tulasī",
        "tkrc": "AK02-B/418 (Ocimum sanctum aerial parts)",
        "ipc": "A61K 36/53",
        "classical_texts": "Bhavaprakasha, Bhaishajya Ratnavali"
    },
    "amla": {
        "botanical": "Phyllanthus emblica (Emblica officinalis)",
        "family": "Phyllanthaceae",
        "sanskrit": "Āmalakī",
        "tkrc": "AK02-B/189 (Emblica officinalis pericarp)",
        "ipc": "A61K 36/47",
        "classical_texts": "Charaka Samhita (Rasayana Adhyaya), Sushruta Samhita"
    },
    "amalaki": {
        "botanical": "Phyllanthus emblica",
        "family": "Phyllanthaceae",
        "sanskrit": "Āmalakī",
        "tkrc": "AK02-B/189 (Emblica officinalis pericarp)",
        "ipc": "A61K 36/47",
        "classical_texts": "Charaka Samhita (Rasayana Adhyaya), Sushruta Samhita"
    },
    "guduchi": {
        "botanical": "Tinospora cordifolia",
        "family": "Menispermaceae",
        "sanskrit": "Guḍūcī / Amṛtā",
        "tkrc": "AK02-B/503 (Tinospora cordifolia stem)",
        "ipc": "A61K 36/59",
        "classical_texts": "Charaka Samhita, Bhavaprakasha, Ayurvedic Formulary of India"
    },
    "giloy": {
        "botanical": "Tinospora cordifolia",
        "family": "Menispermaceae",
        "sanskrit": "Guḍūcī",
        "tkrc": "AK02-B/503 (Tinospora cordifolia stem)",
        "ipc": "A61K 36/59",
        "classical_texts": "Charaka Samhita, Bhavaprakasha"
    },
    "guggulu": {
        "botanical": "Commiphora mukul (Commiphora wightii)",
        "family": "Burseraceae",
        "sanskrit": "Guggulu",
        "tkrc": "AK02-B/088 (Commiphora mukul exudate)",
        "ipc": "A61K 36/324",
        "classical_texts": "Sushruta Samhita, Sharangadhara Samhita, AFI Part I"
    },
    "brahmi": {
        "botanical": "Bacopa monnieri",
        "family": "Plantaginaceae",
        "sanskrit": "Brāhmī",
        "tkrc": "AK02-B/054 (Bacopa monnieri whole plant)",
        "ipc": "A61K 36/68",
        "classical_texts": "Charaka Samhita, Ashtanga Hridaya"
    },
    "shatavari": {
        "botanical": "Asparagus racemosus",
        "family": "Asparagaceae",
        "sanskrit": "Śatāvarī",
        "tkrc": "AK02-B/032 (Asparagus racemosus tuber)",
        "ipc": "A61K 36/896",
        "classical_texts": "Charaka Samhita, Bhavaprakasha"
    },
    "arjuna": {
        "botanical": "Terminalia arjuna",
        "family": "Combretaceae",
        "sanskrit": "Arjuna",
        "tkrc": "AK02-B/492 (Terminalia arjuna bark)",
        "ipc": "A61K 36/185",
        "classical_texts": "Chakradatta (Hridroga Rogadhikara), AFI Part I"
    },
    "neem": {
        "botanical": "Azadirachta indica",
        "family": "Meliaceae",
        "sanskrit": "Nimba",
        "tkrc": "AK02-B/047 (Azadirachta indica leaf/bark)",
        "ipc": "A61K 36/58",
        "classical_texts": "Charaka Samhita, Sushruta Samhita"
    }
}

class TKDLBridgeService:
    def build_query(self, req: TKDLQueryRequest) -> TKDLQueryResponse:
        identified_botanicals: List[Dict[str, str]] = []
        tkrc_codes: List[str] = ["AK01 (Ayurveda - General Therapeutic Applications)"]
        ipc_classes: List[str] = ["A61K 36/00 (Medicinal preparations of plant origin)"]
        classical_refs: List[str] = list(req.classical_texts) if req.classical_texts else []
        search_terms: List[str] = []

        # Analyze formulation name and input terms
        combined_text = f"{req.formulation_name} {' '.join(req.sanskrit_or_botanical_terms)}".lower()

        for key, data in BOTANICAL_TAXONOMY.items():
            if key in combined_text:
                identified_botanicals.append({
                    "common_name": key.title(),
                    "botanical_name": data["botanical"],
                    "sanskrit_name": data["sanskrit"],
                    "family": data["family"]
                })
                tkrc_codes.append(data["tkrc"])
                ipc_classes.append(data["ipc"])
                if data["classical_texts"] not in classical_refs:
                    classical_refs.append(data["classical_texts"])
                search_terms.append(f'"{data["botanical"]}"')
                search_terms.append(f'"{data["sanskrit"]}"')
                search_terms.append(key.title())

        # Fallback if no specific botanical recognized
        if not identified_botanicals:
            search_terms.append(f'"{req.formulation_name}"')
            tkrc_codes.append("AK03 (Compound Ayurvedic Formulations - Yoga)")
            classical_refs.append("Ayurvedic Formulary of India (AFI), Part I & II")

        # Add target therapeutic IPC if specified
        target = (req.therapeutic_target or "").lower()
        if "inflamm" in target or "pain" in target or "arthriti" in target:
            ipc_classes.append("A61P 29/00 (Anti-inflammatory / Analgesic agents)")
            search_terms.append("(inflammation OR arthritic OR analgesic OR Vedanasthapana)")
        elif "diabet" in target or "sugar" in target or "prameha" in target:
            ipc_classes.append("A61P 3/10 (Antidiabetic agents / Prameha)")
            search_terms.append("(diabetes OR glycemic OR Prameha)")
        elif "neuro" in target or "cognit" in target or "memory" in target or "medhya" in target:
            ipc_classes.append("A61P 25/00 (Central nervous system agents / Medhya Rasayana)")
            search_terms.append("(cognitive OR memory OR adaptogen OR Medhya)")

        # Format structured boolean query compatible with InPASS and TKDL search criteria
        botanical_clause = " OR ".join(search_terms[:6])
        ipc_clause = " OR ".join(ipc_classes[:3])
        structured_query = f"({botanical_clause}) AND ({ipc_clause}) AND (extract OR composition OR formulation)"

        disclaimer = (
            "Honest Bridge Notice: This query is constructed for searching IP India InPASS, WIPO Patentscope, "
            "and public prior-art databases. Full TKDL database access is restricted under confidential non-disclosure "
            "agreements (NDAs) exclusively to partner patent offices (USPTO, EPO, JPO, etc.)."
        )

        return TKDLQueryResponse(
            tkrc_codes=list(dict.fromkeys(tkrc_codes)),
            ipc_classes=list(dict.fromkeys(ipc_classes)),
            structured_search_query=structured_query,
            identified_botanicals=identified_botanicals,
            classical_text_references=list(dict.fromkeys(classical_refs)),
            disclaimer=disclaimer
        )

tkdl_bridge = TKDLBridgeService()
