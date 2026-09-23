import codecs
import re

html = codecs.open('app/static/index.html', 'r', 'utf-8').read()

html = html.replace("event.preventDefault(); ", "")
html = html.replace("scrollIntoView({behavior:'smooth'});", "scrollIntoView({behavior:'smooth'}); return false;")
html = html.replace('scrollIntoView({behavior:\\\'smooth\\\'});">', 'scrollIntoView({behavior:\\\'smooth\\\'}); return false;">')

with codecs.open('app/static/index.html', 'w', 'utf-8') as f:
    f.write(html)
print("Removed event.preventDefault() and added return false;")
