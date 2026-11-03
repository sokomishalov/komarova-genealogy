#!/bin/bash
cd /private/tmp/claude-501/-Users-sokomishalov-idea-justplay-backend/ff6ca444-5119-49a5-b0e1-aa24be3961f5/scratchpad/z5; P=../venv/bin/python; v=$1; shift
LC_ALL=C $P -I classify.py r$v/p "$@" > r$v/cls.txt
awk '$2=="F" && $1>4{print $1}' r$v/cls.txt > r$v/faces.txt
echo "faces $(wc -l < r$v/faces.txt) odd=$(awk '$1%2==1' r$v/faces.txt|wc -l)"
rm -rf r$v/c; LIST=r$v/faces.txt SW=560 COLS=3 ROWS=16 $P -I bands.py r$v/p r$v/c "0.15,0.32,1.0,0.43" | tr '\n' ' '
