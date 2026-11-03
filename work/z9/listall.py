import urllib.request,urllib.parse,json,time,sys
H={'User-Agent':'kinship-research/1.0 (genealogy; personal family history)'}
time.sleep(60)
out=[];cont={}
while True:
  p=dict(action='query',list='allimages',aiprefix=sys.argv[1],ailimit='500',aiprop='size',format='json');p.update(cont)
  for a in range(6):
    try:
      d=json.load(urllib.request.urlopen(urllib.request.Request('https://commons.wikimedia.org/w/api.php?'+urllib.parse.urlencode(p),headers=H)));break
    except Exception as e: print(e,flush=True); time.sleep(60*(a+1))
  for i in d['query']['allimages']: out.append(f"{i['name']} {i['size']}")
  if 'continue' not in d: break
  cont=d['continue'];time.sleep(5)
open(sys.argv[2],'w').write('\n'.join(out));print(len(out))
