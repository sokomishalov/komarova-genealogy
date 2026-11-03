#!/bin/bash
# gz.sh vol page... -> parent-band zoom sheet
cd /private/tmp/claude-501/-Users-sokomishalov-idea-justplay-backend/ff6ca444-5119-49a5-b0e1-aa24be3961f5/scratchpad/z5; v=$1; shift
printf "%s\n" "$@" > r$v/gl.txt; rm -rf r$v/g; LIST=r$v/gl.txt SW=800 COLS=2 ROWS=3 ../venv/bin/python -I bands.py r$v/p r$v/g "${B:-0.15,0.32,1.0,0.43;0.15,0.62,1.0,0.80}"
