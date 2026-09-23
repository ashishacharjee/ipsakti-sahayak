import codecs
html = codecs.open('app/static/index.html', 'r', 'utf-8').read()
start = html.find('id="view-classify"')
end = html.find('<!-- /view-classify -->')
print(html[start:end])
