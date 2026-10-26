---
status: Read
paper: LIT-tmpday8e
title: 'Thibaux and Jordan — Hierarchical beta processes and the Indian buffet process'
version: 1
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Read in full from PMLR's own PDF
    (https://proceedings.mlr.press/v2/thibaux07a/thibaux07a.pdf, the
    typeset AISTATS 2007 paper, eight pages; pdfinfo misreports the page
    count), text extracted with pdftotext. Read: §§1–8, the appendix and
    the figure captions. The two-column extraction interleaved some
    passages and garbled the displayed equations of §6; those used here,
    (1)–(7) and (9), were reconstructed from the prose and re-derived.
date: '2026-10-26'
summary: >-
  The beta process BP(c, B0) is the de Finetti mixing measure of the
  Indian buffet process: by beta–Bernoulli conjugacy, customer n + 1 takes
  dish j with probability m_{n,j}/(c + n) and Poisson(cγ/(c + n)) new
  dishes, which is the IBP at (c, γ) = (1, α) and its two-parameter
  generalisation otherwise. A hierarchy of beta processes lets groups share
  features, which requires a discrete shared base, at group-specific
  prevalences Beta(c_j b, c_j(1 − b)). On one unbalanced 20 Newsgroups
  split it beats tuned Laplace-smoothed naive Bayes, 58% against 50%.
---
<!-- inactive-ok-file: CASE-tmplcm41 — Proposed; the construction this reading bears on, filed from the same exchange, cited as open -->

# NOTE-tmp9d3rs: Thibaux and Jordan — Hierarchical beta processes and the Indian buffet process

## Contribution

It identifies the random measure behind the IBP. Griffiths and Ghahramani
had an exchangeable process on binary matrices; de Finetti's theorem says
some mixing measure makes the rows conditionally independent, and this
paper shows it is Hjort's beta process. That gives the IBP the
relationship the Chinese restaurant process has with the Dirichlet
process, and with it a route to the same extensions: a new sampler for
beta processes, and hierarchies of beta processes for features shared
across groups.

## Key insight

Once the measure B is in view, an object is a Bernoulli process on B: it
has feature ω with probability B({ω}). Conjugacy updates B by adding the
observed objects' atoms, so the predictive for the next object is a
mixture of "take an existing feature in proportion to how many have it"
and "draw fresh features from the base". The concentration c sets how
much objects share. If several groups are to share features, their
measures must have atoms in common, which happens only when the measure
they are drawn around is itself discrete, so it is drawn from a beta
process too.

## Assumptions

- B ~ BP(c, B0), a positive Lévy process with Lévy measure
  ν(dω, dp) = c(ω)p⁻¹(1 − p)^{c(ω)−1}dp B0(dω) for continuous B0 (1).
  For a discrete B0 = Σ qi δωi, atoms are pi ~ Beta(c qi, c(1 − qi)) (3).
- Objects Xi | B ~ BeP(B), independent Bernoulli processes.
- For the IBP connection: c constant, B0 continuous with finite mass
  γ = B0(Ω).
- Hierarchy (8): B ~ BP(c0, B0), group measures Aj ~ BP(cj, B), objects
  in group j ~ BeP(Aj). Each object belongs to exactly one group, and
  objects within a group are exchangeable.

## Key results

- **Conjugacy (5).** B | X1…n ~ BP(c + n, c/(c + n) B0 + 1/(c + n) Σ Xi),
  from Kim's theorem 3.3 (or Hjort's Corollary 4.1), cited.
- **Predictive (6).** Xn+1 | X1…n ~ BeP(c/(c + n) B0 + Σj m_{n,j}/(c + n)
  δωj): existing dish j with probability m_{n,j}/(c + n), and a
  Poisson(cγ/(c + n)) number of new dishes. With (c, γ) = (1, α) this is
  the IBP; general (c, γ) is the two-parameter version Griffiths and
  Ghahramani proposed.
- **Count of distinct dishes (7).** Poisson(γ Σ_{i=0}^{n−1} c/(c + i)),
  "roughly" Poisson(γ + γc log((c + n)/(c + 1))). It tends to Poisson(γ) as
  c → 0 (all share) and Poisson(nγ) as c → ∞ (none share). With c = 1 it
  is αH_n, re-computed here.
- **Sampler (§5).** B is built in size-biased order: at step n, draw
  Poisson(cγ/(c + n − 1)) new atoms with weights Beta(1, c + n − 1). The
  expected remaining mass after n steps is cγ/(c + n).
- **Hierarchical beta process (§6).** If B were continuous the groups'
  Aj would share no atoms with probability one, "an undesirable result";
  putting B ~ BP(c0, B0) makes it discrete. At a shared atom the group
  prevalence is aj ~ Beta(cj b, cj(1 − b)) around the baseline b (9).
  Inference splits into observed atoms, sampled by rejection from a Gamma
  bound on the log-concave posterior of b (acceptance "above 90%"), and
  the unobserved rest, handled level by level of the §5 construction.
  Deeper hierarchies (§6.3) need a and b instantiated.
