#!/bin/bash
cd /private/tmp/claude-501/-Users-sokomishalov-idea-justplay-backend/ff6ca444-5119-49a5-b0e1-aa24be3961f5/scratchpad/z5; v=$1; par=${2:-1}; a=${3:-5}
n=$(ls r$v/p | wc -l); seq $a 1 $n | awk -v p=$par '$1%2==p' > r$v/faces.txt
rm -rf r$v/c; LIST=r$v/faces.txt SW=560 COLS=3 ROWS=16 ../venv/bin/python -I bands.py r$v/p r$v/c "${B:-0.15,0.32,1.0,0.43}" | tr '\n' ' '
