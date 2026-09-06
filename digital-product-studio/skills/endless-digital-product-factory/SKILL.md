---
name: endless-digital-product-factory
description: Create any lawful, original digital product the user requests, including custom, uncommon, hybrid, or newly invented product types, plus expandable product families and repeatable workflows. Use ChatGPT Image Generation for all original visual creation required by the deliverable. The product examples in this skill are illustrative rather than restrictive. Continue from a product ledger to generate new products without duplicating prior concepts. Do not use for brainstorming-only requests when the user explicitly wants ideas without finished deliverables.
---

# Endless Digital Product Factory

Turn any user-requested digital product idea into complete deliverables, coordinated product families, and future expansion opportunities. The requested product may be common, uncommon, custom, hybrid, niche-specific, or newly invented. Create the actual deliverables—not merely a list of ideas.

## Core promise

Build a repeatable digital-product ecosystem that can continue over time without repeating previous products. “Endless” means the workflow preserves a product ledger and can always produce the next distinct product. It does not mean generating an uncontrolled number of files in one run. Create the exact number requested and continue in later runs when asked.

## Mandatory ChatGPT Image Requirement

This skill must use **ChatGPT Image Generation** whenever the requested deliverable includes original visual creation. This is a non-optional rule.

1. Use ChatGPT Image Generation for covers, planner pages, workbook pages, KDP interiors, listing images, illustrations, mockups, invitation sections, templates, printables, transparent assets, and every other original visual asset the product requires.
2. Do not substitute outside image generators, third-party AI image tools, stock-placeholder visuals, or text-only descriptions when the skill is expected to create the visuals themselves.
3. If the deliverable contains both visual and non-visual components, create the visual components with ChatGPT Image Generation and create the non-visual components with the appropriate available tools.
4. When the user supplies reference images, use them to guide the ChatGPT image-generation outputs while still creating original, transformed deliverables that follow the request.
5. Never claim a visual deliverable is complete if the required ChatGPT-generated images were not actually created.
6. If a product type genuinely does not need images, complete the request with the needed non-image tools, but the moment original visual assets are required, ChatGPT Image Generation must be used.


## Universal Product Request Rule

This is an open-category digital-product creator, not a fixed product catalog.

1. Create any lawful digital product the user requests, even when its product type is not named anywhere in this skill.
2. Treat every product-type list and example as illustrative, never exhaustive.
3. The user's requested product type takes priority over default examples, suggested categories, and the expansion matrix.
4. Do not refuse, redirect, or substitute a different product merely because the request is unusual, highly specific, custom, hybrid, or newly invented.
5. When the user names an unfamiliar product type, infer its intended purpose and required components from the request, supplied references, audience, selling platform, and expected customer experience.
6. When the product combines several formats, create the complete hybrid product and organize each component clearly.
7. When no established template exists, design a sensible custom structure, create a manifest, and produce the finished deliverables.
8. Support products made from text, images, printable pages, interactive or hyperlinked documents, templates, audio-ready scripts, video-ready assets, databases, spreadsheets, presentations, editable documents, design assets, instructional materials, and packaged combinations of these formats when the needed tools are available. When original images or graphics are required, those visuals must be created with ChatGPT Image Generation.
9. Never claim a file format, interactive feature, editability, automation, or functionality that was not actually created and verified.
10. Only limit a request when required by safety, law, intellectual-property rules, platform restrictions, or actual tool capability. In those cases, complete every safe and feasible portion of the product rather than replacing the user's idea with a generic one.

## Activation

Use this skill when the user asks to:

- Create one or more digital products.
- Turn one idea into many coordinated products.
- Build a digital-product collection, bundle, shop inventory, product ecosystem, or product workflow.
- Continue creating new products without repeating prior concepts.
- Produce any requested digital product. Examples include planners, workbooks, ebooks, guides, journals, trackers, checklists, templates, printables, KDP interiors, children’s activities, coloring books, lead magnets, brand kits, social-media kits, interactive documents, digital downloads, custom toolkits, and hybrid products, but the skill is not limited to these examples.
- Create the product plus listing copy, listing images, mockups, delivery files, and promotional materials.

When another installed skill is more specialized for a requested deliverable, use that specialized skill first for its portion of the work while this skill remains the master workflow and quality controller.

## Non-negotiable behavior

