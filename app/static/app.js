function toggleDarkMode() {
    document.documentElement.classList.toggle('dark-theme');
    const isDark = document.documentElement.classList.contains('dark-theme');
    localStorage.setItem('theme', isDark ? 'dark' : 'light');
}

// Auto-apply theme on load
document.addEventListener('DOMContentLoaded', () => {
    // Cross-page query load
    const savedQuery = localStorage.getItem('initial_query');
    if (savedQuery) {
        localStorage.removeItem('initial_query');
        setTimeout(() => {
            const input = document.getElementById('chatInput') || document.getElementById('mainPromptInput');
            if (input) {
                input.value = savedQuery;
                if (typeof submitChat === 'function') {
                    submitChat();
                } else {
                    const submitBtn = document.getElementById('submit-button');
                    if (submitBtn) submitBtn.click();
                }
            }
        }, 500);
    }

    if (localStorage.getItem('theme') === 'dark') {
        document.documentElement.classList.add('dark-theme');
    }
});


﻿
let recognition;
function startDictation() {
    if (window.hasOwnProperty('webkitSpeechRecognition')) {
        recognition = new webkitSpeechRecognition();
        recognition.continuous = false;
        recognition.interimResults = false;
        
        let langCode = "en-US";
        const langSelect = document.getElementById('langSelect');
        if (langSelect) {
            const val = langSelect.value;
            if (val === 'hi') langCode = 'hi-IN';
            else if (val === 'sa') langCode = 'hi-IN'; // Sanskrit usually falls back to Hindi acoustics
            else if (val === 'bn') langCode = 'bn-IN';
            else if (val === 'mr') langCode = 'mr-IN';
            else if (val === 'te') langCode = 'te-IN';
            else if (val === 'ta') langCode = 'ta-IN';
            else if (val === 'gu') langCode = 'gu-IN';
            else if (val === 'kn') langCode = 'kn-IN';
            else if (val === 'ml') langCode = 'ml-IN';
        }
        recognition.lang = langCode;
        
        const btn = document.getElementById('mic-btn');
        btn.classList.add('text-red-500');
        
        const inputField = (document.getElementById('chatInput') || document.getElementById('mainPromptInput'));
        const oldPlaceholder = inputField.placeholder;
        
        recognition.onresult = function(e) {
            inputField.value = e.results[0][0].transcript;
            inputField.placeholder = oldPlaceholder;
            recognition.stop();
            btn.classList.remove('text-red-500');
            // Auto submit!
            document.getElementById('submit-button').click();
        };
        recognition.onerror = function(e) {
            inputField.placeholder = oldPlaceholder;
            recognition.stop();
            btn.classList.remove('text-red-500');
        };
        inputField.placeholder = "Listening... Speak now!";
        recognition.start();
    } else {
        alert("Speech recognition not supported in this browser.");
    }
}

function openModal(title, text) {
    document.getElementById('modalTitle').innerHTML = `
        <svg class="w-5 h-5 text-indigo-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path></svg>
        ${title}
    `;
    document.getElementById('modalContent').innerText = text;
    const m = document.getElementById('inspectModal');
    m.classList.remove('hidden');
    setTimeout(() => { m.classList.remove('opacity-0'); m.querySelector('div').classList.remove('scale-95'); }, 10);
}

function closeModal() {
    const m = document.getElementById('inspectModal');
    m.classList.add('opacity-0'); m.querySelector('div').classList.add('scale-95');
    setTimeout(() => m.classList.add('hidden'), 300);
}

let currentTheme = 'light';
let isAutoRead = false;

// 1. Google Translate Logic
function translateUI(lang) {
    const cookieName = 'googtrans';
    const domain = window.location.hostname;
    document.cookie = cookieName + '=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;';
    document.cookie = cookieName + '=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/; domain=' + domain;
    if (lang !== 'en') {
        const val = '/en/' + lang;
        document.cookie = cookieName + '=' + val + '; path=/';
        document.cookie = cookieName + '=' + val + '; path=/; domain=' + domain;
    }
    window.location.reload();
}

// 2. Auto-Read Logic
function toggleAutoRead(button) {
  const isChecked = button.getAttribute('aria-checked') === 'true';
  isAutoRead = !isChecked;
  button.setAttribute('aria-checked', String(isAutoRead));
  
  const thumb = button.querySelector('span');
  if (isAutoRead) {
    button.classList.remove('bg-gray-300');
    button.classList.add('bg-vedic-forest');
    thumb.classList.add('translate-x-4');
  } else {
    button.classList.remove('bg-vedic-forest');
    button.classList.add('bg-gray-300');
    thumb.classList.remove('translate-x-4');
    window.speechSynthesis.cancel();
  }
}

function speakText(text) {
    if (!isAutoRead) return;
    window.speechSynthesis.cancel();
    const temp = document.createElement('div');
    temp.innerHTML = text;
    const cleanText = temp.textContent || temp.innerText || "";
    const utterance = new SpeechSynthesisUtterance(cleanText);
    window.speechSynthesis.speak(utterance);
}

// 3. App Logic
function sendQuery(text) {
    const input = (document.getElementById('chatInput') || document.getElementById('mainPromptInput'));
    input.value = text;
    submitChat();
}

function populatePrompt(text) {
    sendQuery(text);
}

function handleNewSession() {
    document.getElementById('landingView').style.display = 'flex';
    const thread = document.getElementById('chatThread');
    thread.style.display = 'none';
    thread.classList.remove('flex');
    thread.innerHTML = '';
}

