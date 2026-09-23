import codecs

with codecs.open('app/static/index.html', 'r', 'utf-8') as f:
    html = f.read()

# Fix header overlapping content in index.html
html = html.replace('pt-16 sm:pt-32', 'pt-32 sm:pt-44')

with codecs.open('app/static/index.html', 'w', 'utf-8') as f:
    f.write(html)
print("Index.html padding increased!")
