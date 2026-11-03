#!/bin/bash
# sequential polite thumb fetcher: reads queue lines "CODE PAGE", writes t2/CODE/pNNN.jpg
S=/private/tmp/claude-501/-Users-sokomishalov-idea-justplay-backend/ff6ca444-5119-49a5-b0e1-aa24be3961f5/scratchpad
Q=$S/t2/queue.txt; LOG=$S/t2/fetch.log
UA="FamilyHistoryResearch/1.0 (personal non-commercial genealogy of own family; sequential, <=1 req/5s; Wikimedia Commons DAKO R-5634 scans)"
fails=0
while true; do
  grep -q '^STOP' $Q && { echo "STOP marker $(date +%T)" >> $LOG; exit 0; }
  line=""
  while read -r c p; do
    [[ "$c" =~ ^[0-9]+$ ]] || continue
    f=$(printf "%s/t2/%s/p%03d.jpg" $S $c $p)
    [ -s "$f" ] && continue
    grep -q "^SKIP $c $p\$" $LOG 2>/dev/null && continue
    line="$c $p"; break
  done < $Q
  if [ -z "$line" ]; then sleep 20; continue; fi
  set -- $line; c=$1; p=$2
  path=$(grep "^$c	" $S/urls.tsv | cut -f2 | sed 's#https://upload.wikimedia.org/wikipedia/commons/##')
  h=${path%/*}; F=${path##*/}
  url="https://upload.wikimedia.org/wikipedia/commons/thumb/$h/$F/page$p-960px-$F.jpg"
  mkdir -p $S/t2/$c; f=$(printf "%s/t2/%s/p%03d.jpg" $S $c $p)
  r=$(curl -s -m 120 -A "$UA" -o "$f.tmp" -w '%{http_code} %{time_total}' "$url"); code=${r%% *}; tt=${r##* }
  if [ "$code" = "200" ]; then
    mv "$f.tmp" "$f"; fails=0
    sleep $(awk -v t="$tt" 'BEGIN{s=5.6-t; if(s<0.6)s=0.6; print s}')
  elif [ "$code" = "404" ]; then
    rm -f "$f.tmp"; echo "SKIP $c $p" >> $LOG; sleep 6
  else
    rm -f "$f.tmp"; fails=$((fails+1))
    w=$((120 * (2 ** (fails-1)))); [ $w -gt 600 ] && w=600
    echo "# $c p$p http=$code fail#$fails wait ${w}s $(date +%T)" >> $LOG
    if [ $fails -ge 6 ]; then echo "STOPPED blocked at $c p$p $(date +%T)" >> $LOG; exit 1; fi
    sleep $w
  fi
done
