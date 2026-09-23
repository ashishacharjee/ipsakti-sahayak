"""
Transform index.html into SPA with view routing, login prominence, and i18n tags.
This script carefully modifies index.html to:
1. Add i18n.js script tag
2. Replace switchLang with switchLanguage
3. Add SPA routing (showView function)
4. Wrap content sections into view divs
5. Move login gateway to be first in home view
6. Wire navigation links to showView()
7. Wire mobile bottom tabs to showView()
8. Add data-i18n attributes to key elements
"""
import codecs
import re

with codecs.open('app/static/index.html', 'r', 'utf-8') as f:
    html = f.read()

# ============================================================
# 1. Add i18n.js script before app.js
# ============================================================
html = html.replace(
    '<script src="/static/app.js"></script>',
    '<script src="/static/i18n.js"></script>\n<script src="/static/app.js"></script>'
)

# ============================================================
# 2. Replace language switcher buttons to use switchLanguage
# ============================================================
html = html.replace(
    '''onclick="if(typeof switchLang==='function')switchLang('en')"''',
    '''onclick="switchLanguage('en')" data-lang-btn="en"'''
)
html = html.replace(
    '''onclick="if(typeof switchLang==='function')switchLang('hi')"''',
    '''onclick="switchLanguage('hi')" data-lang-btn="hi"'''
)

# ============================================================
# 3. Update desktop nav links to use showView()
# ============================================================
# Statutory Overview
html = html.replace(
    '''data-path="sovereign-portal-landing" href="#" onclick="alert('Access Restricted: Requires Sovereign Portal Authentication.')"''',
    '''data-path="sovereign-portal-landing" href="#" onclick="event.preventDefault(); showView('view-statutory')"'''
)
# TKDL & Patent Search
html = html.replace(
    '''data-path="tkdl-and-patent-search" href="#" onclick="alert('Access Restricted: Requires Sovereign Portal Authentication.')"''',
    '''data-path="tkdl-and-patent-search" href="#" onclick="event.preventDefault(); showView('view-tkdl')"'''
)
# Product Classification Guide
html = html.replace(
    '''data-path="product-classification-guide" href="#" onclick="alert('Access Restricted: Requires Sovereign Portal Authentication.')"''',
    '''data-path="product-classification-guide" href="#" onclick="event.preventDefault(); showView('view-classify')"'''
)
# Gazette Bulletins
html = html.replace(
    '''data-path="gazette-bulletins" href="#" onclick="alert('Access Restricted: Requires Sovereign Portal Authentication.')"''',
    '''data-path="gazette-bulletins" href="#" onclick="event.preventDefault(); showView('view-gazette')"'''
)

# ============================================================
# 4. Update mobile bottom tab bar to use showView()
# ============================================================
# Overview tab
html = html.replace(
    '''<a href="#" onclick="alert('Access Restricted: Requires Sovereign Portal Authentication.')" class="flex flex-col items-center gap-1 p-2 py-3 text-on-surface-variant hover:text-primary transition-colors flex-1">
        <span class="material-symbols-outlined text-[20px]">gavel</span>
        <span class="text-[10px] font-medium text-center leading-tight">Overview</span>
    </a>''',
    '''<a href="#" onclick="event.preventDefault(); showView('view-statutory')" class="flex flex-col items-center gap-1 p-2 py-3 text-on-surface-variant hover:text-primary transition-colors flex-1" data-tab="view-statutory">
        <span class="material-symbols-outlined text-[20px]">gavel</span>
        <span class="text-[10px] font-medium text-center leading-tight" data-i18n="tab_overview">Overview</span>
    </a>'''
)
# TKDL tab
html = html.replace(
    '''<a href="#" onclick="alert('Access Restricted: Requires Sovereign Portal Authentication.')" class="flex flex-col items-center gap-1 p-2 py-3 text-on-surface-variant hover:text-primary transition-colors flex-1">
        <span class="material-symbols-outlined text-[20px]">search</span>
        <span class="text-[10px] font-medium text-center leading-tight">TKDL</span>
    </a>''',
    '''<a href="#" onclick="event.preventDefault(); showView('view-tkdl')" class="flex flex-col items-center gap-1 p-2 py-3 text-on-surface-variant hover:text-primary transition-colors flex-1" data-tab="view-tkdl">
        <span class="material-symbols-outlined text-[20px]">search</span>
        <span class="text-[10px] font-medium text-center leading-tight" data-i18n="tab_tkdl">TKDL</span>
    </a>'''
)
# Classify tab
html = html.replace(
    '''<a href="#" onclick="alert('Access Restricted: Requires Sovereign Portal Authentication.')" class="flex flex-col items-center gap-1 p-2 py-3 text-on-surface-variant hover:text-primary transition-colors flex-1">
        <span class="material-symbols-outlined text-[20px]">category</span>
        <span class="text-[10px] font-medium text-center leading-tight">Classify</span>
    </a>''',
    '''<a href="#" onclick="event.preventDefault(); showView('view-classify')" class="flex flex-col items-center gap-1 p-2 py-3 text-on-surface-variant hover:text-primary transition-colors flex-1" data-tab="view-classify">
        <span class="material-symbols-outlined text-[20px]">category</span>
        <span class="text-[10px] font-medium text-center leading-tight" data-i18n="tab_classify">Classify</span>
    </a>'''
)
# Gazette tab
html = html.replace(
    '''<a href="#" onclick="alert('Access Restricted: Requires Sovereign Portal Authentication.')" class="flex flex-col items-center gap-1 p-2 py-3 text-on-surface-variant hover:text-primary transition-colors flex-1">
        <span class="material-symbols-outlined text-[20px]">article</span>
        <span class="text-[10px] font-medium text-center leading-tight">Gazettes</span>
    </a>''',
    '''<a href="#" onclick="event.preventDefault(); showView('view-gazette')" class="flex flex-col items-center gap-1 p-2 py-3 text-on-surface-variant hover:text-primary transition-colors flex-1" data-tab="view-gazette">
        <span class="material-symbols-outlined text-[20px]">article</span>
        <span class="text-[10px] font-medium text-center leading-tight" data-i18n="tab_gazette">Gazettes</span>
    </a>'''
)
# About tab - add data-i18n
html = html.replace(
    '''<a href="/static/about.html" class="flex flex-col items-center gap-1 p-2 py-3 text-on-surface-variant hover:text-primary transition-colors flex-1">
        <span class="material-symbols-outlined text-[20px]">info</span>
        <span class="text-[10px] font-medium text-center leading-tight">About</span>
    </a>''',
    '''<a href="/static/about.html" class="flex flex-col items-center gap-1 p-2 py-3 text-on-surface-variant hover:text-primary transition-colors flex-1">
        <span class="material-symbols-outlined text-[20px]">info</span>
        <span class="text-[10px] font-medium text-center leading-tight" data-i18n="tab_about">About</span>
    </a>'''
)

