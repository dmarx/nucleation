---
status: Skimmed
paper: LIT-tmp1hbb9
title: 'Theory of Value: An Axiomatic Analysis of Economic Equilibrium'
version: 1
history:
- version: 1
  date: '2026-10-23'
  note: >-
    Read in part, from the Cowles Foundation's scanned PDF of the fourth
    printing (126 pp., no text layer). Read in full: §4.6 "Continuity
    assumption on preferences" (pp. 55–59), including the proof of
    theorem (1); chapter 4 notes 1–3 (pp. 72–73); and the bibliography
    entries for Debreu and Eilenberg (pp. 103–104). These pages were OCRed
    with tesseract, and quotations were checked by script against the OCR.
    Pages 56, 72 and 73 were checked by eye against the page images, since
    OCR misreads some words ("fexicographic" for "lexicographic") and
    drops subscripts. Symbols are transcribed from the images, with the
    consumer subscript i sometimes dropped. The rest of the book was not
    read, hence Skimmed: this is a section-level reading of a monograph.
date: '2026-10-23'
summary: >-
  Read for §4.6 only. Not every complete preorder has a utility function:
  the lexicographic ordering of R² has none. Under a continuity
  assumption (closed upper and lower contour sets), a complete preorder on
  a connected subset of Rˡ, and more generally on a connected separable
  space, has a continuous utility function, and conversely. Debreu
  credits the separable form to Eilenberg (1941), and his own 1954 paper
  for dropping connectedness on second-countable spaces. Utility is
  defined only up to increasing transformation.
---
<!-- inactive-ok-file: LIT-tmpin6y6 — Unavailable, unread; the 1954 paper §4.6 restates -->
<!-- inactive-ok-file: CLAIM-tmp85p0g CLAIM-tmp83ge2 CLAIM-tmpz8lli THEORY-090 THEORY-101 — Proposed; the claims and accounts this reading bears on, cited as open -->

# NOTE-tmpsug0b: Theory of Value: An Axiomatic Analysis of Economic Equilibrium

## Contribution

For this record, one section of the founding text of axiomatic general
equilibrium. §4.6 gives Debreu's statement and proof of the existence of
a continuous utility function for continuous preferences, and its notes
give the counterexample and the history.

## Key insight

Representability is not automatic. It needs a topological condition on
the preferences (continuity) and a countability condition on the space
(a countable dense subset). The lexicographic order shows what goes
wrong without them. The reals cannot hold uncountably many disjoint
intervals (pp. 72–73).

## Assumptions

- Preferences are a complete preorder ("completely preordered by ≾").
- (a): for every x′ the sets {x | x ≾ x′} and {x | x ≿ x′} are closed.
- The consumption set is connected, and either a subset of Rˡ or, in
  the note's generalisation, a separable topological space.

## Key results

- Theorem (1), p. 56: "Let Xᵢ be a connected subset of Rˡ, completely
  preordered by ≾. Under assumption (a) there is on Xᵢ a continuous
  utility function."
- Its converse, p. 56: "If there is a continuous utility function on Xᵢ,
  preferences satisfy assumption (a)".
- The generalisation, p. 73: the proof used Rˡ "only to obtain a
  countable dense subset", so the theorem holds on "a connected,
  separable topological space". This is "essentially a result of S.
  Eilenberg [1]" (American Journal of Mathematics 63:39–45, 1941). The
  1954 paper removes connectedness for second-countable spaces.
- The counterexample, pp. 72–73: the lexicographic ordering of R²,
  (a, b) ≺ (a′, b′) if (1) a < a′, or (2) a = a′ and b < b′. A representation
  f would give each a a non-degenerate interval Iₐ, pairwise disjoint,
  so "a one-to-one correspondence a ↔ Iₐ is established between the set
  of real numbers (which is uncountable) and a set of pairwise disjoint,
  non-degenerate, real intervals (which is countable), a contradiction."
- Ordinality, p. 56: "Given a preference preordering, a corresponding
  utility function is thus arbitrary to a large extent."

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | A continuous complete preorder on a connected subset of Rˡ has a continuous utility function | strong | proof, pp. 56–59 |
| C2 | The same holds on any connected separable space | strong | the proof uses only a countable dense subset, p. 73 |
| C3 | The lexicographic order on R² has no real-valued representation | strong | proof, pp. 72–73 |
| C4 | A utility function is fixed only up to increasing transformation | strong | immediate, p. 56 |

## Concepts

- **complete preorder** — a complete, transitive relation ≾ on the
  consumption set.
- **utility function** — "an increasing function from Xᵢ preordered by ≾
  to R" (p. 56).
- **continuity assumption (a)** — closed upper and lower contour sets.
- **lexicographic ordering** — order by the first coordinate, and by the
  second only on ties.

## Connections

