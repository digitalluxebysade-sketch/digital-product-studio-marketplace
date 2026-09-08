---
name: create-consistent-tabbed-digital-planner
description: Creates complete multi-page digital planner products exclusively with ChatGPT Images 2.0 image generation and image editing, including separately generated full-bleed functional pages and a locked tab system that remains identical on every tabbed page. Use when the user asks to create a digital planner, planner cover, planner interior or interiors, GoodNotes planner, hyperlinked-style planner, tabbed planner, PLR planner, or coordinated planner-page collection. This skill requires an exact page manifest and makes the image canvas itself the planner page, never a smaller sheet on a background or mockup.
---

# Create Consistent Tabbed Digital Planner

## Writing-First Worksheet Layout Rule

Design every worksheet and functional planner page around practical writing space. Do not make headings, decorative boxes, or individual sections unnecessarily large. Use a balanced, compact layout with about 4–7 useful sections when the page type supports it. Keep section titles small, clear, and easy to read; use thin borders, compact labels, efficient spacing, and consistent compact padding.

Use writing areas for about 60–75% of the page and decorative elements for no more than about 10–15%. Avoid oversized blank boxes that only fit one or two items. Divide large areas into useful lines, checkboxes, grids, or columns. Do not crowd the page or waste space. Keep decorations small and around the edges rather than centered over the worksheet. Do not simplify a worksheet by removing useful sections: when space is limited, reduce decorations, heading size, padding, and border thickness before reducing writing space. A side margin is allowed only on the cover page; every interior worksheet must be full-canvas with no exterior side margin.

**Version: 2.2.1**

## Purpose

Create a complete, polished, sellable digital planner using **ChatGPT Images 2.0** for the cover and every visual planner page. Treat **planner interior** as the complete collection of separately generated, full-canvas, functional planner pages. It never means one generic blank or reusable sheet.

## Image-generation-only product creation

Use ChatGPT Images 2.0 image generation or image editing as the only method for creating, revising, or correcting every planner visual. This includes covers, master shells, divider pages, tabs, rings or binding treatments, layouts, page content, and decorations.

Do not create planner visuals with Canva, code, HTML, CSS, JavaScript, SVG, a spreadsheet, PDF drawing, or any other non-image-generation method. A later PDF assembly or hyperlink stage may preserve and annotate the approved image-generated pages, but it must never become a substitute for image-generated planner creation.

The tab system is a locked master design. After approval, the tabs must not change in count, wording, order, size, shape, placement, spacing, font, color, border, shadow, or alignment on any page.

This skill creates actual visual assets. Do not stop at concepts, outlines, page lists, or image prompts unless the user specifically asks for planning only.

## Non-negotiable rules

1. Use ChatGPT Images 2.0 for all original planner visuals.
2. Do not code the planner or create HTML, CSS, JavaScript, or an app.
3. Create every requested page at the user's exact dimensions.
4. Keep the design uncluttered, writable, and practical.
5. Create one approved **Master Interior Shell** before generating the full interior.
6. Every later tabbed page must be made by editing or reusing that exact approved Master Interior Shell.
7. Never redraw the tab system from memory or from a text-only description after the master is approved.
8. Do not change the theme, palette, paper texture, margins, full-canvas page base, approved internal dividers, binding area, or tab rail unless the user requests a redesign.
9. Do not claim the tabs are consistent until they pass the Tab Lock Quality Check.
10. Do not place tabs outside the planner page or outside an iPad screen when making a mockup.
11. Do not create fake clickable links inside a flat image. Create a hyperlink map for later linking in Canva, PDF software, GoodNotes, or another editor when requested.
12. Do not copy exact copyrighted artwork from a reference. Use references for theme, mood, palette, layout inspiration, and level of polish while creating an original design.
13. Ask how many finished functional pages the user wants unless the user already supplied the number.
14. Create and count a numbered page manifest before page generation. Confirm that it contains exactly the requested number of finished pages.
15. Use the blank Master Interior Shell only as an internal consistency source. Do not deliver or count it as a completed planner page unless the user specifically requests it.
16. After shell approval, complete every manifest entry using the locked system. Perform one quality-control pass, correct only failing entries, preserve passing pages, and stop when the manifest passes.
17. Deliver each finished page as a separate full-canvas image or page file with unique, useful page-specific content.
18. Do not count a cover, blank shell, navigation-only page, empty writing sheet, decorative background, mockup, duplicate, or multi-page collage toward the requested functional page count unless the user explicitly defines a different count scope.
19. Apply the **Canvas Equals Planner Page** rule to the shell and every finished page: the cream or white worksheet must fill the entire canvas edge to edge, with no exterior layer visible.
20. Reject any page that shows surrounding plaid, black margins, backing, a mat, outer frame area, rounded corners revealing another layer, floating paper, or an exterior drop shadow. Read `references/canvas-equals-planner-page-protocol.md` before shell or page generation.

