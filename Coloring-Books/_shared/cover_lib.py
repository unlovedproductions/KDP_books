"""Shared KDP wrap-cover engine for the Big Easy coloring books.

Spec source of truth: each book's PRODUCTION_LOCKS.md (8.5x11 trim, 0.125" bleed,
white B&W paper spine = pages * 0.002252", glossy, barcode zone, text inset).
A book supplies only its colors, artwork and copy through a CoverSpec.
"""

from __future__ import annotations

import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Callable

from reportlab.lib.colors import Color, white
from reportlab.lib.units import inch as IN
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

TRIM_W = 8.5 * IN
TRIM_H = 11.0 * IN
BLEED = 0.125 * IN
SAFE = 0.25 * IN  # text inset from trim (lock: >= 0.25")
WHITE_PPI = 0.002252  # KDP official white B&W paper
SPINE_TEXT_PT = 7
DEFAULT_PAGE_COUNT = 104

NAVY = Color(0.12, 0.22, 0.38)
CREAM = Color(1.0, 0.97, 0.92)


def register_fonts(font_dir: Path) -> None:
    pdfmetrics.registerFont(TTFont("DejaVu", str(font_dir / "DejaVuSans.ttf")))
    pdfmetrics.registerFont(TTFont("DejaVuBold", str(font_dir / "DejaVuSans-Bold.ttf")))


def rewrite_embedded_fonts(path: Path) -> None:
    """Re-run the PDF through Ghostscript so every font is embedded (KDP requirement)."""
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


def filled_ellipse(c, x, y, rx, ry, fill, stroke=NAVY, width=8) -> None:
    c.setFillColor(fill)
    c.setStrokeColor(stroke)
    c.setLineWidth(width)
    c.setLineCap(1)
    c.setLineJoin(1)
    c.ellipse(x - rx, y - ry, x + rx, y + ry, stroke=1, fill=1)


def filled_circle(c, x, y, r, fill, stroke=NAVY, width=8) -> None:
    c.setFillColor(fill)
    c.setStrokeColor(stroke)
    c.setLineWidth(width)
    c.circle(x, y, r, stroke=1, fill=1)


def filled_poly(c, pts, fill, stroke=NAVY, width=8) -> None:
    c.setFillColor(fill)
    c.setStrokeColor(stroke)
    c.setLineWidth(width)
    p = c.beginPath()
    p.moveTo(pts[0][0], pts[0][1])
    for px, py in pts[1:]:
        p.lineTo(px, py)
    p.close()
    c.drawPath(p, stroke=1, fill=1)


def filled_rrect(c, x, y, w, h, r, fill, stroke=NAVY, width=8) -> None:
    c.setFillColor(fill)
    c.setStrokeColor(stroke)
    c.setLineWidth(width)
    c.roundRect(x, y, w, h, r, stroke=1, fill=1)


@dataclass(frozen=True)
class CoverSpec:
    pdf_name: str
    pdf_title: str
    background: Color
    spine_text: str
    draw_title: Callable  # (c, cx, top): title block under the AGES badge
    draw_art: Callable  # (c, cx): hero + mini pictures
    tagline: str  # line under "100 SIMPLE PICTURES"
    back_headline: str
    back_lines: list[str]
    author: str = "Unloved Productions"


def build_cover(root: Path, spec: CoverSpec) -> Path:
    """Build <root>/output/<pdf_name> from output/interior_page_count.txt (default 104 pages)."""
    register_fonts(root / "fonts")
    out = root / "output"
    count_file = out / "interior_page_count.txt"
    pages = int(count_file.read_text().strip()) if count_file.exists() else DEFAULT_PAGE_COUNT

    spine = pages * WHITE_PPI * IN
    width = BLEED + TRIM_W + spine + TRIM_W + BLEED
    height = TRIM_H + 2 * BLEED
    out.mkdir(exist_ok=True)
    path = out / spec.pdf_name
    c = canvas.Canvas(str(path), pagesize=(width, height))
    c.setTitle(spec.pdf_title)
    c.setAuthor(spec.author)

    c.setFillColor(spec.background)
    c.rect(0, 0, width, height, stroke=0, fill=1)

    back_x = BLEED
    spine_x = BLEED + TRIM_W
    front_x = BLEED + TRIM_W + spine

    # Spine
    c.setFillColor(NAVY)
    c.rect(spine_x, 0, spine, height, stroke=0, fill=1)
    c.saveState()
    c.translate(spine_x + spine / 2, height / 2)
    c.rotate(90)
    c.setFillColor(white)
    c.setFont("DejaVuBold", SPINE_TEXT_PT)
    c.drawCentredString(0, -2, spec.spine_text)
    c.restoreState()

    # Front
    cx = front_x + TRIM_W / 2
    top = BLEED + TRIM_H - SAFE
    c.setFillColor(NAVY)
    c.roundRect(cx - 70, top - 0.55 * IN, 140, 0.48 * IN, 14, stroke=0, fill=1)
    c.setFillColor(white)
    c.setFont("DejaVuBold", 16)
    c.drawCentredString(cx, top - 0.38 * IN, "AGES 2–5")

    spec.draw_title(c, cx, top)
    spec.draw_art(c, cx)

    c.setFillColor(NAVY)
    c.setFont("DejaVuBold", 16)
    c.drawCentredString(cx, BLEED + 1.85 * IN, "100 SIMPLE PICTURES")
    c.setFont("DejaVu", 12)
    c.drawCentredString(cx, BLEED + 1.48 * IN, spec.tagline)
    c.setFont("DejaVu", 11)
    c.drawCentredString(cx, BLEED + 1.12 * IN, "Thick lines for little hands")
    c.setFont("DejaVu", 10)
    c.drawCentredString(cx, BLEED + SAFE + 0.15 * IN, spec.author)

    # Back
    bx = back_x + TRIM_W / 2
    c.setFillColor(NAVY)
    c.setFont("DejaVuBold", 18)
    c.drawCentredString(bx, BLEED + TRIM_H - 1.6 * IN, spec.back_headline)
    c.setFont("DejaVu", 13)
    y = BLEED + TRIM_H - 2.25 * IN
    for line in spec.back_lines:
        c.drawCentredString(bx, y, line)
        y -= 24

    # KDP auto barcode: 2" x 1.2", >= 0.25" from spine and from trim.
    # https://kdp.amazon.com/en_US/help/topic/G5HDYGP4BXLX4RUW
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
        f"{spec.author}  ·  First edition 2026",
    )

    c.save()
    rewrite_embedded_fonts(path)
    (out / "cover_dimensions.txt").write_text(
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
    return path
