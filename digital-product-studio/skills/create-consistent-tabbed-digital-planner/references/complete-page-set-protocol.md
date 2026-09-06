# Complete Page-Set Generation Protocol

## Objective

Generate the exact requested number of separate, full-canvas, functional planner pages. Use the approved master shell internally for consistency, never as a substitute for the finished page set.

## Count contract

1. Obtain the requested finished functional page count.
2. Clarify whether the count includes a cover only when the user makes that ambiguous.
3. Exclude covers and auxiliary assets by default.
4. Create exactly one manifest row for each counted page.
5. Confirm `Manifest count: N of N requested pages` before generation.

Do not count:

- Blank master shells
- Navigation-only pages
- Empty writing sheets
- Decorative backgrounds
- Covers unless explicitly included
- Mockups
- Duplicate pages without meaningful functional changes
- Collages or contact sheets containing miniature pages

## Manifest requirements

Record for every page:

- Sequence number
- Unique page title
- Functional purpose
- Required worksheet components
- Filename
- Active tab
- Generation status
- QA result

Reject a manifest that has too few or too many rows, duplicate-only entries, empty-purpose rows, or pages without useful worksheet content.

## Production loop

For page `X` of `N`:

1. Start from the approved master shell.
2. Preserve the locked full-canvas base, tabs, navigation, internal dividers, margins, and theme.
3. Add the manifest page's unique title and complete functional content.
4. Fill the full canvas edge to edge with the cream or white worksheet; do not place a smaller page inside a background, mockup, frame, mat, or decorative scene.
5. Save one separate full-size file.
6. Run content, text, dimension, and tab-lock QA.
7. Mark `Page X of N: completed` only after the page passes.
8. Regenerate failures from the master shell.
9. Continue to the next incomplete row automatically.

Use manageable batches when necessary, but do not stop merely because a batch completed. Stop only when all `N` manifest rows pass QA or when user input is genuinely required.

## Functional-content rule

Every page must be ready to use. Select components appropriate to its purpose, such as:

- Calendars with verified dates and weekday placement
- Schedules and time blocks
- Tables with meaningful column headings
- Trackers with labels, scales, or check fields
- Checklists with usable writing space
- Grids or structured writing lines
- Prompts that guide the intended activity
- Totals, summaries, priorities, notes, and reflection fields where useful

A title above an otherwise blank area is not sufficient functional content.

## Completion gate

Before export, verify:

- Final file count equals the requested count.
- Every manifest row has one separate full-size file.
- No file is missing, blank, duplicate-only, or a miniature collage.
- No blank shell is included unless separately requested.
- Every page contains accurate, page-specific functional content.
- All tabs and locked visual elements match the approved shell.
- Every outer edge passes the Canvas Equals Planner Page checks with zero surrounding background.
- All headings, prompts, tables, and calendar data are accurate.

Create the high-resolution PDF only after this gate passes. Keep the separate page files available.
