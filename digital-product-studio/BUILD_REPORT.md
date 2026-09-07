# Build report: Digital Product Studio by Sadé

Built 2026-09-04; updated 2026-09-07. Slug: `digital-product-studio`. Developer: Sadé. Version: 1.1.0.

## Locations

Distribution plugin: `digital-product-studio/`. Marketplace manifest: `.agents/plugins/marketplace.json`. Original ZIP archives are not included in this repository; their checksums remain recorded in `docs/source-archives.json`.

## Included skills

- digital-planner-tab-shape-selector
- create-consistent-tabbed-digital-planner
- hyperlink-digital-planner-pdf
- planner-quality-control
- create-etsy-product-automation
- create-product-listing
- etsy-listing-image-generator
- create-any-product-mockup
- e-book-generator
- editable-ebook-workbook-creator
- create-recipe-ebook
- childrens-kdp-book-creator
- create-coloring-book-collection
- kdp-interior-page-creator
- kdp-product-bundle-creator
- low-content-kdp-book-creator
- puzzle-activity-book-creator
- create-digital-paper-pack
- create-worksheet-level-variants
- teacher-resource-automation
- small-business-branding-kit-automation
- canva-social-media-template-pack-creator
- youtube-branding-kit-creator
- create-canva-interactive-birthday-invitation
- create-canva-interactive-invitation
- create-wedding-stationery-suite
- invitation-card-suite-creator
- endless-digital-product-factory
- seasonal-digital-product-bundle-creator
- digital-product-studio-orchestrator

## Existing skills preserved

All 25 supplied SKILL.md files are byte-for-byte unchanged, including frontmatter descriptions, production workflows, image-generation rules, QA, and activation examples. All 355 supplied files were retained in their original skill-relative locations. 330 source files remain byte-identical. All 218 images, templates, references, licenses, original skill manifests, and supporting documents were retained. All original executable modes were preserved.

## Modified files

The original archives and extracted source copies are unchanged. Only plugin copies received the following compatibility corrections:

- `skills/canva-social-media-template-pack-creator/agents/openai.yaml`: Removed unsupported policy.products; retained implicit invocation.
- `skills/childrens-kdp-book-creator/agents/openai.yaml`: Removed unsupported policy.products; retained implicit invocation. Added required interface.short_description.
- `skills/create-any-product-mockup/agents/openai.yaml`: Removed unsupported policy.products; retained implicit invocation.
- `skills/create-coloring-book-collection/agents/openai.yaml`: Removed unsupported policy.products; retained implicit invocation. Added required interface.short_description.
- `skills/create-consistent-tabbed-digital-planner/agents/openai.yaml`: Removed unsupported policy.products; retained implicit invocation.
- `skills/create-digital-paper-pack/agents/openai.yaml`: Removed unsupported policy.products; retained implicit invocation. Added required interface.short_description.
- `skills/create-etsy-product-automation/agents/openai.yaml`: Removed unsupported policy.products; retained implicit invocation.
- `skills/create-product-listing/agents/openai.yaml`: Removed unsupported policy.products; retained implicit invocation.
- `skills/create-recipe-ebook/agents/openai.yaml`: Removed unsupported policy.products; retained implicit invocation. Added required interface.short_description.
- `skills/create-worksheet-level-variants/agents/openai.yaml`: Removed unsupported policy.products; retained implicit invocation. Added required interface.short_description.
- `skills/e-book-generator/agents/openai.yaml`: Removed unsupported policy.products; retained implicit invocation.
- `skills/editable-ebook-workbook-creator/agents/openai.yaml`: Removed unsupported policy.products; retained implicit invocation.
- `skills/endless-digital-product-factory/agents/openai.yaml`: Removed unsupported policy.products; retained implicit invocation.
- `skills/etsy-listing-image-generator/agents/openai.yaml`: Removed unsupported policy.products; retained implicit invocation.
- `skills/hyperlink-digital-planner-pdf/agents/openai.yaml`: Removed unsupported policy.products; retained implicit invocation. Added required interface.short_description.
- `skills/kdp-interior-page-creator/agents/openai.yaml`: Removed unsupported policy.products; retained implicit invocation. Added required interface.short_description.
- `skills/kdp-product-bundle-creator/agents/openai.yaml`: Removed unsupported policy.products; retained implicit invocation. Added required interface.short_description.
- `skills/low-content-kdp-book-creator/agents/openai.yaml`: Removed unsupported policy.products; retained implicit invocation. Added required interface.short_description.
- `skills/planner-quality-control/agents/openai.yaml`: Removed unsupported policy.products; retained implicit invocation.
- `skills/puzzle-activity-book-creator/agents/openai.yaml`: Removed unsupported policy.products; retained implicit invocation. Added required interface.short_description.
- `skills/seasonal-digital-product-bundle-creator/agents/openai.yaml`: Removed unsupported policy.products; retained implicit invocation.
- `skills/small-business-branding-kit-automation/agents/openai.yaml`: Removed unsupported policy.products; retained implicit invocation.
- `skills/teacher-resource-automation/agents/openai.yaml`: Removed unsupported policy.products; retained implicit invocation.
- `skills/youtube-branding-kit-creator/agents/openai.yaml`: Removed unsupported policy.products; retained implicit invocation.
- `skills/hyperlink-digital-planner-pdf/scripts/hyperlink_planner_pdf.py`: Replaced nonexistent Page.delete_links() with iteration over Page.get_links() and supported Page.delete_link(); tested replacement without duplicate annotations or changed artwork.

