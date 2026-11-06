---
number: 555
status: Proposed
formerly:
- CLAIM-tmpzj6at
title: 'In statistical learning, the compatibility complex of the demands a training distribution presents and the singular geometry singular learning theory studies are two invariants of one object, not descriptions of two: each demand''s acceptance set is a sublevel set of its loss on the parameter space, the complex is the nerve of those sets, and the aggregate loss whose geometry fixes the learning coefficient is built from the same losses; the nerve is coarse, the learning coefficient finer, and over a fixed architecture the complex changes in training only through which configurations are accessible'
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  Two decompositions of one training objective into demands, each as
  defensible as the other, that give complexes disagreeing on whether a
  given transition is relief. The complex would then belong to a chosen
  description, not to the learning problem, and the identification with
  the problem's geometry would fail. Also defeated if a learner's
  SLT-relevant geometry is shown not to be fixed by the losses of any
  demand decomposition of its objective, so that the two share no object.
  Not defeated by two learners with the same nerve and different learning
  coefficients: the claim says the nerve is coarser.
tags:
- learning-theory
- loss-landscapes
- mathematics
date: '2026-11-04'
line:
- learned-structure
- will-organization
rests_on:
- CLAIM-347
complements:
- CLAIM-366
- CLAIM-554
uses:
- TERM-060
grounds:
- THEORY-1275
- CASE-197
- CASE-115
bears_on:
- QUESTION-127
- QUESTION-275
- QUESTION-363
- QUESTION-122
summary: >-
  The owner's U5 of the exchange "Organizational Nucleation and SLT"
  (2026-11-04), against A4's "One concerns the topology of jointly
  feasible demands; the other concerns the singular geometry and
  statistical favorability of learned parameter configurations": "I'm not
  convinced these are different things. the parameter configurations are
  responding to different demands manifested within the training data,
  which the parameters are being trained to learn to satisfy jointly." A5
  conceded and built the nerve; the reader ran its proposed test
  ([CASE-197](../cases.d/CASE-197.md)). The thesis is the owner's. The construction is A5's,
  with qualifications the reader added from the record. Proposed: the
  identification is argued, its formal core is definitional, and one model
  has been checked. The wording of the construction is A's, sharpened by
  the reader; adopting it is the owner's call.
---

# CLAIM-555: In statistical learning, the compatibility complex of the demands a training distribution presents and the singular geometry singular learning theory studies are two invariants of one object, not descriptions of two: each demand's acceptance set is a sublevel set of its loss on the parameter space, the complex is the nerve of those sets, and the aggregate loss whose geometry fixes the learning coefficient is built from the same losses; the nerve is coarse, the learning coefficient finer, and over a fixed architecture the complex changes in training only through which configurations are accessible

## The claim

**The owner's correction.** In A4 the assistant had separated two things: the
topology of jointly feasible demands ([CLAIM-347](CLAIM-347.md), [CASE-119](../cases.d/CASE-119.md)) and the singular
geometry of learned parameters ([NOTE-1462](../notes.d/NOTE-1462.md), [THEORY-1275](../theory.d/THEORY-1275.md)). The owner's U5
denies that separation: "the parameter configurations are responding to
different demands manifested within the training data, which the parameters
are being trained to learn to satisfy jointly." A5: "I think your objection
is right, and my distinction was too sharp."

**The construction (A5).** Let the training distribution present m demands,
with losses L_i(θ) ≥ 0 on the parameter space Θ.

- Demand i's acceptance set at tolerance ε_i is the sublevel set
  A_i(ε_i) = {θ : L_i(θ) ≤ ε_i}.
- The compatibility complex is 𝒦(ε) = {S : ⋂_{i∈S} A_i(ε_i) ≠ ∅}. In A5's
  words, "**This complex is exactly the nerve of the demand-satisfaction
  regions in parameter space.**"
- The aggregate L = Σ w_i L_i, with every w_i > 0, is tied to it both ways.
  L(θ) ≤ ε gives L_i(θ) ≤ ε/w_i for every i. Meeting every ε_i gives
  L(θ) ≤ Σ w_i ε_i.

