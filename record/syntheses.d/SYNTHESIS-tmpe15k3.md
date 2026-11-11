---
status: Proposed
title: 'Agreement in ordinary operation does not fix how a system responds to an intervention on its mechanism: a coarse-graining exactly closed under its ordinary dynamics can lose that response, a deficiency of sufficiency measures the loss and cannot rise under refinement while closure is ordered by refinement in neither direction, causal abstraction does not secure the sufficiency, matched trajectories can hide efficacy and maintenance, and fidelity in ordinary operation certifies nothing about viability; where maintenance is realized is shown only by intervening on the production mechanisms relative to a boundary no intervention supplies, interventions show that a capacity is produced through a mechanism and not that it consists in it, and closure needs at least two constraints as persistence needs a productive cycle'
version: 1
defeated_if: >-
  A component misstated or misattributed here; an in-force component of
  the intervention-and-sufficiency part of the formal-apparatus line left
  out without a reason given; or a link this account states that no
  component states. Its standing is its components': a component retired
  or demoted takes its clause with it, and nothing here holds the clause
  up.
tags:
- causality
- information-theory
- philosophy-of-science
date: '2026-11-11'
line:
- formal-apparatus
integrates:
- CLAIM-407
- CASE-164
- CLAIM-399
- CLAIM-409
- CLAIM-387
- CLAIM-392
- TERM-068
- TERM-062
- CLAIM-414
- CLAIM-517
- CLAIM-540
- CLAIM-536
- CLAIM-522
- ARG-050
- CLAIM-530
- CLAIM-528
- CLAIM-480
- CLAIM-515
- CLAIM-395
- CLAIM-516
summary: >-
  A part account of the formal-apparatus line: what agreement in ordinary
  operation leaves open about responses to intervention, how a deficiency
  of sufficiency and informational closure behave under refinement, and
  where maintenance is realized. Twenty entries, most of them first in
  distributed-agency, will-organization, learned-structure or
  evidence-for-experience and set out already by those lines' accounts;
  the mechanical map's part also held six entries on correspondences and
  the comparison of experiments, which the sibling account sets out
  because they barely link to these. The line's account is built over this
  one. It adds nothing of its own; its standing is its components'.
---
<!-- inactive-ok-file: CASE-164 CLAIM-477 CLAIM-478 THEORY-072 THEORY-085 — Proposed; a component and the entries components cite, with their standing -->
<!-- inactive-ok-file: CASE-203 CASE-227 CLAIM-044 CLAIM-632 — Proposed; entries of other parts whose stated links to these components are listed -->
<!-- inactive-ok-file: SYNTHESIS-019 SYNTHESIS-029 SYNTHESIS-030 SYNTHESIS-036 SYNTHESIS-041 SYNTHESIS-047 SYNTHESIS-048 SYNTHESIS-054 — Proposed; other lines' accounts that already integrate components, named and not integrated -->
<!-- inactive-ok-file: ADR-075 ADR-083 ADR-084 — Proposed; the decisions this account is drafted under -->
<!-- inactive-ok-file: QUESTION-244 — Answered; cited with its standing -->
<!-- inactive-ok-file: SYNTHESIS-tmp2gov9 SYNTHESIS-tmp68daz SYNTHESIS-tmpa7ef9 SYNTHESIS-tmpc35sn SYNTHESIS-tmpemzd4 SYNTHESIS-tmpgtv7b SYNTHESIS-tmphb9rl SYNTHESIS-tmpvz4mj — Proposed; cited with its standing -->

# SYNTHESIS-tmpe15k3: Agreement in ordinary operation does not fix how a system responds to an intervention on its mechanism: a coarse-graining exactly closed under its ordinary dynamics can lose that response, a deficiency of sufficiency measures the loss and cannot rise under refinement while closure is ordered by refinement in neither direction, causal abstraction does not secure the sufficiency, matched trajectories can hide efficacy and maintenance, and fidelity in ordinary operation certifies nothing about viability; where maintenance is realized is shown only by intervening on the production mechanisms relative to a boundary no intervention supplies, interventions show that a capacity is produced through a mechanism and not that it consists in it, and closure needs at least two constraints as persistence needs a productive cycle

