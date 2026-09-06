---
name: create-coloring-book-collection
description: Create an original, cohesive coloring-book product from concept through print-ready interior, cover, preview images, and customer files. Use when the user asks for a coloring book, coloring-page collection, themed coloring bundle, or printable line-art product.
---

# Create Coloring Book Collection

## Purpose

Create an original, cohesive coloring-book product from concept through print-ready interior, cover, preview images, and customer files.

## Trigger

Use when the user asks for a coloring book, coloring-page collection, themed coloring bundle, or printable line-art product.

## Required outputs

- Approved theme, audience, trim size, page count, and difficulty level
- Original cover and coordinated interior title/copyright pages
- 30–50 consistent black-and-white coloring pages, or the user’s requested count
- Print-ready PDF plus individual high-resolution page files
- Listing previews, mockups, file manifest, and customer instructions

## Workflow

1. Define the audience, theme, visual rules, page count, trim size, bleed choice, and intended marketplace.
2. Create a short visual style sheet covering line weight, complexity, borders, recurring motifs, and prohibited elements.
3. Generate the cover and interior artwork with ChatGPT Image Generation 2.0. Do not stop at writing prompts.
4. Inspect every page for duplicate scenes, accidental gray fills, clipped lines, malformed hands, unreadable text, or inconsistent line weight.
5. Assemble the interior in a logical order and export the requested print and digital formats.
6. Create uncluttered listing previews that accurately represent the finished pages.

## Quality checks

- All interior art is original and suitable for coloring.
- Line art is crisp, black on white, and not overly detailed for the target age.
- No copyrighted characters, logos, artist imitation, watermarks, or fake endorsements.
- Page dimensions, margins, bleed, and resolution match the user’s request.

## Global production rules

1. Produce finished, usable product assets—not merely ideas, outlines, or image prompts.
2. For artwork, covers, decorative assets, illustrations, mockups, or visual product pages, use ChatGPT Image Generation 2.0 when image generation is available.
3. Do not replace requested image generation with code, SVG programming, placeholder boxes, stock-image search, or a list of prompts.
4. Preserve the user’s supplied theme, brand, dimensions, wording, and approved design choices. Use reasonable defaults only when a missing detail does not block safe completion.
5. Keep layouts polished, readable, and intentionally uncrowded.
6. Use original content. Do not copy copyrighted characters, brand logos, commercial templates, living artists’ signature styles, or another seller’s exact product.
7. Verify spelling, dates, answer keys, page counts, dimensions, file names, and promised contents before final delivery.
8. Clearly distinguish what was generated, what was verified, and what still needs physical testing, professional review, or platform-specific checking.
9. Organize final files into customer-ready folders and include a contents list or start-here guide when useful.
10. When the user supplies reference images, use them for direction and structure without recreating protected artwork exactly.

## Completion behavior

Complete as much of the product as the available tools allow in the current task. Provide the finished files or assets directly. Do not promise background work or claim that a file, link, test, upload, or editable template exists unless it was actually created or verified.


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


## Character Lock Requirement

For recurring or referenced characters, establish and preserve face shape, eye shape, nose, lips, skin tone, hairstyle, hair color, body proportions, age appearance, clothing details, and illustration style. Do not reinterpret or redesign an established character between images. Change expressions and poses only when requested while preserving identity.
