---
status: Proposed
title: "Where a party's fallback is valued by what it could produce alone from a capacity learned by doing that needs capacity already present to grow, and its terms are bargained by a rule under which a more valuable fallback gets more, supply that does the party's own work lowers the terms it can obtain at any renegotiation while it never exits and no price, rule or exit changes; ending the supply restores them, asymptotically, if it ends before the capacity's deadline and not after; supply that covers only what the party cannot yet do leaves the capacity, and so the terms, as they would be with no supply; and where the party cannot exit, the fallback does not enter the terms"
version: 2
history:
- version: 2
  date: '2026-11-25'
  note: >-
    Revised on the review of the manuscript governance-of-becoming, Part
    III (2026-11-25, Part B, J9.1), whose joins reader found the claim
    right in substance and named five corrections, all applied. The title
    and summary say "no price, rule or exit changes", not "no term
    rewritten": the split is the terms and is re-solved at each t, so the
    model assumes renegotiation. The capacity-first clause is restated:
    in CLAIM-605's model capacity-first supply is the unsupported
    dynamics, so there is no decay for it to stop, and a party below the
    threshold decays and loses terms anyway. The body now gives the
    derivation, and the script is its check. The defeater names the
    premise (a valuation nondecreasing in the stand-alone output path)
    instead of a clause that could not be met. "Under both of
    LEAD-tmpeo8wq's readings" is narrowed to what holds under which. Added
    to the limits: J9.2's residue (the Nash arm never gives terms P could
    earlier have refused), that the capacity is P's self-supply, and that
    CASE-264 is a fictional thought-experiment. The summary's "the script
    asserts its figures" is corrected (Part A, 2.17). Standing records the
    review's independent recheck. No change of status.
role: thesis
warrant: demonstrated
defeated_if: >-
  A step of the derivation in the body that fails in CLAIM-605's model
  with the symmetric Nash split: in particular, stand-alone paths from
  ordered capacities that cross, so that the stand-alone output is not
  nondecreasing in the capacity it starts from; or an error in
  scratch/manuscripts/governance-of-becoming/analysis/fallback_decay_bargaining.py
  whose correction, at the parameters run, leaves the party's Nash share
  unchanged under full substitutive supply, lets supply ended after
  CLAIM-605's deadline restore the fallback, or moves the share under
  capacity-first supply from above the threshold or with no exit. Or a
  showing that the fallback of a party in CLAIM-605's model is properly
  valued by a valuation that is not nondecreasing in its stand-alone
  output path, so that the decay need not lower it. Not defeated by
  parameters under which the fall is gradual rather than a step at the
  deadline, which the claim does not assert; nor by the absence of a
  measured case, since the claim is about the model.
tags:
- game-theory
- society-and-governance
- complex-systems
date: '2026-11-25'
line:
- dependence-and-domination
- transient-support
rests_on:
- CLAIM-605
grounds:
- CASE-264
complements:
- CLAIM-tmp2jhc1
- CLAIM-670
summary: >-
  The assistant's derivation and computation for the manuscript
  governance-of-becoming, Article 9 §9.4 (gap G9.1, join J9.1), filed under
  write-manuscript step 6 and revised on the review of Part III. The
  record held a capacity that decays under substitutive supply (CLAIM-605)
  and a Nash split that moves with an outside option set by hand (CASE-264's
  arm A, a fictional thought-experiment; CLAIM-tmp2jhc1, whose A24 §4 model
  already lowers the terms with the fallback as comparative statics). Here
  P's outside option is valued from its decaying capacity, and the split is
  re-solved at each t, which assumes renegotiation. Over six time units of
  full substitution P's share falls from 6.000 to 4.199 with no exit and no
  price, rule or exit changed; supply ended before the deadline restores the
  fallback toward 4, and after it leaves it at 0.041 or 0.003. Capacity-first
  supply is the unsupported dynamics, so it leaves the terms where they would
  be without supply; with no exit the fallback does not enter the terms. A
  five-step derivation gives the qualitative clauses; the script, run with
  python3 -I, asserts the components and the shape of the results, and its
  other figures are reproduced by comparing its output with the dated
  output. For a scalar capacity it answers yes, on the first of
  LEAD-tmpeo8wq's two readings only, the item that lead left open. The
  review of Part III rechecked it from separate code. The wording is the
  assistant's (Claude, in this session); adopting it is the owner's call.
