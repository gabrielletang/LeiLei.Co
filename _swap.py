with open('leilei_co.html','r',encoding='utf-8') as f:
    lines=f.readlines()
start=end=None
for i,l in enumerate(lines):
    if l.strip().startswith('const articleHTML = `'):
        start=i
    elif start is not None and l.strip()=='`;':
        end=i; break
with open('_newart.html','r',encoding='utf-8') as f:
    block=f.read().replace('__BACKTICK__','`')
if not block.endswith('\n'): block+='\n'
new=lines[:start]+[block]+lines[end+1:]
with open('leilei_co.html','w',encoding='utf-8') as f:
    f.writelines(new)
c=''.join(new)
print("replaced",start+1,"-",end+1)
print("title_ok:", "P-hacking and the garden of forking paths</h1>" in c)
print("img_ok:", "multiplecomparisonsrisk.png" in c)
print("sources_ok:", "Gelman, A. and Loken" in c)
print("markers:", c.count("const articleHTML = `"))
