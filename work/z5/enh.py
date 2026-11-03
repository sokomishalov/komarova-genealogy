import sys,glob,os,re
from PIL import Image,ImageOps,ImageDraw
src,out,x0,y0,x1,y1=sys.argv[1],sys.argv[2],*map(float,sys.argv[3:7]);sw=int(sys.argv[7]) if len(sys.argv)>7 else 1000
ims=[]
for f in sorted(glob.glob(src+"/*.jpg")):
  im=Image.open(f).convert("L");w,h=im.size;c=ImageOps.equalize(im.crop((int(x0*w),int(y0*h),int(x1*w),int(y1*h))));c=c.resize((sw,int(c.height*sw/c.width)))
  ImageDraw.Draw(c).text((3,2),os.path.basename(f),fill=0);ims.append(c)
H=sum(i.height+4 for i in ims);s=Image.new("L",(sw,H),255);y=0
for i in ims: s.paste(i,(0,y));y+=i.height+4
s.save(out,quality=85)
