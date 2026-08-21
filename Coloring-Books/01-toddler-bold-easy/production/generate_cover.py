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
SAFE = 0.25 * IN
WHITE_PPI = 0.002252
SPINE_TEXT_PT = 7

YELLOW = Color(0.98, 0.82, 0.22)
NAVY = Color(0.12, 0.22, 0.38)
CORAL = Color(0.92, 0.38, 0.28)
CREAM = Color(1.0, 0.97, 0.92)
APPLE = Color(0.86, 0.22, 0.22)
TRUCK = Color(0.18, 0.55, 0.32)


def page_count() -> int:
    if COUNT_FILE.exists():
        return int(COUNT_FILE.read_text().strip())
    return 104


def _filled_ellipse(c, x, y, rx, ry, fill, stroke=NAVY, width=8) -> None:
    c.setFillColor(fill)
    c.setStrokeColor(stroke)
    c.setLineWidth(width)
    c.setLineCap(1)
    c.setLineJoin(1)
    c.ellipse(x - rx, y - ry, x + rx, y + ry, stroke=1, fill=1)


def _filled_circle(c, x, y, r, fill, stroke=NAVY, width=8) -> None:
    c.setFillColor(fill)
    c.setStrokeColor(stroke)
    c.setLineWidth(width)
    c.circle(x, y, r, stroke=1, fill=1)


def _filled_poly(c, pts, fill, stroke=NAVY, width=8) -> None:
    c.setFillColor(fill)
    c.setStrokeColor(stroke)
    c.setLineWidth(width)
    p = c.beginPath()
    p.moveTo(pts[0][0], pts[0][1])
    for px, py in pts[1:]:
        p.lineTo(px, py)
    p.close()
    c.drawPath(p, stroke=1, fill=1)


def _filled_rrect(c, x, y, w, h, r, fill, stroke=NAVY, width=8) -> None:
    c.setFillColor(fill)
    c.setStrokeColor(stroke)
    c.setLineWidth(width)
    c.roundRect(x, y, w, h, r, stroke=1, fill=1)


def hero_cat(c, x, y) -> None:
    _filled_ellipse(c, x - 115, y - 10, 48, 16, CORAL)
    _filled_ellipse(c, x, y - 20, 95, 78, CREAM)
    _filled_ellipse(c, x - 72, y - 70, 30, 38, CREAM)
    _filled_ellipse(c, x + 72, y - 70, 30, 38, CREAM)
    _filled_rrect(c, x - 45, y - 128, 30, 90, 15, CREAM)
    _filled_rrect(c, x + 15, y - 128, 30, 90, 15, CREAM)
    _filled_ellipse(c, x - 30, y - 138, 20, 11, CREAM)
    _filled_ellipse(c, x + 30, y - 138, 20, 11, CREAM)
    _filled_circle(c, x, y + 88, 58, CREAM)
    _filled_poly(c, [(x - 48, y + 122), (x - 60, y + 178), (x - 16, y + 138)], CORAL)
    _filled_poly(c, [(x + 48, y + 122), (x + 60, y + 178), (x + 16, y + 138)], CREAM)
    c.setFillColor(NAVY)
    c.setStrokeColor(NAVY)
    c.circle(x - 18, y + 90, 8, stroke=0, fill=1)
    c.circle(x + 18, y + 90, 8, stroke=0, fill=1)
    _filled_poly(c, [(x, y + 78), (x - 8, y + 68), (x + 8, y + 68)], CORAL, width=4)
    c.setStrokeColor(NAVY)
    c.setLineWidth(5)
    c.arc(x - 16, y + 68, x + 16, y + 88, 200, 140)


def mini_truck(c, x, y, scale: float = 0.45) -> None:
    c.saveState()
    c.translate(x, y)
    c.scale(scale, scale)
    _filled_rrect(c, -120, -20, 240, 70, 22, TRUCK)
    _filled_rrect(c, -70, 48, 140, 48, 16, CREAM)
    _filled_circle(c, -70, -28, 28, NAVY)
    _filled_circle(c, 70, -28, 28, NAVY)
    _filled_circle(c, -70, -28, 10, CREAM, width=4)
    _filled_circle(c, 70, -28, 10, CREAM, width=4)
    c.restoreState()


