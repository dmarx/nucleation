---
status: Read
paper: 'LIT-tmpqp2pi'
title: 'Unveiling mode-connectivity of the ELBO landscape'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read in full from the workshop PDF, all six pages, through its text
    layer; page 3, which holds the only figure, was also read as an image.
    The paper is short and states no numerical results, so this reading is
    short too.
date: '2026-10-03'
summary: >-
  Claims, without reported results, that LDA's ELBO maxima from two SVI runs
  (New York Times corpus) are joined by essentially flat maximum-energy
  paths found by the simplified string method with natural-gradient bead
  updates; that the paths flatten with data size and number of topics K;
  and that statistical degeneracy, not only over-parameterisation (K > K*),
  explains it. The only figure is a schematic.
---

<!-- inactive-ok-file: LIT-tmpqp2pi — Proposed by this reading; the note is the reading that placed it -->
<!-- inactive-ok-file: LIT-tmpcuw4i — Proposed: named as the other paper a degeneracy candidate would draw on -->
<!-- inactive-ok-file: LIT-354 — Deferred: Watanabe's book is unread; named as the record's holding on singular models, with no relation claimed -->

# NOTE-tmp95bxe: Unveiling mode-connectivity of the ELBO landscape

## Contribution

It proposes that mode connectivity, known for neural network losses, holds
for the variational objective of a classical latent-variable model, and it
brings a chemistry path-finding method (the simplified string method) to the
ELBO. The contribution in this version is a conjecture and a method, not a
demonstration.

## Key insight

A topic model's optima need not be distinct answers. If the topics can be
rotated continuously into another set that explains the corpus as well, the
optima form a connected set, and the familiar experience that LDA has "no
best answer" is a fact about the shape of its objective.

## Assumptions

- **LDA** with K topics, Dirichlet priors η and α, words drawn per document
  from θ_i and β (App. A); count-data form with p_iv = Σ_k θ_ik β_kv.
- **Mean-field VI**: q(β, θ, z) = Π_k Dir(λ_k) Π_i Dir(γ_i) Π Cat(φ_ij)
  (App. B); ELBO L(λ, γ, φ) = E_q[log p(β, θ, z, x)] − E_q[log q(β, θ, z)]
  (Eq. 2).
- **Optima** from two SVI runs on the New York Times corpus ("two million
  text documents"); local parameters then fitted by batch VI on a held-out
  set, where the string method is run (§2, App. C).
- **String method**: N = 15 beads; each step a natural-gradient ascent step
  (equivalent to a batch VI update), then re-spacing along the piecewise
  linear string (App. C).

## Key results

- **Stated, not shown**: maximum-energy paths between ELBO maxima are
  essentially flat (abstract); they become "increasingly optimal" as data
  size and K increase (§1.1); experiments with synthetic data show this as K
  grows (§3); near-optimal paths appear even in an under-parameterised model
  (§1). No figures, tables or numbers support these statements.
- **Heuristic** (§3): with K > K*, reassigning a word can be offset by small
  shifts in topic identities, the analogue of a perturbed weight being
  absorbed by other weights in an over-fitted network (Kuditipudi et al.;
  Draxler et al.). The paper also notes that in truth there is no "true
  number of topics" K*.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | LDA ELBO maxima from different initialisations are connected by flat paths | weak: described, no results shown | abstract, §2 |
| C2 | Paths flatten with data size and with the number of topics | weak: asserted | §1.1, §3 |
| C3 | Statistical degeneracy explains connectivity beyond over-parameterisation | weak: argued by analogy and a schematic | §1, §3 |

## Method

Simplified string method on the ELBO: initialise beads on the segment
between two optima m₁ = (λ₁, γ₁, φ₁) and m₂; alternate a natural-gradient
ascent step for every bead with re-parameterisation that keeps beads evenly
spaced along the string; stop at convergence. The string relaxes to a
maximum-energy path.

## Concepts

- **MEP (maximum energy path)**: here, the path of highest ELBO between two
  maxima; the ELBO is maximised, so "maximum" replaces the chemist's
  "minimum".
- **statistical degeneracy**: no single optimum, but a connected set of
  optimal parameters.
- **K\***: a notional true number of topics.

## Connections

- **Draxler et al. ([LIT-tmp3kyq9](../literature.d/LIT-tmp3kyq9.md))**: the paper says its empirical method
  resembles theirs; both relax an elastic chain of points between minima.
- **Kuditipudi et al. ([LIT-tmplpsy5](../literature.d/LIT-tmplpsy5.md))**: the theoretical discussion it says
  it is closest to, relating over-parameterisation and resilience to
  connectivity.
- **Garipov et al. ([LIT-tmpotq71](../literature.d/LIT-tmpotq71.md))** and **Freeman & Bruna (2016)** are cited
  as the neural-network evidence.
- **Singular learning theory ([LIT-354](../literature.d/LIT-354.md), unread)**: not cited, but the obvious
  formal home for "statistical degeneracy".

## Bearing on the record

- It is the record's only link between mode connectivity and probabilistic
  modelling outside deep learning. A THEORY candidate, connectivity as a
  consequence of non-identifiability, would draw on it alongside the
  generative-model reading ([LIT-tmpcuw4i](../literature.d/LIT-tmpcuw4i.md)). This paper's evidence is nil as
  it stands.
- No ML instruction.

## Limitations

- **No reported results.** The text refers to an "experimental section" and
  to experiments with synthetic data that the paper does not contain.
- App. C's loop says "Repeat steps 3 and 4", where the steps to repeat are 2
  and 3.
- Mean-field VI on one model (LDA); the extension to "deeper hierarchical
  models" is conjecture (§1).

## Open questions

- The paths themselves: their ELBO profile, against the line between the
  same optima.
- Is the connected set of optima a consequence of label switching and
  topic rotation alone, or of degeneracy beyond those symmetries?
