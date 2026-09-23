import codecs
import re

with codecs.open('app/static/index.html', 'r', 'utf-8') as f:
    html = f.read()

skip_btn = '''
    <!-- Skip Animation Button -->
    <button id="skip-preloader-btn" class="absolute bottom-6 right-6 z-[1001] pointer-events-auto text-white hover:text-white flex items-center gap-2 font-semibold transition-colors bg-black/30 hover:bg-black/50 px-5 py-2.5 rounded-full backdrop-blur-md border border-white/30 cursor-pointer shadow-lg" onclick="skipPreloader()">
        <span>Skip Animation</span>
        <span class="material-symbols-outlined text-[20px]">fast_forward</span>
    </button>
  </div>'''

# Replace the closing div of the preloader
html = re.sub(r'</svg>\s*</div>', '</svg>' + skip_btn, html)

# Add skipPreloader function to the SPA View Routing script block
script_find = '// SPA View Routing'
script_replace = '''// Skip Preloader
function skipPreloader() {
    const preloaderEl = document.getElementById("words-preloader");
    if (preloaderEl) {
        preloaderEl.style.transform = 'translateY(-100%)';
        setTimeout(() => {
            preloaderEl.style.display = 'none';
        }, 1200);
        window.dispatchEvent(new Event('skipAnimation'));
    }
}

// SPA View Routing'''

html = html.replace(script_find, script_replace)

# Footer links replacement
# We need to replace href="/static/terms.html" with hyperlink.html only for the specific data-i18n
html = re.sub(r'<a href="[^"]*?"([^>]*?data-i18n="footer_hyperlink"|[^>]*?Hyperlink Policy)', r'<a href="/static/hyperlink.html"\1', html)
html = re.sub(r'<a href="[^"]*?"([^>]*?data-i18n="footer_tkdl_nda"|[^>]*?TKDL Non-Disclosure Registry)', r'<a href="/static/tkdl-nda.html"\1', html)
html = re.sub(r'<a href="[^"]*?"([^>]*?data-i18n="footer_security"|[^>]*?Sovereign Security Audit)', r'<a href="/static/security-audit.html"\1', html)

with codecs.open('app/static/index.html', 'w', 'utf-8') as f:
    f.write(html)

print("Updated index.html!")
