#!/bin/bash
curl -s -m 25 -A 'Mozilla/5.0 (Macintosh)' --data-urlencode "q=$1" "https://html.duckduckgo.com/html/" | python3 -I -c '
import sys,re,html
t=sys.stdin.read()
for m in re.finditer(r"class=\"result__a\" href=\"([^\"]+)\"[^>]*>(.*?)</a>.*?class=\"result__snippet\"[^>]*>(.*?)</a>",t,re.S):
  u,ti,sn=m.groups()
  u=html.unescape(u)
  mm=re.search(r"uddg=([^&]+)",u)
  import urllib.parse
  if mm: u=urllib.parse.unquote(mm.group(1))
  print("*",re.sub("<[^>]+>","",html.unescape(ti)),"|",u); print("  ",re.sub("<[^>]+>","",html.unescape(sn))[:300])
'
echo -----
