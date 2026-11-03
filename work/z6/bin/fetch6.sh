#!/bin/bash
cd /private/tmp/claude-501/-Users-sokomishalov-idea-justplay-backend/ff6ca444-5119-49a5-b0e1-aa24be3961f5/scratchpad/z6
g(){ T="File:$(grep -h "^ДАКО_Р-5634-1-$1[._]" ai.txt ai2.txt | head -1 | awk '{print $1}')"; echo "== $1"; STEP=2 DELAY=4 python3 -I ../z4/fetchpdf2.py "$T" t$1 $2 $3 900 | tail -1; sleep 8; }
g 2334 214 400
g 2680 330 468
g 2688 466 592
echo ALLDONE
