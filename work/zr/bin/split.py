import sys,os,re
from PIL import Image,ImageOps,ImageDraw
src,out,a,b=sys.argv[1],sys.argv[2],int(sys.argv[3]),int(sys.argv[4])
os.makedirs(out,exist_ok=True)
num=lambda f:int(re.findall(r"\d+",f)[-1])
files=sorted([f for f in os.listdir(src) if f.endswith(".jpg") and a<=num(f)<=b],key=num)
land=[];port=[]
for f in files:
  im=Image.open(os.path.join(src,f)).convert("L"); w,h=im.size
  if w>h:
    c=ImageOps.autocontrast(im.crop((0,int(.07*h),int(.19*w),h)),cutoff=2); c=c.resize((190,int(c.height*190/c.width)))
    d=ImageDraw.Draw(c); d.rectangle((0,0,30,13),fill=0); d.text((2,1),str(num(f)),fill=255); land.append(c)
  else:
    c=ImageOps.autocontrast(im.crop((0,int(.33*h),w,int(.56*h))),cutoff=2); c=c.resize((520,int(c.height*520/c.width)))
    d=ImageDraw.Draw(c); d.rectangle((0,0,30,13),fill=0); d.text((2,1),str(num(f)),fill=255); port.append(c)
def sheet(lst,cols,rows,tag):
  per=cols*rows
  for s in range(0,len(lst),per):
    b=lst[s:s+per]; W=max(x.width for x in b); H=max(x.height for x in b)
    sh=Image.new("L",(cols*(W+6),rows*(H+6)),255)
    for i,c in enumerate(b): sh.paste(c,((i%cols)*(W+6),(i//cols)*(H+6)))
    sh.save(os.path.join(out,f"{tag}-{a:03d}-{b and s:03d}.jpg"),quality=80)
sheet(land,9,2,"L"); sheet(port,3,7,"P")
print(len(land),len(port))