## Default design preferences

Use the user's requested theme first. When the user supplies no style details, use:

- Soft feminine digital-boutique style
- Pastel pink, cream, soft green, baby blue, lavender, and pale yellow
- Bows, gingham, polka dots, scallops, stitched details, florals, butterflies, or other coordinated accents
- Spacious writing areas
- Clean hierarchy
- Premium, sellable finish
- No overcrowding
- Portrait orientation
- Default page size: 567 × 726 px
- GoodNotes-, Notability-, iPad-, and Canva-friendly visual layout
- Tabs positioned fully inside the page boundary
- Full-bleed cream or white page base with zero visible exterior background

The user can override any default.

## Required project inputs

Determine or obtain:

- Planner name
- Theme or reference images
- Exact width and height in pixels
- Orientation
- Dated or undated
- Start month and year when dated
- Number of pages
- Whether the requested count includes or excludes covers and auxiliary pages; exclude them by default
- Requested page types
- Tab labels
- Tab location: right, left, top, bottom, or mixed
- Cover wording
- Binding style: none, rings, discs, notebook spine, stitched spine, or folder
- Commercial, personal, or PLR use
- Whether the user wants listing images, mockups, a PDF, or a hyperlink map

Do not repeatedly ask for information the user already supplied. When nonessential details are missing, choose sensible defaults and state them briefly.

## Workflow

### Phase 1 — Project brief

Create a concise project brief containing:

- Product name
- Dimensions
- Orientation
- Theme
- Palette
- Font direction
- Tab labels in exact order
- Total page plan
- Cover plan
- Interior plan
- Output list

Preserve every spelling choice exactly as approved.

### Phase 1A — Complete Page-Set Manifest

Before generating the cover, shell, or finished pages:

1. Obtain the exact number of finished functional pages. Do not ask again when the user already supplied it.
2. Clarify count scope only when ambiguous. By default, count functional planner pages and treat covers, shells, mockups, licenses, and listing images as auxiliary deliverables.
3. Create a numbered manifest with exactly one row per finished page.
4. Give every row a unique page title, purpose, filename, functional content specification, active tab, and status.
5. Count the rows and explicitly confirm `Manifest count: [N] of [N] requested pages`.
6. Resolve missing, duplicate, decorative-only, or nonfunctional entries before generation begins.

Read `references/complete-page-set-protocol.md` when planning, producing, tracking, or exporting a multi-page planner. Use `assets/planner-project-manifest-template.md` for the manifest and completion tracker.

### Phase 2 — Master style system

Define and lock:

- Six-color palette with HEX values
- Heading font direction
- Body font direction
- Accent font direction
- Internal divider-line style; no exterior frame or mat
- Full-canvas cream or white page treatment
- Decorative asset family
- Icon style
- Writing-line style
- Corner shape
- Shadow and depth rules
- Binding or spine treatment
- Safe writing margins

Use the same master style system throughout the planner.

### Phase 3 — Cover creation

Generate the planner cover with ChatGPT Images 2.0 at the exact requested size.

Cover requirements:

- Original artwork
- Correct title spelling
- Coordinated with the interior
- Clear focal point
- Readable title
- No cropped text
- No accidental extra words
- No overcrowding
- Suitable for a digital product listing
- Do not place interior tabs on the closed cover unless the user requests visible tabs

When requested, create front cover, back cover, closed cover, open cover, and coordinating divider covers separately.

### Phase 4 — Tab Blueprint

Before generating interior pages, create a written Tab Blueprint using `assets/tab-blueprint-template.md`.

Lock the following:

- Exact number of tabs
- Exact labels
- Exact order
- Exact side or edge
- Exact top-to-bottom or left-to-right sequence
- Tab width and height
- Corner radius
- Gap between tabs
- Distance from page edge
- Fill color for each tab
- Active-tab color
- Inactive-tab color
- Border color and thickness
- Shadow direction and softness
- Label font, size, case, and orientation
- Text alignment
- Icon use or no-icon rule

Assign every tab a stable ID such as TAB-01, TAB-02, and TAB-03. IDs and labels must never be reordered.

### Phase 5 — Master Interior Shell

Generate one blank but fully styled interior base page using ChatGPT Images 2.0.

The Master Interior Shell must contain:

- Cream or white page color from x=0, y=0 through the final right and bottom edges
- No exterior background, backing board, frame area, mat, surface, mockup, or drop shadow
- Final binding or spine area
- Final tab rail
- All tabs in the approved order
- Final tab colors
- Final tab typography
- Final margins
- A blank central content-safe area
- No page-specific planner content yet
- Top navigation within 7% of canvas height and right tabs within 6% of canvas width
- A single flat composition: the full-canvas page base remains underneath all tabs and navigation; no tab may sit on an exposed backing layer

Save and treat this image as the immutable master reference.

Name it:

`00-master-interior-shell-[WIDTH]x[HEIGHT]`

Do not proceed to full-page production until the shell is visually correct.

The shell is an internal production asset, not a finished planner page. Never present the shell as the completed planner, include it in the requested page count, or substitute it for any manifest entry unless the user specifically requests the blank shell as an extra file.

### Phase 6 — Tab Lock Snapshot

Create a close inspection record of the approved shell:

- Count every tab
- Record every tab label
- Record the order
- Record edge placement
- Record approximate pixel position or percentage coordinates
- Record tab colors
- Record tab dimensions
- Record label orientation
- Record the content-safe zone

Use `assets/planner-project-manifest-template.md` to preserve these details.

### Phase 7 — Page production by image editing

After the shell is approved, automatically generate every manifest page. For every finished page:

1. Start from the approved Master Interior Shell as the image reference.
2. Use image editing, not a fresh text-to-image recreation of the whole page.
3. Instruct ChatGPT Images 2.0 to preserve all pixels outside the central content-safe zone.
4. Add or replace content only inside the safe zone.
5. Keep all tabs visible and fully inside the page.
6. Highlight only the correct active tab when the design uses active-tab highlighting.
7. Preserve the exact page dimensions.
8. Generate the actual page image.
9. Run the Tab Lock Quality Check before accepting it.
10. Verify the page title, purpose, and functional components against its manifest row.
11. Save it as a separate full-canvas file.
12. Update the tracker as `Page [X] of [N]: completed` only after it passes QA.

Generate manageable batches when necessary. After checking a batch, continue with the next incomplete manifest row until `Page [N] of [N]: completed`. A batch boundary is not a stopping point.

Use this page-edit instruction pattern:

> Edit the approved Master Interior Shell. Preserve the full-canvas cream or white page base, binding area, tab rail, every tab, every tab label, tab order, dimensions, colors, spacing, font, internal dividers, and position exactly. The page base remains underneath the tabs and navigation to every canvas edge. Do not redraw, move, resize, recolor, rename, add, remove, or restyle any tab. Change only the central content-safe area to create the requested [PAGE TYPE] page. Keep the final image exactly [WIDTH] × [HEIGHT] px.

Append this exact sentence to every shell and page-generation prompt:

> Single flat full-canvas digital-planner export. Start with a cream or white page base covering every pixel and keep it underneath all tabs and navigation. The worksheet is the canvas itself: no exterior background, surrounding pattern, backing surface, frame area, mat, mockup, floating paper, outer drop shadow, black bar, rounded corner revealing another layer, or visible space outside the functional page.

### Phase 8 — Interior page standards

Each interior page must:

- Have a unique page title and purpose
- Fill the complete canvas rather than appearing on a decorative background or mockup
- Keep the white or cream base behind every tab and navigation element so no decorative perimeter layer can appear
- Contain complete functional worksheet content appropriate to its purpose
- Be ready to use without requiring the customer to design or finish it
- Include appropriate tables, writing lines, calendars, trackers, checklists, grids, or prompts
- Have enough space for handwriting
- Use clear sections
- Maintain safe margins
- Use readable labels
- Avoid tiny text
- Avoid decorative elements covering writing areas
- Match the master palette and fonts
- Keep recurring headers and footers consistent
- Use correct spelling
- Avoid duplicate, missing, or malformed sections
- Remain uncluttered