---

<!-- inactive-ok-file: CASE-264 CLAIM-tmp2jhc1 CLAIM-670 CLAIM-690 TERM-123 TERM-124 — Proposed or new; the bargaining case, the claims this complements, and the terms a verdict of exploitation or domination would need, cited with their standing -->
<!-- inactive-ok-file: SYNTHESIS-032 CASE-367 CLAIM-954 CASE-362 CLAIM-946 — Proposed; the account that declines a neighbouring join, and two executed studies with their claims, cited for contrast -->

# CLAIM-tmp6nzs1: Where a party's fallback is valued by what it could produce alone from a capacity learned by doing that needs capacity already present to grow, and its terms are bargained by a rule under which a more valuable fallback gets more, supply that does the party's own work lowers the terms it can obtain at any renegotiation while it never exits and no price, rule or exit changes; ending the supply restores them, asymptotically, if it ends before the capacity's deadline and not after; supply that covers only what the party cannot yet do leaves the capacity, and so the terms, as they would be with no supply; and where the party cannot exit, the fallback does not enter the terms

## The gap it fills

CLAIM-605 (Active, demonstrated) holds capacity learned by doing,
dC/dt = λPC(1 − C) − μC, under substitutive support P = min(τC, 1 − A)
or capacity-first support P = min(τC, 1), with a deadline after which
withdrawal no longer restores capacity. CASE-264's arm A and
CLAIM-tmp2jhc1 hold the symmetric Nash split, u_P = o_P + (S − o_P − o_R)/2,
in which each unit of outside option moves half a unit of the split
whether or not it is used. In both, the outside option is a number set
by hand. That the terms fall as an arrangement erodes a party's fallback
is held already, as comparative statics: CLAIM-tmp2jhc1's A24 §4 model
(specialization "lowering B's independent capacity", the split 14.75 to
11.25), CLAIM-670's note ("As B's relationship-specific investment lowers
o_B …") and CLAIM-675. What no entry held is the decay in time and its
deadline carried into the terms: the manuscript's digest searched by
mechanism and found the joint dynamics "not done", and no account
declines the join (SYNTHESIS-032's "funding loop with a deadline" needs
learning from drills, a premise this claim does not use). LEAD-tmpeo8wq,
in its first note of 2026-11-24, keeps open "whether solo reach's
shrinkage, not a price, moves the terms the other can offer".

## The derivation

The review of Part III (2026-11-25, Part B, J9.1) gave it; it does not
depend on the script.

1. Under full substitution, P = min(τC, 0) = 0, so C(t) = 0.7e^(−0.3t),
   strictly decreasing (CLAIM-605).
2. With supply removed, dC/dt = f(C) = λ min(τC, 1)C(1 − C) − μC is
   scalar and autonomous, and f is Lipschitz. Solutions from ordered
   starts stay ordered (the comparison principle), so P's stand-alone
   output path min(τC_s, 1) is pointwise nondecreasing in the capacity it
   starts from. Any valuation of the fallback that is nondecreasing in the
   output path therefore makes o_P nondecreasing in C(t). The two used
   here, the forward value and current output, both qualify.
3. P's Nash share u_P = (S − o_R + o_P)/2 is increasing in o_P, and so is
   its take-it-or-leave-it share u_P = o_P. So P's terms are
   nonincreasing in t while it never exits. The split is re-solved
   against the current fallback at each t, so the terms move by
   renegotiation; what stays fixed is every price, the bargaining rule and
   P's choice to stay.
4. Once supply ends, o_P depends only on the capacity C(T) at its end. If
   C(T) > C_L = 0.2764, that is T < 3.098, then C → 0.7 and o_P → w. If
   C(T) < C_L, then C → 0 and o_P → the value of zero output, 0. So the
   terms are restorable, asymptotically, exactly when the supply ends
   before the deadline.
