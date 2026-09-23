import codecs
import re

with codecs.open('app/static/app.js', 'r', 'utf-8') as f:
    js = f.read()

# 1. Add language to generatePayload
js = js.replace(
    'query: q, \n            jurisdiction: "dual"',
    'query: q, \n            jurisdiction: "dual",\n            language: (typeof getCurrentLanguage === "function") ? getCurrentLanguage() : "en"'
)
js = js.replace(
    "query: q, \n            jurisdiction: 'dual'",
    "query: q, \n            jurisdiction: 'dual',\n            language: (typeof getCurrentLanguage === 'function') ? getCurrentLanguage() : 'en'"
)

# 2. Fix the switchLang reference to point to our i18n
js = js.replace(
    'function translateUI(lang) {',
    'function translateUI(lang) {\n    if (typeof switchLanguage === "function") { switchLanguage(lang); return; }\n'
)

# 3. Clean up the language logic inside startDictation
# This is around line 38
dictation_old = """        if (langSelect) {
            const val = langSelect.value;
            if (val === 'hi') langCode = 'hi-IN';
            else if (val === 'sa') langCode = 'hi-IN'; // Sanskrit usually falls back to Hindi acoustics
            else if (val === 'bn') langCode = 'bn-IN';
            else if (val === 'mr') langCode = 'mr-IN';
            else if (val === 'te') langCode = 'te-IN';
            else if (val === 'ta') langCode = 'ta-IN';
            else if (val === 'gu') langCode = 'gu-IN';
            else if (val === 'kn') langCode = 'kn-IN';
            else if (val === 'ml') langCode = 'ml-IN';
        }"""
dictation_new = """        if (typeof getCurrentLanguage === 'function' && getCurrentLanguage() === 'hi') {
            langCode = 'hi-IN';
        }"""
js = js.replace(dictation_old, dictation_new)

# 4. Remove dark theme enforcement
js = js.replace(
    "if (localStorage.getItem('theme') === 'dark') {\n        document.documentElement.classList.add('dark-theme');\n    }",
    "// Dark theme removed"
)

with codecs.open('app/static/app.js', 'w', 'utf-8') as f:
    f.write(js)
print("[OK] app.js patched safely!")
