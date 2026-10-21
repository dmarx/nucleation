---
status: Active
title: 'In Arthur''s model of two agent types arriving in random order, each adopting whichever of two technologies pays it more, with returns linear in previous adoptions, increasing returns make the adoption difference a random walk with absorbing barriers: one technology takes the whole market with probability one, A with probability Δ_R/(Δ_R + Δ_S) where Δ_R and Δ_S are the gaps at which each type switches, the winner need not be the better technology, and once it has locked in no small change in returns alters later choices; with diminishing returns the barriers reflect and the shares go predictably to one half'
version: 1
history:
- version: 1
  date: '2026-10-21'
  note: >-
    Filed Active from NOTE-tmpyyaar, a full reading of the 1983 IIASA
    working paper that preceded the article the LIT names; the article
    itself was not reached. The switching gaps and the absorption
    probability, garbled in the scan's OCR, are re-derived below, and the
    regimes were checked by simulation. A checked re-derivation meets the
    condition for Active under ADR-047 v2. The comparison with
    CLAIM-tmpptl3y is the record's.
tags:
- social-science
- complex-systems
date: '2026-10-21'
source:
- LIT-tmp5l842
summary: >-
  Arthur (1983 working paper; published 1989), LIT-tmp5l842, read in
  NOTE-tmpyyaar. A result about one model: two types, linear returns, no
  expectations, no pricing, no sponsors. It does not show that any
  historical technology won by small events, and the "efficiency" it says
  can fail is a weak search criterion. Its lock-in is absorption in
  accumulated adoptions, which a small reversal of returns cannot undo.
---
<!-- inactive-ok-file: THEORY-429 — Proposed; a held reading named for comparison, nothing here rests on it -->
# THEORY-tmpxzls4: In Arthur's model of two agent types arriving in random order, each adopting whichever of two technologies pays it more, with returns linear in previous adoptions, increasing returns make the adoption difference a random walk with absorbing barriers: one technology takes the whole market with probability one, A with probability Δ_R/(Δ_R + Δ_S) where Δ_R and Δ_S are the gaps at which each type switches, the winner need not be the better technology, and once it has locked in no small change in returns alters later choices; with diminishing returns the barriers reflect and the shares go predictably to one half

## Source

Arthur, W. B., "On Competing Technologies and Historical Small Events: The
Dynamics of Choice under Increasing Returns", IIASA WP-83-90 (1983), the
precursor of the *Economic Journal* article (1989) in LIT-tmp5l842. Read in
full in NOTE-tmpyyaar. The derivation below is the record's.

## What was actually shown

Agents arrive one at a time, each an R or an S with probability one half,
and adopt the technology with the higher return to them. With n_A and n_B
previous adopters, an R-agent gets a_R + r n_A from A and b_R + r n_B from
B, and an S-agent a_S + s n_A and b_S + s n_B, with a_R > b_R and
a_S < b_S. Let d = n_A − n_B.

**Switching gaps (increasing returns, r, s > 0).** An R-agent chooses B
iff b_R + r n_B > a_R + r n_A, that is d < −Δ_R with
Δ_R = (a_R − b_R)/r. An S-agent chooses A iff d > Δ_S with
Δ_S = (b_S − a_S)/s. Inside (−Δ_R, Δ_S) each type takes its own favourite,
so d moves ±1 with probability one half: a fair walk. Once d passes Δ_S,
both types choose A, d only rises, and it never returns. The same holds for
B below −Δ_R. These are the paper's absorbing barriers.

**Lock-in and its odds.** A fair walk between two absorbing barriers is
absorbed with probability one, so the share of A goes to 0 or 1. By
gambler's ruin from d = 0, A wins with probability
Δ_R/(Δ_R + Δ_S) = s(a_R − b_R)/(s(a_R − b_R) + r(b_S − a_S)). The observer
knows this number and not the outcome.

**Diminishing returns (r, s < 0).** The inequalities reverse: an R-agent
switches to B when A is far enough ahead, and an S-agent to A when B is. So
both types choose the technology behind, the barriers reflect, d stays
between constants, and d/n → 0. Shares go to one half from every sequence
of arrivals: predictable and ergodic.

**Inflexibility.** After absorption, the gap in returns between the
leader and the other grows linearly in n. A change of either returns
function by a small ε shifts the barrier by ε/r and is passed, so it does
not change any later choice.

**Simulation, here.** 2,000 runs of 4,000 arrivals each, with a_R = 1,
b_R = 0, a_S = 0, b_S = 1. With r = s = 0.1, every run locked in, and A won
47% of them (predicted 50%). With b_S = 2, it won 30.5% (predicted
33.3%). With s = 0.3, it won 73% (predicted 75%). The shortfall is the
discrete barriers and ties broken toward B, and it shrank with finer
barriers (r = s = 0.04 and b_S = 2: 31.3% of 1,000 runs, with 3% not yet
locked by 20,000 arrivals, predicted 33.3%; s = 0.12: 74.6%, predicted
75%). With r = s = −0.1 the share of A was 0.500 with a standard
deviation of 0.0008. With r = s = 0 it was 0.500 with a standard
deviation of 0.008.

What could have failed: the walk could have wandered for ever between the
barriers, keeping both technologies in the market. It does not, because a
fair walk on a finite interval is absorbed.

## What this does not say

- **Not that any real technology won this way.** The paper's QWERTY,
  rail-gauge and steam-car stories are illustrations it does not analyse.
- **Not that the winner is worse.** Only that it need not be better. With
  returns rising at different rates, "the adoption process may easily
  become inefficient". The efficiency criterion is weak: no unadopted
  option better than an adopted one.
- **Not beyond the model.** Expectations, pricing, sponsors who can
  subsidize, and agents who can wait are excluded and named as open. The
  extensions to N technologies, unequal type shares and nonlinear returns
  are stated without proof. With returns that level off, the market can be
  shared.
- **Not about the 1989 article's model.** That text was not read.

## Connections

- **CLAIM-tmpptl3y.** Both are symmetric dynamics that select one side.
  They differ in what happens when the conditions are reversed. In the
  pitchfork, restoring κ > α restores the equal allocation. Here, lock-in
  is absorption in accumulated adoptions. Arthur: "Small subsidies to the
  excluded choice will not re-establish it; large subsidies, on the other
  hand, will swing the market and drive the dominant choice out." The
  persistence is stored in a state variable that the reversal does not
  touch.
- **CASE-112.** Arthur's advice to "'tilt' the process ... toward the
  favored technology at the outset" is the tilt h applied before the
  symmetric state breaks. After lock-in a small tilt does nothing, as in
  CASE-112's hysteresis in h.
- **THEORY-429.** North carries increasing returns to institutions.
