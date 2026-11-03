import sys,re
b=open(sys.argv[1],'rb').read()
t=b.decode('utf-16le',errors='replace')
# keep only cyrillic-rich runs
runs=re.findall(r'[Ѐ-ӿA-Za-z0-9 .,;:()\-/№"«»\'\r\n\t]{30,}',t)
open(sys.argv[2],'w').write('\n'.join(runs))
