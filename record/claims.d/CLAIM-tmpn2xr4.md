---
status: Active
title: 'Matched ordinary trajectories can conceal differences in an interpretation''s efficacy, in the allocation of that efficacy, and in the maintenance of its enabling constraints: in two finite constructions, systems that agree under ordinary operation differ in each, and a specified intervention exposes the difference that passive observation of the matched trajectories does not'
version: 3
history:
- version: 2
  date: '2026-10-22'
  note: >-
    Narrowed after the owner relayed a review of 2026-10-22. The
    constructions show that matched ordinary trajectories can conceal
    differences in efficacy, allocation and maintenance, and that the
    specified interventions expose them. They are not a general independence
    theorem for the four properties. Nor is intervention the only way to tell
    the systems apart: knowing their mechanisms would. What fails is the
    matched passive observation. Status and warrant are unchanged.
- version: 3
  date: '2026-10-22'
  note: >-
    Note of 2026-10-22 added, from the readings of that day: an empirical
    parallel in a language model, and two criteria the claim bears on. The
    claim is unchanged.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in either construction of CASE-tmp60jh6: a pair of its systems
  that differ under ordinary operation, or that respond alike to the
  stated intervention. The claim says only that matched passive
  observation can fail to identify these differences in the systems
  constructed. It is not a general independence theorem, is not defeated
  by a model class in which some of the properties coincide, and it does not say any of them bears on experience.
tags:
- mathematics
- individuation
- consciousness
date: '2026-10-22'
line:
- evidence-for-experience
- formal-apparatus
grounds:
- CASE-tmp60jh6
complements:
- CLAIM-407
- CLAIM-194
uses:
- TERM-070
- TERM-tmpgqmop
summary: >-
  A10 of the exchange on experience and interpretation, re-run here.
  Three one-bit systems behave alike when the interpretation is 0. Under
  an intervention that sets it to 1, the first never acts on it, the
  second acts at once, and the third acts one step late, because its own
  interpretation opens the gate. Two two-constraint systems have the same
  trajectory, (1,1) throughout. A single perturbation runs one into (0,0)
  and leaves the other restored to (1,1): one maintains its constraints
  by [CLAIM-395](CLAIM-395.md)'s minimal slow–fast closure, the other is reset from
  outside. These are [CLAIM-407](CLAIM-407.md)'s lesson about governance and [CLAIM-194](CLAIM-194.md)'s
  about boundaries, applied to interpretation.
illustrated_by:
- CASE-tmp60jh6
---
<!-- inactive-ok-file: TERM-tmpe36gg TERM-tmpgqmop — Proposed; the terms and claims filed with this one from the same exchange, cited as open, nothing here rests on their adoption -->

# CLAIM-tmpn2xr4: Matched ordinary trajectories can conceal differences in an interpretation's efficacy, in the allocation of that efficacy, and in the maintenance of its enabling constraints: in two finite constructions, systems that agree under ordinary operation differ in each, and a specified intervention exposes the difference that passive observation of the matched trajectories does not

## The claim

A10 proposed "four progressively stronger properties": representation,
efficacy, endogenous allocation and constitutive maintenance. "These are
not four degrees of consciousness. They are different organizational
facts, each requiring different evidence." It built two constructions to
show that they come apart. "Interpretation" here is [TERM-tmpgqmop](../terms.d/TERM-tmpgqmop.md)'s, and
maintenance is closure of constraints in [TERM-070](../terms.d/TERM-070.md)'s sense. Both
constructions are [CASE-tmp60jh6](../cases.d/CASE-tmp60jh6.md), re-run here by script.
Its tables are reproduced exactly.