No production skill was replaced, shortened, or merged. YAML serialization changed formatting alongside the stated metadata fixes. The hyperlink replacement repair is the only source code change.

## New skills

`digital-planner-tab-shape-selector` was added from the supplied ZIP. It selects and locks only the visual tab shape before planner image generation and hands the choice to the existing planner creator.

`digital-product-studio-orchestrator`, with agent metadata and a linked routing reference. It chooses an existing owner, tracks handoffs in that owner’s manifest, preserves inputs, and coordinates specialist QA and sales stages. It does not reproduce the production methodologies.

Version 1.1.0 adds the supplied `create-canva-interactive-birthday-invitation`, `create-canva-interactive-invitation`, `create-wedding-stationery-suite`, and `invitation-card-suite-creator` skills. The supplied `create-etsy-product-automation` bundle matched the existing skill instructions and updated only its agent product-availability metadata. SVG artwork was preserved while affected icon canvases were increased from 24×24 to 48×48 for directory compatibility.

## Overlap decisions

All overlaps represent specialization or orchestration; none justified consolidation. Etsy automation owns complete selling packages; listing copy, listing graphics, and mockups remain independent. The factory owns product expansion and ledger continuation; the coordinator supplies cross-skill handoffs. Recipe books and editable teaching/workbook pairs retain specialized entrypoints. Coloring takes pure coloring requests, children’s handles early learning/tracing, puzzles handles puzzle mechanics, low-content handles journals/logbooks, interiors handles inside-page scope, and KDP bundles owns product families. Branding assets feed social and channel templates without recreating approved identity. Teacher packs use worksheet differentiation only as needed.

The coordinator documents source conflicts: factory page-size rules versus specialist print requirements; undated all-in-one planner baselines versus requested dated/custom planners; five versus seven listing-image defaults; and functional-page counts versus covers and shells. Explicit user specifications remain authoritative. All original rules remain available in their source files.

## Validation

