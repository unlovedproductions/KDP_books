#!/usr/bin/env python3
"""Wrap cover for the cream-paper sudoku paperback.

Spine uses the official cream / groundwood factor, 0.0025 inch per page.
Do not use the white-paper factor from the coloring-book cover engine.
"""

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

TRIM_W = 8.5 * IN
TRIM_H = 11.0 * IN
BLEED = 0.125 * IN
SAFE = 0.25 * IN
CREAM_PPI = 0.0025
SPINE_TEXT_MIN_PAGES = 79

NAVY = Color(0.08, 0.13, 0.24)
CREAM = Color(0.98, 0.95, 0.88)


def rewrite_embedded_fonts(path: Path) -> None:
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


def _draw_empty_grid(c: canvas.Canvas, left: float, bottom: float, size: float) -> None:
    cell = size / 9
    c.setStrokeColor(white)
    c.setFillColor(white)
    c.setLineWidth(1.2)
    c.rect(left, bottom, size, size, stroke=1, fill=0)
    for i in range(1, 9):
        c.setLineWidth(2.4 if i % 3 == 0 else 0.9)
        c.line(left + i * cell, bottom, left + i * cell, bottom + size)
        c.line(left, bottom + i * cell, left + size, bottom + i * cell)
    c.setLineWidth(2.6)
    c.rect(left, bottom, size, size, stroke=1, fill=0)


def build() -> Path:
    out = ROOT / "output"
    count_file = out / "interior_page_count.txt"
    pages = int(count_file.read_text().strip())
    if pages % 2 != 0:
        raise SystemExit(f"interior page count {pages} is odd")
    spine = pages * CREAM_PPI * IN
    width = BLEED + TRIM_W + spine + TRIM_W + BLEED
    height = TRIM_H + 2 * BLEED
    path = out / "Large_Print_Sudoku_Poor_Vision_COVER.pdf"
    c = canvas.Canvas(str(path), pagesize=(width, height))
    c.setTitle("Large Print Sudoku for Seniors with Poor Vision — cover")
    c.setAuthor("Unloved Productions")

    c.setFillColor(NAVY)
    c.rect(0, 0, width, height, stroke=0, fill=1)

    back_x = BLEED
    spine_x = BLEED + TRIM_W
    front_x = BLEED + TRIM_W + spine

    c.setFillColor(Color(0.05, 0.08, 0.16))
    c.rect(spine_x, 0, spine, height, stroke=0, fill=1)
    if pages > SPINE_TEXT_MIN_PAGES:
        spine_text = "LARGE PRINT SUDOKU FOR SENIORS WITH POOR VISION"
        c.saveState()
        c.translate(spine_x + spine / 2, height / 2)
        c.rotate(90)
        c.setFillColor(white)
        c.setFont("DejaVuBold", 7)
        if c.stringWidth(spine_text, "DejaVuBold", 7) > TRIM_H - 0.6 * IN:
            raise SystemExit("spine text is wider than the spine length")
        c.drawCentredString(0, -2.5, spine_text)
        c.restoreState()

    cx = front_x + TRIM_W / 2
    c.setFillColor(white)
    c.setFont("DejaVuBold", 22)
    c.drawCentredString(cx, BLEED + TRIM_H - 0.85 * IN, "LARGE PRINT")
    c.setFont("DejaVuBold", 40)
    c.drawCentredString(cx, BLEED + TRIM_H - 1.55 * IN, "SUDOKU")
    c.setFont("DejaVuBold", 22)
    c.drawCentredString(cx, BLEED + TRIM_H - 2.15 * IN, "FOR SENIORS")
    c.drawCentredString(cx, BLEED + TRIM_H - 2.6 * IN, "WITH POOR VISION")
    c.setStrokeColor(CREAM)
    c.setLineWidth(2)
    c.line(front_x + SAFE, BLEED + TRIM_H - 2.95 * IN, front_x + TRIM_W - SAFE, BLEED + TRIM_H - 2.95 * IN)
    c.setFillColor(CREAM)
    c.setFont("DejaVu", 13)
    c.drawCentredString(cx, BLEED + TRIM_H - 3.35 * IN, "40 easy puzzles  ·  one giant grid per page")
    c.drawCentredString(cx, BLEED + TRIM_H - 3.65 * IN, "Blank back behind every puzzle")
    grid = 5.2 * IN
    _draw_empty_grid(c, cx - grid / 2, BLEED + 1.7 * IN, grid)
    c.setFillColor(white)
    c.setFont("DejaVu", 11)
    c.drawCentredString(cx, BLEED + 0.72 * IN, "Unloved Productions")

    bx = back_x + TRIM_W / 2
    c.setFillColor(white)
    c.setFont("DejaVuBold", 18)
    c.drawCentredString(bx, BLEED + TRIM_H - 1.15 * IN, "One grid. Blank back.")
    c.setFillColor(CREAM)
    c.setFont("DejaVu", 13)
    back_lines = [
        "40 easy sudoku puzzles.",
        "Each puzzle is one giant grid.",
        "The other side of that page is blank,",
        "so the next puzzle does not show through.",
        "Solutions are full size, after the puzzles.",
        "Cream paper. 8.5 x 11 inches.",
    ]
    y = BLEED + TRIM_H - 1.7 * IN
    for line in back_lines:
        c.drawCentredString(bx, y, line)
        y -= 22

    barcode_w, barcode_h = 2.0 * IN, 1.2 * IN
    barcode_inset = 0.25 * IN
    barcode_x = back_x + TRIM_W - barcode_inset - barcode_w
    c.setFillColor(white)
    c.rect(barcode_x, 0, barcode_w, BLEED + barcode_inset + barcode_h, stroke=0, fill=1)
    c.setFillColor(CREAM)
    c.setFont("DejaVu", 8)
    c.drawString(back_x + SAFE, BLEED + barcode_inset + barcode_h + 0.35 * IN, "Unloved Productions  ·  First edition 2026")

    c.save()
    rewrite_embedded_fonts(path)
    (out / "cover_dimensions.txt").write_text(
        "\n".join(
            [
                f"page_count={pages}",
                "paper=cream_bw",
                f"spine_in={pages * CREAM_PPI:.6f}",
                "trim=8.5x11",
                "bleed=0.125",
                f"total_width_in={(width / IN):.6f}",
                f"total_height_in={(height / IN):.6f}",
                "formula=spine=pages*0.0025 (KDP official cream)",
                "spine_text_pt=7",
                "barcode=KDP auto 2.0x1.2 lower-right back, 0.25in clear",
                f"output={path.name}",
                "",
            ]
        )
    )
    print(f"wrote {path} spine={pages * CREAM_PPI:.4f}in")
    return path


if __name__ == "__main__":
    build()
