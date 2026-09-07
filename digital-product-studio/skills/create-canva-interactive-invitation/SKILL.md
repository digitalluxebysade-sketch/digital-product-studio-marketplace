---
name: create-canva-interactive-invitation
description: Creates complete Canva-ready invitations for any event using ChatGPT image generation. Use for weddings, bridal showers, baby showers, gender reveals, birthdays, graduations, anniversaries, memorials, holidays, religious events, business events, fundraisers, parties, and other invitations. Produces each invitation section as a separate image at the user's requested size, with optional closed/open envelope reveal, transparent assets, and product-listing images. Do not code.
metadata:
  author: Digital Luxe by Sade
  version: "1.1.0"
  category: invitation-design
---

# Create Canva Interactive Invitation

Create polished, Canva-ready invitation graphics for any event. Adapt the content and section set to the event instead of forcing birthday-specific sections onto every project.

## Use this skill when

Use this skill when the user asks for:

- An interactive invitation website or scrolling invitation made in Canva
- A digital invitation, e-vite, animated invitation concept, invitation mini-site, or invitation section set
- A printable or mobile invitation created with ChatGPT image generation
- Wedding, bridal shower, engagement, baby shower, gender reveal, graduation, birthday, anniversary, retirement, housewarming, holiday, memorial, funeral, church, fundraiser, grand opening, conference, launch, or other event invitations
- Separate invitation sections, matching transparent assets, or invitation product-listing images

Do not use this skill merely to write invitation wording unless the user also wants the visual invitation designed.

## Non-negotiable rules

1. Use ChatGPT image generation for all original invitation visuals.
2. Do not code the invitation. The final graphics are intended for assembly in Canva.
3. Generate every finished section as its own separate image.
4. Never combine multiple finished sections into a collage, grid, contact sheet, or preview board.
5. One requested section equals one individual image-generation output.
6. Generate the complete requested set. Do not stop after one image or the first batch.
7. Use the image tool's available batch capacity efficiently. Up to 10 separate images may be generated in one batch when supported.
8. Preserve approved work. When a correction is requested, edit only the affected image or element instead of restarting the entire project.
9. Follow the exact dimensions requested by the user. Keep every section in a project at the same dimensions unless the user requests mixed sizes.
10. Keep layouts elegant, readable, balanced, and uncluttered.
11. For interactive Canva invitations, design the sections as connected slices of one larger invitation experience. Think of the invitation as one long panoramic Canva experience split into page-sized sections.
12. The right edge of one page must connect naturally to the left edge of the next page unless an intentional transition is required.
13. Do not add labels such as "opened version," "closed version," "slide 1," or explanatory speech bubbles inside the final artwork.
14. Clearly identify each generated output outside the artwork by its section name and sequence number.

## Default output modes

Determine the mode from the user's request.

### Interactive Canva invitation

Use this mode when the user asks for an invitation website, interactive invitation, scrolling invitation, multiple sections, or a design similar to the birthday invitation workflow.

- Default dimensions when none are supplied: 988 × 559 px
- Begin with a closed envelope image, followed by a matching opened envelope image, unless the user explicitly removes the envelope intro.
- Build the rest of the invitation section by section.
- Each section must look like part of one continuous visual system and, for interactive multi-page invitations, part of one connected scene that flows across page cut-offs.

### Single invitation card

Use this mode when the user asks for one invitation card only.

- Default printable portrait size: 1500 × 2100 px, representing a 5 × 7 ratio
- Do not add the envelope sequence unless requested.
- Place only the essential event information on the card.

### Mobile invitation

Use this mode for story-style, phone-first, or vertical invitations.

- Default dimensions: 1080 × 1920 px
- Keep text within comfortable mobile-safe margins.

Always honor the user's requested dimensions over these defaults.

## Required project analysis

Before generating, determine from the conversation and uploaded references:

- Event type and purpose
- Host, honoree, couple, organization, or event name
- Date, time, location, RSVP information, and other supplied details
- Invitation mode and exact dimensions
- Theme, colors, mood, level of formality, and target audience
- Whether the user supplied reference images, characters, people, logos, or a video
- Whether the project needs transparent assets or product-listing images
- Whether any sections are required, optional, or inappropriate for the event

Do not repeat questions that the user already answered. If important event details are missing, use tasteful editable placeholders rather than blocking the workflow.

## Reference handling

- Treat the user's uploaded references as the primary style guide.
- Preserve the approved color palette, character appearance, facial features, skin tone, clothing, proportions, and recurring decorative elements across sections.
- Do not redesign or alter an approved character unless the user requests it.
- When the user says a reference is for inspiration only, capture the mood and design language without copying its exact composition.
- When a reference video shows the interaction sequence, use it to understand the order and reveal concept, then create original graphics.
- Do not introduce unrelated characters or decorative motifs.

## Step-by-step workflow

### Step 1: Select the event playbook

Read `references/invitation-playbooks.md` and choose the closest event type. Use that playbook as a starting point, not a rigid checklist.

### Step 2: Build the section manifest

Create a complete section manifest before image generation. Use this adaptable structure:

Core interactive sections:

1. Closed envelope
2. Opened envelope
3. Cover or hero
4. Welcome or announcement
5. Event details
6. RSVP or response information
7. Closing or thank-you

Add only the event-relevant sections from `references/section-library.md`, such as:

- Countdown
- Schedule, agenda, ceremony order, or timeline
- Dress code
- Directions, parking, travel, or accommodations
- Registry, gift note, donation information, or wish list
- Hosts, wedding party, speakers, sponsors, or honorees
- Menu or refreshments
- Gallery or memories
- FAQ
- Livestream details
- Tickets or admission
- Playlist
- Memorial tribute or order of service

