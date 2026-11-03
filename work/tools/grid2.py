import sys,os,re
from PIL import Image,ImageOps,ImageDraw
src,out,parity=sys.argv[1],sys.argv[2],sys.argv[3]
x0,y0,x1,y1=map(float,sys.argv[4:8]); cols,rows,sw=map(int,sys.argv[8:11])
os.makedirs(out,exist_ok=True)
num=lambda f:int(re.findall(r"\d+",f)[-1])
files=sorted([f for f in os.listdir(src) if f.endswith(".jpg")],key=num)
if parity in("odd","even"): files=[f for f in files if num(f)%2==(1 if parity=="odd" else 0)]
per=cols*rows
for s in range(0,len(files),per):
  batch=files[s:s+per]; strips=[]
  for f in batch:
    im=Image.open(os.path.join(src,f)).convert("L"); w,h=im.size
    c=ImageOps.autocontrast(im.crop((int(x0*w),int(y0*h),int(x1*w),int(y1*h))),cutoff=3)
    c=c.resize((sw,int(c.height*sw/c.width)))
    d=ImageDraw.Draw(c); d.rectangle((0,0,30,13),fill=255); d.text((2,1),str(num(f)),fill=0)
    strips.append(c)
  sh=max(x.height for x in strips)
  sheet=Image.new("L",(cols*(sw+6),rows*(sh+3)),255)
  for i,c in enumerate(strips): sheet.paste(c,((i//rows)*(sw+6),(i%rows)*(sh+3)))
  sheet.save(os.path.join(out,f"g-{num(batch[0]):04d}-{num(batch[-1]):04d}.jpg"),quality=80)
