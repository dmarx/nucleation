---
status: Read
paper: LIT-tmpxjwsp
title: Cho & Garcia-Molina — Synchronizing a database to improve freshness (SIGMOD
  2000)
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: >-
    Read in full on 2026-10-15 from the conference version as published, the 12-page
    PDF of SIGMOD 2000 pages 117–128 that ACM SIGMOD's own SIGMOD Record site serves
    for the June 2000 proceedings issue (download link on sigmodrecord.org/?p=6714,
    which resolves to sigmodrecord.org/publications/sigmodRecord/0006/pdfs/Synchronizing%20a%20Database%20to%20Improve%20Freshness.pdf;
    the page footers carry the ACM 2000 copyright line and printed page numbers
    117 to 128). The ACM Digital Library refused direct requests (403); Unpaywall,
    OpenAlex and Semantic Scholar list no open copy; the author's UCLA page (oak.cs.ucla.edu/~cho/papers/)
    did not answer from this environment (503, upstream timeout, retried eight times)
    and the old Stanford address now redirects there; a University of Washington
    course copy (courses.cs.washington.edu/courses/cse591d/00sp/cho.pdf) sits behind
    a login. Text extracted with pdftotext; the two-column layout scrambles the
    formula tables, so Table 2, Table 3 and Figure 6 were checked against page images
    rendered with pdftoppm. Read: every section, the examples, Tables 1–6, the experiments,
    the conclusion and the references. Nothing skipped. The conference paper proves
    nothing itself and defers every proof to its technical report [3]. To state
    the conditions of the two general results it asserts (uniform beats proportional
    for any distribution; the shape of the optimal allocation is the same for any
    distribution), Appendices D and E of that report were also read, from the 30-page
    Stanford technical report dated 25 October 1999, which a KTH course page hosts
    (kth.se/social/files/554f1d5bf27654514fd00393/synchronizing-a-database-to-improve-freshness.pdf).
    Statements drawn from the report are marked as such. The optimum of Example
    4 (Table 5) was recomputed by script from the fixed-order formula and the Lagrange
    condition: freshness frequencies 1.15, 1.36, 1.35, 1.14, 0.00 and age frequencies
    0.83, 0.97, 1.03, 1.07, 1.09, against the paper's 0.84 for the first, a rounding
    difference. Every quotation below from the paper was checked by script, with
    whitespace normalised, against the extracted text of the conference PDF, except
    the one footnote quoted from the technical report, which was checked against
    that report's extracted text; the quotation of A11 is CLAIM-303's.
date: '2026-10-15'
summary: >-
  For a local copy of N items, each changing as an independent Poisson process with
  a known rate and refreshed at fixed intervals under a fixed total refresh rate,
  refreshing every item equally keeps the copy fresher and younger on average than
  refreshing in proportion to change rate, under any distribution of rates (proved
  in the technical report by convexity). The freshness-optimal allocation is neither:
  it rises and then falls with change rate, and gives no refresh at all to items
  that change too fast for the budget, while the age-optimal allocation rises slowly
  with change rate. On estimates from 270 web sites, proportional, uniform and optimal
  refresh give freshness 0.12, 0.57 and 0.62. Every item matters equally, staleness
  is a time average with no access or query model, the refresh budget is fixed rather
  than priced, and refresh, change and its detection are free of any other cost.
---

# NOTE-tmp4d27w: Cho & Garcia-Molina — Synchronizing a database to improve freshness (SIGMOD 2000)

## Contribution

A formal model of keeping a polled copy of an autonomous source current. It
defines two measures of staleness, models change as a Poisson process per
item, separates the refresh problem into how often, how to share the budget
among items, in what order, and at what times, and solves the order and the
sharing questions in closed form or by Lagrange multipliers. It then checks
the Poisson model and estimates the gains on daily crawls of about 720,000
pages from 270 sites, 17 February to 24 June 1999.

## Key insight

