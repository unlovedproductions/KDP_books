# Demand gap shortlist

Fetched 2026-11-03. One phrase passed and one book was built. A second phrase passed on 2026-11-05. No book was built from it.

## Decision

`large print sudoku for seniors with poor vision` cleared the pass rule. The book is `Sudoku-Books/01-large-print-poor-vision/`. The paperback was submitted on 2026-11-03 (KDP title RB22WEEEPAA, ISBN 9798167680128). On 2026-11-04 the bookshelf says Live, ASIN B0HQ9ZBP9J, $9.99. The live listing stays as it is. The 2026-11-05 search below found one more phrase that passes the same rule. No interior, cover, or KDP draft was made for it.

The rule, fixed before scoring and not fit to a model:

- At least three page-one US paperbacks have a Books Best Sellers Rank on the product page better than 150,000. That line is ongoing sales. A rank near or past a million is a dead shelf.
- Page one is not a review wall. A wall is three or more of those books with 100 or more reviews.
- A fetched 1-star or 2-star review names a defect this repo can fix. A star histogram is not that. Seller copy is not that.
- The book is not a trademark, a cure claim, or a low-content log.

Demand and review-moat stay separate. An empty shelf does not pass for being empty.

## What passed which clause

`large print sudoku for seniors with poor vision` was the phrase that cleared the rule on 2026-11-03. It has three product-page ranks under 150,000, and it does not have a three-book review wall. A second phrase cleared the same rule on 2026-11-05. That result is in the section below.

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

`listings.csv` holds the product pages that showed a real Books rank. The first 19 rows are the 2026-11-03 pages. The 2026-11-05 rows are appended after them. Every `source_url` is one of those pages, and each URL appears once. Two maze paperbacks already had a row from 2026-11-03, so today's pages for those same URLs were not appended again. No Best Sellers Rank is stored as zero. Blank `review_count` means the search page did not show a count for that ASIN.

The data-quality validator from `senior-data-engineer` was run on that CSV against `listings.schema.json` on 2026-11-05. It exited 0. It records failures only, and it recorded none. 79 rows, 0 duplicate URLs. Completeness is 95.5 because 32 review counts are blank, which the schema allows. The report's accuracy figure is a pattern-detection score inside that script, not a check on these ranks. It also labels `fetched_date` as a phone pattern. That label is a script quirk.

## Live check, 2026-11-04

The KDP bookshelf shows the paperback Live. Nothing on the listing was edited. No proof was ordered. No Kindle was created. No ads were turned on.

The US Books search `large print sudoku for seniors with poor vision` was read twice the same morning, once through Jina and once in the signed-in browser. Both put ASIN B0HQ9ZBP9J first under Results (`sr=1-1`), paperback, $9.99, dated Nov 3, 2026. That card did not show a review count.

The product page `https://www.amazon.com/dp/B0HQ9ZBP9J` shows paperback $9.99, ISBN-13 979-8167680128, 124 pages, and the line "There are 0 customer reviews." The product-details list has no Best Sellers Rank, and the page HTML does not contain one. That rank is missing. It is not stored as zero, and it is not treated as a rank under 150,000 or as a rank past a million.

Price stays at the 60% floor. The live listing was not edited. The search recorded below found one new phrase that passes the same four clauses. No book was built from it.

## Easier phrases, 2026-11-05

Same four clauses. US Books searches, `i=stripbooks`, read through Jina with cache bypass. Two searches came back as the Amazon spinner and were fetched again. A blocked page stayed a missing row. Review counts below are paperback counts on the search page. Spiral-bound books are named where they sat on the page, and they are not in the wall count.

### Passed

`large print word search one puzzle per page` clears the rank clause and the wall clause, and a fetched 1-star review names a print-size defect.

