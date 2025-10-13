#!/usr/bin/env bash
set -euo pipefail

MODE="${1:-}"; shift || true
SCENES_FILE="scenes.list"
SITE="site"
PYTHONPATH_IN="."
MANIM_FLAGS=""
# For a single self-contained HTML use --one-file; drop it to get an assets folder.
SLIDES_FLAGS="--offline --one-file"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --scenes-file) SCENES_FILE="$2"; shift 2 ;;
    --site)        SITE="$2"; shift 2 ;;
    --pythonpath)  PYTHONPATH_IN="$2"; shift 2 ;;
    --manim-flags) MANIM_FLAGS="$2"; shift 2 ;;
    --slides-flags) SLIDES_FLAGS="$2"; shift 2 ;;
    *) echo "Unknown arg: $1" >&2; exit 2 ;;
  esac
done

[[ -n "${MODE}" ]] || { echo "MODE required: render|html|all" >&2; exit 2; }
[[ -f "$SCENES_FILE" ]] || { echo "No $SCENES_FILE" >&2; exit 2; }
mkdir -p "$SITE"

export PYTHONPATH="${PYTHONPATH_IN}${PYTHONPATH:+:${PYTHONPATH}}"

render() {
  while read -r file scene || [[ -n "${file:-}${scene:-}" ]]; do
    [[ -z "${file:-}" || "${file:0:1}" == "#" ]] && continue
    echo "Render: $file $scene"
    PYTHONPATH="$PYTHONPATH" manim $MANIM_FLAGS "$file" "$scene"
  done < "$SCENES_FILE"
}

html() {
  mapfile -t scenes < <(awk '!/^#/ && NF{print $2}' "$SCENES_FILE")
  echo "HTML (combined): ${scenes[*]} -> $SITE/index.html"
  PYTHONPATH="$PYTHONPATH" manim-slides convert $SLIDES_FLAGS "${scenes[@]}" "$SITE/index.html"
}

case "$MODE" in
  render) render ;;
  html)   html ;;
  all)    render; html ;;
  *) echo "Unknown MODE: $MODE" >&2; exit 2 ;;
esac
