#!/usr/bin/env bash

# Recursively convert supported images to AVIF using ffmpeg.
# Compatible with Linux and macOS.
#
# Usage:
#   ./convert-to-avif.sh INPUT_PATH [--max-side 800] [--crf 35] [--overwrite]
#
# Examples:
#   ./convert-to-avif.sh .
#   ./convert-to-avif.sh ~/Pictures --max-side 1200 --crf 30 --overwrite

set -u

input_path=""
max_side=800
crf=35
overwrite=0

usage() {
  cat <<'USAGE'
Usage:
  convert-to-avif.sh INPUT_PATH [options]

Options:
  --max-side N, -m N   Resize so the longest side is at most N pixels. Default: 800
  --crf N, -q N        AVIF quality/CRF value. Lower is higher quality. Default: 35
  --overwrite, -y      Replace existing .avif files
  --help, -h           Show this help

Supported input files:
  .jpg, .jpeg, .png, .gif, .webp

Requires:
  ffmpeg with libaom-av1 support
USAGE
}

fail() {
  printf 'Error: %s\n' "$1" >&2
  exit 1
}

resolve_dir() {
  # Resolve an existing directory to an absolute physical path without relying on GNU realpath.
  local path=$1
  (cd "$path" 2>/dev/null && pwd -P) || return 1
}

is_positive_integer() {
  case "$1" in
    ''|*[!0-9]*) return 1 ;;
    *) [ "$1" -gt 0 ] ;;
  esac
}

while [ "$#" -gt 0 ]; do
  case "$1" in
    --max-side|-m)
      [ "$#" -ge 2 ] || fail "$1 requires a value"
      max_side=$2
      shift 2
      ;;
    --crf|-q)
      [ "$#" -ge 2 ] || fail "$1 requires a value"
      crf=$2
      shift 2
      ;;
    --overwrite|-y)
      overwrite=1
      shift
      ;;
    --help|-h)
      usage
      exit 0
      ;;
    --)
      shift
      break
      ;;
    -*)
      fail "Unknown option: $1"
      ;;
    *)
      if [ -z "$input_path" ]; then
        input_path=$1
      else
        fail "Unexpected argument: $1"
      fi
      shift
      ;;
  esac
done

# Support a positional INPUT_PATH after -- as well.
if [ -z "$input_path" ] && [ "$#" -gt 0 ]; then
  input_path=$1
  shift
fi

[ "$#" -eq 0 ] || fail "Unexpected argument: $1"
[ -n "$input_path" ] || { usage >&2; exit 2; }

command -v ffmpeg >/dev/null 2>&1 || fail "ffmpeg not found in PATH."
[ -e "$input_path" ] || fail "Input path does not exist: $input_path"
[ -d "$input_path" ] || fail "Input path must be a directory: $input_path"

is_positive_integer "$max_side" || fail "--max-side must be a positive integer: $max_side"
is_positive_integer "$crf" || fail "--crf must be a positive integer: $crf"

input_root=$(resolve_dir "$input_path") || fail "Could not resolve input path: $input_path"

found=0
converted=0
skipped=0
failed=0
ffmpeg_overwrite_flag="-n"
[ "$overwrite" -eq 1 ] && ffmpeg_overwrite_flag="-y"

# Resize to max side, avoid upscaling, then flatten transparency onto white.
filter="[0:v]scale='trunc(iw*min(1,min(${max_side}/iw,${max_side}/ih))/2)*2':'trunc(ih*min(1,min(${max_side}/iw,${max_side}/ih))/2)*2':in_range=pc:out_range=tv,format=rgba,split[fg][bg];[bg]drawbox=x=0:y=0:w=iw:h=ih:color=white:t=fill[bgw];[bgw][fg]overlay,format=yuv420p"

while IFS= read -r -d '' file; do
  found=1

  dir=$(dirname "$file")
  name=$(basename "$file")
  base=${name%.*}
  target_file="${dir}/${base}.avif"

  if [ -e "$target_file" ] && [ "$overwrite" -ne 1 ]; then
    printf 'Skipping already converted: %s\n' "$file"
    skipped=$((skipped + 1))
    continue
  fi

  printf 'Converting: %s\n' "$file"

  if ffmpeg \
    "$ffmpeg_overwrite_flag" \
    -i "$file" \
    -filter_complex "$filter" \
    -frames:v 1 \
    -c:v libaom-av1 \
    -still-picture 1 \
    -crf "$crf" \
    -b:v 0 \
    -pix_fmt yuv420p \
    "$target_file"; then
    converted=$((converted + 1))
  else
    printf 'Warning: ffmpeg failed for: %s\n' "$file" >&2
    failed=$((failed + 1))
  fi
done < <(
  find "$input_root" -type f \( \
    -iname '*.jpg' -o \
    -iname '*.jpeg' -o \
    -iname '*.png' -o \
    -iname '*.gif' -o \
    -iname '*.webp' \
  \) -print0
)

if [ "$found" -eq 0 ]; then
  printf 'No supported image files found under: %s\n' "$input_root"
  exit 0
fi

printf 'Done. Converted: %d, skipped: %d, failed: %d.\n' "$converted" "$skipped" "$failed"

if [ "$failed" -gt 0 ]; then
  exit 1
fi
