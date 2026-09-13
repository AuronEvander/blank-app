#!/usr/bin/env bash
# Downloads the AI-generated media listed in site/media/manifest.json into site/media/.
# Run from the repo root on a machine with normal internet access.
set -euo pipefail
cd "$(dirname "$0")/.."
base=$(python3 -c "import json;print(json.load(open('site/media/manifest.json'))['base'])")
python3 -c "import json;[print(i['file'],i['remote']) for i in json.load(open('site/media/manifest.json'))['items'] if i['remote']]" |
while read -r file remote; do
  echo "→ $file"; curl -fsSL -o "site/media/$file" "$base$remote"
done
echo "done: $(ls site/media | wc -l) files in site/media/"