When making calendar pages:

- Verify weekday order
- Verify the correct number of days
- Verify the correct day/date placement for the requested month and year
- Do not invent dates
- Use a calendar calculation when needed before generating the image
- Inspect the rendered page for date errors

### Phase 9 — Page sequence

Unless the user supplies a sequence, use this default:

1. Planner dashboard
2. How to use
3. Year at a glance
4. Annual goals
5. Goal breakdown
6. Vision board prompts
7. Important dates
8. Quarterly goals
9. Monthly dashboard
10. Monthly calendar
11. Monthly goals
12. Monthly budget
13. Weekly planner
14. Daily planner
15. Habit tracker
16. Self-care tracker
17. Mood tracker
18. Savings tracker
19. Expense tracker
20. Content planner
21. Meal planner
22. Grocery list
23. To-do list
24. Project planner
25. Password tracker
26. Gratitude prompts
27. Monthly reflection
28. Annual reflection

Modify the sequence and count to match the user's requested product. A cover may be created as an auxiliary deliverable but is excluded from this default functional page count.

### Phase 10 — Tab Lock Quality Check

Compare every page against the Master Interior Shell.

Reject and regenerate any page when one or more of these occurs:

- Tab count changed
- A tab disappeared
- An extra tab appeared
- A label changed
- Spelling changed
- Order changed
- Tabs shifted
- Tab dimensions changed
- Tab color changed
- Font changed
- Text orientation changed
- Gap spacing changed
- Border or shadow changed
- Tabs were cropped
- Tabs moved outside the page
- Binding area changed
- Page dimensions changed
- Full-canvas base or approved internal dividers drifted
- Any dark, plaid, black, or other exterior area surrounds the cream worksheet
- The worksheet appears smaller than the canvas or floats above another layer
- Rounded outer corners reveal a background or a drop shadow separates the page from the canvas
- The cream page fails to reach the left or bottom edge
- Right tabs exceed 6% of canvas width or top navigation exceeds 7% of canvas height
- Any edge pixel belongs to a backing surface instead of the functional page base or an approved tab drawn over that base

A page is not complete until it passes every check.

If a page fails twice, return to the approved Master Interior Shell and generate that page again individually. Never use the failed page as the new reference.

### Phase 11 — Page naming

Name final files in sequence:

- `00-cover`
- `01-belongs-to`
- `02-how-to-use`
- `03-index`
- `04-year-at-a-glance`
- `05-goals`
- Continue with two-digit numbering

Include dimensions in filenames when helpful:

`05-goals-567x726.png`

### Phase 12 — Hyperlink map

When the planner will be hyperlinked, produce a separate map that lists:

- Tab ID
- Visible label
- Destination page
- Destination filename
- Pages where the tab appears
- Active-tab state
- Notes for Canva or PDF linking

Do not state that the flat PNG pages are already clickable.

### Phase 13 — Product completion

When requested, create:

- All individual PNG planner pages
- Front and back cover
- Coordinating divider pages
- Transparent decorative assets
- Hyperlink map
- Final PDF assembled in correct order
- Five product-listing images
- Tablet and phone mockups
- Product title
- Product description
- Customer instructions
- PLR license page

Use exact user-requested dimensions for listing images and mockups. Keep mockups uncluttered and keep tabs inside the tablet screen.

Before any PDF export:

1. Count the final separate page files and confirm the exact requested number exists.
2. Match every file to one manifest row and confirm no row is missing.
3. Confirm every page is full-sized, full-canvas, unique, functional, and page-specific.
4. Exclude the blank shell unless the user requested it as an extra.
5. Confirm the tabs, navigation, dimensions, margins, and theme remain locked.
6. Verify headings, prompts, tables, trackers, calendars, and labels for accuracy.
7. Assemble the high-resolution PDF only after all individual pages pass QA.
8. Keep every separate page file available alongside the PDF.

## Batch-generation rules

- ChatGPT Images 2.0 may create multiple images, but consistency takes priority over speed.
- Use the approved Master Interior Shell as the reference for every page in a batch.
- Do not generate unrelated page layouts in the same image.
- Each final planner page must be a separate full-size image.
- After each batch, inspect every page individually.
- Regenerate only failed pages.
- Never approve a contact sheet as the final planner pages.
- Continue across batches until the tracker reaches the exact requested total.

