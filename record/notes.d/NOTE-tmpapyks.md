---
status: Read
paper: LIT-246
title: 'Poole et al. — On Variational Bounds of Mutual Information'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from the arXiv PDF (1905.06922v1, the only version, 14
    pages), text extracted with pdftotext in both reading-order and layout
    modes: abstract, §§1–4, figure captions 1–7, and appendices A–E
    (Tables 1–3, experimental details, the hyperparameter sweep, the I_JS
    derivation and the alternative I_TNCE derivation). Equations were read
    from the layout extraction, which garbles fractions; Eq. 10's indices
    were checked there and against Table 2 and Eq. 12. The figures are
    plots without a text layer and were read from their captions and the
    text that describes them. Replaces the seeded skim NOTE-233.
date: '2026-10-14'
summary: >-
  The common variational lower bounds on mutual information (Barber–Agakov,
  Donsker–Varadhan, NWJ, MINE, InfoNCE) are derived from one unnormalized
  Barber–Agakov bound. InfoNCE is the multi-sample NWJ bound with the batch
  mean as its partition estimate, which proves it a lower bound for every
  critic when the K pairs are i.i.d.; it is capped at log K. An interpolated
  family I_α trades InfoNCE's bias against NWJ's variance, and none of them
  gives low bias and low variance when MI is large and the batch small.
---
<!-- inactive-ok-file: THEORY-001 THEORY-006 LIT-226 LIT-256 LIT-258 NOTE-233 — Proposed, Deferred or Skimmed; the theories that cite this paper, the work that relies on its §2.5, the papers set beside it, and the skim this reading replaces -->

# NOTE-tmpapyks: Poole et al. — On Variational Bounds of Mutual Information

## Contribution

Before this paper the neural MI estimators of the day (MINE, NWJ/f-GAN-KL,
CPC's InfoNCE, the Barber–Agakov bound used by variational information
bottlenecks) were separate devices with separate derivations, and CPC's
claim that InfoNCE lower-bounds MI rested on an approximation. After it,
they are one family: each is the unnormalized Barber–Agakov bound with a
particular choice of a normalizing parameter a(y). InfoNCE is proved a lower
bound exactly, the bias and variance of each member are characterized on
Gaussians with known MI, and a one-parameter family I_α interpolates between
InfoNCE and NWJ.

## Key insight

Put an energy-based variational family q(x|y) = p(x)e^{f(x,y)}/Z(y) into the
Barber–Agakov bound and the intractable entropy cancels, leaving one
intractable term, log Z(y). Every estimator is a different way of bounding
that term. Bounding it with a learned or constant a(y) gives unbiased but
high-variance single-sample bounds (TUBA, NWJ). Bounding it with the batch
mean (1/K)Σ e^{f(x_i,y)} gives InfoNCE, whose variance is low because the
positive term appears in its own denominator, and which for that same reason
can never exceed log K.

## Assumptions

- **Densities exist** for p(x,y), p(x), p(y), and the expectations in each
  bound are finite. The paper does not state measure-theoretic conditions.
- **Unnormalized bounds (§2.2):** a(y) > 0; the inequality
  log x ≤ x/a + log a − 1 for x, a > 0.
- **Multi-sample bounds (§2.3):** X_2:K are independent of (X_1, Y). The
  identity I(X_1, X_2:K; Y) = I(X_1; Y) holds for any r(x_2:K) independent
  of X_1 and Y. For InfoNCE specifically, r_{K−1}(x_2:K) = ∏_{j=2}^K p(x_j),
  i.e. the negatives are drawn from the true marginal, and the expectation
  in Eq. 10 is over K independent samples ∏_j p(x_j, y_j).
- **Structured bounds (§2.5):** the encoder p(y|x) is known and tractable,
  as for a stochastic representation y of data x; the total-correlation
  bound additionally assumes a mean-field encoder p(y|x) = ∏_i p(y_i|x).
- **Experiments:** infinite data and no overfitting (§4 states this as a
  limitation); 20-dimensional correlated Gaussians with
  I = −(d/2) log(1 − ρ²), d = 20 (App. B), and the same with y mapped to
  (Wy)³, W_ij ∼ N(0,1).

## Key results

- **Barber–Agakov (Eqs. 1–2).** Upper: I(X;Y) ≤ E_{p(x)}[KL(p(y|x)‖q(y))] ≜ R,
  tight at q(y) = p(y). Lower: I(X;Y) ≥ E_{p(x,y)}[log q(x|y)] + h(X) ≜ I_BA,
  tight at q(x|y) = p(x|y).
