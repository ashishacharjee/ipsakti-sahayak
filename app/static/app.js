/**
 * IP-SAKTI Sahayak - Frontend Application Logic
 * Problem Statement 26045 - SIH 2026
 * Team: Coders of GNIT
 */

let currentLanguage = 'en';
let lastGuidanceResult = null;
let lastReviewBrief = null;
let allCorpusProvisions = [];

document.addEventListener('DOMContentLoaded', () => {
    // Initial run on sample formulation
    handleRunAssessment();
    loadCorpusData();
});

// Set Language (English / Hindi)
async function setLanguage(lang) {
    currentLanguage = lang;
    document.getElementById('btn-lang-en').classList.toggle('active', lang === 'en');
    document.getElementById('btn-lang-hi').classList.toggle('active', lang === 'hi');

    try {
        const res = await fetch(`/api/i18n/${lang}`);
        if (res.ok) {
            const strings = await res.json();
            document.getElementById('lbl-title').innerHTML = `${strings.title} <span class="badge-sih">SIH 2026 • PS 26045</span>`;
            document.getElementById('lbl-motto').textContent = `“${strings.motto}”`;
            document.getElementById('lbl-banner-text').textContent = strings.disclaimer_banner;
            document.getElementById('lbl-wizard-title').textContent = strings.classification_wizard;
            document.getElementById('lbl-step1-q').textContent = strings.step_1_q;
            document.getElementById('lbl-step2-q').textContent = strings.step_2_q;
            document.getElementById('lbl-step3-q').textContent = strings.step_3_q;
            document.getElementById('lbl-step4-q').textContent = strings.step_4_q;
            document.getElementById('lbl-abs-title').textContent = strings.abs_gate_title;
            document.getElementById('lbl-applicant-type').textContent = strings.applicant_type_label;
            document.getElementById('lbl-btn-classify').textContent = strings.btn_classify;
            document.getElementById('lbl-btn-reset').textContent = strings.btn_reset;
            document.getElementById('tab-india').textContent = strings.jurisdiction_india;
            document.getElementById('tab-intl').textContent = strings.jurisdiction_intl;
        }
    } catch (e) {
        console.error('Error fetching localization:', e);
    }
}

// Run Deterministic Assessment
async function handleRunAssessment(e) {
    if (e) e.preventDefault();

    const productName = document.getElementById('product-name').value.trim() || 'Ayurvedic Formulation';
    const ingredientsRaw = document.getElementById('ingredients-input').value.trim();
    const ingredients = ingredientsRaw ? ingredientsRaw.split(',').map(s => s.trim()) : [];

    const intendedUse = document.getElementById('step-intended-use').value;
    const formulationBasis = document.getElementById('step-formulation-basis').value;
    const claimType = document.getElementById('step-claim-type').value;
    const extractionClinical = document.getElementById('step-extraction-clinical').value;

    const applicantType = document.getElementById('abs-applicant-type').value;
    const filingIndia = document.getElementById('chk-ipr-india').checked;
    const filingAbroad = document.getElementById('chk-ipr-abroad').checked;

    const payload = {
        classification: {
            product_name: productName,
            ingredients: ingredients,
            intended_use: intendedUse,
            formulation_basis: formulationBasis,
            claim_type: claimType,
            extraction_clinical: extractionClinical
        },
        abs_check: {
            applicant_type: applicantType,
            is_commercial_utilization: true,
            filing_ipr_in_india: filingIndia,
            filing_ipr_outside_india: filingAbroad
        },
        jurisdiction: 'dual'
    };

    const runBtn = document.getElementById('btn-run');
    runBtn.disabled = true;
    runBtn.textContent = 'Analyzing...';

    try {
        const response = await fetch('/api/guidance', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
        });

        if (!response.ok) {
            throw new Error(`Server returned ${response.status}`);
        }

        const data = await response.json();
        lastGuidanceResult = data;
        renderGuidanceResults(data, payload);
    } catch (err) {
        console.error('Failed to run assessment:', err);
        alert('Assessment error: ' + err.message);
    } finally {
        runBtn.disabled = false;
        runBtn.innerHTML = '⚡ <span id="lbl-btn-classify">Run Deterministic Assessment</span>';
    }
}

