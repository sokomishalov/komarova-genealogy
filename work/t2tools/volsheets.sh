#!/bin/bash
# wait for volume, then build sheets: volsheets.sh CODE FIRSTPAGE [bands]
S=/private/tmp/claude-501/-Users-sokomishalov-idea-justplay-backend/ff6ca444-5119-49a5-b0e1-aa24be3961f5/scratchpad
c=$1; first=$2; bands=${3:-0.31:0.42:0.22,0.63:0.79:0.28}
$S/t2tools/waitvol.sh $c
n=$(grep "^$c	" $S/pagecounts.tsv | cut -f2)
rm -rf $S/t2/sh$c
$S/venv/bin/python -I $S/t2tools/sheet.py $S/t2/$c $S/t2/sh$c $first-$n:2 $bands 2 8 520 s | wc -l
