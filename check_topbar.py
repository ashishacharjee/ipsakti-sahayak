import codecs
with codecs.open('app/static/index.html', 'r', 'utf-8') as f:
    html = f.read()

idx = html.find('bg-surface-container-high py-1 px-4 lg:px-margin hidden sm:block')
end_idx = html.find('</div>', html.find('data-lang-btn="hi"')) + 6
print(html[idx:end_idx])