// Render Results to UI
function renderGuidanceResults(data, requestPayload) {
    const score = data.evidence_score;
    const national = data.national_guidance;
    const intl = data.international_guidance;

    // 1. Evidence Strength Gauge
    const scoreNum = document.getElementById('score-number');
    const scoreBadge = document.getElementById('score-level-badge');
    const scoreCircle = document.getElementById('score-circle').parentElement;

    scoreNum.textContent = Math.round(score.total_score);

    // Color code and gradient
    let badgeClass = 'badge-high';
    let gradientColor = '#10b981';

    if (score.confidence_level.includes('HIGH')) {
        badgeClass = 'badge-high';
        gradientColor = '#10b981';
        scoreBadge.textContent = 'HIGH CONFIDENCE (≥ 75/100)';
    } else if (score.confidence_level.includes('MODERATE')) {
        badgeClass = 'badge-mod';
        gradientColor = '#f59e0b';
        scoreBadge.textContent = 'MODERATE (DEFERS TO HUMAN)';
    } else {
        badgeClass = 'badge-low';
        gradientColor = '#ef4444';
        scoreBadge.textContent = 'LOW (SAFE ABSTENTION)';
    }

    scoreBadge.className = `score-level-badge ${badgeClass}`;
    const deg = Math.round((score.total_score / 100) * 360);
    scoreCircle.style.background = `conic-gradient(${gradientColor} 0deg ${deg}deg, #e2e8f0 ${deg}deg 360deg)`;

    // Breakdown
    document.getElementById('val-agreement').textContent = `${score.source_agreement}/35`;
    document.getElementById('val-authority').textContent = `${score.source_authority}/20`;
    document.getElementById('val-currency').textContent = `${score.currency_score}/20`;
    document.getElementById('val-jurisdiction').textContent = `${score.jurisdiction_match}/15`;
    document.getElementById('val-classification').textContent = `${score.classification_certainty}/10`;

    // 2. Safe Abstention Banner
    const abstentionBanner = document.getElementById('safe-abstention-banner');
    if (data.safe_abstention) {
        abstentionBanner.classList.remove('hidden');
        document.getElementById('abstention-reason-text').textContent = data.abstention_reason || 'Evidence strength is below certainty threshold. Pre-assembled review brief ready for human IP facilitator.';
    } else {
        abstentionBanner.classList.add('hidden');
    }

    // 3. Classification Badge Card
    document.getElementById('res-category-name').textContent = national.classification_category;
    document.getElementById('res-statute-citation').textContent = national.statutory_citation;
    document.getElementById('res-category-summary').textContent = national.ip_strategy;

    // 4. National Pane
    document.getElementById('in-patent-verdict').textContent = national.ip_patentability_assessment;
    
    const barsList = document.getElementById('in-bars-list');
    barsList.innerHTML = '';
    national.statutory_bars_evaluated.forEach(bar => {
        const li = document.createElement('li');
        li.textContent = bar;
        barsList.appendChild(li);
    });

    const absBox = document.getElementById('in-abs-posture');
    const absStatus = national.abs_compliance_status;
    absBox.innerHTML = `
        <strong>${absStatus.applicant_track}</strong><br>
        <span>${absStatus.action_required}</span>
    `;

    const regList = document.getElementById('in-reg-list');
    regList.innerHTML = '';
    national.regulatory_pathway.forEach(req => {
        const li = document.createElement('li');
        li.textContent = req;
        regList.appendChild(li);
    });

    // 5. International Pane
    document.getElementById('intl-gratk-status').textContent = 
        `${intl.wipo_gratk_treaty_status.treaty_name} — ${intl.wipo_gratk_treaty_status.status}. ${intl.wipo_gratk_treaty_status.impact}`;
    
    document.getElementById('intl-hague-status').textContent = 
        intl.trademark_and_design.hague_agreement_alert;

    document.getElementById('intl-pct-status').textContent = 
        `${intl.patent_filing_channels.pct_system} ${intl.patent_filing_channels.nba_foreign_filing_rule}`;

    document.getElementById('intl-export-status').textContent = 
        `USA: ${intl.export_market_regulatory_access.united_states} | EU: ${intl.export_market_regulatory_access.european_union}`;

    // 6. Cited Authorities Chips
    const chipsContainer = document.getElementById('sources-chips-container');
    chipsContainer.innerHTML = '';
    data.cited_provisions.forEach(prov => {
        const chip = document.createElement('span');
        chip.className = 'source-chip';
        chip.title = `${prov.statute_name} - ${prov.key_excerpt.slice(0, 80)}...`;
        chip.textContent = `${prov.section_or_rule} (${prov.statute_name.split(',')[0]})`;
        chipsContainer.appendChild(chip);
    });

    // Auto-update TKDL input box
    document.getElementById('tkdl-input-terms').value = `${requestPayload.classification.product_name}, ${requestPayload.classification.ingredients.join(', ')}`;
}

