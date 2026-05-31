with open('leilei_co.html','r',encoding='utf-8') as f:
    lines = f.readlines()
start = end = None
for i, l in enumerate(lines):
    if l.strip().startswith('const articleHTML = `'):
        start = i
    elif start is not None and l.strip() == '`;':
        end = i
        break
print("start_1based", start + 1 if start is not None else None)
print("end_1based", end + 1 if end is not None else None)
print("FIRST", repr(lines[start])[:100])
print("LAST", repr(lines[end])[:100])
print("NUM_LINES_IN_BLOCK", (end - start + 1) if (start is not None and end is not None) else None)
