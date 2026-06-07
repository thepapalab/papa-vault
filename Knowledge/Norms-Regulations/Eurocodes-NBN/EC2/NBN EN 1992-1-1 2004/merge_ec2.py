import os
import re
from datetime import datetime

directory = '.'

# Define target files and the prefixes of the source files that should be merged into them
merges = {
    'EC2_00_avant-propos.md': ['EC2_00_avant-propos.md'],
    'EC2_1_generalites.md': [f'EC2_1.{i}' for i in range(1, 10)] + ['EC2_1_'],
    'EC2_2_bases-calcul.md': [f'EC2_2.{i}' for i in range(1, 10)] + ['EC2_2_'],
    'EC2_3_materiaux.md': [f'EC2_3.{i}' for i in range(1, 10)] + ['EC2_3_'],
    'EC2_4_durabilite-enrobage.md': [f'EC2_4.{i}' for i in range(1, 10)] + ['EC2_4_'],
    'EC2_5_analyse-structurale.md': [f'EC2_5.{i}' for i in range(1, 20)] + ['EC2_5_'],
    'EC2_6_elu.md': [f'EC2_6.{i}' for i in range(1, 10)] + ['EC2_6_'],
    'EC2_7_els.md': [f'EC2_7.{i}' for i in range(1, 10)] + ['EC2_7_'],
    'EC2_8_dispositions-armatures.md': [f'EC2_8.{i}' for i in range(1, 20)] + ['EC2_8_'],
    'EC2_9_dispositions-elements.md': [f'EC2_9.{i}' for i in range(1, 10)] + ['EC2_9_'],
    'EC2_10_elements-prefabriques.md': [f'EC2_10.{i}' for i in range(1, 10)] + ['EC2_10_'],
    'EC2_11_beton-granulats-legers.md': [f'EC2_11.{i}' for i in range(1, 20)] + ['EC2_11_'],
    'EC2_12_beton-non-arme.md': [f'EC2_12.{i}' for i in range(1, 20)] + ['EC2_12_'],
    'EC2_A_coefficients-partiels.md': ['EC2_A.'],
    'EC2_B_fluage-retrait.md': ['EC2_B.'],
    'EC2_C_armatures.md': ['EC2_C.'],
    'EC2_D_relaxation.md': ['EC2_D.'],
    'EC2_E_durabilite.md': ['EC2_E.'],
    'EC2_FGHIJ_annexes-diverses.md': ['EC2_F.', 'EC2_G.', 'EC2_H.', 'EC2_I.', 'EC2_J.']
}

all_files = [f for f in os.listdir(directory) if f.endswith('.md') and f != 'EC2_index.md' and f != 'merge_ec2.py']