// Switch Jurisdiction Tabs
function switchJurisdictionTab(tab) {
    document.getElementById('tab-india').classList.toggle('active', tab === 'india');
    document.getElementById('tab-intl').classList.toggle('active', tab === 'intl');
    document.getElementById('tab-both').classList.toggle('active', tab === 'both');

    const paneIn = document.getElementById('pane-india');
    const paneIntl = document.getElementById('pane-intl');

    if (tab === 'india') {
        paneIn.classList.remove('hidden');
        paneIntl.classList.add('hidden');
    } else if (tab === 'intl') {
        paneIn.classList.add('hidden');
        paneIntl.classList.remove('hidden');
    } else {
        paneIn.classList.remove('hidden');
        paneIntl.classList.remove('hidden');
    }
}

// Reset Form
function resetForm() {
    document.getElementById('assessment-form').reset();
    handleRunAssessment();
}

// TKDL Search Bridge Modal
function openTKDLModal() {
    document.getElementById('modal-tkdl').classList.remove('hidden');
    runTKDLBuilder();
}

async function runTKDLBuilder() {
    const rawTerms = document.getElementById('tkdl-input-terms').value.trim();
    const terms = rawTerms ? rawTerms.split(',').map(s => s.trim()) : [];
    const productName = terms[0] || 'Ayurvedic Compound';

    try {
        const res = await fetch('/api/tkdl-query', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                formulation_name: productName,
                sanskrit_or_botanical_terms: terms,
                therapeutic_target: 'General / Synergistic'
            })
        });
        if (res.ok) {
            const data = await res.json();
            const botList = data.identified_botanicals.map(b => `${b.botanical_name} (${b.sanskrit_name})`).join(', ') || 'General ASU Botanicals';
            document.getElementById('tkdl-botanicals-list').textContent = botList;
            document.getElementById('tkdl-codes-list').textContent = `${data.tkrc_codes.join(', ')} • IPC: ${data.ipc_classes.join(', ')}`;
            document.getElementById('tkdl-query-string').textContent = data.structured_search_query;
            document.getElementById('tkdl-bridge-notice').textContent = data.disclaimer;
        }
    } catch (e) {
        console.error('TKDL error:', e);
    }
}

function copyQueryToClipboard() {
    const query = document.getElementById('tkdl-query-string').textContent;
    navigator.clipboard.writeText(query).then(() => {
        alert('Prior-art boolean query copied to clipboard for InPASS / Patentscope!');
    }).catch(err => {
        console.error('Clipboard copy failed:', err);
    });
}

// Facilitator Review Brief Modal
async function openReviewBriefModal() {
    document.getElementById('modal-brief').classList.remove('hidden');

    if (!lastGuidanceResult) return;

    const payload = {
        classification: {
            category: lastGuidanceResult.national_guidance.classification_category,
            category_id: lastGuidanceResult.national_guidance.classification_category.includes('Classical') ? 'CLASSICAL' : 'PATENT_PROPRIETARY',
            governing_statute: lastGuidanceResult.national_guidance.governing_statute,
            statutory_citation: lastGuidanceResult.national_guidance.statutory_citation,
            description: lastGuidanceResult.national_guidance.ip_strategy,
            ip_posture: lastGuidanceResult.national_guidance.ip_strategy,
            patentability_verdict: lastGuidanceResult.national_guidance.ip_patentability_assessment,
            abs_posture: lastGuidanceResult.national_guidance.abs_compliance_status.applicant_track,
            regulatory_requirements: lastGuidanceResult.national_guidance.regulatory_pathway,
            potential_hurdles: lastGuidanceResult.national_guidance.critical_traps || [],
            rule_path_traversed: ["Rule path verified"]
        },
        abs_result: {
            applicant_type: "Indian Commercial Entity / Company / LLP (Sec 7 BDA)",
            applicant_track: lastGuidanceResult.national_guidance.abs_compliance_status.applicant_track,
            requires_nba_approval: true,
            requires_sbb_intimation: true,
            is_exempted: lastGuidanceResult.national_guidance.abs_compliance_status.is_exempted,
            exemption_basis: lastGuidanceResult.national_guidance.abs_compliance_status.exemption_basis,
            statutory_provisions: ["Biological Diversity Act"],
            mandated_forms: lastGuidanceResult.national_guidance.abs_compliance_status.mandated_forms || ["Form I"],
            benefit_sharing_applicable: true,
            guidance_notes: "Evaluated under 2024 ABS rules.",
            penal_provisions: lastGuidanceResult.national_guidance.abs_compliance_status.penalties
        },
        evidence_score: lastGuidanceResult.evidence_score,
        formulation_name: document.getElementById('product-name').value
    };

    try {
        const res = await fetch('/api/review-brief', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
        });
        if (res.ok) {
            const brief = await res.json();
            lastReviewBrief = brief;
            document.getElementById('brief-modal-id').textContent = brief.brief_id;
            document.getElementById('brief-modal-time').textContent = brief.generated_at;
            document.getElementById('brief-case-summary').textContent = brief.case_summary;
            document.getElementById('brief-abs-summary').textContent = `${brief.abs_summary.track}: ${brief.abs_summary.notes}`;

            const qList = document.getElementById('brief-open-questions-list');
            qList.innerHTML = '';
            brief.open_questions_for_human.forEach(q => {
                const li = document.createElement('li');
                li.textContent = q;
                qList.appendChild(li);
            });
        }
    } catch (e) {
        console.error('Failed to generate review brief:', e);
    }
}

