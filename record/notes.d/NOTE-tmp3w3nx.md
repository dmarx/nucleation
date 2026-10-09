---
status: Read
paper: 'LIT-tmp56yt5'
title: 'Wang, Solloway, Shiffrin & Busemeyer, the QQ equality in 72 surveys'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Main text read in full from PubMed Central (PMC4084470): abstract,
    every section, Table 1, the captions of Figs. 1–2, acknowledgments and
    references. The figures were read from captions and prose only. The
    supporting information was not read: PMC's PDF returned a
    proof-of-work challenge page, PNAS's copy HTTP 403, and Europe PMC
    reports the article closed for supplementary files. So the proof, the
    list of the 72 studies, the χ² distribution tests, the two classical
    models built to satisfy the equality and the "angular distance"
    variant are known only from the main text's description. The per-pair
    q statistics were seen instead in the supplementary table S1 of
    LIT-264, which recomputes them from data the authors supplied.
date: '2026-10-09'
summary: >-
  Across all 66 Pew surveys of 2001–2011 that varied the order of two
  questions, chosen without regard to their outcome, question order
  changes the answers (p = 0.0004 for the order-effect χ² distribution)
  while the probability of answering the two questions alike does not
  change (p = 0.4625 for the q values), as the QQ equality predicts.
  Paired context effects across 72 studies lie along the predicted line of
  slope −1 (r = −0.82).
---

<!-- inactive-ok-file: THEORY-013 — Proposed; this reading bears on it without settling its promote_when -->
<!-- inactive-ok-file: THEORY-tmp9wyar — Proposed; this reading is its primary source -->
<!-- inactive-ok-file: LIT-316 — Deferred; the book is unread here -->

# NOTE-tmp3w3nx: Wang, Solloway, Shiffrin & Busemeyer, the QQ equality in 72 surveys

## Contribution

LIT-tmptn5dr stated the QQ equality and tested it on six data sets, four
of them picked because they showed order effects. This paper tests it on
all 66 Pew surveys of a decade that varied the order of two questions,
plus six other studies. The equality holds across the set while order
effects are present, and the paper presents the result as a regularity
in survey data in its own right, whatever model explains it.

## Key insight

Read the context-effect table, not the marginals. Order effects are
usually reported as shifts in "yes" rates. The QQ equality is a
constraint on the joint table: within each diagonal the two shifts
cancel. That constraint can be checked on data whatever model one holds,
and an unconstrained model would not produce it.

## Assumptions

- Two binary questions asked back to back to two random halves of a
  sample, with nothing inserted before or between them.
- A common initial state across the two halves; individual differences
  are allowed as a mixed state (density matrix), and the equality still
  holds on average.
- Complete two-way tables are needed. Most published order-effect
  studies report only marginals, which limits the studies available.

## Key results

- **Table 1** (three Gallup polls, Moore 2002): order effects significant
  in all three (χ²(3) = 10.14, 73.04, 67.19). q = −0.003 (χ²(1) = 0.01,
  p = 0.91) for Clinton–Gore, −0.02 (χ²(1) = 0.56, p = 0.46) for
  white–black, and 0.1514 (χ²(1) = 28.57, p < 0.001) for Rose–Jackson,
  where background information was read out before each question. The
  text gives that last value as "−0.15"; the table, and the 2013 paper,
  give +0.1514.
- **Algebraic facts about q** (from the main text; proofs in the SI): the
  main-diagonal and off-diagonal q are equal and opposite; |q| cannot
  exceed the size of the larger diagonal's order effect; the tables
  meeting the equality are a triangular plane inside the
  three-dimensional pyramid of possible context-effect tables.
- **Fig. 1, left**: for 72 studies, one diagonal cell against the other
  falls along the a priori line y = −x, r = −0.82 (−0.73 without two
  extremes). **Fig. 1, right**: for the 17 studies with an order effect
  above 0.10, q/(order effect) falls towards zero as the effect grows.
