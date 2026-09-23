import codecs

with codecs.open('app/static/index.html', 'r', 'utf-8') as f:
    html = f.read()

skip_btn = '''
    <!-- Skip Animation Button -->
    <button id="skip-preloader-btn" class="absolute bottom-6 right-6 z-[1001] pointer-events-auto text-white hover:text-white flex items-center gap-2 font-semibold transition-colors bg-black/30 hover:bg-black/50 px-5 py-2.5 rounded-full backdrop-blur-md border border-white/30 cursor-pointer shadow-lg" onclick="skipPreloader()">
        <span>Skip Animation</span>
        <span class="material-symbols-outlined text-[20px]">fast_forward</span>
    </button>
  </div>'''

html = html.replace('</svg>\n      \n  </div>', '</svg>' + skip_btn)

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
        // Dispatch event so app.js can clear its intervals if needed
        window.dispatchEvent(new Event('skipAnimation'));
    }
}

// SPA View Routing'''

html = html.replace(script_find, script_replace)

with codecs.open('app/static/index.html', 'w', 'utf-8') as f:
    f.write(html)
