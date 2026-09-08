"""
Curated Statutory Corpus for IP-SAKTI Sahayak
Problem Statement 26045 - SIH 2026
Verified primary legal provisions with version-tracking, authority weighting, and currency dates.
"""

from typing import List, Dict, Any

PROVISIONS: List[Dict[str, Any]] = [
    {
        "id": "DCA_3A",
        "statute": "Drugs and Cosmetics Act, 1940",
        "section": "Section 3(a)",
        "year": "1940 (as amended)",
        "authority_type": "Statute (Parliament of India)",
        "authority_weight": 20,
        "currency_date": "2024-01-01",
        "is_active": True,
        "jurisdiction": "India",
        "category_tags": ["Classical / Generic Ayurvedic Medicine"],
        "title": "Definition of Ayurvedic, Siddha or Unani drug",
        "content": (
            "Section 3(a) defines 'Ayurvedic, Siddha or Unani drug' to include all medicines intended for "
            "internal or external use for or in the diagnosis, treatment, mitigation or prevention of disease "
            "or disorder in human beings or animals, and manufactured exclusively in accordance with the formulae "
            "described in the authoritative books of Ayurvedic, Siddha and Unani systems of medicine, specified "
            "in the First Schedule."
        ),
        "legal_implication": (
            "Classical formulations must strictly adhere to the 54 authoritative texts listed in the First Schedule. "
            "They qualify as prior art and traditional knowledge, and are generally excluded from patenting under Section 3(p)."
        ),
        "official_url": "https://www.indiacode.nic.in/handle/123456789/2411"
    },
    {
        "id": "DCA_3H",
        "statute": "Drugs and Cosmetics Act, 1940",
        "section": "Section 3(h)",
        "year": "1940 (as amended)",
        "authority_type": "Statute (Parliament of India)",
        "authority_weight": 20,
        "currency_date": "2024-01-01",
        "is_active": True,
        "jurisdiction": "India",
        "category_tags": ["Patent or Proprietary Ayurvedic Medicine (P&P)"],
        "title": "Definition of Patent or Proprietary Medicine in ASU",
        "content": (
            "Section 3(h) defines 'patent or proprietary medicine' in relation to Ayurvedic, Siddha or Unani systems "
            "of medicine as a formulation containing only such ingredients mentioned in the authoritative books of "
            "the First Schedule, but does not include a medicine which is administered by parenteral route and also "
            "a formulation identical in all respects with classical formulations."
        ),
        "legal_implication": (
            "P&P formulations combine First-Schedule herbs in modified ratios or modern dosage forms (capsules, tablets). "
            "Crucially, the statutory exclusion prevents identical classical recipes from masquerading as P&P. "
            "Patentability requires demonstrating surprising synergistic efficacy under Section 3(e) to overcome Section 3(p)."
        ),
        "official_url": "https://www.indiacode.nic.in/handle/123456789/2411"
    },
    {
        "id": "DCA_3AAA",
        "statute": "Drugs and Cosmetics Act, 1940",
        "section": "Section 3(aaa)",
        "year": "1940 (as amended)",
        "authority_type": "Statute (Parliament of India)",
        "authority_weight": 20,
        "currency_date": "2024-01-01",
        "is_active": True,
        "jurisdiction": "India",
        "category_tags": ["Ayurvedic Cosmetic"],
        "title": "Definition of Cosmetic",
        "content": (
            "Section 3(aaa) defines 'cosmetic' as any article intended to be rubbed, poured, sprinkled or sprayed on, "
            "or introduced into, or otherwise applied to, the human body or any part thereof for cleansing, beautifying, "
            "promoting attractiveness, or altering the appearance, and includes any article intended for use as a component of cosmetic."
        ),
        "legal_implication": (
            "Ayurvedic cosmetics fall under the Cosmetics Rules 2020. Products cannot make therapeutic, cure, or medicinal "
            "claims without triggering drug licensing regulations under Section 3(h) or 3(a)."
        ),
        "official_url": "https://www.indiacode.nic.in/handle/123456789/2411"
    },
    {
        "id": "DCR_158B",
        "statute": "Drugs and Cosmetics Rules, 1945",
        "section": "Rule 158-B",
        "year": "1945 (clarified 2018)",
        "authority_type": "Central Government Rules",
        "authority_weight": 16,
        "currency_date": "2024-01-01",
        "is_active": True,
        "jurisdiction": "India",
        "category_tags": ["Classical / Generic Ayurvedic Medicine", "Patent or Proprietary Ayurvedic Medicine (P&P)"],
        "title": "Guidelines for Issue of License with respect to ASU Drugs",
        "content": (
            "Rule 158-B specifies licensing requirements and evidence of safety and efficacy. For Classical drugs, "
            "citation of authoritative texts from the First Schedule suffices. For Patent or Proprietary ASU drugs: "
            "(i) Published textual evidence or published safety/pilot trial literature for modified classical extracts; "
            "(ii) Acute toxicity and clinical safety trials if novel excipients or significant modifications are introduced."
        ),
        "legal_implication": (
            "Delineates the exact evidence burden between classical generic manufacturing (textual citation) and "
            "P&P medicine licensing (safety data + stability testing + pilot studies)."
        ),
        "official_url": "https://cdsco.gov.in"
    },
    {
        "id": "PAT_3P",
        "statute": "The Patents Act, 1970",
        "section": "Section 3(p)",
        "year": "1970 (amended 2002)",
        "authority_type": "Statute (Parliament of India)",
        "authority_weight": 20,
        "currency_date": "2024-01-01",
        "is_active": True,
        "jurisdiction": "India",
        "category_tags": ["Classical / Generic Ayurvedic Medicine", "Patent or Proprietary Ayurvedic Medicine (P&P)"],
        "title": "Inventions Not Patentable: Traditional Knowledge Bar",
        "content": (
            "Section 3(p) bars patentability of 'an invention which in effect, is traditional knowledge or which is "
            "an aggregation or duplication of known properties of traditionally known component or components.'"
        ),
        "legal_implication": (
            "Absolute statutory hurdle for direct classical Ayurvedic recipes. Any patent application claiming known "
            "medicinal uses of plants documented in Ayurvedic literature or TKDL will be rejected under Section 3(p)."
        ),
        "official_url": "https://ipindia.gov.in/patents.htm"
    },
    {
        "id": "PAT_3E",
        "statute": "The Patents Act, 1970",
        "section": "Section 3(e)",
        "year": "1970 (amended 2002)",
        "authority_type": "Statute (Parliament of India)",
        "authority_weight": 20,
        "currency_date": "2024-01-01",
        "is_active": True,
        "jurisdiction": "India",
        "category_tags": ["Patent or Proprietary Ayurvedic Medicine (P&P)", "New Drug / Non-Classical Ayurvedic Drug"],
        "title": "Inventions Not Patentable: Mere Admixture Bar",
        "content": (
            "Section 3(e) bars 'a substance obtained by a mere admixture resulting only in the aggregation of the "
            "properties of the components thereof or a process for producing such substance.'"
        ),
        "legal_implication": (
            "To overcome Section 3(e), an Ayurvedic herbal combination must present empirical, comparative pharmacological "
            "evidence demonstrating synergistic interaction (Combination Index < 1 or super-additive efficacy), not just additive effect."
        ),
        "official_url": "https://ipindia.gov.in/patents.htm"
    },
    {
        "id": "PAT_3D",
        "statute": "The Patents Act, 1970",
        "section": "Section 3(d)",
        "year": "1970 (amended 2005)",
        "authority_type": "Statute (Parliament of India)",
        "authority_weight": 20,
        "currency_date": "2024-01-01",
        "is_active": True,
        "jurisdiction": "India",
        "category_tags": ["New Drug / Non-Classical Ayurvedic Drug", "Phytopharmaceutical Drug"],
        "title": "Inventions Not Patentable: Mere Discovery of New Form or Use",
        "content": (
            "Section 3(d) bars 'the mere discovery of a new form of a known substance which does not result in the "
            "enhancement of the known efficacy of that substance or the mere discovery of any new property or new use "
            "for a known substance or of the mere use of a known process, machine or apparatus unless such known process "
            "results in a new product or employs at least one new reactant.'"
        ),
        "legal_implication": (
            "Using an Ayurvedic herb for a new therapeutic indication requires showing significant enhancement of therapeutic "
            "efficacy compared to the known classical preparation."
        ),
        "official_url": "https://ipindia.gov.in/patents.htm"
    },
    {
        "id": "PAT_10_4",
        "statute": "The Patents Act, 1970",
        "section": "Section 10(4)(d)(ii)",
        "year": "1970 (amended 2002)",
        "authority_type": "Statute (Parliament of India)",
        "authority_weight": 20,
        "currency_date": "2024-01-01",
        "is_active": True,
        "jurisdiction": "India",
        "category_tags": ["All Categories", "Patent or Proprietary Ayurvedic Medicine (P&P)", "New Drug / Non-Classical Ayurvedic Drug"],
        "title": "Mandatory Disclosure of Source and Geographical Origin of Biological Material",
        "content": (
            "Section 10(4)(d)(ii) mandates that if the applicant mentions biological material in the specification which is "
            "obtained from India, the applicant must disclose the source and geographical origin of the biological material, "
            "and submit the approval of the National Biodiversity Authority (under Section 6 of the Biological Diversity Act)."
        ),
        "legal_implication": (
            "Failure to disclose or false disclosure is an explicit ground for pre-grant and post-grant opposition (Sec 25(1)(j), "
            "Sec 25(2)(j)) and revocation of patent under Section 64(1)(p) and 64(1)(q)."
        ),
        "official_url": "https://ipindia.gov.in/patents.htm"
    },
    {
        "id": "PAT_RULES_2024",
        "statute": "Patents (Amendment) Rules, 2024",
        "section": "Rules 12, 131 and Form 27",
        "year": "2024",
        "authority_type": "Central Government Rules",
        "authority_weight": 18,
        "currency_date": "2024-03-15",
        "is_active": True,
        "jurisdiction": "India",
        "category_tags": ["All Categories"],
        "title": "Patents (Amendment) Rules 2024 - Procedural and Working Reforms",
        "content": (
            "Notified in March 2024, simplifies statement of working (Form 27) from annual to once every three financial years. "
            "Streamlines request for examination timelines and reduces official fees for educational institutions and startups. "
            "Clarifies compliance timelines for submitting NBA approval under Section 6 before grant."
        ),
        "legal_implication": (
            "Applicants must ensure NBA approval is on record with the Patent Office prior to the grant of patent; non-compliance "
            "stalls the patent application at the examination stage."
        ),
        "official_url": "https://ipindia.gov.in"
    },
    {
        "id": "BDA_SEC3",
        "statute": "Biological Diversity Act, 2002",
        "section": "Section 3",
        "year": "2002 (amended 2023)",
        "authority_type": "Statute (Parliament of India)",
        "authority_weight": 20,
        "currency_date": "2024-01-01",
        "is_active": True,
        "jurisdiction": "India",
        "category_tags": ["Foreign Entity Track"],
        "title": "Approval of NBA required for foreign persons and entities",
        "content": (
            "Section 3 prohibits non-Indian citizens, non-residents, foreign corporations, or Indian corporations having any "
            "foreign shareholding or management participation, from obtaining biological resources occurring in India or knowledge "
            "associated thereto for research, commercial utilization or bio-survey without previous approval of the National Biodiversity Authority."
        ),
        "legal_implication": (
            "Strict prior approval requirement (Form I) before collecting or accessing any Indian Ayurvedic herb or traditional "
            "knowledge. Even 1% foreign equity in an Indian company triggers Section 3 status."
        ),
        "official_url": "https://nbaindia.org"
    },
    {
        "id": "BDA_SEC6",
        "statute": "Biological Diversity Act, 2002",
        "section": "Section 6",
        "year": "2002 (amended 2023)",
        "authority_type": "Statute (Parliament of India)",
        "authority_weight": 20,
        "currency_date": "2024-01-01",
        "is_active": True,
        "jurisdiction": "India",
        "category_tags": ["All Categories", "Foreign Entity Track", "Indian Commercial Track"],
        "title": "Application for Intellectual Property Rights: NBA Approval Mandatory",
        "content": (
            "Section 6 mandates that no person shall apply for any intellectual property right, in or outside India, for any "
            "invention based on any research or information on a biological resource obtained from India without obtaining the "
            "previous approval of the National Biodiversity Authority. Under the 2023 Amendment, approval must be obtained prior to the grant of patent in India, and before filing patent outside India."
        ),
        "legal_implication": (
            "Mandatory Form III application to NBA. Failure to obtain approval invites penalty and rejection of patent under "
            "Section 10(4) of Patents Act. Crucial distinction: For foreign filings, approval is needed BEFORE filing."
        ),
        "official_url": "https://nbaindia.org"
    },
    {
        "id": "BDA_SEC7",
        "statute": "Biological Diversity Act, 2002",
        "section": "Section 7",
        "year": "2002 (amended 2023)",
        "authority_type": "Statute (Parliament of India)",
        "authority_weight": 20,
        "currency_date": "2024-01-01",
        "is_active": True,
        "jurisdiction": "India",
        "category_tags": ["Indian Commercial Track"],
        "title": "Prior Intimation to State Biodiversity Board for Indian Commercial Entities",
        "content": (
            "Section 7 provides that Indian citizens or bodies corporate registered in India shall give prior intimation to the "
            "State Biodiversity Board concerned in the prescribed manner before obtaining biological resources for commercial utilization."
        ),
        "legal_implication": (
            "Indian MSMEs and startups must intimate the SBB of the state where bioresources are sourced. SBB may regulate or "
            "levy benefit-sharing fees in accordance with NBA ABS guidelines."
        ),
        "official_url": "https://nbaindia.org"
    },
    {
        "id": "BDA_2023_EXEMPTIONS",
        "statute": "Biological Diversity (Amendment) Act, 2023",
        "section": "Sections 3(2), 7 Proviso & 40",
        "year": "2023",
        "authority_type": "Statute Amendment",
        "authority_weight": 20,
        "currency_date": "2024-01-01",
        "is_active": True,
        "jurisdiction": "India",
        "category_tags": ["Exempted AYUSH Track", "Cultivator Track"],
        "title": "Statutory Exemptions for AYUSH Practitioners and Cultivators",
        "content": (
            "The 2023 Amendment explicitly exempts: (1) Local people and communities of the area, including growers and "
            "cultivators of biodiversity; (2) Vaids, hakims and registered AYUSH practitioners practicing indigenous medicine; "
            "(3) Codified traditional knowledge; and (4) Cultivated medicinal plants (subject to certificate of origin) from "
            "intimation to SBB and ABS benefit-sharing obligations for commercial utilization."
        ),
        "legal_implication": (
            "Registered Ayurvedic practitioners and farmers cultivating medicinal herbs are exempt from ABS levies, removing "
            "fear of prosecution and fostering community commercialization."
        ),
        "official_url": "https://nbaindia.org"
    },
    {
        "id": "BDA_RULES_2024",
        "statute": "Biological Diversity Rules, 2024",
        "section": "ABS Guidelines & Benefit Sharing Schedules",
        "year": "2024",
        "authority_type": "Central Government Rules",
        "authority_weight": 18,
        "currency_date": "2024-04-01",
        "is_active": True,
        "jurisdiction": "India",
        "category_tags": ["All Categories", "ABS"],
        "title": "Operationalization of 2024 ABS Rules & Digital Filing",
        "content": (
            "Biological Diversity Rules 2024 prescribe tiered benefit-sharing percentages (0.1% to 0.5% of ex-factory sale price) "
            "for commercial utilization of wild biological resources, electronic application via NBA portal, and fast-track processing for IPR permissions."
        ),
        "legal_implication": (
            "Clear predictable financial exposure for commercial Ayurvedic manufacturers utilizing wild-harvested herbs."
        ),
        "official_url": "https://nbaindia.org"
    },
    {
        "id": "NDCT_2W",
        "statute": "New Drugs and Clinical Trials Rules, 2019",
        "section": "Rule 2(w)",
        "year": "2019",
        "authority_type": "Central Government Rules",
        "authority_weight": 18,
        "currency_date": "2024-01-01",
        "is_active": True,
        "jurisdiction": "India",
        "category_tags": ["New Drug / Non-Classical Ayurvedic Drug"],
        "title": "Definition of New Drug",
        "content": (
            "Rule 2(w) defines 'new drug' to include a drug, including active pharmaceutical ingredient or phytopharmaceutical "
            "drug, which has not been used in the country to any significant extent; or a drug approved with certain claims which "
            "is now proposed to be marketed with modified or new claims including indication, route of administration, dosage form."
        ),
        "legal_implication": (
            "When an Ayurvedic innovator discovers a new therapeutic indication or designs a novel delivery system for an "
            "Ayurvedic ingredient, it moves from classical ASU status into the 'New Drug' framework under CDSCO, requiring "
            "investigational clinical trials, but simultaneously acquiring strong patentability potential."
        ),
        "official_url": "https://cdsco.gov.in"
    },
    {
        "id": "NDCT_2AA",
        "statute": "New Drugs and Clinical Trials Rules, 2019",
        "section": "Rule 2(aa)",
        "year": "2019",
        "authority_type": "Central Government Rules",
        "authority_weight": 18,
        "currency_date": "2024-01-01",
        "is_active": True,
        "jurisdiction": "India",
        "category_tags": ["Phytopharmaceutical Drug"],
        "title": "Definition of Phytopharmaceutical Drug",
        "content": (
            "Rule 2(aa) defines 'phytopharmaceutical drug' as a drug of purified and standardized fraction, assessed "
            "qualitatively and quantitatively with defined minimum four bioactive or analytical marker compounds of an "
            "extract of a medicinal plant or its part, for internal or external use on human beings or animals for diagnosis, "
            "treatment, mitigation or prevention of any disease or disorder, but does not include administration by parenteral route."
        ),
        "legal_implication": (
            "Phytopharmaceuticals bridge traditional Ayurveda and modern allopathy. They require botanical authentication, "
            "fingerprint profiling (≥4 markers), animal toxicity, and clinical trials. High patentability potential for extraction process and purified fraction composition."
        ),
        "official_url": "https://cdsco.gov.in"
    },
    {
        "id": "FSSAI_AAHAR_2022",
        "statute": "Food Safety and Standards (Ayurveda Aahar) Regulations, 2022",
        "section": "Regulations 3, 4, 6 and Schedule A",
        "year": "2022",
        "authority_type": "Statutory Authority Regulations",
        "authority_weight": 17,
        "currency_date": "2024-01-01",
        "is_active": True,
        "jurisdiction": "India",
        "category_tags": ["Ayurveda-Aahar / Nutraceutical"],
        "title": "Ayurveda Aahar Standards and Regulatory Boundary",
        "content": (
            "Defines 'Ayurveda Aahar' as food prepared in accordance with the recipes or books/processes specified in the "
            "Schedule A authoritative Ayurvedic texts. Prohibits claiming treatment, prevention or cure of any specific human disease. "
            "Mandates the official Ayurveda Aahar logo on packaging. Cannot contain added synthetic vitamins/minerals without authorization."
        ),
        "legal_implication": (
            "Dietary supplements and herbal teas claiming general wellness must register under FSSAI Ayurveda Aahar rather than "
            "seeking ASU drug manufacturing licenses. IP protection is primarily through trademarks and trade secrets."
        ),
        "official_url": "https://www.fssai.gov.in"
    },
    {
        "id": "DMRA_1954",
        "statute": "Drugs and Magic Remedies (Objectionable Advertisements) Act, 1954",
        "section": "Sections 3 & 4 and Schedule",
        "year": "1954 (as amended)",
        "authority_type": "Statute (Parliament of India)",
        "authority_weight": 20,
        "currency_date": "2024-01-01",
        "is_active": True,
        "jurisdiction": "India",
        "category_tags": ["All Categories", "Patent or Proprietary Ayurvedic Medicine (P&P)", "Ayurveda-Aahar / Nutraceutical"],
        "title": "Prohibition of Misleading & Objectionable Medical Advertisements",
        "content": (
            "Prohibits advertising any drug (including Ayurvedic formulations) suggesting that it can cure or prevent 54 scheduled "
            "conditions, including cancer, diabetes, blindness, epilepsy, sexual impotence, obesity, and hypertension."
        ),
        "legal_implication": (
            "Violating this Act is a cognizable criminal offense. IP claims and commercial branding cannot incorporate prohibited "
            "cure claims on packaging, marketing or trademarks."
        ),
        "official_url": "https://www.indiacode.nic.in"
    },
    {
        "id": "WIPO_GRATK_2024",
        "statute": "WIPO Treaty on Intellectual Property, Genetic Resources and Associated Traditional Knowledge",
        "section": "Articles 3, 4, 5 & 17",
        "year": "2024 (Adopted May 24, 2024)",
        "authority_type": "International Treaty (WIPO)",
        "authority_weight": 18,
        "currency_date": "2024-05-24",
        "is_active": False,  # Adopted, but awaiting 15 ratifications to enter into force!
        "jurisdiction": "International",
        "category_tags": ["All Categories", "International"],
        "title": "WIPO GRATK Treaty - Mandatory Patent Disclosure of Genetic Resources",
        "content": (
            "Adopted by consensus at WIPO Diplomatic Conference on May 24, 2024. Article 3 establishes a mandatory disclosure "
            "requirement: patent applicants worldwide must disclose the country of origin of genetic resources if the claimed "
            "invention is materially/directly based on genetic resources; and if based on associated TK, disclose the indigenous "
            "peoples or local community who provided it. Article 17 specifies it enters into force 3 months after 15 contracting parties deposit instruments of ratification."
        ),
        "legal_implication": (
            "Historic landmark treaty vindicating India's two-decade crusade against bio-piracy. Innovators filing abroad must "
            "be prepared for mandatory genetic resource origin disclosures once the treaty enters into force."
        ),
        "official_url": "https://www.wipo.int/gratk/en/"
    },
    {
        "id": "CBD_NAGOYA",
        "statute": "Nagoya Protocol on Access and Benefit-Sharing to the CBD",
        "section": "Articles 5, 6, 7 & 15",
        "year": "2010 (in force 2014)",
        "authority_type": "Multilateral Treaty",
        "authority_weight": 18,
        "currency_date": "2024-01-01",
        "is_active": True,
        "jurisdiction": "International",
        "category_tags": ["All Categories", "ABS", "International"],
        "title": "Nagoya Protocol on Fair and Equitable Benefit Sharing",
        "content": (
            "Provides transparent legal framework for the effective implementation of one of the three objectives of the CBD: "
            "the fair and equitable sharing of benefits arising out of the utilization of genetic resources. Mandates Prior Informed "
            "Consent (PIC) and Mutually Agreed Terms (MAT), with user country compliance check points."
        ),
        "legal_implication": (
            "International users of Indian Ayurvedic herbs must comply with ABS checkpoints in treaty member nations (EU, Japan, "
            "UK), presenting Internationally Recognized Certificates of Compliance (IRCC) generated via India NBA."
        ),
        "official_url": "https://www.cbd.int/abs/"
    },
    {
        "id": "TRIPS_27_3",
        "statute": "WTO TRIPS Agreement",
        "section": "Article 27.3(b)",
        "year": "1994",
        "authority_type": "International Multilateral Treaty",
        "authority_weight": 18,
        "currency_date": "2024-01-01",
        "is_active": True,
        "jurisdiction": "International",
        "category_tags": ["All Categories", "International"],
        "title": "Patentable Subject Matter & Biological Exclusions",
        "content": (
            "Article 27.3(b) permits Members to exclude from patentability plants and animals other than micro-organisms, and "
            "essentially biological processes for the production of plants or animals. However, Members must provide for the "
            "protection of plant varieties either by patents or by an effective sui generis system (e.g. PPV&FR Act in India)."
        ),
        "legal_implication": (
            "Raw Ayurvedic medicinal plant cultivars are protected via Plant Variety Protection (PPV&FR Act 2001), while isolated "
            "micro-organisms may be patented under Article 27.3(b) and the Budapest Treaty."
        ),
        "official_url": "https://www.wto.org/english/tratop_e/trips_e/trips_e.htm"
    },
    {
        "id": "PCT_FRAMEWORK",
        "statute": "Patent Cooperation Treaty (PCT)",
        "section": "Articles 11, 22 & 39",
        "year": "1970 (amended)",
        "authority_type": "International Treaty (WIPO)",
        "authority_weight": 18,
        "currency_date": "2024-01-01",
        "is_active": True,
        "jurisdiction": "International",
        "category_tags": ["New Drug / Non-Classical Ayurvedic Drug", "Phytopharmaceutical Drug", "International"],
        "title": "PCT International Patent Filing System",
        "content": (
            "Allows applicants to file a single international patent application seeking patent protection in over 155 PCT "
            "contracting states. Establishes International Searching Authority (ISA) search reports and written opinions, followed "
            "by national phase entry within 30/31 months from priority date."
        ),
        "legal_implication": (
            "Ayurvedic innovators with patentable P&P or Phytopharmaceutical inventions should use PCT for international filings. "
            "Crucially, NBA Section 6 approval must be granted BEFORE international filing if priority is first claimed outside India."
        ),
        "official_url": "https://www.wipo.int/pct/en/"
    },
    {
        "id": "MADRID_SYSTEM",
        "statute": "Madrid Agreement and Madrid Protocol",
        "section": "Articles 1 to 9",
        "year": "1989 (India acceded 2013)",
        "authority_type": "International Treaty (WIPO)",
        "authority_weight": 17,
        "currency_date": "2024-01-01",
        "is_active": True,
        "jurisdiction": "International",
        "category_tags": ["All Categories", "International"],
        "title": "Madrid System for International Registration of Marks",
        "content": (
            "Enables trademark owners to protect a brand in over 130 countries by filing a single international application "
            "with the applicant's national or regional IP office (Trade Marks Registry of IP India). India is a full member."
        ),
        "legal_implication": (
            "Crucial for Ayurvedic brands (e.g. Dabur, Himalaya, Patanjali, Kottakkal) seeking export brand protection in Nice "
            "Class 5 (Pharmaceuticals) and Class 3 (Cosmetics) efficiently across multiple countries."
        ),
        "official_url": "https://www.wipo.int/madrid/en/"
    },
    {
        "id": "HAGUE_STATUS",
        "statute": "Hague Agreement Concerning the International Registration of Industrial Designs",
        "section": "Geneva Act (1999) - India Status Check",
        "year": "1999",
        "authority_type": "International Treaty (WIPO) - Non-member status",
        "authority_weight": 17,
        "currency_date": "2024-01-01",
        "is_active": False,  # India is NOT a member party!
        "jurisdiction": "International",
        "category_tags": ["All Categories", "International"],
        "title": "Hague Agreement - India Non-Membership Status",
        "content": (
            "The Hague Agreement governs international design registration. CRITICAL FACTUAL DISTINCTION: India is NOT "
            "a contracting party to the Hague Agreement (unlike Madrid for trademarks and PCT for patents). Consequently, "
            "applicants cannot designate India via a Hague international application, nor can Indian applicants use the "
            "Hague system directly without qualifying through a presence in a member state. Novel bottle shapes and packaging "
            "must be registered directly under the Indian Designs Act, 2000."
        ),
        "legal_implication": (
            "Prevents fatal procedural error: Ayurvedic packaging/bottle designs in India must be filed locally under the "
            "Designs Act, 2000 with the Kolkata Patent Office / IPO."
        ),
        "official_url": "https://www.wipo.int/hague/en/"
    },
    {
        "id": "BUDAPEST_TREATY",
        "statute": "Budapest Treaty on the Deposit of Microorganisms",
        "section": "Articles 3 & 7",
        "year": "1977 (India acceded 2001)",
        "authority_type": "International Treaty (WIPO)",
        "authority_weight": 17,
        "currency_date": "2024-01-01",
        "is_active": True,
        "jurisdiction": "International",
        "category_tags": ["All Categories", "International"],
        "title": "Budapest Treaty on Microbial Deposits for Patent Procedures",
        "content": (
            "Requires contracting states to recognize the deposit of a microorganism with an International Depositary Authority "
            "(IDA) for patent disclosure purposes. In India, the Microbial Type Culture Collection and Gene Bank (MTCC) at CSIR-IMTECH "
            "Chandigarh and NCMR Pune serve as authorized IDAs."
        ),
        "legal_implication": (
            "Ayurvedic fermented preparations (Asavas and Arishtas) utilizing specific probiotic or yeast ferment strains require "
            "deposit with an IDA if patent claims involve microbial strains or fermentation processes."
        ),
        "official_url": "https://www.wipo.int/treaties/en/registration/budapest/"
    },
    {
        "id": "US_FDA_BOTANICAL",
        "statute": "US FDA Guidance for Industry: Botanical Drug Development",
        "section": "21 CFR Part 312 & Part 314 Guidance",
        "year": "2016",
        "authority_type": "Foreign Regulatory Guidance (US FDA)",
        "authority_weight": 14,
        "currency_date": "2024-01-01",
        "is_active": True,
        "jurisdiction": "International",
        "category_tags": ["New Drug / Non-Classical Ayurvedic Drug", "Phytopharmaceutical Drug", "International"],
        "title": "US FDA Botanical Drug Guidance for Export Market",
        "content": (
            "Outlines requirements for submitting Investigational New Drug (IND) applications and New Drug Applications (NDA) "
            "for complex botanical mixtures. Unlike synthetic drugs requiring single active chemical entities, botanical drugs "
            "rely on batch-to-batch consistency, chemical fingerprinting, raw material controls (GAP), and clinical trials."
        ),
        "legal_implication": (
            "Essential export pathway for Ayurvedic innovators targeting the US market as prescription therapeutics rather "
            "than low-margin dietary supplements (DSHEA)."
        ),
        "official_url": "https://www.fda.gov/regulatory-information/search-fda-guidance-documents/botanical-drug-development-guidance-industry"
    },
    {
        "id": "EU_THMPD",
        "statute": "Directive 2004/24/EC (Traditional Herbal Medicinal Products Directive)",
        "section": "Articles 16a to 16i",
        "year": "2004",
        "authority_type": "European Union Directive",
        "authority_weight": 14,
        "currency_date": "2024-01-01",
        "is_active": True,
        "jurisdiction": "International",
        "category_tags": ["Classical / Generic Ayurvedic Medicine", "Patent or Proprietary Ayurvedic Medicine (P&P)", "International"],
        "title": "EU THMPD Simplified Registration for Traditional Herbal Products",
        "content": (
            "Provides a simplified registration procedure for traditional herbal medicinal products. Crucial hurdle: Applicant "
            "must prove at least 30 years of continuous medicinal use, including at least 15 years within the European Union. "
            "Non-therapeutic herbal teas may alternatively enter under EU Food Supplements Directive 2002/46/EC."
        ),
        "legal_implication": (
            "The 15-year EU usage requirement remains a major market-access barrier for Ayurvedic classical medicines entering "
            "the EU as medicines, necessitating strategic entry through European partner clinical networks or food supplement tracks."
        ),
        "official_url": "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32004L0024"
    },
    {
        "id": "TKDL_TKRC",
        "statute": "Traditional Knowledge Digital Library (TKDL) Specifications",
        "section": "Traditional Knowledge Resource Classification (TKRC) - Section A61K",
        "year": "2001 (expanded continuously)",
        "authority_type": "Indian State Repository / Prior-Art Standard",
        "authority_weight": 16,
        "currency_date": "2024-01-01",
        "is_active": True,
        "jurisdiction": "India",
        "category_tags": ["Classical / Generic Ayurvedic Medicine", "All Categories"],
        "title": "TKDL Prior-Art Search & TKRC Classification Structure",
        "content": (
            "Joint initiative of CSIR and Ministry of Ayush. Digitizes classical texts in 5 international languages (English, "
            "German, French, Japanese, Spanish) structured under TKRC, mapped to IPC Section A61K. TKDL has pre-grant access "
            "agreements with USPTO, EPO, JPO, CIPO, and UKIPO, enabling patent examiners to block invalid biopiracy claims."
        ),
        "legal_implication": (
            "Forms the definitive global prior-art barrier protecting codified Indian traditional medicine against illegitimate "
            "foreign and domestic patent monopolies."
        ),
        "official_url": "https://www.tkdl.res.in"
    }
]
