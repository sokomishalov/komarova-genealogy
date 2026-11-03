import sys,glob,os
from PIL import Image,ImageStat
for f in sorted(glob.glob(sys.argv[1]+"/p*.jpg")):
  im=Image.open(f).convert("L");w,h=im.size
  l=ImageStat.Stat(im.crop((int(.1*w),int(.3*h),int(.4*w),int(.7*h)))).mean[0]
  r=ImageStat.Stat(im.crop((int(.6*w),int(.3*h),int(.9*w),int(.7*h)))).mean[0]
  print(os.path.basename(f)[1:4], "S" if l<215 else "C", int(l), int(r))
