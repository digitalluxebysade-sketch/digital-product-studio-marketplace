---
name: create-any-product-mockup
description: Create Pinterest-ready aesthetic product mockups and Etsy listing graphics using curated visual references for products, poses, scenes, lighting, styling, digital planner device layouts, and commercial presentation.
---

# Skill: create-any-product-mockup

## Purpose
Create Pinterest-ready, Etsy-ready aesthetic mockups for apparel, drinkware, accessories, device/product displays, and lifestyle product scenes. The skill must use a private backend visual reference library to guide product construction, pose, scene, styling, lighting, palette, and framing.

## Use this skill when the user asks for
- product mockups
- Etsy mockups
- Pinterest-ready mockups
- shirt mockups, clothing mockups, model mockups, mannequin mockups
- mug mockups, tumbler mockups, bottle mockups, drinkware mockups
- blank mockups, apply-my-design mockups, or created product mockups
- aesthetic lifestyle product photos
- boutique-style or editorial mockups
- mockup listing image sets

## Main goal
Do not create generic catalog mockups. Create styled, original, save-worthy mockups that feel like polished Pinterest inspiration images and premium Etsy listing photos.

The mockup must reflect:
- the requested product and correct product construction
- the requested scene and aesthetic feel
- pose, framing, and camera angle
- lighting mood and palette
- commercial clarity so the product is easy to view and sell from

## Core output promise
Every image should feel:
- Pinterest-ready
- aesthetic and curated
- boutique and lifestyle-oriented
- product-focused
- original, not copied
- commercially useful for listings, social posts, and marketing

## Supported product families
- women’s apparel
- men’s apparel
- children’s apparel
- mannequin apparel displays
- product-only apparel displays
- ceramic mugs
- sculpted mugs
- glass tumblers
- acrylic tumblers
- travel bottles and drinkware
- phone cases and accessories
- device mockups and digital product display scenes
- related lifestyle product scenes

## Supported output modes
1. **Blank mockup mode**
   Create a plain product with a clean printable area and no accidental design, logo, watermark, or text.

2. **Apply-my-design mode**
   Apply the user’s provided artwork accurately. Preserve spelling, layout, color, transparency, and placement. Make the design follow perspective, folds, fabric tension, print boundaries, reflections, and drinkware curvature.

3. **Create-the-product mode**
   Generate the product itself from the description while using selected references to guide construction, styling, mood, and scene.

4. **Digital planner Etsy listing-graphic mode**
   Create a designed marketplace listing image for a digital planner, journal, template, workbook, or comparable screen-based product. When digital-planner reference images are provided or selected from the digital planner reference library, match their overall listing-graphic visual language as a required output constraint.

## Creative-direction check
Before generating, ask the user to choose the style/scene when they have not already stated it. For digital planners, ask whether they want **Etsy listing graphics** or **lifestyle/workspace mockups**. Do not ask again when the user has already supplied that choice.

## Backend visual reference library rule
This skill uses a private backend visual reference library stored beside this skill package.

Before every generation:
1. Read `reference-index.json`.
2. Classify the request by:
   - product family
   - exact product construction
   - audience or model type
   - blank / apply design / create product mode
   - aesthetic direction
   - scene or environment
   - lighting and mood
   - color palette
   - pose and framing
   - output purpose such as Etsy listing, Pinterest image, hero shot, close-up, or lifestyle shot
3. Select **2 to 5 active references only**. Never use the whole library.
4. Assign each selected reference a role.
5. Use the selected image files as actual visual inputs whenever supported.
6. Never use excluded references, duplicates, interface screenshots, marketplace UI, browser chrome, ads, or watermarked sources.

## Retrieval priority
When choosing references, prioritize in this order:
1. product family and construction
2. audience: adult women, adult men, children, mannequin/product-only
3. requested aesthetic
4. scene/environment
5. lighting and color palette
6. pose and framing
7. commercial purpose

## Allowed reference roles
Each selected image may be used for one or more of these roles:
- product construction
- garment silhouette
- surface-decoration method
- scene/environment
- lighting
- pose
- framing/camera crop
- styling
- color palette
- prop styling
- device/screen composition
- planner listing-graphic composition

Use each reference only for its assigned role. Do not copy irrelevant elements.

## Silent mockup blueprint
Before generating, silently build this blueprint:
- product category and exact construction
- blank / design-applied / create-product mode
- audience and model presentation
- aesthetic direction
- scene/environment
- lighting and mood
- color palette
- pose and framing
- props/accessories
- design-placement zone and print method
- dimensions and number of separate outputs
- chosen reference IDs and assigned roles

## Scene and aesthetic rule
Always preserve the requested scene and aesthetic feel. Treat mood, environment, lighting, styling, and props as required output elements, not optional extras.

If the user provides references or if relevant library references exist, analyze them for:
- atmosphere
- styling energy
- composition style
- set dressing / prop choices
- palette
- light quality
- fashion presentation
- visual softness or editorial sharpness

Then recreate the same overall visual language in an original image.

## Pinterest-ready aesthetic rule
The mockup should feel like a save-worthy Pinterest image or premium boutique campaign, not a flat catalog shot.

Target qualities:
- clean framing
- balanced negative space
- strong subject emphasis
- attractive styling
- coordinated palette
- soft, intentional lighting
- clear product visibility
- visually pleasing scene composition

Avoid:
- dull generic white-only catalog shots unless specifically requested
- random clutter
- harsh or muddy lighting
- lifeless composition
- cheap template-like mockups

