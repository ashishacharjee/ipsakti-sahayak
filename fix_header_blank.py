import codecs

with codecs.open('app/static/hub.html', 'r', 'utf-8') as f:
    hub_html = f.read()

target1 = 'Vedic Jurisprudence AI</span></div></div><nav class="hidden xl:flex items-center gap-space-lg h-16"'
replace1 = 'Vedic Jurisprudence AI</span></div></div></div><nav class="hidden xl:flex items-center gap-space-lg h-16"'

target2 = '</a></nav></div></div>\n<!-- Realtime Sovereign Network Pulse Ticker -->'
replace2 = '</a></nav></div>\n<!-- Realtime Sovereign Network Pulse Ticker -->'

# For safety, let's use regex in case of newlines
import re
hub_html = hub_html.replace(target1, replace1)

# If target2 isn't exact due to newlines:
hub_html = re.sub(r'</a></nav></div></div>\s*<!-- Realtime Sovereign Network Pulse Ticker -->', 
                  '</a></nav></div>\n<!-- Realtime Sovereign Network Pulse Ticker -->', 
                  hub_html)

with codecs.open('app/static/hub.html', 'w', 'utf-8') as f:
    f.write(hub_html)
print("Header spacing layout fixed!")
