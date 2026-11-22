---
status: Proposed
title: 'A check of signalling estimators, a guaranteed interval and an exact no-signalling test for binary Contextuality-by-Default systems, by enumeration and simulation, applied to the three binary systems a corpus study of ambiguous phrases prints as fractions'
version: 1
standing: documented
kind: executed-study
tags:
- mathematical-statistics
- contextuality
date: '2026-11-22'
line:
- pragmatic-transport
- formal-apparatus
draws_on:
- THEORY-177
reported_in:
- LIT-842
summary: >-
  Run in session for LEAD-072 on 2026-11-22 (scratch/studies/lead-072;
  sig.py with 9 passing tests, exact.py, mc.py, floor.py, apply.py; seeds
  fixed). Exact enumeration per content and 4,000-replication simulations
  of correlated rank-2 systems at 2 to 100 occurrences a context. The
  plug-in Δ's bias at zero signalling is 1.5 at two occurrences and 0.22
  at a hundred; the root of the unbiased squared difference cuts it by
  half or more and falls short at large Δ. The simultaneous
  Clopper-Pearson interval never covered below 0.999; Newcombe's
  approximate one fell to 0.93. The Bonferroni-Fisher test kept its size
  (at most 0.034 at 5%) and cannot reject at all below three occurrences.
  On LIT-842's printed systems, at the least counts their fractions
  allow, one signals by the interval, one by the test alone, one by
  neither; a fourth table is inconsistent as printed. LIT-851 could not
  be used. The wording is the assistant's (Claude, in this session);
  adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-tmp1o9d0 — new; the claim this study checks -->
<!-- inactive-ok-file: CLAIM-tmpalxab — Proposed; LEAD-182's finding on the plug-in's bias, cited for comparison -->

# CASE-tmpl6unn: A check of signalling estimators, a guaranteed interval and an exact no-signalling test for binary Contextuality-by-Default systems, by enumeration and simulation, applied to the three binary systems a corpus study of ambiguous phrases prints as fractions

## What was run

For LEAD-072, on 2026-11-22, the estimators, interval and test of
CLAIM-tmp1o9d0 were checked and applied. Code and results are in
scratch/studies/lead-072 (README.md says how to rerun; summary.md holds
the full tables).

- **Estimators of Δ** (CbD signalling, THEORY-177): the plug-in
  Σ2|x/n − y/m|, and the root-U2 estimator Σ2√max(0, U), U the unbiased
  estimate of (p − p′)².
- **Intervals for Δ at 95%**: the "box", simultaneous Clopper-Pearson
  intervals for the 2k context marginals at 0.05/(2k), valid by
  construction; and Newcombe's hybrid-score interval per content at
  0.05/k, folded and summed, approximate.
- **Test** of the null that no content signals: Fisher's exact test per
  content at 0.05/k.
- **Exact enumeration per content** for n = m in {1, 2, 3, 5, 10, 30, 100}
  and eight pairs (p, p′), with per-content signalling 0, 0.2, 0.5 and 1
  at base rates 0.5 and 0.15.
- **Simulation of whole rank-2 systems**: two contents recorded jointly
  in each of two contexts, with correlation inside each context, so the
  two contents' terms are dependent. Six models: two without signalling,
  and true Δ of 0.4, 1, 2 and 3; n = m in {2, 3, 5, 10, 30, 100}; 4,000
  replications a cell.
- **The floor** on any valid test, checked for every n, m up to 40.

## What it found