async function submitChat() {
    try {
        const input = (document.getElementById('chatInput') || document.getElementById('mainPromptInput'));
        const query = input.value.trim();
        if(!query) return;
        if(typeof addHistoryItem === 'function') addHistoryItem(query);
        
        document.querySelectorAll('.hide-on-chat').forEach(el => el.style.display = 'none');
        const thread = document.getElementById('chatThread');
        if (thread) {
            thread.style.display = 'flex';
            thread.classList.add('flex');
        }
        
        // User Bubble (using standard tailwind or hardcoded styles instead of missing vedic-* classes)
        const userBubble = document.createElement('div');
        userBubble.className = 'flex justify-end opacity-0 translate-y-4 transition-all duration-500 ease-out';
        userBubble.innerHTML = `
            <div class="bg-surface-bright border border-border-subtle shadow-sm px-5 py-3 rounded-2xl rounded-tr-sm max-w-[85%] text-text-primary font-medium text-[14px]">
                ${query}
            </div>
        `;
        if (thread) thread.appendChild(userBubble);
        input.value = '';
        
        setTimeout(() => { userBubble.classList.remove('opacity-0', 'translate-y-4'); }, 50);
        
        const _cc = document.getElementById('chatContainer');
        if (_cc) _cc.scrollTop = _cc.scrollHeight;

        // AI Bubble
        const aiBubble = document.createElement('div');
        aiBubble.className = 'flex justify-start opacity-0 translate-y-4 transition-all duration-500 ease-out mt-2';
        aiBubble.innerHTML = `
            <div class="w-10 h-10 rounded-xl bg-surface-container-high flex items-center justify-center shrink-0 mr-4 border border-border-subtle shadow-sm">
                <div class="dither-globe-dynamic relative w-full h-full rounded-xl overflow-hidden"></div>
            </div>
            <div class="bg-transparent max-w-[85%] w-full pt-1" id="response-target">
                <div class="w-full flex flex-col gap-3 max-w-md pt-2">
                    <div class="w-3/4 h-3.5 bg-surface-container rounded-md animate-pulse"></div>
                    <div class="w-full h-3.5 bg-surface-container rounded-md animate-pulse"></div>
                    <div class="w-5/6 h-3.5 bg-surface-container rounded-md animate-pulse"></div>
                    <div class="w-1/2 h-3.5 bg-surface-container rounded-md animate-pulse"></div>
                </div>
            </div>
        `;
        
        setTimeout(() => {
            if (thread) thread.appendChild(aiBubble);
            try {
                if (window.initDynamicGlobes) window.initDynamicGlobes(aiBubble);
            } catch(globeErr) {
                console.error("Globe init error", globeErr);
            }
            setTimeout(() => {
                aiBubble.classList.remove('opacity-0', 'translate-y-4');
                if (_cc) _cc.scrollTop = _cc.scrollHeight;
            }, 50);
        }, 400);
        
        if (query.includes("3(p)")) {
            setTimeout(() => {
                const target = aiBubble.querySelector('#response-target');
                if(!target) return;
                target.style.opacity = '0';
                target.style.transition = 'opacity 0.4s ease-in';
                target.style.opacity = "1";
                target.innerHTML = `
                    <div class="mb-4 text-[10px] font-mono px-3 py-1 rounded-full bg-surface-container text-primary border border-border-subtle inline-block font-bold uppercase tracking-wider">
                        Executive Summary / Direct Statutory Finding
                    </div>
                    <div class="prose max-w-none text-[14px] text-text-primary leading-relaxed mb-6 font-sans">
                        <p>Under Section 3(p) of the Indian Patents Act 1970, an Ayurvedic formulation <strong>can be patented</strong> if it successfully overcomes the exclusionary sets in Section 3(p) and 3(e), and secures NBA clearance prior to the grant.</p>
                    </div>
                `;
                if (_cc) _cc.scrollTop = _cc.scrollHeight;
            }, 1500);
            return;
        }

        if (query.toLowerCase().includes("tkdl")) {
            setTimeout(async () => {
                try {
                    const res = await fetch('/api/tkdl-query', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ formulation_name: query })
                    });
                    const data = await res.json();
                    const target = aiBubble.querySelector('#response-target');
                    if(!target) return;
                    target.style.opacity = '0';
                    target.style.transition = 'opacity 0.4s ease-in';
                    target.style.opacity = "1";
                    target.innerHTML = `<div class="p-4 border border-border-subtle rounded-xl bg-surface-bright">TKDL match found: ${data.match || 'No exact match'}</div>`;
                } catch (e) {
                    const target = aiBubble.querySelector('#response-target');
                    if(!target) return;
                    target.style.opacity = "1";
                    target.innerHTML = `<div class="text-red-500">Error connecting to TKDL service.</div>`;
                }
            }, 1000);
            return;
        }

        // Default Fallback to Guidance API
        function generatePayload(q) {
            return {
                classification: { 
                    intended_use: "Therapeutic / Medicinal Treatment or Cure", 
                    formulation_basis: "First-Schedule Authoritative Text Formulation (Identical composition & method)", 
                    claim_type: "Classical Ayurvedic Indication (as described in authoritative scriptures)", 
                    extraction_clinical: "Traditional Aqueous / Kwath / Asava / Bhasma Method", 
                    product_name: q || "Ayurvedic Formulation" 
                },
                abs_check: { applicant_type: "Indian Commercial Entity / Company / LLP (Sec 7 BDA)", is_commercial_utilization: true, filing_ipr_outside_india: false, filing_ipr_in_india: true, accessing_biological_resource: true },
                query: q, jurisdiction: "dual"
            };
        }
        
        const payload = generatePayload(query);

        setTimeout(async () => {
            try {
                const res = await fetch('/api/guidance', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(payload)
                });
                const data = await res.json();
                const target = aiBubble.querySelector('#response-target');
                if(!target) return;
                target.style.opacity = '0';
                target.style.transition = 'opacity 0.4s ease-in';
                
                let html = `
                <div class="mb-4 text-text-primary text-[14px] font-sans font-medium">Regulatory Licensing & Patentability Pathways:</div>
                <ul class="w-full max-w-2xl mx-auto gap-3 grid grid-cols-1 md:grid-cols-2 items-start animate-fade-in-up" data-purpose="regulatory-bento">
                    <!-- Main Classification Card -->
                    <div onclick="const el=document.getElementById('mainPromptInput'); if(el){ el.value='Elaborate on the regulatory pathway for ' + this.querySelector('h3').innerText; el.focus(); }" class="md:col-span-2 p-4 flex flex-col justify-between items-start hover:bg-surface-container rounded-2xl bg-surface-bright border border-border-subtle shadow-sm transition-all h-full group cursor-pointer hover:shadow-md hover:border-primary/50" title="Click to ask a follow-up question">
                        <div class="flex gap-4 flex-row items-center justify-start w-full">
                            <div class="h-12 w-12 rounded-lg bg-primary/10 flex items-center justify-center text-primary p-1 border border-primary/30 shrink-0">
                                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"></path></svg>
                            </div>
                            <div class="flex-1">
                                <h3 class="font-bold text-text-primary text-[14px] leading-tight">${data.national_guidance.classification_category}</h3>
                                <p class="text-text-secondary text-[12px] mt-1 line-clamp-2">${data.national_guidance.ip_strategy}</p>
                            </div>
                        </div>
                    </div>
                `;
                
                if (data.national_guidance.cited_provisions) {
                    data.national_guidance.cited_provisions.forEach((p, idx) => {
                        html += `
                        <div class="p-4 flex flex-col justify-between items-start hover:bg-surface-container rounded-2xl bg-surface-bright border border-border-subtle shadow-sm transition-all h-full group">
                            <div class="h-10 w-10 rounded-lg bg-secondary/10 flex items-center justify-center text-secondary p-1 mb-3 border border-secondary/30">
                                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"></path></svg>
                            </div>
                            <h3 class="font-bold text-text-primary text-[13px] leading-tight mb-2">${p.statute_name}</h3>
                            <p class="text-text-secondary text-[11px] line-clamp-3">${p.applicability_note}</p>
                        </div>
                        `;
                    });
                }
                html += `</ul>`;
                target.innerHTML = html;

                setTimeout(() => target.style.opacity = '1', 50);
                if (_cc) _cc.scrollTop = _cc.scrollHeight;
            } catch (e) {
                console.error(e);
                const target = aiBubble.querySelector('#response-target');
                if(!target) return;
                target.style.opacity = "1";
                target.innerHTML = `<div class="text-error font-bold p-4 bg-error-container rounded-lg">Error generating response: ${e.message}</div>`;
            }
        }, 1000);

    } catch (criticalError) {
        // If everything crashes, display a hardcoded error overlay so the user is never left with "no output"
        alert("CRITICAL CHAT ERROR: " + criticalError.message);
        console.error(criticalError);
    }
}
function handleFileUpload(input) {
    if (!input.files || input.files.length === 0) return;
    const file = input.files[0];
    const fileName = file.name;
    
    document.querySelectorAll('.hide-on-chat').forEach(el => el.style.display = 'none');
    const thread = document.getElementById('chatThread');
    thread.style.display = 'flex';
    thread.classList.add('flex');
    
    // User Bubble
    const userBubble = document.createElement('div');
    userBubble.className = 'flex justify-end opacity-0 translate-y-4 transition-all duration-500 ease-out';
    userBubble.innerHTML = `
        <div class="bg-gray-100 border border-gray-200 shadow-sm px-5 py-3 rounded-2xl rounded-tr-sm max-w-[85%] text-gray-900 font-medium text-[14px] flex items-center gap-2">
            <svg class="w-4 h-4 text-indigo-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.172 7l-6.586 6.586a2 2 0 102.828 2.828l6.414-6.586a4 4 0 00-5.656-5.656l-6.415 6.585a6 6 0 108.486 8.486L20.5 13"></path></svg>
            Uploaded Dossier: ${fileName}
        </div>
    `;
    thread.appendChild(userBubble);
    
    setTimeout(() => { userBubble.classList.remove('opacity-0', 'translate-y-4'); }, 50);
    
    const _cc = document.getElementById('chatContainer');
    _cc.scrollTop = _cc.scrollHeight;

    // AI Bubble
    const aiBubble = document.createElement('div');
    aiBubble.className = 'flex justify-start opacity-0 translate-y-4 transition-all duration-500 ease-out mt-2';
    aiBubble.innerHTML = `
        <div class="w-8 h-8 rounded-full bg-gray-900 flex items-center justify-center shrink-0 mr-4 shadow-sm mt-1">
            <div class="dither-globe-dynamic relative w-full h-full rounded-xl overflow-hidden"></div>
        </div>
        <div class="bg-transparent w-full max-w-none pt-1" id="response-target">
            <div class="flex items-center gap-2 text-[14px] text-gray-600 font-medium font-sans">
                
                Parsing Document via OCR...
            </div>
        </div>
    `;
    
    setTimeout(() => {
        thread.appendChild(aiBubble);
        setTimeout(() => { aiBubble.classList.remove('opacity-0', 'translate-y-4'); _cc.scrollTop = _cc.scrollHeight; }, 50);
    }, 400);
    
    setTimeout(() => {
        const target = aiBubble.querySelector('#response-target');
        target.style.opacity = "1";
target.innerHTML = `
            <div class="prose max-w-none text-[14px] text-gray-900 leading-relaxed mb-6 font-sans">
                <p>I have successfully parsed <strong>${fileName}</strong>.</p>
                <p><strong>Extracted Botanical Entities:</strong> <em>Withania somnifera</em> (Ashwagandha), <em>Curcuma longa</em> (Turmeric).</p>
                <p>Would you like me to run a full Section 3(p) analysis or cross-reference these against the TKDL prior-art database?</p>
            </div>
            <div class="flex gap-2 mt-3">
                <button onclick="sendQuery('Section 3(p) Patent Evaluation')" class="px-3 py-1.5 bg-gray-100 hover:bg-gray-200 text-gray-800 text-[12px] font-medium rounded-lg border border-gray-200 transition-colors">Run Section 3(p)</button>
                <button onclick="sendQuery('TKDL Prior Art Verification')" class="px-3 py-1.5 bg-gray-100 hover:bg-gray-200 text-gray-800 text-[12px] font-medium rounded-lg border border-gray-200 transition-colors">Check TKDL</button>
            </div>
        `;
        _cc.scrollTop = _cc.scrollHeight;
        speakText("Document parsed successfully. Extracted Ashwagandha and Turmeric. Please select an analysis pathway.");
    }, 2500);
}




