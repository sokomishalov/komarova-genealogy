import sys
from PIL import Image
S=sys.argv[1]; out=sys.argv[2]; pages=sys.argv[3:]
tiles=[]
for p in pages:
    im=Image.open(f'{S}/t2/4493/p{int(p):03d}.jpg').convert('L')
    w,h=im.size
    t=im.crop((0,0,w,int(h*0.22)))
    tiles.append((p,t))
W=max(t.size[0] for _,t in tiles); H=sum(t.size[1]+4 for _,t in tiles)
m=Image.new('L',(W,H),255); y=0
from PIL import ImageDraw
d=ImageDraw.Draw(m)
for p,t in tiles:
    m.paste(t,(0,y)); d.text((5,y+2),str(p),fill=0); y+=t.size[1]+4
m.save(out)
