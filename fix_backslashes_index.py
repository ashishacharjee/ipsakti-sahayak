import codecs

html = codecs.open('app/static/index.html', 'r', 'utf-8').read()

# Fix literal backslashes
html = html.replace("\\'", "'")

with codecs.open('app/static/index.html', 'w', 'utf-8') as f:
    f.write(html)
print("Removed syntax error backslashes from index.html")
