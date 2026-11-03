#!/bin/bash
# usage: dl.sh listfile vol... ; downloads full PDFs from upload.wikimedia.org sequentially into z9/pdf
L=$1; shift
cd "$(dirname "$0")/pdf"
for v in "$@"; do
  n=$(grep "^ДАКО_Р-5634-1-$v[._]" $L | head -1 | awk '{print $1}')
  [ -z "$n" ] && { echo "no $v"; continue; }
  [ -s "$v.pdf" ] && { echo "have $v"; continue; }
  h=$(printf '%s' "$n" | md5 -q)
  u="https://upload.wikimedia.org/wikipedia/commons/${h:0:1}/${h:0:2}/$(python3 -c 'import sys,urllib.parse;print(urllib.parse.quote(sys.argv[1]))' "$n")"
  for a in 1 2 3 4 5; do
    code=$(curl -s -o "$v.part" -w '%{http_code}' -A "kinship-research/1.0 (genealogy; personal family history)" "$u")
    echo "$v http $code $(stat -f%z $v.part 2>/dev/null)"
    if [ "$code" = 200 ]; then mv "$v.part" "$v.pdf"; break; fi
    sleep $((90*a))
  done
  sleep 20
done
echo ALLDONE
