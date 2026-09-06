---
name: digital-planner-tab-shape-selector
description: Required pre-generation tab-shape selection skill for digital planners. Determines only the visual shape/style of planner tabs before image generation begins.
---

# Digital Planner Tab Shape Selector

## Purpose

Use this skill whenever creating a digital planner that includes tabs.

This skill is ONLY used to determine the **shape/style of the planner tabs** before image generation begins.

Do not determine tab labels, planner sections, tab names, or navigation structure in this skill.

## REQUIRED STEP BEFORE IMAGE GENERATION

Before generating the planner cover, interior pages, or planner spreads, determine what tab shape the user wants.

If the user has already provided a clear tab reference image or described the tab shape they want, use it and do not ask again.

If the user has NOT specified a tab shape, ask:

**What tab shape would you like to use for this digital planner?**

Provide visual or written options such as:

1. Classic Rectangle
2. Rounded Rectangle
3. Half-Circle
4. Scalloped
5. Arrow
6. Flag / Ribbon
7. Bow-Shaped
8. Cloud
9. Heart
10. Vintage / Ornamental
11. Custom Shape

The user may also upload an image showing the exact tab shape they want.

## VISUAL REFERENCE

When possible, show the user a visual reference sheet containing different tab shapes so they can choose by number or appearance.

The reference is only for choosing the **shape**.

Do not require the user to choose:
- tab labels
- section names
- months
- colors
- number of tabs
- hyperlink destinations

Those are handled by other planner skills.

## REFERENCE IMAGE RULE

If the user uploads a planner or tab reference image, study only the tab shape for this step.

Pay attention to:
- outer silhouette
- rounded or sharp corners
- curves
- scallops
- decorative edges
- cut-out style
- pointed edges
- ornamental shape
- overall proportions

Do not automatically copy unrelated parts of the reference image.

## TAB SHAPE LOCK

Once the user chooses a tab shape, lock that shape for the planner.

All tabs throughout the planner should use the same selected shape unless the user specifically asks for multiple tab styles.

Image generation must not randomly change the tab shape from page to page.

Preserve:
- the same silhouette
- the same edge style
- the same corner treatment
- the same general proportions

Colors, labels, and active states may vary later depending on the planner design.

## IMAGE GENERATION HANDOFF

Image generation should not begin until the tab shape has been selected.

Workflow:

Planner request
→ Choose tab shape
→ Pass selected shape to planner creation skill
→ Begin image generation

When handing the choice to the planner creator, include:

**SELECTED TAB SHAPE: [chosen shape]**

Example:

**SELECTED TAB SHAPE: Scalloped Tabs**

The planner creation skill must preserve this shape throughout the finished planner.

## IMPORTANT

This skill is a **shape selector only**.

Do not ask the user to determine tab labels or planner navigation during this step.

The goal is simply to make sure the user chooses the visual tab shape they want before any planner images are generated.
