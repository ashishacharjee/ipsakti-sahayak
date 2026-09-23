import codecs

with codecs.open('app/static/hub.html', 'r', 'utf-8') as f:
    hub_html = f.read()

# 1. Fix the big blank space (pb-32 on chatContainer)
hub_html = hub_html.replace('pb-32 pt-6', 'pb-4 pt-6')
hub_html = hub_html.replace('mb-space-xl fade-in-3', 'mb-space-sm fade-in-3') # reduce margin under chat input

# 2. Make the Gazette buttons functional
import re
# We want to replace the href="#" with an onclick for the anchors that contain Read Circular, View Case Law, Download Form
hub_html = re.sub(
    r'<a class="font-label-sm text-label-sm text-primary font-bold hover:text-primary-hover flex items-center gap-1 group w-fit" href="#">\s*<span class="">Read Circular</span>',
    '<a class="font-label-sm text-label-sm text-primary font-bold hover:text-primary-hover flex items-center gap-1 group w-fit cursor-pointer" onclick="setPromptAndSubmit(\'AYUSH Aahar Labeling Guidelines 2024: Permissible classical botanical extracts in food supplements\'); return false;">\n                <span class="">Read Circular</span>',
    hub_html
)

hub_html = re.sub(
    r'<a class="font-label-sm text-label-sm text-primary font-bold hover:text-primary-hover flex items-center gap-1 group w-fit" href="#">\s*<span class="">View Case Law</span>',
    '<a class="font-label-sm text-label-sm text-primary font-bold hover:text-primary-hover flex items-center gap-1 group w-fit cursor-pointer" onclick="setPromptAndSubmit(\'Dabur vs. Controller of Patents 2024: Ashwagandha hydro-ethanolic extraction and Section 3(e) inventive step rulings\'); return false;">\n                <span class="">View Case Law</span>',
    hub_html
)

hub_html = re.sub(
    r'<a class="font-label-sm text-label-sm text-primary font-bold hover:text-primary-hover flex items-center gap-1 group w-fit" href="#">\s*<span class="">Download Form</span>',
    '<a class="font-label-sm text-label-sm text-primary font-bold hover:text-primary-hover flex items-center gap-1 group w-fit cursor-pointer" onclick="setPromptAndSubmit(\'NBA Advisory #12: Biodiversity Form 1 Exemption for Cultivated Herbs and 3.0% ABS exemption\'); return false;">\n                <span class="">Download Form</span>',
    hub_html
)

with codecs.open('app/static/hub.html', 'w', 'utf-8') as f:
    f.write(hub_html)
print("Hub updated with fixed layout and gazette buttons!")
