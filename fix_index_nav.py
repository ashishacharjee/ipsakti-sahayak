import codecs
import re

html = codecs.open('app/static/index.html', 'r', 'utf-8').read()

# Replace showView(...) with an alert in index.html
html = re.sub(
    r'onclick="event\.preventDefault\(\);\s*showView\(\'[^\']+\'\)"',
    r'''onclick="event.preventDefault(); alert('Access Restricted: Requires Sovereign Portal Authentication. Try the Guest Sandbox below.');"''',
    html
)

with codecs.open('app/static/index.html', 'w', 'utf-8') as f:
    f.write(html)
print("Fixed JS ReferenceErrors in index.html desktop nav!")
