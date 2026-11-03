import sys,os,re
from PIL import Image,ImageOps,ImageEnhance,ImageDraw
src,out,x0,y0,x1,y1,cols,rows,sw=sys.argv[1],sys.argv[2],*map(float,sys.argv[3:7]),*map(int,sys.argv[7:10])
os.makedirs(out,exist_ok=True)
files=sorted([f for f in os.listdir(src) if f.endswith(".jpg")],key=lambda f:int(re.findall(r"\d+",f)[-1]))
per=cols*rows
for s in range(0,len(files),per):
  batch=files[s:s+per]; strips=[]
  for f in batch:
    im=Image.open(os.path.join(src,f)).convert("L"); w,h=im.size
    c=im.crop((int(x0*w),int(y0*h),int(x1*w),int(y1*h)))
    c=ImageOps.autocontrast(c,cutoff=1)
    nh=int(c.height*sw/c.width); c=c.resize((sw,nh))
    d=ImageDraw.Draw(c); n=int(re.findall(r"\d+",f)[-1]); d.rectangle((0,0,34,14),fill=255); d.text((2,1),str(n),fill=0)
    strips.append(c)
  sh=max(x.height for x in strips)
  sheet=Image.new("L",(cols*(sw+6),rows*(sh+3)),255)
  for i,c in enumerate(strips):
    col,row=i//rows,i%rows
    sheet.paste(c,(col*(sw+6),row*(sh+3)))
  a=int(re.findall(r"\d+",batch[0])[-1]); b=int(re.findall(r"\d+",batch[-1])[-1])
  sheet.save(os.path.join(out,f"g-{a:04d}-{b:04d}.jpg"),quality=80)
print("ok")