## Digital planner Etsy listing-graphic rule
For a digital planner, journal, template, workbook, or other screen-based digital product requested as an Etsy-ready mockup or listing image, default to **digital planner Etsy listing-graphic mode**. This is a designed product-presentation graphic, not a photo-real desk photograph.

When the planner reference library contains user-approved listing examples, select two to five of those references and treat their visual language as mandatory: the full-canvas poster layout, oversized device screens, multi-device composition, cover-plus-interior-page presentation, tab visibility, themed graphic background, and polished Etsy listing hierarchy. Recreate that language in an original design using the user's planner; never reproduce a seller name, logo, exact wording, page design, or branded visual asset.

Build the image with:
- one to three oversized, crisp tablet devices showing the supplied cover and/or real internal pages
- a full-canvas, poster-like composition with a flat or softly textured themed graphic background that matches the product palette
- cover, visible planner tabs, and inside spreads composed like a premium digital-product listing, with stylus and coordinated decorative accents when supported by the product style
- clean hierarchy, large readable product screens, graphic layers, and deliberate negative space
- optional product facts or callouts only when the user supplied the exact claim and wording

Do not use a wood desk, coffee mug, pedestal, realistic room, hand-held photo, realistic ambient lighting, or lifestyle product photography in this mode. Do not merely place an iPad into a workspace scene. Use a designed graphic background and a planner-centric layout instead. Use lifestyle scenes only when the user explicitly asks for them.

For uploaded planner PDFs, extract and use the cover plus one or two representative internal pages as actual screen inputs. Preserve their artwork, tab layout, colors, and text. Do not invent planner pages, fake feature counts, app compatibility claims, or unreadable marketing copy.

For a five-image listing set, provide varied graphics such as:
- cover hero with a single large iPad
- cover plus internal-page dual-tablet layout
- multi-device showcase featuring tabs and spreads
- close crop highlighting a functional planning page and stylus
- alternate themed product-presentation graphic

## Pose and framing rule
Pose is a core part of the mockup, not a random result.

When the request involves a model, mannequin, handheld product, or product angle, use pose/framing references when available.

The skill should identify and preserve the general pose language of the chosen reference(s), including:
- body posture
- arm placement
- hand position
- leg placement
- seated, standing, walking, or leaning energy
- product-holding position
- crop level
- front, side, back, or three-quarter angle
- editorial or casual pose energy
- camera distance and framing style

The skill may classify or retrieve pose references using tags like:
- `pose_full_body_front`
- `pose_full_body_3quarter`
- `pose_waist_up`
- `pose_close_up`
- `pose_mirror_selfie`
- `pose_seated`
- `pose_walking`
- `pose_leaning`
- `pose_holding_mug`
- `pose_holding_tumbler`
- `pose_product_only_front`
- `pose_product_only_angled`
- `pose_flatlay`
- `pose_mannequin_front`
- `pose_mannequin_side`
- `pose_back_view`

If exact tags are not present, infer equivalent pose/framing intent from the reference’s category, composition, and notes.

## Suggested scene types
The skill should support scenes such as:
- white studio editorial
- soft gray studio
- colored studio editorial
- mirror selfie vibe
- casual indoor fashion
- city street style
- outdoor lifestyle
- cozy bedroom scene
- desk/workspace setup
- shelf styling
- blanket or bedding scene
- soft tabletop scene
- kitchen counter scene
- book-and-mug scene
- warm ambient room scene
- clean digital-product device scene

## Product presentation rule
Provide commercially useful variety when the user requests multiple images.

For apparel sets, useful variations may include:
- front hero pose
- three-quarter pose
- full outfit shot
- close-up crop of garment/product area
- back or alternate-angle view

For mugs/tumblers/bottles, useful variations may include:
- product-only hero image
- handheld lifestyle image
- desk/bedroom scene
- close-up of decoration/materials
- alternate side or wrap view

For digital planner Etsy listing-graphic sets, vary device arrangement, displayed cover/page, crop, background, and accent styling. Keep every image in the same collection visually cohesive.

Do not create several near-identical images unless requested.

## Separate image rule
One requested mockup equals one separate generated image. Generate each requested mockup separately unless the user explicitly asks for a collage, contact sheet, or comparison board.

## Quality control and regeneration rule
Reject and regenerate any result containing:
- broken hands or extra fingers
- awkward anatomy
- distorted faces
- unnatural limbs or posture
- warped seams or impossible garment construction
- floating straps or accessories
- misspelled text
- accidental logos, trademarks, marketplace labels, browser UI, or watermarks
- designs floating off the product
- inaccurate print placement
- planner pages that differ from the supplied artwork or have warped tabs, cut-off pages, or unreadable screen composition
- any photo-real workspace styling, room, desk, pedestal, or lifestyle-photo composition when digital planner Etsy listing-graphic mode was selected
- a single iPad on a generic background when selected references show a multi-device, cover-plus-page, or layered product-presentation composition
- clutter that hides the product
- lighting that breaks the requested aesthetic
- child models styled in an adult-coded way

## Child reference rule
Children’s mockups must remain age-appropriate, comfortable, and commercially styled. Avoid mature styling, adult-coded posing, or suggestive presentation.

## Identity and copyright protection
Use visual language, styling, pose energy, and composition only. Do not recreate a real person’s exact face or identity. Do not reproduce copyrighted characters, branded graphics, visible logos, or exact text from references.

## Final behavior summary
For every request, think in this order:
**product + product construction + mode + aesthetic + scene + lighting + pose + framing + commercial purpose**

The final output should balance:
- aesthetic appeal
- product clarity
- realism
- originality
- Pinterest-worthiness
- Etsy usability
