import codecs
import re

html = codecs.open('app/static/index.html', 'r', 'utf-8').read()

html = re.sub(
    r'<span class="material-symbols-outlined text-\[20px\]">person</span>\s*</div>\s*</div></div></div>\s*<!-- Realtime Sovereign Network Pulse Ticker -->',
    '<span class="material-symbols-outlined text-[20px]">person</span>\n</div>\n</div></div>\n<!-- Realtime Sovereign Network Pulse Ticker -->',
    html
)

with codecs.open('app/static/index.html', 'w', 'utf-8') as f:
    f.write(html)
print("Extra div removed using regex!")
