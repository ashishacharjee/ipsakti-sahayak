import codecs
html = codecs.open('app/static/index.html', 'r', 'utf-8').read()
idx = html.find('id="mobile-nav"')
print(html[max(0,idx-300):idx+50])
