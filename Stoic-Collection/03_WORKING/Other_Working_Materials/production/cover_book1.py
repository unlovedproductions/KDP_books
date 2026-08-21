#!/usr/bin/env python3
"""Build KDP full-wrap cover PDF for Book 1 (6x9, white B&W, 0.125\" bleed).

Spine text uses the KDP quality notice from Stoic Journal for Men:
0.375\" from top and bottom cover edges, and 0.0625\" from spine folds.
Does not overwrite Book 2 cover outputs.
"""

from __future__ import annotations

from pathlib import Path

from reportlab.lib.units import inch as IN
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "output"
FONT_DIR = ROOT / "fonts"
COUNT_FILE = OUT / "book1_interior_page_count.txt"

TRIM_W = 6.0 * IN
TRIM_H = 9.0 * IN
BLEED = 0.125 * IN
SAFE = 0.125 * IN
FOLD_SAFE = 0.0625 * IN
SPINE_TB = 0.375 * IN
WHITE_PPI = 0.002252


def register_fonts():
    pdfmetrics.registerFont(TTFont("LibSerif", str(FONT_DIR / "LiberationSerif-Regular.ttf")))
    pdfmetrics.registerFont(TTFont("LibSerif-Bold", str(FONT_DIR / "LiberationSerif-Bold.ttf")))
    pdfmetrics.registerFont(TTFont("LibSerif-Italic", str(FONT_DIR / "LiberationSerif-Italic.ttf")))
    pdfmetrics.registerFont(TTFont("LibSans", str(FONT_DIR / "LiberationSans-Regular.ttf")))
    pdfmetrics.registerFont(TTFont("LibSans-Bold", str(FONT_DIR / "LiberationSans-Bold.ttf")))
    pdfmetrics.registerFont(TTFont("Helvetica", str(FONT_DIR / "LiberationSans-Regular.ttf")))
    pdfmetrics.registerFont(TTFont("Helvetica-Bold", str(FONT_DIR / "LiberationSans-Bold.ttf")))


def page_count() -> int:
    if COUNT_FILE.exists():
        return int(COUNT_FILE.read_text().strip())
    return 120


