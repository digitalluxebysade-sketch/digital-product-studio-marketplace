#!/usr/bin/env python3
"""Validate preserved source integrity, skill resources, and PDF helper behavior."""
from pathlib import Path
import ast
import hashlib
import json
import re
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET
import yaml
from PIL import Image
import fitz

ROOT = Path(__file__).resolve().parents[1]
errors = []
checks = {}
modified = []

def check(condition, message):
    if not condition:
        errors.append(message)

inventory = json.loads((ROOT / 'docs/source-inventory.json').read_text())
expected = {row['name'] for row in inventory}
skills = sorted(p for p in (ROOT / 'skills').iterdir() if p.is_dir())
check({p.name for p in skills} == expected | {'digital-product-studio-orchestrator'}, 'Skill directory set differs')
for row in inventory:
    for item in row['files']:
        p = ROOT / 'skills' / row['name'] / item['path']
        check(p.is_file(), f'Missing source file: {p}')
        if not p.is_file():
            continue
        if hashlib.sha256(p.read_bytes()).hexdigest() != item['sha256']:
            modified.append(str(p.relative_to(ROOT)))
        mode = int(item['mode'], 8)
        check(not mode & 0o111 or p.stat().st_mode & 0o111, f'Lost executable mode: {p}')
allowed = [item['path'] for item in json.loads((ROOT / 'docs/source-changes.json').read_text())]
check(sorted(modified) == sorted(allowed), f'Unexpected source changes: {modified}')
checks['preserved_source_files'] = sum(len(row['files']) for row in inventory)
checks['source_files_byte_identical'] = checks['preserved_source_files'] - len(modified)

names = []
image_count = 0
local_paths = 0
for skill in skills:
    p = skill / 'SKILL.md'
    check(p.is_file(), f'Missing entrypoint: {skill.name}')
    text = p.read_text()
    fm = yaml.safe_load(text.split('---', 2)[1])
    names.append(fm['name'])
    check(fm['name'] == skill.name, f'Folder/name mismatch: {skill}')
    check(isinstance(fm.get('description'), str) and bool(fm['description'].strip()), f'Missing description: {skill}')
    for p in skill.rglob('*'):
        if not p.is_file():
            continue
        if p.suffix == '.py':
            ast.parse(p.read_text())
        elif p.suffix == '.json':
            json.loads(p.read_text())
        elif p.suffix == '.yaml':
            agent = yaml.safe_load(p.read_text())
            for key in ['icon_small', 'icon_large']:
                value = agent.get('interface', {}).get(key)
                if value:
                    check((skill / value).is_file(), f'Broken icon: {p}: {value}')
        elif p.suffix == '.svg':
            ET.parse(p)
        elif p.suffix.lower() in ['.png', '.jpg', '.jpeg']:
            with Image.open(p) as im:
                im.verify()
            image_count += 1
        if p.suffix in ['.md', '.txt']:
            text = p.read_text()
            for target in re.findall(r'\]\(([^)]+)\)', text):
                if target.startswith(('http:', 'https:', '#', 'mailto:')):
                    continue
                target = target.split('#')[0]
                check((p.parent / target).exists(), f'Broken Markdown reference: {p}: {target}')
                local_paths += 1
            for target in re.findall(r'`((?:references|assets|scripts|templates|agents)/[^`\n]+)`', text):
                check((skill / target).exists() or (p.parent / target).exists(), f'Broken resource: {p}: {target}')
                local_paths += 1
check(len(names) == len(set(names)), 'Duplicate skill names')
checks.update(skill_count=len(skills), decoded_images=image_count, checked_local_paths=local_paths)
mock = ROOT / 'skills/create-any-product-mockup'
index = json.loads((mock / 'reference-index.json').read_text())
for ref in index['references']:
    check((mock / ref['image_path']).is_file(), f'Missing indexed image: {ref["id"]}')
    check(not (ref['active'] and ref['image_path'].startswith('excluded/')), f'Excluded reference active: {ref["id"]}')
checks['active_mockup_references'] = sum(ref['active'] for ref in index['references'])
check(checks['active_mockup_references'] == index['summary']['active_unique_references'], 'Active index count mismatch')
listing = ROOT / 'skills/etsy-listing-image-generator/references'
for ref in json.loads((listing / 'reference-index.json').read_text())['references']:
    check((listing / ref['file']).is_file(), f'Missing listing reference: {ref}')
