import codecs
import re

with codecs.open('app/static/app.js', 'r', 'utf-8') as f:
    js = f.read()

# Remove toggleDarkMode
js = re.sub(r'function toggleDarkMode\(\) \{.*?\n\}\n', '', js, flags=re.DOTALL)

# Remove Auto-apply theme on load
js = re.sub(r'// Auto-apply theme on load.*?if \(localStorage\.getItem\(\'theme\'\) === \'dark\'\) \{\s*document\.documentElement\.classList\.add\(\'dark-theme\'\);\s*\}\s*\}\);', '', js, flags=re.DOTALL)

# Just in case, remove any lingering if (localStorage.getItem('theme') === 'dark') { ... }
js = re.sub(r'if \(localStorage\.getItem\(\'theme\'\) === \'dark\'\) \{\s*document\.documentElement\.classList\.add\(\'dark-theme\'\);\s*\}', '', js, flags=re.DOTALL)

with codecs.open('app/static/app.js', 'w', 'utf-8') as f:
    f.write(js)
print("Cleaned up dark-theme logic!")
