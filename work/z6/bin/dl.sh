#!/bin/bash
Z=/private/tmp/claude-501/-Users-sokomishalov-idea-justplay-backend/ff6ca444-5119-49a5-b0e1-aa24be3961f5/scratchpad/z6
cd $Z/pdf
for v in "$@"; do
  n=$(grep -h "^ДАКО_Р-5634-1-$v[._]" $Z/ai.txt $Z/ai2.txt 2>/dev/null | head -1 | awk '{print $1}')
  [ -z "$n" ] && { echo "noname $v"; continue; }
  [ -s "$v.pdf" ] && { echo "have $v"; continue; }
  h=$(printf '%s' "$n" | md5 -q)
  u="https://upload.wikimedia.org/wikipedia/commons/${h:0:1}/${h:0:2}/$(python3 -I -c 'import sys,urllib.parse;print(urllib.parse.quote(sys.argv[1]))' "$n")"
  for a in 1 2 3 4 5 6 7 8; do
    code=$(curl -s -o "$v.part" -w '%{http_code}' -A "kinship-research/1.0 (genealogy; personal family history)" "$u")
    echo "$v http $code $(stat -f%z $v.part 2>/dev/null) $(date +%T)"
    if [ "$code" = 200 ]; then mv "$v.part" "$v.pdf"; break; fi
    sleep $((300+120*a))
  done
  sleep 240
done
echo ALLDONE
