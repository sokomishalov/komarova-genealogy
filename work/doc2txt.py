import sys,re
b=open(sys.argv[1],'rb').read()
t1=b.decode('utf-16le',errors='ignore')
t2=b.decode('cp1251',errors='ignore')
out=[]
for t in (t1,t2):
    for m in re.finditer(r'[^\x00-\x08\x0b\x0c\x0e-\x1f\ufffd]{40,}',t):
        out.append(m.group(0))
open(sys.argv[2],'w').write('\n'.join(out))
