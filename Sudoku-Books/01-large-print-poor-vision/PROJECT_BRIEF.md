# Large print sudoku for seniors with poor vision

One paperback. Not part of the toddler coloring series. No series until this listing is live.

## Why this book

The search phrase `large print sudoku for seniors with poor vision` is the only seed phrase that cleared the pass rule on 2026-11-03.

Three page-one US paperbacks had a Books rank under 150,000, and only one of them had 100 or more reviews. That is ongoing sales without a review wall. The other ten phrases failed an earlier clause. The toddler coloring books sit on a review wall, which is why a third generic toddler coloring book was not built.

The defect is from a verified paperback review on [Easy Extra Large Print Sudoku for Seniors](https://www.amazon.com/dp/B0FK4HJBD6), 1.0 stars, titled "Semitransparent pages", reviewed in the United States on January 20, 2026:

> You can see through the pages, if you go to do a sudoku, you see all the print from the page behind it!

The 2-star filter on that same page returned 0 matching reviews. A 3-star review on the critical filter complained that the book was marketed only to seniors. That review is not 1 or 2 stars and is not the defect this book answers.

## What this book does about that

Each puzzle is a right-hand page. The back of that sheet is blank. The next grid is the following sheet, not the back of the one being solved. Solutions start only after puzzle 40, one full-size grid per page. Cream paper is the thicker KDP black-ink stock. The blank back is the fix. Cream paper is not claimed to make ink invisible.

40 puzzles, not 150. A 150-puzzle book that prints a grid on both sides is the book the review describes.

## Files

- Interior: `production/output/Large_Print_Sudoku_Poor_Vision_INTERIOR.pdf`
- Cover: `production/output/Large_Print_Sudoku_Poor_Vision_COVER.pdf`
- Locks: `PRODUCTION_LOCKS.md`
- Upload fields: `KDP_LISTING.md`

Regenerate with:

```bash
python3 production/generate_interior.py
python3 production/generate_cover.py
```

The puzzle seed is 20261103. The interior script checks unique solutions, blank versos, page count, trim, and embedded fonts before it exits.
