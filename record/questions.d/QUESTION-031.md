---
number: 31
status: Open
formerly:
- QUESTION-tmpybqw8
title: 'When does a chosen family of observational probes separate the communicative realizations a task needs told apart, and when does it collapse distinct ones, beyond the cases in which the task''s target and the probes'' outcome laws are linear in one state?'
version: 5
history:
- version: 2
  date: '2026-10-25'
  note: >-
    A dated note added: experimental design as the choice of probes, with
    CASE-159. The question is unchanged.
- version: 3
  date: '2026-10-25'
  note: >-
    The note of 2026-10-25 checked against the reading of Chaloner and
    Verdinelli (NOTE-1161): the log det criterion is Bayes
    D-optimality, A29's aim is a c-, Ds- or discrimination criterion, and
    design ranks probe families without giving a separation condition. A
    lemma from partial monitoring answers one decision family. The question
    is unchanged and stays Open.
- version: 4
  date: '2026-10-25'
  note: >-
    Split under ADR-049 at the owner's direction (2026-10-25). Where the
    task's target and the probes' outcome laws are linear in one state is
    QUESTION-272, Answered by THEORY-962 and CLAIM-452. This
    question is reworded to what is left. The previous title was 'When does
    a chosen family of observational probes separate the communicative
    realizations a task needs told apart, and when does it collapse distinct
    ones?'
- version: 5
  date: '2026-10-26'
  note: >-
    A dated note added: a nonlinear case with a known catalog (CASE-
    tmpw6jjd), where one probe collapses two mechanisms and a pair
    separates them. Extended the same day with the lab's v2.4 and v2.5
    (dmarx/PerspectiveLab@f392084), in which probes change the
    organization and a misfit alarm depends on the probes chosen. The
    question is unchanged.
tags:
- mathematics
- pragmatics
date: '2026-10-10'
line: pragmatic-transport
refines:
- QUESTION-001
summary: >-
  A173's secondary question ("When do restricted probes separate
  communicative realizations?"), v7's RQ3 (A178) and A214 §3. It is
  the open half of [CLAIM-142](../claims.d/CLAIM-142.md): observational equivalence is
  relative to the probes, so how rich must the probes be? The discrete
  case has exact answers, and so does a metric-enriched one. The
  stochastic, decision-relative version is open.
refined_by:
- QUESTION-272
bearing:
- CLAIM-193
---
<!-- inactive-ok-file: CLAIM-129 CLAIM-149 THEORY-008 THEORY-019 — listed as material that may bear on this question, not as settled -->
<!-- inactive-ok-file: CLAIM-142 CLAIM-077 — Proposed; open, and cited as open: the claim is under test, not settled -->

# QUESTION-031: When does a chosen family of observational probes separate the communicative realizations a task needs told apart, and when does it collapse distinct ones, beyond the cases in which the task's target and the probes' outcome laws are linear in one state?

## Why it is a question

A173 put it as a secondary question: "When do restricted probes separate
communicative realizations?" A178 made it RQ3: "When does a selected family
of observational probes distinguish relevant communicative realizations, and
when do restricted probing profiles collapse distinct structures?" A214 §3
asked it again: "How rich must the observational relationships be to
separate the communicative kinds we care about?"

It is open because [CLAIM-142](../claims.d/CLAIM-142.md) makes observational equivalence
([TERM-014](../terms.d/TERM-014.md)) relative to the probe family, and says nothing about which
family suffices. [CLAIM-077](../claims.d/CLAIM-077.md) requires a transport to keep specified
distinctions apart, and this question asks when the probes can even see
them. [CLAIM-050](../claims.d/CLAIM-050.md) makes fidelity relative to the receiver's decisions, so
"the realizations a task needs told apart" is fixed by a family of
decisions, not by full structural identity.

An answer would be a condition on a probe family, checkable before the data
are seen, under which two realizations that agree on every probe also agree
on every decision in the stated family. A demonstration that some family
separates some pair is not an answer.

## What is already known

