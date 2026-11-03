import sys,os,subprocess
from PIL import Image,ImageOps,ImageDraw
# usage: mcrop.py SCR out.jpg code:page code:page ...
scr,out=sys.argv[1],sys.argv[2]; items=sys.argv[3:]
tmp=os.path.join(scr,"dl","mc_tmp"); os.makedirs(tmp,exist_ok=True)
crops=[]
for it in items:
  code,p=it.split(":"); p=int(p)
  pref=os.path.join(tmp,f"{code}-{p}")
  f=[x for x in os.listdir(tmp) if x.startswith(f"{code}-{p}-")]
  if not f:
    subprocess.run(["pdftoppm","-f",str(p),"-l",str(p),"-r","80","-gray","-jpeg",os.path.join(scr,"dl",code+".pdf"),pref],check=True)
    f=[x for x in os.listdir(tmp) if x.startswith(f"{code}-{p}-")]
  im=Image.open(os.path.join(tmp,f[0])).convert("L"); w,h=im.size
  c=ImageOps.autocontrast(im.crop((int(.08*w),int(.33*h),int(.95*w),int(.40*h))),cutoff=2)
  m=ImageOps.autocontrast(im.crop((int(.08*w),int(.60*h),int(.95*w),int(.80*h))),cutoff=2)
  W=760
  c=c.resize((W,int(c.height*W/c.width))); m=m.resize((W,int(m.height*W/m.width)))
  s=Image.new("L",(W,c.height+m.height+2),255); s.paste(c,(0,0)); s.paste(m,(0,c.height+2))
  d=ImageDraw.Draw(s); d.rectangle((0,0,70,14),fill=255); d.text((2,1),it,fill=0)
  crops.append(s)
cols=2; rows=(len(crops)+1)//2; H=max(x.height for x in crops)
sheet=Image.new("L",(cols*(760+8),rows*(H+6)),255)
for i,c in enumerate(crops): sheet.paste(c,((i%cols)*768,(i//cols)*(H+6)))
sheet.save(out,quality=82)
