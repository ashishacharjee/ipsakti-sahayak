import codecs

with codecs.open('app/static/hub.html', 'r', 'utf-8') as f:
    hub_html = f.read()

# Fix View Case Law
target_law = 'gap-0.5">View Case Law'
replace_law = 'gap-0.5" onclick="setPromptAndSubmit(\'Dabur vs. Controller of Patents 2024: Ashwagandha hydro-ethanolic extraction and Section 3(e) inventive step rulings\'); return false;">View Case Law'
hub_html = hub_html.replace(target_law, replace_law)

# Fix Download Form
target_form = 'gap-0.5">Download Form'
replace_form = 'gap-0.5" onclick="setPromptAndSubmit(\'NBA Advisory #12: Biodiversity Form 1 Exemption for Cultivated Herbs and 3.0% ABS exemption\'); return false;">Download Form'
hub_html = hub_html.replace(target_form, replace_form)

# Let's also check Read Circular just to be safe, because my previous regex was wrong too but maybe it matched something else?
# Wait, in the debug for circular... I didn't debug it. Let me check if Circular is actually clickable.
target_circ = 'gap-0.5">Read Circular'
replace_circ = 'gap-0.5" onclick="setPromptAndSubmit(\'AYUSH Aahar Labeling Guidelines 2024: Permissible classical botanical extracts in food supplements\'); return false;">Read Circular'
hub_html = hub_html.replace(target_circ, replace_circ)

with codecs.open('app/static/hub.html', 'w', 'utf-8') as f:
    f.write(hub_html)
print("Gazette buttons re-fixed!")
