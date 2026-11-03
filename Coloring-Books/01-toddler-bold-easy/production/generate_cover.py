#!/usr/bin/env python3
"""Book 1 cover: BIG EASY COLORING BOOK (animals / trucks / foods / everyday things).

Shared wrap-cover engine: ../../_shared/cover_lib.py (spec: PRODUCTION_LOCKS.md).
This file holds only this book's colors, artwork and cover copy.
"""

from __future__ import annotations

import sys
from pathlib import Path

from reportlab.lib.colors import Color
from reportlab.lib.units import inch as IN

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parent.parent / "_shared"))
from cover_lib import (  # noqa: E402
    BLEED,
    CREAM,
    NAVY,
    CoverSpec,
    build_cover,
    filled_circle as _filled_circle,
    filled_ellipse as _filled_ellipse,
    filled_poly as _filled_poly,
    filled_rrect as _filled_rrect,
)

YELLOW = Color(0.98, 0.82, 0.22)
CORAL = Color(0.92, 0.38, 0.28)
APPLE = Color(0.86, 0.22, 0.22)
TRUCK = Color(0.18, 0.55, 0.32)

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


def draw_title(c, cx, top) -> None:
    c.setFillColor(NAVY)
    c.setFont("DejaVuBold", 36)
    c.drawCentredString(cx, top - 1.15 * IN, "BIG EASY")
    c.setFont("DejaVuBold", 28)
    c.drawCentredString(cx, top - 1.65 * IN, "COLORING BOOK")
    c.setFont("DejaVu", 16)
    c.drawCentredString(cx, top - 2.05 * IN, "for Toddlers")


def draw_art(c, cx) -> None:
    hero_cat(c, cx, BLEED + 5.05 * IN)
    mini_truck(c, cx - 2.15 * IN, BLEED + 2.55 * IN)
    mini_apple(c, cx + 2.15 * IN, BLEED + 2.65 * IN)


SPEC = CoverSpec(
    pdf_name="Toddler_Bold_Easy_COVER.pdf",
    pdf_title="Big Easy Coloring Book for Toddlers Ages 2-5 — Cover",
    background=YELLOW,
    spine_text="BIG EASY COLORING  ·  AGES 2–5",
    draw_title=draw_title,
    draw_art=draw_art,
    tagline="Animals · Trucks · Foods · Everyday things",
    back_headline="One big picture on every page.",
    back_lines=[
        "100 original easy drawings for ages 2–5.",
        "Thick closed lines. Lots of space to color.",
        "Animals, trucks, foods, and everyday things.",
        "Made for crayons. Markers: put cardboard behind the page.",
        "Not a licensed character book. Original pictures only.",
    ],
)


def main() -> None:
    build_cover(ROOT, SPEC)


if __name__ == "__main__":
    main()