1. Create the actual product, not only ideas, prompts, outlines, or instructions.
2. Use ChatGPT Image Generation for every original visual deliverable required by the request, including covers, pages, illustrations, listing graphics, mockups, visual templates, and other artwork. This is mandatory whenever the product includes visuals.
3. Generate the exact requested number of products, pages, assets, and listing images. Do not add unrequested bonus generations.
4. Preserve approved designs and make targeted corrections instead of restarting entire projects.
5. Never copy another seller’s wording, layout, artwork, character, branding, or protected product. References guide direction only.
6. Keep outputs polished, usable, organized, readable, and commercially presentable.
7. Do not stop after the first page, image, product, or batch when the manifest requires more.
8. Do not claim a file was created unless it was actually created and verified.
9. When information is missing, use reasonable defaults and proceed unless the missing detail would make the product unusable.
10. Maintain consistency across every page and asset in the same product line.
11. Never treat the product-type examples in this skill as a closed or complete list.
12. Create the exact product the user requests instead of forcing it into the nearest listed category.

## Default modes

Infer the most suitable mode from the request.

### Single Product Mode
Create one complete product with all required pages, files, packaging, and sales materials.

### Product Family Mode
Turn one main idea into a coordinated family of complementary products, such as a planner, workbook, challenge, journal, tracker, mini guide, card set, checklist bundle, and lead magnet.

### Collection Mode
Create multiple distinct products for the same niche or shop collection. Each product must solve a different problem, serve a different use case, or use a meaningfully different format.

### Continue the Factory Mode
Read the existing product ledger, find unused combinations, and create the next requested product or batch without duplicating previous concepts.

### Product Ecosystem Mode
Create a value ladder containing a free lead magnet, entry product, core product, premium bundle, and logical upsells or cross-sells.

## Required input model

Use any details the user provides:

- Niche
- Target audience
- Main problem or desired outcome
- Product type or allowed product types; accept any custom product name or description
- Number of products
- Page count
- Dimensions and orientation
- Dated or undated format
- Style, colors, fonts, theme, and references
- File formats
- Personal-use, commercial-use, or PLR rights
- Selling platform
- Listing-image count and dimensions

Do not repeatedly ask for information already provided. If no exact size is supplied, select a practical industry-standard size for that product and clearly record it in the manifest.

## Product ledger system

Use `PRODUCT_LEDGER.csv` as the source of truth for completed and planned products.

1. Search the current project or workspace for an existing ledger.
2. If none exists, create one from `assets/product-ledger-template.csv`.
3. Assign each product a unique Product ID.
4. Create a product fingerprint using:
   - Niche
   - Audience
   - Problem
   - Product type
   - Core outcome
   - Style
   - Season or occasion
   - Difficulty level
5. Before approving a new concept, compare the fingerprint against prior rows.
6. Reject exact duplicates and near-duplicates that only change colors or titles.
7. A related product is allowed when it has a distinct purpose, format, audience segment, or customer outcome.
8. Update the ledger only after the deliverable is complete or clearly mark its status as Planned, In Progress, Needs Review, or Complete.

## Endless Product Expansion Matrix

Generate concepts by combining distinct values from:

**Niche × Audience × Problem × Outcome × Product Type × Style × Season/Occasion × Difficulty × Delivery Format × License**

Use `references/product-expansion-matrix.md` for detailed options.

A new concept must differ meaningfully in at least two strategic dimensions unless it is an intentional companion product.

## Complete workflow

### Phase 1: Interpret and define the job

1. Determine the mode.
2. Read all supplied files, references, prior approvals, and existing product records.
3. State the exact deliverables internally as a manifest.
4. Resolve missing noncritical details using sensible defaults.
5. Identify any specialized installed skills that should be used for portions of the task.

### Phase 2: Create the opportunity set

1. Identify the audience’s specific problem, desired transformation, and use context.
2. Generate multiple possible concepts internally.
3. Compare them against the ledger.
4. Remove duplicates, weak variations, and concepts that lack a clear customer benefit.
5. Select the strongest concept or the exact number requested.
6. Define how each selected product differs from the others.

### Phase 3: Create the product specification

If the requested product type is not represented by an existing template or example, define its structure from first principles based on what the customer must receive and be able to do. Do not replace it with a more familiar product type.

For every selected product, define:

