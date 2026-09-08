#!/usr/bin/env python3
"""Add internal and external hyperlink annotations to a planner PDF."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys
from typing import Any, Iterable

try:
    import fitz  # PyMuPDF
except ImportError as exc:
    raise SystemExit("PyMuPDF is required. Install it with: pip install pymupdf") from exc


def parse_source_pages(value: Any, page_count: int) -> list[int]:
    """Return zero-based source page indices."""
    if value == "all":
        return list(range(page_count))
    if isinstance(value, int):
        values = [value]
    elif isinstance(value, list):
        values = value
    elif isinstance(value, str):
        values = []
        for part in value.split(","):
            part = part.strip()
            if not part:
                continue
            if "-" in part:
                start_s, end_s = part.split("-", 1)
                start, end = int(start_s), int(end_s)
                values.extend(range(start, end + 1))
            else:
                values.append(int(part))
    else:
        raise ValueError(f"Unsupported source_pages value: {value!r}")

    result = []
    for page_number in values:
        index = int(page_number) - 1
        if index < 0 or index >= page_count:
            raise ValueError(f"Source page {page_number} is outside 1-{page_count}")
        result.append(index)
    return sorted(set(result))


def rect_to_points(
    rect_values: list[float],
    units: str,
    page_rect: "fitz.Rect",
    pixel_size: dict[str, float] | None,
) -> "fitz.Rect":
    if len(rect_values) != 4:
        raise ValueError("rect must contain four numbers")
    x0, y0, x1, y1 = map(float, rect_values)

    if units == "normalized":
        rect = fitz.Rect(
            x0 * page_rect.width,
            y0 * page_rect.height,
            x1 * page_rect.width,
            y1 * page_rect.height,
        )
    elif units == "pixels":
        if not pixel_size:
            raise ValueError("page_size_pixels is required for pixel rectangles")
        pw = float(pixel_size["width"])
        ph = float(pixel_size["height"])
        rect = fitz.Rect(
            x0 / pw * page_rect.width,
            y0 / ph * page_rect.height,
            x1 / pw * page_rect.width,
            y1 / ph * page_rect.height,
        )
    elif units == "pdf_points":
        rect = fitz.Rect(x0, y0, x1, y1)
    else:
        raise ValueError(f"Unsupported rect_units: {units}")

    if rect.width <= 0 or rect.height <= 0:
        raise ValueError(f"Rectangle has non-positive size: {rect}")
    if (
        rect.x0 < page_rect.x0
        or rect.y0 < page_rect.y0
        or rect.x1 > page_rect.x1
        or rect.y1 > page_rect.y1
    ):
        raise ValueError(f"Rectangle falls outside page: {rect} vs {page_rect}")
    return rect


def resolve_destination(value: Any, source_index: int, page_count: int) -> int:
    if isinstance(value, int):
        destination = value - 1
    elif value == "next":
        destination = source_index + 1
    elif value == "previous":
        destination = source_index - 1
    else:
        raise ValueError(f"Unsupported destination_page: {value!r}")

    if destination < 0 or destination >= page_count:
        raise ValueError(
            f"Destination page {destination + 1} is outside 1-{page_count}"
        )
    return destination


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--map", required=True, dest="map_path")
    parser.add_argument("--output", required=True)
    parser.add_argument(
        "--replace-existing-links",
        action="store_true",
        help="Delete existing link annotations before adding the new map",
    )
    args = parser.parse_args()

    input_path = Path(args.input)
    map_path = Path(args.map_path)
    output_path = Path(args.output)

    config = json.loads(map_path.read_text(encoding="utf-8"))
    links = config.get("links", [])
    if not links:
        raise SystemExit("The hyperlink map contains no links.")

    doc = fitz.open(str(input_path))
    page_count = len(doc)
    pixel_size = config.get("page_size_pixels")
    inserted = 0
    errors: list[str] = []

    try:
        if args.replace_existing_links:
            for page in doc:
                for existing_link in list(page.get_links()):
                    page.delete_link(existing_link)

        for entry in links:
            link_id = entry.get("id", "UNNAMED")
            try:
                source_indices = parse_source_pages(entry["source_pages"], page_count)
                for source_index in source_indices:
                    page = doc[source_index]
                    rect = rect_to_points(
                        entry["rect"],
                        entry.get("rect_units", "normalized"),
                        page.rect,
                        pixel_size,
                    )

                    if "external_url" in entry:
                        url = str(entry["external_url"]).strip()
                        if not (url.startswith("https://") or url.startswith("http://")):
                            raise ValueError(f"Unsupported external URL scheme: {url}")
                        link = {"kind": fitz.LINK_URI, "from": rect, "uri": url}
                    else:
                        destination = resolve_destination(
                            entry["destination_page"], source_index, page_count
                        )
                        link = {
                            "kind": fitz.LINK_GOTO,
                            "from": rect,
                            "page": destination,
                        }
                    page.insert_link(link)
                    inserted += 1
            except Exception as exc:
                errors.append(f"{link_id}: {exc}")

        if errors:
            raise SystemExit("Link map validation failed:\n- " + "\n- ".join(errors))

        output_path.parent.mkdir(parents=True, exist_ok=True)
        doc.save(str(output_path), garbage=4, deflate=True, incremental=False)
    finally:
        doc.close()

    print(f"Created {output_path}")
    print(f"Inserted link annotations: {inserted}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
