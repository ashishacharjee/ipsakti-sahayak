import codecs

html = codecs.open('app/static/index.html', 'r', 'utf-8').read()
# Replace the very last </div> before <!-- /view-gazette -->
idx = html.find('<!-- /view-gazette -->')
# We know the extra </div> is exactly the last </div> before the comment
last_div_idx = html.rfind('</div>', 0, idx)
# Remove it
html = html[:last_div_idx] + html[last_div_idx+6:]

with codecs.open('app/static/index.html', 'w', 'utf-8') as f:
    f.write(html)
print("Removed extra div from view-gazette in index.html")
