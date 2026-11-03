import re,urllib.request,urllib.parse,json,sys,time,os
title,outdir,first,last,width=sys.argv[1],sys.argv[2],int(sys.argv[3]),int(sys.argv[4]),int(sys.argv[5])
H={"User-Agent":"kinship-research/1.0 (genealogy; personal family history)"}
os.makedirs(outdir,exist_ok=True)
def api(p):
  u="https://commons.wikimedia.org/w/api.php?"+urllib.parse.urlencode(dict(action="query",titles=title,prop="imageinfo",iiprop="url",iiurlwidth=width,iiurlparam=f"page{p}-{width}px",format="json"))
  d=json.load(urllib.request.urlopen(urllib.request.Request(u,headers=H)))
  return list(d['query']['pages'].values())[0]['imageinfo'][0]['thumburl']
tu=api(first)
for p in range(first,last+1,int(os.environ.get("STEP","1"))):
  f=f"{outdir}/p{p:03d}.jpg"
  if os.path.exists(f) and os.path.getsize(f)>10000: continue
  u=re.sub(r"page\d+-(\d+)px",lambda m:f"page{p}-{m.group(1)}px",tu,count=1)
  for attempt in range(3):
    try:
      b=urllib.request.urlopen(urllib.request.Request(u,headers=H),timeout=60).read(); open(f,"wb").write(b); print(p,len(b),flush=True); break
    except Exception as e:
      code=getattr(e,'code',None); print(p,"ERR",code,e,flush=True)
      if code in (429,403,405): print("RATE-LIMITED, stopping",flush=True); sys.exit(2)
      time.sleep(30)
  time.sleep(float(os.environ.get("DELAY","5")))
print("DONE",flush=True)
