#!/bin/bash
cd "$(dirname "$0")"
order="4140 4141 4507 4884 4122 4123 4124 4125 4126 4127 4128 4129 4493 4494 4495 4496 4497 4871 4872 4873 4874 3398 3399 3400 3401 3703 4136 4503 4881"
for c in $order; do
  grep -q "^$c size" fetch.log && continue
  u=$(grep "^$c	" urls.tsv | cut -f2)
  wait=60
  for attempt in 1 2 3 4 5 6; do
    code=$(curl -s -m 1500 -A "genealogy-research/1.0 (personal family history research; low volume)" -o dl/$c.pdf -w '%{http_code}' "$u")
    if [ "$code" = "200" ] && pdfinfo dl/$c.pdf >/dev/null 2>&1; then break; fi
    echo "# $c attempt $attempt http=$code; waiting ${wait}s $(date +%T)" >> fetch.log
    rm -f dl/$c.pdf; sleep $wait; wait=$((wait*2))
  done
  if [ -s dl/$c.pdf ]; then
    mkdir -p dl/r$c; pdftoppm -r 45 -gray -jpeg dl/$c.pdf dl/r$c/p 2>/dev/null
    echo "$c size=$(stat -f %z dl/$c.pdf) pages=$(ls dl/r$c | wc -l) $(date +%T)" >> fetch.log
  else
    echo "$c FAILED $(date +%T)" >> fetch.log
  fi
  sleep 20
done
echo ALLDONE >> fetch.log