- **Document classification (§7).** 1000 20 Newsgroups posts in 20
  categories, decreasing linearly from 100 to 2 documents, binary word
  presence, 40% test. γ = 150 estimated, c0 = 70 by matching (7) to the
  number of distinct words, cj = 10⁻⁴ by cross-validation. hBP: 58%
  accuracy. Naive Bayes with the best Laplace smoothing on a grid
  (a = 10⁻⁸, b = 10⁷): 50%.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | The beta process is the de Finetti mixing measure of the IBP | strong | conjugacy (5), cited; the predictive (6) then matches the buffet; re-derived in [THEORY-tmpgy035](../theory.d/THEORY-tmpgy035.md) |
| C2 | c and γ separate sharing from mass: distinct dishes Poisson(γ Σ c/(c + i)) | strong | (7), from (6) |
| C3 | For groups to share features the shared measure must be discrete, and a beta-process prior on it achieves this, with group prevalences shrunk toward a common baseline | strong | §6 and (3), (9); [THEORY-tmpz726y](../theory.d/THEORY-tmpz726y.md) |
| C4 | The hBP classifies unbalanced text better than smoothed naive Bayes and handles rare features well | weak to moderate | one dataset, one random split, no variance; the naive Bayes grid's selection criterion is not stated |
| C5 | The §5 algorithm is "a simple and efficient alternative" to inverse-Lévy and compound-Poisson samplers | weak | argued, not benchmarked |

## Concepts

- **De Finetti mixing distribution**: the law of the random element B
  given which an exchangeable sequence is i.i.d.
- **Beta process BP(c, B0)**: concentration c (function or constant),
  base measure B0, mass γ = B0(Ω).
- **Bernoulli process BeP(B)**: includes each atom ω of B with probability
  B({ω}); a Poisson process with intensity B where B is continuous.
- **Hierarchical beta process**: B ~ BP(c0, B0), Aj ~ BP(cj, B), the
  factorial analogue of the hierarchical Dirichlet process.

## Connections

It builds on Hjort (1990) for the beta process and Kim (1999) for
conjugacy, on Griffiths and Ghahramani's IBP ([LIT-tmpxrrf9](../literature.d/LIT-tmpxrrf9.md), whose §7.3
summarises this paper), and on Teh et al.'s hierarchical Dirichlet process
for the hierarchy. Its sampler is compared in prose with Wolpert and
Ickstadt's and Lee and Kim's. Williamson, Orbanz and Ghahramani
([LIT-tmpporrt](../literature.d/LIT-tmpporrt.md)) name "dependent beta processes" as their alternative route
to a dependent IBP.

## Bearing on the record

- **[CASE-tmplcm41](../cases.d/CASE-tmplcm41.md).** T22 and T23 cite this paper accurately: it is the
  established way to give groups a shared feature library at group-specific
  prevalences. Three limits matter for T23's use. Each object belongs to
  one group, while T23's membership M_{eg,t} can change and overlap; the
  groups' prevalences are exchangeable around a baseline, with no
  dynamics; and the hierarchy shares prevalences, not persistence. So it
  could replace T23's hand-written team term β_team Σg M_{eg,t} B̄_{gk,t}
  at t = 0, but not the transition. The prevalences it gives,
  aj ~ Beta(cj b, cj(1 − b)), make [CASE-tmplcm41](../cases.d/CASE-tmplcm41.md)'s item 2 sharper: a team
  where a feature is rare would need a stronger persistence term than a
  team where it is common.
- **[QUESTION-tmpixgs8](../questions.d/QUESTION-tmpixgs8.md).** The hierarchy is a way to infer which features
  formal groups share without fixing their number, which is part of what
  the question asks. It infers features of groups, not perspectives.
- **Item 1 of [CASE-tmplcm41](../cases.d/CASE-tmplcm41.md)** gains a second derivation of αH_N, from (7)
  at c = 1 ([THEORY-tmpgy035](../theory.d/THEORY-tmpgy035.md)).

No instruction for machine-learning practice; nothing for the anthology.

## Limitations

- **Conjugacy is cited**, from Kim and from Hjort, not proved here.
- **One experiment.** One dataset, one random 60/40 split, accuracy only,
  no error bars. The naive Bayes baseline's grid search does not say on
  what data it was scored. The comparison is with one weak baseline.
- **The stated reason for a small cj reads against (9).** §7 says
  "Since we expect a lot of commonalities between categories, with
  differences concentrated on a few words only, we take cj to be small",
  and that documents are then "close to being drawn from a common
  BP(c0, γ) prior". But under (9) aj ~ Beta(cj b, cj(1 − b)) has variance
  b(1 − b)/(cj + 1), so a small cj lets each category's prevalence sit
  near 0 or 1 whatever b is, and the predictive (cj b + mj)/(cj + nj) is
  then close to the raw frequency mj/nj. It is a large cj that pulls
  categories together. The value 10⁻⁴ was chosen by cross-validation, so
  the result stands; the explanation is what does not follow. The text
  may mean something it does not spell out.
- **Single-membership groups.** The hierarchy assigns each object one
  category; overlapping membership is not treated.
- **Inference is "elementary"**, in the authors' word, and they say more
  work is needed.

## Open questions

- A hierarchical beta process over overlapping, changing groups, as an
  organization's teams are: what replaces (8) when an object is in
  several groups at once?
- Do group-level prevalences from an hBP, fitted to members' activity,
  recover formal teams, or the informal ones that [QUESTION-tmpixgs8](../questions.d/QUESTION-tmpixgs8.md) is
  after?
