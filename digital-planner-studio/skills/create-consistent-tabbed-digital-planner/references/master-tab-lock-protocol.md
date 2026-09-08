# Master Tab Lock Protocol

## Objective

Keep the tab system visually identical on every tabbed planner page.

The shell is an internal reference asset. Do not count or deliver it as a finished planner page unless the user specifically requests it as an extra. After approval, use it to generate every separate page in the exact approved page manifest.

## The lock method

The approved full-bleed master interior shell is the only source of truth. Every new page must begin as an edit of that shell, not as a new full-page text-to-image generation. The shell must already pass `canvas-equals-planner-page-protocol.md`.

## Immutable area

The immutable area includes:

- Full-canvas cream or white page base
- Edge-to-edge page coverage with no exterior frame, mat, or backing layer
- Binding, rings, spine, or disc area
- Tab rail
- Every tab
- Tab labels
- Tab icons, when approved
- Header and footer elements that are part of the shell
- Outer margins

The immutable area must never include a surrounding plaid surface or other exterior background. Plaid may appear only as an approved small accent inside tabs or header details.

Only the defined content-safe zone may be edited.

Each edit must fill that zone with the manifest page's complete, unique functional content. A blank center, page title without worksheet structure, or navigation-only layout does not qualify as a finished page.

## Tab identity fields

Each tab must have:

- Stable ID
- Exact visible label
- Exact sequence number
- Edge
- Position
- Width
- Height
- Fill color
- Border
- Shadow
- Font
- Font size
- Text orientation
- Active state rule

## Reference hierarchy

Use references in this order:

1. Approved master interior shell image
2. Approved project manifest
3. Approved tab blueprint
4. Approved style guide
5. User's original instructions

A newly generated page must never replace the master reference.

## Failed-page recovery

When tabs drift:

1. Reject the page.
2. Do not edit the failed page.
3. Return to the master interior shell.
4. Repeat the page-specific edit.
5. Reduce the requested change to the center content only.
6. Inspect again.

## Visual comparison checklist

- Same total tab count
- Same exact labels
- Same order
- Same tab rail position
- Same dimensions
- Same gaps
- Same colors
- Same font
- Same label orientation
- Same border
- Same shadow
- Same crop and canvas position
