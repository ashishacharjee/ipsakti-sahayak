import codecs
import re
import os

topbar_html = '''<!-- Unified Top Bar -->
<div class="bg-surface-container-high py-1 px-4 lg:px-margin hidden sm:block border-b border-border-subtle z-[60] relative w-full">
  <div class="max-w-[1360px] mx-auto flex items-center justify-between font-label-sm text-label-sm text-text-secondary">
    <div>
      <span class="font-semibold text-primary" data-i18n="gov_title">GOVERNMENT OF INDIA</span> 
      <span class="text-border-strong mx-2">|</span> 
      <span data-i18n="ministry">Ministry of AYUSH • CSIR-TKDL Statutory Interface</span>
    </div>
    
    <div class="flex items-center gap-space-md">
      <div class="flex items-center gap-2">
        <a href="#" class="flex items-center gap-1 hover:text-primary transition-colors" title="Screen Reader Access">
            <span class="material-symbols-outlined text-[14px]">accessibility_new</span>
            <span data-i18n="screen_reader">Screen Reader Access</span>
        </a>
        <span class="text-outline-variant mx-1">|</span>
        <div class="flex items-center gap-1 font-medium">
            <button class="px-1 hover:text-primary transition-colors text-[11px]" onclick="document.body.style.zoom='0.9'">A-</button>
            <button class="px-1 hover:text-primary transition-colors text-[13px]" onclick="document.body.style.zoom='1.0'">A</button>
            <button class="px-1 hover:text-primary transition-colors text-[15px]" onclick="document.body.style.zoom='1.1'">A+</button>
        </div>
      </div>

      <span class="text-outline-variant hidden sm:inline">|</span>

      <div class="flex items-center gap-2">
        <button class="px-2 py-0.5 rounded bg-surface-container text-on-surface hover:bg-surface-bright transition-colors font-bold text-label-sm shadow-xs border border-border-subtle" onclick="switchLanguage('en')" data-lang-btn="en">EN</button>
        <button class="px-2 py-0.5 rounded text-on-surface-variant hover:text-on-surface hover:bg-surface-container transition-colors font-medium text-label-sm border border-transparent" onclick="switchLanguage('hi')" data-lang-btn="hi">हिन्दी</button>
      </div>
    </div>
  </div>
</div>
'''

files_to_fix = [
    'terms.html',
    'security-audit.html',
    'hyperlink.html',
    'tkdl-nda.html',
    'statutory-overview.html'
]

for filename in files_to_fix:
    filepath = os.path.join('app/static', filename)
    if not os.path.exists(filepath):
        continue
    
    with codecs.open(filepath, 'r', 'utf-8') as f:
        html = f.read()

    # Find the start of the <body tag
    body_start = html.find('<body class="bg-vedic-parchment text-vedic-textPrimar')
    if body_start != -1:
        # Find the end of the corrupted body tag
        body_end = html.find('y antialiased selection:bg-indigo-500/30">', body_start)
        if body_end != -1:
            body_end += len('y antialiased selection:bg-indigo-500/30">')
            
            # Reconstruct correctly
            correct_body = '<body class="bg-vedic-parchment text-vedic-textPrimary antialiased selection:bg-indigo-500/30">\n' + topbar_html
            
            html = html[:body_start] + correct_body + html[body_end:]
            
            with codecs.open(filepath, 'w', 'utf-8') as f:
                f.write(html)
            print(f"Fixed {filename}")
