#!/usr/bin/env python3
"""KDP 8.5x11 glossy wrap cover, 0.125 bleed, white B&W spine formula."""

from __future__ import annotations

import subprocess
from pathlib import Path

from reportlab.lib.colors import Color, white
from reportlab.lib.units import inch as IN
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

ROOT = Path(__file__).resolve().parent
FONT_DIR = ROOT / "fonts"
pdfmetrics.registerFont(TTFont("DejaVu", str(FONT_DIR / "DejaVuSans.ttf")))
pdfmetrics.registerFont(TTFont("DejaVuBold", str(FONT_DIR / "DejaVuSans-Bold.ttf")))
OUT = ROOT / "output"
COUNT_FILE = OUT / "interior_page_count.txt"

TRIM_W = 8.5 * IN
TRIM_H = 11.0 * IN
BLEED = 0.125 * IN
SAFE = 0.25 * IN
WHITE_PPI = 0.002252
SPINE_TEXT_PT = 7

YELLOW = Color(0.98, 0.78, 0.18)
NAVY = Color(0.12, 0.22, 0.38)
ORANGE = Color(0.93, 0.42, 0.12)
CREAM = Color(1.0, 0.97, 0.92)
STEEL = Color(0.55, 0.62, 0.68)


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


def _filled_rrect(c, x, y, w, h, r, fill, stroke=NAVY, width=8) -> None:
    c.setFillColor(fill)
    c.setStrokeColor(stroke)
    c.setLineWidth(width)
    c.roundRect(x, y, w, h, r, stroke=1, fill=1)


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


def hero_dump(c, x, y) -> None:
    _filled_rrect(c, x - 130, y + 8, 90, 80, 10, ORANGE)
    _filled_rrect(c, x - 116, y + 30, 48, 36, 8, CREAM, width=6)
    _filled_rrect(c, x - 40, y - 8, 160, 72, 12, STEEL)
    _filled_circle(c, x - 85, y - 28, 24, NAVY)
    _filled_circle(c, x + 20, y - 28, 24, NAVY)
    _filled_circle(c, x + 95, y - 28, 24, NAVY)
    _filled_circle(c, x - 85, y - 28, 9, CREAM, width=4)
    _filled_circle(c, x + 20, y - 28, 9, CREAM, width=4)
    _filled_circle(c, x + 95, y - 28, 9, CREAM, width=4)


def mini_digger(c, x, y, scale: float = 0.42) -> None:
    c.saveState()
    c.translate(x, y)
    c.scale(scale, scale)
    _filled_rrect(c, -80, -5, 130, 55, 12, ORANGE)
    _filled_rrect(c, -50, 48, 55, 42, 8, CREAM)
    _filled_rrect(c, 40, 20, 90, 22, 10, STEEL)
    _filled_poly(c, [(118, 90), (165, 70), (155, 40), (110, 70)], STEEL)
    _filled_circle(c, -55, -28, 26, NAVY)
    _filled_circle(c, 25, -28, 26, NAVY)
    c.restoreState()


def mini_cone(c, x, y, scale: float = 0.35) -> None:
    c.saveState()
    c.translate(x, y)
    c.scale(scale, scale)
    _filled_poly(c, [(-70, -60), (70, -60), (18, 110), (-18, 110)], ORANGE)
    _filled_ellipse(c, 0, -60, 80, 16, CREAM)
    c.restoreState()


def main() -> None:
    pages = page_count()
    spine = pages * WHITE_PPI * IN
    width = BLEED + TRIM_W + spine + TRIM_W + BLEED
    height = TRIM_H + 2 * BLEED
    OUT.mkdir(exist_ok=True)
    path = OUT / "Toddler_Trucks_COVER.pdf"
    c = canvas.Canvas(str(path), pagesize=(width, height))
    c.setTitle("Big Easy Trucks Coloring Book for Toddlers Ages 2-5 — Cover")
    c.setAuthor("Unloved Productions")

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
    c.setFont("DejaVuBold", SPINE_TEXT_PT)
    c.drawCentredString(0, -2, "BIG EASY TRUCKS  ·  AGES 2–5")
    c.restoreState()

    cx = front_x + TRIM_W / 2
    top = BLEED + TRIM_H - SAFE
    c.setFillColor(NAVY)
    c.roundRect(cx - 70, top - 0.55 * IN, 140, 0.48 * IN, 14, stroke=0, fill=1)
    c.setFillColor(white)
    c.setFont("DejaVuBold", 16)
    c.drawCentredString(cx, top - 0.38 * IN, "AGES 2–5")

    c.setFillColor(NAVY)
    c.setFont("DejaVuBold", 28)
    c.drawCentredString(cx, top - 1.15 * IN, "BIG EASY TRUCKS")
    c.setFont("DejaVuBold", 26)
    c.drawCentredString(cx, top - 1.62 * IN, "COLORING BOOK")
    c.setFont("DejaVu", 16)
    c.drawCentredString(cx, top - 2.02 * IN, "for Toddlers")

    hero_dump(c, cx, BLEED + 5.05 * IN)
    mini_digger(c, cx - 2.15 * IN, BLEED + 2.55 * IN)
    mini_cone(c, cx + 2.2 * IN, BLEED + 2.55 * IN)

    c.setFillColor(NAVY)
    c.setFont("DejaVuBold", 16)
    c.drawCentredString(cx, BLEED + 1.85 * IN, "100 SIMPLE PICTURES")
    c.setFont("DejaVu", 12)
    c.drawCentredString(cx, BLEED + 1.48 * IN, "Dump trucks · Diggers · Cars · Work machines")
    c.setFont("DejaVu", 11)
    c.drawCentredString(cx, BLEED + 1.12 * IN, "Thick lines for little hands")
    c.setFont("DejaVu", 10)
    c.drawCentredString(cx, BLEED + SAFE + 0.15 * IN, "Unloved Productions")

    bx = back_x + TRIM_W / 2
    c.setFillColor(NAVY)
    c.setFont("DejaVuBold", 18)
    c.drawCentredString(bx, BLEED + TRIM_H - 1.6 * IN, "One big truck on every page.")
    c.setFont("DejaVu", 13)
    back_lines = [
        "100 original easy vehicles for ages 2–5.",
        "Dump trucks, diggers, cars, and work machines.",
        "Thick closed lines. Lots of space to color.",
        "Made for crayons. Markers: put cardboard behind the page.",
        "Not a licensed brand book. Original pictures only.",
    ]
    y = BLEED + TRIM_H - 2.25 * IN
    for line in back_lines:
        c.drawCentredString(bx, y, line)
        y -= 24

    barcode_inset = 0.25 * IN
    barcode_w, barcode_h = 2.0 * IN, 1.2 * IN
    barcode_x = back_x + TRIM_W - barcode_inset - barcode_w
    c.setFillColor(white)
    c.setStrokeColor(white)
    c.rect(barcode_x, 0, barcode_w, BLEED + barcode_inset + barcode_h, stroke=0, fill=1)

    c.setFillColor(NAVY)
    c.setFont("DejaVu", 8)
    c.drawString(
        back_x + SAFE,
        BLEED + barcode_inset + barcode_h + 0.4 * IN,
        "Unloved Productions  ·  First edition 2026",
    )

    c.save()
    _rewrite_embedded_fonts(path)
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