Freshness counts whether an item is current, not how many changes it has
missed. An item that changes much faster than it can be refreshed is stale
again almost at once after each refresh, so a refresh spent on it buys
little time current. The same refresh spent on a slow item buys a long
stretch. So under a fixed budget, the marginal freshness bought by a refresh
falls with change rate past a point, and the best allocation starves the
fastest items. Proportional refresh does the opposite, spending most where
each refresh buys least.

## Assumptions

- **Change model.** Each element ei changes as a Poisson process with its
  own rate λi, independently, and the rates are known (Section 2.2). The
  experiments use estimated rates. Section 5.2's two-element illustration
  uses a non-Poisson model in which each element changes exactly once in each of its intervals, then repeats the analysis
  under Poisson.
- **Freshness.** F(ei; t) is 1 if ei equals its source at t and 0
  otherwise; the database's freshness is the mean over elements:
  "Clearly, the freshness is the fraction of the local database that is
  up-to-date." Comparisons use the time average F̄ (Definition 3).
- **Age.** A(ei; t) is 0 if ei is current and otherwise t minus the time
  the source element was modified, read in Figure 2 as growing linearly from
  the first unseen change; the database's age is the mean, again averaged
  over time.
- **Budget.** N elements are refreshed per interval I, so the mean refresh
  frequency (1/N)Σfi equals f = 1/I. The budget is fixed. It is not
  traded against any cost, and a refresh costs the same whatever the item.
- **Timing.** "In this paper, we assume that we synchronize the database
  uniformly over time." No windows (the night-only option of Example 3 is
  set aside).
- **Equal importance.** "In our current framework, we assumed that for
  users the freshness or age of every element is equally important." There
  is no model of queries or of which items are read.
- **Allocation analysis** assumes fixed-order refresh, each element at its
  own fixed interval Ii = 1/fi, because fixed order is best in Section 4.
- **Section 5.1's figures** assume change rates drawn from a gamma
  distribution with mean λ and δ² = variance/mean²; the paper says the
  conclusion holds for any distribution and defers the proof.

## Key results

Notation: r = λ/f, the ratio of change rate to refresh rate.

- **Expected freshness and age between refreshes.** With a refresh at 0 and
  at I, E[F(ei; t)] = e^(−λt) and E[A(ei; t)] = t(1 − (1 − e^(−λt))/(λt))
  for t in (0, I).
- **Order policies, equal change rates (Table 2, Figure 6).** Time-averaged
  freshness is (1 − e^(−r))/r for fixed order, (1/r)(1 − ((1 − e^(−r))/r)²)
  for random order, and 1/(1 + r) for purely random refresh (each refresh
  picks an element at random). Ages are I(1/2 − 1/r + (1 − e^(−r))/r²),
  I(1/3 + (1/2 − 1/r)² − ((1 − e^(−r))/r²)²) and I(r/(1 + r)). Refreshing as
  often as items change (r = 1) gives fixed-order freshness
  (e − 1)/e ≈ 0.63; freshness 0.8 needs r below 0.46, about twice as many
  refreshes as changes. Fixed order is best on both measures; at r = 1 its
  freshness is about 30% above purely random and its age a quarter of
  random order's. "In general, as the variability in the time between
  visits increases, the policy gets less effective."
- **Uniform beats proportional (Section 5.1, Figure 7, Table 3).** Under the
  gamma model, "Surprisingly, we can clearly see that the ratios are below 1
  for any r and δ values: The uniform policy is always better than the
  proportional policy!" The gap widens as rates spread (as δ grows,
  F̄p/F̄u → 0 and Āu/Āp → 0). Proportional freshness is (1 − e^(−r))/r,
  the same as if all items changed at the mean rate. In the technical report
  (Appendix D, Theorems 3 and 4) the general claim is F̄u ≥ F̄p and
  Āu ≤ Āp for any distribution of rates, proved from the convexity of
  F̄(λ, f) in λ and the concavity of Ā(λ, f) in λ at fixed f, by Jensen's
  inequality; equality holds when all rates are equal.
