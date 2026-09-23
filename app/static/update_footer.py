import codecs

with codecs.open('app/static/index.html', 'r', 'utf-8') as f:
    html = f.read()

# Current footer looks like:
# <a href="/static/terms.html" class="hover:text-primary transition-colors" data-i18n="footer_terms">Terms of Public Access</a>
# <a href="/static/terms.html" class="hover:text-primary transition-colors" data-i18n="footer_hyperlink">Hyperlink Policy</a>
# <a href="/static/about.html" class="hover:text-primary transition-colors" data-i18n="footer_tkdl_nda">TKDL Non-Disclosure Registry</a>
# <a href="/static/about.html" class="hover:text-primary transition-colors" data-i18n="footer_security">Sovereign Security Audit</a>

html = html.replace('<a href="/static/terms.html" class="hover:text-primary transition-colors" data-i18n="footer_hyperlink">', '<a href="/static/hyperlink.html" class="hover:text-primary transition-colors" data-i18n="footer_hyperlink">')
html = html.replace('<a href="/static/about.html" class="hover:text-primary transition-colors" data-i18n="footer_tkdl_nda">', '<a href="/static/tkdl-nda.html" class="hover:text-primary transition-colors" data-i18n="footer_tkdl_nda">')
html = html.replace('<a href="/static/about.html" class="hover:text-primary transition-colors" data-i18n="footer_security">', '<a href="/static/security-audit.html" class="hover:text-primary transition-colors" data-i18n="footer_security">')

with codecs.open('app/static/index.html', 'w', 'utf-8') as f:
    f.write(html)
