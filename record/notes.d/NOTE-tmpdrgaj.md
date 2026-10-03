---
status: Read
paper: 'LIT-tmpbgf7s'
title: 'Bayesian model reduction'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read in full from arXiv 1805.07092v2 (32 pages): §§1–8, the gamma
    derivation in the appendix, the software note and the references.
    The text layer lost the displayed equations; Eqs. 9, 10 and 12 were
    read from rendered page images, and Eqs. 11, 16–17 and Table 1 from
    the prose that describes them and from Friston & Penny
    (LIT-tmpuhjzx), whose Eq. 9 is Eq. 11 here. Figures were read from
    captions and text. The Matlab demos were not run. v1 (2018) was not
    compared.
date: '2026-10-03'
summary: >-
  The free energy of any model that differs from a fitted one only in
  its prior is ln E_Q[P̃/P] plus the fitted free energy, with closed forms
  for Gaussian, Dirichlet, beta, gamma, categorical and multinomial
  priors. Greedy pruning by this quantity recovers sparse structure in
  three simulations. Hierarchical models invert as a cascade of
  reductions.
---

<!-- inactive-ok-file: THEORY-073 — Proposed; named as the reading of Markov blankets this paper's usage does not go beyond, with no relation claimed -->

# NOTE-tmpdrgaj: Bayesian model reduction

## Contribution

A technical review that turns the post hoc identity of Friston & Penny
(2011) into a general toolkit. It states the reduced free energy and
reduced posterior for any change of prior (Eqs. 9–10). It gives closed forms
for the common conjugate priors (Table 1; the Dirichlet case is Eq. 12). It
shows the method on three simulations with code, and recasts hierarchical
(empirical Bayes) inversion as successive reductions (Eqs. 15–17).

## Key insight

Comparing models usually means fitting each one. If the models differ only
in what they assume before seeing the data, the fitted posterior of the
most permissive model already contains everything needed: reweight it by
how much more or less each alternative prior would have allowed, and the
average weight is the change in evidence. In a variational scheme with
conjugate forms, that average is a closed-form expression in sufficient
statistics. Structure learning becomes the repeated question "would this
model have been better off never having believed in that parameter?"

## Assumptions

- **Same likelihood** for full and reduced models; the full model contains
  every parameter of every model to be compared (§3). Models of completely
  different form cannot be compared this way.
- **A good approximate posterior and free energy for the full model.** Eqs.
  9–10 hold approximately, with F ≈ ln P(y) and Q ≈ P(θ | y). Any scheme
  that yields them will do, mean-field or not (§2).
- **Known analytic forms** for prior and posterior (Gaussian under the
  Laplace assumption, Dirichlet for categorical models, and so on); this is
  what makes the reduction closed-form.
- **Switched-off parameters** are given precise shrinkage priors, N(0, e⁻¹⁶)
  in the examples, against N(0, 1) or N(0, 1/16) for switched-on ones.

## Key results

- **Free energy decomposition (Eq. 4).** F = ln P(y) − D_KL[Q ∥ P(θ|y)] =
  E_Q[ln P(y|θ)] − D_KL[Q ∥ P(θ)]: a bound, and accuracy minus complexity.
- **Mean-field update (Eq. 5).** The optimal factor Q(θ_i) is the softmax of
  E_{Q\i}[ln P(y, θ)], the expected log joint under the factor's Markov
  blanket (citing Beal 2003).
- **Reduced evidence and posterior (Eqs. 8–10).** P̃(y)/P(y) = ∫ P(θ|y)
  P̃(θ)/P(θ) dθ, so F[P̃ : P] ≈ ln E_Q[P̃(θ)/P(θ)] + F[P] and
  ln Q̃ = ln Q + ln P̃/P − ln E_Q[P̃/P].
- **Gaussian (Eq. 11)** is Friston & Penny's Eq. 9. A parameter whose prior
  variance is shrunk to zero has equal prior and posterior moments and
  drops out of the reduced free energy.
- **Dirichlet (Eq. 12).** Reduced posterior concentration = posterior +
  reduced prior − prior; ΔF = ln B(prior) − ln B(reduced prior) +
  ln B(reduced posterior) − ln B(posterior). "This equation returns the
  difference in free energy we would have observed, had we started
  observing outcomes with simpler prior beliefs."
- **§6.1 regression.** 10 true and 10 spurious orthogonal regressors. A
  greedy search (spm_dcm_bmr_all) leaves 256 candidate models; the best has
  posterior probability 84% and the next 14.6%. The Bayesian model average
  prunes regressors 11–20 and also true regressor 6, whose effect was too
  small to detect; regressor 7 is present with probability 85.2%.
  "Around two seconds" on a desktop.
- **§6.2 Gaussian mixture.** Data from 5 clusters, a model started with 8.
  Clusters are removed when the reduced log evidence exceeds the full
  model's. With an added rule merging clusters less than 3 nats apart (KL),
  the true number is recovered.
