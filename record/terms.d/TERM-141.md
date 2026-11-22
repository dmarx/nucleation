---
number: 141
status: Proposed
formerly:
- TERM-tmpxml4k
title: 'predictive information, or excess entropy, of a process: the mutual information between a block of its past and the adjoining block of its future, read as a function of block length'
version: 2
history:
- version: 2
  date: '2026-11-22'
  note: >-
    Revised in place after the reading of Crutchfield and Feldman
    (LIT-3010, NOTE-tmpe86ty; THEORY-tmpl7rgc, which the term now
    draws_on). The definition gains their identities and the bound
    E′(L) ≤ E(L) ≤ E (Lemma 3), of which this term's I_pred(T) is the
    left side at L = 2T; condition 2 gains the Thue–Morse case,
    logarithmic growth with no parameters, checked by the assistant;
    "What it is not" gains that excess entropy is not the measure of a
    process's structure, which the exchange's use of the work overstated.
    The sentences calling the work unread are replaced. The title and the
    status are unchanged.
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
- THEORY-2151
- THEORY-tmpl7rgc
summary: >-
  For a stationary process, I_pred(T) = I(X_{1:T}; X_{T+1:2T}), and its
  limit as T grows, the excess entropy. The exchange "Rich Get Richer
  Power Laws" uses it at A13 §5 and A21 §3–4, after Bialek, Nemenman and
  Tishby (LIT-3008, read on 2026-11-21 as THEORY-2151) and
  Crutchfield and Feldman (LIT-3010, read on 2026-11-22 as
  THEORY-tmpl7rgc). The record held causal states and statistical
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
<!-- inactive-ok-file: THEORY-tmpl7rgc — Proposed or new; the reading of Crutchfield and Feldman, 2026-11-22 -->
<!-- inactive-ok-file: CLAIM-849 — filed with this term from the same exchange, Proposed -->
<!-- inactive-ok-file: ARG-152 CLAIM-805 THEORY-2151 — Proposed or Rejected entries filed on 2026-11-21 from the exchange "Rich Get Richer Power Laws" and from the readings of its works, or Deferred works not yet read -->

# TERM-141: predictive information, or excess entropy, of a process: the mutual information between a block of its past and the adjoining block of its future, read as a function of block length

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

**Crutchfield and Feldman's identities and bound** ([THEORY-tmpl7rgc](../theory.d/THEORY-tmpl7rgc.md); added
2026-11-22, version 2). With hµ(L) = H(L) − H(L−1), the excess entropy is
E = Σ_L [hµ(L) − hµ], and they show it equals the subextensive part of the
block entropy, E = lim [H(L) − hµL] (Prop. 7), and, when the limit exists,
the mutual information between the semi-infinite past and future
(Prop. 8). Of two finite-L estimates, E(L) = H(L) − L hµ(L) (Eq. 60) and
E′(L) = I between the two halves of an L-block = 2H(L/2) − H(L) (Eq. 61),
"E′(L) ≤ E(L) ≤ E" (Lemma 3). This term's I_pred(T) is E′(2T): at every
window it is a lower bound on E, and a worse estimate of it than E(2T).

Three regimes of growth (A21 §4, after Bialek, Nemenman and Tishby,
[LIT-3008](../literature.d/LIT-3008.md), read; [THEORY-2151](../theory.d/THEORY-2151.md)): bounded, as for a finite-state process; c log T, as
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
   θ ([CLAIM-849](../claims.d/CLAIM-849.md)).
2. **Infinitely many such quantities, or long memory.** Power-law growth
   needs the number of resolvable quantities to grow with T ([CLAIM-849](../claims.d/CLAIM-849.md)
   gives a case), or a long-range dependent process, such as fractional
   Gaussian noise with Hurst exponent H > ½, whose covariances are not
   summable; neither is implied by a power-law correlation alone.
   **Logarithmic growth with no parameters** belongs here, not under
   condition 1 (added 2026-11-22, version 2). The Thue–Morse sequence is
   deterministic, aperiodic, of zero entropy rate, and has no finite-state
   generator ("there is no finite-state process that can generate the
   Thue-Morse sequence"); yet "the excess entropy diverges; E(L) ∝ log2 L,
   indicating an infinite-memory process" (Crutchfield and Feldman §VI,
   [LIT-3010](../literature.d/LIT-3010.md)). There is no θ to learn and no mixture: the Thue–Morse shift
   is uniquely ergodic (a standard fact, not stated in the paper). So
   logarithmic growth has at least two sources, finitely many unknown
   parameters (condition 1, non-ergodic) and aperiodic, infinite-state
   order (condition 2, ergodic), and is not by itself a sign of the first.
   The assistant checked the term's own quantity on a 2²¹-symbol prefix of
   the sequence with `python3 -I`: 2H(T) − H(2T) is 0.59, 2.09, 3.34, 4.46
   and 5.52 bits at T = 2, 4, 8, 16 and 32, about 1.1 bits per doubling of
   T, logarithmic growth like the coin's but with no parameter (scratchpad
   script `tm.py`, not kept).

The assistant checked the coin's growth exactly, summing over head counts
under the Beta(1,1) mixture: 2H(T) − H(2T) minus ½ log₂ T is −0.85,
−1.07, −1.10, −1.104 and −1.104 bits at T = 10, 10², 10³, 10⁴ and 10⁵,
so the O(1) term settles at about −1.10 bits (a numpy script of this
session, not kept; the method is as stated).

