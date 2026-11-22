---
status: Proposed
title: 'One cost model for stored work, run on the cockpit''s speed bugs, a filed argument and a LEGO bin: every case is priced with the same terms; at illustrative values the bugs lose at a flat price of work on their four flap calls and win once the approach is at least twice as busy as the moment they are set, and the bin is made at once except for a brick that stands out'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-108. The model,
    its tests and the pricing script are committed under
    scratch/studies/lead-108/, with results.json and results.md.
standing: documented
kind: executed-study
tags:
- cognition
- information-retrieval
- operations-research
date: '2026-11-22'
line:
- distributed-agency
- nucleating-argument
- realizability
illustrates:
- CLAIM-tmpeklli
- CLAIM-tmpn0u3a
bears_on:
- QUESTION-095
- QUESTION-114
draws_on:
- THEORY-351
- THEORY-348
summary: >-
  LEAD-108 asked for one cost model for stored work, with terms for how
  predictable the later demand is, a retrieval cost that includes search, a
  staleness or bias cost and the erosion of the alternative, keeping
  operational feasibility, lifetime efficiency and distributed costs apart as
  CLAIM-761 and CLAIM-760 do, and then for the three cases of QUESTION-114
  priced with it. The model was written as code, with six tests (it reduces
  to CLAIM-303 and reproduces CASE-088's 45 against 34), and the three cases
  were priced from the sources' numbers where they exist (CASE-088, CLAIM-307)
  and from illustrative values, tagged as such, where they do not (Hutchins
  measured nothing). No case needed a term the others lack. What carries each
  case differs, and that is the result CLAIM-tmpeklli states. The wording is
  the assistant's (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-tmpeklli CLAIM-tmpn0u3a CLAIM-314 THEORY-351 — Proposed or new; filed or cited in this run of 2026-11-22 -->

# CASE-tmpo2iur: One cost model for stored work, run on the cockpit's speed bugs, a filed argument and a LEGO bin: every case is priced with the same terms; at illustrative values the bugs lose at a flat price of work on their four flap calls and win once the approach is at least twice as busy as the moment they are set, and the bin is made at once except for a brick that stands out

## The model

Two routes meet a stream of demands: compute each time (reconstruct,
search), or build a store once, keep it and read it back, falling back to
computing when it does not serve or is wrong. One unit of work throughout.
The terms, fixed before any case was priced (scratch/studies/lead-108/costmodel.py):

| term | meaning | from |
|---|---|---|
| F, λ_F | construction, and the price of work at the moment it is paid | CLAIM-303; the cockpit's low-workload phase |
| U | upkeep over the store's life | CLAIM-303 |
| π | predictability: the chance a demand is one the store serves | the lead |
| ρ, miss | retrieval per served demand (recognizing, searching, reading), and the cost of finding out it does not serve | the lead; CLAIM-314 |
| v, δ | verification per use, and the chance it catches a wrong result | CLAIM-303's c_a; CLAIM-761 |
| σ, L, R | chance the stored result is wrong for this demand (staleness or bias), loss if used undetected, revision when caught | the lead; CLAIM-761 |
| ε | erosion: rise in the on-demand cost, paid whenever the store route falls back on it | the lead (Risko and Gilbert) |
| spill | added retrieval cost the store imposes on other demands | CLAIM-310's k/2; CLAIM-314 |
| c, σ_A, L_A | the on-demand route's cost, chance of error and loss | CLAIM-303's c_r |
| λ, B | price of work at the moment of a demand, and the work available for it then | CLAIM-761's per-task budget; TERM-055 |
| party | who pays each item | CLAIM-760 |

Per served demand the store route costs ρ + v + σ[δ(c(1+ε) + R + σ_A L_A) +
(1 − δ)L]; an unserved one costs miss + c(1+ε) + σ_A L_A. Three verdicts are
reported apart: **feasibility**, the chance a demand is met correctly within
B, TERM-055's availability over the paths a demand can take; **lifetime**,
the priced total λ_F F + λ_U U + spill + Σ n λ (per-demand cost); and
**distribution**, the same totals by party.

Choices the lead left open, made here: costs are expectations, except
feasibility; no discounting; ε is a fixed fraction, not a function of how
long the store has been relied on; staleness is either priced (through L) or
held as a bound on the chance of an undetected wrong result, and each
scenario says which.

## What was run

`python3 -I price_cases.py`; the full table is in results.md. Selected rows:

| scenario | store | on demand | saving | break-even n | availability store / on demand |
|---|---:|---:|---:|---:|---|
| cockpit, 4 flap calls, approach 3× as busy | 11.8 | 18.0 | 6.2 | 2.2 | 0.99 / 0 |
| cockpit, 4 flap calls, flat price, no budget | 9.3 | 6.0 | −3.3 | 6.7 | 1.00 / 0.98 |
| cockpit, calls and 20 salmon-bug checks, 3× | 30.6 | 108.0 | 77.4 | 2.2 | 0.99 / 0 |
| filing, CASE-088 | 34.0 | 45.0 | 11.0 | 2.1 | 1 / 1 |
| filing, staleness priced | 46.0 | 45.0 | −1.0 | 3.1 | 0.95 / 1 |
| filing, in a large store | 45.0 | 45.0 | 0.0 | 3.0 | 1 / 1 |
| LEGO, one copy among 200 similar, deadline 12 | 76.5 | 1000 | 923.5 | 0.07 | 0.95 / 0 |
| LEGO, twenty copies | 31.3 | 95.2 | 64.0 | 0.86 | 1 / 1 |
| LEGO, a black brick among white | 27.0 | 10.0 | −17.0 | never | 1 / 1 |

**Cockpit** (NOTE-867, THEORY-351). π = 1: the task is fixed, mandated and
known. F (choose the card by the displayed weight, call, set four bugs,
cross-check) is paid 25 to 30 minutes ahead at λ_F = 1; the store lasts one
approach, so U = 0 and F recurs per flight. ρ is a judgement of spatial
proximity, with the cue supplied by the needle. Staleness is held as a bound,
not priced, since a wrong speed is a "killer" item and cross-checks are
mandated: the bugs' undetected-wrong chance (0.001) meets an illustrative
bound of 0.005, recall's (0.02) does not. All values are illustrative.
Sweeping the load ratio λ_high/λ_low with the four calls alone, the bugs lose at 1 and 1.5 and win from 2
(savings −3.3, −0.9, 1.5, 6.2, 15.7 at 1, 1.5, 2, 3, 5); with 24 reads they
win at every ratio. Erosion barely moves anything (saving 6.2 at ε = 0, 5.8
at ε = 3), since it is paid only on fallback and the bugs almost never fall
back. Counting the card booklet's share (2,000 units spread over 10,000
approaches, a different party's cost) changes the saving by 0.2.

**Filed argument** (CASE-088's numbers; the split of 3 into ρ = 1, v = 2 is
illustrative). The model reduces to CLAIM-303 exactly. Staleness priced (σ =
0.1, δ = 0.5, L = 60, R = 5, illustrative) turns a saving of 11 into a loss
of 1 at three uses; held as a bound instead (v raised to 5 to catch 95%), the
break-even moves to 3.5. Recognition by search (+2 per use, CLAIM-314),
upkeep of 2 (lint, link repair, CI) and a spill of 0.01 onto 300 other reuses
take it to break-even exactly at three. Without a forecast of n, CLAIM-308's
rule is within 2 − 3/15 = 1.8 of hindsight.

**LEGO bin** (CLAIM-307's m = 200 and deadline D = 12 items; F = 5, U = 1, ρ
= 2, a 5% chance the brick has been moved, illustrative). With one copy the
search, m/(c+1) = 100 items, is over the deadline, so without a bin the brick
is unavailable (CASE-094's "may as well not have the brick"), and the bin
pays at its first use. With twenty copies the search (9.5) is within the
deadline, so no bin is forced, but one still pays over ten uses: feasibility
and lifetime part, as CLAIM-761 says they can. A brick that stands out is
found in about one look, and a bin never pays. If bins are found by
scanning, the spill onto 200 other searches adds 100, and the bin still pays.
Since F is less than one search's overpayment, CLAIM-308's rule makes the bin
at the first find, which is CASE-094's practice.

**The owner's alternatives, priced** (filing, illustrative). Boundary:
counting only the session's work, break-even 1.7 (saving 16); counting the
owner's review at four times the session's price, 3.3 (loss 4). Who
reconstructs when the filing does not serve (π = 0.7): a fresh session, with
nothing to erode, break-even 3.0 (saving 0.2); the owner, whose own
reconstruction has become half again as costly, 4.1 (loss 6.6).

## What it can show

That one fixed set of terms prices all three cases, and which terms carry
each. Three results do not depend on the illustrative values. With π = 1 and
λ flat, the four flap calls repay the bugs only if F < 4(c − ρ − v), that is,
only if setting four bugs costs less than the reads it saves; where it does
not, the bugs pay through λ or B or not at all. Erosion is
weighted by the chance of falling back, (1 − π) + πσδ (CLAIM-tmpn0u3a), so it matters where
predictability is low and not where it is high. A cheap construction at the
moment of a demand (the found brick) and a construction at a quiet moment
(the bugs) are the same term, λ_F F.

## What it cannot show

- Any measured cost. Hutchins gives no timings or counts, so whether the
  bugs pay by reuse (the salmon-bug checks) or by moving work (the calls) is
  open. Feasibility on final approach favours them under either reading.
- That the terms are complete. Two strains are noted in CLAIM-tmpeklli:
  staleness in the cockpit is correlated across a whole approach, which an
  expectation per demand prices right on average and wrong in the tail; and
  the bug prompts the demand as well as answering it, which the model prices
  only as a lower chance of error on the bug route.
- Anything about the record's own filings. The filing numbers are A11's
  construction and illustrative values. CLAIM-303's caveat stands.
