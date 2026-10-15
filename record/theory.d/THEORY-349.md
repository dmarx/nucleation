---
number: 349
status: Active
formerly:
- THEORY-tmpn4mcl
title: "For binary outcomes and a fixed representation of individuals, a predictor can pass every test in a bounded class without being close to nature: outcome indistinguishability to tests that see the sampled prediction is equivalent, with stated losses, to multicalibration over a closely related class of sets, a predictor meeting it exists at size polynomial in the tests' size and the tolerance whatever nature's complexity, and learning one is as hard as weak agnostic learning of the class"
version: 1
tags:
- learning-theory
- probabilistic-modeling
date: '2026-10-15'
source:
- LIT-1068
- LIT-1052
answers:
- QUESTION-103
- QUESTION-104
summary: >-
  Dwork, Kim, Reingold, Rothblum and Yona (2021), [LIT-1068](../literature.d/LIT-1068.md), read in [NOTE-885](../notes.d/NOTE-885.md), and
  Hébert-Johnson, Kim, Reingold and Rothblum (2018), [LIT-1052](../literature.d/LIT-1052.md), read in [NOTE-879](../notes.d/NOTE-879.md).
  A predictor is outcome indistinguishable relative to a class of distinguishers
  when none can tell nature's outcomes from outcomes drawn from the predictor, up
  to ε. With no access or sample access to the predictor this is equivalent to
  multi-accuracy or multicalibration over closely related classes, and a predictor
  meeting it exists at size O(s/ε²) (O(s/α⁴γ) for multicalibration), independent of
  nature. Learning a multicalibrated predictor is equivalent to weak agnostic learning
  of the class. Adequacy here is relative to the class, the outcome and the features,
  and is not unique; it is not closeness to the truth, and the papers say nothing
  about signal detection.
extended_by:
- THEORY-354
---

# THEORY-349: For binary outcomes and a fixed representation of individuals, a predictor can pass every test in a bounded class without being close to nature: outcome indistinguishability to tests that see the sampled prediction is equivalent, with stated losses, to multicalibration over a closely related class of sets, a predictor meeting it exists at size polynomial in the tests' size and the tolerance whatever nature's complexity, and learning one is as hard as weak agnostic learning of the class

## Source

Dwork, Kim, Reingold, Rothblum and Yona (2021), [LIT-1068](../literature.d/LIT-1068.md) (arXiv 2011.13426v1),
read in [NOTE-885](../notes.d/NOTE-885.md): Definitions 2.1–2.3, Theorems 4.3 and 4.4, Algorithm 1 with
Lemma 5.1, Theorem 5.2. Hébert-Johnson, Kim, Reingold and Rothblum (2018),
[LIT-1052](../literature.d/LIT-1052.md) (arXiv 1711.08513v2), read in [NOTE-879](../notes.d/NOTE-879.md): Definitions 2.1–2.9, Algorithm
3.2, Theorems 3.10, 3.12, 4.2 and 4.4, Claim 4.3.

## What was actually shown

**The definition.** Nature is a joint distribution over individuals i and binary
outcomes; a predictor p̃ defines a model that draws i and then an outcome from
Ber(p̃_i). For a class A of distinguishers, p̃ is (A, ε)-outcome-indistinguishable
(OI) if no A in A accepts nature's samples and the model's with probabilities
more than ε apart. The quantity bounded is A's distinguishing advantage Δ_A.
Four levels differ in what A sees of p̃: nothing, the prediction for the sampled
individual, oracle queries, or its code. This document concerns the lower two.

**The equivalences ([LIT-1068](../literature.d/LIT-1068.md), Theorems 4.3, 4.4).** No-access OI against
indicators of the sets in C implies multi-accuracy on C, and multi-accuracy on
two sets per distinguisher implies no-access OI. Sample-access OI against m
distinguishers per set implies multicalibration of the rounded predictor on C,
and multicalibration on 2m sets per distinguisher implies sample-access OI. The
losses come from discretising the predictor into m bins and from exempting
light level sets: tolerances move between ε, ε/2, ε/4 and α²γ_C/m. In the
paper's words, "each notion can enforce the other, for closely related classes
C and A". Multicalibration itself ([LIT-1052](../literature.d/LIT-1052.md), Definition 2.6) asks that, within
every set S in C, individuals given about the same prediction v have true
probabilities averaging within α of v, except on an α-fraction of S.