- All 25 archives passed ZIP integrity checks and extracted separately without collisions or path traversal.
- Exactly 29 supplied specialist skills plus the coordinator are present.
- All 30 skill frontmatters pass the official skill validator.
- The official plugin validator passes after agent metadata compatibility fixes.
- Hash comparison accounts for all 355 source files and all 25 intentional modified files.
- 218 images decode; JSON, YAML, SVG, Python syntax, icons, linked Markdown, and 49 explicitly referenced local paths validate.
- All 197 active mockup references and all listing-image index references resolve; excluded mockup entries remain inactive.
- A three-page PDF fixture verifies seven real annotations, normalized/pixel/point rectangles, dynamic destinations, link replacement, unchanged page dimensions, and pixel-identical before/after renders. Invalid maps and zero-link PDFs are rejected.
- All 18 conceptual routing scenarios are documented and reviewed; see docs/routing-tests.md.

## Issues and limits

- No full image-generation product run or live model-routing evaluation was performed. Fresh-task tests remain necessary.
- Original mockup manifest.txt lists REF-0213 and REF-0214 as historical excluded duplicates, but those files were not in the uploaded archive. Neither is referenced by the live index. Metadata claims three excluded duplicates; the live index has one excluded duplicate and one interface screenshot. This inherited archival discrepancy is documented rather than fabricated or silently rewritten.
- The source PDF inspector checks structural annotations but does not prove expected coverage or detect every conflicting overlap; source workflow and coordinator require map comparison and visual QA separately.
- Supplied reference libraries are private internal material. No public upload or customer-facing plugin ZIP was created. Redistribution rights must be resolved before sharing the complete plugin.
- Image generation and live Canva editing depend on session tools; PyMuPDF is a separate runtime dependency. No fake integration manifests were added.

## New plugin-level files

Listed below. Existing skill-level files remain within each skill.

- `.codex-plugin/plugin.json`
- `README.md`
- `INSTALL.md`
- `BUILD_REPORT.md`
- `docs/skill-catalog.json`
- `docs/source-archives.json`
- `docs/source-inventory.json`
- `docs/source-changes.json`
- `docs/routing-tests.md`
- `docs/validation.json`
- `scripts/validate_studio.py`
- `scripts/install_personal.py`

## Final folder tree

```text
digital-product-studio/
├── .codex-plugin/plugin.json
├── README.md
├── INSTALL.md
├── BUILD_REPORT.md
├── docs/
│   ├── skill-catalog.json
│   ├── source-archives.json
│   ├── source-inventory.json
│   ├── source-changes.json
│   ├── routing-tests.md
│   └── validation.json
├── scripts/
│   ├── install_personal.py
│   └── validate_studio.py
└── skills/
    ├── create-consistent-tabbed-digital-planner/
    ├── hyperlink-digital-planner-pdf/
    ├── planner-quality-control/
    ├── create-etsy-product-automation/
    ├── create-product-listing/
    ├── etsy-listing-image-generator/
    ├── create-any-product-mockup/
    ├── e-book-generator/
    ├── editable-ebook-workbook-creator/
    ├── create-recipe-ebook/
    ├── childrens-kdp-book-creator/
    ├── create-coloring-book-collection/
    ├── kdp-interior-page-creator/
    ├── kdp-product-bundle-creator/
    ├── low-content-kdp-book-creator/
    ├── puzzle-activity-book-creator/
    ├── create-digital-paper-pack/
    ├── create-worksheet-level-variants/
    ├── teacher-resource-automation/
    ├── small-business-branding-kit-automation/
    ├── canva-social-media-template-pack-creator/
    ├── youtube-branding-kit-creator/
    ├── endless-digital-product-factory/
    ├── seasonal-digital-product-bundle-creator/
    └── digital-product-studio-orchestrator/
```

Each original skill retains its complete original relative tree, enumerated file-by-file in `docs/source-inventory.json`. The coordinator contains SKILL.md, agents/openai.yaml, and references/routing.md.

## Installation and test prompts

Follow INSTALL.md for exact commands. All 18 conceptual prompts and expected routes are in docs/routing-tests.md; README.md also includes direct-use prompts for all 30 skills. Begin in a fresh Codex task after installation.
