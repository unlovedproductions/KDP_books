#!/usr/bin/env python3
"""KDP 8.5x11 no-bleed B&W interior: 4 front + 100 drawings = 104 pages."""

from __future__ import annotations

import subprocess
from math import cos, radians, sin
from pathlib import Path

from reportlab.lib.units import inch as IN
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas as pdfcanvas

from drawings import PAGES, OUTER

ROOT = Path(__file__).resolve().parent
FONT_DIR = ROOT / "fonts"
pdfmetrics.registerFont(TTFont("DejaVu", str(FONT_DIR / "DejaVuSans.ttf")))
pdfmetrics.registerFont(TTFont("DejaVuBold", str(FONT_DIR / "DejaVuSans-Bold.ttf")))
FONT = "DejaVu"
FONT_BOLD = "DejaVuBold"
OUT = ROOT / "output"
OUT.mkdir(exist_ok=True)

TRIM_W = 8.5 * IN
TRIM_H = 11 * IN
MARGIN = 0.50 * IN
PAGE_COUNT = 104
DRAWING_COUNT = 100
SCALES: list[float] = []


class _ExtentPath:
    def __init__(self) -> None:
        self.pts: list[tuple[float, float]] = []

    def moveTo(self, x: float, y: float) -> None:
        self.pts.append((x, y))

    def lineTo(self, x: float, y: float) -> None:
        self.pts.append((x, y))

    def close(self) -> None:
        return None


class _DrawExtent:
    """Records drawing geometry, including capsule rotate/translate, in page space."""

    def __init__(self) -> None:
        self._ctm = [1.0, 0.0, 0.0, 1.0, 0.0, 0.0]
        self._stack: list[list[float]] = []
        self.minx = 0.0
        self.miny = 0.0
        self.maxx = 0.0
        self.maxy = 0.0
        self.empty = True

    def saveState(self) -> None:
        self._stack.append(self._ctm[:])

    def restoreState(self) -> None:
        self._ctm = self._stack.pop()

    def translate(self, x: float, y: float) -> None:
        a, b, c, d, e, f = self._ctm
        self._ctm = [a, b, c, d, a * x + c * y + e, b * x + d * y + f]

    def rotate(self, deg: float) -> None:
        r = radians(deg)
        ca, sa = cos(r), sin(r)
        a, b, c, d, e, f = self._ctm
        self._ctm = [a * ca + c * sa, b * ca + d * sa, c * ca - a * sa, d * ca - b * sa, e, f]

    def scale(self, sx: float, sy: float) -> None:
        a, b, c, d, e, f = self._ctm
        self._ctm = [a * sx, b * sx, c * sy, d * sy, e, f]

    def _map(self, x: float, y: float) -> tuple[float, float]:
        a, b, c, d, e, f = self._ctm
        return a * x + c * y + e, b * x + d * y + f

    def _add(self, x: float, y: float) -> None:
        if self.empty:
            self.minx = self.maxx = x
            self.miny = self.maxy = y
            self.empty = False
            return
        self.minx = min(self.minx, x)
        self.miny = min(self.miny, y)
        self.maxx = max(self.maxx, x)
        self.maxy = max(self.maxy, y)

    def _corners(self, x0: float, y0: float, x1: float, y1: float) -> None:
        for x, y in ((x0, y0), (x0, y1), (x1, y0), (x1, y1)):
            self._add(*self._map(x, y))

    def circle(self, x: float, y: float, r: float, stroke: int = 1, fill: int = 0) -> None:
        self._corners(x - r, y - r, x + r, y + r)

    def ellipse(self, x1: float, y1: float, x2: float, y2: float, stroke: int = 1, fill: int = 0) -> None:
        self._corners(x1, y1, x2, y2)

    def roundRect(self, x: float, y: float, w: float, h: float, r: float, stroke: int = 1, fill: int = 0) -> None:
        self._corners(x, y, x + w, y + h)

    def arc(self, x1: float, y1: float, x2: float, y2: float, start: float, extent: float) -> None:
        self._corners(x1, y1, x2, y2)

    def beginPath(self) -> _ExtentPath:
        return _ExtentPath()

    def drawPath(self, path: _ExtentPath, stroke: int = 1, fill: int = 0) -> None:
        for x, y in path.pts:
            self._add(*self._map(x, y))

    def setStrokeColorRGB(self, *_a: float) -> None:
        return None

    def setFillColorRGB(self, *_a: float) -> None:
        return None

    def setLineWidth(self, _w: float) -> None:
        return None

    def setLineCap(self, _n: int) -> None:
        return None

    def setLineJoin(self, _n: int) -> None:
        return None


