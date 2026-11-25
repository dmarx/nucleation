---
number: 577
status: Active
formerly:
- CLAIM-tmplo4ca
title: 'A budget set each period to the peak resource spent the period before never rises, so the configurations an organization can reach shrink monotonically, and any transition whose threshold exceeds the cost of holding the current configuration is lost after one period spent holding it, unless the budget is raised from outside by at least the difference'
version: 8
history:
- version: 2
  date: '2026-11-06'
  note: >-
    Revised at the twenty-sixth status review (ADR-057), at the status
    review's ruling (the owner delegated these rulings), so that its use of
    TERM-106 says which sense. Step 3 and the summary named "positive
    reconfiguration slack against the current configuration", which is
    B*(q, q') − r(q), not the term's threshold less the costlier endpoint;
    they now name the one-sided form, the slack from q, which TERM-106
    defines in the same change. The construction is unchanged.
- version: 3
  date: '2026-11-06'
  note: >-
    Promoted at the twenty-seventh status review (ADR-057), at the status
    review's ruling (the owner delegated these rulings). TERM-110 leaves
    uses: the claim is not stated in it. TERM-110's ratchet effect is an
    agent's distortion of its performance under a principal that cannot
    commit, while the organization here does not respond to the rule, and
    the term itself sets aside "one-way mechanisms with no strategic
    party"; a sentence under "What it does not say" now says so. Its
    premises, CLAIM-571 and TERM-106, are Active, no objection is filed,
    and the construction was re-checked step by step. Nothing in the
    record meets its defeated_if.
- version: 4
  date: '2026-11-11'
  note: >-
    Bears on QUESTION-386, which the body named only in prose (a defect
    listed in the curation entry of 2026-11-10). Its "What it adds" says
    the budget rule is a mechanism "which is why A's worry about
    utilization-based budgeting (QUESTION-386) can come true without
    anyone wanting it": evidence for the question, not an answer to it.
    Under ADR-085 the relation gives this claim QUESTION-386's first
    line, readiness, which it already carries. No other change.
- version: 5
  date: '2026-11-11'
  note: >-
    Bears on QUESTION-373, at the reading review of 2026-11-11 (by
    question, ADR-091). Its own title: a transition whose threshold
    exceeds the holding cost is lost "unless the budget is raised from
    outside by at least the difference", which is who supplies the
    resource across the bottleneck; the question: "CLAIM-577 says one
    condition it needs: a budget rule that does not pin the reserve to the
    holding cost." Carries realizability, QUESTION-373's first line, after
    its own (ADR-085). No other change.
- version: 6
  date: '2026-11-23'
  note: >-
    Joins the work governance-of-possibility (ADR-144), the owner's
    manuscript from the exchange "Explain First Contact RL": A48 §9.1
    states its mechanism, the utilization-matched budget that loses the
    transition. No other change.
- version: 7
  date: '2026-11-25'
  note: >-
    Gains the line governing-possibility (atlas scope 14) under ADR-
    tmpd3ckn: the entry is in that scope's core fiber in the hyperarticle
    atlas v0.3 (scratch/atlas/atlas-v0.3.md), and each atlas scope is
    documented as a line. No other change.
- version: 8
  date: '2026-11-25'
  note: >-
    Joins the work atlas (ADR-149): the hyperarticle atlas v0.3
    states its proposition or uses it as a step, in scope 14. No other
    change.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the construction: a period, under the rule as stated, in
  which the budget rises without an outside increase; a reachable set that
  grows from one period to the next; or a transition with a threshold above
  the holding cost that stays reachable after a period spent holding.
  Not defeated by budget rules with a floor, growth term, carry-over or
  discretion, which the claim does not cover, nor by cumulative or
  rate-limited resources; the claim is about one capacity resource under
  the pure spend-matching rule.
tags:
- operations-research
- society-and-governance
- mathematics
date: '2026-11-05'
line:
- readiness
- formal-apparatus
- realizability
- governing-possibility
rests_on:
- CLAIM-571
complements:
- CLAIM-079
- CLAIM-557
uses:
- TERM-106
summary: >-
  The assistant's own proposition, offered at the owner's invitation on
  2026-11-05 after the constraint-architecture and emergency-readiness
  filings. It joins A's budget ratchet to the transition threshold of
  [CLAIM-571](CLAIM-571.md). Under a capacity budget set each period to the previous
  period's peak spending, an organization that only holds its configuration
  spends the holding cost, so its budget falls to that cost and stays
  there; what it can reach is the connected part of the sublevel set at
  that level around where it is, and every transition needing slack from
  where it is, TERM-106's one-sided form, is lost without anyone choosing to give it up and without any sign
  in routine output. It is [CLAIM-079](CLAIM-079.md)'s stability without viability, produced
  by a budget rule. Demonstrated for the pure rule; real budget rules have
  floors, growth and discretion that weaken it. The wording is the
  assistant's (Claude, in this session); adopting it is the owner's call.
bears_on:
- QUESTION-386
- QUESTION-373
works:
- atlas
- governance-of-possibility
---
<!-- inactive-ok-file: CASE-200 CASE-203 — Proposed or Skimmed; entries of 2026-11-04 and 2026-11-05 from the readiness and constraint-architecture filings, cited as open -->

# CLAIM-577: A budget set each period to the peak resource spent the period before never rises, so the configurations an organization can reach shrink monotonically, and any transition whose threshold exceeds the cost of holding the current configuration is lost after one period spent holding it, unless the budget is raised from outside by at least the difference

## The claim

Let a connected configuration space Q carry a capacity requirement
r(q) ≥ 0, and let the threshold B*(q, q′) of a transition be as in
[CLAIM-571](CLAIM-571.md): the least, over admissible paths, of the peak of r along
the path. In period t the organization has budget B_t, may move along any
path whose peak is at most B_t, and spends s_t, the peak of r over what it
occupied in the period. The rule is

  B_{t+1} = s_t.

Then:

1. **The budget never rises.** s_t ≤ B_t, since nothing above the budget
   can be occupied, so B_{t+1} ≤ B_t.
2. **What is reachable shrinks.** At budget B, the configurations
   reachable from q are R_B(q), the connected component containing q of the
   sublevel set {r ≤ B}. If the organization ends period t at q_{t+1}, then
   q_{t+1} ∈ R_{B_t}(q_t), and R_{B_{t+1}}(q_{t+1}) ⊆ R_{B_t}(q_t), because
   a smaller sublevel set's component through a point of the larger
   component lies inside it.
3. **Holding forecloses.** A period spent holding q costs r(q), so
   B_{t+1} = r(q). Any transition from q with B*(q, q′) > r(q), that is
   with positive slack from q, B*(q, q′) − r(q), the one-sided form of
   reconfiguration slack ([TERM-106](../terms.d/TERM-106.md)), is then out of reach in every later
   period. That includes a move to a configuration costlier to hold than q
   whose two-sided slack is zero.
4. **Only outside money restores it.** Under the rule the budget cannot
   climb back, so reaching q′ again needs an increase from outside of at
   least B*(q, q′) − r(q), the slack from q.

## Worked instance

A's example: r(q) = 0.7 + 2.4q(1 − q) on [0, 1], with B* = 1.3 between the
two ends, each held at 0.7. Start at q = 0 with B_0 = 1.3: the transition is
affordable. Spend the period holding at q = 0: s_0 = 0.7, so B_1 = 0.7,
and the sublevel set at 0.7 is the two endpoints alone. The transition is
gone, and so is every move at all. [CASE-200](../cases.d/CASE-200.md) is the same numbers with a
carry-over rule, under which the transition survives.

## What it adds

- **It is a mechanism, not a choice.** Nothing in the rule decides to give
  up the transition; ordinary efficient operation does it, which is why A's
  worry about utilization-based budgeting ([QUESTION-386](../questions.d/QUESTION-386.md)) can come true
  without anyone wanting it.
- **The loss leaves no trace in output.** The organization holds its
  configuration as well as before; only the set of places it could go has
  changed. [CLAIM-414](CLAIM-414.md)'s matched trajectories and the unrecorded calls of
  [CASE-203](../cases.d/CASE-203.md) are the observational side of this.
- **It is stability without viability by budget** ([CLAIM-079](CLAIM-079.md)): the
  organization stays in a stable regime while losing the transitions it
  would need when that regime stops serving.

## What it does not say

- Real budget rules are rarely pure spend-matching. A floor B̄ ≥ B*, a
  growth term, carry-over ([CASE-200](../cases.d/CASE-200.md)) or discretion each break the
  argument, and which real rules are close enough to the pure one is
  empirical.
- It concerns one capacity resource. Cumulative and rate-limited budgets
  ([TERM-105](../terms.d/TERM-105.md)) need their own treatment, and several resources at once
  bring in [CLAIM-585](CLAIM-585.md).
- It says nothing about whether the lost transitions were worth keeping.
- It is not a ratchet effect in [TERM-110](../terms.d/TERM-110.md)'s incentive sense. The rule is a
  principal's revision of the budget on what spending reveals, but the
  organization here does not anticipate it. One that did, and could reach
  a configuration costing its whole budget, would occupy it each period
  and so keep the budget from falling, which is the over-spending [TERM-110](../terms.d/TERM-110.md)
  describes.

## Note of 2026-11-05: A's fourth paste, and the assistant's contributions

[CLAIM-557](CLAIM-557.md) reads this claim as a decoupling of two budgets: spend-matching shrinks the acting budget, fragmenting what the organization can become, while the observing budget, and so what outsiders can tell apart, is untouched. No status changes.

## Note of 2026-11-05: the DNA origami readings, read across

The assistant's reading across the eight DNA origami readings filed on the owner's request to connect the record's inquiry to DNA origami. The wording is the assistant's (Claude, in this session); adopting it is the owner's call.

DNA origami assembly runs on the opposite rule. Rothemund ([NOTE-1631](../notes.d/NOTE-1631.md)) supplies each staple far above what folding consumes: at 1:1 about 1 % of structures were rectangles and at 1.5:1 they looked "moth-eaten", while a 10-fold excess is called "a “safe” concentration". A supply matched to consumption would starve the rare, late-binding staples a fold needs. The analogy is loose, since staples are consumed once and not budgeted period by period, but it shows a self-assembling system whose reliability depends on standing excess over spend, the slack the claim says spend-matching removes. Majikes et al. 2021 qualify it: for a single fold, excess beyond stoichiometry lowers yield, because two staples can each take one end and block the fold. So the slack that helps a whole origami is a window there, not more-is-better, and the authors' hypothesis for why whole origami tolerate it is that folding displaces the blocking strands.

No status changes.

## Note of 2026-11-22: its first organizational test

[LEAD-080](../leads.d/LEAD-080.md) ran A's readiness simulator under this rule and under carry-over ([CASE-315](../cases.d/CASE-315.md)). The prediction [QUESTION-394](../questions.d/QUESTION-394.md) drew from the claim holds there: a heavy rescue squad priced out after a month in which nothing mobilized it never came back, and under full carry-over it was never lost. A quiet period in an organization turned out to be a month without any mobilization, whether a rescue, a drill, a false alarm or a cancelled provisional dispatch, so the dispatch policy sets how long the capability survives the rule ([CLAIM-878](CLAIM-878.md), which rests on this claim). The run also bears on the scope stated under "What it does not say": the peak rule with a partial rollover, B_{t+1} = s_t + ρ(B_t − s_t) with ρ < 1, behaved exactly as the pure rule, since one held period leaves the budget below the threshold and nothing above it can be spent again; and [CASE-200](../cases.d/CASE-200.md)'s carry-over rule kept the transition but, used every period, allowed it only in every other period. No status changes.

## Note of 2026-11-22: a rule with a base and a payment per use

[LEAD-036](../leads.d/LEAD-036.md) ran [QUESTION-386](../questions.d/QUESTION-386.md)'s funding loop under A's rule B_{t+1} = B̄ + ηM_t, with competence bought from the budget and a capability committed only when competent enough ([CASE-343](../cases.d/CASE-343.md)). It bears on the scope stated under "What it does not say": a floor B̄ breaks this claim's argument, but where the floor alone sustains competence below the level at which the capability is used, the same loss returns, after a stretch without use set by the decay rate rather than after one held period, and only funding maintenance apart from use prevents it ([CLAIM-921](CLAIM-921.md)). No status changes.

<!-- inactive-ok-file: TERM-167 — Proposed; filed in this filing of 2026-11-22 (second share) -->

## Note of 2026-11-22: the industrial reading

A36 of the exchange "Explain First Contact RL" (second share, ChatGPT,
2026-11-22) uses this claim's budget rule verbatim, configurations A and
B costing 1 and the route through M costing 3, as the industrial case of
lost reorganization capacity: "Utilization-based optimization can
destroy capacity whose value appears only under counterfactual future
conditions." A36 names three remedies: reserves, carry-over, and a
cheaper transition architecture. Each acts through a different mechanism.
[TERM-167](../terms.d/TERM-167.md) cites it.

## Note of 2026-11-23: the manuscript governance-of-possibility

Restatement and an objection. A48 §9.1 of the owner's manuscript (ADR-
tmpsfjxu) restates A36's case of this claim. Its §9.3 redesigned route, with
a staging path of peak 2, is lost under this claim's own rule after one
period unless a reserve is also held, which [CLAIM-1099](CLAIM-1099.md) derives and
scratch/formal/redesign_reserve_check.py checks.
