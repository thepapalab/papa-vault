---
title: Eurocode Seminar Notes — Conversion Runbook
type: runbook
created: 2026-06-07
---

# Eurocode Seminar Notes — Conversion Runbook

Convert the Greek-language Eurocode seminar slide decks (Penelis / Kappos et
al., Α.Π.Θ. 2009) under vault folder Βοηθητικό Υλικό - Ευροκώδικες
into **clean, readable Markdown knowledge notes** — optimised for both an AI
agent and a human reader.

---

## 0. How to start a session (for the user)

Open a fresh chat and paste:

> Read `Papa_Vault/Tools/seminar_converter/RUNBOOK.md` and continue the
> Eurocode seminar conversion. Target folder: **`<EC2 | EC3 | … | next>`**.
> Use the micromamba `cuda` interpreter for the scripts.

`next` = "pick the first folder in PROGRESS.md that isn't done." That's all the
agent needs — everything else (state, conventions, resume point) lives on disk.

---

## 1. The golden rules (read before writing anything)

1. **Text first.** The deliverable is clean, well-structured Greek prose +
   equations. Optimise for readability and for an agent grepping it later.
2. **No embedded images in the `.md`.** The user pastes figures themselves, on
   demand. Page renders ARE saved to `_assets/` as a paste library — but the
   note only *points* to them (see §4).
3. **Math as LaTeX** — inline `$…$`, block `$$…$$`. Never leave `V_Rd,c` style
   flat text for a real equation.
4. **Tables as GitHub-flavoured Markdown** when legible. If a table is too dense
   / low-res to transcribe without guessing numbers, do NOT guess — drop a
   figure pointer (§4) to its page instead.
5. **Preserve Greek.** Do not translate the body. (Frontmatter keys stay
   English; section titles stay Greek as on the slides.)
6. **Structure by the document's own numbering** (e.g. `## 6.2 Διάτμηση`), not
   by slide/page number. Two slides often share one PDF page — merge logically.
7. **De-fragment.** Slide builds repeat lines and emit partial "build" lines;
   collapse them. One clean statement, not three half-versions.
8. **Never invent.** Transcribe what the slide shows. Where you render a
   standard EC formula in canonical form, keep symbols faithful to the slide.

---

## 2. Interpreter

The scripts need PyMuPDF. Use:

```
C:\Users\n_pap\.ai-navigator\micromamba\envs\cuda\python.exe
```

The bare `python` on PATH (3.14) does **not** have PyMuPDF. In PowerShell call
with `& "<path>" script.py …`.

---

## 3. Pipeline (per folder)

### Step A — prepare assets + scaffold (cheap, no vision)

```
& $PY build_assets.py "<folder name or substring>"
```

This renders every page to `<output>/_assets/<stem>/pNNN.png`, dumps extracted
text to `<output>/_scaffold/<stem>.txt`, flags byte-identical duplicate PDFs,
and writes `<output>/_manifest.json`. Re-runnable; `--force` re-renders.
`--dry-run` enumerates without writing; `--list` shows all source folders.

**Output location:** `Methodology/Seminar-Notes/<ECx>/` by default; EC2 is
overridden to the existing `Methodology/EC2-Concrete/Seminar-Notes-Penelis/`
(see `OUTPUT_OVERRIDES` in the script — add an override if a folder belongs in
a specific domain).

### Step B — decide which PDFs to transcribe

From the manifest:
- **Skip** entries with `duplicate_of` set (identical file).
- When both a plain and a **`-notes`** version of the same chapter exist,
  transcribe the **`-notes`** one (richer, has speaker notes) and mark the plain
  one `skipped (superseded by <stem>-notes)`.
- Everything else: transcribe.

### Step C — transcribe one chapter → `.md`

For each chapter to do:
1. **Read the scaffold** `_scaffold/<stem>.txt` (cheap text) for the accurate
   Greek wording, page by page.
2. **Open page PNGs selectively** — only pages whose scaffold shows formulas,
   tables, or figures that need structure. You don't need to open every page;
   lean on the scaffold for plain-text slides.
