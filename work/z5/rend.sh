#!/bin/bash
cd /private/tmp/claude-501/-Users-sokomishalov-idea-justplay-backend/ff6ca444-5119-49a5-b0e1-aa24be3961f5/scratchpad/z5
for v in "$@"; do
  while [ ! -s pdf/$v.pdf ]; do sleep 30; done
  mkdir -p r$v/p; [ -n "$(ls r$v/p)" ] || pdftoppm -scale-to-x 1600 -scale-to-y -1 -gray -jpeg -jpegopt quality=80 pdf/$v.pdf r$v/p/p
  echo "rendered $v $(ls r$v/p | wc -l)"
done
