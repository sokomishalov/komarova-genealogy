import sys
from PIL import Image, ImageStat
def first_line(path):
    im=Image.open(path).convert("L").resize((480,360))
    mean=ImageStat.Stat(im).mean[0]; thr=mean-40
    px=im.load(); ys=[]
    for y in range(360):
        c=sum(1 for x in range(48,432) if px[x,y]<thr)
        if c/384>0.55: ys.append(y)
    return (round(ys[0]/360,2) if ys else None), len(ys)
if __name__=="__main__":
    for p in sys.argv[1:]:
        print(p.split('/')[-1], first_line(p))