5. Without exit (CASE-264's arm B), o_P does not enter u_P.

Steps 2 to 4 are the claim's own content; steps 1 and 5 and the half-unit
rate are held. Capacity-first supply, P = min(τC, 1), is the unsupported
dynamics f itself, so it has no decay to stop: from the kept state it
leaves the capacity and the terms as they would be without supply, and a
party below the threshold decays under it anyway ("cannot lift a party
already below the threshold", CLAIM-605), and its terms fall.

## The computation, a check

The script is
`scratch/manuscripts/governance-of-becoming/analysis/fallback_decay_bargaining.py`,
with its README beside it; its output of 2026-11-25 is
`analysis/fallback_decay_bargaining.2026-11-25.txt`. Run with
`python3 -I`; deterministic. It asserts the components (the threshold,
kept state and deadline, CASE-264's and CLAIM-tmp2jhc1's splits), the
half-unit property, the steepest fall at the deadline for r ≤ 0.25 with a
single crossing, restoration exactly before the deadline, and the
controls' shapes. Its other figures, the table's values among them, are
not asserted: a run that prints "checks pass" reproduces them only when
its output is compared with the dated output, which it matches byte for
byte.

- **Capacity**: CLAIM-605's model and parameters, λ = 1, μ = 0.3,
  τ = 1.5. The capacity is P's self-supply, its ability to meet its own
  demand alone, distinct from its contribution to the joint value S, which
  is why S and o_R are held fixed. If R is the supplier and supplying also
  raised o_R, the fall would be larger.
- **Bargain**: CASE-264's arm A, S = 10, o_R = 2. The script recovers
  CASE-264's 4 and 6 at o_P = 0 and CLAIM-tmp2jhc1's 8, 9 and 10.
- **Fallback**: o_P(t) is w times the annuitized, discounted value of P's
  stand-alone output min(τC_s, 1), with C_s following the unsupported
  dynamics from C(t). Added, and invented: w = 4, r = 0.25 and a horizon
  of 80, fixed before the run. A second valuation, current output only,
  w·min(τC, 1), is reported beside it.

| t | C(t) | o_P, forward | u_P | o_P, current output | u_P on it |
|---|---|---|---|---|---|
| 0 | 0.700 | 4.000 | 6.000 | 4.000 | 6.000 |
| 2.0 | 0.384 | 2.954 | 5.477 | 2.305 | 5.153 |
| 3.0 | 0.285 | 1.817 | 4.908 | 1.708 | 4.854 |
| 4.0 | 0.211 | 0.942 | 4.471 | 1.265 | 4.633 |
| 6.0 | 0.116 | 0.399 | 4.199 | 0.694 | 4.347 |

1. **The terms move with no exit and no price, rule or exit changed.**
   P's share never rises and falls 6.000 to 4.199 by t = 6; each unit of
   fallback lost moves half a unit to R, checked at every step.
2. **Restorable before the deadline, not after.** Supply ended at
   T = 2.0 or 3.0, then 20 units unsupported: o_P = 4.000 and 3.916.
   Ended at T = 3.5 or 5.0: o_P = 0.041 and 0.003, P's share near 4.
3. **Controls.** Capacity-first supply from the kept state: the share
   stays 6.000, as with no supply. Partial substitution at A = 0.5, below
   CLAIM-605's a* = 0.585: capacity settles at 0.400 and the share at
   5.535, no cliff. CASE-264's arm B (no exit): P gets 1 whatever its
   fallback is worth, by construction. CLAIM-602's model, without a
   threshold, run through the same pipeline: a smooth fall to 5.547,
   largest fall per 0.05 of 0.005 against 0.042. Take-it-or-leave-it with
   exit (3e): u_P = o_P, 4.000 to 0.399.

## Which reading of LEAD-tmpeo8wq it answers

LEAD-tmpeo8wq's second note of 2026-11-24 gives two readings of whether
a decline of this kind counts as "no change in any single transition's
cost". They are classifications, not valuations, and the two valuations
here do not map onto them: both are functions of P's capacity.

- **On the first reading** (capacity is the actor's state, and transition
  costs are fixed functions of it), no price changes, and the terms move
  on either valuation (to 4.199 forward, to 4.347 on current output). The
  lead's item, "whether solo reach's shrinkage, not a price, moves the
  terms", is answered yes, for a scalar capacity. The deadline shows in
  the terms on the forward valuation only; the current-output fall is
  steepest at t = 0.225.
- **On the second reading** (what it costs P to reach a configuration
  includes rebuilding the capacity), the same decline is a rise in P's
  incoming costs and the lead's null applies. The computation still shows
  the terms moving, but by what the lead counts as a price, so it does not
  answer the item yes. The forward valuation is not this reading: it
  counts the capacity's natural recovery from C(t), not a cost of
  rebuilding it.

Version 1 said the claim answers the item "under both of its readings";
that overstated it.

## What it does not say

- **Not terms P could earlier have refused.** In the Nash arm
  u_P = (10 − 2 + o_P)/2 = 4 + o_P/2 ≥ 4 = o_P(0): P's share never falls
  below what it could get alone at t = 0 (at t = 6, 4.199 against 4.000),
  so P never gets terms it could earlier have refused, CLAIM-670's title.
  What the Nash arm models is the falling floor, CLAIM-670's note's "what
  they can afford to refuse has changed". Terms P could earlier have
  refused appear only in the take-it-or-leave-it control (3e:
  u_P = o_P(t) < o_P(0)), or in the Nash arm for w > (S − o_R)/2 = 4; at
  w = 4 the parameters sit on that boundary (the review of Part III,
  Part B, J9.2).
- **Not a step at the deadline in general.** The steepest fall is in the
  interval centred at t = 3.075, against the deadline 3.098, for
  r ≤ 0.25; at r = 0.5 it moves to t = 2.275. Within half a unit of the
  deadline lies 85 % of the fall by t = 6 at r = 0.02 and 33 % at 0.25.
  The assistant's expectation, stated before the run, was a step at the
  deadline: it holds for where the fall is steepest and fails as a step
  except for a patient party.
- **Not the world's numbers.** Every parameter is CLAIM-605's, CASE-264's,
  or invented here (w, r, the horizon).
- **Not intent or gain.** Supply is exogenous. R's cost of supplying,
  and so whether R would choose to supply past the deadline, is not
  modelled.
- **Not exploitation or domination.** No standard is declared, as
  TERM-123 and TERM-124 require; CLAIM-670's step to exploitation stays
  interpretive. What is shown is a bargaining vulnerability produced by
  supply. That exit is what lets the decay matter at all is CLAIM-690's
  point, which the no-exit control shows in the dynamic case.
- **Not reach over TERM-114**, the authority index or the four
  predicates LEAD-tmpeo8wq asks for: a scalar capacity and a scalar
  split.

## Its ground

CASE-264 is a fictional thought-experiment (`standing: fictional`): two
workshops in "a toy bargaining model", "Fictional, to hold fixed what no
real case does". It supplies the bargaining arm's form and its numbers (S = 10,
o_R = 2, the arm without exit), not evidence. The claim's warrant is the
derivation above from CLAIM-605 and the Nash split; the script checks it
at one set of parameters. The executed computation has no CASE of its
own (the review of Part III, Part C, Region 4, flags this). The
assistant's judgement is that none is needed: the computation checks a
derivation rather than being the evidence, the role CASE-367 has for
CLAIM-954 and CASE-362 for CLAIM-946, and its script, README and dated
output are kept once under analysis/. If the owner wants the run held as
a record entry, an executed-study CASE is the form.

## Standing

Proposed. Run by its filer on 2026-11-25, then rechecked independently by
the joins reader of the review of Part III (2026-11-25, Part B), who
wrote a separate check from the claim's stated model, not from the script
(`scratch/manuscripts/governance-of-becoming/review-III-B-indep-check.py`:
RK4 at step 1e-3 with trapezoid quadrature). It reproduces to three
decimals the threshold 0.2764, the deadline 3.0975 and a* = 0.5854; o_P
and u_P at t = 0, 2, 3, 4 and 6 on both valuations; the four restoration
values (4.000, 3.917, 0.041, 0.0035; the script prints 3.916 and
0.003); and the steepest interval at t = 3.075. On a grid,
o_P is nondecreasing in C. The reader also gave the derivation above.
That is the second-session check this section asked for before any
promotion; promotion is the owner's call. A candidate member of
governance-of-becoming under ADR-104's rule (it is stated in §9.4);
adding it is the owner's call.
