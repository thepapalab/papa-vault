---
title: Python — README
type: index
status: living
created: 2026-06-01
---

# Python — README

Patterns and idioms only. The *how*, not the *maths*. This folder never holds `eurocode-lib` functions — those live on personal hardware and are referenced, never copied (CLAUDE.md §6).

What belongs here:
- handcalcs calc-note structure (cell layout, `%%render`, comment conventions)
- the `pandoc --reference-doc=template.docx` invocation for Word compilation
- the `nbconvert --to webpdf` call for PDF export, code hidden
- the docx XML unpack/modify/repack workflow, incl. the valid `w14:paraId` rule (8-digit hex below 0x7FFFFFFF)
- `msg_to_txt.py`-style utility patterns (Outlook .msg → .txt + PDF)
- multi-agent document-generation pipeline notes (orchestrator + paragraph agents)

What does NOT belong here:
- any function with engineering control flow (solver, load-combination loop, envelope extraction) → that is library code.

---

Links: [[_Knowledge — Index]]
