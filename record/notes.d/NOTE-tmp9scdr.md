---
status: Read
paper: 'LIT-tmpuycxh'
title: 'An argument for hyperbolic geometry in neural circuits'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read in full from the publisher's PDF (4 pages, the version of record)
    deposited in the NSF Public Access Repository
    (par.nsf.gov/servlets/purl/10120231), extracted with pdftotext:
    abstract, the whole text, the captions of Figs. 1–2, the
    acknowledgements and all 46 references with their annotations. The
    figures were seen only through their captions. No equation needs more
    than one line, and each was checked. The cited works (Krioukov et al.
    2010 apart, read in the same batch) were not read; what they show is
    known here only through this paper's account of them.
date: '2026-10-09'
summary: >-
  A perspective, not a result: hyperbolic geometry should suit neural
  circuits because it approximates trees, makes networks navigable, and
  shares with Zipf's law an exponential growth of states. The Zipf link is
  an analogy that any power-law rank distribution, and any system with
  extensive entropy, would satisfy; the case for three dimensions leans on
  Mostow rigidity, which does not bear on noisy embeddings; and the only
  data shown are the olfactory embedding of Zhou, Smith & Sharpee (2018).
---

<!-- inactive-ok-file: THEORY-185 THEORY-tmpae88o THEORY-tmp1y92d CLAIM-119 — Proposed; cited as the accounts this reading is set against -->
<!-- inactive-ok-file: LIT-270 — Rejected; cited for its reading's point that Zipf-like curves do not identify a mechanism -->

# NOTE-tmp9scdr: An argument for hyperbolic geometry in neural circuits

## Contribution

No new result. The paper is a four-page review that puts three
literatures side by side and proposes that they meet in one geometry:
hyperbolic random graphs and their navigability (Krioukov, Boguñá and
colleagues), Zipf's law as a mark of statistical criticality and of
maximally informative representations (Mora & Bialek; Schwab, Nemenman &
Mehta; Aitchison, Corradi & Latham; Cubero et al.), and the hyperbolic
geometry its author's lab had found in odour statistics and odour
perception (Zhou, Smith & Sharpee 2018). After it, the hypothesis that
neural representations are hyperbolic has a citable statement; it was
tested in neural recordings three years later (Zhang et al. 2022,
[LIT-tmpvydv3](../literature.d/LIT-tmpvydv3.md)).

## Key insight

Hierarchy means exponentially many states at each further level; a
low-dimensional hyperbolic space holds exponentially many well-separated
points within a given radius; so a system that must represent a hierarchy
in few dimensions would be expected to use a hyperbolic metric. The
paper's last paragraph puts it as a reconciliation: neural and
behavioural data lie on low-dimensional manifolds, behaviour has
exponentially many hierarchically organised states, and hyperbolic space
of low dimension holds both.

## Assumptions

- **That a shared exponential is a shared geometry.** The Zipf argument
  needs states-with-energy and points-with-radius to be the same kind of
  thing. Nothing in the paper says what the "states" of a circuit are
  as points of a space, or what metric relates them.
- **That Zipf's law marks maximal informativeness.** Taken from Cubero et
  al. and Schwab et al. as cited, with no statement of the conditions
  under which it holds.
- **That 3D is privileged.** It rests on three observations of 3D (two
  olfactory, one from tree visualisation) and on a rigidity theorem.

## Key results

The paper reports no new analysis. What it contains, section by section:

- **Opening survey.** Hyperbolic geometry has been used for vision
  (Luneburg 1947; Gallant et al. on hyperbolic gratings in V4), olfaction,
  touch, colour metrics, ML embeddings (Ganea, Bécigneul & Hofmann,
  *Hyperbolic Neural Networks*, NeurIPS 2018), phylogenetic trees and
  Internet routing.