def mini_apple(c, x, y, scale: float = 0.38) -> None:
    c.saveState()
    c.translate(x, y)
    c.scale(scale, scale)
    _filled_circle(c, 0, 0, 85, APPLE)
    c.setStrokeColor(NAVY)
    c.setFillColor(NAVY)
    c.setLineWidth(8)
    c.roundRect(-6, 80, 12, 48, 6, stroke=1, fill=1)
    _filled_ellipse(c, 28, 118, 28, 14, TRUCK)
    c.restoreState()


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
    c.setFont("Helvetica-Bold", SPINE_TEXT_PT)
    c.drawCentredString(0, -2, "BIG EASY COLORING  ·  AGES 2–5")
    c.restoreState()

    cx = front_x + TRIM_W / 2
    top = BLEED + TRIM_H - SAFE
    c.setFillColor(NAVY)
    c.roundRect(cx - 70, top - 0.55 * IN, 140, 0.48 * IN, 14, stroke=0, fill=1)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(cx, top - 0.38 * IN, "AGES 2–5")

    c.setFillColor(NAVY)
    c.setFont("Helvetica-Bold", 36)
    c.drawCentredString(cx, top - 1.15 * IN, "BIG EASY")
    c.setFont("Helvetica-Bold", 28)
    c.drawCentredString(cx, top - 1.65 * IN, "COLORING BOOK")
    c.setFont("Helvetica", 16)
    c.drawCentredString(cx, top - 2.05 * IN, "for Toddlers")

    hero_cat(c, cx, BLEED + 5.05 * IN)
    mini_truck(c, cx - 2.15 * IN, BLEED + 2.55 * IN)
    mini_apple(c, cx + 2.15 * IN, BLEED + 2.65 * IN)

    c.setFillColor(NAVY)
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(cx, BLEED + 1.85 * IN, "100 SIMPLE PICTURES")
    c.setFont("Helvetica", 12)
    c.drawCentredString(cx, BLEED + 1.48 * IN, "Animals · Trucks · Foods · Everyday things")
    c.setFont("Helvetica", 11)
    c.drawCentredString(cx, BLEED + 1.12 * IN, "Thick lines for little hands")
    c.setFont("Helvetica", 10)
    c.drawCentredString(cx, BLEED + SAFE + 0.15 * IN, "UnlovedProductions")

    bx = back_x + TRIM_W / 2
    c.setFillColor(NAVY)
    c.setFont("Helvetica-Bold", 18)
    c.drawCentredString(bx, BLEED + TRIM_H - 1.6 * IN, "One big picture on every page.")
    c.setFont("Helvetica", 13)
    back_lines = [
        "100 original easy drawings for ages 2–5.",
        "Thick closed lines. Lots of space to color.",
        "Animals, trucks, foods, and everyday things.",
        "Made for crayons. Markers: put cardboard behind the page.",
        "Not a licensed character book. Original pictures only.",
    ]
    y = BLEED + TRIM_H - 2.25 * IN
    for line in back_lines:
        c.drawCentredString(bx, y, line)
        y -= 24

    # KDP auto barcode: 2" x 1.2" white box, back cover lower right.
    barcode_w, barcode_h = 2.0 * IN, 1.2 * IN
    barcode_x = back_x + TRIM_W - barcode_w
    barcode_y = BLEED
    c.setFillColor(white)
    c.setStrokeColor(white)
    c.rect(barcode_x, barcode_y, barcode_w, barcode_h, stroke=0, fill=1)

    c.setFillColor(NAVY)
    c.setFont("Helvetica", 8)
    c.drawString(back_x + SAFE, BLEED + barcode_h + 0.28 * IN, "UnlovedProductions  ·  First edition 2026")

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
                f"spine_text_pt={SPINE_TEXT_PT}",
                "barcode=KDP auto 2.0x1.2 lower-right back, left clear",
                f"output={path.name}",
                "",
            ]
        )
    )
    print(f"wrote {path} spine={pages * WHITE_PPI:.4f}in")


if __name__ == "__main__":
    main()
