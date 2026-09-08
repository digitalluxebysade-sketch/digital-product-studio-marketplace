#!/usr/bin/env python3
"""Build a PDF from ordered PNG/JPG images without stretching them."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

try:
    import fitz  # PyMuPDF
except ImportError as exc:
    raise SystemExit("PyMuPDF is required. Install it with: pip install pymupdf") from exc


SUPPORTED = {".png", ".jpg", ".jpeg", ".webp"}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-dir", required=True, help="Folder containing numbered images")
    parser.add_argument("--output", required=True, help="Output PDF")
    args = parser.parse_args()

    input_dir = Path(args.input_dir)
    output = Path(args.output)
    if not input_dir.is_dir():
        raise SystemExit(f"Input directory not found: {input_dir}")

    images = sorted(p for p in input_dir.iterdir() if p.suffix.lower() in SUPPORTED)
    if not images:
        raise SystemExit("No supported page images found.")

    doc = fitz.open()
    try:
        for image_path in images:
            pix = fitz.Pixmap(str(image_path))
            width, height = float(pix.width), float(pix.height)
            page = doc.new_page(width=width, height=height)
            page.insert_image(page.rect, filename=str(image_path), keep_proportion=True)
        output.parent.mkdir(parents=True, exist_ok=True)
        doc.save(str(output), garbage=4, deflate=True)
    finally:
        doc.close()

    print(f"Created {output} with {len(images)} pages.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
