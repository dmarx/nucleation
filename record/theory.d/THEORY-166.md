---
number: 166
status: Active
formerly:
- THEORY-tmp9wyar
title: 'In the 66 Pew surveys of 2001–2011 that varied the order of two back-to-back binary questions, question order changed the answers but not the probability of giving the same answer to both, the equality a Lüders projection model predicts for any projectors; a classical model with order events can meet the same equality, so the regularity does not by itself favour quantum over classical probability'
version: 2
history:
- version: 2
  date: '2026-10-20'
  note: >-
    Narrowed and promoted, carrying out the promotion audit's decision for
    THEORY-166 (batch 048, ADR-047 v3): one study read in full, whose text
    states the result. "Survey question-order effects" becomes the 66 Pew
    surveys with nothing read out between the questions. The equality and the
    classical construction behind the negative clause are worked in a dated
    note. The promote_when moves to QUESTION-210.
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
  equality derived in [LIT-834](../literature.d/LIT-834.md): across the 66 Pew surveys of 2001-2011 that
  varied the order of two questions, question order shifts the answers
  (p = 0.0004) but not the probability that the two answers agree
  (p = 0.4625). The Lüders projection model predicts this without
  parameters, by a one-line identity. A classical model with order events
  can be built to satisfy the equality, and [LIT-264](../literature.d/LIT-264.md) shows that data meeting
  it are noncontextual, so it is evidence for a constraint on order effects,
  not for nonclassical probability or contextuality. A preregistered test
  with a constrained classical rival is [QUESTION-210](../questions.d/QUESTION-210.md).
supports:
- CLAIM-041
---

<!-- inactive-ok-file: THEORY-013 — Proposed; named as the neighbouring account this one is consistent with -->

# THEORY-166: In the 66 Pew surveys of 2001–2011 that varied the order of two back-to-back binary questions, question order changed the answers but not the probability of giving the same answer to both, the equality a Lüders projection model predicts for any projectors; a classical model with order events can meet the same equality, so the regularity does not by itself favour quantum over classical probability

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

## Note of 2026-10-20: the equality and a classical model that meets it

Worked for the promotion audit (batch 048).

**The equality.** With Lüders projectors P (A yes) and Q (B yes) and a
state S, the probability of agreeing answers in order AB is
⟨S|P Q P + (I − P)(I − Q)(I − P)|S⟩. Since P² = P,
(I − P)(I − Q)(I − P) = I − P − Q + P Q + Q P − P Q P, so the operator is
I − P − Q + P Q + Q P, which is symmetric in P and Q. The agreement
probability is therefore the same in both orders, for any projectors in
any dimension, and for density matrices by linearity.

**A classical model that meets it.** Let the order be an event O that sets
the joint distribution of answers. Take p(yes, yes | AB) = 0.4,
p(yes, no | AB) = 0.2, p(no, yes | AB) = 0, p(no, no | AB) = 0.4, and the
same table with the two discordant cells swapped for BA. Then
P(A yes) is 0.6 in one order and 0.4 in the other, an order effect, while
the agreement probability is 0.8 in both. The equality constrains which
tables occur; it does not by itself require noncommuting operations.