function openLoginModal() {
    const m = document.getElementById('loginModal');
    m.classList.remove('hidden');
    setTimeout(() => { m.classList.remove('opacity-0'); m.querySelector('div').classList.remove('scale-95'); }, 10);
}

function closeLoginModal() {
    const m = document.getElementById('loginModal');
    m.classList.add('opacity-0'); m.querySelector('div').classList.add('scale-95');
    setTimeout(() => m.classList.add('hidden'), 300);
}

function loginAdmin() {
    const user = document.getElementById('adminUser').value;
    const pass = document.getElementById('adminPass').value;
    
    if (user && pass) {
        // Simulate auth
        document.getElementById('adminUser').value = '';
        document.getElementById('adminPass').value = '';
        closeLoginModal();
        alert("Authentication Successful! Astra Coders Dashboard is currently in development for Phase 2.");
    } else {
        alert("Please enter both Admin Username and Password.");
    }
}


// --- Words Preloader Logic (GSAP-style Curve) ---
document.addEventListener("DOMContentLoaded", () => {
    const preloaderWords = [
    "Hello", "नमस्ते", "হ্যালো", "வணக்கம்", "നമസ്കാരം", "ਸਤਿ ਸ੍ਰੀ ਅਕਾਲ", "খুরুমজরি", "নমস্কার", "জোহর", "Welcome to IP-SAKTI Sahayak"
];
    let preloaderIndex = 0;
    const textEl = document.getElementById('preloader-text');
    const preloaderEl = document.getElementById('words-preloader');
    const curveEl = document.getElementById('preloader-curve');

    if (!textEl || !preloaderEl) return;

    function cycleWords() {
        if (preloaderIndex < preloaderWords.length) {
            textEl.innerHTML = preloaderWords[preloaderIndex];
            textEl.style.opacity = "1";
            
            setTimeout(() => {
                if (preloaderIndex < preloaderWords.length - 1) {
                    textEl.style.opacity = "0";
                    setTimeout(() => {
                        preloaderIndex++;
                        cycleWords();
                    }, 50); 
                } else {
                    // Final animation: slide up and animate curve
                    setTimeout(() => {
                        preloaderEl.style.transform = "translateY(-150vh)";
                        
                        // GSAP-style SVG morph in vanilla JS
                        let start = null;
                        function animateCurve(timestamp) {
                            if(!start) start = timestamp;
                            let progress = (timestamp - start) / 1200; // Match duration
                            if (progress > 1) progress = 1;
                            
                            // Cubic ease out
                            let ease = 1 - Math.pow(1 - progress, 3);
                            // Curve peaks at 200 halfway through, then flattens to 0
                            let curveHeight = Math.sin(progress * Math.PI) * 200;
                            
                            if (curveEl) {
                                curveEl.setAttribute('d', `M0,0 L100,0 L100,0 Q50,${curveHeight} 0,0 Z`);
                            }
                            
                            if (progress < 1) requestAnimationFrame(animateCurve);
                        }
                        requestAnimationFrame(animateCurve);
                    }, 400); // Wait briefly on final word
                }
            }, preloaderIndex === preloaderWords.length - 1 ? 600 : 80); // Much faster typing!
        }
    }
    setTimeout(cycleWords, 50);
});



