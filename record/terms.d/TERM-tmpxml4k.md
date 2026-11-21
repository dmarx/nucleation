---
status: Proposed
title: 'predictive information, or excess entropy, of a process: the mutual information between a block of its past and the adjoining block of its future, read as a function of block length'
version: 1
tags:
- information-theory
- probabilistic-modeling
- learning-theory
- complex-systems
date: '2026-11-21'
line:
- formal-apparatus
complements:
- TERM-062
draws_on:
- THEORY-756
- THEORY-087
summary: >-
  For a stationary process, I_pred(T) = I(X_{1:T}; X_{T+1:2T}), and its
  limit as T grows, the excess entropy. The exchange "Rich Get Richer
  Power Laws" uses it at A13 §5 and A21 §3–4, after Bialek, Nemenman and
  Tishby ([LIT-tmpys7v3](../literature.d/LIT-tmpys7v3.md)) and Crutchfield and Feldman ([LIT-tmpzs7sj](../literature.d/LIT-tmpzs7sj.md)), both
  unread. The record held causal states and statistical
  complexity ([TERM-062](TERM-062.md), [THEORY-756](../theory.d/THEORY-756.md)) but no word for how past–future
  information grows with the window, nor A's distinction between a
  process hard to predict because it is random and one hard to predict
  because its structure spans many scales. The conditions on unbounded
  growth (a latent quantity shared by past and future, so a non-ergodic
  mixture, or infinitely many such quantities) are the assistant's,
  filling a gap in A's turns. The wording is A's (the other assistant in
  the exchange "Rich Get Richer Power Laws", A13 and A21); adopting it is
  the owner's call.
---
<!-- inactive-ok-file: LIT-tmpys7v3 LIT-tmpzs7sj — Deferred, registered 2026-11-21 from the exchange, unread -->
<!-- inactive-ok-file: CLAIM-tmpyxiwv — filed with this term from the same exchange, Proposed -->

# TERM-tmpxml4k: predictive information, or excess entropy, of a process: the mutual information between a block of its past and the adjoining block of its future, read as a function of block length

## Definition

For a stationary process X, with H(T) the entropy of a block of T
consecutive values, the **predictive information** at window T is

  I_pred(T) = I(X_{1:T}; X_{T+1:2T}) = 2H(T) − H(2T),

which follows from the definition of mutual information and
stationarity (A21 §4). Writing H(T) = hT + H_sub(T), with h the entropy
rate, the extensive part cancels: I_pred(T) = 2H_sub(T) − H_sub(2T). "The
ordinary, irreducible randomness disappears from this expression" (A21
§4). The **excess entropy** E = I(past; future) is its limit as T → ∞,
finite or not (A13 §5).

Three regimes of growth (A21 §4, after Bialek, Nemenman and Tishby,
[LIT-tmpys7v3](../literature.d/LIT-tmpys7v3.md), unread): bounded, as for a finite-state process; c log T, as
for a model with finitely many parameters learned from the data; and
c T^μ with 0 < μ < 1, as in some nonparametric problems. A's own caveat:
"these regimes are not a one-to-one classification of physical
criticality".

The distinction A13 §5 draws with it, which the term exists to keep:
"**A system can be hard to predict because it is random, or hard to
predict because its relevant structure extends across many scales.**"
The first is high entropy rate with little predictive information; the
second is predictive information that keeps growing with the window.

## Conditions (the assistant's)

A13 §5 says that "in some scale-free processes, the amount of predictive
information contained in an observation window can continue growing
without approaching a finite limit", and gives no condition. It needs
one. For a stationary ergodic process with finitely many hidden states,
I_pred(T) is bounded by the entropy of the causal states ([THEORY-756](../theory.d/THEORY-756.md),
[TERM-062](TERM-062.md)). Unbounded growth comes from one of two sources:

1. **A quantity shared by past and future that the data keep refining.**
   A21 §3's coin of unknown bias θ, uniform prior, has
   I_pred(T) = ½ log₂ T + O(1). The process is an exchangeable mixture of
   i.i.d. processes and is **not ergodic**: each realization has its own
   θ, and the information past and future share is information about θ.
   For a known θ it is zero, which A21 §3 notes. When past and future are
   independent given θ, I_pred(T) = 2G(T) − G(2T) with
   G(T) = I(θ; X_{1:T}), so the growth is set by how fast the data learn
   θ ([CLAIM-tmpyxiwv](../claims.d/CLAIM-tmpyxiwv.md)).
2. **Infinitely many such quantities, or long memory.** Power-law growth
   needs the number of resolvable quantities to grow with T ([CLAIM-tmpyxiwv](../claims.d/CLAIM-tmpyxiwv.md)
   gives a case), or a long-range dependent process, such as fractional
   Gaussian noise with Hurst exponent H > ½, whose covariances are not
   summable; neither is implied by a power-law correlation alone.

The assistant checked the coin's growth exactly, summing over head counts
under the Beta(1,1) mixture: 2H(T) − H(2T) minus ½ log₂ T is −0.85,
−1.07, −1.10, −1.104 and −1.104 bits at T = 10, 10², 10³, 10⁴ and 10⁵,
so the O(1) term settles at about −1.10 bits (a numpy script of this
session, not kept; the method is as stated).

## What it is not

- **Not entropy.** A million fair coin flips have a million bits of
  entropy and zero predictive information (A13 §1, §5).
- **Not statistical complexity.** The entropy of the causal states bounds
  the excess entropy from above and can exceed it ([THEORY-756](../theory.d/THEORY-756.md)); the two
  are equal only for some processes.
- **Not transfer entropy** ([TERM-057](TERM-057.md)), which conditions on a target's own
  past and is directed between two processes.
- **Not a sign of criticality.** Logarithmic growth needs no transition,
  and a critical system need not have divergent predictive information
  under every observation (A21 §4).

## Sources

Bialek, Nemenman and Tishby 2001 ([LIT-tmpys7v3](../literature.d/LIT-tmpys7v3.md)) and Crutchfield and
Feldman 2003 ([LIT-tmpzs7sj](../literature.d/LIT-tmpzs7sj.md)), both Deferred and unread. The relation to
parameter count (½ log T per parameter) is the same coefficient the record
holds as the Bayesian Occam penalty ([THEORY-087](../theory.d/THEORY-087.md)).
