#!/bin/bash
cd /private/tmp/claude-501/-Users-sokomishalov-idea-justplay-backend/ff6ca444-5119-49a5-b0e1-aa24be3961f5/scratchpad/z5
rm -rf $2; export LIST=$4; [ -z "$4" ] && unset LIST; SW=${SW:-560} COLS=3 ROWS=${ROWS:-22} ../venv/bin/python -I bands.py $1 $2 "$3" | tr '\n' ' '
