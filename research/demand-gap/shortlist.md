# Demand gap shortlist

Fetched 2026-11-03. One phrase passed. One book was built.

## Decision

`large print sudoku for seniors with poor vision` cleared the pass rule. The book is `Sudoku-Books/01-large-print-poor-vision/`. The paperback was submitted on 2026-11-03 (KDP title RB22WEEEPAA, ISBN 9798167680128). On 2026-11-04 the bookshelf says Live, ASIN B0HQ9ZBP9J, $9.99. No second title.

The rule, fixed before scoring and not fit to a model:

- At least three page-one US paperbacks have a Books Best Sellers Rank on the product page better than 150,000. That line is ongoing sales. A rank near or past a million is a dead shelf.
- Page one is not a review wall. A wall is three or more of those books with 100 or more reviews.
- A fetched 1-star or 2-star review names a defect this repo can fix. A star histogram is not that. Seller copy is not that.
- The book is not a trademark, a cure claim, or a low-content log.

Demand and review-moat stay separate. An empty shelf does not pass for being empty.

## What passed which clause

`large print sudoku for seniors with poor vision` is the only phrase with three product-page ranks under 150,000, and it does not have a three-book review wall.

The named defect is a verified paperback review on [Easy Extra Large Print Sudoku for Seniors](https://www.amazon.com/dp/B0FK4HJBD6), read while signed in on 2026-11-03. 1.0 stars, title "Semitransparent pages", reviewed in the United States on January 20, 2026:

> You can see through the pages, if you go to do a sudoku, you see all the print from the page behind it!

The 2-star filter on that review page returned 0 matching customer reviews. A 3-star review in the critical set said the book should not be marketed only to seniors. That is not a 1-star or 2-star review, and it is not the defect the book fixes.

The interior puts one puzzle on the odd page and leaves the verso blank. Solutions start after the puzzle block. Title contains the exact phrase. List price is the 60% royalty floor, $9.99. Low-content stays off.

| Books BSR | Reviews on the search page | Price on the product page | Product |
|---|---|---|---|
| 100,870 | 2 | $11.99 | [Extra Large Print Easy Sudoku for seniors & low vision](https://www.amazon.com/dp/B0HFS4T5QN) |
| 76,608 | 39 | $10.99 | [Easy Extra Large Print Sudoku for Seniors](https://www.amazon.com/dp/B0FK4HJBD6) |
| 9,812 | 475 | $9.00 first displayed price | [Brain Games - Large Print Sudoku Puzzles (Arrow)](https://www.amazon.com/dp/1639380752) |

The other ten phrases fail at least one earlier clause.

Review walls, counted on the Amazon Books search page. Best Sellers Rank was not opened for these, because the wall already kills them. This is not a claim that those shelves are dead.

- `toddler coloring book` is the control. [This paperback](https://www.amazon.com/dp/B0DCZN17W9) is rank 832 in Books with 696 reviews. The same search page also shows books with 201 and 151 reviews. High demand, well served.
- `large print word search for seniors`: five page-one books at 100 reviews or more, including 535, 579, and 636.
- `dementia activities book for seniors`: five page-one books at 100 reviews or more.
- `left handed handwriting practice for kids`: three page-one books, at 227, 136, and 125 reviews.
- `number tracing book for ages 3-5`: five page-one books at 100 reviews or more.
- `cursive handwriting workbook 3rd grade`: 725, 156, and 217 reviews.
- `scissor skills workbook for preschoolers`: 486, 136, and 697 reviews.
- `anxiety workbook for teens`: 141, 695, and 792 reviews.

Dead shelves, from product pages that were opened:

- `easy mazes for seniors large print`: best opened rank is 435,121. The others opened are 934,769, 945,912, 1,107,860, and 1,309,189. None are under 150,000.
- `one day at a time sobriety journal`: opened ranks are 1,092,010 and 1,321,519.

## Data check

`listings.csv` is the 19 product pages that were opened. Every `source_url` is one of those pages. No Best Sellers Rank is stored as zero. Blank `review_count` means the search page did not show a count for that ASIN.

The data-quality validator from `senior-data-engineer` was run on that CSV against `listings.schema.json`. It exited 0. It records failures only, and it recorded none. Source URLs are unique. Completeness is 97.08 because some review counts are blank, which the schema allows. The report's accuracy figure is a pattern-detection score inside that script, not a check on these ranks.

## Live check, 2026-11-04

The KDP bookshelf shows the paperback Live. Nothing on the listing was edited. No proof was ordered. No Kindle was created. No ads were turned on.

The US Books search `large print sudoku for seniors with poor vision` was read twice the same morning, once through Jina and once in the signed-in browser. Both put ASIN B0HQ9ZBP9J first under Results (`sr=1-1`), paperback, $9.99, dated Nov 3, 2026. That card did not show a review count.

The product page `https://www.amazon.com/dp/B0HQ9ZBP9J` shows paperback $9.99, ISBN-13 979-8167680128, 124 pages, and the line "There are 0 customer reviews." The product-details list has no Best Sellers Rank, and the page HTML does not contain one. That rank is missing. It is not stored as zero, and it is not treated as a rank under 150,000 or as a rank past a million.

Price stays at the 60% floor. No second title, because no new phrase has passed the same four clauses.

## What was not fetched

- Reddit is `not_added` in `agent-reach doctor`. It was skipped. No posts were invented.
- `agent-reach web search` is Exa. `agent-reach web read` is Jina. A few search pages came back as a spinner; those were reread through Jina with cache bypass.
- Amazon review text for B0FK4HJBD6 was read in the signed-in browser on 2026-11-03. The 1-star body is quoted above. The 2-star filter returned no reviews. Other sudoku product-review pages were not opened.
- The last Exa search hit Exa's free rate limit. Nothing from that call is in the table.
- Ranks, prices, and review counts below are only the ones on the fetched pages.

Search pages used for the review counts:

- https://www.amazon.com/s?k=large+print+word+search+for+seniors&i=stripbooks
- https://www.amazon.com/s?k=large+print+sudoku+for+seniors+with+poor+vision&i=stripbooks
- https://www.amazon.com/s?k=dementia+activities+book+for+seniors&i=stripbooks
- https://www.amazon.com/s?k=easy+mazes+for+seniors+large+print&i=stripbooks
- https://www.amazon.com/s?k=left+handed+handwriting+practice+for+kids&i=stripbooks
- https://www.amazon.com/s?k=cursive+handwriting+workbook+3rd+grade&i=stripbooks
- https://www.amazon.com/s?k=scissor+skills+workbook+for+preschoolers&i=stripbooks
- https://www.amazon.com/s?k=number+tracing+book+for+ages+3-5&i=stripbooks
- https://www.amazon.com/s?k=anxiety+workbook+for+teens&i=stripbooks
- https://www.amazon.com/s?k=one+day+at+a+time+sobriety+journal&i=stripbooks
- https://www.amazon.com/s?k=toddler+coloring+book&i=stripbooks

Raw page bodies stayed in `/tmp/kdp-demand/`.
