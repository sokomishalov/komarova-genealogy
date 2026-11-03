#!/bin/bash
Z=/private/tmp/claude-501/-Users-sokomishalov-idea-justplay-backend/ff6ca444-5119-49a5-b0e1-aa24be3961f5/scratchpad/z6
cd $Z
f(){ T="File:$(grep -h "^ДАКО_Р-5634-1-$1[._]" ai.txt | head -1 | awk '{print $1}')"; STEP=$4 DELAY=5 python3 -I ../z4/fetchpdf2.py "$T" t$1 $2 $3 1000 | tail -2; sleep 10; }
f 3674 191 195 2
f 4092 47 57 2
f 3267 223 225 2
f 4465 176 250 2
f 4841 355 423 2
echo ALLDONE