If the user explicitly lists sections, include every requested section unless it is unsafe or impossible.

### Step 3: Lock the visual system

Before generating the full set, define and keep consistent:

- Canvas dimensions and orientation
- Color palette
- Background treatment
- Typography categories and hierarchy
- Border, frame, texture, and decorative motifs
- Character or subject appearance
- Envelope style, paper shape, ribbon, seal, or opening treatment
- Button or link placeholder style for Canva assembly
- Spacing and safe text zones

Every section must look like it belongs to the same invitation.

### Step 3A: Apply connected page flow for interactive invitations

When the invitation is interactive, scrolling, or assembled page by page in Canva, treat the design as one continuous storyboard instead of unrelated standalone pages.

Connected page flow requirements:

- Plan the entire invitation as one long connected visual journey before generating the full set.
- Each page must preserve continuity from the previous page and create continuity for the next page.
- The right edge of one page should continue naturally into the left edge of the next page.
- If an element approaches or touches a page edge, it should either continue onto the adjacent page or end in a clearly intentional way.
- Keep the same background system, perspective, lighting, scale, and color palette across neighboring pages unless an intentional transition is desired.
- Continue decorative systems across page edges whenever appropriate, including borders, bows, ribbons, lace, florals, vines, sparkles, clouds, curtains, arches, scallops, wallpaper, flooring, frames, pathways, table edges, or string lights.
- Avoid abrupt cut-offs that make pages feel disconnected.
- The first page should begin the visual journey cleanly, and the last page should feel like a proper ending rather than a sudden crop.
- Do not make each page feel like a separate flyer unless the user specifically asks for standalone pages.

### Step 4: Generate the envelope reveal

For interactive mode, create these first unless the user says otherwise:

1. Closed envelope: a complete closed envelope with the event's visual theme and a suitable seal, bow, clasp, sticker, or closure.
2. Opened envelope: the same envelope visibly opened, with a coordinated card or paper reveal.

Envelope continuity requirements:

- Same envelope color, material, proportions, background, camera angle, seal, and decorations
- The opened version must look like the same envelope after opening
- No instructional words, labels, arrows, bubbles, or UI text inside the artwork
- Leave room for Canva animation or clickable interaction if the design calls for it

### Step 5: Generate every section separately

Generate sections in numbered batches until the manifest is complete. In interactive mode, generate each section with awareness of its neighboring pages so the cut-off edges connect correctly.

Recommended batch pattern:

- Batch 1: Envelope reveal and the first core sections, up to 10 separate images
- Batch 2: Remaining informational and experience sections, up to 10 separate images
- Additional batches: Continue as needed until all sections, assets, and listing images are complete

Never stop after Batch 1 when more outputs remain.

### Step 6: Create transparent assets when requested

Create individual PNG-style assets with true transparent backgrounds. Each asset should be separate, not a sheet.

Possible assets include:

- Bows, ribbons, seals, flowers, balloons, rings, baby items, graduation caps, candles, icons, dividers, buttons, arrows, frames, or themed characters
- Matching decorative elements needed to build interactions in Canva

Do not place a checkerboard pattern or fake transparency behind assets.

### Step 7: Create listing images when applicable

For a sellable invitation product, bundle, template, or shop listing, create five separate listing images using `references/listing-image-plan.md`.

For a private customer invitation, do not add listing images unless requested.

### Step 8: Validate the complete set

Before finishing, verify:

- Every requested section exists as a separate image
- All images use the correct dimensions and orientation
- The section order makes sense for the event
- Interactive invitations have proper left-edge and right-edge continuity between neighboring pages
- Event names, dates, times, addresses, and RSVP details are consistent
- Text is legible and not cropped
- No birthday-specific wording remains in a non-birthday invitation
- No unnecessary page is included merely because it existed in another invitation type
- Envelope images match each other
- Approved characters, people, logos, and motifs remain consistent
- No artwork contains generation labels, explanations, or unwanted bubbles
- The set is uncluttered and visually consistent
- Any requested transparent assets are truly isolated
- All batches are complete

Fix only the failed images, then re-check them.

## Continuity correction rule

If continuity breaks between pages, do not restart the entire invitation. Fix only the affected pages and explicitly regenerate them with instructions describing which elements must align on the left edge, which must align on the right edge, and what visual systems must continue across the cut-off.

## Text and content rules

- Use the user's exact event details when provided.
- Keep wording appropriate to the event's formality and emotional tone.
- Use placeholders such as `[Name]`, `[Date]`, `[Time]`, `[Venue]`, and `[RSVP Link]` when details are missing.
- Avoid excessive text on one section. Split dense information into additional sections when needed.
- For memorial and religious events, use respectful and restrained wording.
- For business events, prioritize clarity, agenda, venue, admission, and contact details.
- For children's events, keep the design playful but readable for adults.

## Quality guardrails

- Do not overcrowd the canvas.
- Do not place essential text too close to an edge.
- Do not let decorative elements cover names, dates, locations, or response details.
- Do not change the theme, palette, or character style midway through the project.
- Do not let important decorative systems stop randomly at the page edge when they should continue onto the next page.
- Do not create a generic white card on top of an unrelated background unless the user's reference specifically requires that composition.
- Do not use a mockup frame as the final invitation section.
- Do not replace the user's requested event with a birthday concept.
- Do not invent guest names, addresses, phone numbers, websites, or real-world claims.

## Completion format

Maintain this output order:

1. Closed envelope, when applicable
2. Opened envelope, when applicable
3. Invitation sections in manifest order
4. Transparent assets, when requested
5. Product-listing images, when requested

Use concise external labels such as `Section 03 — Cover` or `Listing Image 02 — What Is Included`. Keep these labels outside the generated artwork.
