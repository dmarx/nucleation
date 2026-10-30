---
number: 342
status: Active
formerly:
- THEORY-tmpf8c2p
title: "In AlphaZero on 9×9 Hex, at fixed playing strength, training compute and tree-search compute substitute along a straight line in log–log space, about 15× less search for each 10× more training over about two decades of training compute, down to a one-node search; the trade is measured for one search and counts no games played"
version: 2
history:
- version: 2
  date: '2026-10-30'
  note: >-
    Promoted to Active under ADR-065, at the status review's ruling (the
    owner delegated these rulings). The title reports what one study, read
    in full in NOTE-884, measured, with the study's hedges kept, and
    nothing in the record contradicts it. The old promote_when read: "The
    same iso-performance measurement (training compute against search
    compute at fixed strength) made on another game, or on Hex with a
    standard AlphaZero implementation or larger networks, with the slope
    reported with its uncertainty and the unit of test-time compute
    stated. It promotes the account if the trade is again a straight line
    in log–log space ending at a one-node floor; it narrows it to Hex, or
    to this implementation, if the curve bends or the slope differs beyond
    the reported uncertainty. More snapshots of the same 9×9 runs, or a
    refit of the same data in another functional form, cannot settle it."
    Its demand for the same measurement on another game, or on Hex with a
    standard implementation or larger networks, asks for generality the
    title does not claim, and the author asks for it rather than asserting
    it; it moves to QUESTION-338.
tags:
- learning-theory
- anthology-candidate
date: '2026-10-15'
source:
- LIT-1069
summary: >-
  Jones (2021), [LIT-1069](../literature.d/LIT-1069.md), read in [NOTE-884](../notes.d/NOTE-884.md). Across about 200 AlphaZero
  models on Hex boards 3×3 to 9×9, the best Elo for a given training compute
  follows one change-point curve, shifted by a fixed factor of compute per
  board row. On 9×9 only, iso-Elo contours of training against
  test-time search compute are straight in log–log space (fit: log test =
  −1.2·log train + 0.004·Elo + 29) over roughly 1e14–1e16 FLOPS-seconds of
  training, ending at a one-node search. One game, one nonstandard
  implementation, no uncertainty on the fitted coefficients, and no count
  of how many searches the trained agent will run, so it gives an exchange
  rate, not an amortization.
bears_on:
- QUESTION-095
---
<!-- inactive-ok-file: CLAIM-295 — Proposed; open claims and accounts cited as open, nothing here rests on their being settled -->

# THEORY-342: In AlphaZero on 9×9 Hex, at fixed playing strength, training compute and tree-search compute substitute along a straight line in log–log space, about 15× less search for each 10× more training over about two decades of training compute, down to a one-node search; the trade is measured for one search and counts no games played

## Source

Jones (2021), [LIT-1069](../literature.d/LIT-1069.md) (arXiv 2104.03113v2), read in [NOTE-884](../notes.d/NOTE-884.md).

## What was actually shown

**The frontier.** About 200 AlphaZero models and 2,800 snapshots on Hex
boards 3×3 to 9×9, rated by Elo with perfect play (MoHex) at zero, fitted
by a five-parameter change-point model. "The slope of the incline is 500
Elo per order of magnitude increase in compute"; "The minimum compute
needed for perfect play increases 7× for each increment in board size."
Fits on small boards predict larger ones, with residual variance falling as
boards are added. Training compute is varied by depth, width and run
length only, with a 64-node search in training and in evaluation.

**The exchange rate.** For 9×9 snapshots, test-time tree size was varied
from 1 to 512 nodes, and for each Elo level the minimum training and
test-time compute reaching it were traced. "the trade-off is linear in
log-compute: for each additional 10× of train-time compute, about 15× of
test-time compute can be eliminated, down to a floor of a single-node tree
search." The fitted line is log(test) = −1.2·log(train) + 0.004·elo + 29;
a slope of −1.2 is about 16× per decade. The contours cover training
compute of about 1e14 to 1e16 FLOPS-seconds, test-time compute of about 1e6
to 1e9, and Elo from −1500 to −250.

**What could have come out the other way.** The contours could have
curved, or search could have been far cheaper than training at equal Elo;
the author expected the second and was "surprised that one could easily
substitute for the other". His account of the near one-for-one rate: "an
optimization at test-time needs only optimise over one sample, while
train-time compute meanwhile must optimise over the entire distribution of
samples."

## What this does not say

- **That the trade prices amortization.** The paper never says how many
  games or moves the trained agent will play, and does not state whether
  test-time compute is per move, per game or per evaluation. Adding a
  reuse count N to the fit (total cost train + N·k·train^−1.2) is the
  record's arithmetic in [NOTE-884](../notes.d/NOTE-884.md), not the paper's.
- **That it holds outside the measured range.** Below a one-node search no
  further training replaces search. Beyond 1e16 FLOPS-seconds, at Elo near
  perfect play, or on other board sizes the trade was not measured.
- **That the rate is general.** One game, small boards, a modified
  AlphaZero with small fully connected nets, Elo assuming transitivity
  (the top-agent check moves fitted parameters by up to about 40%), and no
  standard errors on −1.2, 0.004 or 29. The author asks twice for the test
  on other games.
- **That the two fits agree.** Holding test-time compute fixed, the trade
  fit implies about 300 Elo per decade of training (1.2/0.004), against the
  frontier's 500 at a fixed 64-node search; the paper does not reconcile
  them ([NOTE-884](../notes.d/NOTE-884.md)'s arithmetic).
- **That a trained policy stays fit.** Training and test draw positions
  from the same game and board, so the later query never leaves the
  training distribution. Nothing measures a shift, a stale policy or bias
  carried by training beyond what Elo absorbs.
- **Anything about how to allocate compute in practice.** This is a
  measured relation in one system. A rule for spending compute would be a
  practice and belongs in the Anthology of the SOTA.

## Connections

- [QUESTION-095](../questions.d/QUESTION-095.md)'s note of 2026-10-15 places this as precompute-and-leave-a-
  result (in the weights) against compute at the moment of use, lying on
  one smooth iso-performance curve, the shape the owner's conjecture
  predicts for those two strategies. It supplies the computational part of
  the trade ([CLAIM-295](../claims.d/CLAIM-295.md)'s second component) and none of expected reuse,
  retrieval cost, staleness or erosion. A one-node search is the floor of
  per-use cost: the retrieval cost of the precomputed store, which here is
  not traded.
- [THEORY-331](THEORY-331.md) adds the term this lacks, expected use, in language models.