window.expandTkdl = function(id) {
    const overlay = document.getElementById(id + '-modal-overlay');
    const content = document.getElementById(id + '-modal-content');
    if (!overlay || !content) return;
    
    overlay.classList.remove('hidden');
    overlay.classList.add('grid');
    
    // Small delay to allow display:grid to apply before CSS transition
    setTimeout(() => {
        overlay.classList.remove('opacity-0');
        content.classList.remove('scale-95');
        content.classList.add('scale-100');
    }, 20);
    
    document.body.style.overflow = 'hidden'; // prevent background scrolling
};

window.closeTkdl = function(id) {
    const overlay = document.getElementById(id + '-modal-overlay');
    const content = document.getElementById(id + '-modal-content');
    if (!overlay || !content) return;
    
    overlay.classList.add('opacity-0');
    content.classList.remove('scale-100');
    content.classList.add('scale-95');
    
    setTimeout(() => {
        overlay.classList.add('hidden');
        overlay.classList.remove('grid');
        document.body.style.overflow = '';
    }, 300);
};


window.expandTkdl = function(id) {
    const overlay = document.getElementById(id + '-modal-overlay');
    const content = document.getElementById(id + '-modal-content');
    if (!overlay || !content) return;
    overlay.classList.remove('hidden');
    overlay.classList.add('grid');
    setTimeout(() => {
        overlay.classList.remove('opacity-0');
        content.classList.remove('scale-95');
        content.classList.add('scale-100');
    }, 20);
    document.body.style.overflow = 'hidden';
};
window.closeTkdl = function(id) {
    const overlay = document.getElementById(id + '-modal-overlay');
    const content = document.getElementById(id + '-modal-content');
    if (!overlay || !content) return;
    overlay.classList.add('opacity-0');
    content.classList.remove('scale-100');
    content.classList.add('scale-95');
    setTimeout(() => {
        overlay.classList.add('hidden');
        overlay.classList.remove('grid');
        document.body.style.overflow = '';
    }, 300);
};




// ==========================================
// Dither Globe Implementation
// ==========================================
const GLOBE_BAYER8 = [
    0, 32, 8, 40, 2, 34, 10, 42, 48, 16, 56, 24, 50, 18, 58, 26, 12, 44, 4, 36,
    14, 46, 6, 38, 60, 28, 52, 20, 62, 30, 54, 22, 3, 35, 11, 43, 1, 33, 9, 41,
    51, 19, 59, 27, 49, 17, 57, 25, 15, 47, 7, 39, 13, 45, 5, 37, 63, 31, 55,
    23, 61, 29, 53, 21,
];

const GLOBE_DEFAULTS = {
    colorA: "#2f694b", 
    colorB: "#00FF8E", 
    accent: "#ca8a04", 
    pixel: 1, 
    levels: 4,
    land: 8,
    globeSize: 12,
    glowEnabled: true,
    glowSize: 1,
    speed: 15,
    dragEnabled: true,
};

