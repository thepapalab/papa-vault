"""
Eurocode Seminar Notes — asset & scaffold builder
=================================================
Cheap, deterministic prep step before vision transcription. For one source
folder it:
  * enumerates the PDFs, computes MD5, flags byte-identical duplicates
  * proposes a clean ASCII stem per PDF (chN / partN / transliterated)
  * renders every page to  <output>/_assets/<stem>/pNNN.png   (paste library)
  * dumps extracted text to <output>/_scaffold/<stem>.txt      (cheap reading)
  * writes <output>/_manifest.json  (machine state for resuming)

It does NOT do any transcription — that is the agent's job (see RUNBOOK.md).
No vision tokens are spent here.

Usage (use the interpreter that has PyMuPDF):
    PY="C:/Users/n_pap/.ai-navigator/micromamba/envs/cuda/python.exe"
    & $PY build_assets.py "EC2 - Κατασκευές από Οπλισμένο Σκυρόδεμα"
    & $PY build_assets.py --dry-run "EC2 ..."   # enumerate only, no writes
    & $PY build_assets.py --list                # list all source folders
"""
import argparse
import hashlib
import json
import os
import re
import sys
import io

import fitz  # PyMuPDF

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

ROOT = (r"H:\Backup\2_Work Backup\Design Center\1. Codes"
        r"\Βοηθητικό Υλικό - Ευροκώδικες")
VAULT = r"C:\Users\n_pap\Documents\PapaLab\Papa_Vault"
OUTPUT_BASE = os.path.join(VAULT, "Methodology", "Seminar-Notes")

# Folders whose output lives somewhere other than OUTPUT_BASE/<slug>.
OUTPUT_OVERRIDES = {
    "EC2 - Κατασκευές από Οπλισμένο Σκυρόδεμα":
        os.path.join(VAULT, "Methodology", "EC2-Concrete",
                     "Seminar-Notes-Penelis"),
}

RENDER_ZOOM = 2.5  # ~180 dpi; good enough to read/paste a figure

# Minimal Greek -> Latin transliteration for ASCII slugs/paths.
_GR = {
    "α": "a", "β": "v", "γ": "g", "δ": "d", "ε": "e", "ζ": "z", "η": "i",
    "θ": "th", "ι": "i", "κ": "k", "λ": "l", "μ": "m", "ν": "n", "ξ": "x",
    "ο": "o", "π": "p", "ρ": "r", "σ": "s", "ς": "s", "τ": "t", "υ": "y",
    "φ": "f", "χ": "ch", "ψ": "ps", "ω": "o", "ά": "a", "έ": "e", "ή": "i",
    "ί": "i", "ό": "o", "ύ": "y", "ώ": "o", "ϊ": "i", "ϋ": "y",
}


def translit(text: str) -> str:
    out = "".join(_GR.get(c, _GR.get(c.lower(), c)) for c in text)
    out = re.sub(r"[^A-Za-z0-9]+", "-", out).strip("-").lower()
    return out[:48] or "doc"


def propose_stem(filename: str) -> str:
    name = os.path.splitext(filename)[0]
    low = name.lower()
    m = re.search(r"κεφ\.?\s*([0-9]+(?:\s*[-–]\s*[0-9]+)?)", low)
    if m:
        stem = "ch" + re.sub(r"\s*[-–]\s*", "-", m.group(1))
    elif "γέφυρ" in low or "μέρος 2" in low or "part 2" in low:
        stem = "part2-bridges"
    else:
        stem = translit(name)
    if "σημει" in low:
        stem += "-notes"
    return stem


def md5_of(path: str) -> str:
    h = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def resolve_folder(arg: str) -> str:
    if os.path.isdir(arg):
        return arg
    cand = os.path.join(ROOT, arg)
    if os.path.isdir(cand):
        return cand
    # partial / prefix match against children of ROOT
    matches = [d for d in os.listdir(ROOT)
               if os.path.isdir(os.path.join(ROOT, d))
               and arg.lower() in d.lower()]
    if len(matches) == 1:
        return os.path.join(ROOT, matches[0])
    if not matches:
        sys.exit(f"No source folder matches: {arg!r}")
    sys.exit("Ambiguous folder, matches: " + " | ".join(matches))


