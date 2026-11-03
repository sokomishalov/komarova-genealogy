import sys,glob,os,re
from PIL import Image,ImageOps,ImageDraw
src,out=sys.argv[1],sys.argv[2]; pages=[int(x) for x in sys.argv[3].split(',')]
y0,y1=float(os.environ.get('Y0','0')),float(os.environ.get('Y1','0.78')); W=int(os.environ.get('W','950')); C=int(os.environ.get('C','2'))
os.makedirs(out,exist_ok=True)
fs={int(re.findall(r'\d+',os.path.basename(f))[-1]):f for f in glob.glob(src+'/*.jpg')}
ims=[]
for p in pages:
  im=Image.open(fs[p]).convert('L');w,h=im.size;c=ImageOps.autocontrast(im.crop((0,int(y0*h),w,int(y1*h))),cutoff=1);c=c.resize((W,int(c.height*W/c.width)));d=ImageDraw.Draw(c);d.rectangle((0,0,40,16),fill=255);d.text((3,2),str(p),fill=0);ims.append(c)
H=max(i.height for i in ims);R=(len(ims)+C-1)//C
s=Image.new('L',(C*(W+6),R*(H+6)),255)
for k,i in enumerate(ims): s.paste(i,((k%C)*(W+6),(k//C)*(H+6)))
n=f'{out}/g-{pages[0]}-{pages[-1]}.jpg'; s.save(n,quality=85); print(n)
