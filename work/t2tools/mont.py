import sys,os
from PIL import Image,ImageDraw
src,out=sys.argv[1],sys.argv[2]; pages=list(map(int,sys.argv[3].split(","))); w=int(sys.argv[4]) if len(sys.argv)>4 else 320
ims=[]
for p in pages:
    f=os.path.join(src,f"p{p:03d}.jpg")
    if not os.path.exists(f): continue
    im=Image.open(f).convert("L"); im=im.resize((w,int(im.height*w/im.width)))
    d=ImageDraw.Draw(im); d.rectangle((0,0,30,14),fill=255); d.text((2,1),str(p),fill=0); ims.append(im)
cols=4; rows=(len(ims)+cols-1)//cols; h=max(i.height for i in ims)
sh=Image.new("L",(cols*(w+4),rows*(h+4)),128)
for k,i in enumerate(ims): sh.paste(i,((k%cols)*(w+4),(k//cols)*(h+4)))
sh.save(out,quality=80); print(out,sh.size)
