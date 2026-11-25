---
number: 326
status: Active
formerly:
- CASE-tmpo2iur
title: 'One cost model for stored work'
statement: >-
  One cost model for stored work, run on the cockpit's speed bugs, a filed
  argument and a LEGO bin: every case is priced with the same terms; at
  illustrative values the bugs lose at a flat price of work on their four
  flap calls and win once the approach is at least twice as busy as the
  moment they are set, and the bin is made at once except for a brick that
  stands out
version: 2
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-108. The model,
    its tests and the pricing script are committed under
    scratch/studies/lead-108/, with results.json and results.md.
- version: 2
  date: '2026-11-24'
  note: >-
    Promoted to Active at the owner's word of 2026-11-24 ("promote the
    ten", under the dialectic regime; ADR-057, status-review README
    section 2): a CASE goes Active when it is demonstrated, and its run
    has been checked by a session other than its filer's. Rerun on
    2026-11-24 from a copy of scratch/studies/lead-108/: the 7 tests of
    test_costmodel.py pass, and price_cases.py regenerates results.json
    and results.md byte for byte (the note of that date).
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
- CLAIM-891
- CLAIM-892
bears_on:
- QUESTION-095
- QUESTION-114
draws_on:
- THEORY-351
- THEORY-348
summary: >-
  [LEAD-108](../leads.d/LEAD-108.md) asked for one cost model for stored work, with terms for how
  predictable the later demand is, a retrieval cost that includes search, a
  staleness or bias cost and the erosion of the alternative, keeping
  operational feasibility, lifetime efficiency and distributed costs apart as
  [CLAIM-761](../claims.d/CLAIM-761.md) and [CLAIM-760](../claims.d/CLAIM-760.md) do, and then for the three cases of [QUESTION-114](../questions.d/QUESTION-114.md)
  priced with it. The model was written as code, with six tests (it reduces
  to [CLAIM-303](../claims.d/CLAIM-303.md) and reproduces [CASE-088](CASE-088.md)'s 45 against 34), and the three cases
  were priced from the sources' numbers where they exist ([CASE-088](CASE-088.md), [CLAIM-307](../claims.d/CLAIM-307.md))
  and from illustrative values, tagged as such, where they do not (Hutchins
  measured nothing). No case needed a term the others lack. What carries each
  case differs, and that is the result [CLAIM-891](../claims.d/CLAIM-891.md) states. The wording is
  the assistant's (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-891 CLAIM-314 THEORY-351 — Proposed or new; filed or cited in this run of 2026-11-22 -->

# CASE-326: One cost model for stored work

## The model

Two routes meet a stream of demands: compute each time (reconstruct,
search), or build a store once, keep it and read it back, falling back to
computing when it does not serve or is wrong. One unit of work throughout.
The terms, fixed before any case was priced (scratch/studies/lead-108/costmodel.py):

| term | meaning | from |
|---|---|---|
| F, λ_F | construction, and the price of work at the moment it is paid | [CLAIM-303](../claims.d/CLAIM-303.md); the cockpit's low-workload phase |
| U | upkeep over the store's life | [CLAIM-303](../claims.d/CLAIM-303.md) |
| π | predictability: the chance a demand is one the store serves | the lead |
| ρ, miss | retrieval per served demand (recognizing, searching, reading), and the cost of finding out it does not serve | the lead; [CLAIM-314](../claims.d/CLAIM-314.md) |
| v, δ | verification per use, and the chance it catches a wrong result | [CLAIM-303](../claims.d/CLAIM-303.md)'s c_a; [CLAIM-761](../claims.d/CLAIM-761.md) |
| σ, L, R | chance the stored result is wrong for this demand (staleness or bias), loss if used undetected, revision when caught | the lead; [CLAIM-761](../claims.d/CLAIM-761.md) |
| ε | erosion: rise in the on-demand cost, paid whenever the store route falls back on it | the lead (Risko and Gilbert) |
| spill | added retrieval cost the store imposes on other demands | [CLAIM-310](../claims.d/CLAIM-310.md)'s k/2; [CLAIM-314](../claims.d/CLAIM-314.md) |
| c, σ_A, L_A | the on-demand route's cost, chance of error and loss | [CLAIM-303](../claims.d/CLAIM-303.md)'s c_r |
| λ, B | price of work at the moment of a demand, and the work available for it then | [CLAIM-761](../claims.d/CLAIM-761.md)'s per-task budget; [TERM-055](../terms.d/TERM-055.md) |
| party | who pays each item | [CLAIM-760](../claims.d/CLAIM-760.md) |

Per served demand the store route costs ρ + v + σ[δ(c(1+ε) + R + σ_A L_A) +
(1 − δ)L]; an unserved one costs miss + c(1+ε) + σ_A L_A. Three verdicts are
reported apart: **feasibility**, the chance a demand is met correctly within
B, [TERM-055](../terms.d/TERM-055.md)'s availability over the paths a demand can take; **lifetime**,
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
| filing, [CASE-088](CASE-088.md) | 34.0 | 45.0 | 11.0 | 2.1 | 1 / 1 |
| filing, staleness priced | 46.0 | 45.0 | −1.0 | 3.1 | 0.95 / 1 |
| filing, in a large store | 45.0 | 45.0 | 0.0 | 3.0 | 1 / 1 |
| LEGO, one copy among 200 similar, deadline 12 | 76.5 | 1000 | 923.5 | 0.07 | 0.95 / 0 |
| LEGO, twenty copies | 31.3 | 95.2 | 64.0 | 0.86 | 1 / 1 |
| LEGO, a black brick among white | 27.0 | 10.0 | −17.0 | never | 1 / 1 |

**Cockpit** ([NOTE-867](../notes.d/NOTE-867.md), [THEORY-351](../theory.d/THEORY-351.md)). π = 1: the task is fixed, mandated and
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

**Filed argument** ([CASE-088](CASE-088.md)'s numbers; the split of 3 into ρ = 1, v = 2 is
illustrative). The model reduces to [CLAIM-303](../claims.d/CLAIM-303.md) exactly. Staleness priced (σ =
0.1, δ = 0.5, L = 60, R = 5, illustrative) turns a saving of 11 into a loss
of 1 at three uses; held as a bound instead (v raised to 5 to catch 95%), the
break-even moves to 3.5. Recognition by search (+2 per use, [CLAIM-314](../claims.d/CLAIM-314.md)),
upkeep of 2 (lint, link repair, CI) and a spill of 0.01 onto 300 other reuses
take it to break-even exactly at three. Without a forecast of n, [CLAIM-308](../claims.d/CLAIM-308.md)'s
rule is within 2 − 3/15 = 1.8 of hindsight.

**LEGO bin** ([CLAIM-307](../claims.d/CLAIM-307.md)'s m = 200 and deadline D = 12 items; F = 5, U = 1, ρ
= 2, a 5% chance the brick has been moved, illustrative). With one copy the
search, m/(c+1) = 100 items, is over the deadline, so without a bin the brick
is unavailable ([CASE-094](CASE-094.md)'s "may as well not have the brick"), and the bin
pays at its first use. With twenty copies the search (9.5) is within the
deadline, so no bin is forced, but one still pays over ten uses: feasibility
and lifetime part, as [CLAIM-761](../claims.d/CLAIM-761.md) says they can. A brick that stands out is
found in about one look, and a bin never pays. If bins are found by
scanning, the spill onto 200 other searches adds 100, and the bin still pays.
Since F is less than one search's overpayment, [CLAIM-308](../claims.d/CLAIM-308.md)'s rule makes the bin
at the first find, which is [CASE-094](CASE-094.md)'s practice.

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
weighted by the chance of falling back, (1 − π) + πσδ ([CLAIM-892](../claims.d/CLAIM-892.md)), so it matters where
predictability is low and not where it is high. A cheap construction at the
moment of a demand (the found brick) and a construction at a quiet moment
(the bugs) are the same term, λ_F F.

## What it cannot show

- Any measured cost. Hutchins gives no timings or counts, so whether the
  bugs pay by reuse (the salmon-bug checks) or by moving work (the calls) is
  open. Feasibility on final approach favours them under either reading.
- That the terms are complete. Two strains are noted in [CLAIM-891](../claims.d/CLAIM-891.md):
  staleness in the cockpit is correlated across a whole approach, which an
  expectation per demand prices right on average and wrong in the tail; and
  the bug prompts the demand as well as answering it, which the model prices
  only as a lower chance of error on the bug route.
- Anything about the record's own filings. The filing numbers are A11's
  construction and illustrative values. [CLAIM-303](../claims.d/CLAIM-303.md)'s caveat stands.

<!-- inactive-ok-file: ARG-246 CLAIM-1319 — Proposed; filed or cited in the note of 2026-11-24 from the exchange 'Memes, Contracts, and Systemic Normativity', cited with their standing -->

## Note of 2026-11-24: the exchange 'Memes, Contracts, and Systemic Normativity', A30, a contract reading and its limit

A30 §2 reads this case's terms as a contract's lifecycle (F formation, U
upkeep of expectations, ρ identifying and invoking the contract, v and δ
checking applicability and compliance, σ inadequacy of inherited
arrangements, R renegotiation, ε loss of independent capability through
reliance) and quotes the served-demand formula exactly. "A contract
amortizes the work of establishing mutually intelligible expectations and
coordinating interdependent activity." Its limit, A30 §15: "the current
CASE-326 implementation uses fixed erosion and does not establish the full
endogenous contractual dynamics described here." A qualification of
scope, not of the case: for a store whose use changes it, σ and ε are not
fixed. [ARG-246](../arguments.d/ARG-246.md) holds the judgement, [CLAIM-1319](../claims.d/CLAIM-1319.md) the claim, and
[LEAD-237](../leads.d/LEAD-237.md) the extension that would test it. The wording of this note is the assistant's (Claude, in this session), reporting A's (ChatGPT's) text; adopting what it reports is the owner's call.

## Note of 2026-11-24: rerun, for the promotion review the owner proposed at U33 of the exchange 'Memes, Contracts, and Systemic Normativity'

Rerun on 2026-11-24 by the assistant, from a copy of `scratch/studies/lead-108/` as on this branch: the 7 tests of `test_costmodel.py` pass, and `price_cases.py` regenerates `results.json` and `results.md` byte for byte. A53 of the exchange names this case as a promotion candidate, a study "executed" and awaiting review. The run is now checked by a session other than the one that filed it, which the status-review README (section 2) asks of a demonstrated case; the ruling is the status review's ([LEAD-235](../leads.d/LEAD-235.md)). The note is the assistant's (Claude, in this session). No status change.
