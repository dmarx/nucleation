---
number: 308
status: Active
formerly:
- CLAIM-tmpc3sk7
title: 'Cost-weighted recurrence is the filing rule'
statement: >-
  Where reuse cannot be forecast, recurrence weighted by reconstruction cost
  is the filing criterion, not only evidence for one: filing at the first
  use at which reconstructing again would take the overpayment past the cost
  of filing is within 2 − (c_a + u)/c_r of the hindsight optimum on every
  sequence of uses, at most twice, and no deterministic rule without
  foresight guarantees materially better, under fixed known costs, with
  staleness left out and the cost of recognizing what a filed argument
  answers taken as fixed
version: 7
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
- version: 4
  date: '2026-11-10'
  note: >-
    Answers QUESTION-098, which asks what the second-occurrence rule
    approximates; the claim says recurrence weighted by
    reconstruction cost "is the filing criterion" and that the
    second-occurrence rule "is the break-even rule" when overpayment
    is per reconstruction. Found when the costs part was checked for
    a root question (2026-11-10). No other change.
- version: 5
  date: '2026-11-18'
  note: >-
    Promoted at the status review of 2026-11-18, at the status review's
    ruling (the owner delegated these rulings; ADR-057, ADR-065). The
    two waits of the note of 2026-10-30 are met. A second reviewer
    re-derived the bound step by step, upper and lower, and re-ran it
    with controls (scratch/formal/claim308_rent_or_buy_check.py; the
    note of 2026-11-18). CLAIM-303 writes in this objection at the same
    review, restricting its last clause to reuse that can be forecast
    (ADR-059). QUESTION-098 moves from answers to bears_on: the claim
    answers only the case without a forecast, with staleness left out,
    and the question asks about staleness too. The title is unchanged.
- version: 6
  date: '2026-11-18'
  note: >-
    Answers QUESTION-489, the part of QUESTION-098 split off
    under ADR-049 at the status review's ruling (the owner delegated
    these rulings): when a structure is worth filing, staleness set
    aside, under fixed known costs. It keeps bears_on QUESTION-098 for
    the open remainder.
- version: 7
  date: '2026-11-26'
  note: >-
    A dated note: the exchange 'Alignment consequences brainstorm' (ChatGPT,
    2026-11-26), A29 §7 (see the note). No other change.
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
answers:
- QUESTION-489
bears_on:
- QUESTION-098
---
<!-- inactive-ok-file: CLAIM-185 — Proposed; the claim objected to, and an open claim cited as open -->

# CLAIM-308: Cost-weighted recurrence is the filing rule

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
- **That recognition costs a fixed amount per use.** [CLAIM-314](CLAIM-314.md):
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
reviewer. Promoting this objection makes its concession due on [CLAIM-303](CLAIM-303.md),
which has not answered: it could restrict its last clause to reuse that
can be forecast, or hold that the record always has some forecast.

## Note of 2026-11-18: the bound re-derived by a second reviewer

Re-derived at the status review of 2026-11-18, from the setting above, with
d = c_r − a, a = c_a + u, k = ⌊F/d⌋, and hindsight paying min(n·c_r, F + n·a).

- **Upper bound.** If reuse stops at n ≤ k, then nd ≤ F, so n·c_r ≤ F + n·a
  and the rule pays what hindsight pays. If n ≥ k + 1, the rule pays
  k·c_r + F + (n − k)a = kd + F + n·a, and n·c_r ≥ (k + 1)d + n·a > F + n·a,
  so hindsight pays F + n·a. The ratio is 1 + kd/(F + n·a) ≤ 1 + kd/(F + (k + 1)a).
  That is at most 1 + d/c_r because k·c_r ≤ F + (k + 1)a reduces to kd ≤ F + a,
  which holds since kd ≤ F. So 1 + d/c_r = 2 − a/c_r.
- **Lower bound.** A rule that files at use m meets an adversary who stops
  at n = m. Write K = ⌊F/d⌋ ≥ 1. For m ≤ K, hindsight pays m·c_r. The ratio
  1 + (F + a − c_r)/(m·c_r) falls with m, so it is least at m = K, where it is
  at least (2 − a/c_r) − d/(K·c_r). For m ≥ K + 1, hindsight pays F + m·a. The
  ratio rises with m, since its derivative has the sign of (c_r − a)(F + a) > 0.
  At m = K + 1 it is 1 + Kd/(F + (K + 1)a) > (2 − a/c_r) − d/((K + 1)c_r),
  because F < (K + 1)d. Either way the shortfall is under d/(K·c_r) < 1/K,
  which vanishes as F/d grows, as the claim says.
- **Rounding.** Filing at m = ⌈F/d⌉ + 1, once the overpayment has reached F,
  is the control. With a = 0 and F not a multiple of d it exceeds 2.

scratch/formal/claim308_rent_or_buy_check.py checks the three steps exactly,
over rationals, on 20,000 random instances. Its two controls must fail the
bound, and both do: the reached-F rounding, and filing at once when F is
many overpayments. The break-even rule never exceeds 2 − a/c_r. No filing
use beats (2 − a/c_r) − 1/K against the adversary, and the break-even rule's
gap to the bound at n = k + 1 is O(1/K).

## Note of 2026-11-26: the exchange "Alignment consequences brainstorm" (ChatGPT, U16–A29), the rule moved to availability
<!-- inactive-ok-file: CLAIM-1403 — Proposed; filed from the same exchange on 2026-11-26 -->

A29 §7 cites this claim correctly, as "an active formal result resembling the classical online rent-or-buy problem" under which filing once repeated reconstruction would exceed the cost of filing "provides a competitive bound against an optimal policy with hindsight", and draws from it "a family of retention policies based on the work that memory saves". Its example: an entry used 20 times at 1 unit of reconstruction each against one used twice at 100, so 20 against 200 units saved: "Frequency alone would favor A. A reconstruction-cost-sensitive policy might favor B." The arithmetic checks. The transfer is to availability, not filing ([CLAIM-1403](CLAIM-1403.md)), and the bound does not transfer with it: this claim's guarantee is for a one-way decision under fixed known costs, and a tier can be changed back, which is the setting of paging and caching, whose competitive bounds are of a different form. An application; the bound is not claimed for tiers. The note is the assistant's (Claude, in this session). No status change.