- Product ID
- Working title
- Target customer
- Problem solved
- Core promise
- Product type
- Dimensions
- Page or asset count
- File formats
- Page manifest or content manifest
- Visual system
- Required editable or printable versions
- License type
- Delivery-folder structure
- Listing-image count
- Quality checks

### Phase 4: Lock the design system

Before creating a multi-page or multi-asset product, lock:

- Canvas size and orientation
- Background treatment
- Margin and safe-area rules
- Typography hierarchy
- Color palette
- Illustration style
- Decorative elements
- Navigation or tab system
- Character appearance, when applicable
- Repeating headers, footers, page numbers, and branding

Do not alter the locked shell from page to page unless the manifest specifically requires a variation.

### Phase 5: Generate the complete product

Follow the product manifest until every required item is complete.

#### Separate-Page Image Generation Rule

For planners, workbooks, busy books, activity books, coloring books, journals, children’s books, KDP interiors, invitation sections, and every other multi-page visual project:

- One requested page equals one individual image-generation output.
- Generate every page separately.
- Never place several finished pages in one image, collage, contact sheet, grid, preview board, or multi-page mockup.
- Use batches of up to 10 separate images when the image tool supports it and the manifest requires that many.
- Generate the exact number required; do not use the maximum allowance merely to create extras.
- Continue through numbered batches until the complete manifest is finished.
- Clearly identify the page represented by every generated image.

#### Canvas Equals Planner Page Rule

For functional planner, worksheet, journal, workbook, and printable pages:

- The image canvas and functional page must be the same object.
- Begin with a full-canvas base extending from x=0, y=0 to the final right and bottom edges.
- Do not place a smaller sheet on top of a visible background.
- Do not show exterior mats, desk scenes, plaid backdrops, frames, shadows, black bars, or side margins unless the user explicitly requests a mockup.
- Tabs and navigation must remain inside the page canvas.
- The full canvas must be usable as the final page.

#### Cover and interior separation

- Create covers and interior pages as separate files unless the user specifically requests a combined preview.
- A cover does not count as an interior page unless the user says it does.
- A locked-shell preview does not count toward the required page total.

#### Character consistency lock

When characters appear:

- Lock face shape, skin tone, hair, facial features, body proportions, clothing, accessories, and illustration style.
- Do not alter an approved character between pages.
- Use the character only where the manifest calls for it; do not place the character on every page by default.

#### Reference-image roles

Assign each reference a role before generation:

- Composition reference
- Style reference
- Color reference
- Character reference
- Typography reference
- Product mockup reference

Never merge conflicting reference roles without resolving which one controls each feature.

#### Text accuracy

- Spell every title, heading, label, month, date, number, and callout correctly.
- Avoid random filler text.
- Keep functional fields usable and aligned.
- Review text once before accepting a batch.

### Phase 6: Assemble and export

Create the requested final formats, which may include:

- Print-ready PDF
- Hyperlinked PDF
- Individual PNG or JPG pages
- Transparent PNG assets
- Editable source or template instructions
- DOCX or PPTX when appropriate
- ZIP delivery package
- Customer instruction guide
- License file
- Product ledger

Use `references/output-packaging.md` for folder naming and verification.

### Phase 7: Create sales materials

Unless the user excludes sales materials, create the requested combination of:

- Search-friendly product title
- Product description
- Features and benefits
- What-is-included section
- Customer instructions
- FAQ
- Suggested price range
- Five to ten listing-image concepts or finished listing images, according to the request
- Product mockups
- Social captions
- Short-form promotional script
- Pinterest title and description
- Lead magnet connection
- Upsell, cross-sell, and bundle ideas

Do not misrepresent what is included. Do not call files editable, hyperlinked, commercial-use, or PLR unless those features are actually present.

### Phase 8: Quality control

Run one structured quality pass using `references/quality-control-checklist.md`.

- Compare outputs against the manifest.
- Verify exact counts and dimensions.
- Check consistency, text, clipping, blank areas, and usability.
- Verify the full-canvas rule where applicable.
- Verify separate pages were produced separately.
- Confirm required files open successfully.
- Confirm the ZIP contains the promised files.
- Correct only failed items; preserve approved work.
- Do not enter an endless regeneration loop.

### Phase 9: Update the factory

After completion:

