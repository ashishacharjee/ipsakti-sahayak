import codecs
import re

with codecs.open('app/static/app.js', 'r', 'utf-8') as f:
    js = f.read()

# Fix the orphaned brace from the langSelect regex cleanup
js = re.sub(
    r'\s*// langSelect listener removed - using i18n\.js\s*const val = langSelect\.value;\s*if.*?}\n',
    '\n        if (typeof getCurrentLanguage === "function" && getCurrentLanguage() === "hi") langCode = "hi-IN";\n',
    js, flags=re.DOTALL
)

with codecs.open('app/static/app.js', 'w', 'utf-8') as f:
    f.write(js)
