import codecs
html = codecs.open('app/static/index.html', 'r', 'utf-8').read()
idx = html.find('id="mobile-nav"')
idx = html.find('TKDL &amp; Patent Search', idx)
print(html[max(0,idx-250):idx+50])
