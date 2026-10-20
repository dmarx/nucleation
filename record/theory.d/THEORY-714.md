---
number: 714
status: Active
formerly:
- THEORY-tmp65fz9
title: "Ince's I_ccs, the expected local co-information over only those events where every source, the joint source and the overlap change the target's surprisal in the same direction, under the maximum-entropy joint that preserves the source–target and joint-source marginals, is symmetric and self-redundant and satisfies the independent identity property; it fails Harder et al.'s identity and monotonicity, so its atoms can be negative, and, though its paper says otherwise, it fails subset equality"
version: 2
history:
- version: 2
  date: '2026-10-20'
  note: >-
    Corrected and promoted, carrying out the promotion audit's decision
    for THEORY-714 (batch 056, ADR-047 v2). The definition and its
    properties were re-derived from the paper. Subset equality fails:
    Ince's proof cancels the co-information terms but not the sign
    condition, which still compares a source with one containing it,
    and a two-source counterexample gives 0.0272 bit against 0.0073.
    The title now says so, and no longer claims I_ccs is the right
    measure or reads its negative atoms. That question, the former
    promote_when, moves to QUESTION-223.
tags:
- information-theory
- complex-systems
date: '2026-10-17'
source:
- LIT-1201
summary: >-
  Ince (2017), [LIT-1201](../literature.d/LIT-1201.md), read in [NOTE-968](../notes.d/NOTE-968.md). The definition is exact, and three of
  the four properties the paper claims hold; subset equality does not
  (re-derived 2026-10-20), and every discrete example reproduces. That
  the dropped properties ought to be dropped, and that unique information
  depends on the source–source marginal, are argued, not proved. Whether it is
  the right redundancy measure is open (QUESTION-223). It meets Rauh et al.'s −1-bit bound
  exactly on XORCOPY.
supports:
- CLAIM-343
---

# THEORY-714: Ince's I_ccs, the expected local co-information over only those events where every source, the joint source and the overlap change the target's surprisal in the same direction, under the maximum-entropy joint that preserves the source–target and joint-source marginals, is symmetric and self-redundant and satisfies the independent identity property; it fails Harder et al.'s identity and monotonicity, so its atoms can be negative, and, though its paper says otherwise, it fails subset equality

## Source

Ince (2017), "Measuring multivariate redundant information with pointwise
common change in surprisal", *Entropy* 19(7): 318, arXiv 1602.05063v3,
[LIT-1201](../literature.d/LIT-1201.md), read in [NOTE-968](../notes.d/NOTE-968.md): definitions, properties and
examples in full, the Gaussian section and discussion at lower resolution.

## What was actually shown

**The measure.** Under P̂, the maximum-entropy joint with every Q(Ai, S)
and Q(A1…An) fixed, I_ccs is the expectation of the local co-information
on events where all local informations and the co-information share a
sign, and zero elsewhere (Defs. 4.1–4.2).

**Properties proved (§4.4).** Symmetry, self-redundancy and subset equality,
so the lattice can be used; the independent identity property, so two
independent bits copied into the target share nothing. The subset-equality
proof does not hold: it cancels the co-information terms but not the sign
rule (Note of 2026-10-20).

**Properties that fail.** Harder et al.'s identity, whenever there are
negative local information terms. Monotonicity, by Table 7: redundancy
0.77 bit exceeds I(S; X2) = 0.61, giving unique information −0.16. Hence
non-negative atoms.

**Examples, recomputed.** REDUCEDOR 0/0.31/0.31/0.38; SUM 0/0.5/0.5/0.5; AND
0.104/0.208/0.208/0.293; XORCOPY with {12}{13}{23} = −1; DBLXOR with
{123} = −1; giant bit, parity and XORUNQ as built ([NOTE-968](../notes.d/NOTE-968.md)).

What could have come out otherwise: on XORCOPY the measure could have
violated independent identity to keep the atoms non-negative, as I_min
does. It takes the negative atom instead, exactly at the bound
[THEORY-713](THEORY-713.md) proves.

## What this does not say

- **That negative atoms are meaningful.** "Misinformation" and "mechanistic
  redundancy" are readings the paper offers, not results.
