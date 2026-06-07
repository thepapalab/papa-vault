---
title: Norm Processing — Agent Instructions
type: agent-instructions
status: living
created: 2026-06-06
updated: 2026-06-07
---

# Norm Processing — Agent Instructions

Instructions for splitting a clean markdown norm file into chapter notes, fast and cheap, using a Python script. Read this file in full before starting.

> [!important] Method change (2026-06-07)
> The split is now done by a **Python script that cuts the file at every `## ` (level-2) heading** — one file per chapter. The agent never re-types the content, so the job costs almost no tokens and runs in seconds. The previous method (the agent reading the whole norm and manually writing each split file) is **abandoned** — it was slow and token-expensive. See §4–§6.

---

## Context

**Vault location:** `C:\Users\n_pap\Documents\PapaLab\Papa_Vault\` or `E:\PapaLab\Papa_Vault\`
**Work area:** `Knowledge\Norms-Regulations\` — where raw MD files land and are split.
**Final destination:** `Knowledge\Norms-Regulations\Eurocodes-NBN\EC[N]\[NORM]\` — finished folders are moved *by the user* after review.

**Reference example (this method):** `Knowledge\Norms-Regulations\Eurocodes-NBN\EC2\NBN EN 1992-1-1 ANB 2010\` — produced with the script below.

**Older examples** (subparagraph-level, pre-2026-06-07 method — structurally fine but more granular than the current standard): EC1 `NBN EN 1991-1-4`, EC0 `NBN EN 1990 ANB`, Infrabel-PTR `FR\` (PTR CE01).

---

## 1. Task triggers

You are invoked in one of three situations:

**A — Fresh norm:** A clean MD file exists in a folder under `Norms-Regulations\` with no split files alongside it. Process it fully (§2–§7).

**B — Incomplete or wrong split:** A folder has some split files but the work was stopped or is wrong. Assess, then complete/correct without redoing good work.

**C — Resume or fix:** The user describes a specific problem (missing chapter, bad name). Fix only what is broken.

Scan the target folder first and state your assessment in one sentence before proceeding.

---

## 2. Assess the source file

Read **only the headings** of the source file (e.g. `grep -nE '^#{1,2} '`), not the whole body. Establish:

1. **Norm identity** — full reference code (e.g. `NBN EN 1992-1-1 ANB:2010`), from the filename and frontmatter.
2. **Chapter structure** — the list of `## ` headings, in order. This is the split plan.
3. **Cleanliness** — is the file already clean markdown, or raw OCR with watermarks? If raw OCR, do §3 first. If already clean (the usual case for files prepared in the vault), skip straight to §4.

State the chapter list (one line each) before running the script. No split-plan table is needed — the `## ` headings *are* the plan.

---

## 3. Pre-clean (only if the source is raw OCR)

Skip this section if the file is already clean markdown. If it is raw PDF-to-markdown, clean it **before** splitting:

**Watermarks** — blocks of single words / short reversed-French fragments OCR'd from a rotated stamp. Delete entirely. Recognition signals:
- Contains `SORBALAPAP`, `salociN`, `eb.liarcut`, or `.LIAR` (RAIL reversed).
- Reversed-French single-word lines: `tnemucod`, `eriudorper`, `reilbup`, `ecnecil`, `égétorp`, `ruetua`, `stiord`, `elbinopsid`, `eriaropmet`, `etnenamrep`, `erdner`.
- Isolated fragments (`el`, `in`, `ne`, `uo`, `tios`, `nos`, `rap`, `suos`) between normal paragraphs.

A block usually spans 15–30 lines — delete the whole block. Also remove repeated page headers/footers (ICS codes, NBN publication lines, page numbers) mid-document; keep only the first identification block at the top.

**Formatting** (apply during clean-up so the split files inherit it):
- Headings normalised: `# H1` document title, `## H2` chapter, `### H3` section, `#### H4` sub-section. Do not go deeper than H4.
- Equations to LaTeX (`$…$` inline, `$$…$$` display); Greek as `\gamma`, `\sigma`, never Unicode in equations. Keep the comma decimal separator for French norms.
- Tables preserved as valid Markdown (bold header row, numeric columns right-aligned). Never split a table across files.
- `NOTE` clauses → `> [!note] NOTE [N]`; ANB/PTR overrides → `> [!important]` (sparingly).
- Verbatim text — do **not** paraphrase, summarise, or translate. Fix only unambiguous OCR errors.
- No images: replace a critical figure with a text description or a reconstructed data table; the PDF stays the reference for figures.

**Crucially: make sure every chapter is a `## ` heading before splitting.** The script keys off `## `. If the source uses a different chapter marker, normalise it to `## ` first.

---

## 4. Split method — the Python script

The split cuts the body at every line starting with `## `. Each chapter (heading + its body, including any inner `---` rules and `###` sub-headings) becomes one file. The text before the first `## ` (frontmatter + `# title` + intro) becomes the index file `00 - Index.md`. The original file is renamed to a full-norm archive and kept.

**Output layout** (flat — the parent folder already carries the norm name; no `chapters` subfolder):

