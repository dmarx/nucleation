---
number: 308
status: Proposed
formerly:
- CLAIM-tmpc3sk7
title: 'Where reuse cannot be forecast, recurrence weighted by reconstruction cost is the filing criterion, not only evidence for one: filing at the first use at which reconstructing again would take the overpayment past the cost of filing is within 2 − (c_a + u)/c_r of the hindsight optimum on every sequence of uses, at most twice, and no deterministic rule without foresight guarantees materially better, under fixed known costs, with staleness left out and the cost of recognizing what a filed argument answers taken as fixed'
version: 3
history:
- version: 2
  date: '2026-10-19'
  note: >-
    Corrected at the owner's direction, carrying out the promotion audit's
    decision (record/promotion-audit/decisions/CLAIM-308.yaml, batch 002,
    ADR-047). The title and the lower-bound sentence dropped THEORY-348's
    "deterministic": no deterministic rule without foresight guarantees
    better than 2, but a randomized rule can do better in expectation. The
    qualifier is restored, and a bullet on randomized rules and on small F
    relative to the per-use overpayment is added. The upper bound was
    re-derived for the review and holds. The status stays Proposed: this is
    a counter, and CLAIM-314's objection to it is open.
- version: 3
  date: '2026-10-30'
  note: >-
    Corrected at the eighteenth status review (ADR-057), at the status
    review's ruling (the owner delegated these rulings). A step-by-step
    re-derivation with controls, described in the pass's workbench entry,
    found the lower bound mis-stated for a filed state with a per-use
    cost. The break-even rule is within 2 − (c_a + u)/c_r of hindsight,
    and no deterministic rule guarantees materially better, so "twice" is
    reached only as c_a + u becomes negligible beside c_r. Filing once the
    overpayment has reached F, rather than before it would pass F, can
    exceed 2, so the rounding is now stated. CLAIM-314's objection is
    conceded and written in (ADR-059): the guarantee needs recognizing
    what a filed argument answers to cost a fixed amount per use, which
    fails where reuse is found by search over the store. Version 2's
    title read: 'Where reuse cannot be forecast, recurrence weighted by
    reconstruction cost is the filing criterion, not only evidence for
    one: filing once the reconstruction already paid for equals the cost
    of filing is within twice the hindsight optimum on every sequence of
    uses, and no deterministic rule without foresight does better, under
    fixed known costs and with staleness left out'. The status stays
    Proposed.
role: counter
warrant: demonstrated
tags:
- design-rationale
- epistemology
date: '2026-10-15'
line: nucleating-argument
objects_to:
- CLAIM-303
grounds:
- THEORY-348
summary: >-
  Filed at the owner's request, from the rent-or-buy result of Karlin et al.
  1988 ([THEORY-348](../theory.d/THEORY-348.md)) set against [CLAIM-303](CLAIM-303.md)'s clause that recurrence is
  evidence of reuse, not the criterion. In [CLAIM-303](CLAIM-303.md)'s own terms the break-even
  rule needs no forecast and is worst-case optimal; [ADR-032](../decisions.d/ADR-032.md)'s second-occurrence
  rule is that rule when filing costs about one reconstruction. It does not
  reach staleness, which the theorem forbids rather than prices, or drifting
  costs, and where reuse can be forecast an expected-reuse rule can do better,
  so [CLAIM-303](CLAIM-303.md)'s criterion survives there.
objected_by:
- CLAIM-314
---
<!-- inactive-ok-file: CLAIM-303 CLAIM-185 — Proposed; the claim objected to, and an open claim cited as open -->

# CLAIM-308: Where reuse cannot be forecast, recurrence weighted by reconstruction cost is the filing criterion, not only evidence for one: filing at the first use at which reconstructing again would take the overpayment past the cost of filing is within 2 − (c_a + u)/c_r of the hindsight optimum on every sequence of uses, at most twice, and no deterministic rule without foresight guarantees materially better, under fixed known costs, with staleness left out and the cost of recognizing what a filed argument answers taken as fixed

## The claim

[CLAIM-303](CLAIM-303.md) prices filing as an upfront cost F against reconstruction c_r
per use, with access and verification c_a and upkeep u per use once
filed, and files when expected reuse n exceeds F/(c_r − c_a − u). Its
last clause keeps recurrence out of the criterion: recurrence is evidence
that reuse will come, and the criterion is the expected reuse itself.

That needs a forecast of n, and the record rarely has one. Without it,
the question becomes what rule does well whatever the sequence of uses
turns out to be. Karlin, Manasse, Rudolph and Sleator answer it for two
states with fixed prices ([THEORY-348](../theory.d/THEORY-348.md)): switch "when the cost of
making the change equals the extra cost incurred due to being in state A
instead of A'". Here state A is reconstructing each time, A' is having
filed, the extra cost of staying in A is c_r − c_a − u per use, and the
change costs F. The rule is to file at the use where the reconstruction
overpaid so far reaches F.