check((mock / 'PRIVATE_USE_NOTICE.md').is_file(), 'Private-use notice missing')

# A small fixture tests assembly, normalized/pixel/point coordinates, dynamic
# destinations, replacement, invalid maps, and unchanged rendered artwork.
scripts = ROOT / 'skills/hyperlink-digital-planner-pdf/scripts'
def run(script, *args, success=True):
    result = subprocess.run([sys.executable, str(scripts / script), *map(str, args)], capture_output=True, text=True)
    check((result.returncode == 0) == success, f'{script}: {result.stdout} {result.stderr}')
    return result

with tempfile.TemporaryDirectory(prefix='studio-pdf-check-') as temp:
    t = Path(temp)
    pages = t / 'pages'
    pages.mkdir()
    for i, color in enumerate(['white', 'pink', 'lightblue'], 1):
        Image.new('RGB', (300, 400), color).save(pages / f'{i:03}.png')
    before = t / 'before.pdf'
    after = t / 'after.pdf'
    repaired = t / 'repaired.pdf'
    linkmap = t / 'map.json'
    entries = [
        {'id': 'home', 'source_pages': 'all', 'rect': [.1, .1, .3, .2], 'destination_page': 1},
        {'id': 'next', 'source_pages': '1-2', 'rect': [200, 300, 290, 350], 'rect_units': 'pixels', 'destination_page': 'next'},
        {'id': 'previous', 'source_pages': [2, 3], 'rect': [10, 300, 90, 350], 'rect_units': 'pdf_points', 'destination_page': 'previous'},
    ]
    config = {'page_size_pixels': {'width': 300, 'height': 400}, 'links': entries}
    linkmap.write_text(json.dumps(config))
    run('build_pdf_from_images.py', '--input-dir', pages, '--output', before)
    run('hyperlink_planner_pdf.py', '--input', before, '--map', linkmap, '--output', after)
    run('inspect_pdf_links.py', '--input', after, '--report', t / 'report.json')
    run('hyperlink_planner_pdf.py', '--input', after, '--map', linkmap, '--output', repaired, '--replace-existing-links')
    with fitz.open(before) as b, fitz.open(after) as a, fitz.open(repaired) as c:
        check(len(a) == 3, 'Wrong assembled page count')
        check(sum(len(p.get_links()) for p in a) == 7, 'Wrong inserted link count')
        check(sum(len(p.get_links()) for p in c) == 7, 'Replacement duplicated links')
        expected_destinations = [[0, 1], [0, 2, 0], [0, 1]]
        for i in range(3):
            check([x['page'] for x in a[i].get_links()] == expected_destinations[i], f'Wrong destinations: page {i+1}')
            check(b[i].rect == a[i].rect == c[i].rect, 'Page dimensions changed')
            check(b[i].get_pixmap().samples == a[i].get_pixmap().samples == c[i].get_pixmap().samples, 'Artwork changed')
    for override in [{'destination_page': 99}, {'rect': [-1, 0, 1, 1]}]:
        config['links'] = [dict(entries[0], **override)]
        linkmap.write_text(json.dumps(config))
        run('hyperlink_planner_pdf.py', '--input', before, '--map', linkmap, '--output', t / 'bad.pdf', success=False)
        check(not (t / 'bad.pdf').exists(), 'Invalid map saved an output')
    run('inspect_pdf_links.py', '--input', before, success=False)
checks['pdf_fixture'] = '3 pages; 7 links; destinations, replacement, dimensions and pixel-identical renders checked; invalid maps and unlinked PDF rejected'
report = {'passed': not errors, 'checks': checks, 'modified_source_files': modified, 'errors': errors,
          'limits': ['Conceptual routing review is not a live model routing test.',
                     'Source mockup manifest.txt lists two historical excluded duplicate files absent from the uploaded archive; neither appears in the live retrieval index.',
                     'Source mockup metadata says three excluded duplicates; the supplied live index contains one excluded duplicate plus one interface screenshot. Source metadata preserved.',
                     'Private reference libraries retained locally; no public or customer archive created.',
                     'The supplied PDF inspector does not compare against an expected map or detect all ambiguous overlaps; the skill requires those additional QA checks.']}
(ROOT / 'docs/validation.json').write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps(report, indent=2))
sys.exit(bool(errors))
