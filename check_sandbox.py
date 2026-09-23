import codecs
import re

html = codecs.open('app/static/index.html', 'r', 'utf-8').read()
m = re.search(r'<[^>]+id=[\'"]guest-sandbox[\'"][^>]*>', html)
print(m.group(0) if m else "Not found")
