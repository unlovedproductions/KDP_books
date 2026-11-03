#!/usr/bin/env python3
"""8.5x11 no-bleed interior. Cream paper is selected in KDP, not painted here.

Page map (124 pages, even):
  1 title, 2 copyright, 3 how to use, 4 blank
  5-84: puzzle on the odd page, blank verso (40 puzzles)
  85-124: one full-size solution per page

The verso of a puzzle is empty so the next grid cannot show through.
"""

from __future__ import annotations

import subprocess
from pathlib import Path
from typing import Literal, Never

from reportlab.lib.units import inch as IN
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas as pdfcanvas

from check_output import check_interior, check_puzzles
from sudoku import BOOK_SIZE, Puzzle, generate_book

ROOT = Path(__file__).resolve().parent
FONT_DIR = ROOT / "fonts"
pdfmetrics.registerFont(TTFont("DejaVu", str(FONT_DIR / "DejaVuSans.ttf")))
pdfmetrics.registerFont(TTFont("DejaVuBold", str(FONT_DIR / "DejaVuSans-Bold.ttf")))
FONT = "DejaVu"
FONT_BOLD = "DejaVuBold"

OUT = ROOT / "output"
OUT.mkdir(exist_ok=True)

TRIM_W = 8.5 * IN
TRIM_H = 11.0 * IN
PAGE_COUNT = 124
PUZZLE_COUNT = BOOK_SIZE
GUTTER = 0.625 * IN
OUTER = 0.50 * IN
TOP = 0.55 * IN
BOTTOM = 0.50 * IN

Role = Literal["title", "copyright", "howto", "blank", "puzzle", "solution"]
Slot = tuple[Role, int | None]


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


def page_plan() -> tuple[Slot, ...]:
    pages: list[Slot] = [
        ("title", None),
        ("copyright", None),
        ("howto", None),
        ("blank", None),
    ]
    for index in range(PUZZLE_COUNT):
        pages.append(("puzzle", index))
        pages.append(("blank", None))
    for index in range(PUZZLE_COUNT):
        pages.append(("solution", index))
    if len(pages) != PAGE_COUNT:
        raise RuntimeError(f"page plan is {len(pages)}, expected {PAGE_COUNT}")
    for index in range(PUZZLE_COUNT):
        puzzle_page = 5 + index * 2
        slot = pages[puzzle_page - 1]
        verso = pages[puzzle_page]
        if slot != ("puzzle", index) or verso[0] != "blank":
            raise RuntimeError("puzzle is not backed by a blank page")
        solution_page = 85 + index
        if pages[solution_page - 1] != ("solution", index):
            raise RuntimeError("solution sits on the wrong page")
    return tuple(pages)


def _content_box(page_number: int) -> tuple[float, float, float, float]:
    if page_number % 2 == 1:
        left, right = GUTTER, OUTER
    else:
        left, right = OUTER, GUTTER
    width = TRIM_W - left - right
    height = TRIM_H - TOP - BOTTOM
    return left, BOTTOM, width, height


def _draw_grid(
    c: pdfcanvas.Canvas,
    left: float,
    bottom: float,
    size: float,
    puzzle: Puzzle,
    digits: int,
    reveal: bool,
) -> None:
    cell = size / 9
    c.setStrokeColorRGB(0, 0, 0)
    c.setFillColorRGB(0, 0, 0)
    for i in range(1, 9):
        c.setLineWidth(3.25 if i % 3 == 0 else 1.15)
        c.line(left + i * cell, bottom, left + i * cell, bottom + size)
        c.line(left, bottom + i * cell, left + size, bottom + i * cell)
    c.setLineWidth(3.25)
    c.rect(left, bottom, size, size, stroke=1, fill=0)
    c.setFillColorRGB(0, 0, 0)
    for row in range(9):
        for col in range(9):
            clue = puzzle.clues[row][col]
            if clue:
                value = clue
                font = FONT_BOLD
            elif reveal:
                value = puzzle.solution[row][col]
                font = FONT
            else:
                continue
            c.setFont(font, digits)
            cx = left + col * cell + cell / 2
            cy = bottom + (8 - row) * cell + cell / 2 - digits * 0.35
            c.drawCentredString(cx, cy, str(value))


def _fit_grid(box_width: float, box_height: float, reserved_top: float) -> float:
    return min(box_width, box_height - reserved_top)


def _title(c: pdfcanvas.Canvas) -> None:
    c.setFillColorRGB(0, 0, 0)
    center = TRIM_W / 2
    c.setFont(FONT_BOLD, 26)
    c.drawCentredString(center, TRIM_H - 1.7 * IN, "LARGE PRINT")
    c.setFont(FONT_BOLD, 48)
    c.drawCentredString(center, TRIM_H - 2.55 * IN, "SUDOKU")
    c.setFont(FONT_BOLD, 28)
    c.drawCentredString(center, TRIM_H - 3.25 * IN, "FOR SENIORS")
    c.drawCentredString(center, TRIM_H - 3.8 * IN, "WITH POOR VISION")
    c.setLineWidth(2)
    c.line(1.5 * IN, TRIM_H - 4.2 * IN, TRIM_W - 1.5 * IN, TRIM_H - 4.2 * IN)
    c.setFont(FONT, 20)
    lines = [
        "40 easy puzzles",
        "One giant grid on the page",
        "The other side of that page is blank",
        "Solutions are the same size, at the back",
    ]
    y = TRIM_H - 5.0 * IN
    for line in lines:
        c.drawCentredString(center, y, line)
        y -= 0.42 * IN
    c.setFont(FONT, 16)
    c.drawCentredString(center, 1.15 * IN, "Unloved Productions")


