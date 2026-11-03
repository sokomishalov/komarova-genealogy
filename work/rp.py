import sys,re
b=open(sys.argv[1],'rb').read()
t=b.decode('utf-16le',errors='replace')
t=re.sub(r'[\x00-\x1f�]+',' ',t)
recs=re.split(r'(?=\b[А-ЯЁ]{3,}(?:-[А-ЯЁ]+)? [А-ЯЁ][а-яё]+ [А-ЯЁ][а-яё]+[,.])',t)
out=[r.strip()[:230] for r in recs if re.search(r'Реп[а-я]*\.? ?[- ]?Плат|РеаПлат',r[:200])]
for r in out: print(r)
