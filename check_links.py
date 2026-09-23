import codecs
import re

def check_links(filepath):
    with codecs.open(filepath, 'r', 'utf-8') as f:
        html = f.read()
    links = re.findall(r'href="([^"]+)"', html)
    print(f"--- {filepath} ---")
    for link in sorted(set(links)):
        print(link)

check_links('app/static/index.html')
check_links('app/static/hub.html')