- **Two elements (Section 5.2, Table 4, Figure 9).** With λ1 = 9 and
  λ2 = 1 per day: at one refresh per day the best is to refresh only the
  slow element; "when it is not possible to keep up with everything, it is
  better to focus on what we can track." At ten per day the optimum
  (f1 = 7, f2 = 3 in Table 4; x ≈ 0.3 in Figure 9(c)) lies between uniform
  and proportional, and uniform still beats proportional.
- **The optimal allocation (Problem 1, Section 5.3).** Maximize
  (1/N)ΣF̄(λi, fi) subject to (1/N)Σfi = f and fi ≥ 0, solved by Lagrange
  multipliers. In the report (Appendix E) the condition is
  ∂F̄(λi, fi)/∂fi = µ for every refreshed element, with fi = 0 where no
  nonnegative solution exists; for fixed order the derivative is
  (1 − e^(−λ/f))/λ − e^(−λ/f)/f. Its limit as f → 0 is 1/λ, so (the
  record's derivation from that formula, confirmed numerically) an element
  is left unrefreshed exactly when its rate is at least 1/µ. Report
  Theorem 5: the solution curve for any µ is the µ = 1 curve scaled by
  1/µ, which is the basis of the paper's claim that the shape is the same
  for every database.
- **Example 4 (Table 5, Figure 10).** Five elements with rates 1 to 5 per
  day and five refreshes per day. Freshness-optimal frequencies are 1.15,
  1.36, 1.35, 1.14 and 0.00: the fastest element is never refreshed, and
  the optimal frequency falls once λ passes about 2.5. "To improve
  freshness, we should penalize the elements that change too often."
  Age-optimal frequencies rise with rate, 0.84, 0.97, 1.03, 1.07, 1.09, and
  "the optimal solution is rather close to the uniform policy than to the
  proportional policy." (Recomputed for this reading: mean freshness
  0.374 at the optimum, 0.365 uniform, 0.317 proportional, so the optimum's
  gain over uniform here is small.)
- **The web data (Section 6).** Intervals between changes for pages that
  change about every 10 days fit an exponential distribution (Figure 11).
  About 23% of pages changed more than once a day (Figure 12). Assuming 100
  million pages refreshed once a month in total, with change rates from
  Figure 12 and a yearly rate for pages not seen to change, Table 6 gives
  freshness 0.12, 0.57 and 0.62 and age 400, 5.6 and 4.3 days for
  proportional, uniform and optimal refresh: "the freshness increases from
  0.12 to 0.62 (500% increase!), if we use the optimal policy instead of the
  proportional policy", and "the age decreases by 23% from the uniform
  policy to the optimal policy."
- **Limits the paper states.** Daily crawling: "Since we crawled pages on a
  daily basis, we could not obtain detailed change histories for the pages
  that change very often", and pages that rarely change were not seen to
  change in four months; regularly updated pages may not be Poisson; the
  270 sites were chosen for popularity. Table 6 is "a crude
  approximation". Unequal importance is left open, with a preliminary
  finding that an item twice as important should be refreshed more often,
  "but not necessarily twice as often".

## Bearing on the record

**On [QUESTION-114](../questions.d/QUESTION-114.md): this prices staleness, but as the objective under a
fixed refresh budget, not as a cost against savings. It is the staleness
term the question lacks, not the joint model.**

- It is the first work the record has read that measures staleness rather
  than forbidding it. Karlin et al. ([THEORY-348](../theory.d/THEORY-348.md)) keep a copy exactly current
  or drop it; Gupta ([LIT-1091](../literature.d/LIT-1091.md)) and Gupta and Mumick ([LIT-1092](../literature.d/LIT-1092.md)) refresh every
  view in a batch; Bruno and Chaudhuri ([THEORY-332](../theory.d/THEORY-332.md)) have no staleness. Here a
  copy is allowed to be stale, and how stale is a number: the expected
  fraction of items out of date, or their mean time out of date, as a
  function of change rate and refresh rate. That function is what a joint
  model would need for its upkeep-and-staleness term.
