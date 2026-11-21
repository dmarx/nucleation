---
status: Open
title: 'What fixes the exponent a given mechanism for a power law produces: geometry, dimension, a balance of growth against loss, or the distribution of an underlying parameter?'
version: 1
tags:
- probabilistic-modeling
- complex-systems
date: '2026-11-21'
line:
- formal-apparatus
summary: >-
  A's, from the close of A5 of the exchange "Rich Get Richer Power Laws"
  (2026-11-20): "A particularly important next question is **whether
  there are universal principles that determine which of these mechanisms
  produces which exponent**. Some exponents are determined by geometry,
  some by dimensionality, some by the balance of growth and extinction,
  and others by the distribution of underlying parameters." A raised it
  and left it. The section "A partial pattern" is the assistant's
  (Claude, in this session), checked with python3 -I. The wording is A's
  (the other assistant in the exchange "Rich Get Richer Power Laws", A5);
  adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-tmp1dlyp CLAIM-tmply70l CLAIM-tmpiervv CLAIM-tmpdusls CLAIM-tmp8h6nt CLAIM-769 THEORY-2141 THEORY-tmp23821 — Proposed or new; claims filed from the same exchange and held claims and readings that give exponents -->

# QUESTION-tmp21jtb: What fixes the exponent a given mechanism for a power law produces: geometry, dimension, a balance of growth against loss, or the distribution of an underlying parameter?

## The question

A5 lists ten mechanisms ([CLAIM-tmp1dlyp](../claims.d/CLAIM-tmp1dlyp.md)) and ends: "Some exponents are
determined by geometry, some by dimensionality, some by the balance of
growth and extinction, and others by the distribution of underlying
parameters. That is where the study of power laws connects to
universality classes, renormalization, stochastic-process theory, and the
deeper mathematics of complex systems." Is there a principle, or only a
list? And can the exponent tell the mechanisms apart, which
[CLAIM-tmp8h6nt](../claims.d/CLAIM-tmp8h6nt.md) doubts?

## A partial pattern (the assistant's)

In every mechanism the exchange works out, the survival exponent is a
ratio of two rates or two dimensions:

| mechanism | survival exponent | ratio of |
|---|---|---|
| growth with a spread of ages (Reed) | λ/g | exit or entry rate over growth rate |
| linear attachment ([CLAIM-tmply70l](../claims.d/CLAIM-tmply70l.md)) | 1/(1/2) = 2 | entry rate over growth rate, in log time |
| Kesten ([CLAIM-tmpiervv](../claims.d/CLAIM-tmpiervv.md)) | κ with E[A^κ] = 1; −2μ/σ² for lognormal A | drift over diffusion of log W |
| gamma mixture of rates | a | the shape of the spread of rates |
| geometry, influence r^(−β) | d/β | dimension over decay exponent |
| critical cascade, first passage ([CLAIM-tmpdusls](../claims.d/CLAIM-tmpdusls.md)) | 1/2 | diffusion's square root, after the cycle lemma's 1 |
| rate tree ([CLAIM-769](../claims.d/CLAIM-769.md), [THEORY-2141](../theory.d/THEORY-2141.md)) | ln b/(ln(1/g) − ln b) | log branching over log rate ratio |

Each is the exponent at which a growth term exactly offsets a loss term.
The clearest case is Kesten, where κ solves E[A^κ] = 1: κ is the moment at
which multiplicative growth just balances. The hazard form A's reasoning
noted ("a hazard proportional to 1/x produces power-law survival") is the
same thing: h(x) = α/x, and α is the ratio. Every entry in the table was
checked in this session or in the entry cited.

That is a pattern, not an answer. It says what kind of number an exponent
is in these models, not why a given system has the ratio it has, and it
does not cover the exponents of interacting critical systems (τ = 187/91
in 2D percolation), which come from a renormalization fixed point, the
criticality theme's question.

## What would answer it

A derivation showing that a broad class of mechanisms gives tail
exponents as the root of a balance equation, as Kesten's does, with the
class's boundary stated. Or a counterexample: a non-critical mechanism
whose exponent is not such a root.

## Note of 2026-11-21: Mitzenmacher, read

Mitzenmacher's review (LIT-tmpwdtfj, read in NOTE-tmp0rhkc; the reading is
THEORY-tmp23821) **bears on** the question with three exponent formulas,
each a balance, which is evidence for the partial pattern above:

- preferential attachment with a uniform share α: density exponent
  (2 − α)/(1 − α), set by the mix of uniform and proportional choice (§3);
- a lognormal stopped at an exponential time of rate λ: 1 + √(2λ), set by
  the stopping rate against the variance (§7);
- Champernowne's floor: the cumulative exponent is 1, the root of
  (2/3)·2^(−κ) + (1/3)·2^κ = 1 from the up and down probabilities, though
  the paper does not write the equation (§5.1).

None is a counterexample of the kind "What would answer it" asks for. The
second is also a root of a balance, though the paper does not put it so:
κ = √(2λ) solves κ²/2 = λ, the growth rate of E[X_t^κ] for the
zero-drift log-walk set equal to the stopping rate (the filer's
reading, from the paper's integral). THEORY-tmp23821 `bears_on`
this question.
