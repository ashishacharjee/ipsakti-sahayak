import codecs
import re

# Read index.html
with codecs.open('app/static/index.html', 'r', 'utf-8') as f:
    index_html = f.read()

# Extract the index.html top bar EXACTLY.
# It starts with: <div class="bg-surface-container-high py-1 px-4 lg:px-margin hidden sm:block">
# And ends after the language switcher div closes.
start_idx = index_html.find('<div class="bg-surface-container-high py-1 px-4 lg:px-margin hidden sm:block">')

# Let's find the end of this div by counting divs.
open_divs = 0
end_idx = -1
for i in range(start_idx, len(index_html)):
    if index_html[i:i+4] == '<div':
        open_divs += 1
    elif index_html[i:i+6] == '</div>':
        open_divs -= 1
        if open_divs == 0:
            end_idx = i + 6
            break

index_topbar = index_html[start_idx:end_idx]

# Now read hub.html
with codecs.open('app/static/hub.html', 'r', 'utf-8') as f:
    hub_html = f.read()

# The hub top bar starts with: <div class="w-full bg-surface-container px-4 sm:px-margin py-1 items-center justify-between text-on-surface border-b border-border-subtle hidden sm:flex">
hub_start = hub_html.find('<div class="w-full bg-surface-container px-4 sm:px-margin py-1 items-center justify-between text-on-surface border-b border-border-subtle hidden sm:flex">')

# Count divs to find the end of the hub top bar
open_divs = 0
hub_end = -1
for i in range(hub_start, len(hub_html)):
    if hub_html[i:i+4] == '<div':
        open_divs += 1
    elif hub_html[i:i+6] == '</div>':
        open_divs -= 1
        if open_divs == 0:
            hub_end = i + 6
            break

# Replace the hub top bar with the index top bar
if hub_start != -1 and hub_end != -1:
    hub_html = hub_html[:hub_start] + index_topbar + hub_html[hub_end:]
    with codecs.open('app/static/hub.html', 'w', 'utf-8') as f:
        f.write(hub_html)
    print("Hub header replaced perfectly with zero bleed!")
else:
    print("Could not find hub top bar bounds.")