- **Unnormalized BA (Eqs. 3–4).** With q(x|y) = p(x)e^{f(x,y)}/Z(y),
  Z(y) = E_{p(x)}[e^{f(x,y)}]: I ≥ E_{p(x,y)}[f(x,y)] − E_{p(y)}[log Z(y)] ≜ I_UBA,
  "tight when f(x,y) = log p(y|x) + c(y), where c(y) is solely a function of y".
- **Donsker–Varadhan (Eq. 5).** Jensen on E[log Z]: I_UBA ≥
  E_{p(x,y)}[f] − log E_{p(y)}[Z(y)] ≜ I_DV. Still intractable; a Monte-Carlo
  I_DV as in MINE gives "estimates that are neither an upper or lower bound
  on MI".
- **TUBA and NWJ (Eqs. 6–7).** I ≥ I_UBA ≥ E_{p(x,y)}[f] −
  E_{p(y)}[E_{p(x)}[e^f]/a(y) + log a(y) − 1] ≜ I_TUBA, for any a(y) > 0, with
  unbiased estimates and gradients. a(y) = e gives I_NWJ =
  E_{p(x,y)}[f] − e^{−1}E_{p(y)}[Z(y)], with "a unique optimal critic
  f*(x,y) = 1 + log p(x|y)/p(x)". With a(y) an exponential moving average of
  e^f, the gradients of I_TUBA "exactly yield" MINE's bias-corrected
  gradient, so that heuristic is the unbiased gradient of a valid bound.
- **InfoNCE as a bound (Eqs. 8–10).** Applying NWJ to I(X_1, X_2:K; Y) with
  critic 1 + log(e^{f(x_1,y)}/a(y; x_1:K)) and
  a = m(y; x_1:K) = (1/K)Σ_{i=1}^K e^{f(x_i,y)}, then averaging over the K
  choices of which x is paired with y, the last term of Eq. 8 becomes the
  constant 1 (Eq. 9) and
  I(X;Y) ≥ E[(1/K)Σ_{i=1}^K log( e^{f(x_i,y_i)} / ((1/K)Σ_{j=1}^K e^{f(x_i,y_j)}) )] ≜ I_NCE.
  This "provides a proof that I_NCE is a lower bound on MI"; footnote 2:
  "The derivation by van den Oord et al. (2018) relied on an approximation,
  which we show is unnecessary." *Holds when:* any critic f; K pairs i.i.d.
  from the joint.
- **Index convention in Eq. 10.** As printed, the denominator sums over y_j
  for fixed x_i. The derivation (m(y; x_1:K) sums over x_i for fixed y),
  Table 2 (Σ_j f(y_i, x_j)) and Eq. 12 (Σ_j p(y_i|x_j)) all sum over x_j for
  fixed y_i. The derivation proves the second form. The printed Eq. 10 is the
  same bound with the roles of X and Y exchanged, which also holds by
  symmetry. The stated optimal critic, log p(y|x) + c(y), is correct for the
  derived form; for the printed form the free term would be a function of x.
  This settles the check left open by the skim ([NOTE-233](NOTE-233.md)).
- **Optimal InfoNCE critic.** "the optimal critic for I_NCE is
  f(x,y) = log p(y|x) + c(y) where c(y) is any function that depends on y but
  not x (Ma & Collins, 2018)". Stated with a citation, not proved here.
  Equivalently, log of the density ratio p(y|x)/p(y) plus a function of y.
- **The log K ceiling.** "As pointed out in van den Oord et al. (2018), I_NCE
  is upper bounded by log K, meaning that this bound will be loose when
  I(X;Y) > log K." Each summand is at most log K because e^{f(x_1,y)} is one
  of the K terms of the denominator. "Although the optimal critic does not
  depend on the batch size … accurately estimating mutual information still
  needs a large batch size at test time if the mutual information is high."
- **Interpolated bound (Eq. 11).** Critic 1 + log(e^{f(x_1,y)} /
  (αm(y; x_1:K) + (1 − α)q(y))), α ∈ [0,1], gives I_α; α = 0 is NWJ, α = 1 is
  InfoNCE; I_α ≤ log(K/α). The optimal critic for I_α (f = log p(y|x),
  q = p(y)) is a conjecture, not proved.
- **Structured bounds (§2.5).** With p(y|x) known: InfoNCE with
  f = log p(y|x) (Eq. 12) and a leave-one-out upper bound
  I ≤ E[(1/K)Σ_i log(p(y_i|x_i) / ((1/(K−1))Σ_{j≠i} p(y_i|x_j)))] (Eq. 13)
  sandwich MI with no learned parameters; they differ only in whether
  p(y_i|x_i) is in the denominator. A reparameterized NWJ critic
  1 + log p(y|x)/q(y) gives I ≥ R + 1 − E_{p(y)}[E_{p(x)}[p(y|x)]/q(y)]
  (Eq. 14), valid for any q, including unnormalized. Total correlation
  TC(Y) = Σ_i I(X; Y_i) − I(X;Y) is upper-bounded by upper bounds on each
  I(X; Y_i) and a lower bound on I(X;Y).
