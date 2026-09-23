import codecs
html = codecs.open('app/static/index.html', 'r', 'utf-8').read()
idx = html.find("getElementById('mobile-nav').classList.toggle")
if idx == -1:
    idx = html.find("getElementById('mobile-nav').classList.remove")
print("Found toggle/remove:", idx != -1)
if idx != -1:
    print(html[max(0,idx-200):idx+100])
