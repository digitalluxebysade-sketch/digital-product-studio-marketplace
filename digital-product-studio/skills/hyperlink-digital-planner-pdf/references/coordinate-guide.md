# Coordinate Guide

## Rectangle format

All rectangles use:

`[x0, y0, x1, y1]`

where:

- `x0` = left
- `y0` = top
- `x1` = right
- `y1` = bottom

## Normalized coordinates

Normalized coordinates range from 0 to 1.

Example right-side tab:

```json
{
  "rect": [0.90, 0.10, 0.99, 0.18],
  "rect_units": "normalized"
}
```

## Pixel coordinates

Pixel coordinates must match the source page image size declared in the map.

```json
{
  "page_size_pixels": {"width": 567, "height": 726},
  "rect": [510, 72, 565, 130],
  "rect_units": "pixels"
}
```

## PDF points

Use direct PDF points only when they were measured from the PDF.

## Tap comfort

Use a generous hitbox that covers the visible control without overlapping a neighboring control. Small labels may need a slightly larger invisible rectangle.
