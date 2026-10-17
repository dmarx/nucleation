---
number: 714
status: Proposed
formerly:
- THEORY-tmp65fz9
promote_when: >-
  A proof that I_ccs is continuous, together with a system whose
  redundancy is fixed independently of any measure's construction (by a
  mechanism both sides of the operational dispute accept, such as a shared
  bit copied to every source) on which I_ccs agrees and a rival with
  non-negative atoms does not; or an argument that settles whether unique
  information may depend on the source–source marginal, which decides
  between I_ccs and Bertschinger et al. More examples judged by intuition
  do not settle it, nor does agreement on systems where every measure
  agrees.
title: "Redundancy among any number of sources can be measured as the expected local co-information over only those events where every source, the joint source and the overlap change the target's surprisal in the same direction, under the maximum-entropy joint that preserves the source–target and joint-source marginals; this keeps symmetry, self-redundancy, subset equality and identity for independent sources, and gives up Harder et al.'s identity, monotonicity and non-negative atoms, which then read as local misinformation and mechanistic redundancy"
version: 1
tags:
- information-theory
- complex-systems
date: '2026-10-17'
source:
- LIT-1201
summary: >-
  Ince (2017), [LIT-1201](../literature.d/LIT-1201.md), read in [NOTE-968](../notes.d/NOTE-968.md). The definition and the four
  kept properties are exact, and every discrete example reproduces. That
  the dropped properties ought to be dropped, and that unique information
  depends on the source–source marginal, are argued, not proved. Proposed
  until one of those is settled. It meets Rauh et al.'s −1-bit bound
  exactly on XORCOPY.
supports:
- CLAIM-343
---

# THEORY-714: Redundancy among any number of sources can be measured as the expected local co-information over only those events where every source, the joint source and the overlap change the target's surprisal in the same direction, under the maximum-entropy joint that preserves the source–target and joint-source marginals; this keeps symmetry, self-redundancy, subset equality and identity for independent sources, and gives up Harder et al.'s identity, monotonicity and non-negative atoms, which then read as local misinformation and mechanistic redundancy

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
independent bits copied into the target share nothing.

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
