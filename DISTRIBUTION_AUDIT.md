# Distribution audit

Audit date: 2026-09-06

## Inventory

- Plugin: Digital Product Studio by Sadé
- Plugin slug: `digital-product-studio`
- Marketplace name: `sade-digital-product-studio`
- Skill folders: 30
- `SKILL.md` entrypoints: 30
- Plugin files: 371
- Plugin size: 27182287 bytes
- Symlinks: 0
- JSON files parsed: 14
- Image assets decoded by the integrity validator: 218
- Local Markdown/resource references checked: 50

## Skills

- `canva-social-media-template-pack-creator`
- `childrens-kdp-book-creator`
- `create-any-product-mockup`
- `create-coloring-book-collection`
- `create-consistent-tabbed-digital-planner`
- `create-digital-paper-pack`
- `create-etsy-product-automation`
- `create-product-listing`
- `create-recipe-ebook`
- `create-worksheet-level-variants`
- `digital-planner-tab-shape-selector`
- `digital-product-studio-orchestrator`
- `e-book-generator`
- `editable-ebook-workbook-creator`
- `endless-digital-product-factory`
- `etsy-listing-image-generator`
- `hyperlink-digital-planner-pdf`
- `kdp-interior-page-creator`
- `kdp-product-bundle-creator`
- `low-content-kdp-book-creator`
- `planner-quality-control`
- `puzzle-activity-book-creator`
- `seasonal-digital-product-bundle-creator`
- `small-business-branding-kit-automation`
- `teacher-resource-automation`
- `youtube-branding-kit-creator`

## Dependencies and capabilities

- Python standard library for the helper scripts.
- PyMuPDF for the planner PDF assembly, hyperlinking, inspection, and PDF validation fixture.
- PyYAML and Pillow for repository validation.
- Codex image generation for visual production workflows.
- A connected Canva integration for workflows that perform live Canva edits.

No dependency folder or virtual environment is committed.

## Validation results

- All 30 skill entrypoints passed the official skill validator.
- The plugin passed the official plugin validator.
- The studio integrity validator passed.
- All JSON files parsed successfully.
- Every skill file is byte-for-byte identical to the existing working plugin.
- The marketplace target resolves to `digital-product-studio/.codex-plugin/plugin.json`.
- No broken relative Markdown or declared local resource references were found.
- No API keys, tokens, passwords, private keys, credential files, symlinks, or personal computer paths were detected.

## Distribution changes

Created at repository level:

- `.agents/plugins/marketplace.json`
- `.gitignore`
- `README.md`
- `PUBLICATION_REVIEW.md`
- `LICENSE.md`
- `DISTRIBUTION_AUDIT.md`

Modified only in the distribution copy:

- `digital-product-studio/INSTALL.md`
- `digital-product-studio/BUILD_REPORT.md`
- `digital-product-studio/docs/source-archives.json`

The modified files contain installation or provenance documentation. No skill instruction, skill name, workflow, reference, template, script, or asset was changed.

## Publication issue

216 visual-reference files are located under the paths listed in `PUBLICATION_REVIEW.md`. On September 6, 2026, the owner explicitly confirmed that Digital Luxe by Sadé owns these files and has permission to redistribute them with the plugin. They remain present and unchanged.

The legacy `digital-product-studio/scripts/install_personal.py` is preserved for source compatibility. Git marketplace users should follow the root README instead.

## Readiness

The repository is ready for a Git marketplace, first commit, and public push to `digitalluxebysade-sketch/digital-product-studio-marketplace`.
