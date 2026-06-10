---
title: "Karagiozis Crisis Runner — Art Direction and Assets"
type: art-direction
status: active
tags: [game-dev, karagiozis, art, assets, pipeline]
---

# Karagiozis Crisis Runner — Art Direction and Assets

Visual language, the cut-and-rig pipeline, the asset list, and per-character specs. Items marked **(proposed)** are not yet confirmed; **(IP)** marks a commercial-use flag.

## Style Foundation

Two references blended: traditional Greek shadow-theater Karagiozis (flat, hinged, bold ink outlines) and early-platformer nostalgia. The result is a cutout / skeletal puppet aesthetic, not pixel art.

Rules:

- Silhouette-first. Every character reads as a black-on-light silhouette before colour.
- Bold outlines. Heavy ink contours for a stage-puppet read; this is also the target of the AI outline-boldening pass.
- Rough is charm. Slight imperfection in cuts and joints reinforces the handmade-puppet feel. Do not over-polish.
- Colour discipline. Bright colour reserved for symbolic elements (fire, tokens, propaganda, boss attacks). Eras carry palette: golden warm/neon, crisis grey, propaganda green, euro-blue hazards, and a cold grey-rain palette for the emigration scene.

**(IP) Mario reference:** loose era/feel nod only (jump-game silhouette, moustache, retro cues), never recognizable Mario features.

## Production Pipeline (cut-and-rig)

The repeatable method from idea to animated character. The jointed physics arm and pinned body separation are the proven cutout technique; the puppeteer sticks (one on the upper body, one on the hand) are visible control rods.

1. Source art — hand-trace in Illustrator, or generate a stylized base with Nano Banana / local Flux-SD from the traditional cutout plus prompt, then clean for bold outlines.
2. Separate into rig parts — each on its own transparent layer, exported as individual PNG/SVG. Standard humanoid set: head, upper body, lower body, upper-arm segments, forearm/hand pieces, accessory layers, two sticks. Keep small joint overlaps so no gap shows on rotation.
3. Import to Godot as `Sprite2D` nodes under a `Skeleton2D`.
4. Rig — build the `Bone2D` chain: pinned upper/lower body, multi-piece arm chain, sticks as non-deforming overlays; IK on the arm for the controlled-power mode.
5. Animate — author in Godot's `AnimationPlayer`/`AnimationTree`. Floppy idle/run uses light arm physics; powers snap to IK poses.

Conventions: part naming `{char}_{part}.png` (no spaces, no em-dashes — NFC/NFD filename hazard on the work PC); one folder per character; fixed on-screen character height reused for silhouette consistency.

Scope reality: AI covers step 1 only. Steps 2–5 are manual per-character labour and are the bulk of the work.

## Character Visual Specs

### Heroes / allies

| Character | Visual concept | Parts | First-pass animations |
|---|---|---|---|
| Karagiozis | Base puppet; bling in the golden era, stripped in crisis; smurf skin in the Gargamel level | Head, torso, lower body, arm chain (multi-segment), hand, two sticks, accessory layers | Run, jump/fall, hit, die, arm idle-jiggle, power poses |
| Nionios **(proposed/early)** | Brain-drain allegory; emigrates to Germany | Head, torso, lower body, arm, suitcase prop | Idle, walk-away (emigration beat) |
| BaroufMan | Bald faux-savior, biker energy | Head, torso, lower body, arms, bike | Ride-in, gesture, ride-out (betrayal) |
| Tsipster | Robotic compromised-idealism stand-in | Head, torso, limbs, robotic accents | Idle, attack (if miniboss) |
| Hatziavatis **(proposed)** | Theatre foil, guide/tutorial NPC | Head, torso, lower body, arm | Idle, talk |
| Barba Giorgos **(proposed)** | Theatre strongman, ally power-up | Head, torso, lower body, arms | Idle, smash |

### Villains and mobs

| Character | Visual concept | Parts | First-pass animations |
|---|---|---|---|
| Wheels | Wheelchair creditor-boss | Head, torso, wheelchair+wheels, arms | Roll, dash, fire, phase transitions |
| Frau | Chancellor boss, two looks | Head x2 (blonde / helmeted), torso, arms, euro-bomb props | Idle, throw, command, phase-2 transition |
| Olympic villain | "Botox lady" organizer caricature **(IP: living figure)** | Head, torso, gown, arms | Appear, miniboss attack |
| Gargamel Regent | Smirking dynasty ruler; endless-run pursuer **(IP: Peyo)** | Head, torso, robe, arms | Chase-run loop, lunge |
| Troika auditors **(proposed mob)** | Faceless suited men-in-black with briefcases (IMF/ECB/EU coded) | Head, torso, lower body, briefcase | Walk, attack |

## Karagiozis Cosmetics

Additive sprite layers on the base rig — trivial in cutout:

- Bling (golden era): Rolex, Gucci shoes, gold chain, golden sunglasses, cigar, frappe. Falls away visibly across the Olympic Crash transition so wealth is seen to be stripped, not just stated.
- Smurf skin (Gargamel level): blue restyle of Karagiozis. **(IP)** for sale, keep it generic-blue stylization, not literal Smurf design.

## Scenes / Backgrounds

Parallax layers (foreground / midground / background), never single painted scenes. Target 5–7 plus the emigration contrast scene.

| Scene | Concept | Stage |
|---|---|---|
| Shadow-theater base | The berde stage look; default/menu identity | Frame / tutorial |
| Mykonos golden | Coastal night, neon, the big clubs; Petros the pelican recurring | Golden Era |
| Olympic | 2004 stadium and torch; Foivos & Athina to free | Olympic |
| Bank / ATM queue | Capital-controls imagery; the €60-limit queue | Capital Controls |
| Syntagma / Parliament | Protest square and the Vouli | Referendum |
| Germany emigration **(proposed/early)** | Cold, grey, rain — contrast to the Greek light | Nionios beat |
| Crisis Acropolis | The Acropolis in ruins; grey palette | Crisis |
| Smurf-Acropolis | Acropolis under a blue takeover **(IP)** | Endgame / Gargamel chase |

## Collectibles, Weapons, Hazards

- Coins: euro and drachma — drachma abundant in the golden era, euro the constrained crisis currency (60 cap).
- Projectiles/hazards: euro-sign bombs (Frau), memorandum scrolls (Μνημόνιο) as the signature on-theme projectile **(proposed)**, austerity decrees as paper hazards, currency bursts (Wheels). Tear-gas canister as a crisis hazard — on-theme but tonally loaded; use as caricature if at all.

## UI / HUD

- Frame the game in the berde — the shadow-theater cloth screen with its decorative border — as the menu and HUD motif **(proposed)**.
- Stage transitions as theatre act-cards ("Πράξη Α'") **(proposed)**.
- Minimal HUD: drachma/euro token counter, the 60-cap meter in the crisis stage, current arm-form indicator. The world carries the storytelling.

## IP Hygiene (cross-cutting)

For a private hobby build none of this binds. For any build intended for sale:

- Mario likeness (Nintendo): loose era nod only.
- Smurfs / Gargamel / smurf skin (Peyo — Belgian, heavily protected): generic smirking-dynasty villain and generic blue stylization, not literal Smurfs.
- Living public figures (Olympic villain, Frau, Wheels, BaroufMan, Tsipster): coded caricature only; no named person on the store page or in marketing.
- AI-generated source art: train on owned, licensed, or public-domain shadow-puppet imagery, not copyrighted contemporary Karagiozis art or film stills.
