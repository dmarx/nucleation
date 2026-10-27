---
status: Read
paper: LIT-tmpfd531
title: 'Van Gael, Teh and Ghahramani — The infinite factorial hidden Markov model'
version: 1
history:
- version: 1
  date: '2026-10-27'
  note: >-
    Read in full on 2026-10-27 from the NeurIPS proceedings' own PDF
    (https://papers.nips.cc/paper_files/paper/2008/file/2723d092b63885e0d7c260cc007e8b9d-Paper.pdf,
    8 pages), text extracted with pdftotext. Read: §§1–5, the figure
    captions and the references. Several displayed equations were
    garbled by extraction; (3)–(6), (9) and the buffet's two rules were
    reconstructed from the prose and the surrounding equations and
    re-derived. The technical write-up of the M → ∞ limit, which §2.2
    says is "on the author's website", was not read. The predictive
    rules, the row counts and the comparison with CASE-165 were checked
    numerically (record script, 2026-10-27).
date: '2026-10-27'
summary: >-
  Introduces the Markov Indian buffet process: each feature is a
  two-state Markov chain over time steps, starting off, with its own
  probability of switching on, a_m ~ Beta(α/M, 1), and of staying on,
  b_m ~ Beta(γ, δ), drawn independently. In the limit the number of
  features ever on is Poisson(αH_T). Used as the prior of an infinite
  factorial HMM, it recovers who is speaking when in mixed speech better
  than an IBP prior. The sequential buffet as printed has both of its
  predictive rules wrong.
---
<!-- inactive-ok-file: CASE-165 CLAIM-454 — Proposed; the construction and claim this reading bears on, cited as open -->

# NOTE-tmpuk5qe: Van Gael, Teh and Ghahramani — The infinite factorial hidden Markov model

## Contribution

It extends the Indian buffet process from exchangeable rows to rows that
are time steps of one sequence. Each feature becomes a binary Markov
chain, and the number of chains is left unbounded. The derivation follows
the IBP's: a finite model with conjugate priors, integration over the
chains' parameters, and a limit over left-ordered equivalence classes.
The result serves as the prior of a factorial hidden Markov model whose
number of hidden chains is learned. It is the paper that introduces the
Markov IBP; the IBP review describes it from here (LIT-1556, §7.4).

## Key insight

A feature's history is a run of on and off states, and two numbers
govern it: how readily it switches on and how readily it stays on. Give
the first the IBP's prior and the second an independent beta prior. Then
the switching-on part inherits all of the IBP's limit behaviour (the
number of features ever used is Poisson(αH_T)), while persistence is
free, a property of each feature separately.

## Assumptions

- **Finite model (3)–(4).** T rows (time steps), M columns. Column m is a
  chain with transition matrix W⁽ᵐ⁾ = [[1 − a_m, a_m], [1 − b_m, b_m]],
  a_m = P(0 → 1), b_m = P(1 → 1). a_m ~ Beta(α/M, 1), b_m ~ Beta(γ, δ),
  independently. Every chain starts from a dummy off state s₀ₘ = 0.
- **Columns exchangeable, rows Markov exchangeable** (§2.3): the
  distribution is invariant to permuting features and to permutations of
  the transitions within a chain.
