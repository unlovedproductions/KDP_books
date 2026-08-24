#!/usr/bin/env python3
"""KDP 8.5x11 no-bleed B&W interior: 4 front + 100 drawings = 104 pages."""

from __future__ import annotations

import subprocess
from pathlib import Path

from reportlab.lib.units import inch as IN
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas as pdfcanvas

from drawings import OUTER, PAGES, dump_truck

ROOT = Path(__file__).resolve().parent
FONT_DIR = ROOT / "fonts"
pdfmetrics.registerFont(TTFont("DejaVu", str(FONT_DIR / "DejaVuSans.ttf")))
pdfmetrics.registerFont(TTFont("DejaVuBold", str(FONT_DIR / "DejaVuSans-Bold.ttf")))
OUT = ROOT / "output"
OUT.mkdir(exist_ok=True)

TRIM_W = 8.5 * IN
TRIM_H = 11 * IN
MARGIN = 0.50 * IN
PAGE_COUNT = 104
DRAWING_COUNT = 100


def _rewrite_embedded_fonts(path: Path) -> None:
    tmp = path.with_suffix(".gs.pdf")
    subprocess.run(
        [
            "gs",
            "-q",
            "-dNOPAUSE",
            "-dBATCH",
            "-dSAFER",
            "-sDEVICE=pdfwrite",
            "-dCompatibilityLevel=1.4",
            "-dEmbedAllFonts=true",
            "-dSubsetFonts=true",
            "-dPDFSETTINGS=/prepress",
            f"-sOutputFile={tmp}",
            str(path),
        ],
        check=True,
    )
    tmp.replace(path)


def _base(c: pdfcanvas.Canvas) -> None:
    c.setStrokeColorRGB(0, 0, 0)
    c.setFillColorRGB(0, 0, 0)


def title_page(c: pdfcanvas.Canvas) -> None:
    _base(c)
    c.setFont("DejaVuBold", 28)
    c.drawCentredString(TRIM_W / 2, TRIM_H - 2.1 * IN, "BIG EASY TRUCKS")
    c.setFont("DejaVuBold", 32)
    c.drawCentredString(TRIM_W / 2, TRIM_H - 2.7 * IN, "COLORING BOOK")
    c.setFont("DejaVu", 18)
    c.drawCentredString(TRIM_W / 2, TRIM_H - 3.25 * IN, "for Toddlers")
    c.setFont("DejaVuBold", 22)
    c.drawCentredString(TRIM_W / 2, TRIM_H - 3.85 * IN, "Ages 2–5")
    c.setLineWidth(OUTER)
    c.roundRect(2.15 * IN, 4.35 * IN, 4.2 * IN, 1.35 * IN, 12, stroke=1, fill=0)
    c.setFont("DejaVuBold", 16)
    c.drawCentredString(TRIM_W / 2, 5.05 * IN, "100 SIMPLE PICTURES")
    c.setFont("DejaVu", 12)
    c.drawCentredString(TRIM_W / 2, 4.7 * IN, "Dump trucks · Diggers · Cars · Work machines")
    c.setFont("DejaVu", 11)
    c.drawCentredString(TRIM_W / 2, 1.6 * IN, "Thick lines for little hands")
    c.drawCentredString(TRIM_W / 2, 1.25 * IN, "Unloved Productions")
    c.showPage()