- **The unbiased test**: across the 66 Pew surveys, the χ² distribution
  test for order effects gives p = 0.0004 and the test for q gives
  p = 0.4625. Including the four selected national surveys does not
  change the conclusion (SI, not read).
- **Robustness of the model** (SI, not read): if the post-answer state
  moves only part of the angular distance towards the projection, q is no
  longer exactly zero but stays "very close to zero" in every case the
  authors tried.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | In survey question-order experiments, the probability of agreeing answers is order-invariant while order effects are present | strong for this population of surveys: 66 unselected Pew surveys, p = 0.4625 for q against p = 0.0004 for order effects | Results, Fig. 1 |
| C2 | The equality fails when information is inserted between questions | weak: one case | Table 1, Rose–Jackson |
| C3 | No existing cognitive theory imposes this symmetry | weak: an argument from absence; the authors concede a classical model can be built to satisfy it | Results, last paragraph |
| C4 | The result reveals a "quantum nature" of human judgments | not supported: the evidence supports the equality, which a constrained classical model could also meet, and which LIT-264 shows is a noncontextual pattern | title, Discussion |
| C5 | The equality is robust to partial updating | not checkable here | SI, not read |

## Concepts

- **context effect**: the difference between the two orders in the
  proportion of a response pair, cell by cell of the 2 × 2 table.
- **q value**: the sum of the two context effects on a diagonal. The QQ
  equality is E(q) = 0.
- **order effect (size)**: the sum of the absolute context effects on the
  diagonal with the larger sum.
- **law of reciprocity**: |⟨T|V⟩|² = |⟨V|T⟩|² for T = P_A S, V = P_B S;
  the paper presents it as the principle the equality tests.

## Connections

The model and the derivation are LIT-tmptn5dr's. LIT-264 obtained these
data from the authors, re-derived the equality from the identity
P Q P + (I − P)(I − Q)(I − P) = I − (P + Q) + (P Q + Q P), and showed it
implies the Contextuality-by-Default noncontextuality criterion for these
rank-2 cyclic systems. The Discussion leans on beim Graben and
Atmanspacher's account of incompatible observables arising from coarse
measurement of classical systems. The paper cites LIT-316 for proofs.

## Bearing on the record

- **Primary source of THEORY-tmp9wyar**: survey order effects satisfy the
  QQ equality, and the regularity does not discriminate quantum
  probability from every classical model, nor does it show
  contextuality.
- **THEORY-013.** The QQ data are the "73 poll question-order pairs" of
  LIT-264 §3. This reading adds that the data's own authors present the
  regularity as quantum, while the equality is exactly what makes the
  system noncontextual. The two papers agree on the data and differ on
  what it shows.
- **On the title.** "Reveal quantum nature" is stronger than anything in
  the body. The Discussion says that quantum probability "may provide a
  better description" even if the brain is classical, and the Results
  invite alternative accounts. The record should cite this paper for the
  equality and not for the title.
- No instruction for machine-learning practice; nothing for the
  anthology.

## Limitations

- The SI, which holds the proofs, the per-study table and the χ² tests,
  was not read here.
- The 66 Pew surveys are unselected for outcome, but they are all one
  organisation's question pairs and all in one country.
- The equality is a null hypothesis that is "accepted" by failing to
  reject. Many Pew order effects are small, and the paper itself notes
  that q is uninformative when the order effect is small; Fig. 1, right,
  addresses this for 17 studies only.
- The sample sizes are given as 651–3,006 participants per national
  study. LIT-264 gives the Pew N as 125–927. The two figures may count
  different things (whole samples, one order, or only yes/no
  respondents); neither paper says, and the discrepancy is unresolved
  here.

## Open questions

- A classical model fitted to the same 72 tables, constrained to satisfy
  the equality, and compared with the quantum model on the order effects
  themselves. The paper names this need and leaves it to others.
- Pre-registered question pairs with information inserted between the
  questions, to test C2 beyond one poll.