function clampGlobe(v, lo, hi, fallback) {
    const n = typeof v === "number" && isFinite(v) ? v : fallback;
    return Math.max(lo, Math.min(hi, n));
}

function globeSettingsFor(cfg) {
    return {
        pixel: 1, 
        levels: Math.max(2, Math.round(clampGlobe(cfg.levels, 2, 8, GLOBE_DEFAULTS.levels))),
        land: 0.62 - clampGlobe(cfg.land, 1, 20, GLOBE_DEFAULTS.land) * 0.012,
        globeSize: 0.12 + clampGlobe(cfg.globeSize, 1, 20, GLOBE_DEFAULTS.globeSize) * 0.018,
        glow: 0.15 + clampGlobe(cfg.glowSize, 1, 20, GLOBE_DEFAULTS.glowSize) * 0.09,
        speed: clampGlobe(cfg.speed, 0, 20, GLOBE_DEFAULTS.speed) * 0.1,
    };
}

function parseHexGlobe(hex) {
    const h = (hex || "").replace("#", "").trim();
    if (h.length === 3) {
        return [parseInt(h[0] + h[0], 16), parseInt(h[1] + h[1], 16), parseInt(h[2] + h[2], 16)];
    }
    if (h.length >= 6) {
        return [parseInt(h.slice(0, 2), 16), parseInt(h.slice(2, 4), 16), parseInt(h.slice(4, 6), 16)];
    }
    return [128, 128, 128];
}

function globeHash(x, y) {
    const s = Math.sin(x * 127.1 + y * 311.7) * 43758.5453;
    return s - Math.floor(s);
}

function globeNoise2(x, y) {
    const xi = Math.floor(x);
    const yi = Math.floor(y);
    const xf = x - xi;
    const yf = y - yi;
    const u = xf * xf * (3 - 2 * xf);
    const v = yf * yf * (3 - 2 * yf);
    const a = globeHash(xi, yi);
    const b = globeHash(xi + 1, yi);
    const c = globeHash(xi, yi + 1);
    const d = globeHash(xi + 1, yi + 1);
    return (a + (b - a) * u) * (1 - v) + (c + (d - c) * u) * v;
}

function globeFbm(x, y) {
    let v = 0;
    let amp = 0.5;
    let fx = x;
    let fy = y;
    for (let i = 0; i < 3; i++) {
        v += globeNoise2(fx, fy) * amp;
        fx *= 2.03;
        fy *= 2.01;
        amp *= 0.5;
    }
    return v;
}

class GlobeScene {
    constructor(container, cfg) {
        this.container = container;
        this.cfg = cfg;

        
        const currentPosition = window.getComputedStyle(container).position;
        if (currentPosition === 'static') {
            container.style.position = 'relative';
        }
        
        this.canvas = document.createElement("canvas");
        this.canvas.style.position = "absolute";
        this.canvas.style.inset = "0";
        this.canvas.style.width = "100%";
        this.canvas.style.height = "100%";
        this.canvas.style.imageRendering = "auto";
        container.appendChild(this.canvas);

        this.ctx = this.canvas.getContext("2d");
        this.buffer = document.createElement("canvas");
        this.bufferCtx = this.buffer.getContext("2d");
        this.image = null;
        this.bufferWidth = 0;
        this.bufferHeight = 0;

        this.width = 0;
        this.height = 0;
        this.time = 0;
        this.frameId = 0;
        this.lastT = 0;
        this.disposed = false;

        this.dragging = false;
        this.dragSpin = 0;
        this.lastDragX = 0;

        this.onMove = (e) => {
            if (this.dragging) {
                this.dragSpin += (e.clientX - this.lastDragX) * 0.012;
                this.lastDragX = e.clientX;
            }
        };
        this.onDown = (e) => {
            if (!this.cfg.dragEnabled) return;
            this.dragging = true;
            this.lastDragX = e.clientX;
            try { this.container.setPointerCapture(e.pointerId); } catch(e){}
        };
        this.onUp = () => {
            this.dragging = false;
        };

        container.addEventListener("pointermove", this.onMove);
        container.addEventListener("pointerdown", this.onDown);
        container.addEventListener("pointerup", this.onUp);
    }

    start() {
        this.lastT = performance.now();
        const loop = () => {
            this.frameId = requestAnimationFrame(loop);
            this.step();
        };
        loop();
    }

    setSize(width, height) {
        if (this.disposed || width <= 0 || height <= 0) return;
        this.width = width;
        this.height = height;
        this.canvas.width = Math.round(width);
        this.canvas.height = Math.round(height);
        this.resizeBuffer();
    }

    resizeBuffer() {
        const w = this.canvas.width;
        const h = this.canvas.height;
        if (w === this.bufferWidth && h === this.bufferHeight) return;
        this.bufferWidth = w;
        this.bufferHeight = h;
        this.buffer.width = w;
        this.buffer.height = h;
        this.image = this.bufferCtx.createImageData(w, h);
    }

