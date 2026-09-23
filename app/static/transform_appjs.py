"""
Clean up app.js:
1. Remove translateUI() function (Google Translate cookie mechanism)
2. Remove window.switchLang (Google Translate wrapper)
3. Remove the old in-memory translations dictionary and langSelect listener
4. Remove dead currentTheme variable
5. Remove toggleDarkMode and dark-theme auto-apply (if still present)
6. Add language param to generatePayload()
7. Clean up duplicate function definitions
"""
import codecs
import re

with codecs.open('app/static/app.js', 'r', 'utf-8') as f:
    js = f.read()

# ============================================================
# 1. Remove translateUI function
# ============================================================
js = re.sub(
    r'function translateUI\(lang\)\s*\{.*?\n\}',
    '// translateUI removed - using native i18n.js instead',
    js, flags=re.DOTALL
)

# ============================================================
# 2. Remove window.switchLang (Google Translate wrapper)
# ============================================================
js = re.sub(
    r'window\.switchLang\s*=\s*function\s*\(lang\)\s*\{[^}]*translateUI[^}]*\};?',
    '// window.switchLang removed - using switchLanguage() from i18n.js',
    js, flags=re.DOTALL
)

# ============================================================
# 3. Remove the old in-memory translations dictionary
# ============================================================
# This is a large block starting with "const translations = {" or "let translations = {"
js = re.sub(
    r'(?:const|let|var)\s+translations\s*=\s*\{[^;]*\};',
    '// Old translations dictionary removed - using i18n.js',
    js, flags=re.DOTALL
)

# Remove the langSelect change listener block
js = re.sub(
    r'(?:const|let|var)\s+langSelect\s*=\s*document\.getElementById\([\'"]langSelect[\'"]\);.*?(?=\n\s*(?:function|window\.|let |const |var |\/\/|$))',
    '// langSelect listener removed - using i18n.js\n',
    js, flags=re.DOTALL
)

# ============================================================
# 4. Remove dead currentTheme variable
# ============================================================
js = re.sub(r"let currentTheme\s*=\s*'light';", '// currentTheme removed (dead code)', js)

# ============================================================
# 5. Remove toggleDarkMode if still present
# ============================================================
js = re.sub(
    r'function toggleDarkMode\(\)\s*\{.*?\n\}',
    '',
    js, flags=re.DOTALL
)

# ============================================================
# 6. Add language to generatePayload()
# ============================================================
# The generatePayload function is inside submitChat(). We need to add language field.
js = js.replace(
    'query: q, \n            jurisdiction: "dual"',
    'query: q, \n            jurisdiction: "dual",\n            language: (typeof getCurrentLanguage === "function") ? getCurrentLanguage() : "en"'
)
# Also try alternate formatting
js = js.replace(
    "query: q, \n            jurisdiction: 'dual'",
    "query: q, \n            jurisdiction: 'dual',\n            language: (typeof getCurrentLanguage === 'function') ? getCurrentLanguage() : 'en'"
)

with codecs.open('app/static/app.js', 'w', 'utf-8') as f:
    f.write(js)

print("[OK] app.js cleanup complete!")
print("  - Removed translateUI (Google Translate cookies)")
print("  - Removed window.switchLang")
print("  - Removed old translations dictionary")
print("  - Removed dead currentTheme variable")
print("  - Added language param to generatePayload()")