- **The discrete case.** For finite relational structures, homomorphism
  counts from every finite structure determine isomorphism (Lovász 1967,
  noted in [THEORY-032](../theory.d/THEORY-032.md) and [NOTE-195](../notes.d/NOTE-195.md)). Restricted families give exact
  restricted answers: counts from trees characterize colour refinement, and
  counts from graphs of bounded treewidth characterize the k-dimensional
  Weisfeiler–Leman test. That last pair of results is given here from
  memory, without an identifier, and has not been checked.
- **The categorical case.** The restricted Yoneda functor along a family of
  probes is fully faithful exactly when the family is dense
  ([CLAIM-142](../claims.d/CLAIM-142.md)). A probe table without composition is not a Yoneda
  profile at all.
- **The enriched case.** For Lawvere metric spaces the Yoneda embedding is
  an isometry (Lawvere 1973), so "distance between profiles equals distance
  between objects" already holds there. Bradley, Terilla and Vlassopoulos
  model expressions by [0,1]-enriched copresheaves of continuation
  probabilities (arXiv:2106.07890, not held), which is prior art for a
  probabilistic version. A158 §6 proposed "an enriched or probabilistic
  analogue of Yoneda" without knowing of either.

## What stays open

The stochastic, decision-relative version. Probes return distributions, not
hom-sets; the families are finite and fixed by an experimenter; and the
target is not isomorphism but sameness for a stated family of decisions, an
order in Blackwell's sense. No result the record holds says when such a
family separates what the decisions need. A158's probe-weighted distortion,
a weighted sum of per-probe distances, is not a Yoneda construction: it
ignores composition. [QUESTION-022](QUESTION-022.md) asks the neighbouring question for
transports: which stochastic maps carry compatible empirical models to
compatible ones.

## Note of 2026-10-11: material in the record that may bear on this

A synthesis review of 2026-10-11 found these entries bearing on this
question without being linked to it. Each is listed for what its title
says; none has yet been assessed as an answer, and none is linked by
`answers`.

- [THEORY-175](../theory.d/THEORY-175.md): Cosine similarities to matched anchor points are invariant
  exactly to the maps that preserve cosines, and…
- [CLAIM-129](../claims.d/CLAIM-129.md): A factorization recovers only the structure visible in the
  relations it is fitted to, so a topic can…
- [CLAIM-149](../claims.d/CLAIM-149.md): A probe family that supplies a transformation's training
  signal cannot also certify what the…
- [THEORY-019](../theory.d/THEORY-019.md): Symmetry forces spectral degeneracy but degeneracy does not
  identify a symmetry: an operator commuting…
- [THEORY-008](../theory.d/THEORY-008.md): What a regularized linear readout can decode from a
  representation is a function of its normalized kernel,…

[THEORY-008](../theory.d/THEORY-008.md) gives half of an answer for linear probes: a regularized linear
readout can decode only what is a function of the normalized kernel.

## Note of 2026-10-25: choosing probes

From A29–A31 of the exchange of 2026-10-24, continued. Bayesian
experimental design (Chaloner and Verdinelli 1995, [LIT-1525](../literature.d/LIT-1525.md), read in
[NOTE-1161](../notes.d/NOTE-1161.md)) turns this question into a choice: pick the design ξ over
contexts that maximizes a criterion of G_ξ = Σ_c ξ(c)G_c (log det, or a
discrimination or prediction criterion fixed by the task). A29: "our
objectives are often more specific. We might care about distinguishing the
effect of authority from the effect of legibility, rather than estimating
every parameter equally well." In [CASE-152](../cases.d/CASE-152.md), do(b = b₀) gives
G_aa = b₀² > 0 (checked). In [CASE-159](../cases.d/CASE-159.md), a rare context makes authority
shares identifiable that routine probes leave invisible. Both separate by
changing the experiment, not the coordinates ([CLAIM-305](../claims.d/CLAIM-305.md)). A caution from
A29, with [CLAIM-130](../claims.d/CLAIM-130.md): changing a participant's standing to separate
explanations "could also change which communicative act is performed".

