#!/bin/bash
# volready.sh CODE : wait until all queued pages of CODE fetched/skipped (max 590s); print status
S=/private/tmp/claude-501/-Users-sokomishalov-idea-justplay-backend/ff6ca444-5119-49a5-b0e1-aa24be3961f5/scratchpad
end=$(( $(date +%s) + 590 ))
while true; do
  grep -q STOPPED $S/t2/fetch.log && { echo STOPPED; exit 2; }
  last=$(grep "^$1 " $S/t2/queue.txt | tail -1 | awk '{print $2}')
  f=$(printf "%s/t2/%s/p%03d.jpg" $S $1 $last)
  { [ -s "$f" ] || grep -q "^SKIP $1 $last\$" $S/t2/fetch.log; } && { echo "READY $1 $(ls $S/t2/$1 | wc -l)"; exit 0; }
  [ $(date +%s) -gt $end ] && { echo "WAIT $1 $(ls $S/t2/$1 | wc -l) last=$last"; exit 1; }
  sleep 10
done
