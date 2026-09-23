import codecs

with codecs.open('app/static/index.html', 'r', 'utf-8') as f:
    index_html = f.read()

start_idx = index_html.find('<div class="bg-surface-container-high py-1 px-4 lg:px-margin hidden sm:block">')
end_idx = index_html.find('</div>\n    <div class="h-16')
if end_idx == -1:
    end_idx = index_html.find('</div>\n        <div class="h-16')
if end_idx == -1:
    # Just find it manually
    end_idx = index_html.find('</div>', index_html.find('data-lang-btn="hi"')) + 6
    end_idx = index_html.find('</div>', end_idx) + 6
    end_idx = index_html.find('</div>', end_idx) + 6

index_topbar = index_html[start_idx:end_idx]

with codecs.open('scratch/topbar.html', 'w', 'utf-8') as f:
    f.write(index_topbar)