Page one has one paperback at 100 reviews or more: [Jumbo Large Print Word-Finds Word Search Puzzle Book](https://www.amazon.com/dp/1559910755), 231 reviews. That is one book, so the page is not a review wall.

Five page-one paperbacks have a Books rank under 150,000:

| Books BSR | Reviews on the search page | Price on the product page | Product |
|---|---|---|---|
| 371 | not shown | $15.99 | [KAPPA Super Saver LARGE PRINT Word Search Puzzle Pack](https://www.amazon.com/dp/1559930063) |
| 582 | 231 | $4.99 | [Jumbo Large Print Word-Finds Word Search Puzzle Book](https://www.amazon.com/dp/1559910755) |
| 1,820 | not shown | $6.99 | [Huge Book of Large Print Word Search: 9000 Words](https://www.amazon.com/dp/B0DJ8KQRQN) |
| 2,751 | not shown | $9.26 | [Word Search Puzzles (Big Book of Puzzles) (Brain Busters)](https://www.amazon.com/dp/1646380258) |
| 6,264 | not shown | $9.31 | [Large Print Word Search Puzzles Volume 2 (Brain Busters)](https://www.amazon.com/dp/1680528882) |

The first product page for 1559930063 returned HTTP 503. The retry showed rank 371 in Books. These five are the page-one paperbacks on this search. Several of them are large-print word-search editions from Kappa and Brain Busters. The rule scores that search page.

Jina's review URLs redirected to a sign-in page, so those bodies were not used. The 1-star and 2-star filters were then read in the signed-in browser. On [1559910755](https://www.amazon.com/product-reviews/1559910755/?ie=UTF8&filterByStar=one_star&reviewerType=all_reviews), the 1-star filter returned two verified purchases. The print defect is the review titled "NOT JUMBO!!", reviewed in the United States on September 3, 2026:

> Print much smaller than advertised.

The other 1-star review on that page is about price. The 2-star filter on that page returned 0 matching customer reviews. A 2-star review on [1956816062](https://www.amazon.com/dp/1956816062), titled "Too easy!", says the puzzles did not challenge a 90-year-old reader. That is a difficulty complaint. It is not the print defect.

The phrase is a puzzle book. It is not a trademark, a cure claim, or a low-content log. It is a candidate for a later build. This pass did not generate an interior, a cover, or a KDP draft. The live sudoku listing was not edited.

`easy dot to dot for seniors large print` also cleared the rank clause and the wall clause. Its reviews were not opened, because the word-search phrase had already passed. It is not scored as a pass.

One paperback on that search page has 100 or more reviews: [Easy to Read Dot-to-Dot Animals](https://www.amazon.com/dp/1977747000), 290 reviews, Books rank 545,740. Two spiral-bound Brain Games editions on the same page have 999 and 739 reviews. They are spiral-bound, so they are not in the wall count.

Six page-one paperbacks have a Books rank under 150,000: 34,079, 42,276, 63,118, 97,646, 107,980, and 144,265.

### Review wall

These pages already have three or more paperbacks at 100 reviews. Product pages were not opened for them.

- `large print word search for seniors with poor vision`: 521, 537, and 242 reviews.
- `giant print crossword puzzles for seniors easy`: 100, 425, 276, 410, and 329 reviews.
- `large print cryptogram puzzles for seniors`: 109, 111, and 234 reviews.
- `bold easy coloring book for seniors`: 178, 443, 133, 399, 119, and 242 reviews.
- `large print number search puzzles for seniors`: 106, 636, 537, and 231 reviews. The 636, 537, and 231 counts are on word-search titles that appeared on this number-search page. They are still page-one paperbacks on the search, so they count.

### Dead shelf

These pages are not review walls. The opened product pages do not show three Books ranks under 150,000. Pages that still had no Books rank after a retry stay missing.

- `large print kakuro puzzles for seniors`: best opened rank is 329,348. The next opened rank is 680,546. The rest are past a million. Five page-one paperbacks were opened twice and still showed no Books rank: B0HK18LDPB, B0H6V1QCVH, B0GSJ2LGJH, B0GSHWTVWD, and B0GTT325ZX.
- `large print spot the difference for seniors`: one opened rank is under 150,000, [The Ultimate Spot The Difference Book For Adults](https://www.amazon.com/dp/B0FYG14XXR) at 43,543. The next opened rank is 610,870. Two pages still showed no Books rank after a retry: 1773255061, and B0B92H9291. B0B92H9291 shows a rank in Children's Puzzle Books. That line is not a Books rank.
- `simple mazes for visually impaired adults`: one opened rank is under 150,000, [Maze Puzzles for Seniors](https://www.amazon.com/dp/B0GY81LB5W) at 144,269. The next opened ranks are 184,442 and 202,082. Three pages still showed no Books rank after a retry: B0HP8LMYBF, B0DDGYSLD5, and B0H8LV6246. [101 Large Print Easy Mazes](https://www.amazon.com/dp/B099YKJY5Z) is already in `listings.csv` from 2026-11-03 at rank 934,769. Today's product page shows rank 202,082. That URL was not added a second time. Both ranks are past 150,000.

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

The 2026-11-05 searches:

- https://www.amazon.com/s?k=large+print+word+search+for+seniors+with+poor+vision&i=stripbooks
- https://www.amazon.com/s?k=large+print+word+search+one+puzzle+per+page&i=stripbooks
- https://www.amazon.com/s?k=giant+print+crossword+puzzles+for+seniors+easy&i=stripbooks
- https://www.amazon.com/s?k=large+print+kakuro+puzzles+for+seniors&i=stripbooks
- https://www.amazon.com/s?k=large+print+cryptogram+puzzles+for+seniors&i=stripbooks
- https://www.amazon.com/s?k=easy+dot+to+dot+for+seniors+large+print&i=stripbooks
- https://www.amazon.com/s?k=large+print+spot+the+difference+for+seniors&i=stripbooks
- https://www.amazon.com/s?k=bold+easy+coloring+book+for+seniors&i=stripbooks
- https://www.amazon.com/s?k=large+print+number+search+puzzles+for+seniors&i=stripbooks
- https://www.amazon.com/s?k=simple+mazes+for+visually+impaired+adults&i=stripbooks

Review pages opened on 2026-11-05, in the signed-in browser, were the 1-star and 2-star filters for the word-search paperbacks 1956816062, B0FVLPMKJV, B0FGVCQNKN, 1559910755, B0FNMZZPZ8, B0BL2MHNFB, B09WJ1VVTZ, B0CMM3TPS8, and 1680528882. Dot-to-dot review pages were not opened. Jina's copies of the review URLs were sign-in pages, so no review text was taken from them.

Raw page bodies stayed in `/tmp/kdp-demand/`.
