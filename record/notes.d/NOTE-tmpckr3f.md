---
status: Read
paper: 'LIT-1225'
title: 'Cooper and West — Division of labour and the evolution of extreme specialization'
version: 1
history:
- version: 1
  date: '2026-10-29'
  note: >-
    Read in full on 2026-10-29 from the authors' accepted manuscript in
    the Oxford University Research Archive
    (https://ora.ox.ac.uk/objects/uuid:9daf417b-3c69-4380-9f09-bf1ccfab7103,
    file md15e8fcb7611459c8e5ba55a2158c2ec, 17 pages), text extracted
    with pdftotext. The publisher's version is paywalled and was not
    compared. Read: the abstract, the results, the conclusion, the
    methods (fitness equation, equilibrium analysis, assumptions), the
    figure legends, Table 1 and the 49 references. The figures are not in
    the manuscript file; they were read from their legends. The 36-page
    supplementary information (same ORA record) was opened and only its
    title page read; the ESS, uninvadability and convergence-stability
    proofs and the individual-based simulations were not read. The
    methods' fitness function was run as a selection-gradient dynamics
    (record script, 2026-10-29) at α = 3, λ = 0.8, e = 1 and R = 0.1, 0.5,
    0.9: it reaches q2 = 0 at every R, sterile helpers (q1 = 1) at R ≥ 0.5
    and q1 ≈ 0.90 at R = 0.1, with p* rising with R (0.125, 0.333,
    0.474). This agrees with the paper's claims for those values; it is a
    gradient run, not an ESS analysis.
date: '2026-10-29'
summary: >-
  A kin-selection model of one cooperative trait with two phenotypes that
  invest q1 and q2 in helping. Division of labour needs accelerating
  returns to helping (α > 1) but is not guaranteed by it; when it evolves
  one phenotype is always a pure reproductive (q2 = 0), so a feedback
  between helper and reproductive specialization drives the extremes.
  Relatedness does not affect whether division evolves for an essential
  trait, and favours sterile helpers. The authors infer that division of
  labour drives major transitions; the model contains no transition.
---
<!-- inactive-ok-file: CLAIM-279 — Proposed; the claim this reading bears on, cited as open -->

# NOTE-tmpckr3f: Cooper and West — Division of labour and the evolution of extreme specialization

## Contribution

Earlier models assumed clonal groups or a single form of division (often
sterile helpers). This one lets the helping level of each phenotype and
their ratio co-evolve under kin selection with relatedness as a free
parameter, and finds which of the four forms of division (two generalists,
generalist with sterile helper, generalist with pure reproductive, sterile
helper with pure reproductive) can be stable.

## Key insight

Specialization feeds on itself. The more a reproductive phenotype stops
helping, the more the helper is selected to help, and the more the helper
helps, the faster the reproductive is driven to pure reproduction. So
whenever division of labour is favoured, the reproductive end goes to its
extreme, and the helper end often follows, which makes some individuals
wholly dependent on others' help.

## Assumptions

- Infinite population in fixed-size groups, island model, global
  competition; asexual reproduction, non-overlapping generations; rare
  mutations of small effect (weak selection).
- Relatedness R a fixed parameter ("open" model), except in SI 6.
- Fitness (Methods): W = p(1 − q1)[(1 − e) + e((1 − λ)q1^α + λ(PQ1^α +
  (1 − P)Q2^α))] + (1 − p)(1 − q2)[same with q2], where λ is the share of
  benefit going to others, α the returns to investment, e the trait's
  essentiality, and capitals the neighbours' mean traits. The neighbours'
  term replaces a mean of powers by a power of means, which the authors
  justify by weak selection.
- Linear costs (relaxed in SI 4, not read).

## Key results

- **Forms.** Only two forms of division are ever stable: pure
  reproductive with a generalist helper (0 < q1 < 1, q2 = 0) and pure
  reproductive with a sterile helper (q1 = 1, q2 = 0). Combinations with a
  generalist reproductive "never" were.
- **Efficiency.** α > 1 is necessary but not sufficient for division
  (SI 7.1); whenever division arises, α > 1 also stabilizes q2 = 0.
- **Relatedness.** For an essential trait (e = 1), R has no influence on
  whether division is favoured, "because the fitness benefit of being a
  pure reproductive is then exactly cancelled by the indirect fitness
  cost of not helping relatives". For e < 1, higher R favours it. Higher R
  favours the sterile-helper form whether or not the trait is essential.
  R = 1 is not required for any form.
