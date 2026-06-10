---
title: Eurocode Seminar Notes — Progress
type: progress-tracker
created: 2026-06-07
updated: 2026-06-07 (EC0 ✅ 2/2; EC7 ✅ 5/5; EC1 ✅ 6/6 done)
---

# Eurocode Seminar Notes — Progress

Source of truth for "what's left". See [RUNBOOK.md](RUNBOOK.md) for the method.
Status legend: ⬜ pending · 🟡 in-progress · ✅ done · ⏭️ skipped.

## Folder roll-up

| Folder                                      | Output                             | Assets | Chapters done | Status |
| ------------------------------------------- | ---------------------------------- | ------ | ------------- | ------ |
| EC0 — ΕΝ 1990 (εξαχθέν από EC1 source)      | Seminar-Notes/EC0                  | ✅      | 2 / 2         | ✅      |
| EC1 — Βάσεις σχεδιασμού και Γενικές δράσεις | Seminar-Notes/EC1                  | ✅      | 6 / 6         | ✅      |
| EC2 — Κατασκευές από Οπλισμένο Σκυρόδεμα    | EC2-Concrete/Seminar-Notes-Penelis | ✅      | 1 / 4         | 🟡     |
| EC3 — Μεταλλικές Κατασκευές                 | Seminar-Notes/EC3                  | ⬜      | 0 / 1         | ⬜      |
| EC4 — Σύμμικτες Κατασκευές                  | Seminar-Notes/EC4                  | ⬜      | 0 / 2         | ⬜      |
| EC5 — Ξύλινες Κατασκευές                    | Seminar-Notes/EC5                  | ⬜      | 0 / 5         | ⬜      |
| EC6 — Τοιχοποιΐα                            | Seminar-Notes/EC6                  | ⬜      | 0 / 4         | ⬜      |
| EC7 — Γεωτεχνικός Σχεδιασμός                | Seminar-Notes/EC7                  | ✅      | 5 / 5         | ✅      |
| EC8 — Αντισεισμικός Σχεδιασμός              | Seminar-Notes/EC8                  | ⬜      | 0 / 2         | ⬜      |
| EC9 — Κατασκευές από Αλουμίνιο              | Seminar-Notes/EC9                  | ⬜      | 0 / 1         | ⬜      |

(Chapter counts exclude duplicate / superseded PDFs; finalise per folder after
running `build_assets.py`.)

---

## Per-PDF detail

### EC2 — Κατασκευές από Οπλισμένο Σκυρόδεμα  → `EC2-Concrete/Seminar-Notes-Penelis`

| Stem | Pages | md5 | Status | Notes |
|---|---|---|---|---|
| ch1-5 | 31 | 206b5cc8 | ⏭️ | superseded by `ch1-5-notes` |
| ch1-5-notes | 75 | 94fd16f0 | ⬜ | transcribe — scaffold + assets ready |
| ch6 | 29 | ffb18bcf | ✅ | done — `EC2-Seminar_ch6.md` (pilot; embeds a few crops, pre-pointer standard) |
| ch7 | 15 | 0ed80ffa | ⏭️ | superseded by `ch7-notes` |
| ch7-notes | 55 | d636abd0 | ⬜ | transcribe — scaffold + assets ready |
| ch8-9 | 55 | d636abd0 | ⏭️ | byte-identical duplicate of `ch7-notes` |
| part2-bridges | 2 | d76a9043 | ⬜ | transcribe — scaffold + assets ready |

> EC2 cleanup note: the old flat-text `.md` for ch1-5 / ch7 / bridges (and their
> full-page `_assets`) predate this workflow. Overwrite them when transcribing;
> no manual deletion needed.

### EC7 — Γεωτεχνικός Σχεδιασμός → `Seminar-Notes/EC7`