- **§6.3 network discovery.** An 8-node linear dynamical network (0.5 Hz
  feedforward, −1 Hz feedback, −0.25 Hz self-inhibition, noise precision
  400, SNR 8.18 dB). Of three hypothesised models, the true structure wins
  with posterior "at ceiling". An automatic search recovers the network
  except the connection from node 7 to node 8, which was not needed given
  node 6's input.
- **§7.3 hierarchy (Eqs. 15–17).** The free energy of an n-level model is
  expressible recursively by reduced free energies of the levels below, so
  higher levels are optimised from lower-level priors and posteriors alone.
  In Friston et al. (2016), 16 simulated subjects with 158 neuronal
  parameters each: the between-subject level and its reduction took "a few
  seconds" against about a minute per subject-level inversion.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | The free energy and posterior of a model with any new prior follow from the full model's prior, posterior and free energy | strong (derivation), approximate to the extent F and Q are | Eqs. 6–10 |
| C2 | This generalises the Savage–Dickey density ratio to arbitrary reduced priors | strong as a formal statement; the paper asserts it, the derivation is Friston & Penny's Eq. 6 | §3 |
| C3 | Closed forms exist for Gaussian, Dirichlet, beta, gamma, categorical and multinomial priors | strong (derivations; gamma worked in the appendix) | Eqs. 11–12, Table 1, Eqs. 18–20 |
| C4 | Greedy BMR recovers sparse structure in regression, mixtures and linear dynamical networks | weak to moderate: one simulation each, from the model class | §§6.1–6.3, Figs. 1–5 |
| C5 | Hierarchical inversion can be done as a feedforward cascade of reductions with no loss under Laplace or Dirichlet forms | moderate: derivation plus one cited application | Eqs. 15–17; Friston et al. 2016 |
| C6 | BMR is a model of offline synaptic pruning in the brain, as in sleep | weak: a metaphor supported by simulations in cited work, not tested here | §7.2 |

## Concepts

- **reduced free energy** F[P̃ : P]: the free energy of the model with prior
  P̃, computed from the full model's quantities (Eq. 9).
- **full (parent) model**: the model with the least informative priors,
  containing every parameter of every model compared.
- **structure learning**: here, finding which parameters a model needs, by
  scoring reductions of a parent model.
- **parametric empirical Bayes (PEB)**: hierarchical inversion of
  subject-level DCMs with a between-subject general linear model, done by
  reduction (§7.3).

## Connections

- **Friston & Penny ([LIT-tmpuhjzx](../literature.d/LIT-tmpuhjzx.md)).** The source of the identity and of the
  Gaussian form; cited for the derivation of Eq. 11.
- **Savage–Dickey.** The paper cites Savage (1972) and Verdinelli &
  Wasserman (1995) for the ratio, not Dickey. The record's statement of the
  ratio is Wagenmakers et al. ([LIT-tmp2suxj](../literature.d/LIT-tmp2suxj.md)).
- **Smith et al. ([LIT-tmpesz2r](../literature.d/LIT-tmpesz2r.md))** cite this paper (as Friston et al. 2018)
  for post hoc model optimisation, and apply the Dirichlet form to an
  agent's prior over hidden states.
- **Active Inference, Curiosity and Insight (Friston et al. 2017a)** is the
  source of the Dirichlet reduction and the rule-learning simulation of
  §7.2. The record does not hold it.

## Bearing on the record

- **Markov blankets.** Eq. 5 is the statistical home of the term: the
  blanket of a factor in a variational posterior, relative to whatever
  factorisation was chosen. It supports the formal point of [THEORY-066](../theory.d/THEORY-066.md) (a
  blanket is defined relative to a chosen set) by example, and claims
  nothing about individuation, which is what [THEORY-073](../theory.d/THEORY-073.md) disputes in the
  free-energy literature on life.
- With Friston & Penny it would source a THEORY that structure learning by
  pruning a parent model is evidence maximisation over priors, with
  Savage–Dickey as its limiting case.
- **No ML instruction.** Nothing here belongs in the anthology.

## Limitations

- **Only reductions.** BMR cannot add structure the parent model lacks; the
  parent must already contain every candidate parameter.
- **The approximation is inherited.** If the full model's Q is poor (strong
  nonlinearity, local optima), so are all reduced free energies. The paper
  does not revisit Friston & Penny's open question of how good the reduced
  free energy is as a proxy.
- **Search.** Large model spaces still need a greedy search, and the
  pruning outcome can depend on it.
- **Evidence.** The demonstrations are simulations from the assumed model
  class, and the empirical review is, by the authors' own description,
  mostly their lab's and collaborators' work.

## Open questions

- How does BMR behave when the parent model is misspecified, so that no
  reduction contains the truth?
- Can model expansion, adding parameters, be scored with the same economy?
  Smith et al. ([LIT-tmpesz2r](../literature.d/LIT-tmpesz2r.md)) approach it by building spare capacity into
  the parent model.

## Corrections

- **Citation.** The brief's "Friston, Parr & Zeidman et al." has a spurious
  "et al.": there are exactly three authors.
