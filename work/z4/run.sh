#!/bin/bash
# usage: run.sh <vol-number>...
cd "$(dirname "$0")"
for v in "$@"; do
  t=$(grep "^ДАКО_Р-5634-1-$v[._]" allimages.txt | awk '{print $1}')
  n=$(python3 -c "
import urllib.request,urllib.parse,json,sys,time
H={'User-Agent':'kinship-research/1.0 (genealogy; personal family history)'}
u='https://commons.wikimedia.org/w/api.php?'+urllib.parse.urlencode(dict(action='query',titles='File:'+sys.argv[1],prop='imageinfo',iiprop='size',format='json'))
print(list(json.load(urllib.request.urlopen(urllib.request.Request(u,headers=H)))['query']['pages'].values())[0]['imageinfo'][0]['pagecount'])" "$t")
  echo "VOL $v pages $n"; sleep 4
  python3 fetchpdf2.py "File:$t" v$v ${START:-2} $n 800 || { echo "STOP at $v"; exit 2; }
done
echo ALLDONE
