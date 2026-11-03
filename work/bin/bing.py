import sys,urllib.request,urllib.parse,re,html
q=sys.argv[1]
u='https://www.bing.com/search?setlang=ru&cc=RU&q='+urllib.parse.quote(q)
h=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/124 Safari/537.36','Accept-Language':'ru,en'}),timeout=30).read().decode('utf-8','replace')
items=re.findall(r'<li class="b_algo".*?</li>',h,re.S)
print('##',q,len(items))
for it in items[:10]:
    a=re.search(r'<h2.*?href="([^"]+)".*?>(.*?)</a>',it,re.S)
    p=re.search(r'<p[^>]*>(.*?)</p>',it,re.S)
    cl=lambda s: html.unescape(re.sub(r'<[^>]+>','',s or ''))
    print('-',cl(a.group(2)) if a else '', a.group(1) if a else '')
    print('   ',cl(p.group(1))[:250] if p else '')
