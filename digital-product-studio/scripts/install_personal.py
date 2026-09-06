#!/usr/bin/env python3
"""Register this private local plugin using the official scaffold, then install it."""
from pathlib import Path
import json
import shutil
import subprocess
import sys

source = Path(__file__).resolve().parents[1]
home = Path.home()
target = home / 'plugins/digital-product-studio'
marketplace = home / '.agents/plugins/marketplace.json'
helpers = home / '.codex/skills/.system/plugin-creator/scripts'
codex = shutil.which('codex') or '/Applications/ChatGPT.app/Contents/Resources/codex'
if target.exists():
    raise SystemExit(f'Existing source preserved: {target}. Use the documented update flow.')
if marketplace.exists():
    subprocess.run([sys.executable, str(helpers / 'read_marketplace_name.py')], check=True)
    if any(p['name'] == 'digital-product-studio' for p in json.loads(marketplace.read_text())['plugins']):
        raise SystemExit('Existing marketplace entry preserved; inspect its source before continuing.')
manifest = json.loads((source / '.codex-plugin/plugin.json').read_text())
if manifest['name'] != 'digital-product-studio':
    raise SystemExit('Unexpected plugin identity.')
subprocess.run([sys.executable, str(helpers / 'create_basic_plugin.py'), 'digital-product-studio', '--with-marketplace'], check=True)
shutil.copytree(source, target, dirs_exist_ok=True,
                ignore=shutil.ignore_patterns('.DS_Store', '__pycache__', '.venv', '.git'))
name = subprocess.check_output([sys.executable, str(helpers / 'read_marketplace_name.py')], text=True).strip()
subprocess.run([codex, 'plugin', 'add', f'digital-product-studio@{name}', '--json'], check=True)
print(f'Personal source: {target}\nMarketplace: {marketplace}')
