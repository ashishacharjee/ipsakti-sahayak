import codecs
html = codecs.open('app/static/index.html', 'r', 'utf-8').read()
start = html.rfind('<div', 0, html.find('id="view-gazette"'))
end = html.find('<!-- /view-gazette -->')
with codecs.open('dump_gazette.html', 'w', 'utf-8') as f:
    f.write(html[start:end])
