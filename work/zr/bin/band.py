import sys,os,re
from PIL import Image,ImageOps,ImageDraw
src,out,y0,y1=sys.argv[1],sys.argv[2],float(sys.argv[3]),float(sys.argv[4])
W=int(os.environ.get("BW","640")); cols=int(os.environ.get("BC","3")); rows=int(os.environ.get("BR","7"))
os.makedirs(out,exist_ok=True)
num=lambda f:int(re.findall(r"\d+",f)[-1])
files=sorted([f for f in os.listdir(src) if f.endswith(".jpg")],key=num)
a,b=(int(sys.argv[5]),int(sys.argv[6])) if len(sys.argv)>6 else (0,9999)
files=[f for f in files if a<=num(f)<=b]
per=cols*rows
for s in range(0,len(files),per):
  batch=files[s:s+per]; st=[]
  for f in batch:
    im=Image.open(os.path.join(src,f)).convert("L"); w,h=im.size
    c=ImageOps.autocontrast(im.crop((0,int(y0*h),w,int(y1*h))),cutoff=2); c=c.resize((W,int(c.height*W/c.width)))
    d=ImageDraw.Draw(c); d.rectangle((0,0,34,14),fill=0); d.text((3,1),str(num(f)),fill=255); st.append(c)
  sh=max(x.height for x in st)
  sheet=Image.new("L",(cols*(W+8),rows*(sh+4)),255)
  for i,c in enumerate(st): sheet.paste(c,((i//rows)*(W+8),(i%rows)*(sh+4)))
  sheet.save(os.path.join(out,f"b-{num(batch[0]):03d}-{num(batch[-1]):03d}.jpg"),quality=78)
