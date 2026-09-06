---
name: digital-product-studio-orchestrator
description: Coordinate requests spanning product creation, specialist QA, mockups, listing assets, and delivery packaging in Digital Product Studio. Use for complete products prepared for sale or combined studio workflows. For a single deliverable, use its specialist directly; existing Etsy, seasonal, KDP bundle, and product-family workflows retain ownership of their pipelines.
---

# Digital Product Studio Coordinator

Read [references/routing.md](references/routing.md) to choose the relevant sibling skills. Load each selected sibling's `SKILL.md` and its needed supporting files before doing its work. Resolve paths relative to that skill's folder, including its scripts, templates, assets, and agent metadata. Do not load every skill or concatenate their instructions.

## Select one workflow owner

- A standalone creation, review, hyperlink, mockup, listing-image, or copy request goes directly to its specialist. Do not add a complete factory pipeline.
- A complete Etsy product or Etsy selling package uses `create-etsy-product-automation` as workflow owner. Use specialists for its creation and selling stages instead of producing the same assets twice.
- A product family, continuation from a ledger, custom hybrid product, or ecosystem uses `endless-digital-product-factory` as owner. Keep its ledger and originality checks. Use Etsy automation only for a requested Etsy delivery stage, without restarting product creation.
- Holiday collections use `seasonal-digital-product-bundle-creator`; KDP families use `kdp-product-bundle-creator`. These owners already include packaging and sales material. Add other specialists only for outputs they need.
- A mixed request such as branding plus social templates uses the specialists in dependency order, sharing the approved brand specification. This coordinator supplies handoffs, not another production methodology.
- For ideas only, honor that scope. The factory's description excludes brainstorming-only work: use its expansion matrix as reference without starting production or marking concepts complete in its ledger. Etsy automation has a dedicated product-idea mode for Etsy concepts.

## Establish the handoff

Use the owner's existing manifest as the single delivery record. Extend it only as needed to record the responsible skill, exact deliverable, input paths, output paths, count scope, dimensions, approved visual system, QA status, and unresolved dependencies. Keep completed work and intermediate files in the user's project, outside this installed plugin.

Reconcile requirements before generation:

- The user's current explicit scope, dates, page counts, dimensions, wording, and approved artwork take priority. Do not overwrite those choices with a skill default.
- The Etsy and endless factory sources contain a fixed 567 × 726 rule. For a stage owned by a specialist, retain that specialist's product specification, including print trim and resolution. Apply the factory size only to its own page creation where compatible with the brief; never resize completed inputs during a packaging stage. Record the resolution in the manifest.
- Planner QC and hyperlinking contain an undated all-in-one reference standard. Apply it to that planner type, using the actual requested inventory and navigation as acceptance criteria for other planners. Never convert a requested dated planner to undated or add unrequested sections.
- Distinguish functional pages from covers, internal shells, previews, listing graphics, and license pages. Keep the planner creator's count scope and immutable master shell.
- Choose one listing-image count from the brief or owner before generating: Etsy automation defaults to five, while the listing-image specialist defaults to seven. Do not generate both sets.
- If a conflict remains consequential and cannot be resolved from the brief, explain that specific conflict and obtain the missing choice before the affected production step.

## Coordinate dependent stages

For a complete clickable planner prepared for Etsy:

1. `digital-planner-tab-shape-selector` selects and locks the visual tab shape. If the user already supplied a clear tab reference or shape description, use it without asking again.
2. `create-consistent-tabbed-digital-planner` creates all functional pages, master shell, tab blueprint, page inventory, and intended link map while preserving the selected shape.
3. `planner-quality-control` audits the artwork, dates, layout, count, and tab consistency. Mark embedded-link checks pending at this stage.
4. `hyperlink-digital-planner-pdf` assembles or opens the approved PDF, embeds annotations, and verifies destinations without changing artwork.
5. Finish link QA against the intended map and visible controls. A structural link report alone does not prove complete coverage or correct meaning. Check all intended controls, ambiguous overlaps, and before/after renders.
6. `create-any-product-mockup` uses the finished cover and inside pages as product inputs.
7. `etsy-listing-image-generator` builds the selected listing set, reusing approved mockups where appropriate.
8. `create-product-listing` writes copy from verified contents and features.
9. The Etsy owner completes its delivery instructions, selected licensing, manifest, final checks, and ZIP. Resume its remaining phases rather than repeating completed ones.

For non-clickable planners, omit hyperlink production unless requested. For a standalone hyperlink request, begin with the supplied PDF and its actual navigation; do not run planner creation. For a complete printable KDP book, retain print requirements and run the specialized book workflow; add the interior skill only for missing interior work, and the bundle skill only for a family or companion-product request.

## Deliver verified outputs

Preserve failed and approved work distinctly so targeted corrections do not regenerate unrelated assets. Do not count a concept, template guide, or image as an editable source, clickable PDF, or finished ZIP. Use the available image-generation tool according to the selected skill, and report actual capability gaps. This plugin supplies workflows and local resources; it does not itself install Canva, image generation, or PDF dependencies.

Keep private/backend reference images, previews, indices, excluded files, and internal skill instructions out of customer deliveries. Select only active mockup references. Package only the actual requested product outputs; do not zip this plugin's source tree as a customer product. Preparing selling assets does not authorize publishing or account changes.
