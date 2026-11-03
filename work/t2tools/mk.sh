#!/bin/bash
# mk.sh CODE FROM TO STEP BANDS PREFIX [cols rows width]
S=/private/tmp/claude-501/-Users-sokomishalov-idea-justplay-backend/ff6ca444-5119-49a5-b0e1-aa24be3961f5/scratchpad
$S/venv/bin/python -I $S/t2tools/sheet.py $S/t2/$1 $S/t2/sh$1 $2-$3:$4 $5 ${7:-3} ${8:-8} ${9:-420} ${6:-s}
