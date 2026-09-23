import codecs

# 1. Get the beautiful top bar from index.html
with codecs.open('app/static/index.html', 'r', 'utf-8') as f:
    index_html = f.read()

# The top bar in index.html is from <div class="bg-surface-container-high py-1 px-4 lg:px-margin hidden sm:block"> to the next </div></div></div>
start_topbar = index_html.find('<div class="bg-surface-container-high py-1 px-4 lg:px-margin hidden sm:block">')
end_topbar = index_html.find('</div>\n    <div class="h-16 w-full px-4 lg:px-margin flex items-center justify-between">')
if end_topbar == -1:
    end_topbar = index_html.find('<div class="h-16 w-full px-4 lg:px-margin flex items-center justify-between">') - 6

index_topbar = index_html[start_topbar:end_topbar] + "</div>"

# 2. Get hub.html and replace its top bar
with codecs.open('app/static/hub.html', 'r', 'utf-8') as f:
    hub_html = f.read()

# hub's top bar
start_hub_topbar = hub_html.find('<div class="w-full bg-surface-container px-4 sm:px-margin py-1 items-center justify-between text-on-surface border-b border-border-subtle hidden sm:flex">')
end_hub_topbar = hub_html.find('<div class="h-14 sm:h-16 w-full px-4 sm:px-margin flex items-center justify-between">')

# We want to replace hub's top bar with index's top bar.
hub_html = hub_html[:start_hub_topbar] + index_topbar + "\n" + hub_html[end_hub_topbar:]

# Also fix the missing EN/HI button in hub.html that failed earlier!
# Let's put it next to the person icon
person_icon_idx = hub_html.find('id="clerk-mount-point">')
if person_icon_idx != -1:
    # Go back to the <div that starts clerk-mount-point
    div_start = hub_html.rfind('<div', 0, person_icon_idx)
    
    lang_switcher = '''<div class="flex items-center gap-1 mr-4">
<button class="px-2 py-1 rounded bg-surface-container-high text-text-primary hover:bg-surface-bright transition-colors font-bold text-label-sm border border-border-subtle shadow-xs" onclick="switchLanguage('en')" data-lang-btn="en">EN</button>
<button class="px-2 py-1 rounded text-text-secondary hover:text-text-primary hover:bg-surface-container transition-colors font-medium text-label-sm border border-transparent" onclick="switchLanguage('hi')" data-lang-btn="hi">हिन्दी</button>
</div>\n'''
    hub_html = hub_html[:div_start] + lang_switcher + hub_html[div_start:]

with codecs.open('app/static/hub.html', 'w', 'utf-8') as f:
    f.write(hub_html)
print("Hub header unified!")
