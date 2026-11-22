---
number: 798
status: Proposed
formerly:
- CLAIM-tmp526xr
title: "Reading a network's representations as active matter splits into a weak analogy, that embeddings move collectively under optimization and noise through a shared-parameter kernel, and a strong model, that their dynamics carry sustained nonequilibrium currents or persistent orientation-like degrees of freedom not reducible to gradient relaxation; the weak reading follows from gradient flow, the strong one has to be shown, and its flocking observable is alignment of velocities, not clustering of positions"
version: 2
history:
- version: 2
  date: '2026-11-22'
  note: >-
    After the reading of LIT-2975 (NOTE-tmpll97d, THEORY-tmpvwv5n). The
    paragraph on contrastive learning is corrected in place: the paper
    declines A29 §3's attraction–repulsion reading for one modality, has
    no collapse regime, and its "bifurcation" is between two objectives.
    LIT-2975 is replaced in the grounds by its reading, as support for the
    weak reading only (ARG-tmpy3i66). The thesis and status are unchanged.
role: thesis
warrant: interpretive
defeated_if: >-
  Evidence that the two readings cannot come apart: that representations
  whose embeddings move collectively under training always also show
  sustained probability currents or persistent velocity alignment, so that
  the strong reading needs no separate showing; or that alignment of
  embedding velocities never differs from clustering of embedding positions
  in what it detects, so that the flocking observable adds nothing.
tags:
- representation-learning
- complex-systems
- thermodynamics
date: '2026-11-21'
line:
- learned-structure
bears_on:
- QUESTION-515
complements:
- CLAIM-818
grounds:
- THEORY-209
- THEORY-779
- THEORY-tmpvwv5n
summary: >-
  A29 §2–§4 and §11 of the exchange "Rich Get Richer Power Laws"
  (2026-11-21), answering the owner's U18 ([QUESTION-515](../questions.d/QUESTION-515.md)). Under gradient flow,
  embeddings move as particles coupled by a representation-space tangent
  kernel that changes as features are learned; that much makes the
  active-matter reading a useful weak analogy. A strong active-matter
  model needs irreversibility shown, not assumed. The wording is A's (the
  other assistant in the exchange "Rich Get Richer Power Laws", A29);
  adopting it is the owner's call.
---
<!-- inactive-ok-file: THEORY-tmpcij35 — Proposed, Deferred or new; the readings of 2026-11-22 and the entries they bear on -->
<!-- inactive-ok-file: CLAIM-818 THEORY-2033 THEORY-813 THEORY-2012 — new and Proposed, filed from the exchange "Rich Get Richer Power Laws" on 2026-11-21; Deferred works registered from that exchange and not read; Proposed entries the record already held, cited for context -->
<!-- inactive-ok-file: ARG-126 THEORY-209 — new and Proposed or Rejected, filed from the exchange "Rich Get Richer Power Laws" on 2026-11-21 -->
<!-- inactive-ok-file: ARG-tmpy3i66 THEORY-tmpvwv5n — Proposed, Deferred or new; the readings of 2026-11-22 (Wang, Wu and Fan; Yang, Steinhardt and Hu; Ansuini and colleagues; Cai and colleagues; Martínez-Sánchez and colleagues), their arguments, and the entries they bear on -->

# CLAIM-798: Reading a network's representations as active matter splits into a weak analogy, that embeddings move collectively under optimization and noise through a shared-parameter kernel, and a strong model, that their dynamics carry sustained nonequilibrium currents or persistent orientation-like degrees of freedom not reducible to gradient relaxation; the weak reading follows from gradient flow, the strong one has to be shown, and its flocking observable is alignment of velocities, not clustering of positions

## The claim

**The coupling.** A29 §2: take z_i(t) = h_θ(t)(x_i) for a fixed set of
inputs. Under gradient flow,

ż_i = −Σ_j K_ij ∇_(z_j) L, with K_ij = J_i J_jᵀ and J_i = ∂z_i/∂θ,

"a representation-space analogue of a neural tangent kernel". "The training
loss supplies forces. The network architecture supplies an interaction or
mobility kernel. Shared parameters transmit those forces collectively across
representations." And K is not fixed: "The particles move because the network
learns, but the manner in which they can move also changes as the network
learns."

**Weak and strong.** A29 §4: "Ordinary gradient flow is a relaxation
process", and "stochasticity alone does not guarantee broken detailed
balance. Certain noisy gradient systems have equilibrium-like stationary
distributions." Hence:

- "**Weak active-matter analogy:** Embeddings collectively move under
  optimization and stochastic forcing."
- "**Strong active-matter model:** Their effective dynamics exhibit
  sustained nonequilibrium currents, persistent orientation-like degrees of
  freedom, or collective transport that cannot be reduced to ordinary
  gradient relaxation."

