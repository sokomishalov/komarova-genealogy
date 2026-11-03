import sys,glob
from PIL import Image
fs=sorted(glob.glob(sys.argv[1]));out=sys.argv[2];cols=int(sys.argv[3]) if len(sys.argv)>3 else 4
ims=[Image.open(f) for f in fs];w,h=ims[0].size
rows=(len(ims)+cols-1)//cols
s=Image.new('RGB',(w*cols,h*rows),'white')
for i,im in enumerate(ims): s.paste(im.resize((w,h)),((i%cols)*w,(i//cols)*h))
s.save(out,quality=80)