1. **Efficacy and allocation.** Systems R (Y = 0), X (Y = J) and E
   (Y = A·J, A' = J, A₀ = 0) give Y = 0, 0 when J = 0. Under do(J₀ = J₁ = 1)
   they give 0, 0; 1, 1; and 0, 1. "Ordinary behavioral equivalence does not
   determine whether an interpretation is causally effective, nor whether
   its efficacy is allocated endogenously."
2. **Maintenance.** In the closed system each constraint takes part in
   producing the other, C₁ on even steps from C₂ and C₂ every step from C₁.
   The second system is reset to (1, 1) from outside. Both stay at (1, 1).
   After C₂ is set to 0 at t = 0, the first goes (0, 1), then (0, 0) for
   good, and the second returns to (1, 1). "The causal organization of
   maintenance can differ even when the maintained states and ordinary
   behavior are identical."

The second system pair is the smallest closure [CLAIM-395](CLAIM-395.md) allows: two
constraints, one slow dependence (C₁ is conserved for two steps and made
from C₂, which acts for one) and one fast. A10 did not cite [CLAIM-395](CLAIM-395.md), but
its construction meets that claim's conditions (A) and (B).

## Where it sits in the record

- [CLAIM-407](CLAIM-407.md) shows that a description exactly closed under ordinary dynamics
  can lose a system's response to an intervention on its mechanism, as in
  the hidden governance bit ([CASE-125](../cases.d/CASE-125.md)). Part 1 is the same lesson for an
  interpretation's authority, and part 2 for its maintenance.
- [CLAIM-194](CLAIM-194.md) holds that a gap or coupling criterion cannot tell a boundary
  a system produces from one imposed on it. Part 2 shows that a
  perturbation can tell produced maintenance from imposed maintenance where
  the ordinary trajectory cannot. It complements [CLAIM-194](CLAIM-194.md) and does not
  answer it in general. [CLAIM-194](CLAIM-194.md) is about boundaries read from
  observational statistics, and part 2 needs the intervention.
- [TERM-067](../terms.d/TERM-067.md)'s governance-response profile is the tool for describing part
  1. A9 kept [TERM-067](../terms.d/TERM-067.md)'s own warning, that a response profile "would not
  automatically be a judgment about self-governance".

## What it does not say

- Not that the four properties are logically independent pairwise or in
  general. Two constructions exhibit specific separations: efficacy and
  allocation in construction 1, maintenance in construction 2. They are
  existence results for those cases, not an independence theorem.
- Not that only an intervention can tell the systems apart. Knowing their
  mechanisms tells them apart at once. The point is that the matched
  passive observations do not, and that a specified intervention does.

- Not that any of the four facts is a mark of experience, or of a
  perspective. A10: "It does not establish agency, perspectival unity, or
  consciousness." A11 then denied that maintenance (part 2) is necessary
  for a perspective at all ([TERM-tmpe36gg](../terms.d/TERM-tmpe36gg.md)).
- Not that Boolean update rules are constraints in Montévil and Mossio's
  sense. A10: "Boolean transition equations by themselves do not
  demonstrate that a biological or organizational system possesses genuine
  constraint-producing mechanisms." The production relation is stipulated.
- Not that the four are ordered by implication. A10: "These arrows indicate
  increasingly demanding explanatory claims, not logical implications."
  Maintenance without rich representation is possible.

## Note of 2026-10-22: an empirical parallel, and two criteria

- **A parallel in a trained model.** In Gurnee et al. (NOTE-tmpyc06q) the
  language of a passage is represented in all four tasks but is effective
  in only two, and only an activation swap tells them apart. That is the
  claim's first separation, efficacy against representation, found in a
  real system and not constructed. It is an intervention result, not
  passive observation.
- **Criteria that behaviour cannot settle.** Whyte et al.'s criterion of
  consciousness (THEORY-tmpw20ca) is a capacity to affect choice, and
  Laukkonen et al.'s "epistemic depth" (THEORY-tmpw19hw) is precision
  allocated from within. By this claim, matched behaviour can hide both,
  so behavioural tests for them, as Laukkonen et al. propose for AI, need
  an intervention.
- Bo et al. (NOTE-tmphhgp9) show where an appraisal is represented and
  where it changes affect, but by correlational imaging. It is a loose
  parallel, not an instance.
