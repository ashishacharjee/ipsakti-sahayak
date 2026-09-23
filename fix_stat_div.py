import codecs
html = codecs.open('app/static/statutory-overview.html', 'r', 'utf-8').read()
# Add </div> after </section> of the hero
html = html.replace('</section>\n<!-- Educational Explainer: TKDL IP Precedents -->', '</section>\n</div>\n<!-- Educational Explainer: TKDL IP Precedents -->')
with codecs.open('app/static/statutory-overview.html', 'w', 'utf-8') as f:
    f.write(html)
print("Fixed missing div in statutory-overview.html")