# ============================================================
# 5. Wrap sections into SPA views
# ============================================================
# We need to wrap sections into view-home, view-statutory, view-tkdl, view-classify, view-gazette

# --- VIEW-HOME: Login + Hero ---
# Wrap login section start
html = html.replace(
    '<!-- National Access Gateway - Unified Sovereign Authentication Architecture (Multi-Track SSO) -->',
    '<!-- === VIEW: HOME (Login + Hero) === -->\n<div id="view-home" class="spa-view">\n<!-- National Access Gateway - Unified Sovereign Authentication Architecture (Multi-Track SSO) -->'
)

# Close view-home after Hero section (before guest-sandbox)
# The Hero section ends and Guest Sandbox begins
html = html.replace(
    '<!-- Interactive Public Guest Sandbox ("Try Without Login") -->',
    '</div><!-- /view-home -->\n\n<!-- === VIEW: TKDL & Patent Search === -->\n<div id="view-tkdl" class="spa-view hidden">\n<!-- Interactive Public Guest Sandbox ("Try Without Login") -->'
)

# Close view-tkdl after guest-sandbox (before the 4 Pillar cards)
html = html.replace(
    '<!-- Codified Pillars of Ayurvedic Jurisprudence (4 Card Grid in Dark Theme) -->',
    '</div><!-- /view-tkdl -->\n\n<!-- === VIEW: STATUTORY OVERVIEW === -->\n<div id="view-statutory" class="spa-view hidden">\n<!-- Codified Pillars of Ayurvedic Jurisprudence (4 Card Grid in Dark Theme) -->'
)

# Close view-statutory after Sanskrit Banner (before FAQ)
html = html.replace(
    '<!-- Guest Onboarding Pathway / Quick FAQ Strip -->',
    '</div><!-- /view-statutory -->\n\n<!-- === VIEW: GAZETTE BULLETINS === -->\n<div id="view-gazette" class="spa-view hidden">\n<!-- Guest Onboarding Pathway / Quick FAQ Strip -->'
)

# Close view-gazette before the inline script
html = html.replace(
    '</script></main>',
    '</script>\n</div><!-- /view-gazette -->\n</main>'
)

# --- VIEW-CLASSIFY: We'll create a dedicated classification view ---
# Insert it right before the gazette view closing
# For now, we create a placeholder classification view inside the gazette view area
# Actually, let's insert the classify view between statutory and gazette
html = html.replace(
    '</div><!-- /view-statutory -->',
    '</div><!-- /view-statutory -->\n\n<!-- === VIEW: PRODUCT CLASSIFICATION === -->\n<div id="view-classify" class="spa-view hidden">\n<section class="w-full px-4 lg:px-10 py-8 sm:py-16 bg-surface">\n<div class="max-w-[1360px] mx-auto text-center">\n<div class="inline-flex items-center gap-2 px-3 py-1 rounded bg-primary/10 text-primary font-label-sm text-label-sm uppercase font-bold tracking-wider mb-2">\n<span class="material-symbols-outlined text-[14px]">category</span> Deterministic Classification Engine\n</div>\n<h2 class="font-headline-lg text-headline-lg text-on-surface mb-3" data-i18n="nav_classify">Product Classification Guide</h2>\n<p class="font-body-lg text-body-lg text-on-surface-variant max-w-3xl mx-auto mb-8">Classify your Ayurvedic formulation under the Drugs & Cosmetics Act, 1940 through our 4-step deterministic decision tree. Identify whether your product falls under Classical (Sec 3(a)), Patent & Proprietary (Sec 3(h)), New Drug (NDCT 2019), Phytopharmaceutical, Ayurveda-Aahar (FSSAI), or Cosmetic categories.</p>\n<a href="/static/hub.html" class="inline-flex items-center gap-2 px-6 py-3 rounded bg-primary text-on-primary font-label-lg text-label-lg font-bold hover:bg-primary-fixed transition-colors shadow-md">\n<span class="material-symbols-outlined text-[20px]">play_arrow</span> Launch Classification Wizard in Hub\n</a>\n</div>\n</section>\n</div><!-- /view-classify -->'
)

