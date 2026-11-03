import sys,os
from PIL import Image,ImageOps,ImageDraw
src,out=sys.argv[1],sys.argv[2]; pages=[int(x) for x in sys.argv[3:]]
ims=[]
for p in pages:
  im=ImageOps.autocontrast(Image.open(f"{src}/p{p:03d}.jpg").convert("L"),cutoff=2); im.thumbnail((620,900))
  ImageDraw.Draw(im).text((3,3),str(p),fill=0); ims.append(im)
cols=3; rows=(len(ims)+cols-1)//cols; h=max(i.height for i in ims)
s=Image.new("L",(cols*628,rows*(h+6)),255)
for i,im in enumerate(ims): s.paste(im,((i%cols)*628,(i//cols)*(h+6)))
s.save(out,quality=82)
