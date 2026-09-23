import codecs
import re

# 1. Fix statutory-overview.html
filepath = 'app/static/statutory-overview.html'
html = codecs.open(filepath, 'r', 'utf-8').read()

# I need to add </div> right before </main>
if '</main>' in html:
    html = html.replace('</main>', '</div>\n</main>')
    with codecs.open(filepath, 'w', 'utf-8') as f:
        f.write(html)
    print("Fixed statutory-overview.html div balance.")

# 2. Fix index.html
filepath = 'app/static/index.html'
html = codecs.open(filepath, 'r', 'utf-8').read()

# I need to find the stray </div>
# In check_divs.py it said it was right before <!-- /view-gazette --> ?
# Wait! "tContent = val + '... \n  })();\n</script>\n</div><!-- /view-gazette -->\n</main>"
# The extra div was there because all the divs before it didn't match.
# Wait, if the extra div was left where the hero section used to be:
# The hero section was right before "<!-- Four Pillars of Sovereign Intelligence -->".
# So there should be a `</div>` right before `<!-- Four Pillars of Sovereign Intelligence -->`.
# Let's check!
idx = html.find('<!-- Four Pillars of Sovereign Intelligence -->')
if idx != -1:
    snippet = html[max(0, idx-50):idx]
    print("Before Four Pillars:", repr(snippet))
    if '</div>' in snippet:
        # Remove the LAST '</div>' before the Four Pillars.
        stray_idx = html.rfind('</div>', 0, idx)
        html = html[:stray_idx] + html[stray_idx+6:]
        with codecs.open(filepath, 'w', 'utf-8') as f:
            f.write(html)
        print("Fixed index.html div balance.")
