#!/usr/bin/env python3
"""Inspect and validate links in a PDF and optionally write a JSON report."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys
from typing import Any

try:
    import fitz  # PyMuPDF
except ImportError as exc:
    raise SystemExit("PyMuPDF is required. Install it with: pip install pymupdf") from exc


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--report")
    args = parser.parse_args()

    input_path = Path(args.input)
    doc = fitz.open(str(input_path))
    page_count = len(doc)
    records: list[dict[str, Any]] = []
    errors: list[str] = []

    try:
        for page_index, page in enumerate(doc):
            for link_index, link in enumerate(page.get_links(), start=1):
                rect = fitz.Rect(link["from"])
                status = "ok"
                error = None
                destination_page = None
                url = None

                if rect.width <= 0 or rect.height <= 0:
                    status = "error"
                    error = "non-positive rectangle"
                elif (
                    rect.x0 < page.rect.x0
                    or rect.y0 < page.rect.y0
                    or rect.x1 > page.rect.x1
                    or rect.y1 > page.rect.y1
                ):
                    status = "error"
                    error = "rectangle outside page"

                kind = link.get("kind")
                if kind == fitz.LINK_GOTO:
                    destination_index = link.get("page", -1)
                    destination_page = destination_index + 1
                    if destination_index < 0 or destination_index >= page_count:
                        status = "error"
                        error = f"destination outside 1-{page_count}"
                elif kind == fitz.LINK_URI:
                    url = link.get("uri")
                    if not url:
                        status = "error"
                        error = "missing URL"
                else:
                    status = "warning" if status == "ok" else status
                    error = error or f"unhandled link kind {kind}"

                record = {
                    "source_page": page_index + 1,
                    "link_number_on_page": link_index,
                    "kind": kind,
                    "rectangle": [rect.x0, rect.y0, rect.x1, rect.y1],
                    "destination_page": destination_page,
                    "url": url,
                    "status": status,
                    "error": error,
                }
                records.append(record)
                if status == "error":
                    errors.append(
                        f"Page {page_index + 1}, link {link_index}: {error}"
                    )
    finally:
        doc.close()

    report = {
        "input": str(input_path),
        "page_count": page_count,
        "link_annotation_count": len(records),
        "error_count": len(errors),
        "links": records,
        "errors": errors,
    }

    if args.report:
        report_path = Path(args.report)
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(json.dumps(report, indent=2), encoding="utf-8")

    print(json.dumps({
        "page_count": page_count,
        "link_annotation_count": len(records),
        "error_count": len(errors),
    }, indent=2))

    if not records:
        print("ERROR: No link annotations found.", file=sys.stderr)
        return 2
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