# ============================================================
# 6. Move the Hero section into view-home (reorder: login first, then hero)
# ============================================================
# The Hero section (Sovereign National Flag + Hero Section) currently comes BEFORE the login.
# We want login FIRST. So we need to move the Masthead + Hero content AFTER the login section.
# 
# Current order inside <main>: Masthead -> Hero -> Sandbox -> Login -> Pillars -> ...
# Desired order: Login -> Masthead -> Hero -> ... (other views)
#
# The simplest approach: Move the login gateway to be at the very start of view-home,
# which is already accomplished by our wrapping above. The Sovereign Masthead and Hero
# are BEFORE view-home, so they appear on every view. That's actually fine for the
# masthead (government branding), but the Hero should be view-specific.
#
# Let's move Hero content into view-home by wrapping it.

# Actually, looking at the current structure more carefully:
# The Masthead sub-bar (भारत सरकार) is between header and hero - it's fine to keep it global.
# The Hero Section should be inside view-home but AFTER the login.
# Currently our view-home wrapping starts at the login gateway.
# The hero section comes BEFORE login in the original HTML.
# So we need to also include the hero in view-home and ensure login renders first visually.
#
# The cleanest approach: Use CSS flex + order to show login first without moving DOM nodes.
# Let me add the hero to view-home and use order classes.

# Wrap the hero section to be part of view-home
html = html.replace(
    '<!-- Hero Section (Unauthenticated Guest View) -->',
    '<div id="hero-section-wrapper" class="order-2">\n<!-- Hero Section (Unauthenticated Guest View) -->'
)

# Close the hero wrapper just before view-home's login gateway starts
html = html.replace(
    '<!-- === VIEW: HOME (Login + Hero) === -->',
    '</div><!-- /hero-section-wrapper -->\n<!-- === VIEW: HOME (Login + Hero) === -->'
)

# Make view-home a flex column
html = html.replace(
    '<div id="view-home" class="spa-view">',
    '<div id="view-home" class="spa-view flex flex-col">'
)

# Give login section order-1 to appear first
html = html.replace(
    '<!-- National Access Gateway - Unified Sovereign Authentication Architecture (Multi-Track SSO) -->\n<section class="w-full px-4 lg:px-10 py-8 sm:py-16 bg-surface" id="national-auth-gateway">',
    '<!-- National Access Gateway - Unified Sovereign Authentication Architecture (Multi-Track SSO) -->\n<section class="w-full px-4 lg:px-10 py-8 sm:py-16 bg-surface order-1" id="national-auth-gateway">'
)

# ============================================================
# 7. Add the showView() routing JS function
# ============================================================
show_view_script = '''
<script>
// SPA View Routing
function showView(viewId) {
    // Hide all views
    document.querySelectorAll('.spa-view').forEach(v => v.classList.add('hidden'));
    // Show target view
    const target = document.getElementById(viewId);
    if (target) {
        target.classList.remove('hidden');
        window.scrollTo({ top: 0, behavior: 'smooth' });
    }
    // Update active state on bottom tabs
    document.querySelectorAll('[data-tab]').forEach(tab => {
        if (tab.getAttribute('data-tab') === viewId) {
            tab.classList.add('text-primary');
            tab.classList.remove('text-on-surface-variant');
        } else {
            tab.classList.remove('text-primary');
            tab.classList.add('text-on-surface-variant');
        }
    });
    // Update active state on desktop nav
    document.querySelectorAll('nav[data-active-classes] a').forEach(link => {
        link.classList.remove('bg-primary-container', 'text-on-primary-container', 'font-semibold', 'rounded');
    });
}

// Show home view by default on page load
document.addEventListener('DOMContentLoaded', () => {
    showView('view-home');
});
</script>
'''
html = html.replace('<script src="/static/i18n.js"></script>', show_view_script + '\n<script src="/static/i18n.js"></script>')

with codecs.open('app/static/index.html', 'w', 'utf-8') as f:
    f.write(html)

print("[OK] index.html SPA routing transformation complete!")
print("  - Added i18n.js script")
print("  - Replaced switchLang with switchLanguage")
print("  - Created SPA views: view-home, view-statutory, view-tkdl, view-classify, view-gazette")
print("  - Wired desktop nav and mobile tabs to showView()")
print("  - Login gateway placed first in view-home via flex order")
print("  - Added showView() routing script")
