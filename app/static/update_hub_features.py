import codecs
import re

with codecs.open('app/static/hub.html', 'r', 'utf-8') as f:
    html = f.read()

# 1. Re-apply i18n script, initial_query, and language switcher (since we reverted)
# ============================================================
html = html.replace(
    '<script src="/static/app.js"></script>',
    '''<script>
// Handle initial_query from localStorage (coming from index.html)
document.addEventListener('DOMContentLoaded', function() {
    const initialQuery = localStorage.getItem('initial_query');
    if (initialQuery) {
        localStorage.removeItem('initial_query');
        setTimeout(function() {
            setPromptAndSubmit(initialQuery);
        }, 500);
    }
});
</script>
<script src="/static/i18n.js"></script>
<script src="/static/app.js"></script>'''
)

lang_switcher = '''<div class="flex items-center gap-1 mr-2">
<button class="px-2 py-0.5 rounded bg-surface-container text-on-surface hover:bg-surface-bright transition-colors font-bold text-label-sm" onclick="switchLanguage('en')" data-lang-btn="en">EN</button>
<button class="px-2 py-0.5 rounded text-on-surface-variant hover:text-on-surface transition-colors font-medium text-label-sm" onclick="switchLanguage('hi')" data-lang-btn="hi">HI</button>
</div>'''

html = html.replace(
    '<div id="clerk-mount-point"',
    lang_switcher + '\n<div id="clerk-mount-point"'
)

# 2. Add setPromptAndSubmit function
# ============================================================
html = html.replace('</main>', '''
<script>
function setPromptAndSubmit(text) {
    if (typeof setPrompt === 'function') {
        setPrompt(text);
        if (typeof submitChat === 'function') {
            submitChat();
        }
    }
}
function toggleDashboard() {
    const dash = document.getElementById('advanced-dashboard');
    const btn = document.getElementById('toggle-dash-btn');
    if (dash.classList.contains('hidden')) {
        dash.classList.remove('hidden');
        btn.innerHTML = '<span class="material-symbols-outlined text-[20px]">visibility_off</span> Hide Dashboard';
    } else {
        dash.classList.add('hidden');
        btn.innerHTML = '<span class="material-symbols-outlined text-[20px]">dashboard</span> Show Dashboard';
    }
}
</script>
</main>''')

# 3. Wire the 4 feature cards
# ============================================================
cards_prompts = [
    "Section 3(p) IPA 1970 patent evaluation and Sec 3(e) Synergism guidelines",
    "Cross-reference formulation with TKDL prior art, check Charaka Samhita and WIPO IPC A61K 36/00",
    "Evaluate Geographical Indication (GI) and ABS clearance mandates under NBA Form I",
    "Classify my Ayurvedic product under D&C Act categories (Classical, P&P, New Drug, Phytopharmaceutical, Aahar, Cosmetic)"
]

# We will find each card by its comment
card1_idx = html.find('<!-- Card 1: Section 3(p) Patent Evaluation -->')
card2_idx = html.find('<!-- Card 2: TKDL Prior Art Verification -->')
card3_idx = html.find('<!-- Card 3: Geographical Indication (GI) & ABS -->')
card4_idx = html.find('<!-- Card 4: Classify Your Product -->')
end_cards_idx = html.find('<!-- Functional Section Split: Live Regulatory Pipeline')

if card1_idx != -1 and card2_idx != -1 and card3_idx != -1 and card4_idx != -1:
    # Replace Card 1
    c1 = html[card1_idx:card2_idx]
    c1 = c1.replace('<div class="card-hover-fx', f'<div onclick="setPromptAndSubmit(\'{cards_prompts[0]}\')" class="card-hover-fx')
    
    # Replace Card 2
    c2 = html[card2_idx:card3_idx]
    c2 = c2.replace('<div class="card-hover-fx', f'<div onclick="setPromptAndSubmit(\'{cards_prompts[1]}\')" class="card-hover-fx')
    
    # Replace Card 3
    c3 = html[card3_idx:card4_idx]
    c3 = c3.replace('<div class="card-hover-fx', f'<div onclick="setPromptAndSubmit(\'{cards_prompts[2]}\')" class="card-hover-fx')
    
    # Replace Card 4
    c4 = html[card4_idx:end_cards_idx]
    c4 = c4.replace('<div class="card-hover-fx', f'<div onclick="setPromptAndSubmit(\'{cards_prompts[3]}\')" class="card-hover-fx')
    
    html = html[:card1_idx] + c1 + c2 + c3 + c4 + html[end_cards_idx:]


# 4. Wire the Sidebar (Side panel)
# ============================================================
html = html.replace(
    '<a href="#" class="flex flex-col gap-1 p-space-sm rounded-lg hover:bg-surface-container-highest transition-colors group">',
    '<a href="#" onclick="setPromptAndSubmit(this.innerText.replace(/\\n/g, \' \')); return false;" class="flex flex-col gap-1 p-space-sm rounded-lg hover:bg-surface-container-highest transition-colors group">'
)
# There are multiple links in the sidebar, this replace covers all of them!

# 5. Fix the "score one" grid-cols issue
# ============================================================
html = html.replace(
    '<div class="mt-space-md pt-space-sm grid grid-cols-3 gap-space-sm">',
    '<div class="mt-space-md pt-space-sm grid grid-cols-1 md:grid-cols-3 gap-space-sm">'
)

# 6. De-clutter the page by wrapping the extra sections in a hidden dashboard
# ============================================================
# Insert a toggle button below the chat input, and wrap the rest in a div
chat_area_end = html.find('<!-- Functional Section Split: Live Regulatory Pipeline')

toggle_btn = '''
<div class="flex justify-center mt-6 mb-8 hide-on-chat">
    <button id="toggle-dash-btn" onclick="toggleDashboard()" class="flex items-center gap-2 px-4 py-2 bg-surface-container-high hover:bg-surface-bright text-text-secondary hover:text-primary rounded-full transition-colors font-label-md shadow-sm border border-border-subtle">
        <span class="material-symbols-outlined text-[20px]">dashboard</span> Show Advanced Dashboard
    </button>
</div>
<div id="advanced-dashboard" class="hidden">
'''

html = html[:chat_area_end] + toggle_btn + html[chat_area_end:]

# Close the advanced-dashboard div before </main>
html = html.replace('</main>', '</div></main>')

with codecs.open('app/static/hub.html', 'w', 'utf-8') as f:
    f.write(html)
print("Hub successfully transformed!")