Restates Debreu 1954 ([LIT-tmpin6y6](../literature.d/LIT-tmpin6y6.md)) and Eilenberg 1941 (not in
the record), and names Wold as an earlier rigorous special case. Note 2
points to Herstein and Milnor for weaker continuity assumptions. The
record's [LIT-067](../literature.d/LIT-067.md) is Debreu's 1952 equilibrium theorem.

## Bearing on the record

The record's proposal reads Veit's "common currency" ([THEORY-101](../theory.d/THEORY-101.md)) and
ALARM's override ([THEORY-090](../theory.d/THEORY-090.md)) as continuous and lexicographic dominant
orderings ([CLAIM-tmp83ge2](../claims.d/CLAIM-tmp83ge2.md)). It rests the difference on [CLAIM-tmp85p0g](../claims.d/CLAIM-tmp85p0g.md):
an ordering is a currency where it has a numerical representation, and
the lexicographic order has none. §4.6 bears on this as follows.

- **[CLAIM-tmp85p0g](../claims.d/CLAIM-tmp85p0g.md)'s mathematics is right.** Its part 3 states the
  theorem for "a connected, separable topological space whose upper and
  lower contour sets are closed". That is exactly the form on p. 73. Its
  part 2 is Debreu's lexicographic argument, moved from R² to [0, 1]². Its
  part 4, that successive currencies need not share exchange rates,
  follows Debreu's remark that a utility function is "arbitrary to a
  large extent". The claim's stated defeater, "a misstatement of Debreu's
  theorem's hypotheses", does not fire.
- **The attribution should change.** Debreu credits the
  connected-separable form to Eilenberg 1941, and keeps the 1954 paper
  for the second-countable form without connectedness. The claim should
  cite "Eilenberg (1941); Debreu (1954)". Or, if it means the 1954
  theorem, it should state that form: a continuous complete preorder on
  a second-countable space has a continuous representation. Both forms
  cover the option spaces the claim has in mind.
- **Continuity is sufficient, not necessary, for a currency.** Debreu's
  theorem gives a continuous representation for continuous orderings,
  and the converse ties continuity to *continuous* representation. It
  does not say a discontinuous ordering has no representation. Only some
  discontinuous orderings, the lexicographic one among them, have none.
  This matters for [CLAIM-tmp83ge2](../claims.d/CLAIM-tmp83ge2.md)'s test. For ALARM, that claim predicts
  "a step at a threshold beyond which no resource buys the cost". For
  Veit it predicts a continuous indifference curve. A step shows the
  ordering is discontinuous. It does not show it is lexicographic in
  Debreu's sense, or that it lacks a currency. Three cases need telling
  apart.
  - **A two-class override.** Every option over the threshold ranks below
    every option under it, and the options are otherwise traded off. The
    first key then takes two values. Such an ordering has a
    representation: add a large constant penalty above the threshold to
    a trade-off function. It is a currency, a discontinuous one, and it
    is what "no resource buys the cost" describes.
  - **A cost-only override.** Above the threshold, options are ranked
    only by cost and the resource is ignored. This is also representable.
  - **The non-representable case.** The cost dominates *at every level
    across a continuum*, and the resource breaks ties only between equal
    costs. This is Debreu's R² example, and only this has no currency.

  So the test as worded separates continuous from discontinuous
  dominance, not currency from no currency. [CLAIM-tmp85p0g](../claims.d/CLAIM-tmp85p0g.md)'s phrase "a
  lexicographic override lies in the gap" is true only of the third
  case. ALARM's "100% weight", as [CLAIM-tmp83ge2](../claims.d/CLAIM-tmp83ge2.md) operationalises it, is
  the first case and has a currency. Either the two claims should say
  "discontinuous" where they say "lexicographic", or [CLAIM-tmp83ge2](../claims.d/CLAIM-tmp83ge2.md) needs
  a further mark: whether the cost overrides the resource at every cost
  level above the threshold, not only across the threshold.
- **Completeness is presupposed.** Debreu's theorem starts from a
  complete preorder. The proposal's ambivalence, "no ordering at all"
  ([CLAIM-tmpz8lli](../claims.d/CLAIM-tmpz8lli.md), consequence 4), lies outside the theorem's domain, as
  the record already says ([THEORY-027](../theory.d/THEORY-027.md)). Debreu offers nothing on orders
  that fail completeness.

## Limitations

Only one section of the book was read. The OCR is imperfect, and quoted
text was checked against the page images on the three pages quoted most.
Elsewhere the quotations are from OCR checked by script, with symbols
transcribed by eye.

## Open questions

Whether the trade-off experiments Veit's criterion relies on can tell a
discontinuous but representable ordering from a lexicographic one, given
finite stimulus sets. On a finite set every complete preorder is
representable ([CLAIM-tmp85p0g](../claims.d/CLAIM-tmp85p0g.md), part 1), so the distinction is only
empirical in the limit.