- **Density-ratio estimators to bounds (§2.6, App. D).** "the optimal critic
  for both I_NWJ and I_NCE are functions of the log density ratio
  log p(y|x)/p(y)". A critic trained on a Jensen–Shannon (f-GAN) objective,
  read out as V ≈ log p/q and plugged into NWJ, gives
  I ≥ 1 + E_{p(x,y)}[V] − E_{p(x)p(y)}[e^V] ≜ I_JS (Eq. 18), a bound rather
  than the plug-in estimate of earlier work.
- **Experiments (§3, App. C).**
  - Single-sample bounds are high-variance; InfoNCE estimates "saturate at
    log(batch size)"; I_α gives the best estimates on the cubic problem.
  - With the optimal critic, NWJ is unbiased but high-variance at large MI
    and small batch, while InfoNCE's bias "grows linearly with MI" once it
    saturates (Fig. 3).
  - For encoder gradients, the α with smallest MSE is near 1 for small MI
    and batch, near 0 for large MI and batch (Fig. 4).
  - After a full sweep (App. C.1, Table 3), I_α is best or tied at every MI level
    on both problems. At true MI 10, the Gaussian best estimates are I_α 8.9,
    I_NCE 6.0, I_JS 8.1, I_NWJ 8.0; with p(y|x) known, Eq. 12 reaches 4.8
    and Eq. 14 reaches 10.0.
  - Joint critics beat separable ones for NWJ and JS; the multi-sample
    bounds are more robust to critic architecture.
  - On dSprites, I_JS with a structured critic, a TC upper bound and a
    smoothness penalty learns x/y position and scale, not rotation (Fig. 5).
- **Discussion.** "none of the approaches we considered here are capable of
  providing low-variance, low-bias estimates when the MI is large and the
  batch size is small", consistent with McAllester & Stratos.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | NWJ, TUBA, DV and InfoNCE all derive from the unnormalized Barber–Agakov bound | strong | derivation, Eqs. 3–10 |
| C2 | InfoNCE is a lower bound on MI for every critic, given K i.i.d. joint pairs | strong | Eqs. 8–10, exact |
| C3 | I_NCE ≤ log K, so it is loose when I(X;Y) > log K | strong | each term's ratio is at most K; Fig. 2–3 |
| C4 | The optimal InfoNCE critic is log p(y|x) + c(y) and does not depend on K | moderate | stated, cited to Ma & Collins (2018), not proved here |
| C5 | MINE's bias-corrected gradient is the unbiased gradient of I_TUBA with an EMA a(y) | strong | derivation in §2.2 |
| C6 | I_α trades bias against variance and gives lower MSE than NWJ or InfoNCE in some regimes | moderate | Figs. 3, 6, 7 and Table 3, on 20-d Gaussian and cubic toys only |
| C7 | The optimal critic of I_α is f = log p(y|x), q = p(y) | weak | conjecture, §2.4 |
| C8 | With a known encoder, Eqs. 12–13 sandwich MI without learned parameters | strong | derivation, §2.5; loose for small batches (Fig. 3) |
| C9 | No bound studied gives low bias and low variance at large MI and small batch | moderate | experiments, §3; framed as consistent with McAllester & Stratos, not proved |

## Method

The I_α estimator: draw a minibatch of K pairs; compute the batch mean
m(y; x_1:K) of e^{f(x_i,y)}; mix it with a learned unnormalized marginal q(y)
by α; evaluate Eq. 11, with the second expectation estimated by a held-out
(leave-one-out) y from the minibatch as an independent draw from p(y);
maximize over f and q (and, in InfoMax, the encoder).

## Concepts

- **Critic** — the function f(x,y) in an energy-based variational
  distribution q(x|y) ∝ p(x)e^{f(x,y)}; not necessarily normalized.
- **Unnormalized / normalized bounds** — Table 1's "Norm." column marks
  whether a bound needs a normalized critic (BA) or works with an
  unnormalized one (all others).
- **Multi-sample bound** — a bound on I(X_1, X_2:K; Y) = I(X_1; Y), where
  extra independent samples are allowed into the critic.
- **Rate R** — E_{p(x)}[KL(p(y|x)‖q(y))], the BA upper bound, as in
  "Fixing a broken ELBO".