**Existence, independent of nature.** Both papers patch a constant predictor:
while some test is violated, add a correction in its direction. Each correction
lowers squared distance to p* by a fixed amount, so the number of corrections is
bounded by the tolerance alone. Against size-s distinguishers with sample
access, an OI predictor of size O(s/ε²) exists ([LIT-1068](../literature.d/LIT-1068.md), Theorem 5.2); a
multicalibrated predictor has a circuit of size O((s + b)/α⁴γ) when the sets in C
have size-s circuits and size at least γN ([LIT-1052](../literature.d/LIT-1052.md), Theorem 3.12). [LIT-1052](../literature.d/LIT-1052.md)'s
words: "the cardinality of C is not the operative parameter". Neither bound
depends on p*, which "need not come from any realizable or learnable class of
functions".

**Finding one.** [LIT-1052](../literature.d/LIT-1052.md), Theorems 4.2 and 4.4: learning an α-multicalibrated
predictor on the large sets of C is equivalent, up to polynomial factors, to
weak agnostic learning of C. A calibration failure on a large set is a member
of C correlating with the predictor's residual on a level set (Claim 4.3). From
samples, multicalibration needs O(log|C|/α^{11/2}γ^{3/2}) of them (Theorem 2).

**What could have come out otherwise.** The theorems could have failed to hold
in both directions, or the predictor's size could have had to grow with |C| or
with nature's complexity. Neither happens at these levels. At the oracle level
the size bound does fail under hardness assumptions ([THEORY-354](THEORY-354.md)).

## What this does not say

- **That an OI predictor is close to nature.** [LIT-1068](../literature.d/LIT-1068.md): OI "does not guarantee
  statistical closeness to Nature (it need not be the case that p∗ ≈ p̃)". Only
  against all subset distinguishers does no-access OI force statistical closeness.
  Against efficient tests, p̃ ≡ 1/2 can pass where p* is deterministic, if the
  two halves are computationally indistinguishable; that case is given
  informally, not as a theorem.
- **That the adequate predictor is unique or minimal.** p* is multicalibrated for
  every C; many predictors satisfy OI for one A; the output depends on start and
  update order. Calling an OI predictor the class's sufficient partition goes
  beyond both papers.
- **That a bounded agent can find what exists cheaply.** Representation is cheap;
  learning is weak agnostic learning of C, which [LIT-1052](../literature.d/LIT-1052.md) says is hard for rich C
  under cryptographic assumptions. That consequence is asserted, not proved, there.
- **That the guarantee covers small groups.** Sets below γN, and level sets
  lighter than the exemption threshold, are not protected.
- **That the record's link to signal detection is the papers'.** Δ_A is hit rate
  minus false-alarm rate for a Boolean test only under the record's reading of
  nature's samples as signal. Neither paper uses SDT vocabulary, criteria or
  ROC curves, and [LIT-1052](../literature.d/LIT-1052.md) defines no distinguisher at all: its tests are
  first-moment checks on sets, in correlation form. The indistinguishability
  framing is [LIT-1068](../literature.d/LIT-1068.md)'s.
- **That the relativity is to the observer class alone.** The outcome is fixed and
  binary, p* is defined from the features available, and enriching the features
  enlarges the class, so a predictor "likely will no longer satisfy OI".

## Connections

- [QUESTION-103](../questions.d/QUESTION-103.md): this is the formal half the question attributed to these works;
  efficiency for a class and the criterion question are not touched.
- [QUESTION-104](../questions.d/QUESTION-104.md): a weaker class yields, by this construction, a predictor built
  from fewer, cheaper pieces, bounded in size by the class and ε. Neither paper
  has an optimal partition, so the question's main demand is not met.
- [CLAIM-302](../claims.d/CLAIM-302.md) holds that equivalence under feasible tests can be much coarser than
  statistical equivalence; this is the same structure applied to predictors.
- [CLAIM-152](../claims.d/CLAIM-152.md): the target stays fixed here; the class is a second relativity, not
  an argument for the claim's own thesis ([NOTE-885](../notes.d/NOTE-885.md)).
- [THEORY-354](THEORY-354.md) carries this to oracle access, where the cheap predictor is lost.