- **Fig. 1.** The half-plane and disk models; in the disk, nodes are
  sampled with density growing exponentially with radius and degree
  falling exponentially with it, which gives a power-law degree
  distribution (from Krioukov et al.). This is the one derived link in the
  paper between hyperbolic geometry and a power law, and it concerns node
  degrees, not state probabilities.
- **Zipf and criticality.** P(s) ∝ 1/r(s) (Eq. 1); with energy the
  log-improbability, E = log r (Eq. 2, sign written loosely), so the number
  of states grows as e^E. Zipf's law arises in systems whose internal state
  is narrowly distributed for fixed latent variables but shifts strongly
  with them (refs. 24–25), and in the most informative representations of
  those variables (ref. 26). These "echo" the navigability of hyperbolic
  networks (refs. 27–30).
- **Fig. 2 (from ref. 4).** Fruit volatiles from tomato and strawberry,
  placed by the correlation of their concentrations across samples, lie
  near the surface of a 3D Poincaré ball after a topological test excluded
  Euclidean and spherical geometry and hyperbolic non-metric MDS placed
  them. Odorants correlated with human pleasantness ratings cluster in one
  region. The paper reads this as order in the representation where the
  early olfactory code (random projections to the mushroom body) looks
  random, and notes that the "potato-chip" surfaces of earlier perceptual
  studies are consistent with hyperboloid sections.
- **Three dimensions.** 3D appears in odour statistics, odour perception
  and tree visualisation; Mostow rigidity is offered as a reason 3D may be
  the lowest dimension robust to noise.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Hyperbolic geometry should apply broadly to neural and other biological circuits | conjecture | the survey; analogy to complex networks |
| C2 | Zipf's law is a signature of hyperbolic geometry | weak: shown to share an exponential count of states, not a geometry | Eqs. 1–2 |
| C3 | Networks with hyperbolic geometry are maximally responsive to perturbations | asserted in the abstract; in the text only the Zipf-informativeness results (refs. 24–26) and navigability (refs. 27–30) are set side by side | citations |
| C4 | Fruit-odour statistics are best described by a 3D hyperbolic space with a pleasantness topography | moderate, from ref. 4; not new here | Fig. 2 |
| C5 | 3D hyperbolic representations may be the lowest-dimensional ones robust to noise | speculation; the cited theorem does not address noise | Mostow (ref. 41) |
| C6 | Hyperbolic coordinates may reveal topography elsewhere in the nervous system | conjecture | Fig. 2 by analogy |

## Method

Argument by juxtaposition of cited results, one two-line derivation (Eq. 2)
and one reproduced figure.

## Concepts

- **Zipf's law**: P(s) ∝ 1/r(s), probability inverse to rank; here
  generalised from words to the states of any system.
- **energy**: E = −log P(s), as in the statistical-mechanics reading of
  criticality; Zipf's law is then a density of states e^E, an entropy equal
  to the energy.
- **navigability**: greedy routing with only local connectivity and
  coordinates finds near-shortest paths, as in hyperbolic networks.
- **Mostow rigidity**: a finite-volume hyperbolic manifold of dimension
  ≥ 3 is determined up to isometry by its fundamental group, so it admits
  no continuous deformation of its hyperbolic structure; surfaces (2D) do.

## Connections

- **Zhou, Smith & Sharpee 2018** ([LIT-tmpp74b9](../literature.d/LIT-tmpp74b9.md), filed in the same part of
  the batch) is this paper's ref. 4 and the source of Fig. 2, its only data.
- **Zhang, Rich, Lee & Sharpee 2022** ([LIT-tmpvydv3](../literature.d/LIT-tmpvydv3.md), [NOTE-tmp1swq3](NOTE-tmp1swq3.md),
  [THEORY-tmpae88o](../theory.d/THEORY-tmpae88o.md)) is the programme's test in neural activity. It also
  takes 3D as the dimension, and its confound (hyperbolic metric against
  an exponential spread of scales) is the same one Eq. 2 glosses here: an
  exponential count of states is a property of the distribution and does
  not fix a metric.