*A part account of the formal-apparatus line ([ADR-083](../decisions.d/ADR-083.md), [ADR-084](../decisions.d/ADR-084.md)). The
line's account is built over it and over the accounts of the line's other
parts. The mechanical community map put 26 entries in this part. Twenty
are set out here. The other six ([CLAIM-011](../claims.d/CLAIM-011.md), [CLAIM-266](../claims.d/CLAIM-266.md), [CLAIM-373](../claims.d/CLAIM-373.md), [CLAIM-380](../claims.d/CLAIM-380.md),
[CLAIM-381](../claims.d/CLAIM-381.md) and [CLAIM-503](../claims.d/CLAIM-503.md)), on anchoring correspondences and comparing
experiments, are set out in the sibling account, because they form a
second inquiry that barely links to this one: five stored pairs among
themselves and one, a `complements` between [CLAIM-503](../claims.d/CLAIM-503.md) and [CLAIM-517](../claims.d/CLAIM-517.md), to the
twenty, against 31 pairs among the twenty (see "Whether the part holds
together").*

*Most components are first in another line, and other lines' accounts
already integrate them: [SYNTHESIS-048](SYNTHESIS-048.md) (distributed-agency) holds [ARG-050](../arguments.d/ARG-050.md),
[CLAIM-395](../claims.d/CLAIM-395.md), [CLAIM-480](../claims.d/CLAIM-480.md), [CLAIM-515](../claims.d/CLAIM-515.md), [CLAIM-516](../claims.d/CLAIM-516.md), [CLAIM-522](../claims.d/CLAIM-522.md), [CLAIM-528](../claims.d/CLAIM-528.md) and
[CLAIM-530](../claims.d/CLAIM-530.md); [SYNTHESIS-036](SYNTHESIS-036.md) (will-organization) holds [CLAIM-399](../claims.d/CLAIM-399.md) and [CLAIM-407](../claims.d/CLAIM-407.md);
[SYNTHESIS-054](SYNTHESIS-054.md) (distributed-agency) holds [CLAIM-409](../claims.d/CLAIM-409.md); [SYNTHESIS-019](SYNTHESIS-019.md)
(evidence-for-experience) holds [CLAIM-414](../claims.d/CLAIM-414.md); [SYNTHESIS-047](SYNTHESIS-047.md)
(distributed-agency) holds [CLAIM-517](../claims.d/CLAIM-517.md) and [CLAIM-536](../claims.d/CLAIM-536.md); [SYNTHESIS-029](SYNTHESIS-029.md) and
[SYNTHESIS-030](SYNTHESIS-030.md) (learned-structure) hold [CLAIM-387](../claims.d/CLAIM-387.md) and [CLAIM-392](../claims.d/CLAIM-392.md), and
[SYNTHESIS-030](SYNTHESIS-030.md) [CLAIM-536](../claims.d/CLAIM-536.md); [SYNTHESIS-041](SYNTHESIS-041.md) (will-organization) holds [CLAIM-540](../claims.d/CLAIM-540.md).
This account integrates them again because their `line` includes
formal-apparatus. [CASE-164](../cases.d/CASE-164.md), [TERM-062](../terms.d/TERM-062.md) and [TERM-068](../terms.d/TERM-068.md) have no other account.*

## The account

- **Closure under ordinary dynamics is not sufficiency for an
  intervention.** [CLAIM-407](../claims.d/CLAIM-407.md) (A's, from A16 and A17 of the exchange of
  2026-10-20, demonstrated, Active), quoting A16: "a representation can be
  perfectly informationally closed under the ordinary dynamics while
  failing to preserve a governance-relevant counterfactual distinction."
  Its deficiency for a declared intervention distribution is
  Γ = I(S; Y^(I) | T(S), I), which is ρ(h = 1) bits in the hidden
  governance bit ([CASE-125](../cases.d/CASE-125.md)), and "Γ = 0 exactly when, for every
  intervention ρ charges, the response kernels are constant on T's fibres
  over the states of positive probability". It is "an application of
  ordinary causal sufficiency, not new information theory". [CASE-164](../cases.d/CASE-164.md) (the
  lab's construction from an owner-supplied package, Proposed) is a second
  exact witness: on one 192-state kernel "closure on a support, global
  lumpability and sufficiency for a declared intervention mixture give
  different verdicts", with Γ = 0.55·H₂(1/3) ≈ 0.5051 bits for every
  description that omits the maintenance mode and 0 for the full state,
  and "a finite-sample sign test of closure fails in both directions at
  the sample sizes tested".
- **Refinement.** [CLAIM-409](../claims.d/CLAIM-409.md) (the record's join of two of A's drafts,
  demonstrated, Active): for one state law, intervention distribution and
  outcome, "if T₁ = g∘T₂ then Γ(T₂) ≤ Γ(T₁)", while informational closure
  is "monotone in neither direction", because refining a description
  "changes the future it must predict as well as the evidence". Its
  summary: "closure is not reversed by refinement, it is unordered by it."
  [CLAIM-387](../claims.d/CLAIM-387.md) and [CLAIM-392](../claims.d/CLAIM-392.md) (the readers' computations, re-run here,
  demonstrated, Active) show that information-bottleneck optima at two
  budgets need not be nested, for deterministic and for stochastic
  encoders: "Moving from the smaller to the larger budget changes which
  distinctions the representation draws, not only how many" ([CLAIM-392](../claims.d/CLAIM-392.md)).
- **Causal abstraction.** [CLAIM-399](../claims.d/CLAIM-399.md) (the record's join of its readings of
  the causal-abstraction papers with [CLAIM-407](../claims.d/CLAIM-407.md), demonstrated, Active):
  exact transformation, τ-abstraction and zero approximate-abstraction
  distance all accept the hidden-bit coarse-graining, "because each lets
  high-level noise carry what the coarse state drops"; for one outcome and
  the identity correspondence, sufficiency is their compatibility
  condition with the high-level context fixed to the coarse state, and
  "Neither notion is a special case of the other."
- **Which closure.** [TERM-068](../terms.d/TERM-068.md) (asked for by A11 to A14 on the owner's U11
  and U13, adopted by the owner, Active) lists the record's senses of
  "closure" so that a claim says which: informational closure (sense 1)
  is defined in full and is "Not a mark of a system"; organizational
  closure of constraints (sense 6) concerns "a set of constraints", a
  different object. [TERM-062](../terms.d/TERM-062.md) (Crutchfield and Shalizi's causal states and
  Rosas et al.'s υ-machine under one definition, adopted by the owner,
  Active) defines the causal state relative to a declared target, and
  says it is "Not interventional".
- **Matched behaviour conceals.** [CLAIM-414](../claims.d/CLAIM-414.md) (A10's, re-run here,
  demonstrated, Active): "in two finite constructions, systems that agree
  under ordinary operation differ in each, and a specified intervention
  exposes the difference that passive observation of the matched
  trajectories does not"; it is "not a general independence theorem".
  [CLAIM-517](../claims.d/CLAIM-517.md) (A16's, the regularity conditions the reader's, demonstrated,
  Active): a successor regulator within γ/L of a certifying one at every
  boundary context keeps a viable set invariant, an average distillation
  loss certifies this "only through coverage of the boundary contexts",
  and so "fidelity measured in ordinary operation certifies nothing about
  viability". [CLAIM-540](../claims.d/CLAIM-540.md) (A13's, rechecked, disclaimed, demonstrated,
  Active): the reinforcement a Dirichlet–categorical hierarchy gives a run
  of choices is "an observer's learning about a fixed mixture, not a
  change in what selects", raising the predicted repeat from 1/2 to 2/3
  when the first choice is observed and leaving it at 1/2 when it is
  forced. [CLAIM-536](../claims.d/CLAIM-536.md) (the owner's U12, stated precisely with one word
  corrected, demonstrated, Active) is the hierarchy it limits: within an
  episode two acts share a perspective with probability
  (a + 1)/(Ka + 1), against 1/K across episodes.