- **Separable vs joint critic** — h(x)ᵀg(y) (2N forward passes) against
  h([x,y]) (N² passes).

## Connections

It builds on Barber & Agakov (2003), Donsker & Varadhan (1983), Nguyen,
Wainwright & Jordan (2010) and Nowozin et al.'s f-GAN, and recasts MINE
(Belghazi et al., [LIT-256](../literature.d/LIT-256.md)) and CPC (van den Oord et al., [ANTH-LIT-589](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-589.md))
inside one family. The optimal-critic claim for InfoNCE is taken from Ma &
Collins (2018), and the limit on estimation from McAllester & Stratos (2018).
Tschannen et al. ([LIT-247](../literature.d/LIT-247.md)), from the same group, cite this paper for
the InfoNCE bound and its optimal critic, and show that the proof's i.i.d.
assumption is where it fails under dependent negatives (their App. D).

## Bearing on the record

- **[THEORY-006](../theory.d/THEORY-006.md)'s `promote_when` is met for this paper.** §2.3, Eqs. 8–10,
  proves I(X;Y) ≥ I_NCE for every critic, exactly, with negatives drawn
  independently from the marginal (r_{K−1} = ∏ p(x_j); expectation over K
  i.i.d. joint pairs). The log K ceiling and the K-independence of the
  optimal critic are stated as [THEORY-006](../theory.d/THEORY-006.md) says. Three refinements:
  - Eq. 10 is printed with its indices transposed relative to the
    derivation (see Key results). The bound holds either way; the optimal
    critic's free term is c(y) only for the derived form.
  - That the optimal critic does not depend on K is asserted, with Ma &
    Collins cited for the critic's form, not proved in this paper.
  - [THEORY-006](../theory.d/THEORY-006.md)'s "What this does not say" says the result covers nothing
    "for negatives drawn from other positive pairs in the same batch". As far
    as this paper goes, that is wrong in the one-directional case. Eq. 10's
    expectation is over K i.i.d. joint pairs, with each y_i's negatives being
    the other pairs' x_j. That is the in-batch construction. What it does not
    cover is non-i.i.d. batches (Tschannen et al., [LIT-247](../literature.d/LIT-247.md), App. D), and
    any symmetric or two-sided loss that also draws same-view negatives. The
    second is the NT-Xent case [LIT-258](../literature.d/LIT-258.md) is cited for, which this reading
    does not check.
- **[THEORY-001](../theory.d/THEORY-001.md) cites §2.3 as support** for the density ratio as the
  shared optimum. The paper says the optimal InfoNCE critic is
  log p(y|x) + c(y), i.e. the log ratio plus an arbitrary function of y, and
  (§2.6) that the optimal NWJ and InfoNCE critics are functions of
  log p(y|x)/p(y). It says this for general densities, not a finite
  augmentation space. It states the InfoNCE optimum on Ma & Collins's
  authority, without derivation. So it supports [THEORY-001](../theory.d/THEORY-001.md)'s statement in
  form, more weakly in proof, and it says nothing about the spectral or
  logistic losses. Its NWJ critic, 1 + log ratio, is unique, which is
  closer to [THEORY-001](../theory.d/THEORY-001.md)'s "exactly K⁺" for the logistic loss, but NWJ is not
  that loss.
- **CEB ([LIT-226](../literature.d/LIT-226.md)).** §2.5 (Eqs. 12–14) is read in full here. Whether
  CEB's footnote 7 uses exactly these bounds is not checked from the CEB side.
- The paper carries methodological advice for MI estimation in machine
  learning (which bound to use at which batch size and MI). That part is
  the anthology's kind of material; the `anthology-candidate` flag stands.

## Limitations

- Experiments are on 20-dimensional Gaussians, a cubic transform of them,
  and dSprites; no large-scale representation learning (§4 defers it).
- The analysis assumes infinite data and no overfitting (§4).
- The optimal critic of I_α is a conjecture; the InfoNCE optimal critic is
  cited, not derived.
- No rate is given for how fast I_NCE approaches I(X;Y) as K grows.
- dSprites results recover position and scale, not rotation; the
  disentanglement comes with added smoothness and TC constraints, not from
  MI alone (the paper says so, citing Krause et al. and Locatello et al.).

## Open questions

- Whether low-bias, low-variance MI estimation at large MI is impossible in
  general or only without distributional assumptions (posed in §4).
- Whether estimating gradients of MI is easier than estimating MI (§4).
- Whether MI maximization is a better representation-learning objective
  than other self-supervised ones (§4). Tschannen et al. ([LIT-247](../literature.d/LIT-247.md)) take this
  up and answer that it is not sufficient.
