---
title: Norm Fix Tasks — Bringing all splits to PTR CE01 style
type: task-tracker
status: in-progress
created: 2026-06-06
---

# Norm Fix Tasks

## How to use this file (read this first)

You are an AI agent. Your job is to fix the split norm files in this vault so they all conform to the style standard described in `NORM-PROCESSING-AGENT.md` (same folder as this file).

**Before touching any file:**
1. Read `NORM-PROCESSING-AGENT.md` in full — it is the governing spec.
2. Study one PTR CE01 FR file for content/heading style: `Infrabel-PTR\FR\PTR CE01 — Ch03 — Actions — FR.md`
3. Study one well-done Eurocode index for index style: `Eurocodes-NBN\EC1\NBN EN 1991-1-4\EC1-1-4_index.md`
4. Note the footer format: `Liens : [[NORM_index]] · [[prev]] · [[next]] · [[_Knowledge — Index]] · [[CLAUDE]]`

**Working rules:**
- Tick each checkbox `- [x]` as soon as the task is done — before moving to the next one.
- Do not invent content. Fix formatting, frontmatter, and structure only unless a task explicitly says to create content from the raw source file.
- Raw source `.md` files (the OCR originals) are always present in the folder — read them when you need to create missing split files.
- After each norm is fully done, tick its top-level checkbox.
- The vault root is `C:\Users\n_pap\Documents\PapaLab\Papa_Vault\`
- All paths below are relative to `Knowledge\Norms-Regulations\`

---

## Standard checklist (apply to every file you touch)

These apply everywhere. Check each one for every file you create or edit.

| Check | Rule |
|-------|------|
| `type` | `norm-extract` for content, `index` for index. No other values. |
| Forbidden fields | Remove: `language`, `jupyter_ref`, `norms` (plural), `authority`, `sections` (list), processing artefacts |
| Footer language | `Liens :` — never `Links:` |
| Footer links | Content files: `[[NORM_index]] · [[prev]] · [[next]] · [[_Knowledge — Index]] · [[CLAUDE]]` |
| Index footer | `[[_Norms-Regulations — README]] · [[_Knowledge — Index]] · [[CLAUDE]]` |
| Wikilinks | Only link to files that actually exist |
| Index content | Opening paragraph + structure table + key params table. No ✅/pending/status trackers. |

---

## Priority 1 — Critical (structural problems)

### NBN EN 1992-1-1:2004 (EC2)
**Folder:** `NBN EN 1992-1-1 2004\`
**Raw source:** `NBN EN 1992-1-1 2004\NBN EN 1992-1-1_F.md` *(read it to understand what sections exist)*

The existing split is at the wrong granularity (individual clauses as separate files instead of full sections). The index is a work-tracker, not a vault index.

- [ ] **2-1. Rewrite the index** — Replace `EC2_index.md` entirely. It currently has no frontmatter and is a work-tracking document. Write a proper index with: YAML frontmatter (`type: index`, `norm: EC2`, correct `source`, `tags`, `related`, `created: 2026-06-06`), opening paragraph (3–5 sentences describing EC2 Part 1-1), optional Infrabel callout (PTR CE01 Chapter 5 governs EC2 use for Infrabel — you may add a brief `> [!important] Utilisation Infrabel` citing PTR CE01 §5.x), structure table listing the files that actually exist, key parameters table (partial factors γ_c, γ_s, α_cc, α_ct, f_ck classes), and correct footer.

- [ ] **2-2. Re-split at section level** — The ~180 sub-subsection files (e.g., `EC2_2.3.1.1_generalites-actions.md`, `EC2_2.3.1.2_effets-thermiques.md`, etc.) violate the minimum-granularity rule. Merge them into their parent section files. The correct output structure is:
  - `EC2_00_avant-propos.md` — Foreword
  - `EC2_1_generalites.md` — §1 (scope, references, definitions, symbols — all of §1)
  - `EC2_2_bases-calcul.md` — all of §2 (merge all the `EC2_2.x` files)
  - `EC2_3_materiaux.md` — all of §3
  - `EC2_4_durabilite-enrobage.md` — all of §4
  - `EC2_5_analyse-structurale.md` — all of §5 (may split as `5a`/`5b` if > 1500 lines; §5.1–5.7 and §5.8–5.11 is a natural break)
  - `EC2_6_elu.md` — all of §6
  - `EC2_7_els.md` — all of §7
  - `EC2_8_dispositions-armatures.md` — all of §8
  - `EC2_9_dispositions-elements.md` — all of §9
  - `EC2_10_elements-prefabriques.md` — all of §10
  - `EC2_11_beton-granulats-legers.md` — all of §11
  - `EC2_12_beton-non-arme.md` — all of §12
  - `EC2_A_coefficients-partiels.md` — Annex A
  - `EC2_B_fluage-retrait.md` — Annex B
  - `EC2_C_armatures.md` — Annex C
  - `EC2_D_relaxation.md` — Annex D
  - `EC2_E_durabilite.md` — Annex E
  - `EC2_FGHIJ_annexes-diverses.md` — Annexes F–J grouped (short annexes)
  - Read the raw source to fill in any section that currently has no MD file (§1, §3 partial, §4, §6, §7, §8, §11, annexes).
  - After creating section files, delete the hundreds of sub-subsection files.

- [ ] **2-3. Fix frontmatter on any retained files** — If any existing files survive the merge, add `type: norm-extract` and `created: 2026-06-06` where missing. Remove `language`, `jupyter_ref`.

- [ ] **2-4. Fix footers on all EC2 files** — Ensure every file (after the re-split) has the full 5-link footer in `Liens :` format.

- [ ] **2-5. Move to final location** — Once approved by user, the folder moves to `Eurocodes-NBN\EC2\NBN EN 1992-1-1 2004\`. Do not move it yourself — flag it in the §11 report as ready for user review.

---

### NBN EN 1997-1 (EC7-1)
**Folder:** `NBN EN 1997-1\`
**Raw source:** `NBN EN 1997-1\NBN EN 1997-1-2005-2_F.md`

Partial split: 9 sections exist as MD files, 8 sections exist only as `.txt` files in `sections\`, the index is missing entirely. A failed earlier attempt (`failed\` subfolder) uses a different naming convention.

- [ ] **7-1. Delete junk** — Delete the `failed\` subfolder entirely (it is a discarded earlier attempt). Delete `process_norm.py`. Do NOT delete the `sections\` subfolder yet — you need those `.txt` files.

- [ ] **7-2. Convert missing sections** — The following sections exist in `sections\` as `.txt` but have no corresponding `.md` file in the main folder. Convert each one to a proper split file using the existing naming convention (`EC7-1_N_slug.md`):
  - `EC7-1_2_bases-calcul.md` ← from `sections\EC7-1_2_bases-calcul.txt`
  - `EC7-1_3_donnees-geotechniques.md` ← from `sections\EC7-1_3_donnees-geotechniques.txt`
  - `EC7-1_7a_fondations-pieux-generalites.md` ← from `sections\EC7-1_7a_pieux-generalites-essais.txt`
  - `EC7-1_7b_fondations-pieux-calcul.md` ← from `sections\EC7-1_7b_pieux-calcul.txt`
  - `EC7-1_8_ancrages.md` ← from `sections\EC7-1_8_ancrages.txt`
  - `EC7-1_9_soutenement.md` ← from `sections\EC7-1_9_soutenement.txt`
  - `EC7-1_10_rupture-hydraulique.md` ← from `sections\EC7-1_10_rupture-hydraulique.txt`
  - `EC7-1_11_stabilite-generale.md` ← from `sections\EC7-1_11_stabilite-generale.txt`
  - `EC7-1_12_remblais.md` ← from `sections\EC7-1_12_remblais.txt`
  - `EC7-1_AC2009_corrigendum.md` ← from `sections\EC7-1_AC2009_corrigendum.txt`
  - `EC7-1_EF_resistance-pieux.md` ← from `sections\EC7-1_EF_resistance-pieux.txt`
  - `EC7-1_GH_resistance-lat-deform.md` ← from `sections\EC7-1_GH_resistance-lat-deform.txt`
  - `EC7-1_J_pressions-terres.md` ← from `sections\EC7-1_J_pressions-terres.txt`
  Each converted file needs: proper frontmatter (`type: norm-extract`, `norm: EC7-1`, `section`, `chapter`, `tags`, `related`, `created: 2026-06-06`), H1 matching the title, content cleaned of watermarks and page headers, and the standard footer.

- [ ] **7-3. Create the index** — Create `EC7-1_index.md` with the full structure (all 9 existing + 13 new files). Include opening paragraph describing EC7-1, Infrabel callout (PTR CE01 Chapter 4 references EC7 for foundations), structure table, key parameters table (facteurs partiels Tableau A.1–A.14 ANB, approche de calcul 1 Belgique), correct index footer.

- [ ] **7-4. Fix footers on existing files** — Files `EC7-1_00_avant-propos.md`, `EC7-1_1_generalites.md`, `EC7-1_4_surveillance-execution.md`, `EC7-1_5_remblais-rabattement.md`, `EC7-1_6_fondations-superficielles.md`, `EC7-1_A_facteurs-partiels.md`, `EC7-1_B_facteurs-partiels-notes.md`, `EC7-1_C_capacite-portante.md`, `EC7-1_D_tassement-oedometre.md`. Check each: `related` wikilinks to `[[EC7-1_index]]` will now work (index exists), but verify prev/next links are correct for new file order. Add `[[CLAUDE]]` to any footer missing it.

- [ ] **7-5. Delete `sections\` subfolder** — Only after all `.txt` files have been converted to `.md` files and verified.

---

## Priority 2 — Serious (missing files referenced in index)

### EC1-1-4 (NBN EN 1991-1-4:2005)
**Folder:** `Eurocodes-NBN\EC1\NBN EN 1991-1-4\`
**Raw source:** `Eurocodes-NBN\EC1\NBN EN 1991-1-4\NBN EN 1991-1-4-2005-2_F.md`

The index references 5 files that do not exist. All content file frontmatter and footers have minor defects.

- [ ] **1-4-1. Create 5 missing annex/appendix files** — The index table lists these but no files exist:
  - `EC1-1-4_Ea_detachement-tourbillonnaire.md` — Annex E.1 (vortex shedding)
  - `EC1-1-4_Eb_galop-divergence-flottement.md` — Annexes E.2–E.4 (galloping, divergence, flutter)
  - `EC1-1-4_F_dynamique.md` — Annex F (dynamic characteristics)
  - `EC1-1-4_Bibliographie.md` — Bibliography
  - `EC1-1-4_AC-2010.md` — Corrigendum AC:2010
  Read the raw source to extract this content. Apply standard frontmatter and footer.

- [ ] **1-4-2. Fix all content file frontmatter** — For every file in this folder except the index and raw source: add `type: norm-extract` where missing; remove `language: fr` and `jupyter_ref` fields.

- [ ] **1-4-3. Fix all content file footers** — Every content file footer must be: `Liens : [[EC1-1-4_index]] · [[PREV]] · [[NEXT]] · [[_Knowledge — Index]] · [[CLAUDE]]`. The avant-propos currently has only 2 links and uses `[[_Norms-Regulations — README]]` instead of prev/next. Fix all footers to the 5-link format.

- [ ] **1-4-4. Update index structure table** — After creating the 5 new files, verify the structure table in the index lists them correctly with accurate wikilinks.

---

### NBN EN 1991-2
**Folder:** `NBN EN 1991-2\`
**Raw source:** `NBN EN 1991-2\NBN EN 1991-2-2003-1_F.md`

Two annex files are missing. All footers use English `Links:`. No avant-propos file.

- [ ] **1-2-1. Create avant-propos file** — `NBN EN 1991-2 — S0 — Avant-Propos.md`. Extract from raw source. Standard frontmatter (`type: norm-extract`, `norm: EC1-2`, `section: "00"`) and footer.

- [ ] **1-2-2. Create 2 missing annex files** — Extract from raw source:
  - `NBN EN 1991-2 — Ann-A-D — Vehicules-Speciaux-Fatigue.md` — Annexes A–D
  - `NBN EN 1991-2 — Ann-E-H — Dynamique-Avancee.md` — Annexes E–H

- [ ] **1-2-3. Fix all footers** — Replace `Links:` with `Liens :` in every file. Add `· [[_Knowledge — Index]] · [[CLAUDE]]` to every content file footer that is missing them.

- [ ] **1-2-4. Fix frontmatter** — Remove `language: fr` and `jupyter_ref` from all content files. Fix `related` wikilink `[[PTR CE01 — Ch03 — Actions]]` → `[[PTR CE01 — Ch03 — Actions — FR]]`.

- [ ] **1-2-5. Update index** — Update structure table to include the new S0 avant-propos and correct annex wikilinks. Fix index footer: currently `Links:` → `Liens :`. Add `[[_Norms-Regulations — README]]` to the index footer.

---

## Priority 3 — Moderate (frontmatter and footer fixes, no missing files)

### EN 1990 A1
**Folder:** `Eurocodes-NBN\EC0\NBN EN 1990\`
**Files:** 5 content files + 1 index

- [x] **A1-1. Fix content file frontmatter** — In all content files (`EN 1990 A1 — 00` through `EN 1990 A1 — 04`):
  - Change `type: norm-guide` → `type: norm-extract`
  - Remove `norms:` (list) — replace with `norm: EN1990-A1`
  - Remove `authority:`
  - Remove `sections:` (list)
  - Keep `date:` only in the index, not in content files

- [x] **A1-2. Fix content file footers** — Each content file footer should be: `Liens : [[EN 1990 A1 — Index]] · [[PREV]] · [[NEXT]] · [[_Knowledge — Index]] · [[CLAUDE]]`. Currently footers have only 2 links. Add the missing links.

- [x] **A1-3. Fix index frontmatter** — Remove `norms:`, `authority:`. Add `norm: EN1990-A1`. Add `status: en vigueur`.

- [x] **A1-4. Fix index footer** — Currently: `Liens : [[_Norms-Regulations — README]] · [[PTR CE01 — Index — FR]] · [[_Knowledge — Index]]`. Add `· [[CLAUDE]]` at the end.

---

### EN 1990 ANB
**Folder:** `Eurocodes-NBN\EC0\NBN EN 1990 ANB\`
**Files:** 5 content files + 1 index

- [x] **ANB-1. Fix content file frontmatter** — Same pattern as EN 1990 A1:
  - Change `type: norm-guide` → `type: norm-extract`
  - Remove `norms:` → `norm: EN1990-ANB`
  - Remove `authority:`, `sections:` (list)

- [x] **ANB-2. Fix content file footers** — Each content file footer: `Liens : [[EN 1990 ANB — Index]] · [[PREV]] · [[NEXT]] · [[_Knowledge — Index]] · [[CLAUDE]]`. Add missing links.

- [x] **ANB-3. Fix index frontmatter** — Remove `norms:`, `authority:`. Add `norm: EN1990-ANB`. Add `status: en vigueur`.

- [x] **ANB-4. Fix index footer** — Add `· [[CLAUDE]]` to end of current footer.

---

### T7-FR-SpecificationBetons
**Folder:** `Concrete\T7-FR-SpecificationBetons\`
**Files:** 7 content files + 1 index

- [x] **T7-1. Fix content file frontmatter** — Change `type: norm-guide` → `type: norm-extract` in all content files.

- [x] **T7-2. Fix index `related` and footer** — Index `related` currently only has `[[_Knowledge — Index]]`; add `"[[_Norms-Regulations — README]]"`. Index footer currently `Liens : [[_Knowledge — Index]] · [[T7 — 03 — Comment Prescrire]]`; replace with `Liens : [[_Norms-Regulations — README]] · [[_Knowledge — Index]] · [[CLAUDE]]`.

- [x] **T7-3. Fix content file footers** — Verify every content file has `[[_Knowledge — Index]] · [[CLAUDE]]` in its footer. Add where missing.

---

### NBN EN 1992-1-1 ANB 2010
**Folder:** `NBN EN 1992-1-1 ANB 2010\`
**File:** `NBN EN 1992-1-1 ANB 2010.md` (single-file ANB — short enough to stay as one file per §9.7 of NORM-PROCESSING-AGENT.md)

- [x] **ANB2-1. Fix frontmatter** — Current `type: norm-reference` → `type: norm-extract`. Remove non-standard fields (`standard`, `norm-base`, `publication`). Add standard fields: `norm: EC2-ANB`, `section: "ANB"`, `related: ["[[EC2_index]]", "[[_Knowledge — Index]]"]`.

- [x] **ANB2-2. Add footer** — File currently has no footer. Add: `Liens : [[EC2_index]] · [[_Knowledge — Index]] · [[CLAUDE]]`

---

## Priority 4 — Not yet split (awaiting processing)

These are raw OCR source files that have not been split at all. The agent should process them fresh using NORM-PROCESSING-AGENT.md §2–§11.

### NBN EN 1991-1-1
**Folder:** `NBN EN 1991-1-1\`
**Raw source:** `NBN EN 1991-1-1\NBN EN 1991-1-1-2002-1_F.md`
**Target naming:** `EC1-1-1_NN_slug.md`

- [ ] **1-1-1. Full processing** — Run the complete NORM-PROCESSING-AGENT.md workflow (§2 assess → §3 watermarks → §4 split plan → §5–§9 write files → §10 self-check → §11 report). Flag for user review when done.

---

### NBN EN 1992-2
**Folder:** `NBN EN 1992-2\`
**Raw source:** `NBN EN 1992-2\NBN EN 1992-2-2005-2_F.md`
**Target naming:** `EC2-2_NN_slug.md`

- [ ] **1-2-2. Full processing** — Same as above.

---

### NBN EN 1997-1 A1:2014
**Folder:** `NBN EN 1997-1_A1-2014-1_F\`
**Raw source:** `NBN EN 1997-1_A1-2014-1_F\NBN EN 1997-1_A1-2014-1_F.md`

This is a short amendment. Per §9.7 of NORM-PROCESSING-AGENT.md, keep as a single file — do NOT create a separate index.

- [ ] **A1-2014-1. Format as single-file norm** — Rewrite the raw file in place with proper frontmatter (`type: norm-extract`, `norm: EC7-1-A1`, `section: "A1"`, `related: ["[[EC7-1_index]]", "[[_Knowledge — Index]]"]`) and footer. Clean watermarks. Keep content verbatim.

---

## Completion status

| Norm | Status | Last touched |
|------|--------|-------------|
| NBN EN 1992-1-1 2004 | ⬜ Todo | — |
| NBN EN 1997-1 | ⬜ Todo | — |
| EC1-1-4 | ⬜ Todo | — |
| NBN EN 1991-2 | ⬜ Todo | — |
| EN 1990 A1 | ✅ Done | 2026-06-06 |
| EN 1990 ANB | ✅ Done | 2026-06-06 |
| T7-FR | ✅ Done | 2026-06-06 |
| NBN EN 1992-1-1 ANB 2010 | ✅ Done | 2026-06-06 |
| NBN EN 1991-1-1 | ⬜ Todo | — |
| NBN EN 1992-2 | ⬜ Todo | — |
| NBN EN 1997-1 A1:2014 | ⬜ Todo | — |

Update the status column as you work: ⬜ Todo → 🔄 In progress → ✅ Done.

---

Liens : [[_Norms-Regulations — README]] · [[_Knowledge — Index]] · [[CLAUDE]]
