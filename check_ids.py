import codecs
html = codecs.open('app/static/index.html', 'r', 'utf-8').read()
import re
print("hero-section ID:", re.findall(r'id=[\'"]hero-section[\'"]', html))
print("guest-sandbox ID:", re.findall(r'id=[\'"]guest-sandbox[\'"]', html))
print("national-auth-gateway ID:", re.findall(r'id=[\'"]national-auth-gateway[\'"]', html))
