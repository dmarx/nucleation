---
status: Read
paper: LIT-2990
title: 'Park, Bocchi, D''Amico, Lucini & Aarts — Spectral phase transitions and trainability in neural network learning dynamics'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    From the arXiv PDF of 2606.28486v1 (30 pp., dated June 30, 2026),
    fetched 2026-11-22 from arxiv.org without obstacle; the arXiv HTML
    rendering was also fetched and used only to confirm the figures are
    images. The arXiv API confirms the identifier, v1 of 2026-06-26, and
    the authors Chanju Park, Dario Bocchi, Francesco D'Amico, Biagio Lucini
    and Gert Aarts. Read in full: §§I–VI, Appendices A, B, J and K, the
    openings of F, H and I, and the references. Read for headings and
    captions only: Appendices C, D, E, G and the rest of H and I. Figures
    read by caption; Fig. 16's overlap labels read from the PDF layout.
    Code and data are promised for v2. Read by a reader subagent; filed by
    a second one, which rechecked every quote used here against the PDF
    text. No email address sent.
date: '2026-11-22'
summary: >-
  In a linear rank-1 teacher–student model under full-batch gradient
  descent, training shrinks the weight covariance's random bulk and grows
  a spike, so an outlier aligned with the teacher detaches by a BBP
  transition at a critical step size, or at a critical time set by the
  step size and the initial weight variance; the student converges for
  every step size below one whether or not the outlier has appeared. In a
  ReLU MLP on UTKFace, the leading first-layer directions track the data's
  top principal components only in the large-step regime, which converges
  to a worse minimum.
---
<!-- inactive-ok-file: THEORY-tmphbp5a CLAIM-799 ARG-tmps8aog CLAIM-tmp2r6ur CLAIM-tmp9atj9 ARG-tmpun4nl LEAD-tmptgrc7 TERM-tmpf5ymd CLAIM-804 CLAIM-827 CLAIM-837 CLAIM-832 THEORY-108 THEORY-tmpthmd7 LIT-2984 LIT-tmph5ano LIT-tmp810d2 — Proposed, Deferred or new; the account this reading files, the entries it bears on and the works registered from it -->

# NOTE-tmpzethm: Park, Bocchi, D'Amico, Lucini & Aarts — Spectral phase transitions and trainability in neural network learning dynamics

## Contribution

1. **A dynamical BBP transition.** The step size and the initial weight
   variance set both the bulk's scale and the spike's, so whether and when
   an outlier appears is a function of training time and hyperparameters,
   with a lower and an upper critical branch.
2. **A trainability phase diagram** in (step size, 1/σ_W): disordered (no
   outlier), ferromagnetic (an aligned outlier) and paramagnetic (large
   steps: unstable, or convergent to a worse minimum).
3. **A teacher-free order parameter** for real networks: the cross-seed
   top-k subspace self-overlap q_k, with random baseline k/D.

## Key insight

The signal is in the weights from the first step; what has a threshold is
its visibility in the weight spectrum. Gradient descent here "is just an
interpolation between the initial and the target covariance matrices",
and the outlier appears partway along it.

## Assumptions

- Gaussian i.i.d. inputs; rank-1 teacher W* = uvᵀ; square loss; large N, D
  at fixed r = N/D; full-batch gradient descent for the exact result.
- Nonlinear networks by Gaussian equivalence, first step only; multilayer,
  first layer only.
- Finite data through the load α = P/D; SGD only at stationarity, near the
  teacher, with an invertible Hessian.
- Empirics: one dataset (UTKFace age regression, 64×64×3 flattened), one-
  and three-hidden-layer ReLU MLPs, SGD batch 128, 300 epochs.

## Key results

- **Mechanism** (§I): "The emergence of informative representations is
  then realised by isolated eigenvalues detaching from the random spectral
  bulk of a weight matrix".
- **Both sides move** (§II): "the step size ε simultaneously controls the
  spike amplitude and the random bulk, which makes the BBP transition
  dynamical and induces transient behaviour." Exactly, X(t) =
  σ_t²X̂⊥ + θ_t²ŝ_tŝ_tᵀ with σ_t² = (1−ε)^(2t)σ_W² and
  θ_t² = (1−ε)^(2t)rσ_W² + (1−(1−ε)^t)² (eqs. 17–19); the outlier appears
  when θ_t² = σ_t²(r + √r) (eq. 27).
- **Critical time** (§II D, eq. 39): t_c = −ln(1 + 1/(r^(1/4)σ_W))/ln(1−ε)
  for 0 < ε < 1; "the critical time tc is always positive and finite,
  implying that the optimisation always converges to the correct ground
  state".
