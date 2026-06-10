---
title: "Karagiozis Crisis Runner — Gameplay and Mechanics"
type: gameplay
status: active
tags: [game-dev, karagiozis, gameplay, mechanics, levels]
---

# Karagiozis Crisis Runner — Gameplay and Mechanics

## Core Loop

- Run automatically (autorun side-scroll).
- Jump, duck, or sidestep hazards.
- Trigger arm-based powers at precise moments.
- Survive visual attack patterns.
- Reach a short finale or boss phase.

Runner strengths apply: readable timing, symbolic obstacles, repeatability, score pressure.

## Structure

A linear 2D runner with handcrafted stages of roughly 60–180 seconds each — feasible for a solo project while allowing visual storytelling, scripted symbolism, and boss encounters, without the systems load of a roguevania.

## Stage List

| # | Stage | Gameplay focus | Notes |
|---|---|---|---|
| 1 | Golden Era (Mykonos) | Easy collection, bling pickups, bright pace | Clubs in the background; Petros the pelican as a recurring set-piece. |
| 2 | Olympic | Rescue Foivos and Athina, then a miniboss | Quick stage; the botox-lady miniboss closes it. |
| 3 | Capital Controls | Scarcity, bank/ATM hazards, the 60-token cap | The defining austerity stage. |
| 4 | Referendum (Syntagma) | Momentum and false victory; BaroufMan ally beat | BaroufMan helps, then exits. |
| — | Emigration (Germany) | Grey-rain contrast scene (Nionios) | Early concept; may not make the first build. |
| 5 | Wheels boss | First-slice climax | Readable projectile patterns. |
| 6 | Gargamel endless | Endless pursuit; cannot win, only run | Karagiozis in smurf skin; the closing statement. |

## The Arm — signature system and central design problem

The jointed arm is the signature mechanic and the hardest design decision, because aesthetic and gameplay pull opposite ways:

- The floppy physics arm (oval pieces, gravity, jiggle) sells the puppet during idle and run. This is the proven technique.
- The powers are precise, controlled actions. A ragdoll arm cannot perform these cleanly.

Resolution to prototype first: a mode switch. The arm stays physics-floppy during normal movement; on power activation it snaps to a controlled IK pose to execute the action, then relaxes back into physics. This preserves the look and gives input precision. It is genuine engineering, not a free combination, and it is the single most important thing to prototype.

## Power Set

The set is open, not fixed. Confirmed forms (visuals in [[03 Art Direction and Assets]]):

| Form | Function | Role |
|---|---|---|
| Chain hand (basic) | Extend, grab anchors, swing, preserve momentum | Base traversal |
| Catapult grab | Snappy grab of pickups and powerups | Collection / trickster |
| Boxing glove | Damage power-up; punch through enemies and obstacles | Offense |
| Frappe | Slows everything for a window; makes finishing a level easy | Control / panic button |
| Helicopter hand | Spins for brief invincibility, destroying everything in reach | Burst defense/offense |

Open / future: Missile (detaching fist) — keep, fold into the glove, or drop (open question). "Τράβα κουπί" (Karagiozis rows a boat) and others — parked as ideas until the core arm feels good.

First-slice discipline: prove one power fully through the mode-switch system before adding the rest.

## The 60-Token Rule

Collection in the capital-controls stage is capped at 60 tokens per run — a direct nod to the €60 daily ATM withdrawal limit of 2015. Ties the mechanic to the era. Drachma/euro split: drachma abundant in the golden era, euro the constrained crisis currency (see [[03 Art Direction and Assets]]).

## Boss Design

Wheels (first-slice boss):
- Phase 1 — straight projectile patterns, currency bursts, decrees, rockets.
- Phase 2 — wheelchair dash patterns, summoned hazards, tighter platform windows.
- Phase 3 — mixed projectile curtain requiring chain-hand timing and offensive counterplay.

Frau (full-game boss, teaser only in the first slice): two-phase — blonde, then army-helmet — using euro-bombs and command attacks.

## Difficulty and Readability

The screen must read in half a second. Favor readable telegraphs, fair hitboxes, and repeatable patterns over depth of combat. Bright colour is reserved for things that matter (hazards, tokens, attacks).

## MVP First-Slice Checklist

- Karagiozis can run, jump, get hit, and die.
- The arm mode-switch works; at least one power (chain) feels precise.
- Two stages fully playable.
- One transition beat lands emotionally.
- One complete, readable boss fight (Wheels).
- The 60-token rule is implemented.
- The Gargamel chase appears as the closing stinger.
- A non-Greek player understands the premise without political exposition.
- Completable in 8–12 minutes.

## What to Avoid

- Too many mechanics in one slice.
- A tuned endless mode before the core stage runner feels good.
- Detailed painted backgrounds — use parallax layers (see [[03 Art Direction and Assets]]).
