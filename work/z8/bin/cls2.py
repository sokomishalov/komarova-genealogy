import sys,glob,os
from PIL import Image,ImageStat,ImageFilter
for f in sorted(glob.glob(sys.argv[1]+"/p*.jpg")):
  im=Image.open(f).convert("L");w,h=im.size
  c=im.crop((int(.12*w),int(.25*h),int(.35*w),int(.75*h))).filter(ImageFilter.FIND_EDGES)
  print(os.path.basename(f)[1:4], round(ImageStat.Stat(c).mean[0],1))
