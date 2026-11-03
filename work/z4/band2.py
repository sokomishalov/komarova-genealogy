import sys,os,re
from PIL import Image,ImageOps,ImageDraw
src,out,first,last=sys.argv[1],sys.argv[2],int(sys.argv[3]),int(sys.argv[4])
cols,rows,sw=3,10,620
bands=[(0.04,0.25,0.97,0.43),(0.04,0.58,0.97,0.78)]
os.makedirs(out,exist_ok=True)
num=lambda f:int(re.findall(r"\d+",f)[-1])
files=sorted([f for f in os.listdir(src) if f.endswith(".jpg") and first<=num(f)<=last and num(f)%2==0],key=num)
per=cols*rows
for s in range(0,len(files),per):
  batch=files[s:s+per]; strips=[]
  for f in batch:
    im=Image.open(os.path.join(src,f)).convert("L"); w,h=im.size
    parts=[ImageOps.autocontrast(im.crop((int(a*w),int(b*h),int(c*w),int(d*h))),cutoff=2) for a,b,c,d in bands]
    tw=parts[0].width; th=sum(p.height for p in parts)
    c=Image.new("L",(tw,th),255); y=0
    for p in parts: c.paste(p,(0,y)); y+=p.height
    c=c.resize((sw,int(th*sw/tw)))
    d=ImageDraw.Draw(c); d.rectangle((0,0,34,14),fill=255); d.text((2,1),str(num(f)),fill=0)
    strips.append(c)
  sh=max(x.height for x in strips)
  sheet=Image.new("L",(cols*(sw+8),rows*(sh+4)),255)
  for i,c in enumerate(strips): sheet.paste(c,((i//rows)*(sw+8),(i%rows)*(sh+4)))
  sheet.save(os.path.join(out,f"g-{num(batch[0]):04d}-{num(batch[-1]):04d}.jpg"),quality=82)
  print(out, num(batch[0]), num(batch[-1]))
