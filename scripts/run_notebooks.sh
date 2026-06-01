#!/usr/bin/env bash
# Execute notebooks in place via jupyter nbconvert.
#
# Usage:
#   scripts/run_notebooks.sh              # run every notebook under notebooks/
#   scripts/run_notebooks.sh figure_5     # run only notebooks/figure_5/*.ipynb
#
# Outputs are written into the .ipynb files; the pre-commit hook strips them
# again before commit, so re-running before pushing is safe.

set -euo pipefail

repo_root="$(cd "$(dirname "$0")/.." && pwd)"
cd "$repo_root"

target="${1:-}"
if [[ -n "$target" ]]; then
  base="notebooks/$target"
  if [[ ! -d "$base" ]]; then
    echo "error: $base not found" >&2
    exit 1
  fi
else
  base="notebooks"
fi

notebooks=()
while IFS= read -r nb; do
  notebooks+=("$nb")
done < <(find "$base" -name '*.ipynb' -not -path '*/.ipynb_checkpoints/*' | sort)
if [[ ${#notebooks[@]} -eq 0 ]]; then
  echo "no notebooks found under $base" >&2
  exit 1
fi

for nb in "${notebooks[@]}"; do
  echo ">>> $nb"
  uv run jupyter nbconvert --log-level=WARN --to notebook --execute --inplace "$nb"
done