def extract_content(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    # Strip frontmatter
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            content = parts[2].strip()
    # Strip old footer
    content = re.sub(r'---\s+Liens.*$', '', content, flags=re.MULTILINE|re.DOTALL).strip()
    content = re.sub(r'---\s+Links.*$', '', content, flags=re.MULTILINE|re.DOTALL).strip()
    return content

files_to_delete = []

ordered_targets = list(merges.keys())

for idx, target in enumerate(ordered_targets):
    prefixes = merges[target]
    source_files = []
    for f in all_files:
        for p in prefixes:
            if f.startswith(p):
                source_files.append(f)
                break
    
    # Sort files naturally
    import re as regex
    def sort_key(s):
        return [int(text) if text.isdigit() else text.lower() for text in regex.split('([0-9]+)', s)]
    source_files.sort(key=sort_key)
    
    if not source_files:
        continue
        
    merged_content = []
    for sf in source_files:
        merged_content.append(extract_content(os.path.join(directory, sf)))
        if sf != target:
            files_to_delete.append(sf)
            
    # Compute prev/next
    prev_file = ordered_targets[idx-1] if idx > 0 else ""
    next_file = ordered_targets[idx+1] if idx < len(ordered_targets)-1 else ""
    
    section_match = re.search(r'EC2_([0-9A-Z]+)_', target)
    section = section_match.group(1) if section_match else "00"
    
    chapter_title = target.replace('.md', '').split('_', 2)[-1].replace('-', ' ').capitalize()
    
    # Write new file
    frontmatter = f"""---
title: "NBN EN 1992-1-1:2004 — {chapter_title}"
type: norm-extract
source: "NBN EN 1992-1-1:2004"
norm: EC2
section: "{section}"
chapter: "{chapter_title}"
tags: [EC2, eurocode-2, {target.replace('.md', '').split('_', 2)[-1]}]
related: ["[[EC2_index]]", "[[{prev_file}]]", "[[{next_file}]]", "[[_Knowledge — Index]]"]
created: 2026-06-06
---

"""
    
    footer = f"""

---

Liens : [[EC2_index]]{' · [[' + prev_file + ']]' if prev_file else ''}{' · [[' + next_file + ']]' if next_file else ''} · [[_Knowledge — Index]] · [[CLAUDE]]
"""
    
    with open(os.path.join(directory, target), 'w', encoding='utf-8') as f:
        f.write(frontmatter + "\n\n".join(merged_content) + footer)

# Delete small files
for f in set(files_to_delete):
    if os.path.exists(os.path.join(directory, f)):
        os.remove(os.path.join(directory, f))

# Also delete some specific unneeded ones
unneeded = ['EC2_ANNEXES_A-B_index.md', 'EC2_ANNEXES_C-J_index.md', 'EC2_choix-nationaux.md']
for f in unneeded:
    if os.path.exists(os.path.join(directory, f)):
        os.remove(os.path.join(directory, f))

# Rewrite the index
index_content = """---
title: "NBN EN 1992-1-1:2004 — Index"
type: index
source: "NBN EN 1992-1-1:2004"
norm: EC2
date: 2004-12
status: en vigueur
tags: [EC2, eurocode-2, index, beton]
related: ["[[_Norms-Regulations — README]]", "[[_Knowledge — Index]]"]
created: 2026-06-06
---

# NBN EN 1992-1-1:2004 (Eurocode 2, Partie 1-1)

L'Eurocode 2 s'applique au calcul des bâtiments et des ouvrages de génie civil en béton non armé, en béton armé ou en béton précontraint. La Partie 1-1 traite des règles générales et des règles pour les bâtiments. 

> [!important] Utilisation Infrabel
> Voir PTR CE01 Chapitre 5 pour les prescriptions spécifiques à Infrabel concernant l'application de l'Eurocode 2.

## Structure du document

| Fichier | Section | Titre |
|---------|---------|-------|
"""

for target in ordered_targets:
    if os.path.exists(os.path.join(directory, target)):
        section_match = re.search(r'EC2_([0-9A-Z]+)_', target)
        section = section_match.group(1) if section_match else ""
        title = target.replace('.md', '').split('_', 2)[-1].replace('-', ' ').capitalize()
        index_content += f"| [[{target.replace('.md', '')}]] | {section} | {title} |\n"

index_content += """
## Paramètres clés

| Paramètre | Valeur | Article | Note |
|-----------|--------|---------|------|
| $\gamma_c$ | 1,50 | 2.4.2.4 | Coefficient partiel pour le béton |
| $\gamma_s$ | 1,15 | 2.4.2.4 | Coefficient partiel pour l'acier |
| $\\alpha_{cc}$ | 1,00 | 3.1.6 | Coefficient pour la résistance en compression |
| $\\alpha_{ct}$ | 1,00 | 3.1.6 | Coefficient pour la résistance en traction |

---

Liens : [[_Norms-Regulations — README]] · [[_Knowledge — Index]] · [[CLAUDE]]
"""

with open(os.path.join(directory, 'EC2_index.md'), 'w', encoding='utf-8') as f:
    f.write(index_content)

print("Done processing EC2")