- **Naming** (§II B): "We have adopted the nomenclature of disordered
  systems, but note that while the boundary εc is associated with a
  spectral phase transition, εo is an optimisation threshold." εo is "a
  spectral reference scale characterising the most efficient suppression
  of the random bulk, rather than as a general statement about optimal
  loss or generalisation" (§II A).
- **Finite data** (§IV A): "finite-sample fluctuations strongly deform the
  bulk spectrum and suppress signal extraction"; the ferromagnetic window
  narrows as the load falls.
- **Heavy tails** (§IV B): a route to heavy-tailed weight spectra through
  Σ = H⁻¹FH⁻¹, by the authors' account "purely schematic" and "highly
  heuristic".
- **Empirics** (§V): in the disordered phase q_k ∼ k/D, "consistent with
  random subspaces"; the ferromagnetic phase "develops substantial overlap
  over an extended range of k".
- **What the top directions are** (§V C, Fig. 16): the leading learned
  feature's overlap with the data's first principal component is 0.681 in
  the paramagnetic regime and 0.642 in the mixed paramagnetic–disordered
  one, against 0.056 in the ferromagnetic phase and 0.003 in the
  disordered one. The convergent paramagnetic regime "converges but
  reaches a suboptimal minimum", and there "learning is dominated by the
  principal covariance directions of the data rather than by task-relevant
  nonlinear representations"; in the ferromagnetic phase "the dominant
  modes capture nontrivial structure in the data that deviates from the
  principal components" (caption).
- **Limits** (§VI): "the precise universality class of the transition in
  practical deep learning systems remains unclear"; the outlook speaks of
  "the notion of criticality arising during optimisation itself", and of
  the picture as "a temporal extension of the initial edge-of-chaos phase
  diagram".

## Concepts

- **Dynamical BBP transition**; **critical step size** εc (two branches);
  **εo**; **critical time** t_c; **transient BBP**.
- **Trainability phase diagram**: disordered, ferromagnetic, paramagnetic.
- **Self-overlap** q^αβ and top-k **subspace self-overlap** q_k.
- **Load** α = P/D; **effective temperature** ε/|B|.

## Connections

Coeurdoux, Ferré and Bouchaud's transient BBP scenario (LIT-tmph5ano) and
Ben Arous, Gheissari, Huang and Jagannath's spectral alignment of SGD
(LIT-tmp810d2) are registered from this reading. Dandi and colleagues
(LIT-2983) and Wang, Wu and Fan (LIT-2984) are cited as prior BBP-in-networks
work. The load–temperature phase diagram of THEORY-108 is a parallel
hyperparameter phase diagram; THEORY-tmpthmd7's low-curvature bulk is a
parallel to the paper's Σ ∼ F/h², large fluctuations in soft directions.

## Bearing on the record

Filed as THEORY-tmphbp5a. Dated notes of 2026-11-22 on each entry below.

- **CLAIM-799**: supports, from inside the work: the signal is in W before
  the outlier appears; the paper's own framing reads the outlier as "the
  emergence of informative representations", the conflation the claim
  warns against (ARG-tmps8aog). The identifier is confirmed.
- **CLAIM-tmp2r6ur**: parallel, and the source of the rival reading
  CLAIM-tmp9atj9 (ARG-tmpun4nl): top directions tracking the data's leading
  principal components belong here to the large-step regime that converges
  to a worse minimum.
- **LEAD-tmptgrc7**: the test should record the training regime and stage.
- **CLAIM-837**, **CLAIM-827** (parallel: learning precedes spectral
  detection), **CLAIM-804** (parallel: the load plays the sample ratio's
  part), **CLAIM-832** (background: schematic heavy tails),
  **QUESTION-515** (leaves open), **TERM-tmpf5ymd** (an instance of bulk by
  count), **THEORY-108**, **THEORY-tmpthmd7** (parallel).

Nothing here is filed as an instruction for machine-learning practice.

## Limitations

- Exact only for linear, rank-1, Gaussian, full-batch training; the
  nonlinear, multilayer and finite-data cases are first-step or
  first-layer; the SGD heavy-tail account is heuristic by the authors' word.
- Empirics: one dataset, MLPs, no error bars in what was read, code not yet
  released.
- The "trainability" phases conflate spectral visibility with optimisation
  quality: in the linear model every ε < 1 converges, so the disordered
  phase is not untrainable there. The phase names are borrowed, not derived
  from an order–disorder transition.
