import codecs

with codecs.open('app/static/app.js', 'r', 'utf-8') as f:
    lines = f.readlines()

new_lines = []
skip = False
for i, line in enumerate(lines):
    # If we are between lines 37 and 50 (0-indexed 36 and 49)
    if 36 <= i <= 49:
        if i == 36:
            new_lines.append('        let langCode = "en-US";\n')
            new_lines.append('        if (typeof getCurrentLanguage === "function" && getCurrentLanguage() === "hi") {\n')
            new_lines.append('            langCode = "hi-IN";\n')
            new_lines.append('        }\n')
        continue
    new_lines.append(line)

with codecs.open('app/static/app.js', 'w', 'utf-8') as f:
    f.writelines(new_lines)

print("Fixed!")