## What it is not

- **Not entropy.** A million fair coin flips have a million bits of
  entropy and zero predictive information (A13 §1, §5); Crutchfield and
  Feldman's IID processes have E = 0 at any entropy rate.
- **Not the measure of a process's structure** (added 2026-11-22,
  version 2). The exchange invoked Crutchfield and Feldman for "excess
  entropy as the measure of a process's stored structure", and that
  overstates them. They call E "a measure of one kind of memory", and show
  it missing structure twice: three period-5 processes share E = log2 5
  and have transient information T = 4.073, 5.273 and 4.873 bit-symbols
  ("The transient information measures a structural property of the
  system — a property not captured by the excess entropy E"); and their
  simple nondeterministic source has E ≈ 0.147 bits while its optimal
  deterministic predictor has "an infinite number of states", so "relying
  only on information theoretic quantities, one is misled as to the
  process's actual complexity". They assign structure proper to
  computational mechanics: "specifying how this memory is organized
  cannot be done within the framework of information theory". The record
  holds the same lesson from Shalizi and Crutchfield ([NOTE-1372](../notes.d/NOTE-1372.md): excess
  entropy a lower bound on stored memory, not a measure of it).
- **Not statistical complexity.** The entropy of the causal states bounds
  the excess entropy from above and can exceed it ([THEORY-756](../theory.d/THEORY-756.md)); the two
  are equal only for some processes. The simple nondeterministic source
  above, with finite E and infinitely many causal states, is a case.
- **Not transfer entropy** ([TERM-057](TERM-057.md)), which conditions on a target's own
  past and is directed between two processes.
- **Not a sign of criticality.** Logarithmic growth needs no transition,
  and a critical system need not have divergent predictive information
  under every observation (A21 §4).

## Sources

Bialek, Nemenman and Tishby 2001 ([LIT-3008](../literature.d/LIT-3008.md), read on 2026-11-21 in
[NOTE-2243](../notes.d/NOTE-2243.md)) and Crutchfield and Feldman 2003 ([LIT-3010](../literature.d/LIT-3010.md), read on
2026-11-22 in [NOTE-tmpe86ty](../notes.d/NOTE-tmpe86ty.md)). The relation to
parameter count (½ log T per parameter) is the same coefficient the record
holds as the Bayesian Occam penalty ([THEORY-087](../theory.d/THEORY-087.md)).

## Note of 2026-11-21: Bialek, Nemenman & Tishby, read

Read in [NOTE-2243](../notes.d/NOTE-2243.md) ([THEORY-2151](../theory.d/THEORY-2151.md)). It supports the term's regimes,
its distinction and its condition 1, and differs from it in one
convention.

- **The future is infinite in the paper.** Its headline
  I_pred(T) = lim_{T′→∞} I_pred(T, T′) = S₁(T), the subextensive entropy (Eq.
  9); this term's I_pred(T) = I(X_{1:T}; X_{T+1:2T}) is the paper's Eq. 6 with
  T′ = T, a case it covers and does not feature. The regimes and the
  logarithmic coefficient are the same under both: S₁ = (K/2) log T gives
  (K/2) log(T/2) here. For power-law growth S₁ = cT^μ the term's quantity is
  2S₁(T) − S₁(2T) = (2 − 2^μ)cT^μ, a constant factor smaller.
- **The regimes are theirs:** "it may either stay finite, or grow to
  infinity together with T; in the latter case the rate of growth may be
  slow (logarithmic) or fast (sublinear power)" (§3).
- **The distinction is theirs too:** a complexity measure "should be zero
  both for purely regular and for purely random systems" (§5); entropy's
  extensive part cancels.
- **Condition 1** is the paper's own setting: parameters drawn once and
  fixed (Eq. 21), and the data–parameter information equal to I_pred.
  **Condition 2** is in the paper as K*, predictability from intrinsic
  long-range correlations, which "the subextensive entropy makes no
  distinction" from unknown parameters (Eq. 69).
- **"Not a sign of criticality."** The paper leans the other way, asserting
  without proof that predictive information diverges at critical points
  (§6, fn. 9); A's caveat stays A's ([CLAIM-805](../claims.d/CLAIM-805.md), [ARG-152](../arguments.d/ARG-152.md)).

## Note of 2026-11-22: Crutchfield and Feldman, read

Read in [NOTE-tmpe86ty](../notes.d/NOTE-tmpe86ty.md) ([THEORY-tmpl7rgc](../theory.d/THEORY-tmpl7rgc.md), which this term now `draws_on`).
It **supports the definition and its identities, adds a bound, and
qualifies the regimes**; the revisions are made in place above
(version 2).

- **Supports:** E = lim [H(L) − hµL] (Prop. 7) and E = I(past; future)
  (Prop. 8); "Not entropy" (IID processes have E = 0).
- **Adds:** E′(L) ≤ E(L) ≤ E (Lemma 3), with this term's I_pred(T) =
  E′(2T).
- **Qualifies the regimes:** logarithmic growth also comes from
  Thue–Morse, deterministic and parameter-free, under condition 2 rather
  than condition 1.
- **Corrects the exchange's use of the work:** excess entropy is "one kind
  of memory", not the measure of structure.
- **Silent** on "Not a sign of criticality": the paper reports Bialek and
  colleagues' Ising exponents and says their parameter-count result "holds
  in a slightly different context than ours", learning a distribution by
  sampling rather than from block histograms.
