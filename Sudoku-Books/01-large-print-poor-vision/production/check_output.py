"""Checks for the large-print sudoku interior. No network, no guessed ranks."""

from __future__ import annotations

from pathlib import Path

from pypdf import PdfReader
from pypdf.generic import IndirectObject

from sudoku import BOOK_SIZE, Puzzle, count_solutions

PAGE_COUNT = 124
TRIM = (612.0, 792.0)


def check_puzzles(puzzles: tuple[Puzzle, ...]) -> None:
    if len(puzzles) != BOOK_SIZE:
        raise SystemExit(f"expected {BOOK_SIZE} puzzles, got {len(puzzles)}")
    seen: set[tuple[tuple[int, ...], ...]] = set()
    for number, puzzle in enumerate(puzzles, start=1):
        givens = puzzle.given_count
        if not 47 <= givens <= 53:
            raise SystemExit(f"puzzle {number} has {givens} givens")
        if puzzle.clues in seen:
            raise SystemExit(f"puzzle {number} is a duplicate")
        seen.add(puzzle.clues)
        grid = [list(row) for row in puzzle.clues]
        if count_solutions(grid, 2) != 1:
            raise SystemExit(f"puzzle {number} does not have one solution")
        for row in range(9):
            for col in range(9):
                clue = puzzle.clues[row][col]
                if clue and clue != puzzle.solution[row][col]:
                    raise SystemExit(f"puzzle {number} clue does not match the solution")
                if (clue == 0) != (puzzle.clues[8 - row][8 - col] == 0):
                    raise SystemExit(f"puzzle {number} is not symmetric")


def _font_file(font_obj: object) -> object:
    if isinstance(font_obj, IndirectObject):
        font_obj = font_obj.get_object()
    descriptor = font_obj.get("/FontDescriptor")
    if descriptor is None:
        return None
    if isinstance(descriptor, IndirectObject):
        descriptor = descriptor.get_object()
    for key in ("/FontFile2", "/FontFile3", "/FontFile"):
        if descriptor.get(key) is not None:
            return descriptor.get(key)
    return None


def _page_fonts_embedded(page: object) -> None:
    resources = page.get("/Resources")
    if resources is None:
        return
    if isinstance(resources, IndirectObject):
        resources = resources.get_object()
    fonts = resources.get("/Font")
    if fonts is None:
        return
    if isinstance(fonts, IndirectObject):
        fonts = fonts.get_object()
    for name, font in fonts.items():
        if _font_file(font) is None:
            raise SystemExit(f"font {name} is not embedded")


def check_interior(path: Path) -> None:
    reader = PdfReader(str(path))
    if len(reader.pages) != PAGE_COUNT:
        raise SystemExit(f"{path.name} has {len(reader.pages)} pages, expected {PAGE_COUNT}")
    for number, page in enumerate(reader.pages, start=1):
        box = page.mediabox
        width = float(box.width)
        height = float(box.height)
        if abs(width - TRIM[0]) > 0.2 or abs(height - TRIM[1]) > 0.2:
            raise SystemExit(f"page {number} trim is {width} x {height}")
        _page_fonts_embedded(page)
        text = page.extract_text() or ""
        compact = " ".join(text.split())
        if number == 4 or (6 <= number <= 84 and number % 2 == 0):
            if compact:
                raise SystemExit(f"page {number} should be blank, found: {compact[:80]}")
            continue
        if 5 <= number <= 83 and number % 2 == 1:
            puzzle_number = (number - 5) // 2 + 1
            label = f"Puzzle {puzzle_number} of {BOOK_SIZE}"
            if label not in compact:
                raise SystemExit(f"page {number} missing {label!r}, got {compact[:80]!r}")
            if "Solution" in compact:
                raise SystemExit(f"page {number} contains a solution label")
        if 85 <= number <= 124:
            solution_number = number - 84
            label = f"Solution {solution_number} of {BOOK_SIZE}"
            if label not in compact:
                raise SystemExit(f"page {number} missing {label!r}, got {compact[:80]!r}")
    print(f"interior ok: {PAGE_COUNT} pages, blank versos, embedded fonts")
