---
number: 163
status: Active
formerly:
- THEORY-tmp64mn6
title: "In Zaslavsky, Kemp, Regier and Tishby's analysis, the colour-naming systems of the World Color Survey languages and English lie near the information-bottleneck bound for compressing perceptual meanings into words, at a trade-off parameter just above 1 and nearer than hue-rotated variants of themselves, with the need distribution over meanings estimated from the naming data"
version: 2
history:
- version: 2
  date: '2026-10-20'
  note: >-
    Narrowed and promoted, carrying out the promotion audit's decision for
    THEORY-163 (batch 047, ADR-047 v3): one study read through its main
    text, figure legends and Table 1, whose text and table state the results
    the title uses. "The world's languages" becomes the World Color Survey
    languages and English, and the title names the source estimated from the
    naming data. The promote_when moves to QUESTION-tmphu7q4.
tags:
- linguistics
- information-theory
- cognition
date: '2026-10-09'
source:
- LIT-810
- LIT-338
summary: >-
  Zaslavsky, Kemp, Regier & Tishby (2018), [LIT-810](../literature.d/LIT-810.md), read in
  [NOTE-631](../notes.d/NOTE-631.md): treating a colour lexicon as an encoder from Gaussian
  perceptual meanings to words, the World Color Survey languages and
  English lie near the IB curve of [LIT-338](../literature.d/LIT-338.md) at β ≈ 1.03, beat hue-rotated
  variants of themselves, and their soft, partly inconsistent naming is
  what IB optima look like. It does not show that languages are driven to
  the bound by any process, and the need distribution that makes the fit
  best is estimated from the naming data themselves.
supports:
- CLAIM-092
---

# THEORY-163: In Zaslavsky, Kemp, Regier and Tishby's analysis, the colour-naming systems of the World Color Survey languages and English lie near the information-bottleneck bound for compressing perceptual meanings into words, at a trade-off parameter just above 1 and nearer than hue-rotated variants of themselves, with the need distribution over meanings estimated from the naming data

## Source

- Zaslavsky, Kemp, Regier & Tishby (2018), [LIT-810](../literature.d/LIT-810.md), read in
  [NOTE-631](../notes.d/NOTE-631.md): Eqs. 1–7, Fig. 3, Table 1, the rotation control, Fig. 5.
- Tishby, Pereira & Bialek (1999), [LIT-338](../literature.d/LIT-338.md), read in [NOTE-300](../notes.d/NOTE-300.md): the
  objective and its self-consistent solution.

## The claim

Let a language's colour lexicon be a naming policy q(w|m) from meanings m
(distributions over colours, one per World Color Survey chip) to words,
with a Bayesian listener reconstructing m̂_w. Score it by complexity
I(M;W) and accuracy I(W;U). Then the attested systems of the WCS languages
and of English lie close to the information-bottleneck curve, the set of
minimizers of I(M;W) − β I(W;U), each at a β only slightly above 1, and
closer to it than systematically rotated versions of themselves. Because
optima at finite β are stochastic, graded category membership and regions
named inconsistently across speakers are properties of efficient systems.

## What was actually shown

Each language was fitted to the β at which it is closest to optimal, and
its distance measured (ε_l = 0.18 with the LI source, held-out languages).
This could have failed in three ways, and did not: the languages could
have been far from the curve at every β; their full naming distributions
could have matched the IB encoders no better than a deterministic
efficiency model (gNID 0.18 for IB against 0.47 for RKK+); and rotated
variants, which keep each system's complexity profile but misplace it in
colour space, could have done as well (93% of languages beat all 39 of
their own). The yellow category IB predicts at the lowest complexities is
not in the data, a stated failure.

## What this does not say

- **Not that a drive to efficiency produced these systems.** Near the
  bound is a property of the end states; no transmission or learning
  process was modelled, and the "evolution" is the path of optima through
  β, compared with Berlin and Kay's stages by eye. How a population would
  reach the bound is open; iterated learning ([THEORY-155](THEORY-155.md)) is a theory of
  where transmission goes, and the two have not been joined.
- **Not that the bound is fitted without help.** The need distribution
  that gives the best fit is built from the naming data, averaged and
  cross-validated over languages; with a uniform source the fit is worse
  (gNID 0.39).
- **Not that any lexicon in any domain is IB-efficient.** The result is
  for colour, with a fixed CIELAB perceptual model; other domains are the
  authors' future work.
- **Not that I(W;U) is the right notion of accuracy for communication in
  general.** It follows from taking KL as the distortion between
  meanings, which is one choice of loss.
