---
status: Read
paper: LIT-2975
title: 'Cai, Zhang, Liu & Shi — The Geometric Mechanics of Contrastive Representation Learning: Alignment Potentials, Entropic Dispersion, and Cross-modal Divergence'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    From the arXiv PDF of 2601.19597v9 (16 Oct 2026, 58 pages), fetched
    2026-11-22 from arxiv.org without obstacle and converted with
    pdftotext; metadata from the arXiv API. Appendix H: "This is a revised
    presentation of the ICML 2026 version of this paper", with claims and
    results unchanged. Read in full: abstract, §§1–7, Appendix A.3, the
    statements of E.1–E.2, F.2, G and H. Skimmed or skipped: the proofs in
    Appendices B–D, F.1, F.3, F.4 beyond the main-text summary, and the
    references; figures through captions only. Read by a reader subagent;
    filed by a second one, which rechecked every quote used here against
    the PDF text. No email address sent.
date: '2026-11-22'
summary: >-
  As the number of negatives grows, InfoNCE and its gradient converge to a
  deterministic energy over the representation's distribution on a compact
  embedding manifold. For one modality it is a strictly convex free energy,
  alignment potential over temperature minus entropy, with a unique Gibbs
  minimizer, so uniformity is entropy spreading mass inside the aligned
  basin. Symmetric two-modality InfoNCE adds a negative symmetric KL
  divergence between the modalities, which can keep their marginals apart.
---
<!-- inactive-ok-file: ARG-126 ARG-tmpy3i66 CLAIM-762 CLAIM-797 CLAIM-798 CLAIM-818 CLAIM-821 CLAIM-822 CLAIM-838 THEORY-2012 THEORY-2033 THEORY-tmpvwv5n — Proposed, Deferred or new; the readings of 2026-11-22 (Wang, Wu and Fan; Yang, Steinhardt and Hu; Ansuini and colleagues; Cai and colleagues; Martínez-Sánchez and colleagues), their arguments, and the entries they bear on -->

# NOTE-tmpll97d: Cai, Zhang, Liu & Shi — The Geometric Mechanics of Contrastive Representation Learning: Alignment Potentials, Entropic Dispersion, and Cross-modal Divergence

## Contribution

1. Large-batch consistency in value and gradient, from stochastic InfoNCE
   to a deterministic population energy (Theorems 3.1, 4.1).
2. Unimodal InfoNCE read as a strictly convex free energy with a Gibbs
   equilibrium, and Wang and Isola's "uniformity" reread as entropy
   acting inside the alignment basin rather than as a force against
   alignment.
3. A structural difference, called a "bifurcation", between the unimodal
   and the symmetric multimodal objective: the latter carries a negative
   symmetric-KL coupling that can keep a modality gap open. It is a
   difference between two objectives, not a transition in a parameter.
4. Synthetic and CLIP experiments.

## Key insight

The softmax denominator, in the large-batch limit, is a kernel-smoothed
density of the representation's own law, so the objective is a functional
of that law: alignment picks the basin, entropy spreads mass within it,
and with two modalities each one's density is a barrier in the other's
potential.

## Assumptions

- Negatives i.i.d. (in-batch dependence excluded); compact Z with an
  isotropic kernel of constant volume (the sphere is the canonical case,
  Rem. 2.1, not a restriction).
- Bounded C¹ encoder Jacobians; a sharp kernel peak for the low-τ results.
- Strictly positive densities, and density floors in the multimodal
  problem (without them "the variational problem becomes ill-posed").
- Limits in order: N → ∞ at fixed τ, then τ → 0+.
- Singular measures are set aside: "distributions that collapse onto
  lower-dimensional manifolds or discrete sets" (App. G.1).

## Key results

- **Theorem 3.1**: as N → ∞ the finite-N loss minus J_τ(θ) minus
  log(N V_κ(τ)) tends to zero, and so does the gradient difference.
- **Proposition 3.1**: the intrinsic free energy "is strictly convex on
  its effective domain and has the unique Gibbs-form minimizer" ρ*(z) ∝
  exp(−U(z)/τ).
- **Uniformity reread** (§1): "This reframes 'uniformity' (Wang & Isola,
  2020) not as a global force opposing alignment, but as entropy-driven
  spreading inside the alignment basin." §3.2: the entropy term "selects
  the most internally dispersed near-optimal configuration".
- **Multimodal barrier** (Def. 4.3, Prop. 4.1): F^Sym = ½(F(ρ1) + F(ρ2)) −
  D^Sym_KL(ρ1, ρ2); the coordinate map in ρ1 "is concave"; the
  multimodal functional "does not admit Gibbs-type coordinate
  minimization", giving "a winner-take-all-like extremal geometry".
- **Theorem 4.2**: τ → 0+ does not remove the divergence term; "it remains
  an explicit separation-inducing contribution".
- **Takeaway 2**: "Symmetric multimodal InfoNCE is pairwise attractive yet
  population-level repulsive."
- **Experiments** (§5): finite-N gradients approach the reference as N
  grows; particles on S² track the Gibbs law across τ; on OpenCLIP,
  "stronger retrieval does not necessarily imply a smaller modality gap".

## Concepts

- **Population partition field**: the large-batch softmax denominator, a
  kernel-smoothed density of the current representation law.
- **Alignment potential U_θ**: minus the expected similarity under the
  positive conditional.
- **Intrinsic free energy** and its **Gibbs equilibrium**.
- **Negative symmetric-KL coupling**; **occupied-mass barrier**; **modality
  gap** (centroid gap, energy distance).

## Connections

It rereads Wang and Isola's alignment and uniformity (THEORY-2033) as basin
selection plus entropy, and places itself beside the density-ratio view of
contrastive learning, which it says does "not directly describe the
deterministic descent directions induced by the softmax denominator". Not
registered: Liang and colleagues 2022 and Yi and colleagues 2025 on the
modality gap, Betser and colleagues 2026, Calder and Lee 2025; none is
relied on here.

## Bearing on the record

Filed as THEORY-tmpvwv5n. Dated notes of 2026-11-22 on each entry below.

- **CLAIM-798**: supports the weak reading only, and replaces LIT-2975 in
  its grounds (ARG-tmpy3i66). Two characterizations the claim carried
  from A29 are corrected there: the paper declines the "attraction–
  repulsion energy on the sphere" for one modality, and its "bifurcation"
  is between two objectives.
- **THEORY-2033**, **CLAIM-762**: qualifies, by resolving the tension
  between alignment and uniformity as basin selection and spreading.
- **QUESTION-515**, **CLAIM-818**, **ARG-126**, **THEORY-305**,
  **THEORY-2012**, **CLAIM-821**, **CLAIM-797**, **CLAIM-822**,
  **CLAIM-838**, **LEAD-210**: background, parallel or contrast.

Nothing here is filed as an instruction for machine-learning practice.

## Limitations

- A theory of the objective, not of training: "Our theory describes the
  geometry of the objective rather than the trajectory of a specific
  optimization algorithm" (App. G.1); how stochastic optimization explores
  the barrier landscape "remains an important open problem".
- Large-batch limit at fixed τ, then low τ; practice uses finite batches
  and moderate τ, which "may soften the barrier-like geometry".
- The multimodal results rest on density floors and on one encoder held
  fixed at a time.
- CLIP evidence is observational plus one caption-corruption intervention;
  the modality-gap mechanism is not shown to be the only one.
- Proofs not checked.
