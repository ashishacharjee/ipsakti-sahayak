import codecs
import re
import os

# Let's get the pristine index.html from git or from the state before my mess?
# I don't have git history right now. I will reconstruct it.
# Currently in index.html, we have:
# <div id="view-statutory" class="spa-view block"> ... </div>
# <div id="view-classify" class="spa-view hidden"> ... </div>
# <div id="view-tkdl" class="spa-view hidden"> ... </div>
# <div id="view-gazette" class="spa-view hidden"> ... </div>

# But wait, I DELETED hero-section-wrapper from index.html earlier!
# I have it in `hero_extract.html`.
hero_html = codecs.open('hero_extract.html', 'r', 'utf-8').read()

html = codecs.open('app/static/index.html', 'r', 'utf-8').read()

# 1. Reconstruct full view-statutory for statutory-overview.html
idx_stat = html.find('id="view-statutory"')
stat_start = html.rfind('<div', 0, idx_stat)
stat_end = html.find('<!-- /view-statutory -->') + len('<!-- /view-statutory -->')

# The remaining view-statutory content in index.html
remaining_stat = html[stat_start:stat_end]

# Full view-statutory is hero_html + remaining_stat (but remaining_stat has the <div id="view-statutory"> wrapper!)
# Let's cleanly inject hero_html back into remaining_stat right after <div id="view-statutory"...>
start_wrapper = html.find('>', stat_start) + 1
full_statutory = html[stat_start:start_wrapper] + hero_html + html[start_wrapper:stat_end]

# 2. Put full_statutory into statutory-overview.html
stat_page = codecs.open('app/static/statutory-overview.html', 'r', 'utf-8').read()
# We need to replace the <main>...</main> in stat_page with full_statutory
# But stat_page currently has <main> ... hero_html ... </main>
main_start = stat_page.find('<main')
main_end = stat_page.find('</main>') + 7
new_main = f'<main class="w-full pt-16 sm:pt-32 bg-surface min-h-[calc(100vh-280px)]"><div class="flex flex-col w-full">{full_statutory}</div></main>'
stat_page = stat_page[:main_start] + new_main + stat_page[main_end:]
with codecs.open('app/static/statutory-overview.html', 'w', 'utf-8') as f:
    f.write(stat_page)

# 3. Remove view-statutory from index.html entirely
new_index = html[:stat_start] + html[stat_end:]

# 4. Make view-tkdl the default block view
new_index = new_index.replace('id="view-tkdl" class="spa-view hidden"', 'id="view-tkdl" class="spa-view block"')

# 5. Fix the Navigation Links in index.html!
# We need to change href="#guest-sandbox" back to href="#" onclick="showView('view-tkdl')"
new_index = re.sub(
    r'<a class="([^"]+)" data-path="tkdl-and-patent-search" href="[^"]*">TKDL &amp; Patent Search \(Public\)</a>',
    r'<a class="\1" data-path="tkdl-and-patent-search" href="#" onclick="event.preventDefault(); showView(\'view-tkdl\');">TKDL &amp; Patent Search (Public)</a>',
    new_index
)

new_index = re.sub(
    r'<a class="([^"]+)" data-path="product-classification-guide" href="[^"]*">Product Classification Guide</a>',
    r'<a class="\1" data-path="product-classification-guide" href="#" onclick="event.preventDefault(); showView(\'view-classify\');">Product Classification Guide</a>',
    new_index
)

new_index = re.sub(
    r'<a class="([^"]+)" data-path="gazette-bulletins" href="[^"]*">Gazette Bulletins</a>',
    r'<a class="\1" data-path="gazette-bulletins" href="#" onclick="event.preventDefault(); showView(\'view-gazette\');">Gazette Bulletins</a>',
    new_index
)

# And for Mobile Nav
new_index = re.sub(
    r'<a class="([^"]+)" href="[^"]*">TKDL &amp; Patent Search \(Public\)</a>',
    r'<a class="\1" href="#" onclick="event.preventDefault(); document.getElementById(\'mobile-nav\').classList.add(\'hidden\'); showView(\'view-tkdl\');">TKDL &amp; Patent Search (Public)</a>',
    new_index
)

new_index = re.sub(
    r'<a class="([^"]+)" href="[^"]*">Product Classification Guide</a>',
    r'<a class="\1" href="#" onclick="event.preventDefault(); document.getElementById(\'mobile-nav\').classList.add(\'hidden\'); showView(\'view-classify\');">Product Classification Guide</a>',
    new_index
)

new_index = re.sub(
    r'<a class="([^"]+)" href="[^"]*">Gazette Bulletins</a>',
    r'<a class="\1" href="#" onclick="event.preventDefault(); document.getElementById(\'mobile-nav\').classList.add(\'hidden\'); showView(\'view-gazette\');">Gazette Bulletins</a>',
    new_index
)

with codecs.open('app/static/index.html', 'w', 'utf-8') as f:
    f.write(new_index)

print("Restored SPA architecture and extracted full statutory overview!")