def _place_drawing(c: pdfcanvas.Canvas, draw_fn, top: float, bottom: float) -> None:
    ext = _DrawExtent()
    draw_fn(ext, 0, 0)
    if ext.empty:
        raise SystemExit("drawing produced no geometry")
    pad = OUTER / 2 + 2
    minx, miny = ext.minx - pad, ext.miny - pad
    maxx, maxy = ext.maxx + pad, ext.maxy + pad
    bw, bh = maxx - minx, maxy - miny
    if bw < 1 or bh < 1:
        raise SystemExit("drawing bounds collapsed")
    left = MARGIN
    right = TRIM_W - MARGIN
    avail_w = right - left
    avail_h = top - bottom
    scale = min(avail_w / bw, avail_h / bh) * 0.96
    SCALES.append(scale)
    c.saveState()
    c.translate((left + right) / 2, (bottom + top) / 2)
    c.scale(scale, scale)
    c.translate(-(minx + maxx) / 2, -(miny + maxy) / 2)
    draw_fn(c, 0, 0)
    c.restoreState()


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
    c.drawCentredString(TRIM_W / 2, TRIM_H - 2.1 * IN, "BIG EASY")
    c.setFont("DejaVuBold", 36)
    c.drawCentredString(TRIM_W / 2, TRIM_H - 2.7 * IN, "COLORING BOOK")
    c.setFont("DejaVu", 18)
    c.drawCentredString(TRIM_W / 2, TRIM_H - 3.25 * IN, "for Toddlers")
    c.setFont("DejaVuBold", 22)
    c.drawCentredString(TRIM_W / 2, TRIM_H - 3.85 * IN, "Ages 2–5")
    c.setLineWidth(OUTER)
    c.roundRect(2.4 * IN, 4.35 * IN, 3.7 * IN, 1.35 * IN, 12, stroke=1, fill=0)
    c.setFont("DejaVuBold", 16)
    c.drawCentredString(TRIM_W / 2, 5.05 * IN, "100 SIMPLE PICTURES")
    c.setFont("DejaVu", 12)
    c.drawCentredString(TRIM_W / 2, 4.7 * IN, "Animals · Trucks · Foods · Everyday things")
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
        "ISBN 979-8-1940-3221-1",
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
    c.drawCentredString(TRIM_W / 2, 2.0 * IN, "100 pictures · animals, trucks, foods, everyday things")
    c.showPage()


def ready(c: pdfcanvas.Canvas) -> None:
    _base(c)
    c.setFont("DejaVuBold", 28)
    c.drawCentredString(TRIM_W / 2, TRIM_H / 2 + 20, "Let’s color!")
    c.setLineWidth(OUTER)
    c.circle(TRIM_W / 2, TRIM_H / 2 - 70, 40, stroke=1, fill=0)
    c.showPage()


def coloring_page(c: pdfcanvas.Canvas, label: str, draw_fn) -> None:
    _base(c)
    _place_drawing(c, draw_fn, top=TRIM_H - MARGIN, bottom=1.25 * IN)
    c.setFillColorRGB(0, 0, 0)
    c.setFont("DejaVuBold", 22)
    c.drawCentredString(TRIM_W / 2, 0.72 * IN, label)
    c.showPage()


def main() -> None:
    if len(PAGES) != DRAWING_COUNT:
        raise SystemExit(f"expected {DRAWING_COUNT} drawings, got {len(PAGES)}")
    path = OUT / "Toddler_Bold_Easy_INTERIOR.pdf"
    c = pdfcanvas.Canvas(str(path), pagesize=(TRIM_W, TRIM_H))
    c.setTitle("Big Easy Coloring Book for Toddlers Ages 2-5")
    c.setAuthor("Unloved Productions")
    title_page(c)
    belongs_copyright(c)
    how_to(c)
    ready(c)
    for i, (label, fn) in enumerate(PAGES):
        coloring_page(c, label, fn)
    c.save()
    _rewrite_embedded_fonts(path)
    (OUT / "interior_page_count.txt").write_text(f"{PAGE_COUNT}\n")
    print(f"wrote {path} ({PAGE_COUNT} pages); scale {min(SCALES):.2f}–{max(SCALES):.2f}")


if __name__ == "__main__":
    main()