The learning coefficient is read off the aggregate's sublevel volumes,
Vol{L − L_α < ε} ≍ ε^{λ_α}|log ε|^{m_α−1}. So the complex and the singular
geometry are two invariants of one family of functions on one space. They are
not invariants of two spaces that might happen to correlate.

**What separates them (A5).** "The nerve records which collections of regions
have nonempty intersections. The RLCT records fine-grained information about
how loss rises and how near-optimal parameter volume scales." A5's example
is L = θ² against L′ = θ⁶. The zero sets are the same and the sublevel sets
are both intervals, but the learning coefficients are 1/2 and 1/6. The
example has one demand, so it shows only that the coefficient is finer than
any nerve.

**Where development enters (A5).** "For a fixed architecture with fixed
demands, the full set of theoretically feasible configurations doesn't
necessarily change during training." The complex that changes is the one
restricted to what is accessible, 𝒦_t(ε) = {S : U_t ∩ ⋂_S A_i(ε_i) ≠ ∅}. That
is [CLAIM-347](CLAIM-347.md)'s complex indexed to an organization, horizon and budget,
ℛ(𝒪_t; H, B) (A38 §2 of the exchange of 2026-10-17). How accessibility
weights regions is what [THEORY-1258](../theory.d/THEORY-1258.md) leaves underived.

**An invariance the reader adds.** Nonemptiness of an intersection of sets is
preserved by any bijection of Θ. So 𝒦(ε) is unchanged by reparameterization,
and by quotienting function-preserving symmetries. This is the set-level
counterpart of [CLAIM-366](CLAIM-366.md)'s result for common descent directions, and it
answers [QUESTION-127](../questions.d/QUESTION-127.md) for this diagnosis. The learning coefficient has only
the invariance of the analytic setting.

**One model checked.** [CASE-197](../cases.d/CASE-197.md) builds the complex for the toy model of
superposition, with each feature's reconstruction loss as a demand. The
posterior's 5 → 6 transition there is relief at common tolerances from
0.0482 to 1/3. Below 0.0482 it trades five well-met demands for six less
well met. At the critical points no Betti number changes; the vertex set
does.

## What it does not say

- **That the learning coefficient is a topological invariant of the
  complex**, or that every Bayesian transition changes its Betti numbers.
  [CASE-197](../cases.d/CASE-197.md)'s transition changes none.
- **That training's demands are the network's own.** [TERM-060](../terms.d/TERM-060.md): "Ordinary
  training is the case A33 §7 named, where the objectives are the trainer's"
  (see [CLAIM-288](CLAIM-288.md)). Whose demands they are, and to which unit any frustration
  belongs, is [QUESTION-122](../questions.d/QUESTION-122.md)'s question.
- **That SGD follows the posterior.** [THEORY-1275](../theory.d/THEORY-1275.md) records a Bayesian
  transition not seen in training, and [QUESTION-363](../questions.d/QUESTION-363.md) is open.
- **That the decomposition into demands is given.** It is a choice. The
  claim is defeated if equally good choices disagree about relief.
- **That a transition which relieves frustration is self-formation.** That
  needs a capacity that persists and serves later demands of its class
  ([CLAIM-532](CLAIM-532.md), [CASE-191](../cases.d/CASE-191.md)).

## Note of 2026-11-05: the constraint-architecture readings

Mirth et al. ([NOTE-1616](../notes.d/NOTE-1616.md)), from the pasted synthesis on constraint architectures, support the claim as method: sublevel-set persistent homology tracks how one energy's sublevel sets change topology with the threshold, and it is stable, "small changes to the input produce only small changes in the persistent homology". The claim's object, the nerve of several losses' acceptance sets, is a step the paper does not take, and it mentions multi-parameter persistence only in passing. Its landscapes are molecular energies, not training losses. No status changes.

## Note of 2026-11-06: what holds it back

Every ground is now held: CASE-197 went Active in the thirtieth status
review. That case is a construction, though, and adopting it is the
owner's call: its promotion is listed for the owner's assent in that
pass's pull request. This claim is interpretive and rests on it as its
one worked instance, so it waits on that assent and is not promoted in
the same change.
