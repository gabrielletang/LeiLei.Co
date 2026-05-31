with open('leilei_co.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

start = end = None
for i, l in enumerate(lines):
    if l.strip().startswith('const articleHTML = `'):
        start = i
    elif start is not None and l.strip() == '`;':
        end = i
        break

with open('_article.html', 'r', encoding='utf-8') as f:
    new_block = f.read()
if not new_block.endswith('\n'):
    new_block += '\n'

new_lines = lines[:start] + [new_block] + lines[end + 1:]
with open('leilei_co.html', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Replaced lines", start + 1, "to", end + 1)
# quick sanity checks
content = ''.join(new_lines)
print("has Simpson title:", "Simpson's Paradox</h1>" in content)
print("ultimate-sweet remaining:", content.count('ultimate-sweet'))
print("backtick template count:", content.count('const articleHTML = `'))
