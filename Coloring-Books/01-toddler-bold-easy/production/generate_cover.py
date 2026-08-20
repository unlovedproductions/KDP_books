#!/usr/bin/env python3
"""KDP 8.5x11 glossy wrap cover, 0.125 bleed, white B&W spine formula."""

from __future__ import annotations

from pathlib import Path

from reportlab.lib.colors import Color, white
from reportlab.lib.units import inch as IN
from reportlab.pdfgen import canvas

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "output"
COUNT_FILE = OUT / "interior_page_count.txt"

TRIM_W = 8.5 * IN
TRIM_H = 11.0 * IN
BLEED = 0.125 * IN
SAFE = 0.125 * IN
WHITE_PPI = 0.002252

YELLOW = Color(0.98, 0.82, 0.22)
NAVY = Color(0.12, 0.22, 0.38)
CORAL = Color(0.92, 0.38, 0.28)


def page_count() -> int:
    if COUNT_FILE.exists():
        return int(COUNT_FILE.read_text().strip())
    return 104


def main() -> None:
    pages = page_count()
    spine = pages * WHITE_PPI * IN
    width = BLEED + TRIM_W + spine + TRIM_W + BLEED
    height = TRIM_H + 2 * BLEED
    OUT.mkdir(exist_ok=True)
    path = OUT / "Toddler_Bold_Easy_COVER.pdf"
    c = canvas.Canvas(str(path), pagesize=(width, height))
    c.setTitle("Big Easy Coloring Book for Toddlers Ages 2-5 — Cover")
    c.setAuthor("UnlovedProductions")

    c.setFillColor(YELLOW)
    c.rect(0, 0, width, height, stroke=0, fill=1)

    back_x = BLEED
    spine_x = BLEED + TRIM_W
    front_x = BLEED + TRIM_W + spine

    c.setFillColor(NAVY)
    c.rect(spine_x, 0, spine, height, stroke=0, fill=1)
    c.saveState()
    c.translate(spine_x + spine / 2, height / 2)
    c.rotate(90)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 9)
    c.drawCentredString(0, -3, "BIG EASY COLORING  ·  AGES 2–5")
    c.restoreState()

    def front_text(x0: float) -> None:
        cx = x0 + TRIM_W / 2
        c.setFillColor(NAVY)
        c.setFont("Helvetica-Bold", 18)
        c.drawCentredString(cx, BLEED + TRIM_H - 1.15 * IN, "AGES 2–5")
        c.setFont("Helvetica-Bold", 32)
        c.drawCentredString(cx, BLEED + TRIM_H - 1.85 * IN, "BIG EASY")
        c.setFont("Helvetica-Bold", 26)
        c.drawCentredString(cx, BLEED + TRIM_H - 2.4 * IN, "COLORING BOOK")
        c.setFont("Helvetica", 14)
        c.drawCentredString(cx, BLEED + TRIM_H - 2.85 * IN, "for Toddlers")

        c.setStrokeColor(NAVY)
        c.setFillColor(white)
        c.setLineWidth(8)
        c.setLineCap(1)
        c.setLineJoin(1)
        x = cx
        y = BLEED + 5.15 * IN
        c.ellipse(x - 95, y - 90, x + 95, y + 50, stroke=1, fill=0)
        c.circle(x + 70, y + 70, 55, stroke=1, fill=0)
        c.setFillColor(CORAL)
        ear = c.beginPath()
        ear.moveTo(x + 40, y + 110)
        ear.lineTo(x + 28, y + 165)
        ear.lineTo(x + 70, y + 125)
        ear.close()
        c.drawPath(ear, stroke=1, fill=1)
        c.setFillColor(white)
        ear2 = c.beginPath()
        ear2.moveTo(x + 100, y + 110)
        ear2.lineTo(x + 130, y + 165)
        ear2.lineTo(x + 112, y + 120)
        ear2.close()
        c.drawPath(ear2, stroke=1, fill=0)
        c.circle(x + 55, y + 78, 8, stroke=1, fill=0)
        c.circle(x + 88, y + 78, 8, stroke=1, fill=0)
        c.arc(x + 50, y + 50, x + 90, y + 72, 200, 140)
        c.line(x - 95, y - 40, x - 95, y - 110)
        c.line(x - 50, y - 70, x - 50, y - 120)
        c.line(x + 40, y - 70, x + 40, y - 120)
        c.line(x + 80, y - 40, x + 80, y - 110)
        c.arc(x - 150, y - 10, x - 80, y + 50, 20, 160)

        c.setFillColor(NAVY)
        c.setFont("Helvetica-Bold", 16)
        c.drawCentredString(cx, BLEED + 2.15 * IN, "100 SIMPLE PICTURES")
        c.setFont("Helvetica", 12)
        c.drawCentredString(cx, BLEED + 1.75 * IN, "Animals · Trucks · Foods · Everyday things")
        c.setFont("Helvetica", 11)
        c.drawCentredString(cx, BLEED + 1.35 * IN, "Thick lines for little hands")
        c.setFont("Helvetica", 10)
        c.drawCentredString(cx, BLEED + 0.85 * IN, "UnlovedProductions")

    front_text(front_x)

    c.setFillColor(NAVY)
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(back_x + TRIM_W / 2, BLEED + TRIM_H - 2.0 * IN, "One big picture on every page.")
    c.setFont("Helvetica", 12)
    back_lines = [
        "100 original easy drawings for ages 2–5.",
        "Thick lines. Lots of space to color.",
        "Animals, trucks, foods, and everyday things.",
        "Made for crayons. (Markers: put cardboard behind the page.)",
    ]
    y = BLEED + TRIM_H - 2.7 * IN
    for line in back_lines:
        c.drawCentredString(back_x + TRIM_W / 2, y, line)
        y -= 22

    c.setFillColor(NAVY)
    c.setFont("Helvetica", 8)
    c.drawCentredString(back_x + TRIM_W / 2, BLEED + 0.85 * IN, "UnlovedProductions  ·  First edition 2026")

    c.save()
    dim = OUT / "cover_dimensions.txt"
    dim.write_text(
        "\n".join(
            [
                f"page_count={pages}",
                "paper=white_bw",
                f"spine_in={pages * WHITE_PPI:.6f}",
                "trim=8.5x11",
                "bleed=0.125",
                f"total_width_in={(width / IN):.6f}",
                f"total_height_in={(height / IN):.6f}",
                "formula=spine=pages*0.002252 (KDP official white)",
                f"output={path.name}",
                "",
            ]
        )
    )
    print(f"wrote {path} spine={pages * WHITE_PPI:.4f}in")


if __name__ == "__main__":
    main()