def output_dir_for(folder_name: str) -> str:
    if folder_name in OUTPUT_OVERRIDES:
        return OUTPUT_OVERRIDES[folder_name]
    key = folder_name.split(" - ")[0].strip()
    return os.path.join(OUTPUT_BASE, translit(key).upper() or translit(key))


def list_folders():
    for d in sorted(os.listdir(ROOT)):
        if os.path.isdir(os.path.join(ROOT, d)):
            n = len([f for f in os.listdir(os.path.join(ROOT, d))
                     if f.lower().endswith(".pdf")])
            print(f"  [{n:2d} pdf] {d}")


def build(folder: str, dry_run: bool, force: bool):
    fname = os.path.basename(folder.rstrip("\\/"))
    outdir = output_dir_for(fname)
    pdfs = sorted(f for f in os.listdir(folder) if f.lower().endswith(".pdf"))

    print(f"Folder : {fname}")
    print(f"Output : {outdir}")
    print(f"PDFs   : {len(pdfs)}\n")

    seen_md5: dict[str, str] = {}
    entries = []
    for pdf in pdfs:
        src = os.path.join(folder, pdf)
        digest = md5_of(src)
        stem = propose_stem(pdf)
        dup = seen_md5.get(digest)
        doc = fitz.open(src)
        pages = doc.page_count
        entry = {
            "file": pdf, "md5": digest, "pages": pages, "stem": stem,
            "duplicate_of": dup,
            "assets_dir": f"_assets/{stem}",
            "scaffold": f"_scaffold/{stem}.txt",
            "output_md": f"{stem}.md",
            "status": "duplicate" if dup else "assets_pending",
        }
        flag = f"  DUPLICATE of {dup}" if dup else ""
        print(f"  {stem:24s} {pages:3d}p  {digest[:8]}{flag}")
        if dup:
            doc.close()
            entries.append(entry)
            continue
        seen_md5[digest] = stem

        if not dry_run:
            adir = os.path.join(outdir, "_assets", stem)
            sdir = os.path.join(outdir, "_scaffold")
            os.makedirs(adir, exist_ok=True)
            os.makedirs(sdir, exist_ok=True)
            scaffold = []
            for i in range(pages):
                page = doc[i]
                png = os.path.join(adir, f"p{i + 1:03d}.png")
                if force or not os.path.exists(png):
                    pix = page.get_pixmap(
                        matrix=fitz.Matrix(RENDER_ZOOM, RENDER_ZOOM))
                    pix.save(png)
                scaffold.append(f"=== p{i + 1:03d} ===\n{page.get_text()}")
            with open(os.path.join(outdir, entry["scaffold"]), "w",
                      encoding="utf-8") as f:
                f.write("\n".join(scaffold))
            entry["status"] = "assets_ready"
        doc.close()
        entries.append(entry)

    if dry_run:
        print("\n(dry run — nothing written)")
        return

    os.makedirs(outdir, exist_ok=True)
    manifest = {"folder": fname, "output_dir": outdir, "pdfs": entries}
    with open(os.path.join(outdir, "_manifest.json"), "w",
              encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    print(f"\nWrote {os.path.join(outdir, '_manifest.json')}")
    print("Assets + scaffold ready. Next: transcribe per RUNBOOK.md.")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("folder", nargs="?", help="source folder (name or path)")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--force", action="store_true",
                    help="re-render existing PNGs")
    ap.add_argument("--list", action="store_true",
                    help="list source folders and exit")
    args = ap.parse_args()
    if args.list:
        list_folders()
        return
    if not args.folder:
        ap.error("provide a folder, or use --list")
    build(resolve_folder(args.folder), args.dry_run, args.force)


if __name__ == "__main__":
    main()
