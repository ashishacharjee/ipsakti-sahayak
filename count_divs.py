import codecs
import re

html = codecs.open('app/static/index.html', 'r', 'utf-8').read()

def count_divs(text):
    opens = len(re.findall(r'<div[^>]*>', text, re.IGNORECASE))
    closes = len(re.findall(r'</div[^>]*>', text, re.IGNORECASE))
    return opens, closes

print('Header:', count_divs(html[:html.rfind('<div', 0, html.find('id="view-tkdl"'))]))
print('view-tkdl:', count_divs(html[html.rfind('<div', 0, html.find('id="view-tkdl"')):html.find('<!-- /view-tkdl -->')]))
print('view-classify:', count_divs(html[html.rfind('<div', 0, html.find('id="view-classify"')):html.find('<!-- /view-classify -->')]))
print('view-gazette:', count_divs(html[html.rfind('<div', 0, html.find('id="view-gazette"')):html.find('<!-- /view-gazette -->')]))
print('Footer:', count_divs(html[html.find('<!-- /view-gazette -->'):]))
