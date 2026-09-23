/**
 * IP-SAKTI Sahayak — Native Multilingual System (i18n.js)
 * No Google Translate. Pure deterministic frontend dictionary.
 * Supports: English (en), Hindi (hi)
 */

const I18N = {
  en: {
    // Header & Gov Bar
    "gov_title": "GOVERNMENT OF INDIA",
    "ministry": "Ministry of AYUSH • CSIR-TKDL Statutory Interface",
    "platform_badge": "IP-SAKTI Platform",
    "screen_reader": "Screen Reader Access",
    "sovereign_pulse": "SOVEREIGN NETWORK PULSE",
    "shlokas_parsed": "Shlokas Parsed Today",
    "tkdl_sync": "CSIR-TKDL v2.4 Sync:",
    "tkdl_nominal": "NOMINAL (99.98%)",
    "gazette_docketing": "Gazette Rule 158-B Docketing:",
    "gazette_active": "ACTIVE",
    "sovereign_node": "256-Bit Air-Gapped Sovereign Node:",
    "nic_verified": "NIC MEITY VERIFIED",
    "statutory_jurisdiction": "STATUTORY JURISDICTION: SEC 3(p) IPA 1970",

    // Navigation
    "nav_overview": "Statutory Overview",
    "nav_tkdl": "TKDL & Patent Search",
    "nav_classify": "Product Classification",
    "nav_gazette": "Gazette Bulletins",
    "nav_about": "About Us",
    "nav_home": "Home",

    // Mobile Bottom Tabs
    "tab_overview": "Overview",
    "tab_tkdl": "TKDL",
    "tab_classify": "Classify",
    "tab_gazette": "Gazettes",
    "tab_about": "About",

    // Masthead Sub-Bar
    "bharat_goi": "भारत सरकार • GOI",
    "lang_en": "EN",
    "lang_hi": "हिन्दी",

    // Hero Section
    "hero_pill": "STATUTORY INTELLIGENCE UNIT • AIR-GAPPED v2.4",
    "hero_title": "Sovereign Ayurvedic IP & Regulatory Intelligence",
    "hero_subtitle": "India's first autonomous Traditional Knowledge defense engine. Deterministically classifies ASU&H formulations, evaluates Section 3(p) patentability, and generates CSIR-TKDL concordance reports — with zero hallucination.",
    "hero_cta_login": "Authenticate via MeriPehchan",
    "hero_cta_sandbox": "Try Guest Sandbox (Instant Preview)",
    "hero_stat_shlokas": "Shlokas Indexed",
    "hero_stat_3p": "Sec 3(p) Accuracy",
    "hero_stat_dock": "Avg. Docketing",

    // Login Section
    "login_sso_title": "Sovereign Single Sign-On Infrastructure",
    "login_gateway_title": "NATIONAL ACCESS GATEWAY",
    "login_gateway_desc": "Select your statutory jurisdiction. Certified via National Single Sign-On (MeriPehchan / Jan Parichay) and DigiLocker Credential Exchange.",
    "login_track1_label": "Track 01 • Citizen & Innovator",
    "login_track1_title": "MeriPehchan / Jan Parichay",
    "login_track1_desc": "For individual herbalists, start-ups, bio-entrepreneurs, and academic researchers seeking free prior-art clearance and formulation verification.",
    "login_track2_label": "Track 02 • Legal Counsel",
    "login_track2_title": "Patent Attorney & Legal Agents",
    "login_track2_desc": "For registered Indian Patent Agents and IP counsels drafting Section 3(p) objections, FER responses, and pre-grant opposition briefs against biopiracy.",
    "login_track3_label": "Track 03 • Industry & Manufacturing",
    "login_track3_title": "AYUSH Drug Manufacturer (SLA Portal)",
    "login_track3_desc": "For ASU&H pharmaceutical enterprises generating automated Rule 158-B proof packages, Form 24-D manufacturing licenses, and COPP export filings.",
    "login_track4_label": "Track 04 • Sovereign Research",
    "login_track4_title": "Institutions & CSIR / CCRAS",
    "login_track4_desc": "For botanical taxonomy scientists, national pharmacopoeia committees, and CSIR-TKDL officers auditing classified Sanskrit prior art transcripts.",
    "login_auth_title": "Jan Parichay SSO",
    "login_auth_badge": "NIC Sovereign Node",
    "login_tab_otp": "Mobile OTP",
    "login_tab_dsc": "Digital Token (DSC)",
    "login_otp_label": "Registered Mobile Number for OTP",
    "login_consent": "Consent to fetch verified AYUSH/Bar Council credentials",
    "login_btn_auth": "Authenticate & Enter Portal",
    "login_dsc_label": "Enter 4-Digit Sovereign Access Token",
    "login_dsc_demo": "Demo access code:",
    "login_dsc_error": "Invalid token. Please try again.",
    "login_btn_verify": "Verify Token & Enter Portal",
    "login_or_sandbox": "OR SANDBOX TRIAL",
    "login_guest_btn": "Enter Read-Only Evaluator Mode (3 Queries/Day)",
    "login_security": "Secured in compliance with National Cyber Security Policy & IT Act 2000. 256-Bit TLS Sovereign Tunnel.",

    // Guest Sandbox
    "sandbox_pill": "Public Sandbox • No Login Required",
    "sandbox_title": "Instant Ayurvedic Formulation & Patentability Pre-Check",
    "sandbox_desc": "Test unpatented herbal combinations against traditional canonical texts (Charaka, Sushruta, AFI) and determine regulatory clearance pathways in real-time.",
    "sandbox_placeholder": "e.g., Withania somnifera standardized extract with Shilajit...",
    "sandbox_btn": "Execute Pre-Check",
    "sandbox_pills_label": "Test Sample Formulations:",

    // 4 Pillar Cards
    "pillar_title": "Four Sovereign Pillars of Traditional Knowledge Defense",
    "pillar_subtitle": "Core autonomous modules powering deterministic regulatory intelligence across the entire ASU&H product lifecycle.",
    "pillar1_badge1": "94% Clearance",
    "pillar1_badge2": "Patent Defense",
    "pillar1_title": "Section 3(p) Patent Evaluation",
    "pillar1_desc": "Evaluate patentability constraints under Section 3(p) of the Indian Patents Act, 1970. Overcome traditional knowledge obviousness objections with codified synergistic bioavailability evidence.",
    "pillar1_footer": "IPO Manual 2019 • Sec 3(e) Synergism",
    "pillar1_cta": "Run Claim Audit",
    "pillar2_badge1": "542K Shlokas",
    "pillar2_badge2": "CSIR Corpus",
    "pillar2_title": "TKDL Prior Art Verification",
    "pillar2_desc": "Cross-reference formulation components against Sanskrit, Unani, Siddha & Sowa-Rigpa canonical literature. Instantly detect shloka concordance in Charaka, Sushruta, and AFI-Vol I to IV.",
    "pillar2_footer": "WIPO IPC A61K 36/00 Concurrence",
    "pillar2_cta": "Inspect Shlokas",
    "pillar3_badge1": "NBA Form I",
    "pillar3_badge2": "ABS Clearance",
    "pillar3_title": "Geographical Indication (GI) & ABS",
    "pillar3_desc": "Analyze origin-based botanical IP protections, endemic habitat claims, and State Biodiversity Board (SBB) revenue sharing mandates under the Biological Diversity (Amendment) Act 2023.",
    "pillar3_footer": "382 Registered Botanical GIs",
    "pillar3_cta": "Analyze Provenance",
    "pillar4_badge1": "Form 25-D Wizard",
    "pillar4_badge2": "Statutory Map",
    "pillar4_title": "Classify Your Ayurvedic Product",
    "pillar4_desc": "Multi-step guided wizard to determine whether your item classifies as Shastric Classical, Patent & Proprietary (P&P), Nutraceutical (FSSAI AYUSH Aahar), or Topical Cosmetic.",
    "pillar4_footer": "Drugs & Cosmetics Sec 3(a)",
    "pillar4_cta": "Start Classifier",

    // Bio-Cultural Heritage
    "heritage_title": "Bio-Cultural Heritage & Anti-Biopiracy Case Studies",
    "heritage_subtitle": "Landmark international patent revocations achieved through traditional knowledge prior art defense.",

    // Sanskrit Banner
    "sanskrit_title": "Treatise Concordance Authority",
    "sanskrit_subtitle": "Constitutional Statutory Basis: Article 51A(h) — Duty to develop scientific temper. Section 3(p) IPA 1970 — Bar on traditional knowledge patenting.",
    "sanskrit_cta": "Search Shloka Lexicon",

    // FAQ
    "faq1_title": "Who can access IP-SAKTI?",
    "faq2_title": "Is TKDL Data Confidential?",
    "faq3_title": "What is Form 25-D Docketing?",

    // Hub Page
    "hub_title": "How can I assist you with AYUSH regulatory compliance today?",
    "hub_subtitle": "Autonomous statutory intelligence powered by CSIR-TKDL concordance. Every conclusion is evidence-traced, never hallucinated.",
    "hub_input_placeholder": "Ask IP-SAKTI Sahayak about formulation claims, Rule 158-B animal toxicity exemptions, or TKDL prior art...",
    "hub_mode_draft": "Drafting & Statutory Audit",
    "hub_mode_lit": "Litigation & 3(p) Defense",
    "hub_airgap": "256-Bit Sovereign Air-Gapped",
    "hub_disclaimer": "IP-SAKTI Sahayak provides statutory regulatory guidance referencing Gazette Notifications & CSIR-TKDL corpus. SHA-256 Verified.",
    "hub_bench": "AYUSH Bench #4 Active",
    "hub_new_session": "New Evaluation Session",
    "hub_search_placeholder": "Search case files, Samhitas...",

    // Footer
    "footer_gateway": "Official Sovereign Gateway under Section 3(p) Indian Patent Act & Biological Diversity Act, 2002",
    "footer_sso": "National Single Sign-On (Jan Parichay) Compliant",
    "footer_digilocker": "DigiLocker Certified Credentials",
    "footer_wcag": "WCAG 2.1 AA Accessible",
    "footer_copyright": "© 2024–2025 Ministry of AYUSH & Council of Scientific and Industrial Research (CSIR). Hosted on National Informatics Centre sovereign cloud infrastructure.",
    "footer_terms": "Terms of Public Access",
    "footer_hyperlink": "Hyperlink Policy",
    "footer_tkdl_nda": "TKDL Non-Disclosure Registry",
    "footer_security": "Sovereign Security Audit"
  },

  hi: {
    // Header & Gov Bar
    "gov_title": "भारत सरकार",
    "ministry": "आयुष मंत्रालय • CSIR-TKDL सांविधिक इंटरफ़ेस",
    "platform_badge": "IP-SAKTI मंच",
    "screen_reader": "स्क्रीन रीडर एक्सेस",
    "sovereign_pulse": "सॉवरेन नेटवर्क पल्स",
    "shlokas_parsed": "आज पार्स किए गए श्लोक",
    "tkdl_sync": "CSIR-TKDL v2.4 सिंक:",
    "tkdl_nominal": "सामान्य (99.98%)",
    "gazette_docketing": "गजट नियम 158-B डॉकेटिंग:",
    "gazette_active": "सक्रिय",
    "sovereign_node": "256-बिट एयर-गैप्ड सॉवरेन नोड:",
    "nic_verified": "NIC MEITY सत्यापित",
    "statutory_jurisdiction": "सांविधिक अधिकार क्षेत्र: धारा 3(p) IPA 1970",

    // Navigation
    "nav_overview": "विधिक अवलोकन",
    "nav_tkdl": "TKDL और पेटेंट खोज",
    "nav_classify": "उत्पाद वर्गीकरण",
    "nav_gazette": "राजपत्र बुलेटिन",
    "nav_about": "हमारे बारे में",
    "nav_home": "होम",

    // Mobile Bottom Tabs
    "tab_overview": "अवलोकन",
    "tab_tkdl": "TKDL",
    "tab_classify": "वर्गीकरण",
    "tab_gazette": "राजपत्र",
    "tab_about": "परिचय",

    // Masthead Sub-Bar
    "bharat_goi": "भारत सरकार • GOI",
    "lang_en": "EN",
    "lang_hi": "हिन्दी",

    // Hero Section
    "hero_pill": "सांविधिक खुफिया इकाई • एयर-गैप्ड v2.4",
    "hero_title": "सॉवरेन आयुर्वेदिक बौद्धिक संपदा और विनियामक गुप्तचर",
    "hero_subtitle": "भारत का पहला स्वायत्त पारंपरिक ज्ञान रक्षा इंजन। ASU&H फॉर्मूलेशन का निर्धारणात्मक वर्गीकरण, धारा 3(p) पेटेंटयोग्यता का मूल्यांकन, और CSIR-TKDL समन्वय रिपोर्ट — शून्य भ्रम के साथ।",
    "hero_cta_login": "MeriPehchan से प्रमाणित करें",
    "hero_cta_sandbox": "अतिथि सैंडबॉक्स आज़माएँ (तत्काल पूर्वावलोकन)",
    "hero_stat_shlokas": "अनुक्रमित श्लोक",
    "hero_stat_3p": "धारा 3(p) सटीकता",
    "hero_stat_dock": "औसत डॉकेटिंग",

    // Login Section
    "login_sso_title": "सॉवरेन सिंगल साइन-ऑन अवसंरचना",
    "login_gateway_title": "राष्ट्रीय प्रवेश द्वार",
    "login_gateway_desc": "अपना सांविधिक अधिकार क्षेत्र चुनें। राष्ट्रीय सिंगल साइन-ऑन (MeriPehchan / Jan Parichay) और DigiLocker क्रेडेंशियल एक्सचेंज द्वारा प्रमाणित।",
    "login_track1_label": "ट्रैक 01 • नागरिक और नवाचारक",
    "login_track1_title": "MeriPehchan / Jan Parichay",
    "login_track1_desc": "व्यक्तिगत वैद्यों, स्टार्ट-अप्स, जैव-उद्यमियों और शोधकर्ताओं के लिए मुफ्त पूर्व-कला मंजूरी और फॉर्मूलेशन सत्यापन।",
    "login_track2_label": "ट्रैक 02 • विधिक सलाहकार",
    "login_track2_title": "पेटेंट अटॉर्नी और कानूनी एजेंट",
    "login_track2_desc": "पंजीकृत भारतीय पेटेंट एजेंटों और IP परामर्शदाताओं के लिए जो धारा 3(p) आपत्ति, FER प्रतिक्रियाएँ, और जैव-चोरी विरोधी पत्र तैयार करते हैं।",
    "login_track3_label": "ट्रैक 03 • उद्योग और विनिर्माण",
    "login_track3_title": "आयुष औषधि निर्माता (SLA पोर्टल)",
    "login_track3_desc": "ASU&H फार्मास्युटिकल उद्यमों के लिए स्वचालित नियम 158-B प्रमाण पैकेज, फॉर्म 24-D निर्माण लाइसेंस और COPP निर्यात फाइलिंग।",
    "login_track4_label": "ट्रैक 04 • सॉवरेन अनुसंधान",
    "login_track4_title": "संस्थान और CSIR / CCRAS",
    "login_track4_desc": "वनस्पति वर्गीकरण वैज्ञानिकों, राष्ट्रीय फार्माकोपिया समितियों, और CSIR-TKDL अधिकारियों के लिए जो वर्गीकृत संस्कृत पूर्व-कला प्रतिलिपियों का लेखापरीक्षा करते हैं।",
    "login_auth_title": "Jan Parichay SSO",
    "login_auth_badge": "NIC सॉवरेन नोड",
    "login_tab_otp": "मोबाइल OTP",
    "login_tab_dsc": "डिजिटल टोकन (DSC)",
    "login_otp_label": "OTP के लिए पंजीकृत मोबाइल नंबर",
    "login_consent": "सत्यापित आयुष/बार काउंसिल प्रमाण-पत्र प्राप्त करने की सहमति",
    "login_btn_auth": "प्रमाणित करें और पोर्टल में प्रवेश करें",
    "login_dsc_label": "4-अंकीय सॉवरेन एक्सेस टोकन दर्ज करें",
    "login_dsc_demo": "डेमो एक्सेस कोड:",
    "login_dsc_error": "अमान्य टोकन। कृपया पुनः प्रयास करें।",
    "login_btn_verify": "टोकन सत्यापित करें और प्रवेश करें",
    "login_or_sandbox": "या सैंडबॉक्स ट्रायल",
    "login_guest_btn": "केवल-पठन मूल्यांकनकर्ता मोड में प्रवेश करें (3 प्रश्न/दिन)",
    "login_security": "राष्ट्रीय साइबर सुरक्षा नीति और IT अधिनियम 2000 के अनुपालन में सुरक्षित। 256-बिट TLS सॉवरेन टनल।",

    // Guest Sandbox
    "sandbox_pill": "सार्वजनिक सैंडबॉक्स • लॉगिन आवश्यक नहीं",
    "sandbox_title": "तत्काल आयुर्वेदिक फॉर्मूलेशन और पेटेंटयोग्यता पूर्व-जाँच",
    "sandbox_desc": "अपरीक्षित हर्बल संयोजनों को पारंपरिक शास्त्रीय ग्रंथों (चरक, सुश्रुत, AFI) के विरुद्ध परीक्षण करें और वास्तविक समय में विनियामक मंजूरी मार्ग निर्धारित करें।",
    "sandbox_placeholder": "उदा., अश्वगंधा मानकीकृत अर्क शिलाजीत के साथ...",
    "sandbox_btn": "पूर्व-जाँच निष्पादित करें",
    "sandbox_pills_label": "नमूना फॉर्मूलेशन परीक्षण:",

    // 4 Pillar Cards
    "pillar_title": "पारंपरिक ज्ञान रक्षा के चार सॉवरेन स्तंभ",
    "pillar_subtitle": "संपूर्ण ASU&H उत्पाद जीवनचक्र में निर्धारणात्मक विनियामक बुद्धिमत्ता को संचालित करने वाले मुख्य स्वायत्त मॉड्यूल।",
    "pillar1_badge1": "94% मंजूरी",
    "pillar1_badge2": "पेटेंट रक्षा",
    "pillar1_title": "धारा 3(p) पेटेंट मूल्यांकन",
    "pillar1_desc": "भारतीय पेटेंट अधिनियम, 1970 की धारा 3(p) के तहत पेटेंटयोग्यता बाधाओं का मूल्यांकन करें। कोडित सहक्रियात्मक जैव-उपलब्धता साक्ष्य के साथ पारंपरिक ज्ञान स्पष्टता आपत्तियों को पार करें।",
    "pillar1_footer": "IPO मैनुअल 2019 • धारा 3(e) सहक्रियावाद",
    "pillar1_cta": "दावा लेखापरीक्षा चलाएँ",
    "pillar2_badge1": "542K श्लोक",
    "pillar2_badge2": "CSIR कोर्पस",
    "pillar2_title": "TKDL पूर्व-कला सत्यापन",
    "pillar2_desc": "संस्कृत, यूनानी, सिद्ध और सोवा-रिग्पा शास्त्रीय साहित्य के विरुद्ध फॉर्मूलेशन घटकों को क्रॉस-रेफ़रेंस करें। चरक, सुश्रुत और AFI-खंड I से IV में श्लोक समन्वय तत्काल पहचानें।",
    "pillar2_footer": "WIPO IPC A61K 36/00 समन्वय",
    "pillar2_cta": "श्लोक निरीक्षण करें",
    "pillar3_badge1": "NBA फॉर्म I",
    "pillar3_badge2": "ABS मंजूरी",
    "pillar3_title": "भौगोलिक संकेत (GI) और ABS",
    "pillar3_desc": "मूल-आधारित वानस्पतिक बौद्धिक संपदा सुरक्षा, स्थानिक आवास दावों, और जैविक विविधता (संशोधन) अधिनियम 2023 के तहत राज्य जैव विविधता बोर्ड (SBB) राजस्व साझाकरण आदेशों का विश्लेषण करें।",
    "pillar3_footer": "382 पंजीकृत वानस्पतिक GIs",
    "pillar3_cta": "उत्पत्ति विश्लेषण करें",
    "pillar4_badge1": "फॉर्म 25-D विज़ार्ड",
    "pillar4_badge2": "विधिक मानचित्र",
    "pillar4_title": "अपने आयुर्वेदिक उत्पाद का वर्गीकरण करें",
    "pillar4_desc": "यह निर्धारित करने के लिए बहु-चरण निर्देशित विज़ार्ड कि आपकी वस्तु शास्त्रिक शास्त्रीय, पेटेंट और स्वामित्व (P&P), न्यूट्रास्यूटिकल (FSSAI आयुष आहार), या सामयिक सौंदर्य प्रसाधन के रूप में वर्गीकृत होती है।",
    "pillar4_footer": "औषधि और प्रसाधन सामग्री धारा 3(a)",
    "pillar4_cta": "वर्गीकरण शुरू करें",

    // Bio-Cultural Heritage
    "heritage_title": "जैव-सांस्कृतिक विरासत और जैव-चोरी विरोधी केस अध्ययन",
    "heritage_subtitle": "पारंपरिक ज्ञान पूर्व-कला रक्षा के माध्यम से प्राप्त ऐतिहासिक अंतर्राष्ट्रीय पेटेंट निरसन।",

    // Sanskrit Banner
    "sanskrit_title": "ग्रंथ समन्वय प्राधिकरण",
    "sanskrit_subtitle": "संवैधानिक सांविधिक आधार: अनुच्छेद 51A(h) — वैज्ञानिक दृष्टिकोण विकसित करने का कर्तव्य। धारा 3(p) IPA 1970 — पारंपरिक ज्ञान पेटेंटिंग पर रोक।",
    "sanskrit_cta": "श्लोक शब्दकोश खोजें",

    // FAQ
    "faq1_title": "IP-SAKTI तक कौन पहुँच सकता है?",
    "faq2_title": "क्या TKDL डेटा गोपनीय है?",
    "faq3_title": "फॉर्म 25-D डॉकेटिंग क्या है?",

    // Hub Page
    "hub_title": "आज मैं आयुष विनियामक अनुपालन में आपकी कैसे सहायता कर सकता हूँ?",
    "hub_subtitle": "CSIR-TKDL समन्वय द्वारा संचालित स्वायत्त सांविधिक बुद्धिमत्ता। प्रत्येक निष्कर्ष साक्ष्य-ट्रेस किया हुआ है, कभी भ्रमित नहीं।",
    "hub_input_placeholder": "फॉर्मूलेशन दावों, नियम 158-B पशु विषाक्तता छूट, या TKDL पूर्व-कला के बारे में IP-SAKTI सहायक से पूछें...",
    "hub_mode_draft": "प्रारूपण और सांविधिक लेखापरीक्षा",
    "hub_mode_lit": "मुकदमेबाजी और 3(p) रक्षा",
    "hub_airgap": "256-बिट सॉवरेन एयर-गैप्ड",
    "hub_disclaimer": "IP-SAKTI सहायक राजपत्र अधिसूचनाओं और CSIR-TKDL कोर्पस को संदर्भित करते हुए सांविधिक विनियामक मार्गदर्शन प्रदान करता है। SHA-256 सत्यापित।",
    "hub_bench": "आयुष बेंच #4 सक्रिय",
    "hub_new_session": "नया मूल्यांकन सत्र",
    "hub_search_placeholder": "केस फ़ाइलें, संहिताएँ खोजें...",

    // Footer
    "footer_gateway": "भारतीय पेटेंट अधिनियम धारा 3(p) और जैविक विविधता अधिनियम, 2002 के तहत आधिकारिक सॉवरेन गेटवे",
    "footer_sso": "राष्ट्रीय सिंगल साइन-ऑन (Jan Parichay) अनुपालक",
    "footer_digilocker": "DigiLocker प्रमाणित प्रमाण-पत्र",
    "footer_wcag": "WCAG 2.1 AA सुलभ",
    "footer_copyright": "© 2024–2025 आयुष मंत्रालय और वैज्ञानिक तथा औद्योगिक अनुसंधान परिषद (CSIR)। राष्ट्रीय सूचना विज्ञान केंद्र सॉवरेन क्लाउड अवसंरचना पर होस्ट किया गया।",
    "footer_terms": "सार्वजनिक पहुँच की शर्तें",
    "footer_hyperlink": "हाइपरलिंक नीति",
    "footer_tkdl_nda": "TKDL गैर-प्रकटीकरण रजिस्ट्री",
    "footer_security": "सॉवरेन सुरक्षा लेखापरीक्षा"
  }
};


