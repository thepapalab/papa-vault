# Papa_Vault — Engineering Intelligence System

## Structure
- 00-Inbox/: Drop zone for notes from claude.ai (downloaded .md files). Triage periodically.
- Methodology/: One note per Eurocode clause, check type, or engineering method. Curated, dense, no fluff.
- Projects/: Per-project context (decisions, loads, reviewer remarks). NOT synced to GitHub — work PC only.

## Rules for Claude (Code / Desktop)
- When generating a calculation or script: read relevant Methodology/ notes first.
- fyk ≤ 400 MPa always (PTR CE01).
- Eurocodes + Belgian NBN annexes. Never assume a parameter — flag if missing.
- Code output: engineering variable names, commented for teaching.
- Calculation notes: French, natural prose, optimised for Word paste.