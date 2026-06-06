---
title: Norm Processing — Agent Instructions
type: agent-instructions
status: living
created: 2026-06-06
---

# Norm Processing — Agent Instructions

Instructions for an AI agent to convert a raw PDF-to-markdown norm file into clean, split, Obsidian-ready notes. Written for use with a lightweight model (Haiku). Read this file in full before starting any work.

---

## 0. Context

**Vault location:** `C:\Users\n_pap\Documents\PapaLab\Papa_Vault\`
**Work area:** `Knowledge\Norms-Regulations\` — where raw MD files land and are split.
**Final destination:** `Knowledge\Norms-Regulations\Eurocodes-NBN\EC[N]\[NORM]\` — where finished folders are moved *by the user* after review.

**Gold-standard reference:** `Knowledge\Norms-Regulations\Infrabel-PTR\FR\` (PTR CE01 folder). Study this before proceeding if uncertain about content structure and heading style.

**Important limitation of the PTR CE01 reference:** PTR CE01 content files were produced before this spec was finalised. Two known deviations from the current spec: (1) PTR CE01 content files are missing `[[CLAUDE]]` in their footers — the current spec requires it in all footers; (2) PTR CE01 uses `chapters` instead of `section` in frontmatter — use `section` for all new files. In all other respects, PTR CE01 is the model.

**Additional examples:**
- `Knowledge\Norms-Regulations\Eurocodes-NBN\EC1\NBN EN 1991-1-4\` — EC1 wind norm
- `Knowledge\Norms-Regulations\Eurocodes-NBN\EC0\NBN EN 1990 ANB\` — ANB norm
- `Knowledge\Norms-Regulations\Concrete\T7-FR-SpecificationBetons\` — FEBELCEM bulletin

---

## 1. Task triggers

You are invoked in one of three situations:

**A — Fresh norm:** A raw MD file exists in a folder under `Norms-Regulations\` with no split files alongside it. Process it fully (Steps 2–8).

**B — Incomplete split:** A folder exists with some split files but the work was stopped or is wrong. Assess what is done, what is missing or incorrect, and complete/correct it without redoing good work.

**C — Resume or fix:** The user describes a specific problem (wrong structure, missing chapter, bad frontmatter). Read the existing files, identify the gap, fix only what is broken.

When invoked, first scan the target folder to determine which situation applies. State your assessment in one sentence before proceeding.

---

## 2. Assess the source file

Read the raw MD file. Establish:

1. **Norm identity** — full reference code (e.g., `NBN EN 1991-1-4:2005`), title, date, language, what it replaces.
2. **Structure** — list of chapters/sections/annexes in document order.
3. **Split plan** — decide which sections group into which output file (see §4 for splitting rules).
4. **Estimated file count** — chapter files + index file.

Output your split plan as a table before writing any file:

| File name | Sections covered | Key content |
|-----------|-----------------|-------------|
| … | … | … |

Do not write any file until this plan is stated.

---

## 3. Remove watermarks

Watermarks appear as blocks of single words or short fragments per line — OCR'd text from a rotated/mirrored stamp in the PDF. They are **not part of the normative content** and must be deleted entirely.

**Recognition pattern — delete any block that matches these signals:**

- Contains `SORBALAPAP` or `salociN` or `eb.liarcut` (the user's email reversed)
- Contains `.LIAR` (= RAIL reversed)
- Single-word lines that are reversed French: `tnemucod`, `eriudorper`, `reilbup`, `ecnecil`, `égétorp`, `ruetua`, `stiord`, `elbinopsid`, `eriaropmet`, `etnenamrep`, `erdner`
- Fragments like `el`, `in`, `ne`, `uo`, `tios`, `nos`, `rap`, `suos` appearing as isolated single-line entries between otherwise normal paragraphs

The block typically spans 15–30 lines. Delete the entire block, leaving no blank lines in its place (one blank line max between adjacent content blocks). Also remove the header watermark lines that precede the actual content on each page (ICS codes, NBN publication details in multiple languages) when they repeat — keep only the first occurrence at the top of the source if it provides norm identification; remove all subsequent repeats mid-document.

---

## 4. Splitting rules

**Principle:** each output file must be usable standalone when retrieved by an LLM. Keep related content together; avoid files smaller than ~200 words or larger than ~1500 lines.

**Standard groupings:**
- Avant-propos / Foreword → file `00`
- Chapter 1 (Généralités / Scope) alone or with Chapter 2 if both are short
- Each substantial chapter gets its own file
- Long chapters (e.g., Section 7 with sub-parts) may be split by sub-section: `7a`, `7b`, `7c`
- Each lettered Annex gets its own file (A, B, C…) unless trivially short (< 1 page), in which case group two together
- Bibliographie → last file or merged with final annex
- Corrigenda / Amendments → separate file if substantial

**Do not** create a file for a section that is just a title with one sentence; merge it into the adjacent file.

---

## 5. File naming convention

**Chapter/section files:**

```
[NORM-CODE]_[NN]_[topic-slug].md
```

Examples:
- `EC1-1-4_00_avant-propos.md`
- `EC1-1-4_4_vitesse-pression.md`
- `EC1-1-4_7a_generalites-batiments.md`
- `EC1-1-4_A_effets-terrain.md`

For multi-chapter files use: `EC1-1-4_7b_toitures-isolees-murs.md`

**Index file:**

```
[NORM-CODE]_index.md
```

Example: `EC1-1-4_index.md`

**Slug rules:** lowercase, hyphens only, no accents, no spaces, max 40 chars. Use the French title of the section/chapter as the base.

**If the norm already has files with a different naming pattern** (e.g., `PTR CE01 — Ch01 — Title — FR.md`), maintain that existing pattern for consistency — do not mix conventions within a folder.

**Splitting granularity limit** — never create a file for a single sub-subsection or individual clause. The minimum useful file covers a full numbered section (e.g., all of §3.1) or a coherent group of clauses. A file smaller than ~300 words is always wrong. When in doubt, merge upward, not downward.

---

## 6. Frontmatter for chapter files

Every chapter/section file starts with this frontmatter block:

```yaml
---
title: "[NORM full ref] — [Section descriptor]"
type: norm-extract
source: "[Full norm title with year and language edition]"
norm: [short code, e.g. EC1-1-4]
section: "[NN or letter, e.g. 4 or A]"
chapter: "[Title of the section in the document's language]"
tags: [norm-code, eurocode-N, topic-slug, …]
related: ["[[NORM_index]]", "[[adjacent-file]]", "[[_Knowledge — Index]]"]
created: [today's date YYYY-MM-DD]
---
```

Rules:
- `type` is always `norm-extract` for content files, `index` for the index file. **No other values are permitted** — never use `norm-guide`, `norm-reference`, or any other variant.
- `related` must include the index wikilink and at minimum the immediately adjacent files (prev/next). **Only link to files that actually exist**; do not pre-populate wikilinks for files not yet created.
- Tags: always include the norm code slug, the eurocode family (e.g. `eurocode-1`, `eurocode-2`), and 2–4 topic keywords from the section content.
- Do not add `language` unless the vault holds parallel FR/NL/EN versions of the same norm.
- **Forbidden frontmatter fields** — do NOT add any of the following; they are non-standard and pollute the vault schema:
  - `language` (except as noted above)
  - `jupyter_ref`
  - `norms` (plural) — use `norm` (singular, short code)
  - `authority`
  - `sections` (as a list)
  - `status` (in content files — only the index file may have `status: en vigueur`)
  - Processing artefacts: `processing_mode`, `last_updated`, etc.

---

## 7. Content formatting rules

Apply these rules to all content inside chapter files.

### 7.1 Headings

- Document title → `# H1` (one per file, matches the `title` frontmatter)
- Chapter title → `## H2`
- Section title → `### H3`
- Sub-section title → `#### H4`
- Do not go deeper than H4; if the document has 5+ heading levels, flatten the deepest two.
- Remove numbering artifacts from OCR (e.g., `1 .1` → `### 1.1`) and normalise spacing.

### 7.2 Mathematics

Convert all inline and block equations to LaTeX:

- Inline: `$symbol = value$` — use for simple variable references and short expressions.
- Block (display): `$$...$$` — use for full equations, formula chains, and any equation that has a fraction, integral, sum, or subscript/superscript combination.
- Greek letters: always use LaTeX commands (`\gamma`, `\sigma`, `\psi`, etc.) — never write `γ` or `σ` as Unicode in equations.
- Units: write inline without LaTeX unless part of a formula (e.g., `c_s·c_d = 1,0` for body text, `$$F_w = \frac{1}{2}\rho v_b^2$$` for formulas).
- Decimal separator: keep the document's convention (comma for French norms).

### 7.3 Tables

Preserve all tables. Convert to Markdown table format if they are not already. Rules:
- Bold the header row.
- Align numeric columns right (add `:` on right side of separator).
- If a table cell contains a formula, use inline LaTeX.
- Do not split a table across files; if a table spans a chapter boundary, include it in the file where it logically belongs and add a cross-reference in the other file.
- If an OCR table is badly broken (merged cells, missing separators), reconstruct it faithfully — do not simplify or omit rows.

### 7.4 Notes, warnings, and informative clauses

Use Obsidian callout syntax:
- Normative requirements: plain text (no callout needed).
- `NOTE` clauses from the norm: `> [!note] NOTE [N]`
- `[!important]`: reserve for PTR CE01 prescriptions or ANB values that override EN defaults — use sparingly.
- Informative annexes: add `> *Annexe informative*` as the first line of the annex section.

### 7.5 Original text

**Do not paraphrase, summarize, or translate.** Copy the normative text verbatim. You may:
- Fix obvious OCR errors (broken words, missing spaces, scrambled letters) where the correct text is unambiguous.
- Remove repeated headers/footers that appear mid-document (page headers like the norm reference and page number — these are OCR artefacts).
- Correct paragraph breaks broken mid-sentence by the OCR.

**Do not** add explanatory comments, editorial notes, or any text that is not in the original document — unless it is an Obsidian navigation link in the footer (§8).

### 7.6 Lists

Preserve bullet and numbered lists. Restore list hierarchy broken by OCR. Each list item on its own line; one blank line between the introducing paragraph and the list.

---

## 8. Navigation footer

Every file (including the index) ends with a footer line:

```
---

Liens : [[NORM_index]] · [[prev-file]] · [[next-file]] · [[_Knowledge — Index]] · [[CLAUDE]]
```

- First link always points to the norm's index file.
- `prev-file` and `next-file` are the adjacent chapter files in document order (omit if there is no prev/next).
- `[[_Knowledge — Index]]` and `[[CLAUDE]]` are always included.
- **Use `Liens :` (French) always — never `Links:` (English).**
- **`[[CLAUDE]]` is mandatory in every footer without exception**, including content files. (Note: some older PTR CE01 content files lack this — they predate the current spec and are not the model for footer format.)

---

## 9. The index file

The index file is the entry point for the norm. It must contain:

### 9.1 Frontmatter

```yaml
---
title: "[Full norm ref] — Index"
type: index
source: "[Full norm title, publisher, year, language]"
norm: [short code]
date: [norm publication date YYYY-MM]
replaces: "[Previous norm(s) this replaces, if stated]"
status: en vigueur
tags: [norm-code, eurocode-N, index, topic-keywords]
related: ["[[_Norms-Regulations — README]]", "[[_Knowledge — Index]]"]
created: [today's date YYYY-MM-DD]
---
```

### 9.2 Opening paragraph

One paragraph describing what the norm covers, who it applies to, and its relationship to the Belgian ANB (if applicable). 3–5 sentences. This is the only place where you write a short synthesis — keep it factual.

**The index must describe the completed state only** — no status trackers (✅, ⚠️, "Pending"), no processing notes, no "Next Steps" sections. If the split is incomplete, complete it before writing the index, or write an honest incomplete note in the §11 report but keep the index itself clean.

### 9.3 Infrabel note (if applicable)

If the norm is referenced in PTR CE01, add:

```markdown
> [!important] Utilisation Infrabel
> [One or two sentences from PTR CE01 specifying how this norm is applied — cite the PTR article.]
```

If you do not know the PTR CE01 reference, omit this block entirely. Do not invent content.

### 9.4 Structure table

A table listing every split file:

| Fichier | Section | Titre |
|---------|---------|-------|
| [[filename]] | 0 | Avant-propos |
| [[filename]] | 1 | … |

Bold any section that is the primary engineering content (e.g., the bridge section in a wind norm).

### 9.5 Key parameters table (where applicable)

For norms that define numerical parameters (partial factors, coefficients, NDP values), add a table:

| Paramètre | Valeur | Article | Note |
|-----------|--------|---------|------|
| … | … | … | NDP / Belgian ANB to check |

Extract these directly from the norm content. Mark NDP parameters explicitly.

### 9.6 Navigation footer

Same format as §8 but no prev/next (index has none):

```
---

Liens : [[_Norms-Regulations — README]] · [[_Knowledge — Index]] · [[CLAUDE]]
```

---

## 9.7 Short norms and single-file ANBs

A short norm (< 5 printed pages, typically a national annex or corrigendum) need not be split into chapter files. Treat the entire document as a single content file with `type: norm-extract`. Give it proper frontmatter, an appropriate H1, and the standard footer. Do NOT create a separate index file — the single file IS the entry point. Reference it from the parent norm's index via a wikilink.

---

## 10. Self-check before reporting done

Before declaring the work complete, verify:

- [ ] Every section of the source document is covered by exactly one split file (no gaps, no duplicates).
- [ ] All watermark blocks removed — search for `SORBALAPAP` or `tnemucod` in output files; if found, remove.
- [ ] Every split file has valid frontmatter with all required fields.
- [ ] All equations use LaTeX (`$` or `$$`); no bare Unicode math symbols inside equations.
- [ ] All tables render as valid Markdown tables (pipe-delimited, header separator present).
- [ ] Every file has a navigation footer.
- [ ] Index file exists with structure table linking to every split file.
- [ ] Wikilinks in `related` and footers match the actual file names exactly (Obsidian wikilinks are case-sensitive on some systems — match case exactly).
- [ ] No file is empty or contains only frontmatter.
- [ ] Source raw file is still present (do not delete it).

---

## 11. Reporting

When done, output a concise summary:

```
Norm: [full reference]
Files created: N (list them)
Sections: [which sections map to which file]
Issues found and resolved: [any OCR problems fixed, any ambiguous splits made]
Ready for review: yes
```

Do not output the full content of files in the summary — just the file list and any decisions that required judgment.

---

## 12. Half-baked folder recovery

If you are asked to assess or fix an existing split:

1. Read the index file (if it exists) to understand the intended structure.
2. Read each existing split file and check it against the self-check list (§10).
3. Read the source raw file to identify what is missing or wrongly split.
4. List what is wrong before making any changes.
5. Fix only what is broken; do not rewrite files that pass the self-check.
6. Update the index if files were added, removed, or renamed.

---

## 13. Quick-reference: folder layout after completion

```
Norms-Regulations\
└── [NORM-FOLDER]\              ← work area (stays here until user moves it)
    ├── [RAW-SOURCE].md         ← original, untouched
    ├── [CODE]_index.md         ← index (entry point)
    ├── [CODE]_00_avant-propos.md
    ├── [CODE]_1_generalites.md
    ├── [CODE]_2_….md
    └── …
```

After the user approves, they move `[NORM-FOLDER]\` to:
```
Norms-Regulations\Eurocodes-NBN\EC[N]\[NORM]\
```

The raw source file stays in the folder when moved.
