import codecs

with codecs.open('app/static/index.html', 'r', 'utf-8') as f:
    html = f.read()

# Replace links
html = html.replace(
    '<a class="hover:text-primary transition-colors" href="/static/terms.html">Hyperlink Policy</a>',
    '<a class="hover:text-primary transition-colors" href="/static/hyperlink.html" data-i18n="footer_hyperlink">Hyperlink Policy</a>'
)

html = html.replace(
    '<a class="hover:text-primary transition-colors" href="/static/about.html">TKDL Non-Disclosure Registry</a>',
    '<a class="hover:text-primary transition-colors" href="/static/tkdl-nda.html" data-i18n="footer_tkdl_nda">TKDL Non-Disclosure Registry</a>'
)

html = html.replace(
    '<a class="hover:text-primary transition-colors" href="/static/about.html">Sovereign Security Audit</a>',
    '<a class="hover:text-primary transition-colors" href="/static/security-audit.html" data-i18n="footer_security">Sovereign Security Audit</a>'
)

# And terms of public access
html = html.replace(
    '<a class="hover:text-primary transition-colors" href="/static/terms.html">Terms of Public Access</a>',
    '<a class="hover:text-primary transition-colors" href="/static/terms.html" data-i18n="footer_terms">Terms of Public Access</a>'
)

with codecs.open('app/static/index.html', 'w', 'utf-8') as f:
    f.write(html)
