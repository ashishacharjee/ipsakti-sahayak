"""
Internationalization (i18n) and Bhashini Integration Layer
Problem Statement 26045 - SIH 2026
Provides English & Hindi core localization with Bhashini-ready schema.
"""

from typing import Dict, Any

TRANSLATIONS: Dict[str, Dict[str, str]] = {
    "en": {
        "title": "IP-SAKTI Sahayak",
        "subtitle": "Multilingual AI Assistant for Ayurveda Intellectual Property & Regulatory Compliance",
        "motto": "AI Assists. Rules Decide. Evidence Proves — Or Defers to a Human.",
        "disclaimer_banner": "Information, Not Legal Advice | Ministry of Ayush & AIIA Guidance Standard",
        "jurisdiction_india": "🇮🇳 India (National Regime)",
        "jurisdiction_intl": "🌐 International (WIPO / PCT / Nagoya)",
        "classification_wizard": "Deterministic Classification Engine",
        "step_1_title": "Step 1: Intended Application",
        "step_1_q": "What is the primary intended use of the Ayurvedic product?",
        "step_2_title": "Step 2: Formulation Source",
        "step_2_q": "How is the formulation derived or prepared?",
        "step_3_title": "Step 3: Therapeutic Claim",
        "step_3_q": "What is the nature of the claim or medical indication?",
        "step_4_title": "Step 4: Extraction & Clinical Level",
        "step_4_q": "What level of extraction, fingerprinting, or clinical evaluation exists?",
        "abs_gate_title": "Independent ABS & Biodiversity Compliance Gate",
        "applicant_type_label": "Select Applicant Category under Biological Diversity Act:",
        "evidence_meter_title": "100-Point Evidence Strength Engine",
        "btn_classify": "Run Deterministic Assessment",
        "btn_reset": "Reset Assessment",
        "btn_export_brief": "Download Review Brief",
        "btn_tkdl_search": "Generate TKDL / IPC Query",
        "statute_explorer": "Curated Statutory Corpus (25+ Provisions)",
        "safe_abstention_notice": "SAFE ABSTENTION TRIGGERED: Groundwork assembled into Review Brief for human facilitator.",
        "category_classical": "Classical / Generic Ayurvedic Medicine",
        "category_patent_proprietary": "Patent or Proprietary Ayurvedic Medicine (P&P)",
        "category_new_drug": "New Drug / Non-Classical Ayurvedic Drug",
        "category_phytopharma": "Phytopharmaceutical Drug",
        "category_nutraceutical": "Ayurveda-Aahar / Nutraceutical",
        "category_cosmetic": "Ayurvedic Cosmetic"
    },
    "hi": {
        "title": "आईपी-शक्ति सहायक",
        "subtitle": "आयुर्वेद बौद्धिक संपदा (IPR) एवं विनियामक मार्गदर्शन हेतु बहुभाषी एआई सहायक",
        "motto": "एआई सहायता करता है। नियम निर्णय लेते हैं। साक्ष्य प्रमाणित करते हैं — अन्यथा मानव विशेषज्ञ को सौंपते हैं।",
        "disclaimer_banner": "सूचना मात्र, कानूनी सलाह नहीं | आयुष मंत्रालय एवं अखिल भारतीय आयुर्वेद संस्थान (AIIA) मानक",
        "jurisdiction_india": "🇮🇳 भारत (राष्ट्रीय विनियामक ढांचा)",
        "jurisdiction_intl": "🌐 अंतर्राष्ट्रीय (WIPO / PCT / नागोया प्रोटोकॉल)",
        "classification_wizard": "नियम-आधारित वर्गीकरण इंजन (Deterministic Engine)",
        "step_1_title": "चरण 1: उत्पाद का मुख्य उपयोग",
        "step_1_q": "आयुर्वेदिक उत्पाद का प्राथमिक अभीष्ट उपयोग क्या है?",
        "step_2_title": "चरण 2: योग (फॉर्मूलेशन) का आधार",
        "step_2_q": "फॉर्मूलेशन किस प्रकार तैयार किया गया है?",
        "step_3_title": "चरण 3: चिकित्सकीय दावा",
        "step_3_q": "उत्पाद के साथ किस प्रकार का चिकित्सकीय या स्वास्थ्य दावा जुड़ा है?",
        "step_4_title": "चरण 4: निष्कर्षण एवं नैदानिक साक्ष्य",
        "step_4_q": "मानकीकरण, फिंगरप्रिंटिंग या नैदानिक परीक्षण (Clinical Trials) का क्या स्तर है?",
        "abs_gate_title": "स्वतंत्र जैव विविधता एवं ABS अनुपालन गेट",
        "applicant_type_label": "जैविक विविधता अधिनियम के तहत आवेदक की श्रेणी चुनें:",
        "evidence_meter_title": "100-अंकीय साक्ष्य शक्ति मीटर (Evidence Strength)",
        "btn_classify": "वर्गीकरण एवं विश्लेषण आरंभ करें",
        "btn_reset": "रीसेट करें",
        "btn_export_brief": "समीक्षा विवरण (Review Brief) डाउनलोड करें",
        "btn_tkdl_search": "टीकेडीएल / आईपीसी खोज क्वेरी बनाएं",
        "statute_explorer": "सत्यापित कानूनी संकलन (25+ वैधानिक प्रावधान)",
        "safe_abstention_notice": "सुरक्षित परहेज (Safe Abstention) सक्रिय: मानव विशेषज्ञ के लिए समीक्षा विवरण तैयार किया गया है।",
        "category_classical": "शास्त्रीय / जेनेरिक आयुर्वेदिक औषधि",
        "category_patent_proprietary": "पेटेंट या प्रोप्राइटरी आयुर्वेदिक औषधि (P&P)",
        "category_new_drug": "नवीन औषधि (New Drug) / गैर-शास्त्रीय औषधि",
        "category_phytopharma": "फाइटोफार्मास्युटिकल औषधि (Phytopharmaceutical)",
        "category_nutraceutical": "आयुर्वेद-आहार / न्यूट्रास्युटिकल",
        "category_cosmetic": "आयुर्वेदिक प्रसाधन सामग्री (Cosmetic)"
    }
}

class LocalizationService:
    def get(self, key: str, lang: str = "en") -> str:
        lang_dict = TRANSLATIONS.get(lang.lower(), TRANSLATIONS["en"])
        return lang_dict.get(key, TRANSLATIONS["en"].get(key, key))

    def get_all(self, lang: str = "en") -> Dict[str, str]:
        return TRANSLATIONS.get(lang.lower(), TRANSLATIONS["en"])

    def bhashini_translate(self, text: str, source_lang: str, target_lang: str) -> Dict[str, Any]:
        """
        Bhashini API integration stub.
        Can interface directly with Ulca / Bhashini NMT APIs when API credentials are provided.
        """
        return {
            "source_language": source_lang,
            "target_language": target_lang,
            "original_text": text,
            "pipeline_type": "Bhashini_NMT_ASU_Domain",
            "translated_text": text if source_lang == target_lang else f"[{target_lang.upper()}] {text}",
            "status": "ready"
        }

localization_service = LocalizationService()
