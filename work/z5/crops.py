import sys,glob,os,re
from PIL import Image,ImageOps,ImageDraw
src,out,x0,y0,x1,y1=sys.argv[1],sys.argv[2],*map(float,sys.argv[3:7])
sw=int(sys.argv[7]) if len(sys.argv)>7 else 520; cols=int(sys.argv[8]) if len(sys.argv)>8 else 3; rows=int(sys.argv[9]) if len(sys.argv)>9 else 8
os.makedirs(out,exist_ok=True)
num=lambda f:int(re.findall(r"\d+",os.path.basename(f))[-1])
fs=sorted(glob.glob(src+"/*.jpg"),key=num); P=os.environ.get("PAR"); fs=[f for f in fs if P is None or num(f)%2==int(P)]; R=os.environ.get("RNG"); fs=[f for f in fs if R is None or int(R.split("-")[0])<=num(f)<=int(R.split("-")[1])]
L=os.environ.get("LIST"); fs=[f for f in fs if L is None or num(f) in set(map(int,open(L).read().split()))]
per=cols*rows
for s in range(0,len(fs),per):
  b=fs[s:s+per];st=[]
  for f in b:
    im=Image.open(f).convert("L");w,h=im.size
    c=ImageOps.autocontrast(im.crop((int(x0*w),int(y0*h),int(x1*w),int(y1*h))),cutoff=1)
    c=c.resize((sw,int(c.height*sw/c.width))); c=c.crop((0,0,sw,min(c.height,int(sw*float(os.environ.get("MAXR","0.45"))))))
    d=ImageDraw.Draw(c);d.rectangle((0,0,40,16),fill=255);d.text((3,2),str(num(f)),fill=0)
    st.append(c)
  sh=max(x.height for x in st)
  sheet=Image.new("L",(cols*(sw+6),rows*(sh+4)),255)
  for i,c in enumerate(st): sheet.paste(c,((i//rows)*(sw+6),(i%rows)*(sh+4)))
  n=f"{out}/s-{num(b[0]):03d}-{num(b[-1]):03d}.jpg";sheet.save(n,quality=85);print(n)
