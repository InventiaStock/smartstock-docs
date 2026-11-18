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

STYLE="""<style>
*{font-size:inherit;}
body{font-family:"Segoe UI",Calibri,Arial,sans-serif;line-height:1.55;font-size:21pt !important;color:#222;}
h1{font-size:30pt !important;color:#111;font-weight:bold;margin:0 0 14px;border:none !important;padding:0 !important;}
h2{font-size:25pt !important;color:#111;font-weight:bold;margin:20px 0 8px;border:none !important;padding:0 !important;}
h3{font-size:23pt !important;color:#111;font-weight:bold;margin:15px 0 6px;border:none !important;}
h4{font-size:21pt !important;color:#111;font-weight:bold;margin:12px 0 5px;border:none !important;}
p{text-align:justify;margin:7px 0;font-size:21pt !important;}
img{max-width:90%;max-height:11cm;height:auto;display:block;margin:10px auto;page-break-inside:avoid;}
table{border-collapse:collapse;margin:12px auto;width:95%;font-size:15pt !important;}
th,td{border:1px solid #777;padding:6px 9px;font-size:15pt !important;vertical-align:top;}
th{background:none !important;color:#111;font-weight:bold;}
blockquote{border:none !important;background:none !important;margin:7px 0;padding:0 !important;color:#222;font-size:16pt !important;}
em{color:#333;font-size:inherit !important;}
ul,ol{margin:6px 0 6px 10px;font-size:16pt !important;}
li{margin:3px 0;font-size:16pt !important;}
hr{display:none;}
tr,td,th{page-break-inside:auto;}
a{word-break:break-all;font-size:inherit !important;}
td,th{text-align:left;}
td p,td li,td ul,td ol{text-align:left;margin:3px 0;font-size:15pt !important;}
table img{max-height:5cm;max-width:100%;height:auto;margin:4px auto;}
img{break-before:avoid;}
h1,h2,h3,h4{break-after:avoid;}
span,div,strong,em,a,code,pre,b,i,u{font-size:inherit !important;}
td span,td div,td strong,td em,td a,td code,td b,td i,td u{font-size:15pt !important;}
</style>
"""

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