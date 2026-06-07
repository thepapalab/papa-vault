import os
import re

directory = '.'
sections_dir = 'sections'

# List of files in document order
document_order = [
    'EC7-1_00_avant-propos.md',
    'EC7-1_1_generalites.md',
    'EC7-1_2_bases-calcul.md',
    'EC7-1_3_donnees-geotechniques.md',
    'EC7-1_4_surveillance-execution.md',
    'EC7-1_5_remblais-rabattement.md',
    'EC7-1_6_fondations-superficielles.md',
    'EC7-1_7a_fondations-pieux-generalites.md',
    'EC7-1_7b_fondations-pieux-calcul.md',
    'EC7-1_8_ancrages.md',
    'EC7-1_9_soutenement.md',
    'EC7-1_10_rupture-hydraulique.md',
    'EC7-1_11_stabilite-generale.md',
    'EC7-1_12_remblais.md',
    'EC7-1_A_facteurs-partiels.md',
    'EC7-1_B_facteurs-partiels-notes.md',
    'EC7-1_C_capacite-portante.md',
    'EC7-1_D_tassement-oedometre.md',
    'EC7-1_EF_resistance-pieux.md',
    'EC7-1_GH_resistance-lat-deform.md',
    'EC7-1_J_pressions-terres.md',
    'EC7-1_AC2009_corrigendum.md'
]

conversion_map = {
    'EC7-1_2_bases-calcul.md': 'EC7-1_2_bases-calcul.txt',
    'EC7-1_3_donnees-geotechniques.md': 'EC7-1_3_donnees-geotechniques.txt',
    'EC7-1_7a_fondations-pieux-generalites.md': 'EC7-1_7a_pieux-generalites-essais.txt',
    'EC7-1_7b_fondations-pieux-calcul.md': 'EC7-1_7b_pieux-calcul.txt',
    'EC7-1_8_ancrages.md': 'EC7-1_8_ancrages.txt',
    'EC7-1_9_soutenement.md': 'EC7-1_9_soutenement.txt',
    'EC7-1_10_rupture-hydraulique.md': 'EC7-1_10_rupture-hydraulique.txt',
    'EC7-1_11_stabilite-generale.md': 'EC7-1_11_stabilite-generale.txt',
    'EC7-1_12_remblais.md': 'EC7-1_12_remblais.txt',
    'EC7-1_AC2009_corrigendum.md': 'EC7-1_AC2009_corrigendum.txt',
    'EC7-1_EF_resistance-pieux.md': 'EC7-1_EF_resistance-pieux.txt',
    'EC7-1_GH_resistance-lat-deform.md': 'EC7-1_GH_resistance-lat-deform.txt',
    'EC7-1_J_pressions-terres.md': 'EC7-1_J_pressions-terres.txt'
}

watermark_pattern = re.compile(r'(SORBALAPAP|salociN|eb\.liarcut|\.LIAR|tnemucod|eriudorper|reilbup|ecnecil|égétorp|ruetua|stiord|elbinopsid|eriaropmet|etnenamrep|erdner)', re.IGNORECASE)

def clean_watermarks(text):
    # Instead of line by line, if we find a block with single words that match the pattern, we remove them
    lines = text.split('\n')
    out = []
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        # Look for a block of short lines matching watermarks
        if line and watermark_pattern.search(line):
            # check if it's part of a block
            j = i
            while j < len(lines) and len(lines[j].strip()) < 50:
                if watermark_pattern.search(lines[j].strip()) or lines[j].strip() in ('el', 'in', 'ne', 'uo', 'tios', 'nos', 'rap', 'suos', ''):
                    pass
                j += 1
            # Skip lines from i to j-1 if they look like watermark
            skip = False
            for k in range(i, min(j+10, len(lines))):
                 if watermark_pattern.search(lines[k]):
                     skip = True
                     break
            if skip:
                while i < len(lines) and (watermark_pattern.search(lines[i]) or len(lines[i].strip()) < 50 and lines[i].strip() != '' and not lines[i].startswith('#')):
                    i += 1
                continue
        # simple check
        if watermark_pattern.search(lines[i]):
            i += 1
            continue
            
        out.append(lines[i])
        i += 1
    return '\n'.join(out)

