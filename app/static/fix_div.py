import codecs
with codecs.open('app/static/hub.html', 'r', 'utf-8') as f:
    html = f.read()

html = html.replace('</main>', '</div></main>')

with codecs.open('app/static/hub.html', 'w', 'utf-8') as f:
    f.write(html)
