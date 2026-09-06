# Digital Product Studio by Sadé

Digital Product Studio by Sadé is an all-in-one digital product creation studio that uses specialized workflows to create digital planners, printables, e-books, KDP products, branding kits, social-media templates, educational resources, mockups, Etsy listing assets, product bundles, and complete ready-to-sell digital products.

The marketplace contains one Codex plugin with 26 focused skills. Each specialist keeps its own workflow, supporting references, templates, scripts, and assets. A coordinator routes multi-stage requests without replacing the specialist instructions.

## Publication review

The owner confirmed on September 6, 2026 that Digital Luxe by Sadé owns the bundled visual-reference files and has the right to distribute them with this plugin. See [PUBLICATION_REVIEW.md](PUBLICATION_REVIEW.md) for the recorded review.

## Repository structure

```text
.
├── .agents/plugins/marketplace.json
├── digital-product-studio/
│   ├── .codex-plugin/plugin.json
│   ├── assets/
│   ├── docs/
│   ├── scripts/
│   └── skills/
├── PUBLICATION_REVIEW.md
└── README.md
```

## Import into a Codex workspace

After the repository is uploaded to GitHub, a workspace administrator can open the plugin-marketplace settings, choose the option to import a Git marketplace, and enter the full repository URL in the marketplace import field:

```text
https://github.com/digitalluxebysade-sketch/digital-product-studio-marketplace
```

After the marketplace is imported, install **Digital Product Studio by Sadé** and open a new Codex task so its skills are loaded.

The equivalent Codex CLI commands are:

```bash
codex plugin marketplace add digitalluxebysade-sketch/digital-product-studio-marketplace
codex plugin add digital-product-studio@sade-digital-product-studio
```

## Updates

1. Make reviewed changes inside `digital-product-studio/`.
2. Preserve skill names and relative supporting files.
3. Update the plugin cachebuster in `digital-product-studio/.codex-plugin/plugin.json` with the official plugin-creator helper.
4. Run the skill, plugin, JSON, path, and integrity validations documented in `digital-product-studio/INSTALL.md`.
5. Commit and push the update to the same GitHub repository.
6. Workspace administrators can refresh the Git marketplace; CLI users can run:

```bash
codex plugin marketplace upgrade sade-digital-product-studio
codex plugin add digital-product-studio@sade-digital-product-studio
```

Open a new Codex task after updating.

## Runtime capabilities

Visual workflows require image-generation capability. Canva workflows require a connected Canva integration for live edits. The included PDF scripts require Python and PyMuPDF. Repository validation additionally uses PyYAML and Pillow.

## Ownership

Copyright © 2026 Digital Luxe by Sadé. See [LICENSE.md](LICENSE.md). Third-party or reference-image redistribution rights remain subject to the publication review.