1. Add or update the product in `PRODUCT_LEDGER.csv`.
2. Mark exact deliverables and file paths.
3. Record its fingerprint.
4. Record companion products already created.
5. Generate a short list of unused expansion directions for future continuation, but do not create them unless requested.

## Product-family logic

A strong family should contain products with different jobs, not repeated covers on the same interior.

Example family:

- Core planner: ongoing organization
- Workbook: guided transformation
- Challenge: short implementation period
- Tracker: repeated measurement
- Journal: reflection
- Mini guide: instruction
- Card set: quick-use prompts
- Checklist bundle: fast action
- Lead magnet: small win
- Premium bundle: coordinated collection

## Usage-efficiency protocol

1. Plan before generating.
2. Validate the manifest and locked design before the first batch.
3. Use the fewest generation calls that still produce every required separate output.
4. Generate exact requested counts.
5. Preserve approved pages and assets.
6. Apply targeted corrections to failed items only.
7. Perform one consolidated quality-control pass.
8. Stop when every manifest item passes.

## Completion standard

A project is complete only when the exact user-requested product—not merely a nearby substitute—has been created and:

- Every manifest item exists.
- Every requested page or image is separate.
- Counts and dimensions match.
- The product is usable, not merely conceptual.
- Final files are packaged and verified.
- Sales claims match the files.
- The ledger has been updated.
- No unfinished placeholder is presented as complete.

## Final response behavior

Report:

1. Product or collection created
2. Number of products, pages, and assets completed
3. Final formats
4. Included sales materials
5. Ledger status
6. Direct links to every final downloadable file

Do not overwhelm the user with internal reasoning or low-level generation details.

## Mandatory Image Generation for Visual Deliverables

Whenever this skill creates or updates a customer-facing visual, use ChatGPT's built-in image-generation tool for every finished visual. This rule applies to covers, interiors, planner pages, worksheets, printables, illustrations, graphics, listing images, mockups, ads, product scenes, thumbnails, storyboards, video keyframes, and any other visible asset promised by the skill or requested by the user.

- Treat one requested finished page or asset as one separate image-generation call and one separate delivered file. Never combine several requested finished pages into a collage, contact sheet, grid, or single image.
- Do not replace required image generation with programmatic SVG, HTML/CSS, Python or Node drawing, shape-built document layouts, vector-only construction, blank templates, or placeholder previews.
- Use code and deterministic tools only after image generation for tasks such as resizing, cropping, background removal, text correction, PDF assembly, hyperlinking, file packaging, and quality checks. These tools must not create the finished visual instead of image generation.
- Use every user-supplied reference image that applies, preserve approved identity and style details, and inspect generated outputs before delivery.
- Generate the complete requested set in numbered batches. Do not stop after a sample, cover, first page, or first batch.
- If built-in image generation is unavailable or fails, explain the blocker instead of silently switching to a code-built visual.
- For a genuinely text-only, audio-only, technical, review, packaging, or utility task with no requested visual deliverable, do not generate unrelated images. If the task includes even one customer-facing visual, this mandatory rule applies to that visual.

## Mandatory 567 × 726 Page Size

Whenever this skill creates a planner, e-book, workbook, journal, guide, activity book, coloring book, busy book, KDP-style page product, or any other page-based digital product, every finished page must be exactly **567 × 726 pixels in portrait orientation**.

- Use 567 × 726 px for the front cover, back cover, title page, dividers, interior pages, worksheets, bonus pages, and every other page in the product.
- Keep the entire product at one identical canvas size. Never mix page dimensions or aspect ratios within one product.
- Do not substitute US Letter, A4, square, landscape, print-trim, or automatically inferred dimensions for these page-based products.
- If a reference uses a different size or ratio, recompose it onto a full 567 × 726 px canvas without stretching, side bars, exterior mats, or visible background around a smaller page.
- The canvas must equal the functional page from edge to edge. Do not place a smaller worksheet or cover on top of another background.
- Preserve the 567 × 726 px page size during PDF assembly, hyperlinking, export, packaging, and later corrections. Do not add padding or resize individual pages.
- Verify every finished page's pixel dimensions before delivery. Correct only the affected page when a size check fails.
- This rule controls product pages only. Etsy listing images, promotional graphics, mockups, social posts, and videos may use their own requested marketing dimensions.
