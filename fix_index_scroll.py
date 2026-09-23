import codecs
import re

html = codecs.open('app/static/index.html', 'r', 'utf-8').read()

# Replace the alert with smooth scrolling
html = re.sub(
    r'<a class="([^"]+)" data-path="sovereign-portal-landing" href="#" onclick="[^"]+">Statutory Overview</a>',
    r'<a class="\1" data-path="sovereign-portal-landing" href="#" onclick="event.preventDefault(); document.getElementById(\'hero-section\').scrollIntoView({behavior:\'smooth\'});">Statutory Overview</a>',
    html
)

html = re.sub(
    r'<a class="([^"]+)" data-path="tkdl-and-patent-search" href="#" onclick="[^"]+">TKDL &amp; Patent Search \(Public\)</a>',
    r'<a class="\1" data-path="tkdl-and-patent-search" href="#" onclick="event.preventDefault(); document.getElementById(\'guest-sandbox\').scrollIntoView({behavior:\'smooth\'});">TKDL &amp; Patent Search (Public)</a>',
    html
)

html = re.sub(
    r'<a class="([^"]+)" data-path="product-classification-guide" href="#" onclick="[^"]+">Product Classification Guide</a>',
    r'<a class="\1" data-path="product-classification-guide" href="#" onclick="event.preventDefault(); document.getElementById(\'guest-sandbox\').scrollIntoView({behavior:\'smooth\'});">Product Classification Guide</a>',
    html
)

html = re.sub(
    r'<a class="([^"]+)" data-path="gazette-bulletins" href="#" onclick="[^"]+">Gazette Bulletins</a>',
    r'<a class="\1" data-path="gazette-bulletins" href="#" onclick="event.preventDefault(); document.getElementById(\'national-auth-gateway\').scrollIntoView({behavior:\'smooth\'});">Gazette Bulletins</a>',
    html
)

with codecs.open('app/static/index.html', 'w', 'utf-8') as f:
    f.write(html)
print("Index.html nav links wired to scroll!")
