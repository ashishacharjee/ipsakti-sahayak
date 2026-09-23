import codecs

html = codecs.open('app/static/statutory-overview.html', 'r', 'utf-8').read()

import re
tokens = []
for m in re.finditer(r'<(div|/div)[^>]*>', html, re.IGNORECASE):
    tag = m.group(1).lower()
    tokens.append((tag, m.start(), m.group(0)))

stack = []
for tag, pos, text in tokens:
    if tag == 'div':
        stack.append((pos, text))
    elif tag == '/div':
        if stack:
            stack.pop()
        else:
            print(f"Extra closing div at char {pos}: {text}")
            print(html[max(0, pos-100):pos+100])

if stack:
    print(f"{len(stack)} unclosed divs:")
    for pos, text in stack:
        print(f"  {text} at {pos}")
