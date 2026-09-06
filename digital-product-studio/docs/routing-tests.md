# Routing acceptance scenarios

Conceptual review completed against source descriptions, workflows, and coordinator handoffs; live model selection and product generation are not claimed. In a fresh task, first ask for a routing-only plan to check scope without generating a full product. Then execute a small representative product.

1. **Prompt:** Create a 100-page feminine digital planner.

   **Expected:** digital-planner-tab-shape-selector → create-consistent-tabbed-digital-planner

2. **Prompt:** Hyperlink this completed planner PDF.

   **Expected:** hyperlink-digital-planner-pdf

3. **Prompt:** Check this planner for mistakes before I sell it.

   **Expected:** planner-quality-control

4. **Prompt:** Make Pinterest-ready mockups for this product.

   **Expected:** create-any-product-mockup

5. **Prompt:** Create Etsy listing images for this digital product.

   **Expected:** etsy-listing-image-generator

6. **Prompt:** Write the Etsy listing for this product.

   **Expected:** create-product-listing

7. **Prompt:** Create an entire Etsy digital product from scratch.

   **Expected:** create-etsy-product-automation

8. **Prompt:** Create a children’s coloring book.

   **Expected:** create-coloring-book-collection

9. **Prompt:** Create a puzzle activity book.

   **Expected:** puzzle-activity-book-creator

10. **Prompt:** Create a recipe e-book.

   **Expected:** create-recipe-ebook

11. **Prompt:** Create a 60-template social media pack for a salon.

   **Expected:** canva-social-media-template-pack-creator

12. **Prompt:** Create my small business branding kit.

   **Expected:** small-business-branding-kit-automation

13. **Prompt:** Create a YouTube branding package.

   **Expected:** youtube-branding-kit-creator

14. **Prompt:** Create classroom printables for third-grade math.

   **Expected:** teacher-resource-automation → create-worksheet-level-variants (if differentiation requested)

15. **Prompt:** Create a Christmas digital-product bundle.

   **Expected:** seasonal-digital-product-bundle-creator

16. **Prompt:** Create several new product ideas based on one successful digital product.

   **Expected:** ideas only; reference the factory expansion matrix, do not launch its production workflow

17. **Prompt:** Create a complete planner and prepare everything I need to sell it on Etsy.

   **Expected:** digital-product-studio-orchestrator → create-etsy-product-automation (owner) → digital-planner-tab-shape-selector → create-consistent-tabbed-digital-planner → planner-quality-control (artwork) → hyperlink-digital-planner-pdf → planner-quality-control (final links) → create-any-product-mockup → etsy-listing-image-generator → create-product-listing → create-etsy-product-automation (remaining packaging)

18. **Prompt:** Use scalloped tabs for my digital planner.

   **Expected:** digital-planner-tab-shape-selector → create-consistent-tabbed-digital-planner, with `SELECTED TAB SHAPE: Scalloped Tabs` preserved in the handoff

Case 16 preserves the request for ideas only. The source factory explicitly excludes brainstorming-only activation, so its expansion matrix can inform ideation without creating finished products.
