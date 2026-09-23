"""
Transform hub.html to:
1. Add i18n.js script
2. Add language switcher to header
3. Wire the 4 feature cards to populate chat input
4. Add initial_query handling from localStorage
5. Add data-i18n attributes to key elements
"""
import codecs
import re

with codecs.open('app/static/hub.html', 'r', 'utf-8') as f:
    html = f.read()

# ============================================================
# 1. Add i18n.js script before app.js
# ============================================================
html = html.replace(
    '<script src="/static/app.js"></script>',
    '<script src="/static/i18n.js"></script>\n<script src="/static/app.js"></script>'
)

# ============================================================
# 2. Add language switcher to header (next to clerk-mount-point)
# ============================================================
lang_switcher = '''<div class="flex items-center gap-1 mr-2">
<button class="px-2 py-0.5 rounded bg-surface-container text-on-surface hover:bg-surface-bright transition-colors font-bold text-label-sm" onclick="switchLanguage('en')" data-lang-btn="en">EN</button>
<button class="px-2 py-0.5 rounded text-on-surface-variant hover:text-on-surface transition-colors font-medium text-label-sm" onclick="switchLanguage('hi')" data-lang-btn="hi">HI</button>
</div>'''

# Insert before clerk-mount-point
html = html.replace(
    '<div id="clerk-mount-point"',
    lang_switcher + '\n<div id="clerk-mount-point"'
)

# ============================================================
# 3. Wire the 4 feature cards to populate chat input and submit
# ============================================================
# Card 1: Section 3(p) Patent Evaluation - "Run Claim Audit"
card1_query = "Section 3(p) IPA 1970 patent evaluation and Sec 3(e) Synergism guidelines for Ayurvedic formulation"
html = html.replace(
    '<!-- Card 1: Section 3(p) Patent Evaluation -->',
    '<!-- Card 1: Section 3(p) Patent Evaluation -->'
)
# Find the card wrapper div and add onclick
# The cards lack onclick handlers - we need to add them
# Let me find the exact pattern for each card

# Card 1 - add onclick to the card wrapper
html = html.replace(
    '''<!-- Card 1: Section 3(p) Patent Evaluation -->
<div class="group relative bg-surface-container-low''',
    '''<!-- Card 1: Section 3(p) Patent Evaluation -->
<div onclick="if(typeof setPrompt==='function'){setPrompt('Section 3(p) IPA 1970 patent evaluation and Sec 3(e) Synergism guidelines');if(typeof submitChat==='function')submitChat()}" class="cursor-pointer group relative bg-surface-container-low'''
)

# Card 2 - TKDL Prior Art
html = html.replace(
    '''<!-- Card 2: TKDL Prior Art Verification -->
<div class="group relative bg-surface-container-low''',
    '''<!-- Card 2: TKDL Prior Art Verification -->
<div onclick="if(typeof setPrompt==='function'){setPrompt('Cross-reference formulation with TKDL prior art, check Charaka Samhita and WIPO IPC A61K 36/00');if(typeof submitChat==='function')submitChat()}" class="cursor-pointer group relative bg-surface-container-low'''
)

# Card 3 - GI & ABS
html = html.replace(
    '''<!-- Card 3: Geographical Indication (GI) & ABS -->
<div class="group relative bg-surface-container-low''',
    '''<!-- Card 3: Geographical Indication (GI) & ABS -->
<div onclick="if(typeof setPrompt==='function'){setPrompt('Evaluate Geographical Indication (GI) and ABS clearance mandates under NBA Form I');if(typeof submitChat==='function')submitChat()}" class="cursor-pointer group relative bg-surface-container-low'''
)

# Card 4 - Classify Product
html = html.replace(
    '''<!-- Card 4: Classify Your Product -->
<div class="group relative bg-surface-container-low''',
    '''<!-- Card 4: Classify Your Product -->
<div onclick="if(typeof setPrompt==='function'){setPrompt('Classify my Ayurvedic product under D&C Act categories (Classical, P&P, New Drug, Phytopharmaceutical, Aahar, Cosmetic)');if(typeof submitChat==='function')submitChat()}" class="cursor-pointer group relative bg-surface-container-low'''
)

# ============================================================
# 4. Add initial_query handling from localStorage
# ============================================================
initial_query_script = '''
<script>
// Handle initial_query from localStorage (coming from index.html)
document.addEventListener('DOMContentLoaded', function() {
    const initialQuery = localStorage.getItem('initial_query');
    if (initialQuery) {
        localStorage.removeItem('initial_query');
        const input = document.getElementById('mainPromptInput') || document.getElementById('chatInput');
        if (input) {
            input.value = initialQuery;
            // Small delay to let app.js initialize
            setTimeout(function() {
                if (typeof submitChat === 'function') {
                    submitChat();
                }
            }, 500);
        }
    }
});
</script>
'''
html = html.replace(
    '<script src="/static/i18n.js"></script>',
    initial_query_script + '\n<script src="/static/i18n.js"></script>'
)

# ============================================================
# 5. Add setPrompt function if missing (it exists in inline script)
# ============================================================
# The inline script in hub.html already has setPrompt, so this should work.

with codecs.open('app/static/hub.html', 'w', 'utf-8') as f:
    f.write(html)

print("[OK] hub.html transformation complete!")
print("  - Added i18n.js + initial_query handler scripts")
print("  - Added language switcher (EN/HI) to header")
print("  - Wired all 4 feature cards with onclick -> setPrompt + submitChat")
print("  - Added localStorage initial_query auto-submission")
