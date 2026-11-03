import re,sys,html,urllib.request,time
UA={'User-Agent':'Mozilla/5.0'}
def get(u):
    r=urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=60).read()
    for enc in ('utf-8','cp1251'):
        try: return r.decode(enc)
        except: pass
    return r.decode('utf-8','replace')
base='https://www.pobediteli.ru'
for reg in sys.argv[1:]:
    try: idx=get(f'{base}{reg}/s/index.html')
    except Exception as e: print(reg,'ERR',e); continue
    links=sorted(set(re.findall(r'href="(%s/s/([a-z\-]+)-([a-z\-]+)/index\.html)"'%re.escape(reg),idx)))
    pages=[l for l,a,b in links if a<= 'snim' <= b] or ([f'{reg}/s/index.html'] if not links else [])
    hits=[]
    for p in pages:
        t=get(base+p) if p!=f'{reg}/s/index.html' else idx
        t2=html.unescape(re.sub('<[^>]+>',' | ',t)); t2=re.sub(r'(\s*\|\s*)+',' | ',t2)
        for m in re.finditer(r'Сним[щш]\w*[^|]*\|[^|]*',t2): hits.append(m.group(0).strip())
        time.sleep(1)
    print(reg, len(links),'ranges; pages',pages, '\n   ', '\n    '.join(hits) or 'нет')
