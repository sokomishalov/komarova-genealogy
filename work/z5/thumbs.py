import sys,glob,os,re
from PIL import Image,ImageDraw
src,out=sys.argv[1],sys.argv[2];tw=int(sys.argv[3]) if len(sys.argv)>3 else 330;cols=int(sys.argv[4]) if len(sys.argv)>4 else 5;rows=int(sys.argv[5]) if len(sys.argv)>5 else 8
os.makedirs(out,exist_ok=True)
num=lambda f:int(re.findall(r"\d+",os.path.basename(f))[-1])
fs=sorted(glob.glob(src+"/*.jpg"),key=num);R=os.environ.get("RNG")
if R: a,b=map(int,R.split("-"));fs=[f for f in fs if a<=num(f)<=b]
per=cols*rows
for s in range(0,len(fs),per):
  b=fs[s:s+per];ims=[]
  for f in b:
    im=Image.open(f).convert("L");im=im.resize((tw,int(im.height*tw/im.width)));d=ImageDraw.Draw(im);d.rectangle((0,0,30,14),fill=255);d.text((2,1),str(num(f)),fill=0);ims.append(im)
  th=max(i.height for i in ims);sh=Image.new("L",(cols*(tw+4),((len(ims)+cols-1)//cols)*(th+4)),255)
  for i,im in enumerate(ims): sh.paste(im,((i%cols)*(tw+4),(i//cols)*(th+4)))
  n=f"{out}/t-{num(b[0]):03d}-{num(b[-1]):03d}.jpg";sh.save(n,quality=80);print(n)
