import codecs
import re

html = codecs.open('app/static/index.html', 'r', 'utf-8').read()

# Replace mobile nav links
html = re.sub(
    r'<a class="([^"]+)" href="#" onclick="alert\(\'Access Restricted[^\']+\'\); document.getElementById\(\'mobile-nav\'\)\.classList\.add\(\'hidden\'\)">TKDL &amp; Patent Search</a>',
    r'<a class="\1" href="#" onclick="event.preventDefault(); document.getElementById(\'mobile-nav\').classList.add(\'hidden\'); showView(\'view-tkdl\');">TKDL &amp; Patent Search</a>',
    html
)

html = re.sub(
    r'<a class="([^"]+)" href="#" onclick="alert\(\'Access Restricted[^\']+\'\); document.getElementById\(\'mobile-nav\'\)\.classList\.add\(\'hidden\'\)">Product Classification Guide</a>',
    r'<a class="\1" href="#" onclick="event.preventDefault(); document.getElementById(\'mobile-nav\').classList.add(\'hidden\'); showView(\'view-classify\');">Product Classification Guide</a>',
    html
)

html = re.sub(
    r'<a class="([^"]+)" href="#" onclick="alert\(\'Access Restricted[^\']+\'\); document.getElementById\(\'mobile-nav\'\)\.classList\.add\(\'hidden\'\)">Gazette Bulletins</a>',
    r'<a class="\1" href="#" onclick="event.preventDefault(); document.getElementById(\'mobile-nav\').classList.add(\'hidden\'); showView(\'view-gazette\');">Gazette Bulletins</a>',
    html
)

with codecs.open('app/static/index.html', 'w', 'utf-8') as f:
    f.write(html)
print("Mobile nav links fixed!")
