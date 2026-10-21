---
number: 222
status: Open
formerly:
- QUESTION-tmpxapb2
title: 'Beyond the scalar linear Gaussian case, when a coarse variable''s reduced dynamics carry memory of the eliminated variables, does it admit a finite-dimensional Markovian augmentation whose prediction error is bounded in terms of the eliminated dynamics, and is a level whose history, not its present state, does the predicting still a level?'
version: 2
history:
- version: 2
  date: '2026-10-21'
  note: >-
    Split under ADR-049. The scalar linear Gaussian VAR(1) case is
    QUESTION-tmphwjsk, Answered by CLAIM-398. The title gains "Beyond the
    scalar linear Gaussian case" and asks for error bounded in terms of
    the eliminated dynamics.
tags:
- complex-systems
- mathematics
- natural-sciences
date: '2026-10-19'
line: distributed-agency
summary: >-
  A3 and A5 of the exchange of 2026-10-19 on coarse-to-fine processes,
  A5's candidate Q3. The Mori–Zwanzig decomposition writes any projected
  dynamics as a Markovian term, a memory term and noise. The record holds
  no reading of it. Its criteria of closure ([THEORY-257](../theory.d/THEORY-257.md)) condition on the
  coarse variable's own history, so memory is not by itself a failure of
  them, and [CLAIM-327](../claims.d/CLAIM-327.md) already locates a collective in a variable members
  read from the past.
answered_by:
- CLAIM-389
- THEORY-752
- THEORY-760
- THEORY-762
- THEORY-773
- THEORY-818
- THEORY-819
- CLAIM-397
refined_by:
- QUESTION-tmphwjsk
---
<!-- inactive-ok-file: NOTE-1029 — new reading, cited as where CLAIM-397 was derived -->
<!-- inactive-ok-file: THEORY-818 — Proposed; the Lorenz 96 finding, cited as partial -->
<!-- inactive-ok-file: LIT-1245 LIT-1251 LIT-1253 LIT-1259 — Deferred; works registered unread, cited as open, nothing here rests on them -->
<!-- inactive-ok-file: CLAIM-157 CLAIM-327 THEORY-257 — Proposed; open claims and readings named for context, nothing here rests on their being settled -->
# QUESTION-222: Beyond the scalar linear Gaussian case, when a coarse variable's reduced dynamics carry memory of the eliminated variables, does it admit a finite-dimensional Markovian augmentation whose prediction error is bounded in terms of the eliminated dynamics, and is a level whose history, not its present state, does the predicting still a level?

## Why it is a question

Eliminating variables does not remove their influence. It returns as
memory and noise. A5's example: with ẋ = −ax + by and ẏ = cx − dy,
keeping only x gives

ẋ(t) = −a x(t) + bc ∫₀ᵗ e^{−d(t−s)} x(s) ds + b e^{−dt} y(0),

with memory kernel K(t) = bc e^{−dt}. When d is large the memory fades and
a Markovian model of x may serve. When d is small it persists. A5: "it
would be premature to interpret persistent memory as evidence that the
system has no meaningful macroscopic organization. It might instead mean
that **the correct macrostate includes history or an additional internal
memory coordinate**."

A3 gave the general form, Ż = F(Z) + ∫ K(t − s, Z_s) ds + η, and a caution
the record keeps: the split into drift, memory and noise depends on the
projection, so "an arbitrary norm of the memory kernel is not, by itself, a
representation-invariant measure of emergence."

## What the record holds

- [THEORY-257](../theory.d/THEORY-257.md): dynamical independence conditions on Y's own history. A5:
  "non-Markovianity of Z_t is not automatically a violation of its
  dynamical-independence criterion." What it forbids is information from
  the micro history beyond that.
- [CLAIM-327](../claims.d/CLAIM-327.md): a reputation or standing is an endogenous variable because
  members read the accumulated past and act on it.
- [CLAIM-157](../claims.d/CLAIM-157.md) and [CASE-043](../cases.d/CASE-043.md): a block test on synchronous dynamics misses a
  coupling that runs through storage, such as Otto's notebook, and needs a
  time-lagged version that is not built.
