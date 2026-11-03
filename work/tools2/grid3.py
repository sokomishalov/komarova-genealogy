import sys,os,re
from PIL import Image,ImageOps,ImageDraw
# grid3.py src out parity cy0 cy1 my0 my1 [first last]
src,out,parity=sys.argv[1:4]; cy0,cy1,my0,my1=map(float,sys.argv[4:8])
a,b=(int(sys.argv[8]),int(sys.argv[9])) if len(sys.argv)>9 else (0,99999)
os.makedirs(out,exist_ok=True)
num=lambda f:int(re.findall(r"\d+",f)[-1])
files=sorted([f for f in os.listdir(src) if f.endswith(".jpg") and a<=num(f)<=b],key=num)
if parity in("odd","even"): files=[f for f in files if num(f)%2==(1 if parity=="odd" else 0)]
H=int(os.environ.get("GH","48")); rows=int(os.environ.get("GR","38")); cols=2; per=rows*cols
def strip(f):
  im=Image.open(os.path.join(src,f)).convert("L"); w,h=im.size
  c=ImageOps.autocontrast(im.crop((int(.10*w),int(cy0*h),int(.93*w),int(cy1*h))),cutoff=2)
  m=ImageOps.autocontrast(im.crop((int(.55*w),int(my0*h),int(.95*w),int(my1*h))),cutoff=2)
  c=c.resize((int(c.width*H/c.height),H)); m=m.resize((int(m.width*H*1.3/m.height),int(H*1.3)))
  s=Image.new("L",(c.width+m.width+6,int(H*1.3)),255); s.paste(c,(0,0)); s.paste(m,(c.width+6,0))
  d=ImageDraw.Draw(s); d.rectangle((0,0,26,12),fill=255); d.text((1,0),str(num(f)),fill=0)
  return s
for st in range(0,len(files),per):
  batch=files[st:st+per]; ss=[strip(f) for f in batch]
  W=max(x.width for x in ss); hh=max(x.height for x in ss)
  sh=Image.new("L",(cols*(W+8),rows*(hh+3)),255)
  for i,x in enumerate(ss): sh.paste(x,((i//rows)*(W+8),(i%rows)*(hh+3)))
  sh.save(os.path.join(out,f"h-{num(batch[0]):04d}-{num(batch[-1]):04d}.jpg"),quality=80)
