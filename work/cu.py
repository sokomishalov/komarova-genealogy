import hashlib,urllib.parse,sys
for n in sys.argv[1:]:
  n=n.replace(" ","_"); h=hashlib.md5(n.encode()).hexdigest()
  print(f"https://upload.wikimedia.org/wikipedia/commons/{h[0]}/{h[:2]}/{urllib.parse.quote(n)}")