## Reference-image rules

When the user uploads references:

- Identify theme, palette, motifs, layout traits, and typography direction.
- Preserve a user's own character or brand asset when they explicitly require it and provide a usable reference.
- Do not alter a supplied character's face, skin tone, hairstyle, or defining features when the user says to keep the character exact.
- Do not copy another seller's complete planner or exact artwork.
- Create an original coordinated planner.
- Assign explicit roles to conflicting references. A theme reference controls palette, motifs, stitched-tab styling, and typography only; ignore its page-within-a-background composition.
- Let a full-page layout reference always control page coverage, tab placement, proportions, and edge-to-edge worksheet composition when references conflict.

## Failure prevention

Do not:

- Create a new tab design for each page
- Approximate the tab labels from memory
- Change singular labels to plural labels
- Rotate labels differently between pages
- Move the active tab rail
- Add random icons
- Replace the selected palette
- Add rings or a binding the user did not request
- Put tabs beyond the canvas
- Make listing mockups before the actual planner pages are complete
- Promise a hyperlink that has not been added
- Mark a page complete without inspecting it
- Deliver the Master Interior Shell as the planner
- Stop after generating one generic interior or one batch
- Count blank, navigation-only, decorative-only, duplicate, mockup, or collage outputs as finished pages
- Export a PDF before all separate manifest pages are complete
- Use plaid as a visible exterior background or place a smaller worksheet on top of any backing layer

## Final handoff format

Provide:

1. Project summary
2. Final dimensions
3. Tab Blueprint
4. Ordered page inventory
5. Individual full-canvas page images matching the exact manifest count
6. List of any regenerated pages
7. Tab Lock Quality Check result
8. Hyperlink map when requested
9. PDF and listing assets when requested

State clearly whether the output includes visual tabs only or completed clickable hyperlinks. Report the final tracker as `Page [N] of [N]: completed` and state whether the shell was excluded or separately requested.

## Changelog

### 2.2.1

- Added the image-generation efficiency protocol, targeted correction, one-pass quality control, controlled completion, and explicit planner-canvas safeguards.

### 2.2.0

- Define the planner as a single flat composition with the page base underneath tabs and navigation.
- Remove ambiguous page-frame/background preservation language that could create a smaller sheet on a themed surface.
- Add an edge-pixel rejection test for exposed backing layers.

### 2.1.0

- Add the strict Canvas Equals Planner Page rule and mandatory full-bleed prompt sentence.
- Limit the right tab strip to 6% and top navigation strip to 7% of the canvas.
- Reject surrounding plaid, margins, backing layers, revealed corners, mockups, and page drop shadows.
- Give full-page layout references priority over theme-reference composition.

### 2.0.0

- Define planner interior as the full finished page collection.
- Require an exact numbered page manifest and count confirmation before generation.
- Require page-set completion after shell approval with page-by-page tracking, one quality-control pass, targeted correction of failures, and a firm stop after the manifest passes.
- Prohibit blank shells, navigation-only pages, mockups, duplicates, decorative backgrounds, and collages from counting as finished pages.
- Require exact-count verification before PDF export while retaining all separate page files.

## Activation examples

Use this skill for prompts such as:

- "Create a 28-page digital planner with tabs that stay the same."
- "Make a GoodNotes planner cover and interior using ChatGPT Images 2.0."
- "Create all planner pages in 567 × 726 px and lock the monthly tabs."
- "Use this theme to make a PLR planner with identical tabs on every page."
- "Generate a planner page collection for Canva without changing the tab design."
- "Create exactly 28 separate functional planner pages and continue until Page 28 of 28 is complete."


## Image-Generation Usage Efficiency Protocol

Apply this protocol whenever this skill creates, edits, regenerates, enhances, or reviews generated images.

### Minimum-generation rule

- Use the fewest image-generation calls necessary to complete the request correctly.
- Generate exactly the number of images requested or explicitly required by this skill's current deliverable.
- Do not automatically create alternate versions, bonuses, extra colorways, tests, mockups, transparent assets, listing images, or decorative extras unless the user requests them or they are an explicit required output.
- Do not use a tool's maximum image allowance merely because it is available.

### Validation-before-batch rule

