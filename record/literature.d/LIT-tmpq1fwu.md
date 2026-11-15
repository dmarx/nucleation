---
status: Active
status_note: >-
  read 2026-11-15 ([NOTE-tmpliu98](../notes.d/NOTE-tmpliu98.md)) from arXiv v1 (NeurIPS 2026): the main
  text in full, and the appendices' statements, with the proofs skimmed
  and not verified. Worth reading as a nonlinear-observer account of
  RNNs: a recurrent estimator whose latent dynamics contract embeds the
  true state, and a gain makes the estimate converge as fast as wanted,
  at a cost in decoder size and noise sensitivity.
title: 'Provable State Estimation with Recurrent Models'
version: 1
history:
- version: 1
  date: '2026-11-15'
  note: >-
    Registered and read on 2026-11-15 at the owner's request ("read and
    file"). Checked first: not held, and the record held no KKL, Neural
    ODE or high-gain observer entry. Citation from the arXiv API and the
    PDF: Vincent Andrieu, Pauline Bernard, Lucas Brivadis, Laurent Praly
    and Christian Wolf, NeurIPS 2026; v1 submitted 2026-11-06 (deposited
    through HAL), which is `published:`. Read by a delegated reader; the
    filer string-matched every quotation used.
tags:
- control-theory
- learning-theory
- mathematics
- anthology-candidate
date: '2026-11-15'
published: '2026-11-06'
arxiv: '2611.09217'
first_author: 'Andrieu'
keywords:
- 'nonlinear observer'
- 'KKL observer'
- 'contraction'
- 'recurrent neural networks'
- 'Neural ODE'
- 'state estimation'
- 'differential observability'
- 'high gain'
implementations: []
summary: >-
  Andrieu, Bernard, Brivadis, Praly & Wolf (2026), NeurIPS. An RNN with an
  MLP readout, read as an Euler-discretized Neural ODE ż = κg(z, o), is a
  nonlinear KKL observer. If g is contracting, a map of the true state
  into the latent space exists and attracts the latent state. If the
  observed system is differentially observable and a "filter rank"
  condition holds, the map is injective, so a decoder recovers the state.
  The error is bounded by a constant times κ^ℓ e^{−κt}: tunable, with a
  noise floor growing like κ^ℓ and a ReLU decoder of size growing like
  (κ^ℓ/ε)^m. A contracting GRU beats a vanilla GRU on a robot odometry
  task, and a trained vanilla GRU forgets its initial state, which the
  authors read as emergent contraction.
---

<!-- inactive-ok-file: THEORY-1431 — Proposed; the reservoir THEORY named for comparison -->

# LIT-tmpq1fwu: Provable State Estimation with Recurrent Models

Vincent Andrieu, Pauline Bernard, Lucas Brivadis, Laurent Praly and
Christian Wolf, "Provable State Estimation with Recurrent Models",
NeurIPS 2026; arXiv:2611.09217.

## Key takeaways

*From the reading, [NOTE-tmpliu98](../notes.d/NOTE-tmpliu98.md).*

- **RNNs as observers.** With latent dynamics contracting in the
  Euclidean metric, a C¹ map T_κ of the true state into the latent space
  exists and attracts the latent state at rate κ (Thm 3.4). It is a KKL
  map, characterized by ∂T_κ/∂x · f = κ g(T_κ, h).
- **Injective, hence decodable.** Under differential observability of
  order ℓ, latent dimension at least p(ℓ+1), and a filter-rank condition,
  T_κ is Lipschitz-injective with constant of order κ^ℓ (Thm 3.7).
- **Tunable.** The estimation error is at most c κ^ℓ e^{−κt} (Thm 4.1).
  The authors note that the conditions are only sufficient: "nothing says
  that a moderate gain fails".
- **The prices.** A noise floor of order κ^ℓ‖δ‖∞ (Prop. 4.3), and a ReLU
  decoder of size O((κ^ℓ/ε)^m log(κ^ℓ/ε)) (Thm 4.2).
- **Empirical claims.** A contracting GRU beats a GRU on robot odometry
  correction, and a trained GRU "forgets its initial condition under any
  input".

## Standing in the record

Filed on 2026-11-15 at the owner's request. It joins the record's control
holdings: the Luenberger observer and rank tests ([LIT-051](LIT-051.md), [NOTE-062](../notes.d/NOTE-062.md)), of
which its linear case is an instance. It sits close in method to
Del Vecchio and Slotine's contraction theory of singularly perturbed
systems ([LIT-1295](LIT-1295.md), [THEORY-773](../theory.d/THEORY-773.md)). Read as a reservoir result, it gives a
sufficient condition for a fixed contracting reservoir's readout to
recover the driving state. The authors say the echo state property gives
no such guarantee (cf. [THEORY-1431](../theory.d/THEORY-1431.md)). The architecture recommendation
(contracting GRUs) is practice and carries the `anthology-candidate`
flag.