function downloadReviewBrief() {
    if (!lastReviewBrief) {
        alert('Review brief not ready.');
        return;
    }
    const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(lastReviewBrief, null, 2));
    const downloadAnchor = document.createElement('a');
    downloadAnchor.setAttribute("href", dataStr);
    downloadAnchor.setAttribute("download", `${lastReviewBrief.brief_id}.json`);
    document.body.appendChild(downloadAnchor);
    downloadAnchor.click();
    downloadAnchor.remove();
}

// Corpus Explorer Modal
async function loadCorpusData() {
    try {
        const res = await fetch('/api/corpus');
        if (res.ok) {
            allCorpusProvisions = await res.json();
            renderCorpusList(allCorpusProvisions);
        }
    } catch (e) {
        console.error('Failed to load corpus:', e);
    }
}

function openCorpusModal() {
    document.getElementById('modal-corpus').classList.remove('hidden');
    renderCorpusList(allCorpusProvisions);
}

function filterCorpusProvisions() {
    const q = document.getElementById('corpus-search-input').value.toLowerCase();
    const jur = document.getElementById('corpus-jurisdiction-filter').value;

    const filtered = allCorpusProvisions.filter(p => {
        const matchesQuery = !q || 
            p.title.toLowerCase().includes(q) || 
            p.statute.toLowerCase().includes(q) || 
            p.section.toLowerCase().includes(q) || 
            p.content.toLowerCase().includes(q);
        
        const matchesJur = jur === 'all' || p.jurisdiction.toLowerCase() === jur.toLowerCase();
        return matchesQuery && matchesJur;
    });

    renderCorpusList(filtered);
}

function renderCorpusList(provisions) {
    const container = document.getElementById('corpus-items-list');
    container.innerHTML = '';

    if (provisions.length === 0) {
        container.innerHTML = '<p class="modal-intro">No statutory provisions matching filter criteria.</p>';
        return;
    }

    provisions.forEach(p => {
        const item = document.createElement('div');
        item.className = 'corpus-item';
        item.innerHTML = `
            <div class="corpus-item-header">
                <span class="corpus-statute">${p.statute} — ${p.section}</span>
                <span class="pill ${p.jurisdiction === 'India' ? 'pill-green' : 'pill-gold'}">${p.jurisdiction} • Weight: ${p.authority_weight}</span>
            </div>
            <div class="corpus-excerpt"><strong>${p.title}:</strong> ${p.content}</div>
            <div class="corpus-note"><strong>Regulatory Implication:</strong> ${p.legal_implication}</div>
            <div style="margin-top: 6px;">
                <a href="${p.official_url}" target="_blank" rel="noopener noreferrer" style="color: #047857; font-size: 11px; text-decoration: none; font-weight: 600;">
                    🔗 Official Source Record →
                </a>
            </div>
        `;
        container.appendChild(item);
    });
}

// Modal Helpers
function closeModal(id) {
    document.getElementById(id).classList.add('hidden');
}