- Mori–Zwanzig, read on 2026-10-20:
  - Chorin, Hald and Kupferman (2000), [NOTE-989](../notes.d/NOTE-989.md). The decomposition
    is exact for any flow, and with Zwanzig's projection the noise is
    uncorrelated with, not independent of, the resolved variables. For a
    deterministic flow with an invariant measure, zero memory, zero noise
    and exact closure coincide (the record's derivation, in the NOTE).
  - Chorin, Hald and Kupferman (2002), [NOTE-975](../notes.d/NOTE-975.md). Three projections
    give three different splits, which bears out A3's caution. In
    Hamiltonian systems the leading memory effect is a damping that grows
    linearly in time ([THEORY-752](../theory.d/THEORY-752.md)). There is no augmentation and no
    error bound.
  - Parish and Duraisamy (2017), [NOTE-973](../notes.d/NOTE-973.md). The turbulence literature's
    working answer has this question's shape: the resolved modes plus
    (m + 1)N memory coordinates, the first of them the subgrid force
    ([THEORY-760](../theory.d/THEORY-760.md)). Its error is not controlled: the memory length is
    fitted, and the kernel's shape is fixed by a quadrature rule rather
    than by the eliminated spectrum.
- Slow eigenfunctions of a reversible diffusion ([THEORY-762](../theory.d/THEORY-762.md), from
  Nadler et al., [NOTE-986](../notes.d/NOTE-986.md)). A generator eigenfunction has
  E[ψ(X_{t+s}) | past] = e^{−λs}ψ(X_t), so its Mori–Zwanzig memory and noise
  vanish in mean, exactly. It is Markov in law only if |∇ψ|² is a function
  of ψ. Otherwise the memory sits in the noise intensity, and one extra
  coordinate, |∇ψ|², carries it. That is a finite augmentation for this
  class.
- Memory against dynamical independence, settled for linear Gaussian
  VAR(1) ([CLAIM-389](../claims.d/CLAIM-389.md)). Independence implies zero memory, but zero
  memory does not imply independence. A5's own example shows the gap: with
  c = 0 and b ≠ 0 there is no memory, yet x is not closed.
- Germano ([LIT-1251](../literature.d/LIT-1251.md), Unavailable) supplies a related distinction: a
  hierarchy of filtered descriptions can exist with no closed equation at
  any level.
- When the eliminated variable is fast and contracting, no augmentation
  is needed: the memoryless quasi-steady-state reduction predicts to O(ε)
  uniformly in time, with explicit constants, provided the reduced system
  is itself contracting (Del Vecchio and Slotine, [THEORY-773](../theory.d/THEORY-773.md); the
  paper's Theorem 3 omits that hypothesis and is false without it). On
  A5's example with c = κd the memory kernel tends to a delta and the
  Markovian error is O(1/d), checked at d = 5 to 500. Deterministic only;
  open for slow or noisy eliminated variables.
- Chorin and Lu (2015, [LIT-1304](../literature.d/LIT-1304.md), [NOTE-1028](../notes.d/NOTE-1028.md)): a discrete NARMAX
  closure is a finite augmentation by past states, discrepancies and
  innovations. On Lorenz 96 at ε = 0.5, with no gap of time scales, one or
  two lags sufficed ([THEORY-818](../theory.d/THEORY-818.md), Proposed), with orders tuned by trial
  and no error bound. Its derivation from Mori–Zwanzig is motivation only.
- In the linear Gaussian VAR(1) the augmentation is exact and needs only
  the coarse variable's own history: a scalar coarse variable is ARMA of
  orders at most (n, n − 1) ([CLAIM-398](../claims.d/CLAIM-398.md), demonstrated), though its
  Mori–Zwanzig kernels are non-zero at every lag. In one example the extra
  error of truncating to AR(p) fell at a rate set by the moving-average
  zero, not by the eliminated dynamics' spectrum; three projections gave
  three memory lengths, as A3 cautioned.
- Lin and Lu (2019, [LIT-1307](../literature.d/LIT-1307.md), [NOTE-1029](../notes.d/NOTE-1029.md)) prove the discrete
  Mori–Zwanzig identity exactly for any projection, and, for the Wiener
  projection onto the whole past of the resolved variables under a
  measure-preserving invertible map, that the memory term vanishes and the
  next state is a causal Wiener filter of the past ([THEORY-819](../theory.d/THEORY-819.md),
  Active). Their step to NARMAX is a heuristic rational approximation
  with no error bound. In the linear Gaussian VAR(1) the filter is exactly
  rational, and its pole, the moving-average zero, sets the truncation
  rate. Mori's memory for a scalar variable is fixed by its own
  autocovariance and has Hankel rank one less than it ([CLAIM-397](../claims.d/CLAIM-397.md)).
  So every stationary variable has an own-history representation in
  second order; having one marks nothing. What can mark a level is that
  the micro past does not predict the residual ([THEORY-257](../theory.d/THEORY-257.md)'s test), or that
  the representation is finite.

## What would count as an answer

For a stated class, conditions under which the reduced process has a
finite-dimensional Markovian augmentation (the coarse variable plus k
memory coordinates) whose prediction error is bounded, with k and the error
in terms of the spectrum of the eliminated dynamics; and a ruling on
whether the record's level criteria should be applied to the augmented
state or to the instantaneous one. A5's own limit: this is "a candidate
theoretical extension, not a result already established for social or
cognitive systems."

**Split, 2026-10-21 ([ADR-049](../decisions.d/ADR-049.md)).** The scalar linear Gaussian VAR(1) case
is [QUESTION-tmphwjsk](QUESTION-tmphwjsk.md), Answered by [CLAIM-398](../claims.d/CLAIM-398.md): an exact finite
augmentation from Y's own history. This question keeps nonlinear and
noisy classes, vector coarse variables, error in terms of the eliminated
spectrum, and the ruling on levels.
