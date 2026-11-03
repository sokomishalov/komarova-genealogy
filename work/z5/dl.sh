#!/bin/bash
# usage: dl.sh vol... ; downloads full PDFs from upload.wikimedia.org sequentially
Z4=/private/tmp/claude-501/-Users-sokomishalov-idea-justplay-backend/ff6ca444-5119-49a5-b0e1-aa24be3961f5/scratchpad/z4
cd "$(dirname "$0")/pdf"
for v in "$@"; do
  n=$(grep "^ДАКО_Р-5634-1-$v[._]" $Z4/allimages.txt | awk '{print $1}')
  [ -s "$v.pdf" ] && { echo "have $v"; continue; }
  h=$(printf '%s' "$n" | md5 -q)
  u="https://upload.wikimedia.org/wikipedia/commons/${h:0:1}/${h:0:2}/$(python3 -c 'import sys,urllib.parse;print(urllib.parse.quote(sys.argv[1]))' "$n")"
  for a in 1 2 3 4; do
    code=$(curl -s -o "$v.part" -w '%{http_code}' -A "kinship-research/1.0 (genealogy; personal family history)" "$u")
    echo "$v http $code $(stat -f%z $v.part 2>/dev/null)"
    if [ "$code" = 200 ]; then mv "$v.part" "$v.pdf"; break; fi
    sleep $((60*a))
  done
  sleep 10
done
echo ALLDONE
