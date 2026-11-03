import urllib.request,urllib.parse,json,time,sys
H={'User-Agent':'kinship-research/1.0 (genealogy; personal family history)'}
def q(p):
  for a in range(6):
    try: return json.load(urllib.request.urlopen(urllib.request.Request('https://commons.wikimedia.org/w/api.php?'+urllib.parse.urlencode(p),headers=H)))
    except Exception as e: print(e,flush=True); time.sleep(60*(a+1))
for s in ['Фастів 1949','Фастів 1950','Фастівський 1949','Фастівський 1950','Фастівський 1951','Фастів шлюб 1949','Фастів народження 1950']:
  d=q(dict(action='query',list='search',srsearch=s,srnamespace=6,srlimit=50,format='json'))
  print('##',s,d['query']['searchinfo']['totalhits'])
  for i in d['query']['search']:
    if any(y in i['title'] for y in ['1949','195']): print(i['title'])
  time.sleep(8)
