import codecs

html = codecs.open('app/static/index.html', 'r', 'utf-8').read()
idx = html.find('id="view-statutory"')
if idx != -1:
    end = html.find('<!-- /view-statutory -->')
    with codecs.open('debug_view.txt', 'w', 'utf-8') as f:
        f.write(html[idx-100:end+100])
