import codecs
import re
import os

# 1. Read index.html
html = codecs.open('app/static/index.html', 'r', 'utf-8').read()

# 2. Extract Hero Section
idx = html.find('id="hero-section-wrapper"')
start = html.rfind('<div', 0, idx)
end = html.find('</section>', idx) + 10

hero_html = html[start:end]

# 3. Create statutory-overview.html using terms.html as a template (to get header/footer right)
terms_html = codecs.open('app/static/terms.html', 'r', 'utf-8').read()

# Replace the <main> content in terms.html with the hero_html
main_start = terms_html.find('<main')
main_content_start = terms_html.find('>', main_start) + 1
main_end = terms_html.find('</main>')

# We want the page to look like a full page, so just put hero_html in main
new_main = f'<main class="w-full pt-16 sm:pt-32 bg-surface min-h-[calc(100vh-280px)]"><div class="flex flex-col w-full">{hero_html}</div></main>'

statutory_html = terms_html[:main_start] + new_main + terms_html[main_end+7:]

# Fix title
statutory_html = statutory_html.replace('<title>Terms of Service - IP-SAKTI Sahayak</title>', '<title>Statutory Overview - IP-SAKTI Sahayak</title>')

with codecs.open('app/static/statutory-overview.html', 'w', 'utf-8') as f:
    f.write(statutory_html)

# 4. Remove Hero Section from index.html
new_index_html = html[:start] + html[end:]

# 5. Fix Links in index.html (both desktop and mobile)
# Statutory Overview -> href="/static/statutory-overview.html"
new_index_html = re.sub(
    r'<a class="([^"]+)" data-path="sovereign-portal-landing" href="[^"]*" onclick="[^"]*">Statutory Overview</a>',
    r'<a class="\1" data-path="sovereign-portal-landing" href="/static/statutory-overview.html">Statutory Overview</a>',
    new_index_html
)
# For mobile nav which might have different classes or onclicks:
new_index_html = re.sub(
    r'<a class="([^"]+)" href="[^"]*" onclick="[^"]*">Statutory Overview</a>',
    r'<a class="\1" href="/static/statutory-overview.html">Statutory Overview</a>',
    new_index_html
)

# TKDL & Patent Search -> href="#guest-sandbox"
new_index_html = re.sub(
    r'<a class="([^"]+)" data-path="tkdl-and-patent-search" href="[^"]*" onclick="[^"]*">TKDL &amp; Patent Search \(Public\)</a>',
    r'<a class="\1" data-path="tkdl-and-patent-search" href="#guest-sandbox">TKDL &amp; Patent Search (Public)</a>',
    new_index_html
)
# Mobile
new_index_html = re.sub(
    r'<a class="([^"]+)" href="[^"]*" onclick="[^"]*">TKDL &amp; Patent Search \(Public\)</a>',
    r'<a class="\1" href="#guest-sandbox">TKDL &amp; Patent Search (Public)</a>',
    new_index_html
)

# Product Classification Guide -> href="#guest-sandbox"
new_index_html = re.sub(
    r'<a class="([^"]+)" data-path="product-classification-guide" href="[^"]*" onclick="[^"]*">Product Classification Guide</a>',
    r'<a class="\1" data-path="product-classification-guide" href="#guest-sandbox">Product Classification Guide</a>',
    new_index_html
)
# Mobile
new_index_html = re.sub(
    r'<a class="([^"]+)" href="[^"]*" onclick="[^"]*">Product Classification Guide</a>',
    r'<a class="\1" href="#guest-sandbox">Product Classification Guide</a>',
    new_index_html
)

# Gazette Bulletins -> href="#national-auth-gateway"
new_index_html = re.sub(
    r'<a class="([^"]+)" data-path="gazette-bulletins" href="[^"]*" onclick="[^"]*">Gazette Bulletins</a>',
    r'<a class="\1" data-path="gazette-bulletins" href="#national-auth-gateway">Gazette Bulletins</a>',
    new_index_html
)
# Mobile
new_index_html = re.sub(
    r'<a class="([^"]+)" href="[^"]*" onclick="[^"]*">Gazette Bulletins</a>',
    r'<a class="\1" href="#national-auth-gateway">Gazette Bulletins</a>',
    new_index_html
)

with codecs.open('app/static/index.html', 'w', 'utf-8') as f:
    f.write(new_index_html)

print("Extraction and link fixes complete!")
