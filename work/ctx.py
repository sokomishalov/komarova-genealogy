import sys,re
b=open(sys.argv[1],'rb').read()
t=b.decode('utf-16le',errors='replace')
for key in sys.argv[2:]:
    for m in re.finditer(key,t):
        s=t[m.start():m.start()+260]
        s=re.sub(r'[\x00-\x1f�]+','|',s)
        print(s); print('--')
