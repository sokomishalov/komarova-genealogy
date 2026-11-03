import sys,os,re
from PIL import Image,ImageOps,ImageDraw
# usage: sheet.py SRC_DIR OUT_DIR pages(comma list or a-b[:step]) bands  cols rows width
src,out,spec=sys.argv[1],sys.argv[2],sys.argv[3]
bands=[tuple(map(float,b.split(":"))) for b in sys.argv[4].split(",")]  # y0:y1:x0
cols,rows,sw=int(sys.argv[5]),int(sys.argv[6]),int(sys.argv[7])
prefix=sys.argv[8] if len(sys.argv)>8 else "s"
os.makedirs(out,exist_ok=True)
pages=[]
for part in spec.split(","):
    if "-" in part:
        r,_,st=part.partition(":"); a,b=map(int,r.split("-")); pages+=list(range(a,b+1,int(st or 1)))
    else: pages.append(int(part))
def load(p):
    for fn in (f"p{p:03d}.jpg",f"p-{p:03d}.jpg"):
        f=os.path.join(src,fn)
        if os.path.exists(f): return Image.open(f).convert("L")
    return None
items=[]
for p in pages:
    im=load(p)
    if im is None: continue
    w,h=im.size; parts=[]
    for y0,y1,x0 in bands:
        parts.append(im.crop((int(x0*w),int(y0*h),w,int(y1*h))))
    W=max(x.width for x in parts); H=sum(x.height for x in parts)
    c=Image.new("L",(W,H),255); y=0
    for x in parts: c.paste(x,(0,y)); y+=x.height
    c=ImageOps.autocontrast(c,cutoff=2)
    c=c.resize((sw,int(c.height*sw/c.width)))
    cap=float(os.environ.get('CAP','0.75'))
    if c.height>int(sw*cap): c=c.crop((0,0,sw,int(sw*cap)))
    d=ImageDraw.Draw(c); d.rectangle((0,0,26,12),fill=255); d.text((1,0),str(p),fill=0)
    items.append((p,c))
per=cols*rows
for s in range(0,len(items),per):
    b=items[s:s+per]; sh=max(c.height for _,c in b)
    sheet=Image.new("L",(cols*(sw+8),rows*(sh+4)),128)
    for i,(_,c) in enumerate(b): sheet.paste(c,((i//rows)*(sw+8),(i%rows)*(sh+4)))
    sheet.save(os.path.join(out,f"{prefix}-{b[0][0]:03d}-{b[-1][0]:03d}.jpg"),quality=82)
    print(os.path.join(out,f"{prefix}-{b[0][0]:03d}-{b[-1][0]:03d}.jpg"), sheet.size)
