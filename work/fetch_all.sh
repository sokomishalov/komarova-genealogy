#!/bin/bash
cd "$(dirname "$0")"
order="3693 3694 3695 3696 3697 3698 3699 3700 3702 3407 4140 4141 4507 4884 4122 4123 4124 4125 4126 4127 4128 4129 4493 4494 4495 4496 4497 4871 4872 4873 4874 3398 3399 3400 3401 3703 4136 4503 4881"
for c in $order; do
  u=$(grep "^$c	" urls.tsv | cut -f2)
  [ -s dl/$c.pdf ] || curl -s -m 1500 --retry 3 --retry-delay 20 -A "genealogy-research/1.0 (personal family history research)" -o dl/$c.pdf "$u"
  sz=$(stat -f %z dl/$c.pdf 2>/dev/null)
  mkdir -p dl/r$c; pdftoppm -r 45 -gray -jpeg dl/$c.pdf dl/r$c/p 2>/dev/null
  echo "$c size=$sz pages=$(ls dl/r$c | wc -l) $(date +%T)"
done
echo ALLDONE