- **One sequence.** The rows are the time steps of a single object.
  There is no second axis of objects (§2, "rows correspond to timesteps
  and the columns to features or Markov chains").
- **Likelihood conditions** (§3): for the limit to be valid the likelihood
  must be invariant to permuting features and must not depend on a
  feature's parameter while the feature is off.

## Key results

- **Collapsed finite model (5)–(6).** With c⁰⁰, c⁰¹, c¹⁰, c¹¹ the counts of
  each transition in a chain (the dummy step included), p(S | α, γ, δ) =
  ∏ₘ (α/M)Γ(α/M + c⁰¹)Γ(c⁰⁰ + 1)/Γ(α/M + c⁰⁰ + c⁰¹ + 1) ·
  Γ(γ + δ)Γ(δ + c¹⁰)Γ(γ + c¹¹)/(Γ(γ)Γ(δ)Γ(γ + δ + c¹⁰ + c¹¹)).
- **The limit (9).** On lof-equivalence classes, p([S]) → α^{M₊} / ∏_h M_h! ·
  exp{−αH_T} · ∏_{m ≤ M₊} (c⁰¹ − 1)! c⁰⁰! / (c⁰⁰ + c⁰¹)! times the same
  b-terms, where M₊ is the number of chains that switch on at least once.
  The derivation is deferred to the first author's website.
- **The buffet (§2.3).** The first customer (time step) takes Poisson(α)
  dishes. Customer t, at each earlier dish, consults whether customer
  t − 1 took it and the waiter's transition counts. After the dishes
  already tried, customer t tries Poisson(α/t) new ones. Hence M₊ ~
  Poisson(αH_T), the IBP's count with T in place of N.
- **Stick-breaking (§2.4).** The ordered a's have the IBP's stick-breaking
  law (Teh, Görür and Ghahramani 2007). The b paired with each is an
  independent Beta(γ, δ). This licenses a slice sampler that truncates
  the model adaptively. Columns are then resampled by forward filtering,
  backward sampling (§3.2).
- **Experiments (§4).** Five speakers, four sentences each, with pauses,
  mixed linearly into ten channels with Uniform(0, 1) weights, noise
  σ_Y = 0.3, subsampled to 245 points. The ICA iFHMM, with priors
  γ ~ Gamma(10, 1) and δ ~ Gamma(1, 1) "to encode our belief that people
  speak for larger stretches of time", finds five signals. The same model
  with an IBP prior (iICA) finds nine. Average mutual information with
  the true activity is 0.296 against 0.068. With three microphones and
  489 noiseless points, both get the number wrong (the iFHMM by one, a
  near-copy of the third signal), at 0.091 against 0.028.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | The finite Markov model with a_m ~ Beta(α/M, 1) has a limit on lof-classes, (9) | strong, derivation not in the paper | §2.2; the limit's form re-derived for the a-factor |
| C2 | The number of features ever on is Poisson(αH_T) | strong | the buffet's Poisson(α/t) new dishes; consistent with (9) |
| C3 | Persistence b_m is a per-feature parameter independent of a_m | definitional | (3)–(4), §2.4 (THEORY-tmpzv1fw) |
| C4 | The mIBP's stick-breaking construction supports a slice sampler with dynamic programming | strong | §2.4, §3.2 |
| C5 | On mixed speech, an mIBP prior recovers speaker activity better than an IBP prior | weak | two single runs, one dataset, no variance |

## Concepts

- **Markov IBP (mIBP)**: the M → ∞ limit of independent two-state chains
  with Beta(α/M, 1) onset and Beta(γ, δ) persistence.
- **iFHMM**: a factorial HMM with an mIBP prior on its binary chains.
- **Markov exchangeable**: invariant under permutations of a chain's
  transitions.
- **M₊**: the number of chains that are ever on, the model's effective
  dimension.

## Connections

It extends the IBP of Griffiths and Ghahramani (NIPS 2005; the review,
LIT-1556) and uses Teh, Görür and Ghahramani's stick-breaking
construction. Its inference follows the beam sampler for the infinite HMM
(Van Gael, Saatci, Teh and Ghahramani, ICML 2008). The dependent IBP
(LIT-1548, NOTE-1175) sets itself against it in its footnote 1: the dIBP
"does not have Markov and time-invariance restrictions, and has IBP
marginals at any covariate value". THEORY-tmp29uzx confirms that the mIBP
lacks IBP marginals after the first step. The correlated latent-feature
paper (LIT-1544, NOTE-1184) counts the infinite factorial HMM among models
that correlate observations, not features.

## Bearing on the record

- **CASE-165, item 2.** The case's sticky transition, with its social,
  team and learning terms set to zero, is itself a two-state chain per
  feature. Its on-rate is π_k and its stay-rate σ(logit π_k + ρ). The
  mIBP is the same chain with the stay-rate drawn independently of the
  on-rate. That independence is what the case says T23's term lacks. At
  the paper's prior means (γ = 10, δ = 1) every feature, however rare,
  stays on with probability 10/11 = 0.91 on average. The case's sticky
  term gives 0.16 at ρ = 2 for the median feature (π = 0.025, re-checked)
  and needs ρ = 5.97 to reach 0.91. The mIBP does not hold prevalence
  fixed either: a_m is an onset rate, not a prevalence, and a chain's
  stationary on-fraction is a/(1 − b + a). That is 0.22 at a = 0.025,
  b = 10/11, and 0.34 averaged over b ~ Beta(10, 1). The case's
  "stationary prevalence departs from π_k" (0.36 against 0.2 at ρ = 2) is
  the same formula, a/(1 − b + a) with b = 0.649 (re-computed). And the
  count of active features drifts from α too (THEORY-tmp29uzx). So the
  mIBP repairs the coupling of persistence to rarity, not the drift away
  from the t = 0 prior. Only the dependent IBP holds each feature's
  prevalence fixed (THEORY-1006).
- **CASE-165 and NOTE-1172, the citation.** Both write "Van Gael et al.
  2009". The work is NIPS 21, the conference of December 2008. The review
  cites the proceedings volume's printed year, 2009, while the
  proceedings' own BibTeX gives 2008. The same paper either way, but the
  record's date for it is 2008-12-01 (LIT-tmpfd531).
- **CASE-165, the members' axis.** The mIBP models one sequence: rows are
  time steps, with no axis of members. A model of N employees with
  features persisting over time needs N chains per feature sharing
  (a_m, b_m), or some such hierarchy. The paper neither derives that
  nor its limit. "The Markov IBP gives each feature its own
  probabilities" is true of one member's sequence. For an organization
  it is a proposal.
- **QUESTION-276.** For the candidate method's dynamic prior, the mIBP is
  the established form with persistence per feature and an unbounded
  number of features, and it is the one with a working sampler.

No instruction for machine-learning practice; nothing for the anthology.

## Limitations

- **Errors in the paper.**
  - Both of the sequential buffet's predictive rules are misprinted.
    Staying on is printed as (c¹¹ + δ)/(γ + δ + c¹⁰ + c¹¹). From (6),
    and from the posterior mean of b ~ Beta(γ, δ), it is (c¹¹ + γ)/(γ + δ
    + c¹⁰ + c¹¹), so δ should be γ. Switching on is printed as
    c⁰⁰/(c⁰⁰ + c⁰¹), the probability of staying off. From (6) in the
    limit it is c⁰¹/(c⁰⁰ + c⁰¹ + 1). The record computed the exact
    predictive ratios from (6) for three count vectors: the corrected
    forms match, and the printed ones do not (0.21 against 0.86 for the
    first). The paper's own experimental prior, which puts the larger
    parameter on γ "to encode our belief that people speak for larger
    stretches of time", reads γ as the stay-on count, as (6) does.
  - (11) writes a₍₁₎ "∝ Beta(α, 1)" for "∼".
  - Typos: "the mIBP do build", "the bulck of the computation", "more
    microphones then speakers". The NeurIPS site's abstract ("We
    introduces", "After working out") differs from the PDF's.
- **The limit is not derived in the paper**, only stated, with the
  details on a website.
- **Row marginals are not the IBP's** after the first step, and the paper
  does not say so (THEORY-tmp29uzx).
- **Experiments.** One dataset, two runs, a single summary number each.
  Features are matched to ground truth "to have maximal overlap" before
  the mutual information is computed.

## Open questions

- With N objects sharing each feature's (a_m, b_m), does the limit
  M → ∞ still exist on lof-classes, and is the count of features ever on
  Poisson(α Σ) over the N T rows, or something else?
- What prior on (a_m, b_m) would keep each time step's marginal at
  Poisson(α), as the dependent IBP does by construction?
