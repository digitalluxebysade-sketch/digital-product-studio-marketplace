# Canvas Equals Planner Page Protocol

## Core rule

Treat the image canvas and planner page as the same object. The full 567 × 726 canvas must be the functional planner page. Begin with a cream or white base layer extending from x=0, y=0 through the final right and bottom pixels.

Never place a smaller cream sheet on another layer. The finished result must look like a flat exported planner page, not a photograph, mockup, stationery sheet, framed document, or planner lying on a surface.

## Required construction

1. Fill 100% of the canvas with the cream or white worksheet color.
2. Place the functional worksheet directly on that base.
3. Extend the main cream page beneath all navigation and tabs.
4. Keep the cream or white page base underneath the tabs all the way to every outer canvas pixel. Tabs are overlays within the canvas, not objects attached to a smaller sheet sitting on a surface.
5. Reserve no more than 6% of canvas width for the attached right tab strip.
6. Keep top tabs inside a strip no more than 7% of canvas height.
7. Keep content, lines, tables, and writing boxes within the remaining safe area.
8. Use brown plaid only as a small tab or header accent when useful.
9. Keep the left and bottom edges fully cream or white with 0% exterior spacing.

Do not create:

- An exterior background or backing board
- A desktop, fabric, plaid surface, or photographic scene
- A mat, border area, device frame, or mockup
- Rounded outer page corners that expose another layer
- A drop shadow around the planner page
- A black or colored margin around the canvas
- A floating or inset cream sheet

Internal worksheet lines and section dividers are allowed. They must not read as an outer frame separating the page from the canvas.

## Reference precedence

When two references have different roles:

1. Use the theme reference only for brown, cream, stitched-tab styling, small plaid accents, motifs, and typography inspiration. Ignore page-within-a-background composition.
2. Use the full-page layout reference for canvas coverage, page proportions, navigation placement, tab placement, and edge-to-edge worksheet structure.
3. If the references conflict, the full-page layout reference controls composition.

Record these roles in the project brief and generation prompt.

## Mandatory prompt sentence

Add this exact sentence to every master-shell and finished-page generation prompt:

> Single flat full-canvas digital-planner export. Start with a cream or white page base covering every pixel and keep it underneath all tabs and navigation. The worksheet is the canvas itself: no exterior background, surrounding pattern, backing surface, frame area, mat, mockup, floating paper, outer drop shadow, black bar, rounded corner revealing another layer, or visible space outside the functional page.

Do not paraphrase or omit this sentence.

## Automatic rejection

Reject and regenerate from the approved full-bleed shell when:

- Brown, plaid, black, or any other area appears around the cream worksheet.
- The worksheet looks like a smaller sheet placed on a background.
- The canvas resembles a product mockup or photographed stationery.
- Rounded page corners reveal another layer.
- A drop shadow separates the worksheet from the canvas.
- The cream page does not reach the left or bottom edges.
- More than 6% of canvas width is used for right-side tabs.
- More than 7% of canvas height is used for top navigation.
- Any tab appears to extend from a smaller sheet onto an exposed backing layer.
- Any outer-edge pixel reads as a surface behind the planner instead of the page base or an approved tab over that base.

Do not crop away a failed background and call the page corrected when cropping would change the required canvas, tab proportions, or content. Regenerate from a compliant shell.

## QA measurements

For a 567 × 726 page:

- Right tab/navigation strip: at most 34 pixels wide.
- Top navigation strip: at most 51 pixels high.
- Left exterior spacing: 0 pixels.
- Bottom exterior spacing: 0 pixels.
- Visible surrounding background: 0 pixels.

Inspect all four outer edges at full resolution before accepting the page.