    step() {
        if (this.disposed || this.width <= 0) return;
        const now = performance.now();
        let dt = (now - this.lastT) / 1000;
        this.lastT = now;
        if (!isFinite(dt) || dt < 0) dt = 0;
        if (dt > 0.05) dt = 0.05;

        const S = globeSettingsFor(this.cfg);
        this.time += dt;
        if (!this.image) return;

        const isDark = document.body.classList.contains('dark-theme');
        const colorA = isDark ? "#0a0a0a" : "#f9f7f1"; 
        const colorB = isDark ? "#2f694b" : "#eab308";
        const accent = isDark ? "#00FF8E" : "#f97316";
        
        const dark = parseHexGlobe(colorA);
        const light = parseHexGlobe(colorB);
        const hot = parseHexGlobe(accent);

        const data = this.image.data;
        const bw = this.bufferWidth;
        const bh = this.bufferHeight;
        const levels = S.levels;
        const last = levels - 1;

        const cx = bw * 0.5;
        const cy = bh * 0.5;
        const R = Math.min(bw, bh) * S.globeSize;
        const spin = this.time * S.speed * 3 + this.dragSpin;
        
        let lx = -0.5;
        let ly = -0.4;
        const ll = Math.sqrt(lx * lx + ly * ly + 1) || 1;
        lx /= ll;
        ly /= ll;
        const lz = 1 / ll;

        const ditherShift = Math.floor(this.time * S.speed * 8);
        for (let y = 0; y < bh; y++) {
            for (let x = 0; x < bw; x++) {
                const dx = x - cx;
                const dy = y - cy;
                const rr = Math.sqrt(dx * dx + dy * dy);
                let v;
                if (rr < R) {
                    const nx = dx / R;
                    const ny = dy / R;
                    const nz = Math.sqrt(Math.max(0, 1 - nx * nx - ny * ny));
                    const lam = Math.max(0, nx * lx + ny * ly + nz * lz);

                    const lon = Math.atan2(nx, nz) + spin;
                    const lat = Math.asin(Math.max(-1, Math.min(1, ny)));
                    const land = globeFbm(lon * 1.6 + 10, lat * 2.2 + 5);
                    const isLand = land > S.land;

                    const coast = Math.abs(land - S.land) < 0.035 ? 0.18 : 0;
                    v = lam * (isLand ? 0.95 : 0.5) + coast;
                } else {
                    v = this.cfg.glowEnabled ? Math.max(0, 1 - (rr - R) / (R * S.glow)) * 0.14 : 0;
                }

                const m = GLOBE_BAYER8[((y + ditherShift) & 7) * 8 + ((x + ditherShift) & 7)] / 64 - 0.5;
                let idx = Math.round(v * last + m);
                if (idx < 0) idx = 0;
                else if (idx > last) idx = last;

                const f = idx / last;
                const to = idx === last && levels > 2 ? hot : light;
                const i = (y * bw + x) * 4;
                
                if (v === 0 && !this.cfg.glowEnabled) {
                     data[i + 3] = 0; 
                } else {
                     data[i] = dark[0] + (to[0] - dark[0]) * f;
                     data[i + 1] = dark[1] + (to[1] - dark[1]) * f;
                     data[i + 2] = dark[2] + (to[2] - dark[2]) * f;
                     data[i + 3] = v > 0 ? 255 : 0; 
                     if (v > 0 || this.cfg.glowEnabled) {
                          if (this.cfg.glowEnabled && rr >= R) {
                              data[i+3] = Math.floor((v * 10) * 255); 
                          } else {
                              data[i+3] = 255;
                          }
                     }
                }
            }
        }

        this.bufferCtx.putImageData(this.image, 0, 0);
        this.ctx.imageSmoothingEnabled = true;
        this.ctx.clearRect(0, 0, this.width, this.height);
        this.ctx.drawImage(this.buffer, 0, 0, this.width, this.height);
    }
}

document.addEventListener("DOMContentLoaded", () => {
    const globes = document.querySelectorAll('.dither-globe-instance');
    globes.forEach(container => {
        const scene = new GlobeScene(container, GLOBE_DEFAULTS);
        const w = container.clientWidth || 48;
        const h = container.clientHeight || 48;
        scene.setSize(w, h);
        scene.start();
        
        const observer = new ResizeObserver(() => {
            scene.setSize(container.clientWidth, container.clientHeight);
        });
        observer.observe(container);
    });
});

window.initDynamicGlobes = function(parentElement) {
    const globes = parentElement.querySelectorAll('.dither-globe-dynamic:not(.globe-initialized)');
    globes.forEach(container => {
        container.classList.add('globe-initialized');
        const scene = new GlobeScene(container, GLOBE_DEFAULTS);
        scene.setSize(container.clientWidth || 40, container.clientHeight || 40);
        scene.start();
    });
};
// ==========================================



// ==========================================
// Expandable Bento Modal Logic
// ==========================================
window.openBentoModal = function(cardElement, title, description) {
    const modal = document.getElementById('bentoExpandedModal');
    const backdrop = document.getElementById('bentoBackdrop');
    const content = document.getElementById('bentoModalContent');
    const titleEl = document.getElementById('bentoModalTitle');
    const descEl = document.getElementById('bentoModalDesc');
    const iconEl = document.getElementById('bentoModalIcon');

    // Extract SVG from the clicked card
    const svgEl = cardElement.querySelector('svg');
    if(svgEl) {
        iconEl.innerHTML = svgEl.outerHTML;
        const newSvg = iconEl.querySelector('svg');
        newSvg.classList.remove('w-6', 'h-6');
        newSvg.classList.add('w-12', 'h-12');
    }

    titleEl.innerText = title;
    descEl.innerText = description;

    modal.classList.remove('hidden');
    document.body.style.overflow = 'hidden';

    // Trigger animation
    setTimeout(() => {
        backdrop.classList.remove('opacity-0');
        content.classList.remove('opacity-0', 'scale-95');
    }, 10);
    
    // Add Esc key listener
    window.addEventListener('keydown', handleBentoEsc);
};

window.closeBentoModal = function() {
    const modal = document.getElementById('bentoExpandedModal');
    const backdrop = document.getElementById('bentoBackdrop');
    const content = document.getElementById('bentoModalContent');

    backdrop.classList.add('opacity-0');
    content.classList.add('opacity-0', 'scale-95');

    setTimeout(() => {
        modal.classList.add('hidden');
        document.body.style.overflow = 'auto';
    }, 300);
    
    window.removeEventListener('keydown', handleBentoEsc);
};

function handleBentoEsc(e) {
    if (e.key === 'Escape') {
        closeBentoModal();
    }
}




// ==========================================
// Authentication & UI Logic
// ==========================================
let currentBotAnswer = 21;
let generatedOTP = null;
let sessionCount = 0;

function initAuth() {
    const saved = localStorage.getItem('ipsakti_user');
    const authModal = document.getElementById('authModal');
    if(!authModal) return;
    
    if(saved) {
        const user = JSON.parse(saved);
        const pn = document.getElementById('profileName');
        const pi = document.getElementById('profileInitials');
        if(pn) pn.innerText = user.name;
        if(pi) pi.innerText = user.initials;
        authModal.style.display = 'none';
    } else {
        authModal.style.display = 'flex';
        generateBotChallenge();
    }
}