- **Feedback.** Individual-based simulations: with q2 fixed above 0, q1
  evolves to an intermediate value; released, both go to the extremes
  within 10,000 generations (Fig. 4d legend).
- **Evidence (Table 1).** Of seven microbial examples, five are sterile
  helper with pure reproductive, one generalist with pure reproductive,
  one sterile helper with generalist (volvocine algae), the last a form
  the model does not allow, explained by a resource discontinuity outside
  the model.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | When division of labour is stable, one phenotype is a pure reproductive | strong, within the model | equilibrium analysis (SI 1–3, not read); gradient run agrees |
| C2 | α > 1 is necessary, not sufficient | moderate | SI 7.1 (not read) |
| C3 | For essential traits relatedness does not affect whether division evolves | strong, within the model | cancellation argument; gradient run agrees at α = 3 |
| C4 | Higher relatedness favours sterile helpers | moderate | model; consistent with comparative and experimental data cited |
| C5 | Division of labour drives major transitions, not the reverse | weak | interpretive; the model has no transition |

## Concepts

- **Essentiality e**: the fraction of fitness that comes from cooperation
  rather than the asocial environment; e = 1 means no cooperation, no
  fitness.
- **Trait sociality λ**: the share of a helper's benefit that goes to
  group neighbours rather than itself.
- **Efficiency α**: returns to investment in helping; α > 1 accelerating.
- **Extreme specialization**: a phenotype that does only one task, so
  others depend on it wholly.

## Connections

It works in the Taylor–Frank neighbour-modulated fitness framework and
Brown and Taylor's multi-trait method. The authors' review of division of
labour in microbes (West & Cooper 2016) and Michod's volvocine models are
its context; none is registered. The record's major-transitions readings
([LIT-749](../literature.d/LIT-749.md)) are the frame for C5.

## Bearing on the record

- **[CLAIM-279](../claims.d/CLAIM-279.md)** quotes A46: specialization "may improve local
  coordination while simultaneously increasing the organization's
  vulnerability to the loss or capture of a specialist". The paper says
  neither. It has no notion of coordination, and no loss or capture of a
  specialist is modelled or discussed. What it shows is dependence: "some
  individuals are completely dependent upon the helping behaviour of
  others". A46's vulnerability point is a fair inference from
  dependence, not the paper's finding, and the claim's note should say so.
- **[CLAIM-279](../claims.d/CLAIM-279.md)**'s thesis, that roles are regimes rather than kinds, gets
  partial support of a specific shape: phenotypes here are not given
  roles, they are two draws of one developmental lottery whose
  investments evolve. But the regimes do not stay intermediate; selection
  drives them to the extremes. A model of niche specialization among
  operators built on this logic would predict sharp, not graded, roles.
- **[QUESTION-083](../questions.d/QUESTION-083.md)**: the model's division emerges with no group-level
  selection and no coded roles, from individual-level (kin) selection on
  one shared rule. It is a positive instance for the question's first
  half, in a setting with relatedness and a single task.
- **[QUESTION-277](../questions.d/QUESTION-277.md)** lists it as a sixth route to individuality. The
  route is asserted in the conclusion ("a driver, not a consequence"),
  not shown: the model ends at dependence and has no higher-level unit.
- No instruction for machine-learning practice; nothing for the
  anthology.

## Limitations

- **Table 1 contradicts Figure 5.** Prediction 11 reads: "(a) If the
  helpers are sterile (q1 = 1), a higher efficiency benefits to
  specialisation (higher α) favours a lower proportion of helpers (lower
  p*). (b) Otherwise, there is no effect." The Figure 5 legend says the
  reverse: with sterile helpers "higher α has no effect upon the optimal
  proportion", with generalist helpers "a higher α decreases the optimal
  proportion of helpers". One of the two is wrong in this manuscript;
  the published version was not checked.
- Table 1 numbers two predictions "5".
- One trait, two phenotypes, open-model relatedness, no group-size
  effect except through assumed α(N), λ(N).
- The proofs and simulations are in the supplement, which was not read.

## Open questions

- Does the feedback to extremes survive several cooperative traits, where
  a pure reproductive for one trait may help with another (the authors'
  cyanobacteria example)?
- What would a model need for the dependence to become a new unit of
  selection, which C5 asserts?
