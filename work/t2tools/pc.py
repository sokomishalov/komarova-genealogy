import sys,urllib.parse,urllib.request,json
rows=[l.rstrip("\n").split("\t") for l in open(sys.argv[1]) if l.strip()]
want=sys.argv[2].split(",")
rows=[r for r in rows if r[0] in want]
titles="|".join("File:"+r[2] for r in rows)
q=urllib.parse.urlencode({"action":"query","titles":titles,"prop":"imageinfo","iiprop":"size","format":"json"})
req=urllib.request.Request("https://commons.wikimedia.org/w/api.php?"+q,headers={"User-Agent":"FamilyHistoryResearch/1.0 (personal non-commercial genealogy; sequential low-rate requests)"})
d=json.load(urllib.request.urlopen(req))
bytitle={p["title"]:p["imageinfo"][0].get("pagecount") for p in d["query"]["pages"].values() if "imageinfo" in p}
for r in rows:
    t="File:"+r[2]
    print(r[0], bytitle.get(t), sep="\t")
