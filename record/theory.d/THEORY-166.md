---
number: 166
status: Proposed
formerly:
- THEORY-tmp9wyar
promote_when: >-
  A test of the equality on question pairs chosen before the data were
  seen, by investigators other than its proposers, with the per-pair
  tables published, and a comparison against a classical model with
  memory that is constrained to satisfy the same equality and fitted to
  the same tables. Re-analyses of the same 72 studies cannot settle it,
  and neither can a fit of the quantum model alone.
title: 'Survey question-order effects leave the probability of giving the same answer to both questions unchanged, as a projection model predicts, and this regularity does not by itself favour quantum over classical probability'
version: 1
tags:
- cognition
- social-science
- probabilistic-modeling
date: '2026-10-09'
source:
- LIT-795
- LIT-834
- LIT-264
summary: >-
  Wang, Solloway, Shiffrin & Busemeyer (2014), [LIT-795](../literature.d/LIT-795.md), on the QQ
  equality derived in [LIT-834](../literature.d/LIT-834.md): across 66 unselected Pew surveys,
  question order shifts the answers (p = 0.0004) but not the probability
  that the two answers agree (p = 0.4625). The Lüders projection model
  predicts this without parameters. The authors concede that a classical
  model can be built to satisfy the equality, and [LIT-264](../literature.d/LIT-264.md) shows that data
  meeting it are noncontextual, so it is evidence for a constraint on
  order effects, not for nonclassical probability or contextuality.
supports:
- CLAIM-041
---

<!-- inactive-ok-file: THEORY-013 — Proposed; named as the neighbouring account this one is consistent with -->

# THEORY-166: Survey question-order effects leave the probability of giving the same answer to both questions unchanged, as a projection model predicts, and this regularity does not by itself favour quantum over classical probability

## Source

Wang, Solloway, Shiffrin & Busemeyer (2014), [LIT-795](../literature.d/LIT-795.md), main text.
The derivation is Wang & Busemeyer (2013), [LIT-834](../literature.d/LIT-834.md), Appendix.
Dzhafarov, Zhang & Kujala (2015), [LIT-264](../literature.d/LIT-264.md), §3 and supplementary table S1,
for the re-derivation and the contextuality analysis.

## What was actually shown

Ask two yes/no questions in both orders to two random halves of a sample.
If each answer is a Lüders projection of one belief state (or one density
matrix), then p(same answers) in order AB equals p(same answers) in order
BA, for any projectors in any dimension. The reason is that
P Q P + (I − P)(I − Q)(I − P) = I − (P + Q) + (P Q + Q P) is symmetric in
P and Q ([LIT-264](../literature.d/LIT-264.md) §3); equivalently, Re⟨S|P Q|S⟩ = Re⟨S|Q P|S⟩
([LIT-834](../literature.d/LIT-834.md), Appendix). The prediction could have failed. Possible
context-effect tables fill a three-dimensional pyramid, and the equality
picks out a plane in it. It did fail where the conditions were broken:
in the Rose–Jackson poll, background information was read out before each
question, and q = 0.1514 (χ²(1) = 28.57).

On 66 Pew surveys, which were every Pew survey of 2001–2011 that varied
the order of two questions, the distribution of order-effect χ² values
departs from the null (p = 0.0004) and that of the q values does not
(p = 0.4625). Across 72 studies, paired context effects lie along the
predicted line of slope −1 (r = −0.82). [LIT-264](../literature.d/LIT-264.md)'s recomputation from the
authors' data agrees: summing the 72 one-degree-of-freedom χ² values in
its table S1 (excluding Rose–Jackson) gives 76.04, p ≈ 0.35. Two
individual pairs reject the equality at 0.05 (one Pew pair at p = 0.008,
one study at about p = 0.02), about what 72 tests would produce by
chance.

## What this does not say

- **That human judgment is quantum.** The equality follows from a
  symmetry of self-adjoint projectors under one update rule. Wang et al.
  concede that "it is possible to construct a model that is narrowly
  constrained to satisfy the QQ equality" and ask for alternatives. The
  case against Bayesian and Markov models in [LIT-834](../literature.d/LIT-834.md) §6 is informal,
  and its Markov proof is withheld. What is shown is that unconstrained
  classical models need not produce the regularity, not that none can.
- **That the data are contextual.** The opposite holds. The QQ equality
  makes the Contextuality-by-Default criterion for these rank-2 systems
  hold automatically ([LIT-264](../literature.d/LIT-264.md) §3). Data that confirm the quantum model
  here are noncontextual data. That is consistent with [THEORY-013](THEORY-013.md), which
  this account narrows to one paradigm and gives its mechanism.
- **That order effects establish noncommuting operations of any
  particular kind.** Within the model, non-commuting projectors are
  necessary for order effects. But the order effect alone does not pick
  out the model: the 2013 paper itself notes that a Bayesian model with
  order events and a Markov model with memory produce order effects too.
  The equality is the part of the evidence that discriminates.
- **Anything outside back-to-back binary survey questions.** Inserted
  information breaks the prediction, the tests are on US surveys (mostly
  one organisation's), and the regularity is uninformative where order
  effects are small.
