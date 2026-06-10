---
title: "Karagiozis Crisis Runner — Tools and Tech Stack"
type: tech-stack
status: active
tags: [game-dev, karagiozis, tooling, godot, pipeline]
---

# Karagiozis Crisis Runner — Tools and Tech Stack

Selection principle: open source first. A paid tool is the choice only where it gives a real, concrete advantage — a capability the open-source option lacks, or an existing asset/skill that would be wasteful to abandon.

## Stack at a Glance

| Layer | Primary (open source) | Fallback / paid option | Verdict |
|---|---|---|---|
| Game engine | Godot 4 (MIT) | — | Decided. No paid engine warranted. |
| Scripting | GDScript | C# (free, in-engine) | GDScript default; C# only for perf-critical code (not needed for a 2D runner). |
| AI coding agent | Godot MCP bridge + community plugins | Claude Code (owned); Ziva (paid in-editor agent) | Drive Godot via MCP; pay only if a live-scene agent proves worth it. |
| Vector art (characters) | Inkscape | Adobe Illustrator (owned) | Illustrator stays — real advantage: existing skill + the original puppet already traced in it. |
| AI image / reference edit | Local Flux or Stable Diffusion (ComfyUI) | Nano Banana (Gemini, via MCP); Scenario.gg | Nano Banana for fast edits/props; local SD for zero-cost control; Scenario only for batch style consistency. |
| UI / icons / store art | Inkscape / Krita | Claude Design (owned) | Use the Claude Design license for HUD, icons, capsule and marketing layout. |
| Skeletal / cutout rig | Godot `Skeleton2D` + `Bone2D` + IK | DragonBones (FOSS); Spine (paid) | Native rig is enough for pinned-cutout puppets. Spine only if mesh deformation is ever needed. |
| Raster cleanup | Krita / GIMP | Photoshop (only if owned) | Krita for paint-over and part cutting. No advantage to paying. |
| Music | LMMS / MuseScore / Audacity | Suno or Udio (paid AI); commissioned composer | Originals required for any paid release. See [[04 Audio]] and the IP note. |
| SFX | Bfxr / jsfxr; Freesound (check licence) | — | Free covers all early needs. |
| Version control | Git + GitHub + Git LFS | — | Already in use via thepapalab. LFS for binary assets. |
| Knowledge / docs | Obsidian | — | This vault. No change. |
| Distribution | itch.io (demo) | Steam (Steam Direct fee); mobile stores later | itch first for the demo; Steam for the commercial release. |

## Game Engine and Language

Godot 4 (current 4.6 line), MIT-licensed, no royalties, one codebase to desktop/mobile/web. Chosen for AI legibility: text-based scene files and a small Python-like scripting language make the whole project readable and editable by an AI agent, which is the core of the intended workflow. GDScript is the default — Python-adjacent, fastest iteration, best-documented. C# is available in-engine for free but carries a larger export and weaker web export; reserve it for performance-critical systems, which a 2D runner will not have.

Rejected: Unity (platform dependence, licensing history) and Bevy/Rust (matches "fully code-based" literally, but the Rust curve and a thin, fast-churning AI corpus would undercut the AI-leverage goal).

## AI Coding and Agent Layer

The intended mode is to direct in natural language and code while an AI agent scaffolds scenes and scripts. Open-source first: community Godot MCP bridges and bring-your-own-key in-editor plugins (Godot AI Suite, AI Assistant Hub) let an external agent read and modify the project through the text scene files. Claude Code (owned) is the agent; connect it via the MCP bridge.

Paid option with a real advantage: Ziva, the most complete in-editor agent — it manipulates the live scene tree through the editor's own API rather than patching scene files, runs tests, and reads debugger output. Worth paying for only if the MCP-bridge approach proves too indirect. Add a `CLAUDE.md` at the repo root to govern agent behaviour, mirroring the eurocode-lib pattern.

## Vector Art (Characters and Riggable Parts)

The one place a paid tool wins on real merit. Inkscape is the open-source vector editor and is fully capable. But Adobe Illustrator is already owned, already mastered, and already holds the original traced Karagiozis puppet — switching would discard a working asset and a real skill for no gain. Keep Illustrator as primary; use Inkscape only if a clean SVG export into Godot is ever smoother through it. The riggable parts are authored by hand; no AI tool produces clean separated parts.

## AI Image Generation and Reference Modification

Two different jobs: editing/stylizing a reference, and generating backgrounds.

Open source first: local Flux or Stable Diffusion via ComfyUI, with img2img plus ControlNet and IP-Adapter. Local GPU, zero marginal cost, full control. Strongest fit for the reference-modification idea — feed the traditional cutout, restyle for bold outlines, add gaming effects, regenerate variants. Setup cost is the only downside.

Paid where they earn it:
- Nano Banana (Gemini image, via MCP) — genuine reference-conditioned editing with strong consistency, very low per-image cost, near-zero setup. Best low-friction choice for stylizing the puppet reference and generating small props (sunglasses, Gucci shoes, watches, tokens).
- Scenario.gg — train a custom model on a curated reference set, then batch-generate on-style assets. Worth it only for many consistent assets at once; likely overkill for 5–7 backgrounds.

Not for this layer: Claude Design (a design/canvas agent, not a raster image editor) — it belongs in the UI layer.

Scope reality: these tools produce source raster art, not animated characters. Cutting, rigging, and animation remain manual (see [[03 Art Direction and Assets]]).

## UI, Icons, and Store Art

Inkscape and Krita cover this for free. Claude Design (owned) fits here — HUD layout, icon sets, the Steam capsule, and marketing key-art composition iterated through chat.

## Skeletal / Cutout Animation

Godot's built-in `Skeleton2D` with `Bone2D` and an IK solver (CCDIK/FABRIK) is primary and best: native, no import pipeline, FOSS. It handles the pinned body, the multi-piece arm, and the puppeteer sticks, and is where the physics-floppy ↔ controlled-IK arm mode switch lives. Alternatives: DragonBones (FOSS) for an external rigging UI; Spine (paid) only if weighted mesh deformation is ever required — not needed for a pinned-cutout puppet.

## Raster Editing, Audio, Version Control, Docs, Distribution

- Raster: Krita and GIMP cover all needs for free.
- Audio: LMMS / MuseScore / Audacity for originals; Bfxr / Freesound for SFX; paid AI music (Suno/Udio) or a commissioned composer for commercial originals — see [[04 Audio]].
- Version control: Git + GitHub (thepapalab), Git LFS for binary assets, small milestone branches.
- Docs: Obsidian — this vault.
- Distribution: itch.io first (free, low friction, demo home); Steam for the commercial release (Steam Direct fee per title); mobile stores deferred until PC proves the concept.

## IP Hygiene (cross-cutting)

For any build intended for sale: train image models on owned, licensed, or public-domain imagery; use original or licensed music; verify every borrowed SFX licence. For a private hobby build none of this binds, but keeping assets clean from the start preserves the option to ship without a later rebuild. Full per-asset flags in [[03 Art Direction and Assets]].

## Open Items

- Confirm the Godot MCP bridge choice and write the repo `CLAUDE.md`.
- Decide local Flux/SD versus Nano Banana as the default image tool (control versus setup cost).
