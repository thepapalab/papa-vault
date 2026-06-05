"""
Bulk Document to Markdown Converter
=====================================
Converts Word (.docx, .doc), PDF, PowerPoint (.pptx), Excel (.xlsx),
Outlook emails (.msg, .eml) and more to Markdown (.md) in-place.

Requirements: pip install markitdown
"""

import sys
import subprocess
import logging
from pathlib import Path
from datetime import datetime

# ─── CONFIG ───────────────────────────────────────────────────────────────────
FOLDER     = Path(r"E:\Design Center\1. Norms and regulations\04_Articles techniques")
EXTENSIONS = {".docx", ".doc"}          # extend as needed: ".pdf", ".pptx", ".xlsx", ".msg", ".eml"
RECURSIVE  = True                        # True = scan subfolders too
OVERWRITE  = False                       # True = re-convert files that already have a .md
LOG_FILE   = FOLDER / "_conversion.log" # set to None to disable file logging
# ──────────────────────────────────────────────────────────────────────────────


def setup_logging(log_path):
    # Force UTF-8 on stdout so box-drawing chars don't crash on cp1252 consoles
    stream = open(sys.stdout.fileno(), mode="w", encoding="utf-8", buffering=1, closefd=False)
    handlers = [logging.StreamHandler(stream)]
    if log_path:
        log_path.parent.mkdir(parents=True, exist_ok=True)
        handlers.append(logging.FileHandler(log_path, encoding="utf-8"))
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s  %(levelname)-6s  %(message)s",
        datefmt="%H:%M:%S",
        handlers=handlers,
    )


def ensure_markitdown():
    try:
        from markitdown import MarkItDown
        return MarkItDown
    except ImportError:
        logging.info("markitdown not found — installing via pip...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "markitdown"])
        from markitdown import MarkItDown
        return MarkItDown


def collect_files(folder: Path, extensions: set, recursive: bool):
    pattern = "**/*" if recursive else "*"
    return sorted(
        f for f in folder.glob(pattern)
        if f.is_file() and f.suffix.lower() in extensions
    )


def convert_file(md_converter, src: Path, overwrite: bool):
    dest = src.with_suffix(".md")

    if dest.exists() and not overwrite:
        logging.info(f"SKIP    {src.relative_to(FOLDER)}")
        return "skipped"

    try:
        result = md_converter.convert(str(src))
        content = result.text_content

        if not content or not content.strip():
            logging.warning(f"EMPTY   {src.relative_to(FOLDER)}  — no text extracted, skipping")
            return "empty"

        dest.write_text(content, encoding="utf-8")
        size_kb = dest.stat().st_size / 1024
        logging.info(f"OK      {src.relative_to(FOLDER)}  →  {dest.name}  ({size_kb:.1f} KB)")
        return "ok"

    except Exception as exc:
        logging.error(f"FAIL    {src.relative_to(FOLDER)}  →  {exc}")
        return "failed"


def main():
    setup_logging(LOG_FILE)

    logging.info("=" * 60)
    logging.info(f"Bulk Markdown Converter — {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    logging.info(f"Folder    : {FOLDER}")
    logging.info(f"Extensions: {', '.join(sorted(EXTENSIONS))}")
    logging.info(f"Recursive : {RECURSIVE}")
    logging.info(f"Overwrite : {OVERWRITE}")
    logging.info("=" * 60)

    if not FOLDER.exists():
        logging.error(f"Folder not found: {FOLDER}")
        sys.exit(1)

    MarkItDown = ensure_markitdown()
    converter  = MarkItDown()

    files = collect_files(FOLDER, EXTENSIONS, RECURSIVE)
    if not files:
        logging.info("No matching files found. Nothing to do.")
        return

    logging.info(f"Found {len(files)} file(s) to process.\n")

    counts = {"ok": 0, "skipped": 0, "empty": 0, "failed": 0}

    for src in files:
        status = convert_file(converter, src, OVERWRITE)
        counts[status] += 1

    logging.info("")
    logging.info("─" * 60)
    logging.info(
        f"Finished — "
        f"{counts['ok']} converted, "
        f"{counts['skipped']} skipped, "
        f"{counts['empty']} empty, "
        f"{counts['failed']} failed."
    )
    if LOG_FILE:
        logging.info(f"Log saved to: {LOG_FILE}")
    logging.info("─" * 60)


if __name__ == "__main__":
    main()