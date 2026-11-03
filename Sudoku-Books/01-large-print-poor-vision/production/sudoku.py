"""Easy sudoku with a single solution.

Clues stay on a 180-degree symmetry. The center cell stays filled, so the
given count stays odd. Target is 47 givens: enough that the puzzle is easy,
few enough that it is still a puzzle.
"""

from __future__ import annotations

import random
from dataclasses import dataclass

TARGET_GIVENS = 47
MAX_GIVENS = 53
BOOK_SIZE = 40
SEED = 20261103

Grid = list[list[int]]


@dataclass(frozen=True)
class Puzzle:
    clues: tuple[tuple[int, ...], ...]
    solution: tuple[tuple[int, ...], ...]

    @property
    def given_count(self) -> int:
        return sum(1 for row in self.clues for value in row if value)


def _candidates(grid: Grid, row: int, col: int) -> list[int]:
    used = set(grid[row])
    used.update(grid[i][col] for i in range(9))
    box_row = (row // 3) * 3
    box_col = (col // 3) * 3
    for i in range(box_row, box_row + 3):
        used.update(grid[i][box_col : box_col + 3])
    used.discard(0)
    return [n for n in range(1, 10) if n not in used]


def _next_empty(grid: Grid) -> tuple[int, int, list[int]] | None:
    best: tuple[int, int, list[int]] | None = None
    for row in range(9):
        for col in range(9):
            if grid[row][col] != 0:
                continue
            found = _candidates(grid, row, col)
            if not found:
                return (row, col, [])
            if best is None or len(found) < len(best[2]):
                best = (row, col, found)
                if len(found) == 1:
                    return best
    return best


def _fill(rng: random.Random, grid: Grid) -> bool:
    spot = _next_empty(grid)
    if spot is None:
        return True
    row, col, found = spot
    if not found:
        return False
    order = found[:]
    rng.shuffle(order)
    for number in order:
        grid[row][col] = number
        if _fill(rng, grid):
            return True
        grid[row][col] = 0
    return False


def count_solutions(grid: Grid, limit: int = 2) -> int:
    """Count solutions up to `limit`. Restores `grid`."""
    spot = _next_empty(grid)
    if spot is None:
        return 1
    row, col, found = spot
    if not found:
        return 0
    total = 0
    for number in found:
        grid[row][col] = number
        total += count_solutions(grid, limit)
        grid[row][col] = 0
        if total >= limit:
            return total
    return total


def _valid_completed(grid: Grid) -> bool:
    digits = set(range(1, 10))
    for row in grid:
        if set(row) != digits:
            return False
    for col in range(9):
        if {grid[row][col] for row in range(9)} != digits:
            return False
    for box_row in range(0, 9, 3):
        for box_col in range(0, 9, 3):
            box = {
                grid[r][c]
                for r in range(box_row, box_row + 3)
                for c in range(box_col, box_col + 3)
            }
            if box != digits:
                return False
    return True


def _given_count(grid: Grid) -> int:
    return sum(1 for row in grid for value in row if value)


def _pairs() -> list[tuple[tuple[int, int], tuple[int, int]]]:
    pairs: list[tuple[tuple[int, int], tuple[int, int]]] = []
    for row in range(9):
        for col in range(9):
            mirror = (8 - row, 8 - col)
            if (row, col) >= mirror:
                continue
            pairs.append(((row, col), mirror))
    return pairs


def _one_puzzle(rng: random.Random) -> Puzzle:
    for _attempt in range(80):
        completed: Grid = [[0] * 9 for _ in range(9)]
        if not _fill(rng, completed):
            continue
        if not _valid_completed(completed):
            continue
        clues: Grid = [row[:] for row in completed]
        pairs = _pairs()
        rng.shuffle(pairs)
        for (row, col), (mirror_row, mirror_col) in pairs:
            saved = (clues[row][col], clues[mirror_row][mirror_col])
            clues[row][col] = 0
            clues[mirror_row][mirror_col] = 0
            if count_solutions(clues, 2) != 1:
                clues[row][col], clues[mirror_row][mirror_col] = saved
            elif _given_count(clues) <= TARGET_GIVENS:
                break
        givens = _given_count(clues)
        if not TARGET_GIVENS <= givens <= MAX_GIVENS:
            continue
        if count_solutions(clues, 2) != 1:
            continue
        puzzle = Puzzle(
            clues=tuple(tuple(row) for row in clues),
            solution=tuple(tuple(row) for row in completed),
        )
        if puzzle.clues[4][4] == 0:
            continue
        return puzzle
    raise RuntimeError("could not build an easy unique sudoku")


def generate_book(seed: int = SEED, count: int = BOOK_SIZE) -> tuple[Puzzle, ...]:
    rng = random.Random(seed)
    puzzles: list[Puzzle] = []
    seen: set[tuple[tuple[int, ...], ...]] = set()
    while len(puzzles) < count:
        puzzle = _one_puzzle(rng)
        if puzzle.clues in seen:
            continue
        for row in range(9):
            for col in range(9):
                clue = puzzle.clues[row][col]
                if clue and clue != puzzle.solution[row][col]:
                    raise RuntimeError("clue disagrees with the solution")
                mirror = puzzle.clues[8 - row][8 - col]
                if (clue == 0) != (mirror == 0):
                    raise RuntimeError("clues broke 180-degree symmetry")
        puzzles.append(puzzle)
        seen.add(puzzle.clues)
    return tuple(puzzles)