```
[NORM-NAME]\                              ← already named after the norm
├── [NORM-NAME] — FULL (archive).md       ← the original, renamed (kept for archive)
├── 00 - Index.md                         ← frontmatter + title + intro
├── 01 - Remarques générales ANB.md
├── 02 - Bases de calcul.md
├── 03 - Matériaux.md
└── …                                     ← one file per ## chapter, in order
```

**The script** (set `SRC` to the source file; nothing else needs changing):

```python
import re
from pathlib import Path

# --- only thing to edit: the path to the clean source MD file ---
SRC = Path(r"C:/.../[NORM-NAME]/[NORM-NAME].md")

OUT = SRC.parent                      # flat: split into the norm folder itself
text = SRC.read_text(encoding="utf-8")

# 1. Peel off YAML frontmatter (kept on the index file).
fm = ""
body = text
m = re.match(r"^(---\n.*?\n---\n)", text, flags=re.DOTALL)
if m:
    fm = m.group(1)
    body = text[m.end():]

# 2. Split the body at every "## " (level-2 heading). Lookahead keeps the
#    heading attached to its section and ignores inner "---" rules.
parts = re.split(r"(?m)^(?=## )", body)
preamble = parts[0].strip()                       # title + intro -> index
sections = [p.strip() for p in parts[1:] if p.strip()]

def slugify(s):
    s = s.strip().replace("—", "-")
    s = re.sub(r'[\\/:*?"<>|]', "", s)            # illegal Windows chars
    s = re.sub(r"\s+", " ", s).strip()
    return s[:80]

parent = SRC.stem

# 3. Index file (00) = frontmatter + title + intro.
if preamble:
    (OUT / "00 - Index.md").write_text(fm + preamble + "\n", encoding="utf-8")

# 4. One file per chapter, numbered in document order, with a backlink.
for i, sec in enumerate(sections, start=1):
    heading = sec.splitlines()[0].lstrip("# ").strip()
    name = f"{i:02d} - {slugify(heading)}.md"
    header = f'---\nparent: "[[{parent}]]"\n---\n\n'
    (OUT / name).write_text(header + sec + "\n", encoding="utf-8")
    print(f"  {name}")

# 5. Archive the original full norm (rename in place, keep it).
archive = OUT / f"{parent} — FULL (archive).md"
SRC.rename(archive)
print(f"\nArchived original -> {archive.name}\nDone -> {OUT}")
```

Run it with `python split_norm.py`. It writes UTF-8 (accents are correct in the files even if the console shows them garbled — verify with the file tool, not the console).

> [!note] Optional backlink in the archive
> The archive file keeps its original content unchanged. If you want it discoverable from the chapters, the `parent:` frontmatter on each chapter already points to `[[NORM-NAME]]`, which now resolves to the archive (same stem). No extra step needed.

---

## 5. File naming convention

- **Chapter files:** `NN - [chapter title].md` — two-digit order index, then the chapter heading text, accents kept (e.g. `03 - Matériaux.md`). The script derives this automatically; do not hand-rename unless the heading text is unusable.
- **Index file:** `00 - Index.md` (the preamble — frontmatter, `# title`, intro).
- **Archive (original full norm):** `[NORM-NAME] — FULL (archive).md`.

The script strips Windows-illegal filename characters (`\ / : * ? " < > |`) and trims to 80 chars. If two chapters produce the same slug, the numeric prefix keeps them distinct.

---

## 6. Frontmatter

The fast method keeps frontmatter **minimal** — the script does not read content, so it cannot generate tags or `related` links. Each chapter file gets only a backlink to the full norm:

```yaml
---
parent: "[[NORM-NAME]]"
---
```

The index file (`00 - Index.md`) keeps the **original frontmatter** of the source norm verbatim.

> [!note] Optional enrichment pass
> Richer per-file frontmatter (`type: norm-extract`, `norm`, `section`, `tags`, `related`) and navigation footers (`Liens : … · [[CLAUDE]]`) — as used in the older subparagraph-split norms — can be added in a **separate manual pass** if the norm warrants it. That pass *does* require reading each file and costs tokens, so do it only on request. The default deliverable is the minimal-frontmatter chapter split above.

---

## 7. Self-check before reporting done

- [ ] Every `## ` chapter of the source maps to exactly one numbered file (no gaps, no duplicates) — count `## ` headings in the source vs. chapter files produced.
- [ ] `00 - Index.md` exists and contains the original frontmatter + title + intro.
- [ ] The original file is renamed to `[NORM-NAME] — FULL (archive).md` and still present (never deleted).
- [ ] Accents render correctly in filenames and content (check with the file tool, not the console).
- [ ] If the source was raw OCR: no watermark remnants (`SORBALAPAP`, `tnemucod`) survive in any file.
- [ ] No chapter file is empty or frontmatter-only.

---

## 8. Reporting

```
Norm: [full reference]
Chapters split: N (list the file names)
Archive: [NORM-NAME] — FULL (archive).md
Issues found and resolved: [any OCR / heading-normalisation fixes]
Ready for review: yes
```

Do not dump file contents in the summary — just the file list and any judgment calls.

---

## 9. Folder recovery (situation B / C)

1. List the source `## ` headings and compare against the chapter files present.
2. If a chapter is missing or mis-cut, re-run the script (it overwrites cleanly) or fix the single file.
3. Confirm the archive file exists and the original is not lost.
4. Do not rewrite files that already pass §7.

---
