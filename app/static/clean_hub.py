import codecs
import re

with codecs.open('app/static/hub.html', 'r', 'utf-8') as f:
    html = f.read()

# Remove Live Regulatory Pipeline
html = re.sub(r'<!-- Functional Section Split: Live Regulatory Pipeline.*?<!-- Live Statutory Feed', '<!-- Live Statutory Feed', html, flags=re.DOTALL)

# Remove Live Statutory Feed
html = re.sub(r'<!-- Live Statutory Feed & Gazette Precedents.*?<!-- Treatise Concordance', '<!-- Treatise Concordance', html, flags=re.DOTALL)

# Remove Treatise Concordance
html = re.sub(r'<!-- Treatise Concordance Authority & Sub-footer -->.*?</main>', '</main>', html, flags=re.DOTALL)

with codecs.open('app/static/hub.html', 'w', 'utf-8') as f:
    f.write(html)
print("Hub cleaned!")
