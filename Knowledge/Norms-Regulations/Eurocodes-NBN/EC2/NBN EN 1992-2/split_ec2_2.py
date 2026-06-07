# -*- coding: utf-8 -*-
"""
Split NBN EN 1992-2:2005 (F) raw-OCR markdown into chapter notes.
Per NORM-PROCESSING-AGENT.md: raw OCR -> pre-clean (watermarks + page
furniture) -> insert ## headings at the real chapter boundaries -> split.
Chapter boundaries are taken from confirmed line anchors so the Sommaire TOC
and the English AC:2008 sub-headers are NOT mistaken for chapters.
"""
import re
from pathlib import Path

FOLDER = Path(__file__).resolve().parent
SRC = FOLDER / "NBN EN 1992-2-2005-2_F.md"
lines = SRC.read_text(encoding="utf-8").splitlines()

# --- watermark strings (reversed-French OCR stamp) ---
WM1 = ("el in ,eitrap ne uo tnemelargétni tios unetnoc nos reilbup in eriudorper "
       "sap en à egagne's eb.liarcut@SORBALAPAP.salociN .LIAR à NBN el rap ecnecil "
       "suos énnod te ruetua 'd stiord sel rus iol al rap égétorp tse tnemucod eC")
WM2 = ".sreit sed à etnenamrep uo eriaropmet noçaf ed elbinopsid erdner"

TOKENS = {"ne","uo","tnemelargétni","tios","unetnoc","nos","reilbup","in",
          "eriudorper","sap","en","à","egagne's","eb.liarcut@SORBALAPAP.salociN",
          "salociN",".LIAR","NBN","el rap","el","ecnecil","suos","énnod","te",
          "ruetua","'d","stiord","sel","rus","iol","al","rap","égétorp","tse",
          "tnemucod","eC",".sreit","sed","etnenamrep","eriaropmet","noçaf","ed",
          "elbinopsid","erdner"}

FURNITURE = [
    re.compile(r"^EN 1992-2 : 2005 \(F\)$"),
    re.compile(r"^EN 1992-2:2005/AC:2008 \(E\)$"),
    re.compile(r"^Page \d+$"),
    re.compile(r"^\d{1,3}$"),
]

def clean(seg):
    out = []
    for ln in seg:
        s = ln.replace(WM1, "").replace(WM2, "")
        if s != ln:                       # a watermark substring was present
            rem = re.sub(r"[|\-\s]", "", s)
            if len(rem) <= 2:             # only stray chars / broken table cells left
                s = ""
        out.append(s.rstrip())
    # drop contiguous runs (>=6) of broken-block watermark tokens
    keep = [True] * len(out)
    i = 0
    while i < len(out):
        if out[i].strip() in TOKENS:
            j = i
            while j < len(out) and out[j].strip() in TOKENS:
                j += 1
            if j - i >= 6:
                for k in range(i, j):
                    keep[k] = False
            i = j
        else:
            i += 1
    out = [o for o, k in zip(out, keep) if k]
    # drop page furniture
    out = [o for o in out if not any(p.match(o) for p in FURNITURE)]
    # collapse blank runs, trim ends
    res = []
    for o in out:
        if o.strip() == "":
            if res and res[-1] == "":
                continue
            res.append("")
        else:
            res.append(o)
    while res and res[0] == "":
        res.pop(0)
    while res and res[-1] == "":
        res.pop()
    return res

# (1-based start line, chapter title) -- confirmed against the source body
anchors = [
    (334,  "Section 1 — Généralités"),
    (655,  "Section 2 — Bases de calcul"),
    (664,  "Section 3 — Matériaux"),
    (761,  "Section 4 — Durabilité et enrobage des armatures"),
    (821,  "Section 5 — Analyse structurale"),
    (1088, "Section 6 — États limites ultimes (ELU)"),
    (2005, "Section 7 — États limites de service (ELS)"),
    (2244, "Section 8 — Dispositions constructives relatives aux armatures de béton armé et de précontrainte — Généralités"),
    (2353, "Section 9 — Dispositions constructives relatives aux éléments et règles particulières"),
    (2455, "Section 10 — Règles additionnelles pour les éléments et les structures préfabriqués en béton"),
    (2500, "Section 11 — Structures en béton de granulats légers"),
    (2529, "Section 12 — Structures en béton non armé ou faiblement armé"),
    (2535, "Section 113 — Calcul des phases d'exécution"),
    (2607, "Annexe A — Modification des coefficients partiels relatifs aux matériaux"),
    (2616, "Annexe B — Déformations dues au fluage et au retrait"),
    (3054, "Annexe C — Propriétés des armatures compatibles avec l'utilisation de cet Eurocode"),
    (3063, "Annexe D — Méthode de calcul détaillée des pertes de précontrainte par relaxation"),
    (3072, "Annexe E — Classes indicatives de résistance pour la durabilité"),
    (3082, "Annexe F — Expressions pour le calcul des armatures tendues dans les situations de contraintes planes"),
    (3180, "Annexe G — Interaction sol-structure"),
    (3188, "Annexe H — Effets globaux du second ordre sur les structures"),
    (3196, "Annexe I — Analyse des planchers-dalles et des voiles de contreventement"),
    (3213, "Annexe J — Dispositions constructives pour des cas particuliers"),
    (3325, "Annexe KK — Effets structurels induits par le comportement différé du béton"),
    (3652, "Annexe LL — Éléments de plaque en béton"),
    (4170, "Annexe MM — Effort tranchant et flexion transversale"),
    (4315, "Annexe NN — Étendue de contrainte équivalente vis-à-vis de l'endommagement pour les vérifications à la fatigue"),
    (4904, "Annexe OO — Régions de discontinuité types pour les ponts"),
    (5026, "Annexe PP — Format de sécurité pour l'analyse non linéaire"),
    (5191, "Annexe QQ — Maîtrise de la fissuration par cisaillement des âmes"),
    (5229, "Corrigendum EN 1992-2:2005/AC:2008"),
]

