---
number: 821
status: Read
formerly:
- NOTE-tmp2pndd
paper: LIT-039
title: 'Kupiainen — Rigorous renormalization group'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from the author's accepted manuscript (RG_Nature_Final.pdf,
    6 pp. with the repository cover page) in the University of Helsinki
    repository Helda (hdl 10138/589681; record marked openAccess,
    acceptedVersion). The handle page served only a JavaScript shell, so
    the record and file were reached through the repository's DSpace
    REST API. Text extracted with pdftotext: every section, the
    acknowledgements and all ten references. The typeset Nature Physics
    version (19, 1539–1541) was not seen. The cover page says the
    reprint may differ from it in pagination and typographic detail.
date: '2026-10-14'
summary: >-
  A three-page orientation by a principal of rigorous RG. It covers
  Wilson's block-spin map as an iteration on Hamiltonians, made rigorous
  by cluster (polymer) expansions that control large fields, and what
  this proved. The massless 4D lattice φ⁴ model is Gaussian at long
  distances. The continuum 4D φ⁴ limit is always Gaussian (Aizenman and
  Duminil-Copin). The Gross–Neveu model and Hall-conductivity
  universality have been constructed or proved. The method stays near
  Gaussian, and a non-perturbative formalism is missing. The piece makes
  no new claim of its own.
---
<!-- inactive-ok-file: THEORY-194 THEORY-202 — Proposed; the record's accounts of renormalization and learning, which this Comment gives context for -->

# NOTE-821: Kupiainen — Rigorous renormalization group

## Contribution

A Comment, not a research paper. It explains to a general physics
audience what rigorous renormalization group means and what it has
achieved, and names where it stops. It adds no result. Its value here is
as an authoritative map of the constructive programme by one of its
authors.

## Key insight

The block-spin integral at one step has a UV cutoff (the lattice) and an
IR cutoff (the block size L), so a single RG step is a non-critical
problem of high-temperature statistical mechanics. The difficulty is not
the step but iterating it. The perturbative expansion of each step
diverges like n!, because the φ⁴ term grows faster than quadratically.
Rigour comes from a cluster expansion that converges where the field is
small and treats large-field regions separately ("instantons") as
improbable.

## Assumptions

None of its own. The setting it describes: the Euclidean (imaginary
time) formulation, in which Wightman functions become moments of a
random field with formal density e^{−S(φ)/ħ} (Eq. 1). A lattice UV
cutoff ε and a finite-box IR cutoff reduce the problem to classical
statistical mechanics of continuous spins.

## Key results

As reported, not proved here:

- **Superrenormalizable φ⁴ (d < 4).** Only mass renormalization is
  needed: δm²(ε) = aλ log ε in d = 2 and bλ/ε + cλ² log ε in d = 3. In
  d = 4 infinitely many divergent counterterms are needed, for both mass
  and coupling.
- **Scaling.** The scaled field ℓ^{(d−2)/2}φ(ℓx) has parameters
  (ℓm, ℓ^{4−d}λ). So the interaction is suppressed at short distances
  for d < 4 and at long distances for d > 4.
- **The block-spin map (Eq. 3).** e^{−H_{Lℓ}(ϕ′)} = ∫e^{−H_ℓ(ϕ)}δ(ϕ′ − Cϕ)Dϕ,
  with C block averaging and rescaling. The flow is the iteration of a
  fixed map R on Hamiltonians.
- **Polymer representation (Eq. 6).** e^{−(RH)(ϕ′)} = Σ_k Σ_{X₁…X_k} Π ρ_{X_i}(ϕ′),
  with weights decaying in polymer size. It re-exponentiates to a
  convergent version of the local expansion (5) where the field is small.
  Where the field is large, ρ_X ≈ exp[−cg Σϕ′⁴].
- **4D massless lattice φ⁴ (Gawędzki–Kupiainen 1985).** In d = 4 the
  relevant and marginal terms are those already in H. The marginal g
  contracts at second order. Fine-tuning µ(g) puts the flow on the
  Gaussian fixed point. The critical two-point function is
  ⟨ϕ(x)ϕ(y)⟩ ∼ Z|x − y|^{−2} (Eq. 7). Feldman, Magnen, Rivasseau and
  Sénéor proved the same by another method.
- **Continuum 4D φ⁴ is trivial.** Under the perturbative condition, the
  ε → 0 limit must be Gaussian, since g shrinks under RG and so must
  start large. Aizenman and Duminil-Copin (2021) proved this for any
  choice of bare parameters.
