import os
import re

directory = '.'
raw_file = 'NBN EN 1991-1-4-2005-2_F.md'

with open(raw_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()

def clean_watermarks(lines_list):
    text = "".join(lines_list)
    # Basic watermark cleanup
    pattern = re.compile(r'(SORBALAPAP|salociN|eb\.liarcut|\.LIAR|tnemucod|eriudorper|reilbup|ecnecil|égétorp|ruetua|stiord|elbinopsid|eriaropmet|etnenamrep|erdner)', re.IGNORECASE)
    lines = text.split('\n')
    out = []
    for line in lines:
        if pattern.search(line):
            continue
        if len(line.strip()) < 5 and line.strip() in ('el', 'in', 'ne', 'uo', 'tios', 'nos', 'rap', 'suos'):
            continue
        out.append(line)
    return '\n'.join(out)

Ea_lines = lines[8396:9354]
Eb_lines = lines[9354:9757]
F_lines = lines[9757:10557]
biblio_lines = lines[10557:10641]
ac2010_lines = lines[10641:]

new_files = {
    'EC1-1-4_Ea_detachement-tourbillonnaire.md': {
        'title': 'Détachement tourbillonnaire',
        'section': 'E.1',
        'content': clean_watermarks(Ea_lines)
    },
    'EC1-1-4_Eb_galop-divergence-flottement.md': {
        'title': 'Galop divergence et flottement',
        'section': 'E.2',
        'content': clean_watermarks(Eb_lines)
    },
    'EC1-1-4_F_dynamique.md': {
        'title': 'Caractéristiques dynamiques des structures',
        'section': 'F',
        'content': clean_watermarks(F_lines)
    },
    'EC1-1-4_Bibliographie.md': {
        'title': 'Bibliographie',
        'section': 'Bib',
        'content': clean_watermarks(biblio_lines)
    },
    'EC1-1-4_AC-2010.md': {
        'title': 'Corrigendum AC:2010',
        'section': 'AC',
        'content': clean_watermarks(ac2010_lines)
    }
}

file_order = [
    'EC1-1-4_00_avant-propos.md',
    'EC1-1-4_1_generalites.md',
    'EC1-1-4_2_situations-projet.md',
    'EC1-1-4_3_modelisation.md',
    'EC1-1-4_4_vitesse-pression.md',
    'EC1-1-4_5_actions-vent.md',
    'EC1-1-4_6_coefficient-cscd.md',
    'EC1-1-4_7a_generalites-batiments.md',
    'EC1-1-4_7b_toitures-isolees-murs.md',
    'EC1-1-4_7c_elements-structuraux.md',
    'EC1-1-4_8_actions-ponts.md',
    'EC1-1-4_A_effets-terrain.md',
    'EC1-1-4_B_procedure1-cscd.md',
    'EC1-1-4_C_procedure2-cscd.md',
    'EC1-1-4_D_valeurs-cscd.md',
    'EC1-1-4_Ea_detachement-tourbillonnaire.md',
    'EC1-1-4_Eb_galop-divergence-flottement.md',
    'EC1-1-4_F_dynamique.md',
    'EC1-1-4_Bibliographie.md',
    'EC1-1-4_AC-2010.md'
]

# Generate/update files
for i, filename in enumerate(file_order):
    prev_file = file_order[i-1].replace('.md', '') if i > 0 else ""
    next_file = file_order[i+1].replace('.md', '') if i < len(file_order) - 1 else ""
    
    footer = f"Liens : [[EC1-1-4_index]]{' · [[' + prev_file + ']]' if prev_file else ''}{' · [[' + next_file + ']]' if next_file else ''} · [[_Knowledge — Index]] · [[CLAUDE]]"
    
    if filename in new_files:
        info = new_files[filename]
        frontmatter = f"""---
title: "NBN EN 1991-1-4:2005 — {info['title']}"
type: norm-extract
source: "NBN EN 1991-1-4:2005"
norm: EC1-1-4
section: "{info['section']}"
chapter: "{info['title']}"
tags: [EC1-1-4, eurocode-1, vent]
related: ["[[EC1-1-4_index]]", "[[{prev_file}]]", "[[{next_file}]]", "[[_Knowledge — Index]]"]
created: 2026-06-06
---"""
        full_text = f"{frontmatter}\n\n{info['content'].strip()}\n\n---\n\n{footer}\n"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(full_text)
    else:
        # Existing file update
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Remove jupyter_ref and language: fr
            content = re.sub(r'^jupyter_ref:.*?\n', '', content, flags=re.MULTILINE)
            content = re.sub(r'^language:\s*fr\s*\n', '', content, flags=re.MULTILINE)
            # Make sure type is norm-extract
            content = re.sub(r'^type:\s*.*?\n', 'type: norm-extract\n', content, flags=re.MULTILINE)
            
            # strip old footer
            content = re.sub(r'---\s+Liens.*$', '', content, flags=re.MULTILINE|re.DOTALL).strip()
            content = re.sub(r'---\s+Links.*$', '', content, flags=re.MULTILINE|re.DOTALL).strip()
            
            # Update related
            content = re.sub(r'^related:\s*\[.*?\]', f'related: ["[[EC1-1-4_index]]", "[[{prev_file}]]", "[[{next_file}]]", "[[_Knowledge — Index]]"]', content, flags=re.MULTILINE)
            
            full_text = f"{content}\n\n---\n\n{footer}\n"
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(full_text)

# Update the index file
index_path = 'EC1-1-4_index.md'
if os.path.exists(index_path):
    with open(index_path, 'r', encoding='utf-8') as f:
        idx_content = f.read()

    # Create new structure table
    structure = "## Structure du document\n\n| Fichier | Section | Titre |\n|---------|---------|-------|\n"
    for f in file_order:
        sec_match = re.search(r'EC1-1-4_([0-9A-Za-z]+)_', f)
        sec = sec_match.group(1) if sec_match else ""
        title = f.replace('.md', '').split('_', 2)[-1].replace('-', ' ').capitalize()
        structure += f"| [[{f.replace('.md', '')}]] | {sec} | {title} |\n"

    # Replace old structure table
    idx_content = re.sub(r'## Structure du document.*?##', structure + '\n##', idx_content, flags=re.DOTALL)
    
    # Fix the footer of index
    idx_content = re.sub(r'---\s+Links.*$', '', idx_content, flags=re.MULTILINE|re.DOTALL).strip()
    idx_content = re.sub(r'---\s+Liens.*$', '', idx_content, flags=re.MULTILINE|re.DOTALL).strip()
    idx_content += f"\n\n---\n\nLiens : [[_Norms-Regulations — README]] · [[_Knowledge — Index]] · [[CLAUDE]]\n"
    
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(idx_content)

print("Done EC1-1-4")
