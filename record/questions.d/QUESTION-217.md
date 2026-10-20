---
number: 217
status: Open
formerly:
- QUESTION-tmp8qovh
title: 'When a learning system is said to go from coarse to fine, do the order in which its representations refine one another, the order of their relevance to a task and the order in which training acquires them admit one common chain, and under what conditions on the learning operator?'
version: 1
tags:
- learning-theory
- representation-learning
- information-theory
date: '2026-10-19'
line: learned-structure
summary: >-
  A1 and A2 of the exchange of 2026-10-19 on coarse-to-fine processes. The
  record already holds that "coarse to fine" names different things: an
  order in training time by singular value ([THEORY-186](../theory.d/THEORY-186.md)), an order in
  noise ([THEORY-199](../theory.d/THEORY-199.md)), and a sample-complexity result in which every
  level arrives at once ([THEORY-195](../theory.d/THEORY-195.md)). No entry separates refinement,
  relevance and acquisition as three relations and asks when they agree.
  An answer is a theorem giving sufficient conditions for a common chain,
  or a minimal family of counterexamples.
refined_by:
- QUESTION-220
answered_by:
- THEORY-745
- THEORY-746
- THEORY-758
- THEORY-759
---
<!-- inactive-ok-file: THEORY-759 — Proposed; the spectral-bias order of acquisition, cited as open -->
<!-- inactive-ok-file: THEORY-186 THEORY-199 THEORY-481 — Proposed; open claims and readings named for context, nothing here rests on their being settled -->
# QUESTION-217: When a learning system is said to go from coarse to fine, do the order in which its representations refine one another, the order of their relevance to a task and the order in which training acquires them admit one common chain, and under what conditions on the learning operator?

## Why it is a question

A2 of the exchange of 2026-10-19 separated three relations on a family of
representations Z_ℓ:

- **refinement**: Z_a is a function of Z_b (σ(Z_a) ⊆ σ(Z_b));
- **relevance**: Z_b is at least as informative about a stated target;
- **acquisition**: the distinctions in Z_a become recoverable no later in
  training than those in Z_b, with an acquisition time
  T_ℓ(δ) = inf{t : R(D_{ℓ,t}, Z_ℓ) ≤ δ} for a decoder D and a risk R.

"The information ordering and the acquisition ordering must be represented
separately. The first is structural. The second is dynamical." A coarse-to-
fine schedule is the case where the three admit a common monotone chain.
A2: "Crucially, the default should not be to assume these orderings agree."

## What the record holds

- [THEORY-186](../theory.d/THEORY-186.md): in a deep linear network the order is by singular
  value, and "Fine distinctions come first whenever the data make them
  stronger". So acquisition and refinement can be reversed. It is exact
  only for decoupled, balanced starts and white inputs.
- [THEORY-086](../theory.d/THEORY-086.md): in the kernel regime the order is by NTK eigenvalue,
  "not by degree".
- [THEORY-481](../theory.d/THEORY-481.md): in linear attention the order is by input variance,
  with alignment to the eigenbasis assumed, and at finite context the
  modes couple at order 1/N.
- [THEORY-199](../theory.d/THEORY-199.md), [THEORY-195](../theory.d/THEORY-195.md) and [NOTE-687](../notes.d/NOTE-687.md): orders in noise and in sample
  size that run opposite to [THEORY-186](../theory.d/THEORY-186.md)'s, and "should not be cited as
  one account".
- Read on 2026-10-20:
  - [THEORY-745](../theory.d/THEORY-745.md) (diffusion maps, [NOTE-985](../notes.d/NOTE-985.md)): the exactly commuting
    case. When the levels are the operator's own spectral projectors,
    truncated diffusion maps form an exact refinement chain ordered by
    |λ_l|, and repeated application of the operator acquires them in the
    same order. The two orders agree only because they come from one
    eigenbasis. The order also depends on the normalization α, so it is
    not a property of the data alone.
  - [THEORY-742](../theory.d/THEORY-742.md) (Raju, Machta and Sethna, [NOTE-972](../notes.d/NOTE-972.md)): along nested
    coarse-grainings the Fisher metric of the parameters can only fall, so
    refinement and relevance to the parameters share a chain. Under an
    exact RG step the singular part of the metric is kept. There is no
    learning operator, so it says nothing about acquisition.
  - [CLAIM-387](../claims.d/CLAIM-387.md): among optimal compressions at different budgets the
    refinement order itself can fail to be a chain.
