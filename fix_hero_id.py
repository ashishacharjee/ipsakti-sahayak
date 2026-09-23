import codecs
import re

html = codecs.open('app/static/index.html', 'r', 'utf-8').read()

html = html.replace("getElementById('hero-section')", "getElementById('hero-section-wrapper')")

with codecs.open('app/static/index.html', 'w', 'utf-8') as f:
    f.write(html)
print("hero-section ID fixed!")
