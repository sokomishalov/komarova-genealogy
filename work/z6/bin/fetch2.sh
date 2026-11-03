#!/bin/bash
Z=/private/tmp/claude-501/-Users-sokomishalov-idea-justplay-backend/ff6ca444-5119-49a5-b0e1-aa24be3961f5/scratchpad/z6
cd $Z
g(){ T=$(grep -h "Р-5634-1-$1[._ ]" stav.txt kras.txt | head -1); [ -z "$T" ] && T="File:$(grep -h "^ДАКО_Р-5634-1-$1[._]" ai.txt | head -1 | awk '{print $1}')"; echo "== $1 $T"; DELAY=5 python3 -I ../z4/fetchpdf2.py "$T" t$1 $2 $3 1000 | tail -1; sleep 8; }
g 3267 227 227
g 2329 2 5
g 2339 2 5
g 3044 2 5
g 2032 2 5
g 2041 2 5
g 976 2 5
echo ALLDONE
