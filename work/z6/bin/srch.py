import urllib.request,urllib.parse,json,sys,time
H={'User-Agent':'kinship-research/1.0 (genealogy; personal family history)'}
q=sys.argv[1]; off=0
while True:
    u='https://commons.wikimedia.org/w/api.php?'+urllib.parse.urlencode(dict(action='query',list='search',srsearch=q,srnamespace=6,srlimit=100,sroffset=off,format='json'))
    d=json.load(urllib.request.urlopen(urllib.request.Request(u,headers=H)))
    if 'query' not in d: print('ERR',d,file=sys.stderr); break
    for r in d['query']['search']: print(r['title'])
    if 'continue' in d: off=d['continue']['sroffset']; time.sleep(5)
    else: break