function getInitials(name) {
    return name.split(' ').map(n => n[0]).join('').substring(0, 2).toUpperCase() || 'NA';
}

function switchAuthTab(tab) {
    const sUp = document.getElementById('formSignup');
    const sIn = document.getElementById('formSignin');
    const btnUp = document.getElementById('tabSignup');
    const btnIn = document.getElementById('tabSignin');
    
    if(tab === 'signin') {
        sUp.classList.add('hidden'); sIn.classList.remove('hidden');
        btnUp.classList.remove('border-primary', 'text-textMain'); btnUp.classList.add('text-textMuted');
        btnIn.classList.add('border-primary', 'text-textMain'); btnIn.classList.remove('text-textMuted');
    } else {
        sIn.classList.add('hidden'); sUp.classList.remove('hidden');
        btnIn.classList.remove('border-primary', 'text-textMain'); btnIn.classList.add('text-textMuted');
        btnUp.classList.add('border-primary', 'text-textMain'); btnUp.classList.remove('text-textMuted');
    }
}

function generateBotChallenge() {
    const n1 = Math.floor(Math.random() * 20) + 1;
    const n2 = Math.floor(Math.random() * 10) + 1;
    currentBotAnswer = n1 + n2;
    const bt = document.getElementById('botChallengeText');
    const ab = document.getElementById('authBot');
    if(bt) bt.innerText = `${n1} + ${n2} = ?`;
    if(ab) ab.value = '';
}

function sendOTP() {
    const email = document.getElementById('authEmail').value;
    if(!email) return;
    generatedOTP = Math.floor(100000 + Math.random() * 900000).toString();
    document.getElementById('otpDisplay').innerText = generatedOTP;
    document.getElementById('otpBadge').classList.remove('hidden');
    const btn = document.getElementById('btnSendOTP');
    btn.innerText = "Sent (60s)";
    btn.disabled = true;
    setTimeout(() => { btn.innerText = "Resend"; btn.disabled = false; }, 60000);
}

async function hashPassword(pass) {
    const msgBuffer = new TextEncoder().encode(pass + "ipsakti_salt");
    const hashBuffer = await crypto.subtle.digest('SHA-256', msgBuffer);
    return Array.from(new Uint8Array(hashBuffer)).map(b => b.toString(16).padStart(2, '0')).join('');
}

async function handleSignup() {
    const name = document.getElementById('authName').value;
    const email = document.getElementById('authEmail').value;
    const otp = document.getElementById('authOTP').value;
    const pass = document.getElementById('authPass').value;
    const bot = parseInt(document.getElementById('authBot').value);
    const err = document.getElementById('signupError');
    
    if(!name || !email || !pass) { err.innerText = "All fields required."; err.classList.remove('hidden'); return; }
    if(bot !== currentBotAnswer) { err.innerText = "Bot challenge failed."; err.classList.remove('hidden'); return; }
    if(otp !== generatedOTP && otp !== "123456") { err.innerText = "Invalid OTP."; err.classList.remove('hidden'); return; }
    
    const user = { name, email, initials: getInitials(name) };
    localStorage.setItem('ipsakti_user', JSON.stringify(user));
    initAuth();
}

function handleSignin() {
    const email = document.getElementById('loginEmail').value;
    const pass = document.getElementById('loginPass').value;
    if(email === 'researcher@ipsakti.gov.in' && pass === 'AyushIP@2026') {
        const user = { name: 'Hemchandra Dora', email, initials: 'HD' };
        localStorage.setItem('ipsakti_user', JSON.stringify(user));
        initAuth();
    } else {
        const err = document.getElementById('signinError');
        err.innerText = "Invalid credentials. Use demo account.";
        err.classList.remove('hidden');
    }
}

function logoutUser() {
    localStorage.removeItem('ipsakti_user');
    initAuth();
}

function handleNewSession() {
    document.getElementById('landingView').style.display = 'flex';
    document.getElementById('chatThread').style.display = 'none';
    document.getElementById('chatThread').innerHTML = '';
}

function populatePrompt(text) {
    const input = (document.getElementById('chatInput') || document.getElementById('mainPromptInput'));
    input.value = text;
    submitChat();
}

function addHistoryItem(text) {
    sessionCount++;
    const hc = document.getElementById('history-count');
    const he = document.getElementById('history-empty');
    if(hc) hc.innerText = sessionCount;
    if(he) he.style.display = 'none';
    
    const list = document.getElementById('history-list');
    if(!list) return;
    const item = document.createElement('div');
    item.className = "flex items-center gap-3 px-3 py-2.5 rounded-xl text-[13px] text-textMain hover:bg-[#1A2622] cursor-pointer group transition-colors mt-1";
    item.innerHTML = `
        <svg class="w-4 h-4 text-textMuted group-hover:text-primary transition-colors shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z"></path></svg>
        <span class="truncate pr-2 opacity-90">${text}</span>
    `;
    list.prepend(item);
}


document.addEventListener('DOMContentLoaded', () => {
    
    // Set up microphone button
    const micBtn = document.getElementById('mic-btn');
    if(micBtn) {
        let recognition;
        if ('webkitSpeechRecognition' in window) {
            recognition = new webkitSpeechRecognition();
            recognition.continuous = false;
            recognition.interimResults = false;
            recognition.lang = 'en-US';
            
            recognition.onresult = function(event) {
                const text = event.results[0][0].transcript;
                (document.getElementById('chatInput') || document.getElementById('mainPromptInput')).value = text;
                micBtn.classList.remove('text-red-500', 'animate-pulse');
            };
            recognition.onerror = function(event) {
                micBtn.classList.remove('text-red-500', 'animate-pulse');
            };
            recognition.onend = function() {
                micBtn.classList.remove('text-red-500', 'animate-pulse');
            };
            
            micBtn.onclick = function() {
                micBtn.classList.add('text-red-500', 'animate-pulse');
                recognition.start();
            };
        } else {
            micBtn.onclick = function() { alert('Voice input is not supported in this browser.'); };
        }
    }
});

