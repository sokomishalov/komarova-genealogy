#!/bin/bash
cd /private/tmp/claude-501/-Users-sokomishalov-idea-justplay-backend/ff6ca444-5119-49a5-b0e1-aa24be3961f5/scratchpad/z6
while pgrep -f "t3265 354" >/dev/null; do sleep 10; done
for v in 2334 2680 2688; do T="File:$(grep -h "^ДАКО_Р-5634-1-$v[._]" ai.txt ai2.txt | head -1 | awk '{print $1}')"; DELAY=5 python3 -I ../z4/fetchpdf2.py "$T" t$v 2 5 1000 | tail -1; sleep 6; done
echo ALLDONE
