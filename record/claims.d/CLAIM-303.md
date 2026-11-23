---
number: 303
status: Active
formerly:
- CLAIM-tmpygqjz
title: 'Filing an argument moves work across time: it is paid for now, in filing, indexing, tracking dependencies and checking it is still current, against reconstruction later, so it is worth its cost only when expected reuse covers it, and where reuse can be forecast, recurrence is evidence of reuse, not the criterion'
version: 5
history:
- version: 2
  date: '2026-11-18'
  note: >-
    CLAIM-308's objection conceded and written in (ADR-059), at the status
    review of 2026-11-18, at the status review's ruling (the owner
    delegated these rulings; ADR-057), when CLAIM-308 went Active. Where
    reuse cannot be forecast, CLAIM-308's break-even rule, a function of
    past recurrences weighted by reconstruction cost, is within
    2 − (c_a + u)/c_r of the hindsight optimum, and no deterministic rule
    without foresight guarantees materially better; recurrence so
    weighted is then the criterion. The last clause is restricted to reuse
    that can be forecast, the first of the two answers CLAIM-308 offered
    it, and "What it does not say" says so. Version 1's title read:
    'Filing an argument moves work across time: it is paid for now, in
    filing, indexing, tracking dependencies and checking it is still
    current, against reconstruction later, so it is worth its cost only
    when expected reuse covers it, and recurrence is evidence of reuse,
    not the criterion'. The status stays Proposed.
- version: 3
  date: '2026-11-18'
  note: >-
    Promoted at the status review's ruling (the owner delegated these
    rulings; ADR-057). Its grounds, THEORY-386 and THEORY-389, are
    Active; its one objection, CLAIM-308, is conceded and written in
    (version 2). Nothing meets its defeated_if: CLAIM-308 makes
    recurrence weighted by reconstruction cost the criterion only where
    reuse cannot be forecast, which the title now excepts, and it does
    not show the second-occurrence rule filing as well as any rule using
    cost estimates; CLAIM-630 shows the two parting once filing costs
    twice a reconstruction's overpayment. QUESTION-098 moves from
    answers to bears_on: as narrowed, the claim answers only where
    reuse can be forecast, as CLAIM-308 answers only where it cannot,
    and the question asks what the second-occurrence rule approximates
    and when it fails. Interpretive. The title is unchanged.
- version: 4
  date: '2026-11-18'
  note: >-
    Answers QUESTION-489, the part of QUESTION-098 split off
    under ADR-049 at the status review's ruling (the owner delegated
    these rulings): when a structure is worth filing, staleness set
    aside, under fixed known costs. It keeps bears_on QUESTION-098 for
    the open remainder.
- version: 5
  date: '2026-11-19'
  note: >-
    Joins the work cost-structure-of-possibility (ADR-106), the
    owner's manuscript from the exchange "Topological protection
    explained": A43 §3.1 states its proposition in general form, with
    §3.3 the costs of keeping. No other change.
role: thesis
warrant: interpretive
defeated_if: >-
  A record in which the second-occurrence rule is shown to file at least as well
  as any rule using estimates of reconstruction cost and staleness, so that recurrence
  is the criterion and not merely evidence for it. Or an accounting of the record's
  own filings in which upkeep and stale reuse are negligible, so that only the reuse
  count matters.
tags:
- design-rationale
- epistemology
date: '2026-10-15'
line: nucleating-argument
works:
- cost-structure-of-possibility
answers:
- QUESTION-489
bears_on:
- QUESTION-098
complements:
- CLAIM-185
- CLAIM-182
grounds:
- THEORY-386
- THEORY-389
summary: >-
  A11, at the owner's request for "content to the effect of computation-storage
  tradeoffs". A11's four expenditures (materialization, indexing, dependency tracking,
  refresh) and its break-even condition. The arithmetic is trivial. The thesis is
  about the record: that its second-occurrence rule ([ADR-032](../decisions.d/ADR-032.md)) and the nucleation
  threshold of [CLAIM-185](CLAIM-185.md) are approximations to this trade, and can fail in both
  directions.
---
<!-- inactive-ok-file: THEORY-2023 — Proposed; cited in this filing of 2026-11-19 -->
<!-- inactive-ok-file: CLAIM-603 CLAIM-731 — Proposed; cited in this filing of 2026-11-19 -->
<!-- inactive-ok-file: CLAIM-182 CLAIM-185 — Proposed; open claims and accounts cited as open, nothing here rests on their being settled -->

# CLAIM-303: Filing an argument moves work across time: it is paid for now, in filing, indexing, tracking dependencies and checking it is still current, against reconstruction later, so it is worth its cost only when expected reuse covers it, and where reuse can be forecast, recurrence is evidence of reuse, not the criterion

## The claim

A11: "Memory does not merely preserve information. It allocates work
across time. Filing an argument performs computation now to avoid
uncertain future reconstruction; indexing makes the result accessible;
dependency tracking makes it revisable; verification manages the risk of
reusing stale conclusions."

For a fixed workload: upfront cost F, reconstruction c_r per use, access
and verification c_a per use, upkeep u per use, n uses. Filing is cheaper
when F + n(c_a + u) < n·c_r, that is, when c_r > c_a + u and
n > F/(c_r − c_a − u). [CASE-088](../cases.d/CASE-088.md) works one case. A11 added the term that makes
this more than caching: "the cost of incorrectly reusing an obsolete
argument may exceed the cost of recomputing it", and "persistence can
preserve errors as efficiently as valid discoveries."

