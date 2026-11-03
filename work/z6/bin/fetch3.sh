#!/bin/bash
cd /private/tmp/claude-501/-Users-sokomishalov-idea-justplay-backend/ff6ca444-5119-49a5-b0e1-aa24be3961f5/scratchpad/z6
g(){ T=$(grep -h "Р-5634-1-$1[._ ]" stav.txt kras.txt | head -1); [ -z "$T" ] && T="File:$(grep -h "^ДАКО_Р-5634-1-$1[._]" ai.txt | head -1 | awk '{print $1}')"; STEP=$4 DELAY=5 python3 -I ../z4/fetchpdf2.py "$T" t$1 $2 $3 1000 | tail -1; sleep 8; }
g 2329 220 238 2
g 2041 342 388 2
echo ALLDONE
