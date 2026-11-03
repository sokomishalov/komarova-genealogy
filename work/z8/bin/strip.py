import sys,glob,os,re
from PIL import Image,ImageOps,ImageDraw
# usage: strip.py srcdir out first last x0 y0 x1 y1 width per
src,out=sys.argv[1],sys.argv[2]; a,b=int(sys.argv[3]),int(sys.argv[4]); x0,y0,x1,y1=map(float,sys.argv[5:9]); W=int(sys.argv[9]); per=int(sys.argv[10])
fs=[f"{src}/p{p:03d}.jpg" for p in range(a,b+1) if os.path.exists(f"{src}/p{p:03d}.jpg")]
os.makedirs(os.path.dirname(out) or ".",exist_ok=True)
for s in range(0,len(fs),per):
  st=[]
  for f in fs[s:s+per]:
    im=Image.open(f).convert("L");w,h=im.size
    c=ImageOps.autocontrast(im.crop((int(x0*w),int(y0*h),int(x1*w),int(y1*h))),cutoff=1)
    c=c.resize((W,int(c.height*W/c.width)));d=ImageDraw.Draw(c);d.rectangle((0,0,44,18),fill=255);d.text((3,3),re.findall(r"\d+",os.path.basename(f))[0],fill=0);st.append(c)
  H=sum(x.height+4 for x in st); sh=Image.new("L",(W,H),255); y=0
  for c in st: sh.paste(c,(0,y)); y+=c.height+4
  n=f"{out}-{s//per:02d}.jpg"; sh.save(n,quality=85); print(n)