## What it bears on

[ADR-032](../decisions.d/ADR-032.md) files a thing the second time it turns up, as a throttle on
capture by agents. A11 reads recurrence as evidence of reuse: "But
frequency alone is not a sufficient filing rule: a rare,
expensive-to-reconstruct argument might deserve persistence more than an
often-repeated trivial observation." [CLAIM-185](CLAIM-185.md) calls the threshold
"whatever makes a structure persist"; this says what makes persisting
worth it. [CLAIM-182](CLAIM-182.md) is not touched: A11's null case, an argument filed for
20 units that never recurs, is an anchor that works and does not pay.

## What it does not say

- Not that the record's filing pays off. A11: "I would keep that last
  statement as a proposed economic account of nucleation, not an
  established explanation of how this particular repository performs."
- Not that recurrence is only evidence where reuse cannot be forecast.
  There [CLAIM-308](CLAIM-308.md)'s break-even rule, which files once the reconstruction
  overpaid so far would pass the cost of filing, is within
  2 − (c_a + u)/c_r of the hindsight optimum on every sequence of uses,
  and recurrence weighted by reconstruction cost is the criterion.
  [CLAIM-308](CLAIM-308.md)'s objection is conceded, and the title's last clause is
  restricted to reuse that can be forecast.
- Not that saved effort is better reasoning. A filed answer to an
  objection can be wrong, and can stop being right.

## Note of 2026-11-19: the exchange "Topological protection explained"

Two qualifications, both A's. (a) Deadline feasibility. This claim's break-even prices total work. With a per-task budget, stored work can move a task across the budget line before it has repaid its cost: "A learned capability can be operationally enabling before it has economically repaid its acquisition cost" (A62 §2; A39 §1 gives 12 units fresh against 3 with a framework, at a budget of 5). That is [CLAIM-571](CLAIM-571.md)'s point that a peak, not a total, can bind. It is filed in [CLAIM-761](CLAIM-761.md), which rests on this claim.

(b) Across agents. A fall in one party's operating cost may be work transferred, to past training, to maintenance or to other agents, not work saved. A62 §9 separates "work saved", "work transferred" and "valuable capability expanded", with a bureaucracy cheap for administrators because claimants do the work of fitting its categories; A41 §9 adds a recommender cheap for viewers that burdens creators "to remain legible to its classifications". This claim's accounting is one agent's. Neighbours: [CLAIM-060](CLAIM-060.md), [CLAIM-603](CLAIM-603.md), [CLAIM-676](CLAIM-676.md), [CLAIM-731](CLAIM-731.md). It is not filed as a claim, being close to definitional; the owner may want it.

No status change.

## Note of 2026-11-19: readings for the exchange "Topological protection explained"

Lu and Kankanhalli ([THEORY-2023](../theory.d/THEORY-2023.md)), read, apply this claim's criterion to test-time-trained skills and learn it: a skill pays adaptation compute now and is kept when expected reuse covers it, and of 100 reuses of earlier skills 61 helped and 1 harmed. Under a compute penalty the policy builds fewer costly skills without loss of utility. That supports the claim, for parameter skills, with an independent measured case. It leaves the defeat condition about the second-occurrence rule untouched, and the paper prices neither upkeep nor a stale skill.

No status change.

## Note of 2026-11-19: Howard and Ruder, read
An analogy ([NOTE-2141](../notes.d/NOTE-2141.md)): Howard and Ruder's pretraining "only needs to be performed once" and serves many tasks, stored work repaid by reuse, though they do no accounting.

## Note of 2026-11-22: a general model this claim is a case of
<!-- inactive-ok-file: CASE-326 CLAIM-891 — new; filed by LEAD-108's run of 2026-11-22 -->

[LEAD-108](../leads.d/LEAD-108.md)'s cost model ([CASE-326](../cases.d/CASE-326.md)) reduces to this claim's inequality,
and to [CASE-088](../cases.d/CASE-088.md)'s 45 against 34, when predictability is 1, staleness,
erosion and spill are 0, work has one price throughout and one party pays.
Each of those, at illustrative values, can take [CASE-088](../cases.d/CASE-088.md)'s saving to
nothing, and whose costs count decides its sign ([CLAIM-891](CLAIM-891.md)). No status
change.

## Note of 2026-11-23: the work transferred to claimants, filed

<!-- inactive-ok-block: CLAIM-tmpjg4h2 CLAIM-tmpbt43r — Proposed; filed from the exchange "Explain First Contact RL" -->
The point in (b) of the note of 2026-11-19, a bureaucracy cheap for
administrators because claimants do the work of fitting its categories,
left unfiled as close to definitional, came back at A56 §4 of the exchange
"Explain First Contact RL" (2026-11-23) with content of its own: who must
pay to make a proposal legible steers which questions an institution
pursues. It is filed as [CLAIM-tmpjg4h2](CLAIM-tmpjg4h2.md), in A's voice, on the owner's U29
([CLAIM-tmpbt43r](CLAIM-tmpbt43r.md)). No status change. The note is the assistant's (Claude, in
this session); adopting it is the owner's call.
