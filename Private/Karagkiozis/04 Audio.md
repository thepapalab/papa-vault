---
title: "Karagiozis Crisis Runner — Audio"
type: audio
status: active
tags: [game-dev, karagiozis, audio, music, sfx]
---

# Karagiozis Crisis Runner — Audio

## Music Direction

Strong tonal direction by era:

- Opening scene — the famous Karagiozis anthem; a natural opener.
- Levels — Zorba, starting slow and relaxed and accelerating toward the end of the level (the syrtaki naturally accelerates, which fits the rising tension).
- Golden-era / getting-rich scenes — Greek trap (e.g. "Mama", "Kotera") for the flashy pre-fall mood; pairs with the Mykonos visuals.
- Boss fights — a slow, rhythmic German / old-film motif (the "occupation arriving" register from old Greek cinema). To be located and confirmed.

**Licensing caveat:** every track above is copyrighted. Free for a private hobby build; unusable on a paid release without licensing or original re-composition in the same style. Theodorakis's Zorba/Sirtaki is protected in the EU until roughly 2091 and the estate is protective. For a commercial path, commission or compose originals "in the style of" each (see audio tooling in [[05 Tools and Tech Stack]]).

## Sound Effects

- Generators: Bfxr / jsfxr / sfxr for retro arcade-style effects that fit the tone.
- Library: Freesound.org — verify the licence per clip (prefer CC0).
- Signature cues to author: the Karagiozis laugh, the arm extend/snap, frappe slow-time onset/release, helicopter spin, token pickup (distinct drachma vs euro), boss telegraphs.

## Implementation Notes

- Godot handles layered music and SFX natively. Use the level track's acceleration as a tension signal that maps to stage progress.
- Audio cues for hazards and powers are a polish-phase priority but should be roughed in early enough to test readability.
