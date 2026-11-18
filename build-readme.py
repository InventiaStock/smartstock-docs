#!/usr/bin/env python3
# Genera README.md: une docs/, indice sin azul/subrayado, saltos solo en secciones mayores.
# Uso (en la raiz del repo):  python build-readme.py
import re, os
DOCS='docs'
seq=['00-cover.md','01-logs.md','02-collaboration-insights.md','04-outcome.md',
     '05-chapter-1.md','06-chapter-2.md','07-chapter-3.md','08-chapter-4.md',
     '09-chapter-5.md','10-conclusions.md','11-bibliography.md','12-annexes.md']
BREAK={'01-logs.md','04-outcome.md','05-chapter-1.md','06-chapter-2.md','07-chapter-3.md',
       '08-chapter-4.md','09-chapter-5.md','10-conclusions.md','11-bibliography.md','12-annexes.md'}
PB='<div style="page-break-before:always"></div>'
ST='color:#111;text-decoration:none'

STYLE=""

def anchor(h, seen):
    a=re.sub(r'[^\w\s-]','',h.strip().lower(),flags=re.U); a=re.sub(r'\s+','-',a)
    if a in seen: seen[a]+=1; a=f'{a}-{seen[a]}'
    else: seen[a]=0
    return a

docs={fn:open(os.path.join(DOCS,fn),encoding='utf-8').read().strip().replace('../assets/','assets/')
      for fn in seq if os.path.exists(os.path.join(DOCS,fn))}
body='\n\n'.join(docs.values())

seen={}; toc=['## Tabla de contenidos\n']
for line in body.split('\n'):
    m=re.match(r'^(#{1,4})\s+(.+)', line)
    if not m: continue
    txt=m.group(2).strip()
    if re.match(r'tabla de contenido', txt, re.I): continue
    toc.append('  '*(len(m.group(1))-1)+f'- <a href="#{anchor(txt,seen)}" style="{ST}">{txt}</a>')
toc_md='\n'.join(toc)

out=STYLE
for fn in seq:
    if fn not in docs: continue
    if out.strip() != STYLE.strip():
        out += ('\n\n'+PB+'\n\n') if fn in BREAK else '\n\n'
    out += docs[fn]
    if fn=='02-collaboration-insights.md':
        out += '\n\n'+PB+'\n\n'+toc_md
open('README.md','w',encoding='utf-8').write(out)
print('README.md:', round(os.path.getsize('README.md')/1024,1),'KB | indice:', len(toc)-1)