---
name: create-product-listing
description: Use when the user has a product or product concept and wants a listing title, description, included-items section, usage instructions, FAQs, keywords, listing-image plan, or store-ready copy. Do not use for broad brand strategy without a specific product.
---

# Digital Product Listing Creator

## Purpose

Turn a finished digital product into a clear, conversion-focused listing and promotional asset plan.

## Activation behavior

Use this skill when its description matches the user's actual job-to-be-done. It may be invoked explicitly as `$create-product-listing`. Do not force this skill onto unrelated tasks.

## Required inputs

- Product name and finished deliverables
- Target buyer and primary outcome
- Store or marketplace
- License terms and usage limitations
- Brand voice and visual style
- Any verified technical features

When a critical input is missing, ask one focused question. When a reasonable default will not materially change the outcome, proceed with the default and label it under **Assumptions**. Never pretend an unknown detail was supplied.

## Workflow

1. Inventory the actual product files and separate confirmed features from planned features.
2. Identify the primary buyer problem, desired transformation, strongest differentiators, and likely purchase objections.
3. Create a truthful product title and subtitle appropriate for the chosen storefront. Avoid keyword stuffing and unsupported superlatives.
4. Write the listing in this order: opening promise, who it is for, what is included, key benefits, how it works, file details, important notes, license summary, and concise FAQ.
5. Create a listing-image sequence that answers buyer questions visually: hero, transformation, included items, feature close-up, how-to-use, compatibility, license or bonus, and final call to action.
6. Generate search phrases and tags based on the buyer, use case, product type, and aesthetic. Mark platform-specific limits when known; otherwise provide a prioritized pool.
7. Proofread the listing against the actual files. Remove any claim that cannot be verified.
8. Prepare a final copy block and a separate production checklist for the listing graphics.

## Output contract

Return the following, adapting the format to the user's requested deliverable:

- Product positioning summary
- Store-ready title and description
- What-is-included list
- FAQ and important notes
- Listing-image storyboard
- Keyword and tag pool
- Final verification checklist

Put the primary usable deliverable first. Keep process notes brief unless the user asks for detail. Clearly separate verified facts, assumptions, recommendations, and work that still requires testing.

## Final quality checks

- [ ] Every feature described is actually included
- [ ] File types, page counts, sizes, and compatibility are accurate
- [ ] The first paragraph explains the value quickly
- [ ] License language matches the supplied license
- [ ] The listing distinguishes digital delivery from physical shipping
- [ ] No income guarantees or fabricated urgency

Do not call the work complete until every applicable item passes or is clearly marked as unresolved.

## Guardrails

- Do not manufacture reviews, scarcity, rankings, or results.
- Do not give legal advice; label license language as a template when appropriate.
- Do not say “instant download” unless the sales platform is configured for it.
- Do not use trademarked names as the seller’s own brand identity.

## Failure and edge-case handling

- When source files are missing or unreadable, state exactly what could not be inspected and continue with the parts that can be completed safely.
- When requirements conflict, prioritize explicit non-negotiables, current corrections, safety, and acceptance criteria. Surface any remaining conflict.
- When current prices, laws, platform behavior, compatibility, schedules, or technical requirements matter, verify them from authoritative current sources before relying on them.
- Never claim that a file, link, build, feature, calculation, or test works without evidence.
- Preserve the user's supplied names, dimensions, wording, and assets unless they request changes.

## Starter prompts

- `Use $create-product-listing for this 2027 digital planner and create an eight-image listing plan.`
- `Write a store-ready listing for this brand-kit bundle using only the features shown in the delivery folder.`
