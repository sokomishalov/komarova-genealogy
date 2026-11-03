import sys,os,re
from PIL import Image,ImageOps,ImageDraw
# sheet.py srcdir out "pages" x0 y0 x1 y1 colw cols
src,out=sys.argv[1],sys.argv[2]; pages=[int(x) for x in sys.argv[3].split(",")]; x0,y0,x1,y1=map(float,sys.argv[4:8]); W=int(sys.argv[8]); cols=int(sys.argv[9])
st=[]
for p in pages:
  f=f"{src}/p{p:03d}.jpg"
  if not os.path.exists(f): continue
  im=Image.open(f).convert("L");w,h=im.size
  c=ImageOps.autocontrast(im.crop((int(x0*w),int(y0*h),int(x1*w),int(y1*h))),cutoff=1)
  c=c.resize((W,int(c.height*W/c.width)));d=ImageDraw.Draw(c);d.rectangle((0,0,44,18),fill=255);d.text((3,3),str(p),fill=0);st.append(c)
H=max(c.height for c in st); sh=Image.new("L",(cols*(W+6),H*((len(st)+cols-1)//cols)),255)
for i,c in enumerate(st): sh.paste(c,((i%cols)*(W+6),(i//cols)*H))
sh.save(out,quality=85); print(out,sh.size)
