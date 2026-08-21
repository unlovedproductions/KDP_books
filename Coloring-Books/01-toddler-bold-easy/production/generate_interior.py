#!/usr/bin/env python3
"""KDP 8.5x11 no-bleed B&W interior: 4 front + 100 drawings = 104 pages."""

from __future__ import annotations

from pathlib import Path

from reportlab.lib.units import inch as IN
from reportlab.pdfgen import canvas as pdfcanvas

from drawings import PAGES, OUTER

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "output"
OUT.mkdir(exist_ok=True)

TRIM_W = 8.5 * IN
TRIM_H = 11 * IN
MARGIN = 0.50 * IN
PAGE_COUNT = 104
DRAWING_COUNT = 100


def _base(c: pdfcanvas.Canvas) -> None:
    c.setStrokeColorRGB(0, 0, 0)
    c.setFillColorRGB(0, 0, 0)


def title_page(c: pdfcanvas.Canvas) -> None:
    _base(c)
    c.setFont("Helvetica-Bold", 28)
    c.drawCentredString(TRIM_W / 2, TRIM_H - 2.1 * IN, "BIG EASY")
    c.setFont("Helvetica-Bold", 36)
    c.drawCentredString(TRIM_W / 2, TRIM_H - 2.7 * IN, "COLORING BOOK")
    c.setFont("Helvetica", 18)
    c.drawCentredString(TRIM_W / 2, TRIM_H - 3.25 * IN, "for Toddlers")
    c.setFont("Helvetica-Bold", 22)
    c.drawCentredString(TRIM_W / 2, TRIM_H - 3.85 * IN, "Ages 2–5")
    c.setLineWidth(OUTER)
    c.roundRect(2.4 * IN, 4.35 * IN, 3.7 * IN, 1.35 * IN, 12, stroke=1, fill=0)
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(TRIM_W / 2, 5.05 * IN, "100 SIMPLE PICTURES")
    c.setFont("Helvetica", 12)
    c.drawCentredString(TRIM_W / 2, 4.7 * IN, "Animals · Trucks · Foods · Everyday things")
    c.setFont("Helvetica", 11)
    c.drawCentredString(TRIM_W / 2, 1.6 * IN, "Thick lines for little hands")
    c.drawCentredString(TRIM_W / 2, 1.25 * IN, "UnlovedProductions")
    c.showPage()


def belongs_copyright(c: pdfcanvas.Canvas) -> None:
    _base(c)
    c.setFont("Helvetica-Bold", 18)
    c.drawString(MARGIN + 0.15 * IN, TRIM_H - 1.4 * IN, "This book belongs to")
    c.setLineWidth(2)
    c.line(MARGIN + 0.15 * IN, TRIM_H - 2.15 * IN, TRIM_W - MARGIN - 0.15 * IN, TRIM_H - 2.15 * IN)
    c.setFont("Helvetica", 11)
    c.drawString(MARGIN + 0.15 * IN, TRIM_H - 2.45 * IN, "Name")
    c.line(MARGIN + 0.15 * IN, TRIM_H - 3.2 * IN, TRIM_W - MARGIN - 0.15 * IN, TRIM_H - 3.2 * IN)
    c.drawString(MARGIN + 0.15 * IN, TRIM_H - 3.5 * IN, "Age")
    c.setFont("Helvetica", 10)
    y = 2.8 * IN
    lines = [
        "Copyright © 2026 UnlovedProductions. All rights reserved.",
        "ISBN 979-8-1940-3221-1",
        "KDP imprint: Independently published. Brand: UnlovedProductions.",
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
    c.setFont("Helvetica-Bold", 22)
    c.drawCentredString(TRIM_W / 2, TRIM_H - 1.5 * IN, "How to use this book")
    c.setFont("Helvetica", 14)
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
    c.setFont("Helvetica", 12)
    c.drawCentredString(TRIM_W / 2, 2.0 * IN, "100 pictures · animals, trucks, foods, everyday things")
    c.showPage()


def ready(c: pdfcanvas.Canvas) -> None:
    _base(c)
    c.setFont("Helvetica-Bold", 28)
    c.drawCentredString(TRIM_W / 2, TRIM_H / 2 + 20, "Let’s color!")
    c.setLineWidth(OUTER)
    c.circle(TRIM_W / 2, TRIM_H / 2 - 70, 40, stroke=1, fill=0)
    c.showPage()


def coloring_page(c: pdfcanvas.Canvas, label: str, draw_fn) -> None:
    _base(c)
    cx = TRIM_W / 2
    cy = TRIM_H / 2 + 0.35 * IN
    draw_fn(c, cx, cy)
    c.setFillColorRGB(0, 0, 0)
    c.setFont("Helvetica-Bold", 22)
    c.drawCentredString(TRIM_W / 2, 0.78 * IN, label)
    c.showPage()


def main() -> None:
    if len(PAGES) != DRAWING_COUNT:
        raise SystemExit(f"expected {DRAWING_COUNT} drawings, got {len(PAGES)}")
    path = OUT / "Toddler_Bold_Easy_INTERIOR.pdf"
    c = pdfcanvas.Canvas(str(path), pagesize=(TRIM_W, TRIM_H))
    c.setTitle("Big Easy Coloring Book for Toddlers Ages 2-5")
    c.setAuthor("UnlovedProductions")
    title_page(c)
    belongs_copyright(c)
    how_to(c)
    ready(c)
    for label, fn in PAGES:
        coloring_page(c, label, fn)
    c.save()
    (OUT / "interior_page_count.txt").write_text(f"{PAGE_COUNT}\n")
    print(f"wrote {path} ({PAGE_COUNT} pages)")


if __name__ == "__main__":
    main()