- **Where maintenance is realized.** [CLAIM-522](../claims.d/CLAIM-522.md) (A10's Proposition 5,
  demonstrated, Active): an outside controller supplying the production
  law as state feedback "yields the same trajectory under every
  perturbation of state", and "only interventions on the production
  mechanisms, relative to a declared boundary, separate the two". [ARG-050](../arguments.d/ARG-050.md)
  (the reader's, on the fat-handedness debate, contrast, Active) concludes
  [CLAIM-522](../claims.d/CLAIM-522.md) against that debate: the pathway "causes the capacities with a
  delay and can be intervened on surgically", and "intervention data
  locate a producer relative to a boundary and do not fix the boundary".
  [CLAIM-530](../claims.d/CLAIM-530.md) (the record's join of [CLAIM-522](../claims.d/CLAIM-522.md) with the mechanist account,
  interpretive, Active): producer and controller meet mutual
  manipulability's two manipulability conditions identically, so "what
  puts one inside and the other outside is parthood, a boundary the
  experiments presuppose and do not find".
- **Produced through, or consists in.** [CLAIM-528](../claims.d/CLAIM-528.md) (the reader's, on the
  same debate, interpretive, Active): "interventions show only the first";
  the synchronic relation "is underdetermined by intervention data", and
  which of the two a dependence is "depends on the time resolution at
  which a description treats the parts' response as instantaneous".
  [CLAIM-480](../claims.d/CLAIM-480.md) (A22's and A23's, demonstrated, Active) supplies the chain:
  eliminating an equilibrated interior leaves a coupling neither part has,
  a slowly relaxing one leaves a memory kernel, and "separation of time
  scales decides only whether that constraint is approximately
  memoryless"; for cellular sheaves the reduced constraint can relate
  three boundary values.
- **Four questions.** [CLAIM-515](../claims.d/CLAIM-515.md) (the owner's principle, interpretive,
  Active): whether an organization has a cognitive property is four
  questions, recoverable, exercisable, realized and maintained, which "can
  come apart, and none should be silently substituted for another"; it
  "says the four are where to look, not that they always come apart".
- **What maintenance needs.** [CLAIM-395](../claims.d/CLAIM-395.md) (the record's proof of Montévil
  and Mossio's property, demonstrated, Active): "a closed set of
  constraints has at least two members", and under its conditions (A) and
  (B) it has at least one slow and one fast dependence. [CLAIM-516](../claims.d/CLAIM-516.md) (A10's,
  rechecked, demonstrated, Active): with turnover and no basal production
  "a capacity that persists needs a productive cycle among its
  ancestors", and "a cycle is necessary and not sufficient, and a
  one-member cycle is not closure".

## The components

- [CLAIM-407](../claims.d/CLAIM-407.md), A's (A16 and A17, exchange of 2026-10-20), thesis,
  demonstrated, Active; first line formal-apparatus, also
  will-organization; rests on [CLAIM-350](../claims.d/CLAIM-350.md); grounds [CASE-125](../cases.d/CASE-125.md), [THEORY-820](../theory.d/THEORY-820.md),
  [THEORY-424](../theory.d/THEORY-424.md) and [THEORY-848](../theory.d/THEORY-848.md); uses [TERM-067](../terms.d/TERM-067.md) and [TERM-023](../terms.d/TERM-023.md); complements
  [CLAIM-414](../claims.d/CLAIM-414.md), [CLAIM-450](../claims.d/CLAIM-450.md), [CLAIM-517](../claims.d/CLAIM-517.md) and [CLAIM-522](../claims.d/CLAIM-522.md); corroborates [CLAIM-122](../claims.d/CLAIM-122.md).
- [CASE-164](../cases.d/CASE-164.md), the lab's construction (dmarx/PerspectiveLab), filed at the
  owner's direction from an owner-supplied package, stipulated
  construction, Proposed; formal-apparatus only; variant of [CASE-125](../cases.d/CASE-125.md);
  illustrates [CLAIM-407](../claims.d/CLAIM-407.md) and [CLAIM-409](../claims.d/CLAIM-409.md).
- [CLAIM-399](../claims.d/CLAIM-399.md), the record's join of its readings with [CLAIM-407](../claims.d/CLAIM-407.md), thesis,
  demonstrated, Active; first line formal-apparatus, also
  will-organization; rests on [CLAIM-407](../claims.d/CLAIM-407.md); grounds [THEORY-848](../theory.d/THEORY-848.md), [THEORY-849](../theory.d/THEORY-849.md),
  [THEORY-843](../theory.d/THEORY-843.md) and [CASE-125](../cases.d/CASE-125.md); uses [TERM-067](../terms.d/TERM-067.md).
- [CLAIM-409](../claims.d/CLAIM-409.md), the record's join of A's drafts (A6, A7, A16, A17), thesis,
  demonstrated, Active; first line formal-apparatus, also
  distributed-agency; rests on [CLAIM-407](../claims.d/CLAIM-407.md); grounds [THEORY-820](../theory.d/THEORY-820.md), [THEORY-717](../theory.d/THEORY-717.md)
  and [THEORY-822](../theory.d/THEORY-822.md); uses [TERM-068](../terms.d/TERM-068.md).
- [CLAIM-387](../claims.d/CLAIM-387.md), the reader's, from the reading of Equitz and Cover, re-run
  here, thesis, demonstrated, Active; first line learned-structure;
  answers [QUESTION-244](../questions.d/QUESTION-244.md); corroborates [CLAIM-405](../claims.d/CLAIM-405.md).
- [CLAIM-392](../claims.d/CLAIM-392.md), the reader's, from the reading of Charvin, Catenacci Volpi and
  Polani, re-run here, thesis, demonstrated, Active; first line
  learned-structure; rests on [CLAIM-387](../claims.d/CLAIM-387.md); answers [QUESTION-244](../questions.d/QUESTION-244.md).
- [TERM-068](../terms.d/TERM-068.md), asked for by A11 to A14 on the owner's U11 and U13, adopted by
  the owner, Active; formal-apparatus only.
- [TERM-062](../terms.d/TERM-062.md), the readings' definitions under one statement, at A13's and
  A14's request, adopted by the owner, Active; formal-apparatus only.
- [CLAIM-414](../claims.d/CLAIM-414.md), A10's (exchange on experience and interpretation), re-run
  here, narrowed after a review the owner relayed, thesis, demonstrated,
  Active; first line evidence-for-experience; grounds [CASE-126](../cases.d/CASE-126.md); uses
  [TERM-070](../terms.d/TERM-070.md) and [TERM-073](../terms.d/TERM-073.md); complements [CLAIM-407](../claims.d/CLAIM-407.md), [CLAIM-194](../claims.d/CLAIM-194.md), [CLAIM-456](../claims.d/CLAIM-456.md),
  [CLAIM-515](../claims.d/CLAIM-515.md), [CLAIM-521](../claims.d/CLAIM-521.md), [CLAIM-522](../claims.d/CLAIM-522.md), [CLAIM-528](../claims.d/CLAIM-528.md) and [CLAIM-530](../claims.d/CLAIM-530.md).
- [CLAIM-517](../claims.d/CLAIM-517.md), A16's (exchange "Analyze nucleation concepts"), with the
  regularity conditions stated by the reader, thesis, demonstrated,
  Active; first line distributed-agency; grounds [THEORY-134](../theory.d/THEORY-134.md); complements
  [CLAIM-503](../claims.d/CLAIM-503.md) and [CLAIM-407](../claims.d/CLAIM-407.md).
- [CLAIM-540](../claims.d/CLAIM-540.md), A13's (exchange "Assess SDT Coverage"), rechecked here,
  disclaimed, demonstrated, Active; first line will-organization; rests
  on [CLAIM-414](../claims.d/CLAIM-414.md); complements [CLAIM-025](../claims.d/CLAIM-025.md) and [CLAIM-536](../claims.d/CLAIM-536.md); uses [TERM-099](../terms.d/TERM-099.md) and
  [TERM-023](../terms.d/TERM-023.md).
- [CLAIM-536](../claims.d/CLAIM-536.md), the owner's U12 stated precisely, one word corrected, with
  the record's derivation, thesis, demonstrated, Active; first line
  learned-structure, also distributed-agency; complements [CLAIM-543](../claims.d/CLAIM-543.md) and
  [CLAIM-540](../claims.d/CLAIM-540.md); bears on [QUESTION-276](../questions.d/QUESTION-276.md) and [QUESTION-370](../questions.d/QUESTION-370.md).
- [CLAIM-522](../claims.d/CLAIM-522.md), A10's (its Proposition 5), thesis, demonstrated, Active;
  first line distributed-agency; grounds [CASE-189](../cases.d/CASE-189.md); uses [TERM-100](../terms.d/TERM-100.md);
  complements [CLAIM-414](../claims.d/CLAIM-414.md), [CLAIM-194](../claims.d/CLAIM-194.md), [CLAIM-407](../claims.d/CLAIM-407.md), [CLAIM-515](../claims.d/CLAIM-515.md), [CLAIM-528](../claims.d/CLAIM-528.md) and
  [CLAIM-531](../claims.d/CLAIM-531.md); bears on [QUESTION-093](../questions.d/QUESTION-093.md).
- [ARG-050](../arguments.d/ARG-050.md), the reader's, filed on reading the fat-handedness debate,
  contrast, Active; first line distributed-agency; concludes [CLAIM-522](../claims.d/CLAIM-522.md);
  grounds [CASE-189](../cases.d/CASE-189.md), [THEORY-1288](../theory.d/THEORY-1288.md) and [THEORY-1293](../theory.d/THEORY-1293.md).
- [CLAIM-530](../claims.d/CLAIM-530.md), the record's join of [CLAIM-522](../claims.d/CLAIM-522.md) with the mechanist account,
  thesis, interpretive, Active; first line distributed-agency; rests on
  [CLAIM-522](../claims.d/CLAIM-522.md); grounds [THEORY-1287](../theory.d/THEORY-1287.md) and [CASE-189](../cases.d/CASE-189.md); complements [CLAIM-194](../claims.d/CLAIM-194.md) and
  [CLAIM-414](../claims.d/CLAIM-414.md); bears on [QUESTION-086](../questions.d/QUESTION-086.md) and [QUESTION-093](../questions.d/QUESTION-093.md).
- [CLAIM-528](../claims.d/CLAIM-528.md), the reader's, filed on reading the same debate, thesis,
  interpretive, Active; first line distributed-agency; rests on [CLAIM-480](../claims.d/CLAIM-480.md);
  grounds [THEORY-1288](../theory.d/THEORY-1288.md), [THEORY-1293](../theory.d/THEORY-1293.md) and [CASE-189](../cases.d/CASE-189.md); complements [CLAIM-522](../claims.d/CLAIM-522.md),
  [CLAIM-515](../claims.d/CLAIM-515.md), [CLAIM-414](../claims.d/CLAIM-414.md) and [CLAIM-194](../claims.d/CLAIM-194.md); bears on [QUESTION-284](../questions.d/QUESTION-284.md).
- [CLAIM-480](../claims.d/CLAIM-480.md), A22's and A23's (exchange of 2026-10-27), revised at the
  owner's review, thesis, demonstrated, Active; first line
  distributed-agency; corroborates [CLAIM-477](../claims.d/CLAIM-477.md); complements [CLAIM-478](../claims.d/CLAIM-478.md) and
  [CLAIM-471](../claims.d/CLAIM-471.md); uses [TERM-090](../terms.d/TERM-090.md) and [TERM-091](../terms.d/TERM-091.md).
- [CLAIM-515](../claims.d/CLAIM-515.md), the owner's principle, thesis, interpretive, Active; first
  line distributed-agency; complements [CLAIM-474](../claims.d/CLAIM-474.md), [CLAIM-414](../claims.d/CLAIM-414.md), [CLAIM-522](../claims.d/CLAIM-522.md),
  [CLAIM-523](../claims.d/CLAIM-523.md) and [CLAIM-528](../claims.d/CLAIM-528.md); bears on [QUESTION-362](../questions.d/QUESTION-362.md).
- [CLAIM-395](../claims.d/CLAIM-395.md), the record's proof, filed from [THEORY-072](../theory.d/THEORY-072.md), thesis,
  demonstrated, Active; first line distributed-agency; grounds [LIT-582](../literature.d/LIT-582.md);
  complements [CLAIM-478](../claims.d/CLAIM-478.md) and [CLAIM-516](../claims.d/CLAIM-516.md).
- [CLAIM-516](../claims.d/CLAIM-516.md), A10's, rechecked by the reader, thesis, demonstrated,
  Active; first line distributed-agency; grounds [CASE-189](../cases.d/CASE-189.md); uses [TERM-070](../terms.d/TERM-070.md);
  complements [CLAIM-395](../claims.d/CLAIM-395.md), [CLAIM-566](../claims.d/CLAIM-566.md), [CLAIM-597](../claims.d/CLAIM-597.md) and [CLAIM-604](../claims.d/CLAIM-604.md).

## Links the components state, and where

- **Sufficiency, its witnesses and abstraction.** [CLAIM-399](../claims.d/CLAIM-399.md) and [CLAIM-409](../claims.d/CLAIM-409.md)
  rest on [CLAIM-407](../claims.d/CLAIM-407.md), and [CASE-164](../cases.d/CASE-164.md) illustrates [CLAIM-407](../claims.d/CLAIM-407.md) and [CLAIM-409](../claims.d/CLAIM-409.md).
  [CLAIM-407](../claims.d/CLAIM-407.md)'s body: "How sufficiency sits beside them is [CLAIM-399](../claims.d/CLAIM-399.md)", and
  its note of 2026-10-26: "[CASE-164](../cases.d/CASE-164.md) is a second exact witness, built
  separately from [CASE-125](../cases.d/CASE-125.md)". [CASE-164](../cases.d/CASE-164.md) reads its refinement result as
  "[CLAIM-409](../claims.d/CLAIM-409.md)'s monotone half", and its ablation as "the shape of
  [CLAIM-409](../claims.d/CLAIM-409.md)'s non-monotone half, but it is in strong lumpability, not in
  informational closure". [CLAIM-399](../claims.d/CLAIM-399.md) lists what the papers do not contain,
  among it "Γ's monotonicity under refinement ([CLAIM-409](../claims.d/CLAIM-409.md))"; [CLAIM-409](../claims.d/CLAIM-409.md)'s
  last limit is "Not the causal-abstraction papers' transitivity."
  [CLAIM-399](../claims.d/CLAIM-399.md) and [CLAIM-407](../claims.d/CLAIM-407.md) share [CASE-125](../cases.d/CASE-125.md) as ground, and [CASE-164](../cases.d/CASE-164.md) is a
  variant of it.
- **Senses of closure.** [CLAIM-409](../claims.d/CLAIM-409.md) uses [TERM-068](../terms.d/TERM-068.md) and states closure in its
  sense 1; [TERM-068](../terms.d/TERM-068.md)'s sense 1 says it "is not preserved by refinement, nor
  by coarsening" ([CLAIM-409](../claims.d/CLAIM-409.md)), and its sense 6 cites [CLAIM-395](../claims.d/CLAIM-395.md). In [CASE-164](../cases.d/CASE-164.md)'s
  summary the senses of closure of [TERM-068](../terms.d/TERM-068.md) "are computed exactly side by
  side".
  [TERM-062](../terms.d/TERM-062.md) and [TERM-068](../terms.d/TERM-068.md) cite each other: the ε-machine and the υ-machine
  of a coarse-graining "coincide exactly when Z is informationally closed
  ([THEORY-820](../theory.d/THEORY-820.md) (c); [TERM-068](../terms.d/TERM-068.md), sense 1)".
- **Budgets and refinement.** [CLAIM-392](../claims.d/CLAIM-392.md) rests on [CLAIM-387](../claims.d/CLAIM-387.md), and
  [CLAIM-387](../claims.d/CLAIM-387.md)'s limits say the stochastic case "was settled the same day"
  by [CLAIM-392](../claims.d/CLAIM-392.md). [CLAIM-409](../claims.d/CLAIM-409.md)'s limits place both: "That optimal partitions
  at two budgets need not nest ([CLAIM-387](../claims.d/CLAIM-387.md), [CLAIM-392](../claims.d/CLAIM-392.md)) is about optima, not
  about one description's deficiency."
- **From governance to interpretation, maintenance and viability.**
  [CLAIM-414](../claims.d/CLAIM-414.md) and [CLAIM-407](../claims.d/CLAIM-407.md) complement each other; [CLAIM-414](../claims.d/CLAIM-414.md)'s summary:
  "These are [CLAIM-407](../claims.d/CLAIM-407.md)'s lesson about governance and [CLAIM-194](../claims.d/CLAIM-194.md)'s about
  boundaries, applied to interpretation", and its body: "Part 1 is the
  same lesson for an interpretation's authority, and part 2 for its
  maintenance." [CLAIM-517](../claims.d/CLAIM-517.md) and [CLAIM-407](../claims.d/CLAIM-407.md) complement each other, and
  [CLAIM-517](../claims.d/CLAIM-517.md)'s body: "This is the coverage form of [CLAIM-407](../claims.d/CLAIM-407.md): closure under
  ordinary dynamics does not fix responses to intervention." [CLAIM-407](../claims.d/CLAIM-407.md)
  and [CLAIM-522](../claims.d/CLAIM-522.md) complement each other; neither body says how.
- **Observer learning.** [CLAIM-540](../claims.d/CLAIM-540.md) rests on [CLAIM-414](../claims.d/CLAIM-414.md): self-formation "is
  told apart from the observer's learning only by intervening
  ([CLAIM-414](../claims.d/CLAIM-414.md))". [CLAIM-540](../claims.d/CLAIM-540.md) and [CLAIM-536](../claims.d/CLAIM-536.md) complement each other; [CLAIM-540](../claims.d/CLAIM-540.md)'s
  summary: "It limits the record's own H1/H2 reading ([CLAIM-536](../claims.d/CLAIM-536.md))", and
  [CLAIM-536](../claims.d/CLAIM-536.md)'s limits: "its reinforcement of a run of choices is the
  observer's learning ([CLAIM-540](../claims.d/CLAIM-540.md))".
- **The minimal closure.** [CLAIM-414](../claims.d/CLAIM-414.md)'s body: "The second system pair is
  the smallest closure [CLAIM-395](../claims.d/CLAIM-395.md) allows", and "A10 did not cite [CLAIM-395](../claims.d/CLAIM-395.md),
  but its construction meets that claim's conditions (A) and (B)."
  [CLAIM-395](../claims.d/CLAIM-395.md) and [CLAIM-516](../claims.d/CLAIM-516.md) complement each other; [CLAIM-516](../claims.d/CLAIM-516.md)'s summary: "a
  self-loop is not closure in [TERM-070](../terms.d/TERM-070.md)'s sense or [CLAIM-395](../claims.d/CLAIM-395.md)'s, which need
  two or more constraints."
- **From passive observation to state interventions to the boundary.**
  [CLAIM-522](../claims.d/CLAIM-522.md)'s summary: "It extends [CLAIM-414](../claims.d/CLAIM-414.md) from passive observation to
  every intervention on state", and the two complement each other.
  [ARG-050](../arguments.d/ARG-050.md) concludes [CLAIM-522](../claims.d/CLAIM-522.md) and names [CLAIM-528](../claims.d/CLAIM-528.md): "[CLAIM-528](../claims.d/CLAIM-528.md) states the
  distinction." [CLAIM-530](../claims.d/CLAIM-530.md) rests on [CLAIM-522](../claims.d/CLAIM-522.md); [CLAIM-522](../claims.d/CLAIM-522.md)'s note of
  2026-11-01 records it ("Filed as [CLAIM-530](../claims.d/CLAIM-530.md)"), and [CLAIM-414](../claims.d/CLAIM-414.md)'s note of
  2026-11-01 says interlevel experiments "show componency only relative to
  a boundary drawn beforehand ([THEORY-1287](../theory.d/THEORY-1287.md), [CLAIM-530](../claims.d/CLAIM-530.md))". [ARG-050](../arguments.d/ARG-050.md),
  [CLAIM-516](../claims.d/CLAIM-516.md), [CLAIM-522](../claims.d/CLAIM-522.md), [CLAIM-528](../claims.d/CLAIM-528.md) and [CLAIM-530](../claims.d/CLAIM-530.md) share [CASE-189](../cases.d/CASE-189.md) as ground.
- **The two senses of realized.** [CLAIM-528](../claims.d/CLAIM-528.md) rests on [CLAIM-480](../claims.d/CLAIM-480.md), and
  [CLAIM-480](../claims.d/CLAIM-480.md)'s note of 2026-11-01 says "[CLAIM-528](../claims.d/CLAIM-528.md) part 3 rests on this."
  [CLAIM-528](../claims.d/CLAIM-528.md): "[CLAIM-522](../claims.d/CLAIM-522.md) stands as stated", and "[CLAIM-515](../claims.d/CLAIM-515.md)'s third question
  should say which reading it means"; "The fat-handedness result does not
  reach them ([ARG-050](../arguments.d/ARG-050.md))". [CLAIM-515](../claims.d/CLAIM-515.md)'s notes of 2026-11-01 take both up:
  "[CLAIM-528](../claims.d/CLAIM-528.md) states the split", and the fourth question "presupposes an
  answer to where the organization ends" ([CLAIM-530](../claims.d/CLAIM-530.md)). [CLAIM-515](../claims.d/CLAIM-515.md) names
  [CLAIM-414](../claims.d/CLAIM-414.md) and [CLAIM-522](../claims.d/CLAIM-522.md) as its instances for maintenance; [CLAIM-515](../claims.d/CLAIM-515.md)
  complements [CLAIM-414](../claims.d/CLAIM-414.md), [CLAIM-522](../claims.d/CLAIM-522.md) and [CLAIM-528](../claims.d/CLAIM-528.md); [CLAIM-414](../claims.d/CLAIM-414.md) complements
  [CLAIM-515](../claims.d/CLAIM-515.md), [CLAIM-528](../claims.d/CLAIM-528.md) and [CLAIM-530](../claims.d/CLAIM-530.md), and [CLAIM-528](../claims.d/CLAIM-528.md) and [CLAIM-530](../claims.d/CLAIM-530.md)
  complement [CLAIM-414](../claims.d/CLAIM-414.md) in turn. Of these, the pair [CLAIM-414](../claims.d/CLAIM-414.md) and [CLAIM-528](../claims.d/CLAIM-528.md)
  has no body text saying how.

## Links to other parts, stated

Outgoing, from these components to entries of other parts of the line:

- **To the effective-description part ([SYNTHESIS-tmpa7ef9](SYNTHESIS-tmpa7ef9.md)).** [CLAIM-407](../claims.d/CLAIM-407.md) rests on
  [CLAIM-350](../claims.d/CLAIM-350.md), and its "Where it was before" quotes [CLAIM-350](../claims.d/CLAIM-350.md)'s "What it does
  not say": "That observational adequacy is causal adequacy." [CLAIM-409](../claims.d/CLAIM-409.md):
  "Nothing in it is special to governance: it is any fixed-target
  sufficiency, as in [CLAIM-152](../claims.d/CLAIM-152.md)." [TERM-062](../terms.d/TERM-062.md)'s summary lists [CLAIM-152](../claims.d/CLAIM-152.md) among
  the entries that used the causal state "with no TERM", and its limits
  cite "[CLAIM-152](../claims.d/CLAIM-152.md)'s note of 2026-10-20". [TERM-068](../terms.d/TERM-068.md) names [CLAIM-386](../claims.d/CLAIM-386.md),
  [CLAIM-389](../claims.d/CLAIM-389.md), [CLAIM-394](../claims.d/CLAIM-394.md) and [CLAIM-398](../claims.d/CLAIM-398.md) as uses of informational closure,
  [CLAIM-389](../claims.d/CLAIM-389.md), [CLAIM-397](../claims.d/CLAIM-397.md) and [CLAIM-398](../claims.d/CLAIM-398.md) for vanishing Mori–Zwanzig memory,
  [CLAIM-386](../claims.d/CLAIM-386.md) for the linear closure defect, and [CLAIM-294](../claims.d/CLAIM-294.md) as a homonym.
- **To the naming part ([SYNTHESIS-tmpgtv7b](SYNTHESIS-tmpgtv7b.md)).** [TERM-068](../terms.d/TERM-068.md) names [CLAIM-388](../claims.d/CLAIM-388.md) as a use of
  informational closure.
- **To the stability part ([SYNTHESIS-tmpemzd4](SYNTHESIS-tmpemzd4.md)).** [CLAIM-414](../claims.d/CLAIM-414.md) complements [CLAIM-521](../claims.d/CLAIM-521.md), and
  its note of 2026-11-07 says the software instance "is this claim and
  [CLAIM-521](../claims.d/CLAIM-521.md)".
- **To the Granger and transfer-entropy account ([SYNTHESIS-tmp2gov9](SYNTHESIS-tmp2gov9.md)).** [TERM-068](../terms.d/TERM-068.md) defines informational
  closure as "transfer entropy from the micro past with Z's whole history
  and no environment ([TERM-057](../terms.d/TERM-057.md) with k and l unbounded)".
- **To the entries the line account integrates directly ([SYNTHESIS-tmpvz4mj](SYNTHESIS-tmpvz4mj.md)).** [CLAIM-395](../claims.d/CLAIM-395.md)'s history: filed Active
  and demonstrated "as [CLAIM-391](../claims.d/CLAIM-391.md) was from [THEORY-085](../theory.d/THEORY-085.md)".

Incoming, stated by entries of other parts:

- **Reachability ([SYNTHESIS-tmpc35sn](SYNTHESIS-tmpc35sn.md)).** [CLAIM-577](../claims.d/CLAIM-577.md): "[CLAIM-414](../claims.d/CLAIM-414.md)'s matched trajectories
  and the unrecorded calls of [CASE-203](../cases.d/CASE-203.md) are the observational side of
  this." [CLAIM-632](../claims.d/CLAIM-632.md) quotes [CLAIM-414](../claims.d/CLAIM-414.md)'s limit, "Nor is intervention the only
  way to tell the systems apart". [QUESTION-391](../questions.d/QUESTION-391.md) lists [CLAIM-480](../claims.d/CLAIM-480.md)'s memory
  case.
- **Effective description ([SYNTHESIS-tmpa7ef9](SYNTHESIS-tmpa7ef9.md)).** [CLAIM-350](../claims.d/CLAIM-350.md)'s note: Construction B is
  "filed as [CLAIM-407](../claims.d/CLAIM-407.md) with [CASE-125](../cases.d/CASE-125.md)", and the hidden governance bit
  separates exact transformation from its factorization ("[THEORY-848](../theory.d/THEORY-848.md),
  [CLAIM-399](../claims.d/CLAIM-399.md)"). [CLAIM-401](../claims.d/CLAIM-401.md) and [QUESTION-252](../questions.d/QUESTION-252.md) read [CASE-164](../cases.d/CASE-164.md) as non-implications
  among the conditions on an effective description, [QUESTION-252](../questions.d/QUESTION-252.md) naming
  "[CLAIM-407](../claims.d/CLAIM-407.md)'s shape". [TERM-065](../terms.d/TERM-065.md) names [CLAIM-387](../claims.d/CLAIM-387.md) as "The budget of a
  compression". [TERM-069](../terms.d/TERM-069.md): two systems equivalent under every passive probe
  "can respond differently to an intervention on their mechanism
  ([CASE-125](../cases.d/CASE-125.md), [CLAIM-407](../claims.d/CLAIM-407.md))".
- **Frustration ([SYNTHESIS-tmp68daz](SYNTHESIS-tmp68daz.md)).** [CLAIM-459](../claims.d/CLAIM-459.md): a subthreshold effect "shows only
  under a further perturbation, as [CLAIM-414](../claims.d/CLAIM-414.md)'s method requires".
- **Gluing ([SYNTHESIS-tmphb9rl](SYNTHESIS-tmphb9rl.md)).** [CLAIM-044](../claims.d/CLAIM-044.md) cites [CLAIM-409](../claims.d/CLAIM-409.md) for a property that fails
  to survive a join.
- **Stability ([SYNTHESIS-tmpemzd4](SYNTHESIS-tmpemzd4.md)).** [CLAIM-521](../claims.d/CLAIM-521.md) complements [CLAIM-414](../claims.d/CLAIM-414.md). [CASE-227](../cases.d/CASE-227.md)'s
  proposed arms include "c kept by an outside controller, and c kept by
  internal production (compare [CLAIM-522](../claims.d/CLAIM-522.md) and [CLAIM-456](../claims.d/CLAIM-456.md))".

Across to the sibling account of this part: [CLAIM-503](../claims.d/CLAIM-503.md) and [CLAIM-517](../claims.d/CLAIM-517.md)
complement each other, in front matter only.

## Whether the part holds together

Counting pairs of members joined by a front-matter relation or a mention
in either's body, summary or history, the mechanical part has 37 pairs:

- 14 among the maintenance entries ([ARG-050](../arguments.d/ARG-050.md), [CLAIM-395](../claims.d/CLAIM-395.md), [CLAIM-414](../claims.d/CLAIM-414.md),
  [CLAIM-480](../claims.d/CLAIM-480.md), [CLAIM-515](../claims.d/CLAIM-515.md), [CLAIM-516](../claims.d/CLAIM-516.md), [CLAIM-522](../claims.d/CLAIM-522.md), [CLAIM-528](../claims.d/CLAIM-528.md), [CLAIM-530](../claims.d/CLAIM-530.md));
- 12 among the sufficiency and closure entries ([CASE-164](../cases.d/CASE-164.md), [CLAIM-387](../claims.d/CLAIM-387.md),
  [CLAIM-392](../claims.d/CLAIM-392.md), [CLAIM-399](../claims.d/CLAIM-399.md), [CLAIM-407](../claims.d/CLAIM-407.md), [CLAIM-409](../claims.d/CLAIM-409.md), [CLAIM-517](../claims.d/CLAIM-517.md), [TERM-062](../terms.d/TERM-062.md),
  [TERM-068](../terms.d/TERM-068.md)), [CLAIM-517](../claims.d/CLAIM-517.md)'s one link being to [CLAIM-407](../claims.d/CLAIM-407.md);
- 3 between those two groups ([CLAIM-395](../claims.d/CLAIM-395.md) with [TERM-068](../terms.d/TERM-068.md), [CLAIM-407](../claims.d/CLAIM-407.md) with
  [CLAIM-414](../claims.d/CLAIM-414.md) and with [CLAIM-522](../claims.d/CLAIM-522.md)), and 2 for [CLAIM-536](../claims.d/CLAIM-536.md) and [CLAIM-540](../claims.d/CLAIM-540.md) (to each
  other, and [CLAIM-540](../claims.d/CLAIM-540.md) to [CLAIM-414](../claims.d/CLAIM-414.md)): 31 among the twenty here;
- 5 among the six correspondence and deficiency entries, and 1 from them
  to the twenty ([CLAIM-503](../claims.d/CLAIM-503.md) with [CLAIM-517](../claims.d/CLAIM-517.md)).

The first two groups are joined by stated readings ([CLAIM-414](../claims.d/CLAIM-414.md)'s and
[CLAIM-517](../claims.d/CLAIM-517.md)'s of [CLAIM-407](../claims.d/CLAIM-407.md), [CLAIM-522](../claims.d/CLAIM-522.md)'s of [CLAIM-414](../claims.d/CLAIM-414.md)) and are kept in one
account; the six are not, and are set out in the sibling account.
[CLAIM-536](../claims.d/CLAIM-536.md) reaches the part only through [CLAIM-540](../claims.d/CLAIM-540.md), and [CLAIM-387](../claims.d/CLAIM-387.md) and
[CLAIM-392](../claims.d/CLAIM-392.md) only through [CLAIM-409](../claims.d/CLAIM-409.md)'s limit; both are kept because their
`line` places them in formal-apparatus and nothing in another part claims
them.

## Not stated on the record

Links across the components that no entry states, tested by
[ADR-075](../decisions.d/ADR-075.md)'s step 5 and not filed:

- **One ladder of what separates.** That passive observation, interventions
  on state, interventions on mechanisms relative to a boundary, and the
  boundary itself form one order, each separating what the one before
  cannot and presupposing more. Its steps are stated: [CLAIM-522](../claims.d/CLAIM-522.md)'s summary
  (from [CLAIM-414](../claims.d/CLAIM-414.md)), [ARG-050](../arguments.d/ARG-050.md)'s "Does the contrast supply the boundary?",
  [CLAIM-530](../claims.d/CLAIM-530.md) and [CLAIM-515](../claims.d/CLAIM-515.md)'s note. Joined, it is a juxtaposition: no case
  has every step hold and the order fail, and no derivation adds to them.
- **The producer's location as a hidden bit.** That [CLAIM-522](../claims.d/CLAIM-522.md)'s pair is
  [CLAIM-407](../claims.d/CLAIM-407.md)'s shape, with where the producer sits as the hidden parameter:
  a description by the capacities is closed under ordinary dynamics and
  has Γ > 0 for any distribution charging a pathway knockout. The
  derivation is a substitution, and the identification is already stated
  by [CLAIM-414](../claims.d/CLAIM-414.md) (its part 2 is [CLAIM-407](../claims.d/CLAIM-407.md)'s lesson "for its maintenance") and
  [CLAIM-522](../claims.d/CLAIM-522.md) (which extends [CLAIM-414](../claims.d/CLAIM-414.md)); [CASE-164](../cases.d/CASE-164.md)'s maintenance mode is the
  instance, though it does not cite [CLAIM-522](../claims.d/CLAIM-522.md).
- **Fidelity where it was fitted certifies nothing.** That agreement
  measured where a system was trained or observed in ordinary operation
  never certifies what it preserves elsewhere, joining [CLAIM-517](../claims.d/CLAIM-517.md) to the
  sibling part's [CLAIM-266](../claims.d/CLAIM-266.md) and [CLAIM-011](../claims.d/CLAIM-011.md). As a universal it is false by
  [CLAIM-517](../claims.d/CLAIM-517.md)'s own coverage step: a distillation whose training contexts
  include the boundary contexts, each with probability at least μ_min, is
  certified by its training loss. As "need not certify", it is a
  conjunction of held instances. The narrower sentence, that a training
  signal certifies only where it sees the response in full at the
  contexts that decide, leaves "the contexts that decide" free.
- **Closure across time scales.** That a closed set of constraints, having
  a slow and a fast dependence ([CLAIM-395](../claims.d/CLAIM-395.md)), mixes constitution and
  causation in [CLAIM-528](../claims.d/CLAIM-528.md)'s sense at any resolution between its scales. The
  resolution is a free parameter: at a resolution coarser than every scale
  every dependence is synchronic. [CLAIM-395](../claims.d/CLAIM-395.md)'s note of 2026-10-27 holds the
  nearest form, that "a closed network of dependence cannot be described
  as a strictly one-directional descent through that hierarchy".
- **Closure as the boundary.** That [CLAIM-516](../claims.d/CLAIM-516.md)'s productive cycle supplies
  the boundary [CLAIM-530](../claims.d/CLAIM-530.md) says the experiments presuppose. [CLAIM-522](../claims.d/CLAIM-522.md)'s note
  names closure as "A candidate source for the boundary", and [CLAIM-530](../claims.d/CLAIM-530.md)
  leaves open "Whether that is a constitutive criterion, or only another
  declared boundary"; with no basal production the sentence is close to a
  definition.
- **Budgets and deficiency.** That a larger budget's optimum need not have
  a lower deficiency than a smaller one's. [CLAIM-409](../claims.d/CLAIM-409.md)'s limit already says
  its inequality holds along refinement chains only and that [CLAIM-387](../claims.d/CLAIM-387.md) and
  [CLAIM-392](../claims.d/CLAIM-392.md) are about optima.

## What it does not say

- That closure, sufficiency or maintenance marks a system or an agent
  ([CLAIM-407](../claims.d/CLAIM-407.md), [CLAIM-409](../claims.d/CLAIM-409.md), [TERM-068](../terms.d/TERM-068.md); [CLAIM-414](../claims.d/CLAIM-414.md), [CLAIM-522](../claims.d/CLAIM-522.md)).
- That the separations are a general independence theorem ([CLAIM-414](../claims.d/CLAIM-414.md),
  [CLAIM-515](../claims.d/CLAIM-515.md)).
- That intervention data fix a boundary, or show what a capacity consists
  in at a time ([ARG-050](../arguments.d/ARG-050.md), [CLAIM-528](../claims.d/CLAIM-528.md), [CLAIM-530](../claims.d/CLAIM-530.md)).
- Anything with standing of its own.
