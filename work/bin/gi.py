import re,sys,html,urllib.request,urllib.parse,time,os
out=sys.argv[1]; term=sys.argv[2]; match=sys.argv[3] if len(sys.argv)>3 else 'ocr'; scope=sys.argv[4] if len(sys.argv)>4 else 'any'; coll=sys.argv[5] if len(sys.argv)>5 else 'any'
data=urllib.parse.urlencode(dict(term=term,scope=scope,match=match,sort='dist',collection=coll,date='any',transliteration=os.environ.get('TR','none'))).encode()
req=urllib.request.Request('https://genealogyindexer.org/',data=data,headers={'User-Agent':'Mozilla/5.0 (genealogy research)'})
h=urllib.request.urlopen(req,timeout=60).read().decode('utf-8','replace')
fn=os.path.join(out,re.sub(r'\W','_',term)+'_'+match+'_'+scope+'.html'); open(fn,'w').write(h)
m=re.search(r'Matches Found:\s*(~?[\d,]+)',h); print('###',term,match,scope,coll,'matches:',m.group(1) if m else re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',h))[-400:])
parts=re.split(r'(?=<a href="(?:https?:)?//[^"]*" target="_blank">[^<]*</a>)',h)
for p in parts[1:]:
    l=re.match(r'<a href="([^"]*)" target="_blank">([^<]*)</a>',p)
    if not l or 'About this source' not in p: continue
    body=p[:p.find('About this source')]
    t=html.unescape(re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',body)))
    src=html.unescape(re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',p[p.find('About this source'):p.find('About this source')+1500])))
    title=re.search(r'Original Title:(.*?)(Images From|Genealogy Indexer ID)',src); gid=re.search(r'Indexer ID:\s*(\S+)',src)
    print('--',l.group(2),'|',l.group(1),'| ID',gid.group(1) if gid else '?','|',(title.group(1).strip() if title else '')[:150])
    key=os.environ.get('KEY',term[:4]).lower(); i=t.lower().find(key)
    print('   ',t[max(0,i-300):i+300] if i>=0 else t[:500])
