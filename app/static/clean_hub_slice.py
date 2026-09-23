import codecs

with codecs.open('app/static/hub.html', 'r', 'utf-8') as f:
    html = f.read()

start_idx = html.find('<!-- Functional Section Split: Live Regulatory Pipeline')
end_idx = html.find('</main>')

if start_idx != -1 and end_idx != -1:
    html = html[:start_idx] + '\n        </div>\n    </div>\n' + html[end_idx:]
    with codecs.open('app/static/hub.html', 'w', 'utf-8') as f:
        f.write(html)
    print("Hub completely cleaned!")
else:
    print("Could not find boundaries")
