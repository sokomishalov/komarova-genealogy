import urllib.request,urllib.parse,json,sys,time
H={'User-Agent':'kinship-research/1.0 (genealogy; personal family history)'}
for p in sys.argv[1:]:
    c=None
    while True:
        a=dict(action='query',list='allimages',aiprefix=p,ailimit=500,aiprop='size',format='json')
        if c: a['aicontinue']=c
        u='https://commons.wikimedia.org/w/api.php?'+urllib.parse.urlencode(a)
        for t in range(4):
            try: d=json.load(urllib.request.urlopen(urllib.request.Request(u,headers=H))); break
            except Exception as e: print('ERR',e,file=sys.stderr); time.sleep(30*(t+1))
        for r in d['query']['allimages']: print(r['name'], r.get('size'), flush=True)
        c=d.get('continue',{}).get('aicontinue')
        time.sleep(6)
        if not c: break