The reading places these. Σ_c ξ(c)G_c with log det is Bayes D-optimality
on the expected Fisher information ([THEORY-956](../theory.d/THEORY-956.md) for the linear case,
[THEORY-954](../theory.d/THEORY-954.md) for the nonlinear one). A29's "distinguish authority from
legibility" is c- or Ds-optimality, or Spezzaferri's discrimination
criterion ([NOTE-1161](../notes.d/NOTE-1161.md), §8.3). The review gives no separation condition:
it ranks probe families by a utility, and so it does not answer this
question.

One decision family does have an answer. In a finite partial-monitoring
game, two outcome laws that agree on the signals of every probe in a set D
also agree on the comparison of actions i and j for every such pair iff
ℓ_i − ℓ_j lies in the span of those probes' signal row spaces
([THEORY-962](../theory.d/THEORY-962.md), from Bartók et al.). That condition can be checked
before any data. It covers pairwise comparisons only, with deterministic
or known-law signals, so the question stays Open. The question is
unchanged.

## Split, 2026-10-25 ([ADR-049](../decisions.d/ADR-049.md))

The linear case is [QUESTION-272](QUESTION-272.md), Answered. When the task's target
and the probes' outcome laws are linear in one state, a probe family
separates what the task needs exactly when the target lies in the span of
what the probes reveal: for pairwise comparisons of actions, the loss
difference in the probes' combined signal row space ([THEORY-962](../theory.d/THEORY-962.md)); for
the authority shares of a mixture of known profiles, affinely independent
profiles over the probe contexts ([CLAIM-452](../claims.d/CLAIM-452.md)). This question keeps the
rest: targets or outcome laws that are not linear in a common state,
profiles that must themselves be estimated, and probes whose availability
the organization's own choices decide.

## Note of 2026-10-26: a nonlinear case, with a known catalog

<!-- inactive-ok-file: CASE-163 — Proposed; the lab's identification runs filed 2026-10-26, cited as bearing on the remainder, not as settling it -->
<!-- inactive-ok-file: QUESTION-272 — Answered; the linear child, named to say this case is not in it -->

[CASE-163](../cases.d/CASE-163.md) is a case of the remainder: nonlinear production laws,
noisy readouts, and a catalog of four known mechanisms
(dmarx/PerspectiveLab@9f82bfd). For a fixed candidate family the
condition is the ordinary factorization one: a probe family d separates
what a target intervention a needs exactly when any two candidates with
the same law under d have the same law under a.

The case shows the collapse the question names. A complete audit pulse
leaves self-dependent production and feedback only alike, so class
accuracy is 75.0%, against 82.6% for a milder pulse. A short producer
interruption added to it separates all four (100%). For the parameters of
self-dependent production at nominal values, an audit pulse gives a local
observation Jacobian of rank 2 for three parameters, and so does a pulse
with an audit-producer interruption. Interrupting both producer teams as
well gives rank 3.

All of this is local, the catalog is given, and each probe runs on a
reset copy of the organization, so which probes are available is not the
organization's choice. The case is not linear in one state, so it is not
[QUESTION-272](QUESTION-272.md)'s. The question is unchanged and stays Open.

The lab's v2.4 and v2.5 (dmarx/PerspectiveLab@f392084
experiments/adaptive_interventions/ and adequacy_guard/) drop the reset:
probes are chosen online, within a cost ceiling, on one organization they
change. v2.5 adds alarms for when no candidate fits, scored
prequentially and calibrated on 160 in-catalog episodes for a nominal
10% familywise rate. On 120 independent in-catalog episodes they fired
13.3% and 16.7% of the time. An alarm says the catalog fits badly, not
which law is missing, and what it can see depends on the probes the
policy has already chosen. The resulting fallback helped under one
withheld law and hurt under another. So within a stipulated family, a
probe set that separates in principle is not yet one that a policy which
alters the system will reach.
