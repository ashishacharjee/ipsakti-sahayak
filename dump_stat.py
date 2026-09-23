import codecs

html = codecs.open('app/static/statutory-overview.html', 'r', 'utf-8').read()
with codecs.open('debug_stat.txt', 'w', 'utf-8') as f:
    f.write(html[:5000])