// Build bidirectional maps for auto-translation of text nodes
let autoTransMapEnToHi = new Map();
let autoTransMapHiToEn = new Map();

function initAutoTransMaps() {
  const en = I18N['en'];
  const hi = I18N['hi'];
  for (const key in en) {
    if (en[key] && hi[key]) {
      autoTransMapEnToHi.set(en[key].trim(), hi[key].trim());
      autoTransMapHiToEn.set(hi[key].trim(), en[key].trim());
    }
  }
}

function autoTranslateNode(node, targetLang) {
  const text = node.nodeValue.trim();
  if (!text) return;
  
  if (targetLang === 'hi') {
    if (autoTransMapEnToHi.has(text)) {
      node.nodeValue = node.nodeValue.replace(text, autoTransMapEnToHi.get(text));
    }
  } else if (targetLang === 'en') {
    if (autoTransMapHiToEn.has(text)) {
      node.nodeValue = node.nodeValue.replace(text, autoTransMapHiToEn.get(text));
    }
  }
}

/**
 * Apply translations to all elements with [data-i18n] attributes AND auto-translate text nodes
 */
function applyTranslations(lang) {
  if (autoTransMapEnToHi.size === 0) initAutoTransMaps();
  
  const dict = I18N[lang] || I18N['en'];
  
  // 1. Data attribute translation
  document.querySelectorAll('[data-i18n]').forEach(el => {
    const key = el.getAttribute('data-i18n');
    if (dict[key]) {
      if (!el.hasAttribute('data-i18n-original')) {
        el.setAttribute('data-i18n-original', el.textContent);
      }
      el.textContent = dict[key];
    }
  });
  
  // 2. Placeholder translation
  document.querySelectorAll('[data-i18n-placeholder]').forEach(el => {
    const key = el.getAttribute('data-i18n-placeholder');
    if (dict[key]) {
      el.placeholder = dict[key];
    }
  });

  // 3. Auto-translate all text nodes that match dictionary strings
  const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT, null, false);
  let node;
  while ((node = walker.nextNode())) {
    // Skip script and style tags
    if (node.parentElement && (node.parentElement.tagName === 'SCRIPT' || node.parentElement.tagName === 'STYLE')) {
      continue;
    }
    autoTranslateNode(node, lang);
  }
}
function switchLanguage(lang) {
  localStorage.setItem('ipsakti_lang', lang);
  applyTranslations(lang);
  // Update language button active states
  document.querySelectorAll('[data-lang-btn]').forEach(btn => {
    const btnLang = btn.getAttribute('data-lang-btn');
    if (btnLang === lang) {
      btn.classList.add('bg-surface-container', 'text-on-surface', 'font-bold');
      btn.classList.remove('text-on-surface-variant', 'font-medium');
    } else {
      btn.classList.remove('bg-surface-container', 'text-on-surface', 'font-bold');
      btn.classList.add('text-on-surface-variant', 'font-medium');
    }
  });
}

/**
 * Get the current active language
 */
function getCurrentLanguage() {
  return localStorage.getItem('ipsakti_lang') || 'en';
}

/**
 * Initialize i18n on page load
 */
document.addEventListener('DOMContentLoaded', () => {
  const lang = getCurrentLanguage();
  applyTranslations(lang);
});