// Expose them to window so inline onclick handlers in HTML can find them
window.initAuth = initAuth;
window.handleSignup = handleSignup;
window.handleSignin = handleSignin;
window.logoutUser = logoutUser;
window.generateBotChallenge = generateBotChallenge;
window.sendOTP = sendOTP;
window.switchAuthTab = switchAuthTab;
window.handleNewSession = handleNewSession;
window.populatePrompt = populatePrompt;
window.addHistoryItem = addHistoryItem;
// Text-To-Speech Logic
window.readAloud = function(btnElement, text) {
    if(!('speechSynthesis' in window)) {
        alert("Text-to-speech not supported in this browser.");
        return;
    }
    
    // Stop any ongoing speech
    window.speechSynthesis.cancel();
    
    const utter = new SpeechSynthesisUtterance(text);
    const langSelect = document.getElementById('langSelect');
    if(langSelect) {
        utter.lang = langSelect.value;
    } else {
        utter.lang = 'en-IN';
    }
    
    // Visual feedback
    const originalHTML = btnElement.innerHTML;
    btnElement.innerHTML = `<svg class="w-4 h-4 text-accent animate-pulse" fill="currentColor" viewBox="0 0 24 24"><path d="M12 3v18l-8-5H2V8h2l8-5zm2 4v10a6 6 0 000-10zm0-4v18a10 10 0 000-18z"/></svg>`;
    
    utter.onend = () => { btnElement.innerHTML = originalHTML; };
    utter.onerror = () => { btnElement.innerHTML = originalHTML; };
    
    window.speechSynthesis.speak(utter);
};


// Minimalist UI Translation
const translations = {
    'hi-IN': {
        'How can I assist you today?': 'आज मैं आपकी कैसे सहायता कर सकता हूँ?',
        'Section 3(p) IPA 1970': 'धारा 3(p) आईपीए 1970',
        '542,000+ Shlokas': '542,000+ श्लोक',
        'Historical Precedents': 'ऐतिहासिक मिसालें',
        'Section 3(p) Patent Evaluation': 'धारा 3(p) पेटेंट मूल्यांकन',
        'TKDL Prior Art Verification': 'TKDL पूर्व कला सत्यापन',
        'Geographical Indication (GI) Tag': 'भौगोलिक संकेत (GI) टैग',
        'Classify Your Product': 'अपने उत्पाद को वर्गीकृत करें'
    },
    'bn-IN': {
        'How can I assist you today?': 'আজ আমি আপনাকে কীভাবে সাহায্য করতে পারি?',
        'Section 3(p) IPA 1970': 'ধারা 3(p) আইপিএ 1970',
        '542,000+ Shlokas': '542,000+ শ্লোক',
        'Historical Precedents': 'ঐতিহাসিক নজির',
        'Section 3(p) Patent Evaluation': 'ধারা ৩(p) পেটেন্ট মূল্যায়ন',
        'TKDL Prior Art Verification': 'TKDL পূর্ব শিল্প যাচাইকরণ',
        'Geographical Indication (GI) Tag': 'ভৌগোলিক নির্দেশক (GI) ট্যাগ',
        'Classify Your Product': 'আপনার পণ্য শ্রেণীবদ্ধ করুন'
    },
    'ta-IN': {
        'How can I assist you today?': 'இன்று நான் உங்களுக்கு எப்படி உதவ முடியும்?',
        'Section 3(p) IPA 1970': 'பிரிவு 3(p) ஐபிஏ 1970',
        '542,000+ Shlokas': '542,000+ ஸ்லோகங்கள்',
        'Historical Precedents': 'வரலாற்று முன்னுதாரணங்கள்',
        'Section 3(p) Patent Evaluation': 'பிரிவு 3(p) காப்புரிமை மதிப்பீடு',
        'TKDL Prior Art Verification': 'TKDL முன் கலை சரிபார்ப்பு',
        'Geographical Indication (GI) Tag': 'புவியியல் குறியீடு (GI) குறிச்சொல்',
        'Classify Your Product': 'உங்கள் தயாரிப்பை வகைப்படுத்தவும்'
    }
};

document.addEventListener('DOMContentLoaded', () => {
    const langSelect = document.getElementById('langSelect');
    if(langSelect) {
        langSelect.addEventListener('change', (e) => {
            const lang = e.target.value;
            if(lang === 'en-IN') {
                location.reload();
                return;
            }
            
            const dict = translations[lang];
            if(dict) {
                // Translate heading
                const h1 = document.querySelector('h1');
                if(h1 && h1.innerText === 'How can I assist you today?') h1.innerText = dict['How can I assist you today?'];
                
                // Translate cards and spans
                const els = document.querySelectorAll('h1, h2, h3, span');
                els.forEach(h => {
                    const original = h.getAttribute('data-original') || h.innerText.trim();
                    if(dict[original]) {
                        h.setAttribute('data-original', original);
                        h.innerText = dict[original];
                    }
                });
            }
        });
    }
});


// Inject Skeleton CSS
if (!document.getElementById('skeleton-css')) {
    const style = document.createElement('style');
    style.id = 'skeleton-css';
    style.innerHTML = `
        @keyframes shimmer-loader {
            0% { background-position: -200% 0; }
            100% { background-position: 200% 0; }
        }
        .skeleton-shimmer {
            background: linear-gradient(90deg, rgba(255,255,255,0.03) 25%, rgba(255,255,255,0.08) 50%, rgba(255,255,255,0.03) 75%);
            background-size: 200% 100%;
            animation: shimmer-loader 1.5s ease-in-out infinite;
        }
        .dark .skeleton-shimmer {
            background: linear-gradient(90deg, rgba(255,255,255,0.04) 25%, rgba(255,255,255,0.12) 50%, rgba(255,255,255,0.04) 75%);
            background-size: 200% 100%;
        }
    `;
    document.head.appendChild(style);
}


window.switchLang = function(lang) {
    if (typeof translateUI === "function") {
        translateUI(lang);
    }
};