- **What it does not price.** There is no query or read model. Freshness is
  averaged over time and items, not over reads, and every item counts the
  same. So the loss from a stale read is not in it: only if reads arrive at
  random times, uniformly over items, is time-averaged freshness the share
  of reads that find current data (the record's reading, not the paper's).
  There is no build cost, no saving per query, and no option of fetching on
  demand instead of keeping a copy. The budget is fixed, so the paper never
  weighs refresh cost against staleness; the Lagrange multiplier µ is the
  marginal freshness of one more unit of refresh rate, which is a shadow
  price, but the paper does not use it as one.
- **What it adds to the question's answers.** The value of keeping an item
  current is not proportional to how fast it changes. Under the freshness
  measure, an item that changes faster than the budget can follow is
  better left stale than chased. That narrows the staleness
  bullet of [QUESTION-114](../questions.d/QUESTION-114.md): upkeep that rises with drift is not always worth paying, and a
  binary current-or-not measure says to abandon the fastest-drifting items.
  Under the age measure the conclusion flips direction (refresh faster
  items more, but far less than proportionally), so which items to keep
  current depends on how staleness is scored. For a LEGO bin, a refresh is
  re-sorting; new bricks arriving fast into a bin argue, under freshness,
  for leaving that bin unsorted and sorting the slow ones.

**On [CLAIM-303](../claims.d/CLAIM-303.md): it gives a model of the "checking it is still current"
term, and the model's units do not match the claim's.**

- [CLAIM-303](../claims.d/CLAIM-303.md) charges upkeep u per use. Here refresh is charged per unit
  time, independent of use, and its value depends on the item's rate of
  change, not on how often it is read. A filed argument whose premises
  change at rate λ and are re-checked at fixed intervals 1/f is current a
  fraction (1 − e^(−λ/f))·f/λ of the time. That is a usable form for the
  verification term, if re-checking is periodic and premises change at
  random.
- [CLAIM-303](../claims.d/CLAIM-303.md)'s added term, that "the cost of incorrectly reusing an obsolete
  argument may exceed the cost of recomputing it", is a cost per stale use.
  Neither freshness nor age is that. Age comes closer, since it grows with
  time out of date, but it is still not weighted by use or by the harm of
  the error. So the paper does not price A11's term; it prices exposure to
  it.
- The freshness result bears on the claim's break-even in one direction:
  for an argument whose grounds change faster than the record can re-check,
  the optimal re-check rate is zero under freshness, so the filed copy is
  stale nearly always and every use must either reconstruct or risk a stale
  reuse. In [CLAIM-303](../claims.d/CLAIM-303.md)'s terms, c_a then includes reconstruction and the
  break-even condition c_r > c_a + u fails. The paper says nothing of filing
  decisions, so this is the record's application.

**On [CLAIM-308](../claims.d/CLAIM-308.md).** [CLAIM-308](../claims.d/CLAIM-308.md) states plainly that it leaves staleness out. This
paper does not reach that gap in [CLAIM-308](../claims.d/CLAIM-308.md)'s own setting: it has no online
decision, no sequence of uses, no competitive ratio and no file-or-not
choice. It shows only that once staleness is scored, the value of keeping a
copy current depends on its rate of change in a non-monotone way, so a
filing rule that ignores how fast an argument's grounds drift can misjudge
its upkeep.

## Limitations

- Known, constant, independent Poisson rates. No bursts, no regular
  updates, no correlated changes, no learning of rates (deferred to [4]).
- Every element equally important; no query or access model; time-averaged
  measures only.
- Fixed refresh budget; refresh cost uniform; no cost of staleness weighed
  against cost of refresh.
- The conference paper proves nothing in itself; the general claims rest
  on the technical report, whose convexity step is asserted by a footnote
  ("We can verify that ... is convex over λi by computing" the second
  derivative) rather than shown for each policy.
- Table 6 is an extrapolation from daily crawls of popular sites, with
  assumed rates for unchanged pages, not a measurement of a deployed policy.
