#!/bin/bash
# run.sh vol "refs" x0 y0 x1 y1
S=/private/tmp/claude-501/-Users-sokomishalov-idea-justplay-backend/ff6ca444-5119-49a5-b0e1-aa24be3961f5/scratchpad
export LC_ALL=C; cd $S/z5; v=$1; P=$S/venv/bin/python
$P -I classify.py r$v/p $2 > r$v/cls.txt
awk '{a=$3;b=$4;m=(a>b)?a:b;d=a-b;if(d<0)d=-d; if($2=="F"||m<0.5||d<0.3) print $1}' r$v/cls.txt > r$v/faces.txt
rm -rf r$v/c r$v/l; LIST=r$v/faces.txt $P -I crops.py r$v/p r$v/c $3 $4 $5 $6 520 3 10
true