for i, target in enumerate(document_order):
    prev_file = document_order[i-1] if i > 0 else ""
    next_file = document_order[i+1] if i < len(document_order) - 1 else ""
    
    footer = f"Liens : [[EC7-1_index]]{' · [[' + prev_file.replace('.md', '') + ']]' if prev_file else ''}{' · [[' + next_file.replace('.md', '') + ']]' if next_file else ''} · [[_Knowledge — Index]] · [[CLAUDE]]"
    
    section_match = re.search(r'EC7-1_([0-9A-Z]+[a-z]?)_', target)
    section = section_match.group(1) if section_match else ""
    chapter_title = target.replace('.md', '').split('_', 2)[-1].replace('-', ' ').capitalize()
    
    frontmatter = f"""---
title: "NBN EN 1997-1:2005 — {chapter_title}"
type: norm-extract
source: "NBN EN 1997-1:2005"
norm: EC7-1
section: "{section}"
chapter: "{chapter_title}"
tags: [EC7-1, eurocode-7, geotechnique, {chapter_title.replace(' ', '')}]
related: ["[[EC7-1_index]]", "[[{prev_file.replace('.md', '')}]]", "[[{next_file.replace('.md', '')}]]", "[[_Knowledge — Index]]"]
created: 2026-06-06
---"""
    
    if target in conversion_map:
        # Convert new file
        txt_path = os.path.join(sections_dir, conversion_map[target])
        if os.path.exists(txt_path):
            with open(txt_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            content = clean_watermarks(content)
            
            # Ensure H1 exists
            h1_match = re.search(r'^#\s+', content, re.MULTILINE)
            if not h1_match:
                content = f"# NBN EN 1997-1:2005 — {chapter_title}\n\n" + content
                
            full_text = f"{frontmatter}\n\n{content.strip()}\n\n---\n\n{footer}\n"
            
            with open(target, 'w', encoding='utf-8') as f:
                f.write(full_text)
    else:
        # Update existing file
        if os.path.exists(target):
            with open(target, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Strip old footer
            content = re.sub(r'---\s+Liens.*$', '', content, flags=re.MULTILINE|re.DOTALL).strip()
            content = re.sub(r'---\s+Links.*$', '', content, flags=re.MULTILINE|re.DOTALL).strip()
            
            # Also fix frontmatter 'related' field to match correct prev/next
            content = re.sub(r'related:\s*\[.*?\]', f'related: ["[[EC7-1_index]]", "[[{prev_file.replace(".md", "")}]]", "[[{next_file.replace(".md", "")}]]", "[[_Knowledge — Index]]"]', content)
            
            full_text = f"{content}\n\n---\n\n{footer}\n"
            
            with open(target, 'w', encoding='utf-8') as f:
                f.write(full_text)

# Create Index
index_content = """---
title: "NBN EN 1997-1:2005 — Index"
type: index
source: "NBN EN 1997-1:2005"
norm: EC7-1
date: 2005-04
status: en vigueur
tags: [EC7-1, eurocode-7, index, geotechnique]
related: ["[[_Norms-Regulations — README]]", "[[_Knowledge — Index]]"]
created: 2026-06-06
---

# NBN EN 1997-1:2005 (Eurocode 7, Partie 1)

L'Eurocode 7 s'applique aux aspects géotechniques du calcul des bâtiments et des ouvrages de génie civil. La Partie 1 traite des règles générales.

> [!important] Utilisation Infrabel
> Voir PTR CE01 Chapitre 4 pour les prescriptions concernant l'application de l'Eurocode 7 pour les fondations et soutènements.

## Structure du document

| Fichier | Section | Titre |
|---------|---------|-------|
"""

for target in document_order:
    section_match = re.search(r'EC7-1_([0-9A-Z]+[a-z]?)_', target)
    section = section_match.group(1) if section_match else ""
    title = target.replace('.md', '').split('_', 2)[-1].replace('-', ' ').capitalize()
    index_content += f"| [[{target.replace('.md', '')}]] | {section} | {title} |\n"

index_content += """
## Paramètres clés

| Paramètre | Valeur | Article | Note |
|-----------|--------|---------|------|
| Facteurs partiels | Tableau A.1–A.14 ANB | Annexe A | Voir ANB |
| Approche de calcul | Approche 1 | ANB | Approche 1 en Belgique |

---

Liens : [[_Norms-Regulations — README]] · [[_Knowledge — Index]] · [[CLAUDE]]
"""

with open('EC7-1_index.md', 'w', encoding='utf-8') as f:
    f.write(index_content)

print("Done EC7-1")
import shutil
if os.path.exists('sections'):
    shutil.rmtree('sections')
