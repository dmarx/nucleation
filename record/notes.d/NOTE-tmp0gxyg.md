---
status: Read
paper: 'LIT-1215'
title: 'Sengupta, Tozzi, Cooray, Douglas and Friston — Towards a neuronal gauge theory'
version: 1
history:
- version: 1
  date: '2026-10-29'
  note: >-
    Read in full on 2026-10-29 from the publisher's own PDF
    (https://journals.plos.org/plosbiology/article/file?id=10.1371/journal.pbio.1002400&type=printable,
    12 pages, CC BY), text extracted with pdftotext, and its supporting
    information from the same site (S1 Appendix, S1 Glossary, S1–S5 Text
    as .docx; S1–S2 Figs as TIFF captions only). Read: the essay's
    abstract, §§I–III, Box 1, Figure 1 and its caption, the conclusions,
    the 45 references, and the prose of every supplement. The displayed
    equations in S2–S4 are embedded equation objects that did not
    extract; they were not read, so the supplements' derivations were
    followed from the prose only. OpenAlex lists arXiv 1705.06614 as a
    copy of this work; it is a different paper ("Approximate Bayesian
    inference as a gauge theory", Sengupta and Friston, 2017) and was not
    read. The Fisher metric and curvature of the univariate normal
    family were checked by hand.
date: '2026-10-29'
summary: >-
  An essay proposing that variational free-energy minimization be cast as
  a gauge theory. The only connection it names is the Levi-Civita
  connection of the Fisher information metric on the manifold of a
  belief's sufficient statistics, so its gauge freedom is reparameterization
  of the variational family; its claimed payoff is that attention is
  precision weighting forced by that manifold's curvature. No gauge group,
  invariant Lagrangian or compensating field is written down.
---

# NOTE-tmp0gxyg: Sengupta, Tozzi, Cooray, Douglas and Friston — Towards a neuronal gauge theory

## Contribution

A programme, not a result. It lists the three ingredients it takes a
gauge theory to need (a system with a continuous symmetry, local forces,
compensating gauge fields), proposes the free energy, or the entropy of
sensory samples it bounds, as the Lagrangian, sensory perturbations as the
local forces, and the geometry of the belief manifold as the source of the
gauge field. It then reads natural-gradient descent on that manifold as
gauge-covariant inference and precision weighting, and so attention, as a
force arising from its curvature.

## Key insight

Beliefs are points on a curved statistical manifold, so moving between
them needs a connection, and the Fisher metric supplies one, the
Levi-Civita connection. On this reading the "gauge field" of a Bayesian
brain is the Christoffel symbols of the Fisher metric: the fictitious
forces of a non-inertial frame, made to look like attention.

## Assumptions

- The free-energy principle: a system at nonequilibrium steady state
  with a Markov blanket minimizes variational free energy, which bounds
  surprise, and the long-term average of surprise is sensory entropy
  (ergodicity, S1 Text).
- A parametric variational density, Gaussian under the Laplace
  approximation, whose sufficient statistics are the coordinates of the
  manifold.
- The Fisher information (with the prior's Hessian added, S3 Text) as
  the metric, by Čencov's theorem.

## Key results

There are no theorems. The paper's substantive statements:

- **The connection.** "This creates a problem, in that H_i and H_{i−1}
  are in two different tangent spaces ... Addition is replaced by
  exponential mapping followed with parallel transport described using a
  covariant gauge field (Levi-Civita connection)" (S1 Fig. caption; S3.2).
  The gauge field is thus fixed by the metric, not chosen.
- **Natural gradient.** The Euclidean gradient is replaced by the inverse
  Fisher information times the gradient, "invariant under
  re-parameterisation of the approximate probability distribution"
  (S3.2), and its precision is bounded by Cramér–Rao.
- **Attention.** "Attention is a force that manifests from the curvature
  of information geometry, in exactly the same way that gravity is
  manifest when the space–time continuum is curved" (§III).
- **Between-model symmetry.** After model selection, symmetry
  transformations could give "a family of models that explain the data
  with equal probability" (Conclusions, Fig. 1); the authors are
  "tempted" to associate these classes with species.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Free-energy minimization on a belief manifold needs a connection, and the Levi-Civita connection of the Fisher metric serves | strong | standard information geometry (S2–S3) |
| C2 | Natural-gradient inference is invariant under reparameterization of the variational family | strong | standard (Amari) |
| C3 | This construction is a gauge theory of the brain | weak | asserted; no gauge group or invariant Lagrangian is specified |
| C4 | Attention is precision weighting arising from the manifold's curvature | weak | analogy with gravity; no derivation or data |

## Concepts

- **Gauge field** (S1 Glossary): "fictitious forces (mathematically, an
  Ehresmann connection) that are introduced to compensate for a poorly
  chosen coordinate system".
- **Local gauge invariance** (S1 Appendix): a pendulum whose frame rotates
  by a time-dependent angle keeps its equation of motion if the time
  derivative is replaced by a covariant one with a compensating field.
- **Free-energy manifold**: the space of sufficient statistics of the
  variational density, with the Fisher metric.

## Connections

The information geometry is Amari's; the free-energy principle is
Friston's (2010, not registered); the record holds other works on it, among them
[LIT-1181](../literature.d/LIT-1181.md) and [LIT-1262](../literature.d/LIT-1262.md). A later preprint by the first and last
authors, "Approximate Bayesian inference as a gauge theory" (arXiv
1705.06614, 2017), continues the programme; it is not registered.

## Bearing on the record

- **[QUESTION-130](../questions.d/QUESTION-130.md)** asks whether evaluative transport between
  contexts admits a connection "fixed by independently established
  relations rather than chosen". The LIT asked where this paper's
  connection comes from. Answer: from the Fisher metric. It is the
  Levi-Civita connection of the belief manifold, so it is fixed and not
  chosen, and its holonomy is the manifold's curvature (−1/2 for the
  univariate normal, checked). But what it transports is a descent
  direction between tangent spaces of one agent's belief manifold, not an
  evaluation between contexts with the situation held fixed. The
  curvature belongs to the statistical family, whatever is evaluated. So
  the paper supplies a natural connection of the wrong kind for the
  question: non-arbitrary, nontrivially curved, and not about context.