- When a coordinated visual system has not been approved, create one representative validation image before a multi-image batch.
- Validate dimensions and aspect ratio, canvas coverage, composition, background treatment, typography placement, character appearance, palette, borders, tabs, panels, margins, decorative density, and functional areas.
- Do not generate a large batch from an unverified composition.
- If the user explicitly requests the entire batch immediately, proceed without requesting another approval message; internally validate the composition before starting the batch.

### Approved-design locking rule

After approval, lock the canvas dimensions, grid, layout, background, margins, heading placement, typography hierarchy, character identity, skin tone, facial features, hairstyle, clothing, illustration style, planner tabs, border thickness, palette, decorative style, spacing, and product-cover proportions. Change only content that must differ. Do not redesign each image independently.

### Targeted-correction rule

- Modify only the affected image and specified elements.
- Preserve everything that already passes.
- Do not regenerate a complete batch because one image fails.
- Prefer a targeted edit over restarting a nearly correct image.
- Correct only the title for a misspelling, only the tab for a moved tab, only the canvas composition for an exposed planner background, and only the changed character for identity drift.

### One-quality-control-pass rule

Perform one structured quality-control pass against explicit requirements. Correct only clear failures. Do not repeatedly regenerate acceptable images for subjective perfection. Stop generating after all explicit checks pass.

### Full-canvas composition rule

For planner pages, worksheets, printables, invitations, covers, activity pages, workbook pages, and similar full-page designs:

- Treat the design canvas and functional page as the same object.
- Start the intended page background at x=0 and y=0 and extend it to the final right and bottom edges.
- Fill the complete requested canvas.
- Never place a smaller page over an exterior background.
- Do not show a desktop, room, table, fabric, plaid surface, backing board, mat, frame, device, paper stack, or mockup unless explicitly requested.
- Do not add unrequested outer margins or borders.
- Use decorative patterns only inside intentional design areas permitted by the user.

### Transparent-asset rule

When transparency is requested, use a genuinely transparent background—not white, cream, gray, colored, or checkered. Keep the complete asset visible, do not crop important parts, and add no shadow or outline unless requested.

### Reference-image role rule

- Assign each reference a role before generating: composition, character, color, theme, typography, product-preservation, or sequence/animation.
- Use each reference only for its assigned purpose; do not copy unrelated content from a composition reference.
- Preserve any referenced character, product cover, logo, planner layout, or illustration that the user requires to remain exact.

### Text-accuracy rule

- Use only user-supplied or explicitly required text. Do not invent names, dates, prices, addresses, schedules, appointments, product details, labels, or sample entries.
- Proofread visible text before finalizing.
- Prevent misspellings, clipping, warping, duplicate headings, unreadable lettering, overlaps, placeholder text, random symbols, and unrequested handwritten entries.
- Keep blank templates free of sample writing, appointments, stickers, checklist entries, and example content unless requested.

### Batch-consistency rule

Establish one master visual system for coordinated sets. Keep dimensions, orientation, background, margins, headers, footers, font hierarchy, tabs, borders, line weight, character design, illustration style, decorative density, palette, spacing, and functional layout consistent. Change only the required title, content, date, month, activity, or functional fields.

### Processing-efficiency rule

Do not use image generation for text-only work such as descriptions, page lists, section planning, filenames, prompts, instructions, content organization, marketing copy, proofreading before layout, or assembly explanations. Do not inspect unrelated applications, repositories, files, tools, or connected services.

### Controlled-completion rule

Stop after the requested image count is complete, dimensions are correct, the approved system is preserved, one quality-control pass is complete, clear failures are corrected, and requested files are delivered. Do not automatically begin PDF assembly, hyperlinking, Canva setup, animation, listing creation, marketing copy, or social promotion unless requested or explicitly required by this skill's current function.

## Canvas Equals Planner Page

The complete requested image canvas is the planner page. The planner page must fill the entire canvas from edge to edge. Never display the planner page as a smaller cream or white sheet placed over another background. Never generate an exterior background behind or around the planner page. Tabs must be integrated into the full-canvas planner composition and remain consistent across all applicable pages.

- Reuse one approved tab system.
- Do not allow tab positions to shift randomly.
- Keep page margins consistent and the worksheet area functional.
- Keep decorative elements out of writing areas.
- Keep covers and interior pages as separate outputs unless the user requests otherwise.
