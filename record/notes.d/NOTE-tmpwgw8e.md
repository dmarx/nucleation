---
status: Read
paper: LIT-3004
title: 'Barabási and Albert, Emergence of Scaling in Random Networks, read for growth and preferential attachment as the origin of power-law degree tails'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Read on 2026-11-22 by a delegated reader from the arXiv preprint
    (https://arxiv.org/pdf/cond-mat/9910332, v1 of 21 Oct 1999, the
    authors' submitted version, 11 pp.), in full: the text, references and
    notes 1 to 20, and the captions of Figs. 1 and 2; the figures were seen
    only as extracted axis text. The published Science version was not
    read: https://www.science.org/doi/10.1126/science.286.5439.509
    returned 403 with a Cloudflare challenge on 2026-11-22, and the reader
    stopped there. OpenAlex, queried by DOI with no email sent, lists the
    arXiv copy as the only open one. Every quotation the filing leans on
    rechecked by the filer by script against the preprint's text; page
    numbers are the preprint's.
date: '2026-11-22'
summary: >-
  Reports power-law degree tails in actor, Web, power-grid and citation
  networks and proposes growth plus linear preferential attachment as
  their generic origin. Simulation gives γ = 2.9 ± 0.1 and a mean-field
  argument γ = 3. Model A (growth, no preference) gives an exponential;
  Model B (preference, no growth) shows power-law scaling at early times,
  is not stationary and ends as a complete graph; "both ingredients ...
  are needed", and "scaling is present only for α = 1". The empirical
  exponents are slopes drawn on log–log plots, with no fit or test.
---
<!-- inactive-ok-file: ARG-149 — Proposed; the argument whose gap this reading fills -->
<!-- inactive-ok-file: CLAIM-817 CLAIM-830 CLAIM-803 SYNTHESIS-119 THEORY-tmpfrz0k THEORY-tmphcnj3 ARG-tmp3q9cy ARG-tmpmylwc — Proposed or new; the reading of this work, the arguments filed with it and the entries it bears on -->

# NOTE-tmpwgw8e: Barabási and Albert, Emergence of Scaling in Random Networks, read for growth and preferential attachment as the origin of power-law degree tails

## Contribution

Growth plus preferential attachment, named as the generic mechanism of
scale-free degree distributions; the mean-field derivation of γ = 3 from
arrival times; and an argument that removes one ingredient at a time
(Models A and B) to show both are needed. The reading is [THEORY-tmpfrz0k](../theory.d/THEORY-tmpfrz0k.md).
The book chapter that restates it is read in [NOTE-tmpnpqc8](NOTE-tmpnpqc8.md).

## Key results

Page numbers are the preprint's.

- **Empirical tails** (pp. 2 to 4). Actors γ = 2.3 ± 0.1, WWW in-links
  2.1 ± 0.1, the western-US power grid about 4, citations 3 (after
  Redner). "The dashed lines have slopes" of these values; no fit or test
  is given.
- **The model** (p. 5): "starting with a small number (m0) of vertices, at
  every timestep we add a new vertex with m(≤ m0) edges", attached with
  Π(k_i) = k_i/Σ_jk_j. Simulation: "an exponent γmodel = 2.9±0.1", and
  "P(k) is independent of time"; "the system organizes itself into a
  scale-free stationary state".
- **Model A**, growth without preference (p. 6): "leads to
  P(k) ∼ exp(−βk)".
- **Model B**, preference without growth (p. 6): "In model B we start with
  N vertices and no edges ... While at early times the model exhibits
  power-law scaling, P(k) is not stationary"; after T ≃ N² steps "the
  system reaches a state in which all vertices are connected". So "both
  ingredients, namely growth and preferential attachment, are needed for
  the development of the stationary power-law distribution."
- **Mean field** (pp. 6 to 7). ∂k_i/∂t = k_i/2t, so k_i(t) = m(t/t_i)^0.5;
  "older (smaller ti) vertices increase their connectivity at the expense
  of the younger", a "rich-gets-richer" phenomenon. "Assuming that we add
  the vertices at equal time intervals", P(k_i < k) = 1 − m²t/k²(t + m0),
  and at long times P(k) = 2m²/k³, "giving γ = 3, independent of m".
- **Nonlinear kernel** (p. 7): "while in general Π(k) could have an
  arbitrary nonlinear form Π(k) ∼ k^α, simulations indicate that scaling
  is present only for α = 1."
- **Other exponents** (p. 7). With a fraction p of directed links,
  γ(p) = 3 − p, "which is supported by numerical simulations", with no
  derivation. Note 16: "choosing m randomly will not change the exponent".
- **Generality** (pp. 7 to 8): "a generic property of many complex
  networks", and "the scale-free inhomogeneities are the inevitable
  consequence of self-organization due to the local decisions made by the
  individual vertices, based on information that is biased towards the
  more visible (richer) vertices, irrespective of the nature and the
  origin of this visibility."

## Assumptions

- Undirected edges, constant m, vertices arriving at equal time intervals.
- An exactly linear kernel with no offset.
- No rewiring, no edges added between existing vertices, no deletion.
- k_i treated as a deterministic continuum (mean field).
- The empirical exponents are read off log–log plots by eye.

## Concepts

Growth; preferential attachment; the scale-free stationary state;
rich-gets-richer; the mean-field continuum rate equation; the arrival-time
(age) argument; Models A and B as tests that remove one ingredient; the
nonlinear kernel k^α.

## Bearing on the record

- **[CLAIM-817](../claims.d/CLAIM-817.md)** (supports both halves at the base case). Model B shows
  growth is needed, Model A that preference is, and "scaling is present
  only for α = 1" that the kernel must be linear. This is the lawful
  source for A3's "preferential attachment alone does not guarantee this
  result", which Mitzenmacher's review did not carry ([ARG-149](../arguments.d/ARG-149.md));
  [ARG-tmp3q9cy](../arguments.d/ARG-tmp3q9cy.md). The regimes for α ≠ 1 are Krapivsky, Redner and Leyvraz's
  ([NOTE-tmp2z733](NOTE-tmp2z733.md)). "irrespective of the nature and the origin of this
  visibility" supports "unequal outcomes need no unequal ability". The
  base case as the claim states it matches pp. 6 to 7, dropping the
  factor m, which is harmless at m = 1; 3 is the mean-field exponent and
  the simulated one is 2.9 ± 0.1.
- **[CLAIM-830](../claims.d/CLAIM-830.md)** (supports the premise; qualifies one contrast). The
  premise is the arrival-time derivation at equal intervals. The paper
  casts nothing in log time and does not mention Gibrat. Model B is a
  fixed-N model with preferential attachment that "at early times ...
  exhibits power-law scaling" before ending as a complete graph. That
  qualifies the claim's Pólya-urn contrast but does not meet its
  `defeated_if`, since the tail is transient and not stationary.
  [ARG-tmpmylwc](../arguments.d/ARG-tmpmylwc.md).
- **[QUESTION-505](../questions.d/QUESTION-505.md)** (bears on it, leaves it open). γ = 3 is "independent of
  m". γ(p) = 3 − p is stated without derivation and is not obviously a
  ratio of rates: a row the question's partial pattern must fit or set
  aside.
- **[NOTE-tmpleyjh](NOTE-tmpleyjh.md)**, **[THEORY-tmphcnj3](../theory.d/THEORY-tmphcnj3.md)** (contrast). The generality claim
  rests on four networks with slopes drawn by eye. It is the premise
  Broido and Clauset test and most networks fail. The power grid (γ ≃ 4,
  scaling "less prominent") is the kind of infrastructure network they
  class Not Scale Free; whether they class this power grid was not
  checked.
- **[CLAIM-803](../claims.d/CLAIM-803.md)**, **[SYNTHESIS-119](../syntheses.d/SYNTHESIS-119.md)** (contrast). "a generic property of many
  complex networks", inferred from the shape of four tails, is the
  inference from a power law to its mechanism that [CLAIM-803](../claims.d/CLAIM-803.md) rejects.

## Limitations

- The preprint, not the print version.
- The empirical claims carry no statistics.
- The nonlinear-kernel result is one sentence ("simulations indicate").
- γ(p) = 3 − p has no derivation.