"The first is generally useful. The second is a substantive hypothesis to
test."

**The observable.** A29 §3–§4: "Alignment of embedding *positions* is
different from alignment of particle *velocities*", so clusters are not
flocks. The flocking observable is the polarity p_i(t) = ż_i/‖ż_i‖ and
whether neighbouring representations develop correlated movement
directions.

A29 §11 grades the whole proposal into three hypotheses of increasing
strength (collective dynamics, nonequilibrium self-organization, critical
active dynamics), set out in [QUESTION-515](../questions.d/QUESTION-515.md). This claim is the first step of that
ladder and the rule for climbing to the second.

## What the record holds

- [THEORY-086](../theory.d/THEORY-086.md): the kernel regime fits by tangent-kernel eigenspace in
  function space; [THEORY-813](../theory.d/THEORY-813.md): feature learning, not the lazy regime, is what
  changes the representation. Neither writes the kernel between
  embeddings or reads it as a mobility.
- [THEORY-209](../theory.d/THEORY-209.md) and [THEORY-779](../theory.d/THEORY-779.md): SGD's stationary state, with probability
  currents in the quadratic approximation and damped oscillators under
  momentum. These are the held candidates for the irreversibility the
  strong reading needs, located in parameter space.
- For contrastive learning A29 §3 writes an attraction–repulsion energy on
  the sphere, with collapse, dispersion and structured regimes; the record
  holds the pieces ([THEORY-2033](../theory.d/THEORY-2033.md), [THEORY-305](../theory.d/THEORY-305.md), [THEORY-2012](../theory.d/THEORY-2012.md)). A29 cites a 2026
  ICML paper for geometry-dependent changes between unimodal and multimodal
  regimes (Cai and colleagues, [LIT-2975](../literature.d/LIT-2975.md), read 2026-11-22 as
  [THEORY-tmpvwv5n](../theory.d/THEORY-tmpvwv5n.md)). **Corrected in place, version 2:** that paper declines
  the attraction–repulsion reading for one modality: what spreads the
  embeddings is entropy inside the aligned basin, "not ... a global force
  opposing alignment", and repulsion appears only between modalities,
  through a negative symmetric-KL term. It has diffuse and concentrated
  Gibbs states, not collapse, dispersion and structured regimes, and sets
  collapsed measures aside. Its "bifurcation" is a difference between the
  unimodal and the multimodal objective, not a transition in a control
  parameter. The sphere is its canonical case, not a restriction.

## Gaps

- A29 gives no mechanism by which the coupled system becomes active. The
  assistant's [CLAIM-818](CLAIM-818.md) shows the coupling cannot be one: under gradient flow
  the loss is a Lyapunov function whatever the kernel does. [ARG-126](../arguments.d/ARG-126.md)
  argues that this closes A29 §2's feedback loop as a route to activity.
- The "particles" are data embeddings, which nothing propels. An
  orientation-like degree of freedom, which polar active matter has, is
  named (p_i) but not given dynamics of its own.

## What it does not say

- Not that representations are active matter, or that they are not.
- Not that a power-law spectrum or slow modes would show the strong
  reading; A29 §8 and §11 say they would not.

## Note of 2026-11-22: Dandi and colleagues, read

Dandi and colleagues ([LIT-2983](../literature.d/LIT-2983.md), [NOTE-tmpdac0o](../notes.d/NOTE-tmpdac0o.md), [THEORY-tmpcij35](../theory.d/THEORY-tmpcij35.md)):
**consistent with the weak reading.** A32 §6 cites the paper against the
strong reading, and it bears that out: one gradient step, no dynamics, and
nothing about active matter. No relation.

## Note of 2026-11-22: Cai and colleagues, read

Cai, Zhang, Liu and Shi ([LIT-2975](../literature.d/LIT-2975.md)) were read ([NOTE-tmpll97d](../notes.d/NOTE-tmpll97d.md); the reading
is [THEORY-tmpvwv5n](../theory.d/THEORY-tmpvwv5n.md)). **Supports the weak reading only** ([ARG-tmpy3i66](../arguments.d/ARG-tmpy3i66.md); the
correction of version 2 above). The population picture is variational and
passive: for one modality a strictly convex free energy with "the unique
Gibbs-form minimizer", the kind of stationary state the strong reading has
to get past. Its "entropic dispersion" is a fixed term of the objective,
the cross-entropy against the model's own smoothed density that comes from
the softmax denominator, not stochastic forcing; τ is the softmax
temperature, not a noise level. With two modalities there is still one
joint energy, so the coupling is reciprocal and joint gradient flow falls
under [CLAIM-818](CLAIM-818.md). The paper leaves dynamics open ("the geometry of the
objective rather than the trajectory"): how stochastic optimization
explores the landscape "remains an important open problem", and the
optimizer is where the strong reading would have to look.