- **That I_broja is wrong.** The REDUCEDOR game shows that a game-theoretic
  operationalisation of unique information disagrees with the
  decision-theoretic one ([THEORY-705](THEORY-705.md)). Which one is right is not shown.
- **That I_ccs is continuous.** Conjectured, and checked only locally in
  the examples.
- **That it is the redundancy ΦID uses.** The ΦID work held here uses the
  minimum-mutual-information redundancy ([NOTE-799](../notes.d/NOTE-799.md)).

## Connections

- [THEORY-713](THEORY-713.md) proves that some axiom must go once there are three
  sources. I_ccs is the measure that gives up non-negativity and keeps an
  independent-sources identity.
- [CLAIM-335](../claims.d/CLAIM-335.md)'s examples and [THEORY-712](THEORY-712.md)'s coupled pair keep their values
  under I_ccs. Harder et al.'s bystander example ([THEORY-708](THEORY-708.md)) gets a third
  split, with a negative unique atom at d = 0.25 ([NOTE-968](../notes.d/NOTE-968.md)).
- [THEORY-706](THEORY-706.md) (I_min) and [THEORY-708](THEORY-708.md) (I_red) are the measures it argues
  against on the two-bit copy and on identity respectively.

## Note of 2026-10-20: the properties re-derived, and subset equality

The promotion audit re-derived each property from Definitions 4.1–4.2 of
the paper. Write i(x; s) = log p(s|x)/p(s) and c for the local
co-information, all under P̂. I_ccs keeps an event only when every
source's i, the joint source's i and c share a sign.

- **Symmetry.** c, the sign rule and P̂'s constraints are all invariant
  under permuting the sources.
- **Self-redundancy.** For one source c = i(a; s), the sign rule is met
  trivially, and P̂ preserves Q(A, S), so I_ccs = I(S; A).
- **Independent identity.** For S = (A1, A2) with I(A1; A2) = 0, every
  admissible joint is supported on s = (a1, a2), so P̂ = P. Then
  i(a1; s) + i(a2; s) = i(a1a2; s) pointwise, c = 0 and I_ccs = 0.
- **Harder et al.'s identity fails.** For the same target with dependent
  sources, c = i(a1; a2), the local mutual information, while all three
  local informations are non-negative. Events with negative local mutual
  information drop out, so I_ccs = Σ p max(i(a1; a2), 0) ≥ I(A1; A2).
  For p(a1, a2) = (0.4, 0.1; 0.2, 0.3) that is 0.3415 bit against
  0.1245.
- **Monotonicity fails.** Table 7 recomputes to I_ccs = 0.7685 bit against
  I(S; X2) = 0.6100, a unique atom of −0.1585.
- **Subset equality fails.** The paper's proof (§4.4, Eqs. 39–41) shows
  the co-information cancels when A_{l−1} ⊆ A_l, which is right. But the
  sign rule still requires sgn i(a_{l−1}; s) = sgn i(a_l; s), and a
  coarse and a fine source can disagree. Take A1 = X1 and
  A2 = (X1, X2) with p(x1, x2, s) ∝ (0,0,0) 0.2, (0,0,1) 0.05,
  (0,1,0) 0.05, (0,1,1) 0.2, (1,0,0) 0.3, (1,0,1) 0.2. Here P̂ = P,
  because A2 determines A1. The events (0,0,0) and (0,0,1) drop out
  (i(x1; s) = −0.138 against i(x1x2; s) = +0.541, and +0.152 against
  −1.170). So I_ccs({1}{12}) = 0.0272 bit, while I_ccs({1}) =
  I(S; X1) = 0.0073 bit.

The recipe, kept in the audit's decision file, fits P̂ by iterative
proportional fitting from the uniform distribution. Every number above
was recomputed with it.

Subset equality is the property Ince argues licenses restricting the
redundancy function to the lattice's antichains, so its failure bears on
the measure's rationale. It leaves the lattice computation and every
value in the record (the −1-bit XORCOPY atom, the examples above, the
values [CLAIM-343](../claims.d/CLAIM-343.md) and [THEORY-712](THEORY-712.md) use) unchanged. Whether a modified sign
rule could restore the property is [QUESTION-223](../questions.d/QUESTION-223.md).