- Third batch, read the same day:
  - [THEORY-758](../theory.d/THEORY-758.md) (diffusion wavelets, [NOTE-984](../notes.d/NOTE-984.md)): the multilevel
    version of the commuting case. The levels are octave bands of an
    operator's spectrum, nested exactly for any operator with spectrum in
    [0, 1]. Spectral decay buys compression, not nesting. The paper's
    compressed algorithm thresholds T^(2^(j−1)), not the T^(2^j − 1) it
    states.
  - [THEORY-746](../theory.d/THEORY-746.md) (slow feature analysis, [NOTE-971](../notes.d/NOTE-971.md)): a third
    commuting case. Slow features are the bottom of a generalized
    eigenproblem, nested by eigenvalue. A stack of SFA stages is a
    refinement chain by construction, and its slowness values cannot rise
    from stage to stage on the training signal. Slow features are coarse
    only in that sense: they include squares, products and location. The
    paper says nothing on predictive sufficiency or learning dynamics.
  - [THEORY-759](../theory.d/THEORY-759.md) (spectral bias, Proposed, [NOTE-983](../notes.d/NOTE-983.md)): a finite
    ReLU network trained with Adam fits sinusoids in order of frequency,
    even when amplitude rises tenfold with frequency. So in that setting
    the learner, not the target's strength, sets the acquisition order,
    against [THEORY-186](../theory.d/THEORY-186.md)'s order by singular value. Fourier bands are not a
    refinement chain, so this order has no structural partner.
    [THEORY-761](../theory.d/THEORY-761.md) is the paper's proved representational bound, which is
    about what a network can contain, not about training.
  - Open: where the amplitude ratio flips the order from by-frequency to
    by-strength. The record has no formula for the product of the
    learner's spectrum and the data's outside the kernel regime.

What the record lacks is the condition under which a spectral order is a
refinement order. A2's candidate ("Conjecture A", in its words "a
candidate research direction, not an established theorem"): let P_ℓ
project onto the observables of level ℓ. If the learning operator A
nearly commutes with every P_ℓ ([A, P_ℓ] ≈ 0) and its effective
eigenvalues fall as finer distinctions are added, acquisition is nearly
coarse to fine, with deviations set by the cross-level coupling and the
spectral gaps. For a moving operator A_t it proposed
∫‖[A_t, P_ℓ]‖ dt ≪ 1 as the measure.

## What would count as an answer

- A theorem giving sufficient conditions, for a stated model class, under
  which the three relations share a chain; or
- a small family of constructions in which each pair comes apart. One is
  already on file: [THEORY-186](../theory.d/THEORY-186.md)'s fine-first case.

A2's first project would test it: synthetic data with a known tree, with
the spectral strength assigned to each level varied independently of the
tree, trained in a deep linear network, a kernel-regime network and a small
nonlinear one, reporting a phase diagram of coarse-first, fine-first,
simultaneous and mixed acquisition. Readings registered with this question:
spectral bias ([LIT-1261](../literature.d/LIT-1261.md)), slow feature analysis ([LIT-1249](../literature.d/LIT-1249.md)),
diffusion maps ([LIT-1246](../literature.d/LIT-1246.md)) and diffusion wavelets ([LIT-1256](../literature.d/LIT-1256.md)), and the
information geometry of coarse-graining ([LIT-1254](../literature.d/LIT-1254.md)). Whether optimal
representations nest at all is [QUESTION-220](QUESTION-220.md).
