---
name: planner-quality-control
description: Use when reviewing a digital or printable planner, journal, calendar, tracker, or workbook for production errors. Use before publishing or after batch generation. Do not use to design the planner from scratch unless paired with a creation skill.
---

# Planner Quality Control

## Required Undated All-in-One Standard

Read `references/all-in-one-planner-standard.md` and inspect `assets/planner-visual-reference.jpg` as the audit baseline. Check the actual inside-page families, clean visual look, softly rounded top tabs, slim right-edge tabs, locked navigation geometry, cover side margin, compact writing-first layouts, and complete hyperlink coverage. Do not require or validate a 2025 year unless the current project explicitly requests it.

## Purpose

Audit planner pages, dates, links, layout, and delivery files before release.

## Activation behavior

Use this skill when its description matches the user's actual job-to-be-done. It may be invoked explicitly as `$planner-quality-control`. Do not force this skill onto unrelated tasks.

## Required inputs

- Planner files or page images
- Page inventory and intended order
- Date range and locale
- Expected hyperlink map
- Target page dimensions and platform
- Known issues or prior corrections

When a critical input is missing, ask one focused question. When a reasonable default will not materially change the outcome, proceed with the default and label it under **Assumptions**. Never pretend an unknown detail was supplied.

## Workflow

1. Create an expected-content checklist from the page inventory before inspecting the files.
2. Check file-level integrity: filenames, duplicates, missing files, dimensions, orientation, color mode when relevant, and export quality.
3. Check content accuracy: headings, spelling, page numbers, labels, examples, repeated copy, and placeholder text.
4. For dated planners, verify month lengths, weekday alignment, leap-year behavior, recurring holidays only when requested, and all date transitions.
5. Inspect layout at normal viewing size and zoomed view. Flag crop risk, unsafe margins, small text, uneven spacing, blocked writing areas, and inconsistent components.
6. For digital-planner page artwork, run a Canvas Equals Planner Page inspection. Verify that the functional white or cream page base reaches all four canvas edges underneath tabs and navigation. Fail any page showing a smaller sheet on a decorative background, visible backing board, mat, fabric, desktop, exterior frame area, black bar, floating-paper shadow, or rounded corner revealing another layer. Theme patterns may appear inside tabs or page accents but never around the worksheet perimeter.
7. Compare the final separate files with the approved inventory. Fail the set when a functional page is missing, duplicated, replaced by a blank shell, represented only in a collage, or not exported at full size.
8. Test every hyperlink against the expected navigation map. Record source page, clicked element, expected target, actual target, and pass or fail.
9. Rank defects as blocker, major, minor, or cosmetic. Group repeated defects into one root-cause issue.
10. Return a release decision: pass, pass with minor corrections, or fail until blockers are repaired.

## Output contract

Return the following, adapting the format to the user's requested deliverable:

- Audit scope
- Defect log with severity
- Date validation report
- Hyperlink test record
- Visual consistency findings
- Release decision and repair order

Put the primary usable deliverable first. Keep process notes brief unless the user asks for detail. Clearly separate verified facts, assumptions, recommendations, and work that still requires testing.

## Final quality checks

- [ ] All expected pages were inspected
- [ ] Every digital page uses the whole canvas as the planner page with zero visible exterior background
- [ ] The finished functional-page count matches the approved inventory exactly
- [ ] Every blocker includes a reproduction location
- [ ] Repeated issues are counted consistently
- [ ] The audit distinguishes evidence from assumptions
- [ ] The final decision matches the severity findings

Do not call the work complete until every applicable item passes or is clearly marked as unresolved.

## Guardrails

- Do not certify links, dates, or print quality that were not tested.
- Do not rely only on thumbnails for legibility checks.
- Do not hide errors to preserve a preferred release date.
- Do not include real personal data in screenshots or examples.

## Failure and edge-case handling

- When source files are missing or unreadable, state exactly what could not be inspected and continue with the parts that can be completed safely.
- When requirements conflict, prioritize explicit non-negotiables, current corrections, safety, and acceptance criteria. Surface any remaining conflict.
- When current prices, laws, platform behavior, compatibility, schedules, or technical requirements matter, verify them from authoritative current sources before relying on them.
- Never claim that a file, link, build, feature, calculation, or test works without evidence.
- Preserve the user's supplied names, dimensions, wording, and assets unless they request changes.

## Starter prompts

- `Use $planner-quality-control to audit this 2027 planner before I list it.`
- `Check these page images for missing months, date errors, cropping, and inconsistent headers.`