def slug(t):
    t = t.replace("—", "-")
    t = re.sub(r'[\\/:*?"<>|]', "", t)
    t = re.sub(r"\s+", " ", t).strip()
    return t[:80]

ARCHIVE_STEM = "NBN EN 1992-2-2005-2_F — FULL (archive)"

# ---- chapter files ----
struct_rows = []
for idx, (start, title) in enumerate(anchors, start=1):
    end = anchors[idx][0] if idx < len(anchors) else len(lines) + 1
    seg = lines[start - 1:end - 1]
    body = clean(seg)
    nn = f"{idx:02d}"
    fname = f"{nn} - {slug(title)}.md"
    header = f'---\nparent: "[[00 - Index]]"\nnorm: "NBN EN 1992-2:2005"\n---\n\n'
    content = header + f"## {title}\n\n" + "\n".join(body) + "\n"
    (FOLDER / fname).write_text(content, encoding="utf-8")
    struct_rows.append(f"| [[{fname[:-3]}]] | {title} |")
    print(fname)

# ---- index (00) ----
preamble = clean(lines[0:333])
fm = (
    "---\n"
    'title: "NBN EN 1992-2:2005 — Index"\n'
    'source: "NBN EN 1992-2:2005 (+ AC:2008) — Eurocode 2 — Calcul des structures en béton — '
    'Partie 2 : Ponts en béton — Calcul et dispositions constructives, Bureau de Normalisation, '
    '2e éd. décembre 2005, version française. Annexe Nationale NBN EN 1992-2 ANB:2014."\n'
    "norm: EC2-2\n"
    "date: 2005-12\n"
    'replaces: "NBN ENV 1992-2:2001"\n'
    "status: en vigueur\n"
    "tags: [EC2-2, eurocode-2, ponts-beton, beton-arme, precontrainte, index]\n"
    'related: ["[[_Norms-Regulations — README]]", "[[_Knowledge — Index]]"]\n'
    "created: 2026-06-07\n"
    "---\n\n"
)
intro = (
    "# NBN EN 1992-2:2005 — Index\n\n"
    "EN 1992-2:2005 constitue la Partie 2 de l'Eurocode 2 (Calcul des structures en béton) et "
    "couvre les ponts en béton. Elle complète et modifie l'EN 1992-1-1 : les clauses portant "
    "modification sont numérotées en ajoutant `100` au numéro de l'EN 1992-1-1, les clauses "
    "complémentaires en ajoutant `101`. La version belge inclut l'Annexe Nationale ANB:2014 "
    "(caractère normatif) et le corrigendum AC:2008. Elle comprend les sections 1 à 12 plus la "
    "section 113 (phases d'exécution) et les annexes A à QQ (A–J reprises de l'EN 1992-1-1, "
    "KK–QQ propres aux ponts).\n\n"
    "## Structure\n\n"
    "| Fichier | Titre |\n|---------|-------|\n"
    + "\n".join(struct_rows)
    + "\n\n---\n\n"
    "## Pages liminaires (avant-propos national, sommaire, avant-propos européen, "
    "annexe nationale)\n\n"
)
(FOLDER / "00 - Index.md").write_text(fm + intro + "\n".join(preamble) + "\n", encoding="utf-8")
print("00 - Index.md")

# ---- archive original ----
SRC.rename(FOLDER / f"{ARCHIVE_STEM}.md")
print(f"\nArchived -> {ARCHIVE_STEM}.md")
print(f"Chapters: {len(anchors)}")
