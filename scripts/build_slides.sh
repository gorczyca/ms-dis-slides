# scripts/build_slides.sh
#!/usr/bin/env bash
set -euo pipefail

# Usage:
#   ./scripts/build_slides.sh render|html|all \
#     [--scenes-file scenes.list] [--site site] \
#     [--pythonpath .] [--manim-flags "..."] [--slides-flags "..."]

MODE="${1:-}"; shift || true
SCENES_FILE="scenes.list"
SITE="site"
PYTHONPATH_IN="."
MANIM_FLAGS=""
SLIDES_FLAGS="--one-file --offline"

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
  while read -r file scene || [[ -n "${file:-}${scene:-}" ]]; do
    [[ -z "${file:-}" || "${file:0:1}" == "#" ]] && continue
    out="$SITE/${scene}.html"
    echo "HTML: $scene -> $out"
    PYTHONPATH="$PYTHONPATH" manim-slides convert $SLIDES_FLAGS "$scene" "$out"
  done < "$SCENES_FILE"
}

case "$MODE" in
  render) render ;;
  html)   html ;;
  all)    render; html ;;
  *) echo "Unknown MODE: $MODE" >&2; exit 2 ;;
esac
