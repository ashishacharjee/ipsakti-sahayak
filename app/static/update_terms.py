import codecs
import re

with codecs.open('app/static/terms.html', 'r', 'utf-8') as f:
    html = f.read()

# 1. Remove Night Mode Icon
html = re.sub(
    r'<button aria-label="Toggle Theme Mode".*?</button>',
    '',
    html, flags=re.DOTALL
)

# 2. Make AsciiGlitchRipple apply to h2 as well
html = html.replace(
    "const mainTitle = document.querySelector('h1');\n    if (mainTitle) {\n        new AsciiGlitchRipple(mainTitle, { spread: 1.0, dur: 800 });\n    }",
    "document.querySelectorAll('h1, h2').forEach(el => new AsciiGlitchRipple(el, { spread: 1.0, dur: 800 }));"
)

# 3. Shift FAQ to the left sidebar
# The FAQ section starts with <!-- FAQ Section --> and ends before </body>
faq_match = re.search(r'<!-- FAQ Section -->.*?</div>\s*<script>\s*function toggleFaq.*?</script>', html, re.DOTALL)
if faq_match:
    faq_code = faq_match.group(0)
    # Remove it from the bottom
    html = html.replace(faq_code, '')
    
    # Scale down text sizes in FAQ for sidebar
    faq_code = faq_code.replace('max-w-3xl mx-auto py-16', 'w-full py-8 border-t border-vedic-border mt-8 pt-8')
    faq_code = faq_code.replace('text-2xl md:text-3xl mb-10', 'text-sm font-bold text-vedic-textMuted uppercase tracking-widest mb-4')
    faq_code = faq_code.replace('IP-SAKTI Sahayak FAQs', 'FAQs')
    
    # Insert it into the <aside>
    html = html.replace('</aside>', f'{faq_code}\n        </aside>')

with codecs.open('app/static/terms.html', 'w', 'utf-8') as f:
    f.write(html)
