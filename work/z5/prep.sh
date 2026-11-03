#!/bin/bash
S=/private/tmp/claude-501/-Users-sokomishalov-idea-justplay-backend/ff6ca444-5119-49a5-b0e1-aa24be3961f5/scratchpad
cd $S/z5; v=$1
mkdir -p r$v/p; [ -n "$(ls r$v/p)" ] || pdftoppm -r 90 -gray -jpeg -jpegopt quality=80 pdf/$v.pdf r$v/p/p
pdfinfo pdf/$v.pdf | grep Pages
RNG=1-24 $S/venv/bin/python -I thumbs.py r$v/p r$v/t0 250 6 4