| Stem | Pages | md5 | Status | Notes |
|---|---|---|---|---|
| eyrokodikas-7-meros-1o-geotechnikos-schediasmos- | 62 | bd771e1b | ✅ | EC7 Μέρος 1ο — Δομή, Αρχές και Επιπτώσεις · Αναγνωστόπουλος |
| efarmoges-toy-eyrokodika-7-en-1997-se-themata-sc | 62 | 76953d8c | ✅ | Εφαρμογές EC7 (62p) · Καββαδάς — Κεφ. 6–11 + σεισμός |
| efarmoges-toy-eyrokodika-7-en-1997-meros-2 *(new stem)* | 104 | dcdf8037 | ✅ | Εφαρμογές EC7 — Εθνικό Προσάρτημα & Παραδείγματα (104p) · Καββαδάς — scaffold re-extracted with distinct stem |
| simeioseis-gia-ton-eyrokodika-7-en-1997-notes | 164 | e37b0607 | ✅ | Σημειώσεις EC7 (full text, not slides) · Αναγνωστόπουλος + Καββαδάς + Παπαδόπουλος |
| schediasmos-themelioseon-me-passaloys-me-vasi-to | 45 | 8e356a76 | ✅ | Σχεδιασμός θεμελιώσεων με πασσάλους · Παπαδόπουλος ΕΜΠ |

> ⚠️ Stem collision: both "Εφαρμογές 2.pdf" (104p) and "Εφαρμογές.pdf" (62p) received the same
> truncated stem. The scaffold covers the 62p file only. The 104p file needs `build_assets.py`
> re-run with a patched stem (or open pages directly).

### EC0 — ΕΝ 1990 → `Seminar-Notes/EC0`

> EC0 PDFs were physically inside the EC1 source folder; extracted and transcribed separately.

| Stem | Pages | md5 | Status | Notes |
|---|---|---|---|---|
| en-1990-vaseis-schediasmoy-ton-feroyson-kataskey | 51 | ffe2e19b | ✅ | Εκπαιδευτικές Σημ. ΤΕΕ — ΕΝ 1990 (πυκνές σημειώσεις) · Μαλακάτας, Τρέζος |
| en-1990-vaseis-schediasmoy-en-1991-draseis-stis- | 181 | c93d1611 | ✅ | Εκπαιδευτικές Διαφάνειες — ΕΝ 1990 p1–60 (EC0) + ΕΝ 1991 p62–181 (→ EC1 μελλοντικά) |

### EC1 — Βάσεις σχεδιασμού και Γενικές δράσεις → `Seminar-Notes/EC1`

> Assets built 2026-06-07 (build_assets.py). EC0 PDFs extracted. Remaining 6 PDFs to transcribe.

| Stem | Pages | md5 | Status | Notes |
|---|---|---|---|---|
| 03a-vassart-ec-firedesign-ws | 142 | 6b24f93b | ✅ | Fire design workshop (Vassart) — EN 1991-1-2, OZone, HASEMI |
| en-1991-1-1-genikes-draseis-draseis-kata-ti-diar | 20 | 5e04b1e7 | ✅ | ΕΝ 1991-1-1 Επιβαλλόμενα — Cat A–H, qk/Qk, αA/αn, FL1–FL6, barriers |
| en-1991-1-3-genikes-draseis-fortia-chionioy | 16 | de2254c0 | ✅ | ΕΝ 1991-1-3 Χιόνι — Ζώνες A/B/Γ, sk, Ce, μi, Εφαρμ. Βόλος |
| en-1991-1-4-genikes-draseis-draseis-anemoy | 22 | 084d725d | ✅ | ΕΝ 1991-1-4 Άνεμος — vb,0=33/27, qp(z), cpe/cpi, Εφαρμ. Μαρκόπουλο |
| en-1991-1-5-genikes-draseis-thermikes-draseis | 13 | 354b733b | ✅ | ΕΝ 1991-1-5 Θερμικές — ΔTu/ΔTM, Rtot, Πίν.5.1–5.3, ΕΠ Ελλάδας |
| en-1991-1-6-genikes-draseis-draseis-kata-ti-diar | 17 | c94fda0c | ✅ | ΕΝ 1991-1-6 Κατά ανέγερση — Qca–Qcf, k-συντ., Annex A1 |

> Note: EN 1991 slides (p62–181) from `en-1990-vaseis-schediasmoy-en-1991-draseis-stis-` in EC0 folder should also be transcribed into EC1.

### EC2–EC9 (other folders)

Not yet enumerated. On first visit, run `build_assets.py "<folder>"`, then add a
detail table here from its `_manifest.json` (stems, pages, md5, duplicates).