Write d = c_r − c_a − u for the overpayment per use and a = c_a + u.
The rule reconstructs k = ⌊F/d⌋ times and files at use k + 1. If reuse
stops by use k, it paid exactly what hindsight pays. If it stops at a
later use n, it paid kd + F + n·a against hindsight's F + n·a, since
(k + 1)d > F. The ratio is then at most 1 + kd/(F + (k + 1)a), which
kd ≤ F bounds by 1 + d/c_r = 2 − a/c_r. That is at most 2, and reaches 2
only as a/c_r goes to 0. No deterministic rule without foresight
guarantees better than this factor, up to a term that vanishes as F/d
grows: an adversary stops reuse at the use where the rule files. The
paper proves the bound of 2 for snoopy caching, whose filed state costs
nothing per use (a = 0). The extension to a per-use cost is the
record's, and it tightens the factor. Rounding matters: filing once the
overpayment so far has reached F can exceed 2 when F is not a multiple
of d.

So where reuse cannot be forecast, the past recurrences, each weighted
by what it cost to redo, are the criterion. The decision is a function
of them, and it carries a guarantee that no forecast-based rule can
carry when there is no forecast.

## What it gives the record

[ADR-032](../decisions.d/ADR-032.md)'s second-occurrence rule is the break-even rule when F is about
one reconstruction's overpayment. The rule should file sooner when
filing is cheap, later when filing is dear, and at once when filing
costs nearly nothing, as with setting a found brick aside
([CASE-094](../cases.d/CASE-094.md)). A11's "rare, expensive-to-reconstruct
argument" is filed by the break-even rule after its first expensive
reconstruction. The unweighted count is what fails, not recurrence as
such.

## What it does not say

- **That no rule at all does better.** The lower bound of 2 is for
  deterministic rules, as [THEORY-348](../theory.d/THEORY-348.md) states. A randomized rule, which
  files at a random point, is known to guarantee e/(e − 1) ≈ 1.58 in
  expectation for rent-or-buy (Karlin, Manasse, McGeoch and Owicki). The
  record does not hold that source. The deterministic bound of 2 is also
  approached only when filing costs many reconstructions' overpayment. When
  F is no more than one, filing at once is optimal.

- **Anything about staleness.** The theorem forbids stale reads rather
  than pricing them. [CLAIM-303](CLAIM-303.md)'s added term, that reusing an obsolete
  argument may cost more than recomputing it, is outside the result. A
  filed argument that can go wrong unnoticed is not the paper's two
  fixed-price states.
- **That the guarantee holds with drifting or unknown costs.** F, c_r,
  c_a and u are fixed and known in the proof. The record's reconstruction
  costs are estimates, and reconstruction gets cheaper as related
  arguments are filed.
- **That recognition costs a fixed amount per use.** CLAIM-314:
  certifying that stored answers cover a new question is NP-complete even
  for conjunctive queries, and its cost grows with what is stored. Where
  reuse is found by search, each filing raises the cost of using the
  others, and item-by-item decisions are not independent. The guarantee
  holds where a filed argument is reached by its code or index. Over the
  whole store it is not shown. Conceded.
- **That worst-case rules beat expected-value rules.** Where reuse can be
  forecast, a rule using the forecast can do better on average. There
  [CLAIM-303](CLAIM-303.md)'s criterion stands, and this objection narrows the clause
  instead of defeating it.
- **That it covers more than two options.** With a third, such as
  filing a pointer instead of the argument, the deterministic bound rises
  to 3 ([THEORY-348](../theory.d/THEORY-348.md)).
- **That the paper says this.** Its case is when to stop maintaining a
  copy. Reading it as when to file is the record's mirror-image use of
  the same principle ([NOTE-893](../notes.d/NOTE-893.md)).
- **Anything about [ADR-032](../decisions.d/ADR-032.md)'s other reason.** The second-occurrence rule
  is also a throttle on capture by agents, and this objection says
  nothing about that.

## How [CLAIM-303](CLAIM-303.md) could answer

It could restrict "the criterion" to the case where reuse is forecastable
and concede the clause elsewhere. Or it could hold that the record always
has some forecast, such as the line an argument belongs to or the
question it answers, so that the worst case is the wrong standard.
[CLAIM-185](CLAIM-185.md)'s threshold would then need to say which case the record is in.

## Note of 2026-10-30: what holds it back

The bound corrected in version 3 has not yet been re-derived by a second
reviewer. Promoting this objection makes its concession due on CLAIM-303,
which has not answered: it could restrict its last clause to reuse that
can be forecast, or hold that the record always has some forecast.