def _copyright(c: pdfcanvas.Canvas) -> None:
    c.setFillColorRGB(0, 0, 0)
    left = GUTTER
    c.setFont(FONT_BOLD, 18)
    c.drawString(left, TRIM_H - 1.3 * IN, "Copyright")
    c.setFont(FONT, 15)
    lines = [
        "Copyright 2026 Unloved Productions.",
        "All rights reserved.",
        "",
        "This is a puzzle book. It is not medical advice,",
        "and it does not claim to improve eyesight.",
        "",
        "The grids are generated in code. They are not",
        "pictures from an image model.",
        "",
        "Print this interior in black ink on cream paper,",
        "8.5 x 11 inches, no bleed.",
    ]
    y = TRIM_H - 1.85 * IN
    for line in lines:
        c.drawString(left, y, line)
        y -= 0.38 * IN


def _howto(c: pdfcanvas.Canvas) -> None:
    c.setFillColorRGB(0, 0, 0)
    left = 0.85 * IN
    c.setFont(FONT_BOLD, 26)
    c.drawString(left, TRIM_H - 1.35 * IN, "How to use this book")
    c.setFont(FONT, 18)
    lines = [
        "Write on the page that has the grid.",
        "The other side of that sheet is blank.",
        "The next puzzle is not printed behind it.",
        "",
        "Easy means 47 to 53 numbers are already filled in.",
        "Each puzzle has one solution.",
        "",
        "Solutions start after puzzle 40.",
        "A solution is never on the back of its puzzle.",
        "Solution pages are printed on both sides.",
        "Puzzle pages are not.",
        "",
        "Pencil works better than pen.",
    ]
    y = TRIM_H - 2.05 * IN
    for line in lines:
        c.drawString(left, y, line)
        y -= 0.42 * IN


def _puzzle_page(c: pdfcanvas.Canvas, page_number: int, puzzle: Puzzle, index: int) -> None:
    left, bottom, width, height = _content_box(page_number)
    c.setFillColorRGB(0, 0, 0)
    c.setFont(FONT_BOLD, 22)
    c.drawCentredString(TRIM_W / 2, bottom + height - 0.15 * IN, f"Puzzle {index + 1} of {PUZZLE_COUNT}")
    c.setFont(FONT, 14)
    c.drawCentredString(TRIM_W / 2, bottom + height - 0.42 * IN, "Easy")
    size = _fit_grid(width, height, 0.7 * IN)
    grid_left = left + (width - size) / 2
    grid_bottom = bottom + (height - 0.7 * IN - size) / 2
    _draw_grid(c, grid_left, grid_bottom, size, puzzle, digits=40, reveal=False)
    c.setFont(FONT, 12)
    c.drawCentredString(TRIM_W / 2, 0.32 * IN, str(page_number))


def _solution_page(c: pdfcanvas.Canvas, page_number: int, puzzle: Puzzle, index: int) -> None:
    left, bottom, width, height = _content_box(page_number)
    c.setFillColorRGB(0, 0, 0)
    c.setFont(FONT_BOLD, 22)
    c.drawCentredString(TRIM_W / 2, bottom + height - 0.15 * IN, f"Solution {index + 1} of {PUZZLE_COUNT}")
    c.setFont(FONT, 14)
    c.drawCentredString(TRIM_W / 2, bottom + height - 0.42 * IN, "Clues are bold")
    size = _fit_grid(width, height, 0.7 * IN)
    grid_left = left + (width - size) / 2
    grid_bottom = bottom + (height - 0.7 * IN - size) / 2
    _draw_grid(c, grid_left, grid_bottom, size, puzzle, digits=36, reveal=True)
    c.setFont(FONT, 12)
    c.drawCentredString(TRIM_W / 2, 0.32 * IN, str(page_number))


def _draw(c: pdfcanvas.Canvas, page_number: int, role: Role, index: int | None, puzzles: tuple[Puzzle, ...]) -> None:
    if role == "title":
        _title(c)
        return
    if role == "copyright":
        _copyright(c)
        return
    if role == "howto":
        _howto(c)
        return
    if role == "blank":
        return
    if role == "puzzle":
        if index is None:
            raise RuntimeError("puzzle page is missing its index")
        _puzzle_page(c, page_number, puzzles[index], index)
        return
    if role == "solution":
        if index is None:
            raise RuntimeError("solution page is missing its index")
        _solution_page(c, page_number, puzzles[index], index)
        return
    unexpected: Never = role
    raise AssertionError(unexpected)


def build(puzzles: tuple[Puzzle, ...]) -> Path:
    if len(puzzles) != PUZZLE_COUNT:
        raise RuntimeError("puzzle count does not match the page plan")
    path = OUT / "Large_Print_Sudoku_Poor_Vision_INTERIOR.pdf"
    c = pdfcanvas.Canvas(str(path), pagesize=(TRIM_W, TRIM_H))
    c.setTitle("Large Print Sudoku for Seniors with Poor Vision")
    c.setAuthor("Unloved Productions")
    for page_number, (role, index) in enumerate(page_plan(), start=1):
        _draw(c, page_number, role, index, puzzles)
        c.showPage()
    c.save()
    rewrite_embedded_fonts(path)
    (OUT / "interior_page_count.txt").write_text(f"{PAGE_COUNT}\n")
    return path


def main() -> None:
    puzzles = generate_book()
    path = build(puzzles)
    check_puzzles(puzzles)
    check_interior(path)
    print(f"wrote {path}")


if __name__ == "__main__":
    main()
