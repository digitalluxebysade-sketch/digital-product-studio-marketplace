---
name: hyperlink-digital-planner-pdf
description: Creates and verifies genuinely clickable hyperlinked digital-planner PDFs from approved planner page images or an existing PDF. Use when the user asks to hyperlink planner tabs, navigation buttons, months, sections, index items, or page thumbnails; assemble planner images into a PDF; repair broken planner links; or test a GoodNotes, Notability, Canva, or tablet planner PDF.
---

# Hyperlink Digital Planner PDF

## Required Undated All-in-One Standard

Read `references/all-in-one-planner-standard.md` and inspect `assets/planner-visual-reference.jpg` as the navigation-coverage baseline. Align rectangles with the exact visible tab and button shapes. Cover all top tabs, right-edge month or section tabs, Index, Quick Menu, Home and category icons, month and week buttons, review buttons, and repeated navigation controls. The standard is undated; do not introduce 2025.

## Purpose

Create a real, clickable digital-planner PDF. The completed PDF must contain embedded internal PDF links or approved external links. Visible tab artwork alone does not count as hyperlinking.

This skill can:

- Assemble final PNG or JPG planner pages into one PDF
- Add invisible clickable rectangles over tabs and navigation buttons
- Link months, sections, index items, and dashboard buttons to destination pages
- Add Home, Back, Next, Previous, Index, Notes, Weekly, Daily, and other navigation
- Add approved external URL links
- Repair or replace broken links
- Inspect and verify link annotations
- Preserve the original page artwork and dimensions
- Produce a link map and validation report

## Non-negotiable rules

1. Never describe a PDF as hyperlinked unless link annotations were actually embedded.
2. Never pretend a flat PNG or JPG is clickable.
3. Use finalized planner pages and finalized page order before hyperlinking.
4. Do not redesign, regenerate, crop, compress, recolor, or alter approved page artwork while adding links.
5. Use invisible link rectangles unless the user asks for visible buttons.
6. Align every link rectangle with the visible tab, icon, text, or button it represents.
7. Use one-based page numbers in user-facing maps and reports.
8. Validate every internal destination page.
9. Reject any rectangle that falls outside its source page.
10. Test link coverage and destinations before delivery.
11. Keep page dimensions and orientation unchanged.
12. Re-render the final PDF to confirm no visible artwork changed.
13. Provide a clear report of any pages or controls that could not be linked reliably.
14. Do not create external links without the user's requested or supplied destination.
15. Do not hyperlink placeholder tabs to invented destinations.

## Inputs

Use the user's existing information without asking again. Determine or obtain only what is still necessary:

- Existing planner PDF, or ordered planner page images
- Exact final page order
- Page dimensions
- Tab and navigation labels
- Destination page for each control
- Pages on which each control appears
- Whether controls repeat across all pages or only a section
- Whether active tabs should also remain clickable
- Any external URLs
- Desired filename
- Whether the user wants a link map and validation report

When destination information is incomplete, infer only obvious structural destinations from filenames or page titles. Mark uncertain destinations for review rather than inventing them.

## Required workflow

### Phase 1 - Preflight

1. Inspect the source files.
2. Confirm page count.
3. Confirm page order.
4. Confirm page dimensions and orientation.
5. Identify duplicate or missing pages.
6. If using images, assemble them into a PDF without changing their proportions.
7. Render the source PDF to images for visual inspection.
8. Save a pre-link reference copy.

Stop and repair the source order before hyperlinking when the page sequence is wrong.

### Phase 2 - Create the page inventory

Create an ordered inventory:

| PDF page | Filename or visible title | Section | Destination ID |
|---:|---|---|---|
| 1 | Front Cover | Cover | PAGE-001 |
| 2 | Dashboard | Home | PAGE-002 |

Use stable destination IDs. Do not renumber IDs after links are created without rebuilding and retesting the link map.

### Phase 3 - Create the hyperlink map

Use `assets/hyperlink-map-template.json` or an equivalent structured map.

Every link entry must record:

- Stable link ID
- Visible label
- Source page or source page range
- Rectangle coordinates
- Coordinate units
- Destination page, dynamic destination, or external URL
- Control type
- Whether it repeats
- Notes

Preferred coordinate units:

- `normalized`: values from 0 to 1, portable across equal-layout pages
- `pixels`: measured against the source image dimensions
- `pdf_points`: direct PDF coordinates

Use normalized coordinates for repeated tabs when all pages use the same locked layout.

### Phase 4 - Build or open the PDF

When the user supplies ordered page images:

1. Sort by the approved numbered filenames.
2. Create one PDF page per image.
3. Match each PDF page to the image aspect ratio.
4. Insert the image edge-to-edge without stretching.
5. Do not add margins unless the user requests them.
6. Preserve the requested sequence.

When the user supplies an existing PDF:

1. Work from a duplicate.
2. Preserve metadata when practical.
3. Remove or replace old broken planner links only when necessary.
4. Do not flatten useful existing links without a reason.

### Phase 5 - Add links

Use PDF link annotations.

For internal links:

- Link to the exact zero-based PDF destination internally while displaying one-based numbering to the user.
- Use `GoTo` links.
- Link repeated tabs on every intended source page.
- Keep Home linked to the dashboard or index.
- Use dynamic Previous and Next links only where a valid page exists.
- Do not create Previous on the first page or Next on the last page unless the user requests wraparound.

For external links:

- Use URI annotations.
- Validate that the URL has a supported scheme such as `https://`.
- Do not silently modify the URL.

### Phase 6 - Navigation logic

Common mappings:

- Home -> dashboard or index
- Month tab -> month divider or monthly dashboard
- Week tab -> first weekly page for that section
- Day tab -> first daily page for that section
- Notes -> notes divider or first notes page
- Budget -> budget divider
- Goals -> goals divider
- Back -> previous logical page
- Next -> next logical page
- Previous month -> prior month divider
- Next month -> next month divider

The user's approved map overrides these defaults.

### Phase 7 - Verification

Run all checks below.

#### Structural checks

- Link annotation count is greater than zero
- Every intended source page contains the expected links
- Every internal destination is within the PDF page range
- Every rectangle has positive width and height
- Every rectangle lies inside the page
- Repeated links appear on all specified pages
- No accidental duplicate annotation occupies the same rectangle with a different destination
- External URLs use an approved scheme

#### Visual checks

- Render the final PDF.
- Confirm no visible artwork changed.
- Confirm no unexpected borders, boxes, or link colors appear.
- Confirm tabs remain fully visible.
- Confirm page dimensions and orientation match the source.
- Compare source and final renders when a source PDF was provided.

#### Destination checks

Create a validation report listing:

- Link ID
- Source page
- Visible label
- Destination page or URL
- Status
- Error, if any

A PDF is not complete while any required link has an unresolved or out-of-range destination.

### Phase 8 - Delivery

Provide:

1. Final hyperlinked PDF
2. Hyperlink map
3. Page inventory
4. Link validation report
5. Page count
6. Total number of link annotations
7. Statement that the links were embedded and structurally verified
8. Any viewer-specific testing limitations

Do not claim that every third-party app was manually tested unless it was actually tested there.

## Preferred helper scripts

This skill includes:

- `scripts/build_pdf_from_images.py`
- `scripts/hyperlink_planner_pdf.py`
- `scripts/inspect_pdf_links.py`

Use them when available. They preserve the visual pages and add PDF annotations programmatically.

### Build from images

```bash
python scripts/build_pdf_from_images.py \
  --input-dir "/path/to/ordered-pages" \
  --output "/path/to/planner-unlinked.pdf"
```

### Add hyperlinks

```bash
python scripts/hyperlink_planner_pdf.py \
  --input "/path/to/planner-unlinked.pdf" \
  --map "/path/to/hyperlink-map.json" \
  --output "/path/to/planner-hyperlinked.pdf"
```

### Inspect links

```bash
python scripts/inspect_pdf_links.py \
  --input "/path/to/planner-hyperlinked.pdf" \
  --report "/path/to/link-validation-report.json"
```

## Coordinate rules

PDF coordinates use a top-left visual coordinate system when handled through the included PyMuPDF scripts.

For normalized rectangles:

- `[0, 0, 1, 1]` covers the whole page.
- `[0.90, 0.10, 0.99, 0.18]` covers a right-edge tab near the top.

For pixel rectangles:

- Supply `page_size_pixels` in the hyperlink map.
- Rectangles are scaled to the actual PDF page.

Never estimate tiny hitboxes. Make the clickable region large enough to tap comfortably while avoiding overlap with neighboring controls.

## Duplicate and overlap policy

Overlapping rectangles are acceptable only when they lead to the same destination and are intentional. Reject ambiguous overlaps that lead to different destinations.

## Repair workflow

When repairing a PDF:

1. Inspect existing annotations.
2. Export a report.
3. Identify incorrect, missing, duplicate, or out-of-range links.
4. Preserve correct links.
5. Replace only defective links when possible.
6. Re-run the full validation.
7. Render and visually compare the repaired PDF.

## GoodNotes and tablet guidance

Internal PDF links are generally activated in reading or navigation mode rather than handwriting/editing mode. Do not label this viewer behavior as a broken PDF link.

Viewer behavior can vary. Structural PDF verification is required even when a particular app cannot be opened in the current environment.

## Failure conditions

Reject and correct the output when:

- The PDF has no link annotations
- A visible tab has no required link
- A link goes to the wrong page
- A destination is out of range
- A hitbox is outside the page
- Adjacent tab hitboxes overlap ambiguously
- The page order changed
- The artwork changed
- Image quality was visibly reduced
- The output was called hyperlinked without being verified

## Activation examples

Use this skill for prompts such as:

- "Hyperlink all monthly tabs in this digital planner PDF."
- "Turn these planner PNGs into a clickable GoodNotes PDF."
- "Add Home, Back, and Next buttons to every page."
- "Repair the tabs that go to the wrong month."
- "Create a hyperlink map and test every link before giving me the PDF."
- "Make the planner tabs clickable without changing the page design."