def belongs_copyright(c: pdfcanvas.Canvas) -> None:
    _base(c)
    c.setFont("DejaVuBold", 18)
    c.drawString(MARGIN + 0.15 * IN, TRIM_H - 1.4 * IN, "This book belongs to")
    c.setLineWidth(2)
    c.line(MARGIN + 0.15 * IN, TRIM_H - 2.15 * IN, TRIM_W - MARGIN - 0.15 * IN, TRIM_H - 2.15 * IN)
    c.setFont("DejaVu", 11)
    c.drawString(MARGIN + 0.15 * IN, TRIM_H - 2.45 * IN, "Name")
    c.line(MARGIN + 0.15 * IN, TRIM_H - 3.2 * IN, TRIM_W - MARGIN - 0.15 * IN, TRIM_H - 3.2 * IN)
    c.drawString(MARGIN + 0.15 * IN, TRIM_H - 3.5 * IN, "Age")
    c.setFont("DejaVu", 10)
    y = 2.8 * IN
    lines = [
        "Copyright © 2026 Unloved Productions. All rights reserved.",
        "ISBN 979-8-1945-6575-7",
        "KDP imprint: Independently published. Brand: Unloved Productions.",
        "Original line drawings. Not affiliated with any other brand.",
        "Printed on demand. Interior: black ink on white paper.",
        "First edition.",
    ]
    for line in lines:
        c.drawString(MARGIN + 0.15 * IN, y, line)
        y -= 16
    c.showPage()


def how_to(c: pdfcanvas.Canvas) -> None:
    _base(c)
    c.setFont("DejaVuBold", 22)
    c.drawCentredString(TRIM_W / 2, TRIM_H - 1.5 * IN, "How to use this book")
    c.setFont("DejaVu", 14)
    notes = [
        "One big picture on every page.",
        "Use crayons first. They work best on this paper.",
        "If you use markers, slide cardboard behind the page.",
        "Stay inside the thick lines — or don’t. It’s your picture.",
        "Ages 2–5. An adult should stay nearby.",
    ]
    y = TRIM_H - 2.4 * IN
    for note in notes:
        c.circle(MARGIN + 0.28 * IN, y + 4, 5, stroke=1, fill=0)
        c.drawString(MARGIN + 0.55 * IN, y, note)
        y -= 36
    c.setFont("DejaVu", 12)
    c.drawCentredString(TRIM_W / 2, 2.0 * IN, "100 pictures · trucks, diggers, cars, work machines")
    c.showPage()


def ready(c: pdfcanvas.Canvas) -> None:
    _base(c)
    c.setFont("DejaVuBold", 28)
    c.drawCentredString(TRIM_W / 2, TRIM_H / 2 + 80, "Let’s color!")
    c.setLineWidth(OUTER)
    dump_truck(c, TRIM_W / 2, TRIM_H / 2 - 50)
    c.showPage()


def coloring_page(c: pdfcanvas.Canvas, label: str, draw_fn, page_num: int) -> None:
    _base(c)
    cx = TRIM_W / 2
    if page_num % 2 == 1:
        cx += 0.12 * IN
    else:
        cx -= 0.12 * IN
    cy = TRIM_H / 2 + 0.35 * IN
    c.saveState()
    c.translate(cx, cy)
    c.scale(0.86, 0.86)
    draw_fn(c, 0, 0)
    c.restoreState()
    c.setFillColorRGB(0, 0, 0)
    c.setFont("DejaVuBold", 22)
    c.drawCentredString(TRIM_W / 2, 0.78 * IN, label)
    c.showPage()


def main() -> None:
    if len(PAGES) != DRAWING_COUNT:
        raise SystemExit(f"expected {DRAWING_COUNT} drawings, got {len(PAGES)}")
    path = OUT / "Toddler_Trucks_INTERIOR.pdf"
    c = pdfcanvas.Canvas(str(path), pagesize=(TRIM_W, TRIM_H))
    c.setTitle("Big Easy Trucks Coloring Book for Toddlers Ages 2-5")
    c.setAuthor("Unloved Productions")
    title_page(c)
    belongs_copyright(c)
    how_to(c)
    ready(c)
    for i, (label, fn) in enumerate(PAGES):
        coloring_page(c, label, fn, page_num=5 + i)
    c.save()
    _rewrite_embedded_fonts(path)
    (OUT / "interior_page_count.txt").write_text(f"{PAGE_COUNT}\n")
    print(f"wrote {path} ({PAGE_COUNT} pages)")


if __name__ == "__main__":
    main()
