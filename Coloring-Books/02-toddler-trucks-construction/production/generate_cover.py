#!/usr/bin/env python3
"""Book 2 cover: BIG EASY TRUCKS COLORING BOOK (trucks / construction vehicles).

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

YELLOW = Color(0.98, 0.78, 0.18)
ORANGE = Color(0.93, 0.42, 0.12)
STEEL = Color(0.55, 0.62, 0.68)

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


def draw_title(c, cx, top) -> None:
    c.setFillColor(NAVY)
    c.setFont("DejaVuBold", 28)
    c.drawCentredString(cx, top - 1.15 * IN, "BIG EASY TRUCKS")
    c.setFont("DejaVuBold", 26)
    c.drawCentredString(cx, top - 1.62 * IN, "COLORING BOOK")
    c.setFont("DejaVu", 16)
    c.drawCentredString(cx, top - 2.02 * IN, "for Toddlers")


def draw_art(c, cx) -> None:
    hero_dump(c, cx, BLEED + 5.05 * IN)
    mini_digger(c, cx - 2.15 * IN, BLEED + 2.55 * IN)
    mini_cone(c, cx + 2.2 * IN, BLEED + 2.55 * IN)


SPEC = CoverSpec(
    pdf_name="Toddler_Trucks_COVER.pdf",
    pdf_title="Big Easy Trucks Coloring Book for Toddlers Ages 2-5 — Cover",
    background=YELLOW,
    spine_text="BIG EASY TRUCKS  ·  AGES 2–5",
    draw_title=draw_title,
    draw_art=draw_art,
    tagline="Dump trucks · Diggers · Cars · Work machines",
    back_headline="One big truck on every page.",
    back_lines=[
        "100 original easy vehicles for ages 2–5.",
        "Dump trucks, diggers, cars, and work machines.",
        "Thick closed lines. Lots of space to color.",
        "Made for crayons. Markers: put cardboard behind the page.",
        "Not a licensed brand book. Original pictures only.",
    ],
)


def main() -> None:
    build_cover(ROOT, SPEC)


if __name__ == "__main__":
    main()