**1. The plug-in's bias, and what root-U2 buys.** With no signalling and
base rate 0.5, the plug-in Δ̂ of a rank-2 system averages 1.51 at two
occurrences a context, 0.71 at ten and 0.22 at a hundred; root-U2
averages 0.51, 0.31 and 0.09, with RMSE lower by about a third. Where
true Δ is 1, root-U2 falls short at small counts (0.74 at ten
occurrences, against the plug-in's 1.11), and per content at true term
1.0 its exact mean is 0.64 at two occurrences and 0.90 at ten. The
plug-in's bias at zero matches the record's earlier figures: per
content, exactly 1 at one occurrence (CLAIM-235's worked case) and 0.113
at a hundred, near CLAIM-tmpalxab's √(2/π) scaling.

**2. Coverage.** The box interval covered the true Δ in at least 99.95%
of replications in every simulated cell, and its exact per-content
coverage was at least 0.9993 in every enumerated cell: valid, and
conservative. Newcombe's interval, folded and summed, covered 0.928 at
ten occurrences with no signalling (Monte Carlo standard error about
0.004), so it is not a stated error in the sense the lead asks for.

**3. Size and power of the test.** Under both no-signalling models its
rejection rate was at most 0.034 at the 5% level. It never rejected at
two or three occurrences a context, as the floor requires. Power is
low at corpus-like counts: for true Δ = 0.4 it was 0.06 at ten
occurrences, 0.19 at thirty and 0.72 at a hundred; for true Δ = 1, 0.14
at ten, 0.47 at thirty and 0.97 at a hundred; for true Δ = 2, 0.61 at
ten. Certifying the level LIT-851 uses to rule a rank-2 system out of
contextuality, Δ ≥ 2, is harder still: the box's lower bound reached 2
only for true Δ = 3, in 1% of replications at thirty occurrences and
86% at a hundred, and never for true Δ = 2 or less.

**4. The floor.** The least worst-case null probability of any table is
nⁿmᵐ/(n+m)ⁿ⁺ᵐ in every case up to 40. At 5% a content needs at least
three occurrences in each context, or one in one and seven in the
other, before any valid test can call it signalling; at 2.5%, two and
four, or one and fifteen.

**5. LIT-842's printed systems.** LIT-851's 90 systems could not be used
(below). LIT-842 (arXiv:2107.14589v1, read from its LaTeX source) prints
four binary corpus systems as fractions. Counts are not given; each
row's count was taken as the least common denominator of its
fractions, the smallest count the row allows; the true count is a
multiple of it.

| system | least row counts | plug-in Δ | root-U2 Δ | 95% box interval | no-signalling p (Fisher, Bonferroni) |
|---|---|---|---|---|---|
| coach/boxer × lap/file (rank 4) | 11, 44, 53, 54 | 1.79 | 1.66 | [0.25, 4.69] | 3×10⁻⁷ |
| adopt/boxer (rank 2) | 30, 4 | 1.87 | 1.34 | [0, 3.76] | 0.005 |
| throw/pitcher (rank 2) | 10, 3 | 0.87 | 0 | [0, 3.56] | 1 |
| tap/box × pitcher/cabinet | — | — | — | — | — |

The coach system signals beyond sampling error by both the interval and
the test. Adopt/boxer signals by the exact test, but the guaranteed
interval reaches 0 until the counts are doubled, because the
subject-verb context rests on four occurrences. Throw/pitcher's Δ of
13/15 is not distinguishable from 0: its subject-verb context rests on
three occurrences, and its interval would leave 0 only at nineteen
times the least counts. The tap/box table's first row, 17/22 and 15/22,
sums to 32/22 as printed, so it was not analysed.

## What it can show

That a stated sampling error for CbD signalling exists at every count
and costs little to compute, and that the plug-in Δ̂ is not one: a
system's Δ̂ at a few occurrences says almost nothing, and below three
occurrences a context nothing a valid test can use. Where counts are
known, the interval and the test can replace the plug-in counts that
CLAIM-235 objects to. On the only corpus systems whose counts can be
inferred, the signalling LIT-842 reports holds up beyond sampling error
in one system of three by the guaranteed interval and in two by the
test.

## What it cannot show

- Anything about LIT-851's 90 systems. Its appendix prints proportions
  and err(Δ), not counts (NOTE-654), and its open copy, UCL Discovery
  eprint 10146180, answered with a Cloudflare challenge (HTTP 403) on
  2026-11-22; the Semantic Scholar API answered HTTP 429. Neither was
  retried.
- The true counts behind LIT-842's fractions. At larger multiples the
  intervals narrow; the verdicts above hold at the least counts and
  could only strengthen toward signalling.
- Anything about the CbD criterion's correlation term, the contextual
  fraction or deficiency.
- The most powerful valid test. Boschloo's unconditional test, in
  sig.py but not simulated, would be more powerful than Fisher's at the
  same guarantee.
