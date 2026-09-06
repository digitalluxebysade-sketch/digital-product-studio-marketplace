# Pinterest Mockup Backend Reference Library v2.0.0

This package was built from the uploaded archive containing **221 one-page PDF references**.

- Active unique references: **197**
- Exact duplicates excluded from retrieval: **3**
- Pinterest/interface screenshot excluded: **1**

## Purpose

Use this as a private visual backend for the `create-any-product-mockup` skill. It is designed to help the skill produce Pinterest-ready, Etsy-ready aesthetic mockups with stronger scene, styling, lighting, product construction, and composition decisions.

## Important

A written `skill.md` cannot magically see files that are not available to the running workspace. The reference folder and index must be uploaded or installed where the skill can access them. The workflow must pass selected image files into image generation as actual visual references whenever supported.

## Install

1. Keep this folder or ZIP private.
2. Upload it to the same ChatGPT Project/workspace as the mockup skill.
3. Add `PROJECT_INSTRUCTIONS.txt` to the Project instructions.
4. Merge `SKILL_PATCH.md` into the existing skill instructions.
5. Keep `reference-index.json` beside the `reference_library` folder.
6. Before every generation, select only 2-5 relevant active references.

## Next merge step

To produce one fully merged installable skill ZIP, provide the current `create-any-product-mockup` skill ZIP. This package is already prepared as the backend visual-library add-on.