def build(n: int | None = None):
    register_fonts()
    n = n or page_count()
    spine = n * WHITE_PPI * IN
    total_w = BLEED + TRIM_W + spine + TRIM_W + BLEED
    total_h = TRIM_H + 2 * BLEED

    out = OUT / "Stoic_Foundations_Book1_COVER.pdf"
    c = canvas.Canvas(str(out), pagesize=(total_w, total_h))

    c.setFillColorRGB(0.12, 0.12, 0.12)
    c.rect(0, 0, total_w, total_h, stroke=0, fill=1)

    back_x0 = BLEED
    spine_x0 = BLEED + TRIM_W
    front_x0 = BLEED + TRIM_W + spine
    trim_y0 = BLEED

    c.setFillColorRGB(0.16, 0.16, 0.16)
    c.rect(back_x0, trim_y0, TRIM_W, TRIM_H, stroke=0, fill=1)
    c.rect(front_x0, trim_y0, TRIM_W, TRIM_H, stroke=0, fill=1)
    c.setFillColorRGB(0.10, 0.10, 0.10)
    c.rect(spine_x0, trim_y0, spine, TRIM_H, stroke=0, fill=1)

    bx = back_x0 + SAFE + 0.15 * IN
    by_top = trim_y0 + TRIM_H - SAFE - 0.35 * IN

    c.setFillColorRGB(0.92, 0.92, 0.92)
    c.setFont("LibSans-Bold", 9)
    c.drawString(bx, by_top, "THE STOIC COLLECTION — BOOK 1")

    c.setFont("LibSerif-Bold", 16)
    y = by_top - 28
    c.drawString(bx, y, "Stoic Foundations")

    c.setFont("LibSerif", 10)
    y -= 22
    back_copy = [
        "A guided workbook that installs judgment, control,",
        "and assent on ordinary incidents — not slogans.",
        "",
        "SEE → SORT → OWN → CHOOSE → REVIEW is the Collection",
        "method. It is a publishing framework, not an ancient slogan.",
        "",
        "Not a quote anthology. Not a blank journal.",
        "Not Book 2 shadow work.",
    ]
    for line in back_copy:
        c.drawString(bx, y, line)
        y -= 14

    y -= 10
    c.setFont("LibSans", 8)
    c.drawString(bx, y, "Series: The Stoic Collection")
    y -= 12
    c.drawString(bx, y, "Book 2: Stoic Shadow Work Journal")
    y -= 12
    c.drawString(bx, y, "Author / Imprint: UnlovedProductions")

    bar_w, bar_h = 2.0 * IN, 1.2 * IN
    bar_x = back_x0 + TRIM_W - SAFE - bar_w
    bar_y = trim_y0 + SAFE
    c.setFillColorRGB(1, 1, 1)
    c.rect(bar_x, bar_y, bar_w, bar_h, stroke=0, fill=1)
    c.setFillColorRGB(0.45, 0.45, 0.45)
    c.setFont("LibSans", 7)
    c.drawCentredString(bar_x + bar_w / 2, bar_y + bar_h / 2 - 3, "KDP BARCODE ZONE")

    cx = spine_x0 + spine / 2
    c.saveState()
    c.translate(cx, trim_y0 + TRIM_H / 2)
    c.rotate(90)
    c.setFillColorRGB(0.95, 0.95, 0.95)
    max_spine_text = TRIM_H - 2 * SPINE_TB
    c.setFont("LibSans-Bold", 9)
    spine_label = "STOIC FOUNDATIONS  ·  UnlovedProductions"
    tw = c.stringWidth(spine_label, "LibSans-Bold", 9)
    if tw > max_spine_text - 4:
        spine_label = "STOIC FOUNDATIONS"
        tw = c.stringWidth(spine_label, "LibSans-Bold", 9)
    if spine > 2 * FOLD_SAFE + 6:
        c.drawCentredString(0, -3, spine_label)
    c.restoreState()

    fx = front_x0 + SAFE + 0.2 * IN
    fy = trim_y0 + TRIM_H - SAFE - 0.55 * IN
    c.setFillColorRGB(0.93, 0.93, 0.93)
    c.setFont("LibSans-Bold", 10)
    c.drawString(fx, fy, "THE STOIC COLLECTION — BOOK 1")

    c.setFont("LibSerif-Bold", 26)
    fy -= 42
    c.drawString(fx, fy, "STOIC")
    fy -= 30
    c.drawString(fx, fy, "FOUNDATIONS")

    c.setFont("LibSerif-Italic", 11)
    fy -= 28
    for line in [
        "A Guided Workbook on Judgment,",
        "Control, and Assent",
    ]:
        c.drawString(fx, fy, line)
        fy -= 15

    fy -= 36
    c.setStrokeColorRGB(0.75, 0.75, 0.75)
    c.setLineWidth(0.7)
    c.line(fx, fy, fx + 2.2 * IN, fy)

    fy -= 28
    c.setFont("LibSans", 10)
    c.setFillColorRGB(0.9, 0.9, 0.9)
    c.drawString(fx, fy, "SEE · SORT · OWN · CHOOSE · REVIEW")

    c.setFont("LibSerif", 12)
    c.drawString(fx, trim_y0 + SAFE + 0.45 * IN, "UnlovedProductions")

    c.setTitle("Stoic Foundations — Cover Wrap")
    c.setAuthor("UnlovedProductions")
    c.showPage()
    c.save()

    meta = OUT / "book1_cover_dimensions.txt"
    meta.write_text(
        "\n".join(
            [
                f"page_count={n}",
                f"paper=white_bw",
                f"spine_in={n * WHITE_PPI:.6f}",
                f"trim=6x9",
                f"bleed=0.125",
                f"spine_top_bottom_in=0.375",
                f"spine_fold_in=0.0625",
                f"total_width_in={(total_w / IN):.6f}",
                f"total_height_in={(total_h / IN):.6f}",
                f"formula=spine=pages*0.002252 (KDP official white)",
                f"output={out.name}",
                "",
            ]
        ),
        encoding="utf-8",
    )
    print(f"Wrote {out}")
    print(f"Pages={n} spine={n * WHITE_PPI:.6f}\" wrap={total_w / IN:.4f}\" x {total_h / IN:.4f}\"")
    return out


if __name__ == "__main__":
    build()