- **Resolution.** Treat S_ℓ as effective theories for ℓ ≥ ε with ε small.
  The renormalized series is then an accurate asymptotic series. For φ⁴
  one can continue to negative g and take ε → 0, getting an exactly
  asymptotic series, but the resulting QFT is not unitary.
- **Other constructions.** Bałaban's finite-volume work on 4D Yang–Mills
  (UV asymptotically free, IR non-perturbative). The 2D Gross–Neveu
  model (Gawędzki–Kupiainen; Feldman et al.). Universality of Hall
  conductivity (Giuliani, Mastropietro and Porta). The 3D random-field
  Ising model and first-order transitions via polymer expansions.
- **Limits and outlook.** The method "has remained restricted to
  situations that are close to Gaussian; a more nonperturbative formalism
  is still missing." Numerical RG has the same problem: truncations keep
  actions local, and nonlocal corrections have not helped. Tensor-network
  RG keeps effective actions strictly local, and Kennedy and Rychkov have
  taken first rigorous steps.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Rigorous RG proceeds by iterating a single block-spin step controlled by cluster expansions, with large fields handled separately | strong | exposition of the author's own method, with reference [7] |
| C2 | The continuum limit of 4D φ⁴ is Gaussian for any choice of bare parameters | strong (reported) | Aizenman and Duminil-Copin (2021), cited |
| C3 | Rigorous RG is limited to near-Gaussian regimes, and no non-perturbative formalism exists | moderate | the author's judgement as a principal of the field |
| C4 | Tensor-network RG is the more promising route because it keeps effective actions local | weak | the author's opinion, one cited first step |

## Concepts

- **Block spin.** The average of spins over a lattice cube of side L,
  rescaled to the unit lattice.
- **Relevant / marginal / irrelevant.** Terms that grow, stay or shrink
  under the linearization of R at the Gaussian fixed point.
- **Polymer.** A connected set of lattice sites carrying a weight that
  depends on the field only inside it.
- **Superrenormalizable.** Needing only finitely many counterterms
  (here mass only, d < 4).
- **Trivial.** Having a Gaussian, non-interacting continuum limit.

## Connections

It summarizes Kadanoff and Wilson's RG and the constructive QFT
programme from the Wightman axioms on. Its references are the primary
works: Gawędzki–Kupiainen, Feldman–Magnen–Rivasseau–Sénéor, Bałaban,
Aizenman–Duminil-Copin, Bauerschmidt–Brydges–Slade, Bricmont–Kupiainen,
Giuliani–Mastropietro–Porta and Kennedy–Rychkov.

## Bearing on the record

- **No THEORY, CLAIM or QUESTION cites it.** [LIT-881](../literature.d/LIT-881.md) and [LIT-873](../literature.d/LIT-873.md) name it
  as an unread neighbour. It is now read, and their inactive-ok
  directives for it can go.
- **The RG-and-learning accounts** ([THEORY-194](../theory.d/THEORY-194.md), [THEORY-197](../theory.d/THEORY-197.md), [THEORY-202](../theory.d/THEORY-202.md)).
  The seed guessed the piece does not address deep learning. It does
  not: no mention of learning, information or data. It does fix what a
  rigorous RG step is. It is the conditional density of the block
  variable under a delta constraint (Eq. 3), iterated, with control of
  the irrelevant remainder and the large fields. [THEORY-202](../theory.d/THEORY-202.md)'s point,
  that matching a partition function or Kadanoff's trace condition does
  not make a coarse-graining a renormalization, is consistent with this.
  The objects rigorous RG controls are the flow of the whole effective
  Hamiltonian and its fixed points, not the fidelity of one step.
  [THEORY-197](../theory.d/THEORY-197.md) identifies an exact RG step with an RBM parametrization.
  Kupiainen's account adds that exactness of one step is the easy part.
  This is context, not evidence, for those accounts.
- **No THEORY is filed.** The Comment reports others' results and its
  author's judgement, and the one result that might be filed here, 4D φ⁴
  triviality, should be filed from Aizenman and Duminil-Copin's paper,
  not a summary of it.
- No instruction for machine-learning practice.

## Limitations

- A popular Comment: no proofs, no conditions stated precisely enough to
  cite as theorems. The δm² coefficients a, b, c are said to be explicit
  but not given.
- It speaks for one school, the block-spin, cluster-expansion line.
  Feldman et al.'s different method appears only as a citation, and
  continuous flow-equation approaches are not mentioned.
- The outlook on tensor-network RG is an opinion.

## Open questions

- A non-perturbative rigorous RG, beyond near-Gaussian regimes. The
  author names its absence as the field's main gap.
- Rigorous construction of 4D Yang–Mills in infinite volume, of which
  Bałaban's finite-volume work is the cited step.
