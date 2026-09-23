import codecs
with codecs.open('app/static/hub.html', 'r', 'utf-8') as f:
    html = f.read()

# The second switcher looks like:
second_switcher = '''<div class="flex items-center gap-1 mr-4">
<button class="px-2 py-1 rounded bg-surface-container-high text-text-primary hover:bg-surface-bright transition-colors font-bold text-label-sm border border-border-subtle shadow-xs" onclick="switchLanguage('en')" data-lang-btn="en">EN</button>
<button class="px-2 py-1 rounded text-text-secondary hover:text-text-primary hover:bg-surface-container transition-colors font-medium text-label-sm border border-transparent" onclick="switchLanguage('hi')" data-lang-btn="hi">हिन्दी</button>
</div>\n'''

html = html.replace(second_switcher, '')

with codecs.open('app/static/hub.html', 'w', 'utf-8') as f:
    f.write(html)
