"""Measure each coloring-page drawing and fit it to the page.

Geometry is scaled up while stroke widths stay at the production-lock values
(8 pt outer / 5 pt inner). Drawings read `drawings.STROKE_K`; the page code sets
it to 1/scale while a drawing is rendered, so the printed line width never changes.
"""

from __future__ import annotations

import subprocess
import tempfile
from pathlib import Path

import numpy as np
from PIL import Image
from reportlab.pdfgen import canvas as pdfcanvas

MEASURE_SIZE = 1400  # pt, square page; drawing origin at the center
MEASURE_DPI = 144    # 2 px per pt
OUTER_STROKE = 8.0


def measure(draw_fns, drawings_module):
    """Return (left, right, bottom, top) geometry bounds per drawing (stroke excluded), in drawing units."""
    drawings_module.STROKE_K = 1.0
    half = MEASURE_SIZE / 2
    with tempfile.TemporaryDirectory() as tmp:
        pdf = Path(tmp) / "measure.pdf"
        c = pdfcanvas.Canvas(str(pdf), pagesize=(MEASURE_SIZE, MEASURE_SIZE))
        for fn in draw_fns:
            c.saveState()
            c.translate(half, half)
            fn(c, 0, 0)
            c.restoreState()
            c.showPage()
        c.save()
        subprocess.run(
            ["pdftoppm", "-r", str(MEASURE_DPI), "-gray", str(pdf), str(Path(tmp) / "m")],
            check=True,
        )
        px_per_pt = MEASURE_DPI / 72
        boxes = []
        for img_path in sorted(Path(tmp).glob("m-*.pgm")):
            a = np.array(Image.open(img_path))
            ys, xs = np.where(a < 200)
            if len(xs) == 0:
                raise SystemExit(f"{img_path.name}: empty drawing")
            l = xs.min() / px_per_pt - half
            r = (xs.max() + 1) / px_per_pt - half
            t = half - ys.min() / px_per_pt
            b = half - (ys.max() + 1) / px_per_pt
            pad = OUTER_STROKE / 2
            boxes.append((l + pad, r - pad, b + pad, t - pad))
    if len(boxes) != len(draw_fns):
        raise SystemExit(f"measured {len(boxes)} pages for {len(draw_fns)} drawings")
    return boxes


def fit(box, max_w, max_h, s_max=3.0):
    """Scale and geometry center so the stroked drawing fits inside max_w x max_h."""
    l, r, b, t = box
    gw, gh = max(r - l, 1.0), max(t - b, 1.0)
    s = min((max_w - OUTER_STROKE) / gw, (max_h - OUTER_STROKE) / gh, s_max)
    return s, ((l + r) / 2, (b + t) / 2)
