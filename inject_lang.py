import codecs
import re

with codecs.open('app/static/hub.html', 'r', 'utf-8') as f:
    hub_html = f.read()

target_str = '<span class="font-code text-code text-on-surface-variant font-medium">FastAPI Live | v2.4 Sovereign</span>'
idx = hub_html.find(target_str)

if idx != -1:
    # Find the closing div of the FastApi Live container
    end_div_idx = hub_html.find('</div>', idx)
    
    lang_switcher = '''
<div class="flex items-center gap-1 ml-4 border-l border-border-subtle pl-4">
<button class="px-2 py-0.5 rounded bg-surface-container-high text-on-surface hover:bg-surface-bright transition-colors font-bold text-label-sm shadow-xs border border-border-subtle" onclick="switchLanguage('en')" data-lang-btn="en">EN</button>
<button class="px-2 py-0.5 rounded text-on-surface-variant hover:text-on-surface hover:bg-surface-container transition-colors font-medium text-label-sm border border-transparent" onclick="switchLanguage('hi')" data-lang-btn="hi">हिन्दी</button>
</div>'''
    
    insert_pos = end_div_idx + 6
    hub_html = hub_html[:insert_pos] + lang_switcher + hub_html[insert_pos:]
    
    with codecs.open('app/static/hub.html', 'w', 'utf-8') as f:
        f.write(hub_html)
    print("Language switcher injected cleanly!")
else:
    print("Target string not found.")