- **[CLAIM-148](../claims.d/CLAIM-148.md)**. The paper's gauge freedom is reparameterization of the
  variational family: the natural gradient is "invariant under
  re-parameterisation", and the Riemann gradient "automatically
  guarantees gauge-invariance by breaking the symmetry within a model"
  (Fig. 1 caption). That is the representational kind the claim holds, a
  change of coordinates on the same distributions. The one symmetry that
  might be more, between models with equal evidence, is proposed in the
  conclusions and not constructed.
- No instruction for machine-learning practice; nothing for the
  anthology.

## Limitations

- **No gauge theory is constructed.** No symmetry group of the
  Lagrangian is named, no local transformation is written, no gauge
  field is derived from a local invariance. What is done is Riemannian
  gradient descent with parallel transport, which needs only a metric.
- **Errors.**
  - §III: the manifold of a probability measure's sufficient statistics
    "has negative curvature and is therefore endowed with a hyperbolic
    geometry". This holds for the normal family, not in general: the
    Fisher geometry of the multinomial simplex is a piece of a sphere,
    with positive curvature, and one-parameter families have no
    curvature.
  - S2 Text, Definition 5: the Levi-Civita connection is called "the
    torsion or curvature free connection". It is the torsion-free
    metric connection; it is curvature-free only on a flat manifold, and
    the paper's own argument needs it curved.
  - S1 Glossary: a gauge field is a fictitious force from a poor choice of
    coordinates "such that there exists no gauge (or coordinate)
    transformation that can make the gauge field vanish". A field that
    comes from a choice of coordinates can be removed by changing them;
    only its curvature cannot. The two halves of the definition conflict.
  - S1 Glossary: "objects such as fields or vector spaces are groups"
    runs together algebraic fields and physical fields.
- The S3.2 conjugate-gradient algorithm's "numerical instantiation ...
  shall be presented elsewhere"; no simulation or data appears.

## Open questions

- Does any neural or behavioural datum distinguish "attention as
  curvature" from precision weighting in a flat parameterization? The
  essay names none.
- Is there a symmetry between generative models of equal evidence that a
  connection could transport across? That would be the non-representational
  case [CLAIM-148](../claims.d/CLAIM-148.md) leaves open.
