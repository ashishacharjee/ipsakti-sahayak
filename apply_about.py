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

def replace_topbar(filepath, is_main=True):
    if not os.path.exists(filepath):
        return
    with codecs.open(filepath, 'r', 'utf-8') as f:
        html = f.read()

    if is_main:
        start_idx = html.find('<div class="bg-surface-container-high py-1 px-4 lg:px-margin hidden sm:block"')
        if start_idx != -1:
            open_divs = 0
            end_idx = -1
            for i in range(start_idx, len(html)):
                if html[i:i+4] == '<div':
                    open_divs += 1
                elif html[i:i+6] == '</div>':
                    open_divs -= 1
                    if open_divs == 0:
                        end_idx = i + 6
                        break
            if end_idx != -1:
                old_unified = html.find('<!-- Unified Top Bar -->')
                if old_unified != -1 and old_unified < start_idx:
                    html = html[:old_unified] + topbar_html + html[end_idx:]
                else:
                    html = html[:start_idx] + topbar_html + html[end_idx:]
    else:
        if '<!-- Unified Top Bar -->' in html:
            start = html.find('<!-- Unified Top Bar -->')
            end = html.find('</div>\n', html.find('data-lang-btn="hi"')) + 7
            if end == -1 or end < start: # fallback
                 end = html.find('</div>', html.find('data-lang-btn="hi"')) + 6
                 if html[end:end+6] == '</div>': end += 6
                 if html[end:end+6] == '</div>': end += 6
                 if html[end:end+6] == '</div>': end += 6
            html = html[:start] + topbar_html + html[end:]
        else:
            body_match = re.search(r'<body[^>]*>', html)
            if body_match:
                end_body = body_match.end()
                if 'i18n.js' not in html:
                    head_end = html.find('</head>')
                    html = html[:head_end] + '  <script src="/static/i18n.js"></script>\n' + html[head_end:]
                html = html[:end_body] + '\n' + topbar_html + html[end_body:]

    with codecs.open(filepath, 'w', 'utf-8') as f:
        f.write(html)
    print(f"Updated {filepath}")

replace_topbar('app/static/about.html', False)

# Fix about.html circle overlapping 'Engine'
with codecs.open('app/static/about.html', 'r', 'utf-8') as f:
    about_html = f.read()

target_circle = '<span class="absolute right-[0.45em] top-[0.1em] w-[0.25em] h-[0.25em] bg-white rounded-full"></span>'
if target_circle in about_html:
    about_html = about_html.replace(target_circle, '')
    with codecs.open('app/static/about.html', 'w', 'utf-8') as f:
        f.write(about_html)
    print("Fixed overlapping circle in about.html")
