#!/bin/bash
# wait until all queued pages of given volume codes are fetched/skipped, or fetcher stopped
S=/private/tmp/claude-501/-Users-sokomishalov-idea-justplay-backend/ff6ca444-5119-49a5-b0e1-aa24be3961f5/scratchpad
while true; do
  grep -q STOPPED $S/t2/fetch.log && { echo "FETCHER STOPPED"; tail -3 $S/t2/fetch.log; exit 0; }
  left=0
  for c in "$@"; do
    while read -r cc p; do
      [ "$cc" = "$c" ] || continue
      f=$(printf "%s/t2/%s/p%03d.jpg" $S $c $p)
      [ -s "$f" ] || grep -q "^SKIP $c $p\$" $S/t2/fetch.log || left=$((left+1))
    done < $S/t2/queue.txt
  done
  [ $left -eq 0 ] && { echo "DONE $*"; exit 0; }
  sleep 30
done
