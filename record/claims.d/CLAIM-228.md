---
number: 228
status: Proposed
formerly:
- CLAIM-tmpeqvy4
title: 'Observational fidelity, as D_obs measures it, is a property of a rendering procedure over a class of source items, tested by one kernel family fitted on some items and scored on others, with the target term the readers'' response averaged over the procedure''s output; one source–target pair does not identify it, and a single rendering is judged as a sample of its procedure or by another measure'
version: 3
history:
- version: 2
  date: '2026-10-10'
  note: >-
    Restated on 2026-10-10 after CLAIM-200 (A240's second
    refinement): the title said more than the body. Version 1's title
    ended: 'for a single rendering of a single item it is not defined'.
    The body already said 'It does not say a single translation cannot
    be judged, only that this measure does not judge it.' The
    derivation, the defeat condition and the body are unchanged.
- version: 3
  date: '2026-10-19'
  note: >-
    Split at the owner's direction, carrying out the promotion audit's
    decision (record/promotion-audit/decisions/CLAIM-228.yaml, batch 014,
    ADR-047). Its derivations (the across-items exclusion of constant
    kernels, exact fit as a garbling, and deficiency as a finite
    linear programme) are now CLAIM-381, demonstrated and Active.
    This claim rests on it. What it keeps is the proposal that
    fidelity so restated is informative, and its defeat condition is
    a study (CASE-055). So its warrant is corrected from demonstrated to
    empirical (ADR-043). The title, body and defeat condition are
    unchanged, and the status stays Proposed.
role: thesis
warrant: empirical
defeated_if: >-
  In the discriminating study (CASE-055), held-out observational
  distortion, with one kernel family fixed across a class of items, does
  not separate rendering procedures that the named receivers'
  task-indexed recovery separates, so that fixing the family across items
  still leaves the measure uninformative.
tags:
- probabilistic-modeling
- mathematical-statistics
- translation
date: '2026-10-10'
line: pragmatic-transport
rests_on:
- CLAIM-011
- CLAIM-381
grounds:
- THEORY-156
complements:
- CLAIM-005
uses:
- TERM-021
- TERM-043
summary: >-
  The record's repair, on 2026-10-10, of the manuscript's L_obs and the
  profile's D_obs after [CLAIM-207](CLAIM-207.md), [CLAIM-230](CLAIM-230.md) and [CLAIM-235](CLAIM-235.md).
  For one pair a constant kernel makes D_obs zero ([CLAIM-207](CLAIM-207.md)); fixed
  across items, it fits only if the target readers' responses do not vary
  with the item. The repair ties the outcome-level kernels to the text
  channel, makes the transport a property of a procedure
  ([CLAIM-230](CLAIM-230.md)), and makes deficiency a finite computation over
  judgement outcomes ([CLAIM-235](CLAIM-235.md)). A proposal: the derivation is
  elementary, but whether the restated measure is informative is the
  defeat condition's empirical question. It does not say a fitted kernel
  is the translator's process.
objected_by:
- CLAIM-200
---
<!-- ref::uses-file: TERM-021 — applied unnamed: the D_obs this claim restates is context-indexed distribution matching -->
<!-- ref::uses-file: TERM-043 — applied unnamed: D_obs is the computable component of the profile of directed distortions -->
<!-- inactive-ok-file: CLAIM-005 — Proposed; open, and cited as the claim whose measure this restates -->
<!-- inactive-ok-file: THEORY-156 — Proposed; cited as the reading of Blackwell's order the exact-fit condition becomes, not as settled -->
<!-- inactive-ok-file: CLAIM-258 — Proposed; open, cited for its point that Blackwell's order needs a common parameter -->

# CLAIM-228: Observational fidelity, as D_obs measures it, is a property of a rendering procedure over a class of source items, tested by one kernel family fitted on some items and scored on others, with the target term the readers' response averaged over the procedure's output; one source–target pair does not identify it, and a single rendering is judged as a sample of its procedure or by another measure

## What it answers

This is the record's reply of 2026-10-10 to three objections from its
audit of the line. [CLAIM-207](CLAIM-207.md) (granted, and right) showed that for one
source–target pair a constant kernel K_C ≡ e′_τ(C) makes every term of
L_obs zero and satisfies naturality, and that the kernels act on judgement
outcomes while a translation acts on texts. [CLAIM-230](CLAIM-230.md) (right) showed
that Blackwell's order orders procedures, not single renderings.
[CLAIM-235](CLAIM-235.md) (right) showed that deficiency over text-valued renderings
has no estimator. The reply repairs the measure; it does not dispute the
objections. Its derivation is elementary and checkable. Whether the
repaired measure tells procedures apart is empirical, so the claim is a
proposal.

## The claim

**The objects.** Let 𝒰 be a class of source items u, finite in any design.
In context C, source readers respond to u with the distribution
e^o_C(· | u) on the context's judgement outcomes. A rendering procedure is a
channel on texts, T(v | u). Target readers respond to a rendering v, in the
corresponding context τ(C), with e^t_τ(C)(· | v). The target term for item u
is the readers' response averaged over what the procedure produces from it:

ē^t_τ(C)(· | u) = Σ_v T(v | u) e^t_τ(C)(· | v).

This relates the two levels that [TERM-008](../terms.d/TERM-008.md) says "are never formally
related": the text channel enters through the average, and the comparison
stays on judgement outcomes.

**The fidelity condition.** One kernel family {K_C}, the same for every
u ∈ 𝒰, with

ē^t_τ(C)(· | u) ≈ (K_C)# e^o_C(· | u) for every u.

**The score.** Fit the family on held-in items and score it on held-out
ones:

D_obs(T; 𝒰) = average over held-out u of Σ_C w_C d_C((K_C)# e^o_C(· | u), ē^t_τ(C)(· | u)).

That is [CLAIM-011](CLAIM-011.md)'s remedy, "estimated on one collection of tasks and
evaluated on another", applied to the outcome kernels.

**The constant kernel is excluded when the target varies with the item.**
If K_C(· | s) = q for every source outcome s, then (K_C)# e = q for every
distribution e. So the condition holds for every u only if
ē^t_τ(C)(· | u) = q for every u: the target readers' averaged responses
carry no information about which item they were given. Whenever they do
carry such information, [CLAIM-207](CLAIM-207.md)'s construction fails the condition.
On held-out items it pays the distance between q and each item's actual
target response.

**Exact fit is a garbling.** If ē^t_τ(C)(· | u) = (K_C)# e^o_C(· | u) for
every u, then, read as experiments about the item, u ↦ ē^t_τ(C)(· | u) is
the kernel K_C applied to u ↦ e^o_C(· | u). That is a garbling in the sense
of [THEORY-156](../theory.d/THEORY-156.md), with the item as the common parameter. [CLAIM-207](CLAIM-207.md) says
so too. The parameter is common because both families are indexed by the
same source items, which is the condition [CLAIM-258](CLAIM-258.md) asks for.

**Deficiency becomes computable.** The outcome spaces are the judgement
categories, which are finite, and a design has finitely many items. So the
experiments compared, u ↦ e^o_C(· | u) and u ↦ ē^t_τ(C)(· | u), are finite
tables, and the space of texts never enters. Le Cam's deficiency between
them, the least over Markov kernels M between the two finite outcome sets
of the largest over u of the total-variation distance between M# e^o_C(· | u)
and ē^t_τ(C)(· | u), is one linear programme. Minimise t over the entries
of M, slack variables s_(u,y) and t, subject to: M is stochastic (its
entries are nonnegative and each row sums to 1); for each u and each
target outcome y, s_(u,y) ≥ (M# e^o_C(· | u))(y) − ē^t_τ(C)(y | u) and
s_(u,y) ≥ ē^t_τ(C)(y | u) − (M# e^o_C(· | u))(y); and for each u,
½ Σ_y s_(u,y) ≤ t. Every constraint is linear in the unknowns, because
M# e^o_C(· | u) is linear in M. For a finite family Q of decision problems
with finite action sets, the Q-restricted form is a finite computation
too. For each problem, the inner minimisation over rules on the source
outcomes is a linear programme, and the outer maximisation over rules on
the target outcomes is of a convex function, so it is attained at a
deterministic rule, of which there are finitely many. The tables are
estimated from finite samples of readers, so the value carries sampling
error, which resampling items and readers estimates. The plug-in bias that
[CLAIM-235](CLAIM-235.md) shows for signalling applies here as well, so the number of
readers per item matters.

**Single renderings.** One rendering of one item is one draw from T at one
u. Its "fidelity" would be the per-item term, which [CLAIM-207](CLAIM-207.md) shows
can be made zero by the kernel. So it is not defined as a measure. A
single rendering such as Henley's Villon ([CASE-010](../cases.d/CASE-010.md)) is judged as a sample
of the procedure that produced it, or by another measure stated as such,
as [CLAIM-230](CLAIM-230.md) says: "For single renderings, a different measure,
stated as such."

## What it does not say

- It does not say a fitted K_C is the translator's process. It is a
  correspondence between response categories, fitted to a procedure's
  effect.
- It does not say the measure succeeds. That is the defeat condition.
- It does not say a single translation cannot be judged, only that this
  measure does not judge it.
- It does not settle where the contexts and their correspondence τ come
  from ([QUESTION-005](../questions.d/QUESTION-005.md)), nor that the contexts are fine enough to see the
  pairing of items with renderings ([CLAIM-005](CLAIM-005.md)'s note of 2026-10-10).

## Note of 2026-10-19: the derivations, split off

The three derivations in "The claim", the constant-kernel exclusion, exact
fit as a garbling and the finite deficiency computation, are now
[CLAIM-381](CLAIM-381.md), demonstrated and Active. This claim keeps the proposal and
its empirical test.
