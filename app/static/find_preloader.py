import codecs
html = codecs.open('app/static/index.html','r','utf-8').read()
idx = html.find('id="words-preloader"')
print(html[idx:idx+800])
