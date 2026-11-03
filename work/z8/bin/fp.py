import urllib.request,urllib.parse,json,sys,time,os
title,outdir,first,last,width=sys.argv[1],sys.argv[2],int(sys.argv[3]),int(sys.argv[4]),int(sys.argv[5])
H={"User-Agent":"kinship-research/1.0 (genealogy; personal family history)"}
os.makedirs(outdir,exist_ok=True)
def get(u):
  for a in range(4):
    try: return urllib.request.urlopen(urllib.request.Request(u,headers=H),timeout=90).read()
    except Exception as e:
      c=getattr(e,'code',None); print("ERR",c,u[:120],flush=True)
      if c==404: return None
      time.sleep(30*(a+1) if c==429 else 10)
  return None
for p in range(first,last+1):
  f=f"{outdir}/p{p:03d}.jpg"
  if os.path.exists(f) and os.path.getsize(f)>10000: continue
  q="https://commons.wikimedia.org/w/api.php?"+urllib.parse.urlencode(dict(action="query",titles=title,prop="imageinfo",iiprop="url",iiurlwidth=width,iiurlparam=f"page{p}-{width}px",format="json"))
  d=json.loads(get(q)); ii=list(d['query']['pages'].values())[0]['imageinfo'][0]
  tu=ii.get('thumburl'); 
  if not tu: print(p,"no thumb");continue
  b=get(tu)
  if b: open(f,"wb").write(b); print(p,len(b),tu[-60:],flush=True)
  time.sleep(4)
print("DONE",flush=True)
