# Install and validate Digital Product Studio by Sadé

## Install from the Git marketplace

After this repository is hosted on GitHub, a workspace administrator can paste its full repository URL into the Codex marketplace import field. CLI users can run:

```bash
codex plugin marketplace add digitalluxebysade-sketch/digital-product-studio-marketplace
codex plugin add digital-product-studio@sade-digital-product-studio
```

Open a new Codex task after installation so the 26 skills are loaded.

## Test

1. Select Digital Product Studio by Sadé from the plugin or skill picker.
2. Paste a prompt from `docs/routing-tests.md`. For a routing-only check, append: “Only identify the skills and handoff sequence; do not create assets yet.”
3. Verify that a narrow request selects its specialist.
4. Test the coordinator with a small complete product before starting a large generation run.
5. Confirm generated deliverables match their manifest and test real PDF links in the intended viewer.

## Dependencies

Visual workflows require Codex image-generation capability. Live Canva editing requires a connected Canva integration. The preserved PDF helpers require Python with PyMuPDF. Repository validation additionally requires PyYAML and Pillow.

Create an isolated validation environment from the repository root:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install PyYAML PyMuPDF Pillow
.venv/bin/python digital-product-studio/scripts/validate_studio.py
.venv/bin/python /PATH/TO/plugin-creator/scripts/validate_plugin.py digital-product-studio
```

Validate an individual skill with the official skill-creator validator:

```bash
.venv/bin/python /PATH/TO/skill-creator/scripts/quick_validate.py digital-product-studio/skills/SKILL-NAME
```

Do not commit `.venv`, generated products, temporary fixtures, customer data, or credentials.

## Update

1. Edit the plugin under `digital-product-studio/`.
2. Run the validators above.
3. Update the plugin manifest cachebuster with the official helper:

```bash
python3 /PATH/TO/plugin-creator/scripts/update_plugin_cachebuster.py digital-product-studio
```

4. Commit and push the reviewed changes.
5. Refresh the Git marketplace and reinstall the plugin:

```bash
codex plugin marketplace upgrade sade-digital-product-studio
codex plugin add digital-product-studio@sade-digital-product-studio
```

Open a new task after updating.
