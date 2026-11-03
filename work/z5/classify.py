import sys,glob,os,re
from PIL import Image,ImageOps
src=sys.argv[1]; refs=sys.argv[2:]  # refs as page numbers: face1,face2,... prefix 'r' for reverse
num=lambda f:int(re.findall(r"\d+",os.path.basename(f))[-1])
fs={num(f):f for f in glob.glob(src+"/*.jpg")}
def vec(f):
  im=ImageOps.autocontrast(Image.open(f).convert("L").resize((48,36)),cutoff=2)
  v=list(im.getdata());m=sum(v)/len(v);v=[x-m for x in v];n=sum(x*x for x in v)**.5 or 1;return [x/n for x in v]
R=[(r[0]=='r',vec(fs[int(r.lstrip('r'))])) for r in refs]
for p in sorted(fs):
  v=vec(fs[p]);sf=max([sum(a*b for a,b in zip(v,rv)) for isr,rv in R if not isr] or [0]);sr=max([sum(a*b for a,b in zip(v,rv)) for isr,rv in R if isr] or [0])
  print(p,'F' if sf>sr else 'R',round(sf,2),round(sr,2))