3. Write `<output>/<stem>.md` using the template in §5. Structure by section,
   LaTeX the math, GFM the legible tables, figure-pointer the rest.
4. **Update progress immediately** (§6) so a context reset can resume.

Work chapter by chapter and save after each — never hold a whole folder in
your head.

---

## 4. Figure / dense-table pointer convention

Where a slide is an irreducible diagram, nomograph, or a table too dense to
transcribe safely, insert a one-line pointer (no embed) so the human can paste
the asset later:

```
> 🖼️ **[Σχήμα]** σύντομη περιγραφή — `_assets/<stem>/p012.png`
```
```
> 📊 **[Πίνακας]** σύντομη περιγραφή — `_assets/<stem>/p003.png`
```

Keep the description short and specific (what the figure shows) so the note is
useful even before the image is pasted. The user replaces/augments with their
own `![[Pasted image …]]` on demand.

---

## 5. Note template

```markdown
---
title: "EC<x> Σεμινάριο — <chapter title (Greek)>"
type: seminar-notes
domain: <Concrete | Steel | Geotechnical | …>
eurocode: EC<x>
source: "<authors> — Σεμινάριο Ευρωκωδίκων, Α.Π.Θ. (2009)"
language: el
status: draft
tags: [EC<x>, eurocode-<x>, seminaire, grec, <topic>, …]
related: ["[[_EC<x>-Seminar — Index]]", "[[<prev stem>]]", "[[<next stem>]]"]
created: <YYYY-MM-DD>
---

# EC<x> Σεμινάριο — <chapter title>

> Πηγή: <authors> — Σεμινάριο Ευρωκωδίκων, Α.Π.Θ. (2009). Μεταγραφή των
> διαφανειών σε Markdown (εξισώσεις σε LaTeX· σχήματα/πυκνοί πίνακες ως
> δείκτες προς `_assets/`, επικόλληση κατ' απαίτηση).

## <section number> <section title>

…clean text, $LaTeX$, tables, figure pointers…

---

Links: [[_EC<x>-Seminar — Index]] · [[<prev>]] · [[<next>]] · [[_EC<x> — Index]] · [[CLAUDE]]
```

**Reference note already done to this standard:**
`Methodology/EC2-Concrete/Seminar-Notes-Penelis/EC2-Seminar_ch6.md`
(it still embeds a few crops — the *new* standard is pointers only, no embed).

### Per-folder index

After the chapters of a folder are done (or as you go), create/update
`<output>/_EC<x>-Seminar — Index.md`: frontmatter (`type: index`), a one-line
description, a `## Chapters` table linking each `[[stem]]` with its title, and
a Links footer. Link it from the domain index (e.g. `[[_EC2 — Index]]`) if one
exists.

---

## 6. Progress tracking & resuming

`PROGRESS.md` (next to this runbook) is the human-readable tracker — **the
source of truth for "what's left".** `_manifest.json` in each output folder is
the machine state (md5, stems, duplicates).

After finishing each chapter, update its row in `PROGRESS.md`:
`pending → in-progress → done` (or `skipped` with reason). Update the folder's
roll-up status too. On launch, read `PROGRESS.md` first to find the resume
point; if the target folder has no `_manifest.json` yet, run Step A.

A folder is **done** when: every non-duplicate, non-superseded PDF has a
transcribed `.md`, the index exists and is linked, and `PROGRESS.md` says so.

---

## 7. Economy guidance

- Step A is free (no vision). Always run it first; never read raw PDFs.
- Prefer the scaffold text; open page images only for math/table/figure pages.
- Read images in batches, but don't reload a page you've already transcribed.
- Skip duplicates and superseded slide-only versions.
- Don't crop or embed images — pointers only. (This is the main change from the
  EC2 pilot, made for economy.)

---

## 8. Source folders (9 Eurocodes, 35 PDFs)

EC1 (8) · EC2 (7) · EC3 (1) · EC4 (2) · EC5 (5) · EC6 (4) · EC7 (5) · EC8 (2) ·
EC9 (1). See `PROGRESS.md` for live status. (`build_assets.py --list` regenerates
this count.)
