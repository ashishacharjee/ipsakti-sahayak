import codecs
import re

html = codecs.open('app/static/index.html', 'r', 'utf-8').read()

# Remove the literal backslashes
html = html.replace("\\'", "'")

# Make sure hero-section is hero-section-wrapper
html = html.replace("getElementById('hero-section')", "getElementById('hero-section-wrapper')")

with codecs.open('app/static/index.html', 'w', 'utf-8') as f:
    f.write(html)
print("Removed syntax error backslashes and fixed hero ID!")
