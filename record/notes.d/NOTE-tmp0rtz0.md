---
status: Read
paper: LIT-tmpkxifq
title: 'Ghahramani and Jordan — Factorial hidden Markov models'
version: 1
history:
- version: 1
  date: '2026-10-27'
  note: >-
    Read in full on 2026-10-27 from the authors' copy on Ghahramani's page
    (https://mlg.eng.cam.ac.uk/zoubin/papers/fhmmML.pdf, 31 pages), the
    journal's typesetting with page numbers "?, 1–31" and no received
    dates; text extracted with pdftotext. Read: §§1–6, Appendices A–D,
    notes 1–10, Tables 1 and 2, the captions of Figures 1–6 and the
    references. Table 1 was read as text. Figures 3–5 (learning curves,
    timings, Bach test likelihoods) are charts, read from their captions
    and the text only; no number was taken from them. The publisher's PDF
    (https://link.springer.com/content/pdf/10.1023/A:1007425814087.pdf,
    pp. 245–273), which Springer served to this client though its page
    does not mark the article open access, was used to check Table 1's
    largest entry, notes 3 and 7, the Bach figures, the junction-tree
    count and the received dates; it agrees on each. The NIPS 1995
    version was not read. Note 3's condition was checked numerically
    (record script, 2026-10-27).
date: '2026-10-27'
summary: >-
  Defines the factorial HMM: M hidden chains of K states, a priori
  independent, whose one-hot states add their columns of W^(m) to set a
  Gaussian observation's mean. Exact inference costs O(TMK^{M+1});
  Gibbs, completely factorized and structured variational E steps make EM
  tractable. On synthetic problems an HMM with K^M states overfits badly
  while the approximate factorial HMMs stay near exact training; on Bach
  chorales factorial HMMs with up to 1000 states predict better than the
  best HMM. Its footnote 3 on when the chains decouple is wrong unless the
  covariance is isotropic.
---
<!-- inactive-ok-file: CASE-165 — Proposed; the construction this reading bears on, cited as open -->

# NOTE-tmp0rtz0: Ghahramani and Jordan — Factorial hidden Markov models

## Contribution

An HMM carries its memory of the past in one multinomial variable, so 30
bits of history need 2³⁰ states. The factorial HMM carries it in M
variables, each its own Markov chain, combined only at the observation.
The paper defines the model, shows why exact inference in it is
exponential in M, and gives three approximate E steps for EM, of which
the structured variational one, M uncoupled HMMs each run by
forward–backward, is the contribution that lasted.

## Key insight

The chains are independent a priori and dependent a posteriori: an
observation is explained jointly, so knowing one chain's state changes
what the others must have been ("explaining away"). Keep the chains'
Markov structure and drop only their coupling, and each chain becomes an
ordinary HMM whose "observation" is a learned, time-varying bias, fitted
to the residual the other chains leave.

## Assumptions

- **The model (2)–(4).** S_t = (S_t^(1), …, S_t^(M)), each a one-hot K × 1
  vector; P(S_t | S_{t−1}) = ∏_m P(S_t^(m) | S_{t−1}^(m)), (3); Y_t ~
  N(μ_t, C) with μ_t = Σ_m W^(m)S_t^(m), (4). The marginal of Y_t is a
  Gaussian mixture with K^M components sharing C.
- **Parameters** θ = {W^(m), π^(m), P^(m), C}, fitted by EM; no prior on
  them (a Bayesian treatment is mentioned in note 4).
- **Transition matrices are column-stochastic** in Appendix A, (A.5).

## Key results

- **Exact E step (§3.2, Appendix B).** The junction tree is a chain of
  T(M + 1) − M cliques of size M + 1, so exact propagation costs
  O(TMK^{M+1}); the naive K^M-state HMM costs O(TK^{2M}). The paper's
  recursion (B.1)–(B.8) sums over one chain at a time.
- **Gibbs E step (§3.3).** Each S_t^(m) resampled from its Markov blanket,
  O(TMK) per sweep; in practice "around ten samples of each hidden
  variable" tend to raise the true likelihood.
- **Completely factorized variational E step (§3.4, Appendix C).** Q =
  ∏_{t,m} Q(S_t^(m) | θ_t^(m)); fixed point (9a), θ_t^(m) = softmax{W^(m)′
  C^{−1}Ỹ_t^(m) − ½Δ^(m) + (log P^(m))θ_{t−1}^(m) + (log P^(m))′
  θ_{t+1}^(m)}, with Ỹ_t^(m) the residual of the other chains;
  O(TMK²) per iteration, converging in 2 to 10 iterations.
- **Structured variational E step (§3.5, Appendix D).** Q is M uncoupled
  HMMs with the true π^(m) and P^(m) and a fictitious observation
  probability h_t^(m) = exp{W^(m)′C^{−1}Ỹ_t^(m) − ½Δ^(m)}, (12a), the
  residual now using ⟨S_t^(ℓ)⟩. (12a) contains no prior or transition
  terms; they "have cancelled". Since it constrains Q less at no cost in
  tractability, it is preferred.
- **Experiment 1 (§4.1, Table 1).** Data from factorial HMMs with all
  parameters but C uniform on [0, 1] and normalized, C = 0.0025I; 20
  training and 20 test sequences of length 20, four-dimensional; four
  sizes (M, K) = (3, 2), (3, 3), (5, 2), (5, 3); 15 parameter sets per
  size; 300 runs in all. Entries are bits per observation relative to the
  true model, ± one standard deviation (standard errors are √15 = 3.9
  times smaller; note 7 says 3.8). Test set:

  | (M, K) | HMM (K^M states) | exact | Gibbs | CFVA | SVA |
  |---|---|---|---|---|---|
  | (3, 2) | 2.29 ± 1.02 | 1.05 ± 0.72 | 1.78 ± 1.22 | 1.20 ± 1.11 | 1.04 ± 1.01 |
  | (3, 3) | 9.81 ± 2.55 | 1.26 ± 0.99 | 2.50 ± 0.87 | 1.50 ± 1.53 | 0.90 ± 0.84 |
  | (5, 2) | 11.57 ± 3.71 | 2.51 ± 1.21 | 3.35 ± 1.14 | 2.07 ± 1.74 | 1.53 ± 1.05 |
  | (5, 3) | 175.35 ± 84.74 | 4.49 ± 2.24 | 3.95 ± 1.14 | 5.14 ± 0.69 | 4.30 ± 1.62 |

  At (5, 3) the HMM's training excess is −4.80 ± 0.52: it fits the
  training data better than the true model. Gibbs is significantly worse
  than exact on the three smaller sizes (p < 0.05); CFVA is never
  significantly different from exact; SVA is not different on three sizes
  and better at (5, 2) (p < 0.05), which the authors offer either as a
  fluke or as the variational constraint regularizing. All methods were
  "very sensitive" to the random seed.
- **Timing (Figure 4).** The HMM and exact factorial HMM are "extremely
  slow" for large state spaces; Gibbs at ten samples per variable is
  slower than the variational methods; the variational methods "scaled
  well".
- **Experiment 2, Bach chorales (§4.2).** Six attributes per event
  (Table 2), all modelled as real numbers; 30 training and 36 test
  chorales of 40 or more events. HMMs of 2 to 100 states show a U-shaped
  test curve; out of 75 runs the best, −9.0 bits per observation, has 30
  states. Factorial HMMs (K 2 to 6, M 2 to 9, structured E step) reach
  1000 states with no sign of overfitting, and "the test set likelihood
  for the best factorial HMM was an order of magnitude larger than the
  test set likelihood for the best HMM" (Figure 5). Neither is "easily
  interpretable from a musicological point of view".
- **Generalizations (§5).** Discrete observations by softmax or noisy-OR
  links; coupled chains (13), at K² × K parameters per transition or via
  undirected energy terms; input-conditioned factorial HMMs (14); hidden
  Markov decision trees.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Exact inference in the factorial HMM costs O(TMK^{M+1}) | strong | §3.2, junction-tree argument, Appendix B |
| C2 | The chains are coupled a posteriori through the shared observation | strong | §2, d-separation; note 3's exception is mis-stated (below) |
| C3 | The structured variational E step's fixed point is (12a), free of prior and transition terms | strong | Appendix D |
| C4 | On small synthetic problems the variational E steps are not significantly worse than exact EM, and an unconstrained HMM overfits | moderate | Table 1, 15 parameter sets per size (THEORY-tmptn4xd) |
| C5 | Gibbs with ten samples per variable is slower than the variational methods and worse on the smaller problems | moderate | Table 1, Figure 4, one machine |
| C6 | Factorial HMMs predict Bach chorale melodies better than HMMs | moderate | Figure 5, one data set, read from a chart |

## Concepts

- **Factorial HMM**: M independent hidden chains jointly emitting each
  observation.
- **Explaining away**: posterior coupling of a priori independent causes
  of a common observation.
- **CFVA / SVA**: the completely factorized and structured variational
  approximations.
- **Fictitious observation h_t^(m)**: the structured approximation's
  per-chain evidence, fitted to the other chains' residual.

## Connections

The infinite factorial HMM (LIT-1577, NOTE-1199) is this model with binary
chains and an unbounded M under the Markov IBP, and its inference uses
Van Gael et al.'s beam sampler (LIT-tmp0oa8w) in place of these E steps.
Its static ancestor is Ghahramani's factorial learning, which Griffiths
and Ghahramani cite among the "factorial" latent-feature models
(LIT-tmp3u0k8). Its linear-Gaussian observation with binary chains is the
iFHMM's ICA-like likelihood, which Knowles and Ghahramani's infinite ICA
(LIT-tmpezspt) shares without the chains.

## Bearing on the record

- **CASE-165, the construction.** The case's output u = Σ_k B a W o +
  W^private o, with each B_{ek} a two-state chain over days, is per
  member a factorial HMM with K binary chains and a linear observation.
  So the case's model inherits two facts from this paper. First, the
  chains are coupled given the outputs, which is the mechanism of the
  case's item 3: a feature's contribution can be explained by another's.
  Second, exact inference costs O(TMK^{M+1}): at the case's K = 16 binary
  features, 16 · 2¹⁷ ≈ 2.1 million terms per member per day, so a fit would
  need an approximation such as the structured one here, or the beam
  sampler (LIT-tmp0oa8w).
- **CASE-165, item 3, decoupling.** Note 3 says the chains decouple when
  the columns of W^(m) and W^(n) are orthogonal and C is diagonal. What is
  needed is that the cross term W^(m)′C^{−1}W^(n) be additively separable
  (for instance zero); Euclidean orthogonality gives that only when C is
  isotropic. With orthogonal features, coupling in the case's model would
  vanish only if the noise were the same in every output dimension.
- **LIT-1577.** NOTE-1199's "a factorial HMM whose number of hidden chains
  is learned" now has its original in the record.

No instruction for machine-learning practice; nothing for the anthology.

## Limitations

- **Experiment 1 is small**: sequences of length 20, four observed
  dimensions, a near-noiseless C = 0.0025I, one run per parameter set, and
  significance tests unnamed.
- **The Bach comparison is read from a chart**, with attributes such as
  key signature and fermata treated as Gaussian; the authors note that
  the likelihoods measure relative coding cost only.
- **Errors and slips.**
  - **Note 3 is wrong as stated.** Orthogonal columns and a diagonal C do
    not make the chains conditionally independent given an observation.
    With W^(m) = [(1, 1)′, (2, 2)′], W^(n) = [(1, −1)′, (3, −3)′] (every
    column of one orthogonal to every column of the other) and C =
    diag(1, 2), the cross term W^(m)′C^{−1}W^(n) = [[0.5, 1.5], [1, 3]] is
    not separable, and the posterior odds ratio of the two chains is
    e^{−1} ≈ 0.37 whatever Y_t is (record script, 2026-10-27). The
    condition holds for C ∝ I, or for orthogonality in the C^{−1} inner
    product.
  - Note 7 says standard errors are "a factor of 3.8 smaller" than the
    standard deviations; with 15 runs per cell the factor is √15 = 3.87,
    3.9 to two figures.
  - "The test set likelihood for the best factorial HMM was an order of
    magnitude larger" leaves its unit open (per event, per sequence or
    for the whole test set); it cannot be checked without the chart.
  - Typos: "the the state variables", "we can chose", "the the form".

## Open questions

- How does the structured approximation behave when chains are strongly
  coupled by the observation, as near-duplicate features would be?