- **Krioukov et al. 2010** ([LIT-tmp0u9c9](../literature.d/LIT-tmp0u9c9.md), [NOTE-tmprhn7r](NOTE-tmprhn7r.md), [THEORY-tmp1y92d](../theory.d/THEORY-tmp1y92d.md)) is
  ref. 8, the source of Fig. 1 and of the tree-approximation claim. There
  the power law is derived, from two exponentials in the radius; here the
  same shape is asserted for state probabilities without a model.
- **Ganea, Bécigneul & Hofmann 2018**: ref. 9 is their *Hyperbolic Neural
  Networks* (NeurIPS), not the entailment-cones paper held as
  [LIT-tmp5o7bs](../literature.d/LIT-tmp5o7bs.md).
- **The record's other Zipf reading**, [NOTE-243](NOTE-243.md) on [LIT-270](../literature.d/LIT-270.md), makes the same
  point from the other side: Zipf-like curves arise in text without
  meaning, so a Zipf curve alone does not identify a mechanism.

## Bearing on the record

- **[QUESTION-025](../questions.d/QUESTION-025.md).** Little, and nothing toward either answer it names.
  The paper's one relevant idea is the general one already in the
  question's notes from Sala et al. and Krioukov et al.: a hierarchy needs
  exponentially many states, and hyperbolic space holds them in low
  dimension, so a hierarchy may live in a radial coordinate and distances
  rather than in linear directions. It adds a reason to think word
  statistics are a case in point, since Zipf's law originated with word
  frequencies and the paper names "word distribution" with olfaction as
  places where its link applies. That reason does not survive reading: a
  Zipfian unigram distribution says nothing about the structure of
  co-occurrence among attributes, which is what [THEORY-185](../theory.d/THEORY-185.md)'s additivity
  premise and the question concern.
- **[CLAIM-119](../claims.d/CLAIM-119.md)** (communicative categories form a lattice rather than a
  hierarchy). Only by contrast: everything this paper argues for is a
  property of trees, and a lattice with shared attributes and cross-cutting
  constraints is exactly what a hyperbolic tree-approximation does not
  favour. It neither supports nor tests the claim.
- No THEORY: the paper's claims are conjectures, and its one finding
  belongs to ref. 4. No CLAIM rests on it.

## Limitations

- **The Zipf-to-hyperbolic step is not an argument for hyperbolic
  geometry.** Eq. 2 holds for any rank distribution: P ∝ r^(−a) gives a
  state count e^(E/a). More broadly, any system with extensive entropy has
  exponentially many states. What makes Zipf special, the unit slope
  (entropy equal to energy), is not used in the link to geometry, so the
  argument would make every power-law system hyperbolic.
- **States are never placed in a space.** The geometry is claimed for
  "networks", but the Zipf states are configurations of a system, and no
  metric on them is proposed.
- **The rigidity argument does not apply.** Mostow's theorem concerns the
  hyperbolic structure of finite-volume manifolds with a given fundamental
  group, holds in every dimension from 3 up, and says nothing about the
  stability of a finite point embedding under noise. The cited ref. 43 is
  about complex hyperbolic geometry.
- **The abstract's "maximally responsive" claim** is not argued in the
  body beyond setting two cited literatures side by side.
- **The evidence is the author's own**, one figure from one prior paper,
  plus older perceptual studies reinterpreted.

## Open questions

- Is there a model in which a hyperbolic latent metric produces Zipf's law
  in the frequencies of a circuit's states, with the unit exponent and not
  just a power law?
- Does any test of "3D is most robust" exist that compares noisy
  embeddings across hyperbolic dimensions, rather than invoking rigidity?
- In a co-occurrence embedding, does Zipfian frequency go with radial
  position (frequent, general words near the centre), as the hub-near-the-
  centre picture of Fig. 1 would suggest by analogy?
