import sys,glob,os,re
from PIL import Image,ImageOps,ImageDraw
src,out=sys.argv[1],sys.argv[2]
bands=[tuple(map(float,b.split(','))) for b in sys.argv[3].split(';')]
sw=int(os.environ.get("SW","520"));cols=int(os.environ.get("COLS","3"));rows=int(os.environ.get("ROWS","12"))
os.makedirs(out,exist_ok=True)
num=lambda f:int(re.findall(r"\d+",os.path.basename(f))[-1])
fs=sorted(glob.glob(src+"/*.jpg"),key=num);L=os.environ.get("LIST")
if L: keep=set(map(int,open(L).read().split()));fs=[f for f in fs if num(f) in keep]
per=cols*rows
for s in range(0,len(fs),per):
  b=fs[s:s+per];st=[]
  for f in b:
    im=Image.open(f).convert("L");w,h=im.size
    parts=[(ImageOps.equalize if os.environ.get("EQ") else (lambda z:ImageOps.autocontrast(z,cutoff=1)))(im.crop((int(a*w),int(c*h),int(x*w),int(y*h)))) for a,c,x,y in bands]
    tw=max(p.width for p in parts);th=sum(p.height for p in parts)+2*len(parts)
    c=Image.new("L",(tw,th),0);yy=0
    for p in parts: c.paste(p,(0,yy));yy+=p.height+2
    c=c.resize((sw,int(th*sw/tw)));d=ImageDraw.Draw(c);d.rectangle((0,0,30,13),fill=255);d.text((2,1),str(num(f)),fill=0);st.append(c)
  sh=max(x.height for x in st);sheet=Image.new("L",(cols*(sw+6),rows*(sh+4)),255)
  for i,c in enumerate(st): sheet.paste(c,((i//rows)*(sw+6),(i%rows)*(sh+4)))
  n=f"{out}/b-{num(b[0]):03d}-{num(b[-1]):03d}.jpg";sheet.save(n,quality=85);print(n)
