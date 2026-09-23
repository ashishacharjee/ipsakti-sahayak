import codecs
html = codecs.open('app/static/index.html', 'r', 'utf-8').read()
idx = html.find('id="hero-section-wrapper"')
start = html.rfind('<div', 0, idx)
end = html.find('</section>', idx) + 10
with codecs.open('hero_extract.html', 'w', 'utf-8') as f:
    f.write(html[start:end])
print("Hero extracted.")
