---
status: Read
paper: 'LIT-tmpcewsq'
title: 'Wu, Yang & Sun — Self-training: denoising vs. signal forgetting'
version: 1
history:
- version: 1
  date: '2026-10-31'
  note: >-
    Read from the arXiv preprint 2602.14029v1 (15 February 2026), 29 pp.
    (8 main), fetched 2026-10-31. The two-column layout was extracted
    column by column with `pdftotext -x/-W`; page numbers are the arXiv
    copy's. I read the abstract, §§1–6, Appendix A (CIFAR-10), B (the
    isotropic case), G (related work) and H (simulation settings), and
    the captions of Figs. 1–6. The proofs of Appendices C–F (deterministic
    equivalents, concentration, iterated GCV, lemmas) were skimmed for
    structure, not checked. I checked Theorem 3.2 by Monte Carlo (numpy,
    my own script; n = 400, p = 800, spike s = 5, r = 1, σ = 1, six
    trials, eight rounds): the simulated risk followed the formula to
    within 0.06 at every round, falling from 1.25 to 1.10 at t = 1 and
    rising to 3.05 at t = 7. Every student interpolated its teacher's
    pseudo-labels to 10⁻¹⁴.
date: '2026-10-31'
summary: >-
  In overparameterized linear regression, iterating self-training with
  fresh covariates, noiseless pseudo-labels and minimum-norm students
  multiplies the estimate by a fresh random orthogonal projection each
  round. Noise inherited from the first fit decays geometrically; signal
  along a direction of variance s decays at the slower rate s/(s + τ).
  Risk is therefore U-shaped when the covariance is anisotropic, monotone
  when it is isotropic, and tends to the risk of predicting zero. Each
  student fits its teacher exactly on its own sample while losing the
  teacher's function elsewhere.
---
<!-- inactive-ok-file: QUESTION-016 — Open; the question this reading bears on, cited as open -->

# NOTE-tmpbslp3: Wu, Yang & Sun — Self-training: denoising vs. signal forgetting

## Contribution

An exact high-dimensional account of iterated self-training in
overparameterized linear regression. Deterministic-equivalent recursions
give the prediction risk at every round, with concentration bounds
uniform over ridge parameters (Theorem 4.2). The risk splits into a
systematic part that grows (signal forgetting) and a stochastic part that
decays (denoising), whose rate mismatch gives a U-shaped curve and an
optimal stopping round (Theorem 3.2). An iterated GCV estimates the curve
from the first round's data alone (Theorem 4.3).

## Key insight

With p > n_t a minimum-norm student trained on noiseless labels
Y_t = X_t β̂_{t−1} is β̂_t = P_t β̂_{t−1}, with P_t the orthogonal
projection onto the row space of a fresh X_t (§3.2). Each round
annihilates whatever of the teacher falls in a random (p − n_t)-
dimensional null space. Noise is spread evenly over directions and loses
about a fraction τ/(1 + τ) per round. A strong signal direction is
nearly always inside the row space and survives. Weak directions go the
way of noise. Each projection is idempotent, but a new one is drawn
every round, and the product of independent projections tends to zero.

## Assumptions

- **Linear model** y = xᵀβ + ε with Gaussian noise **only at t = 0**
  (Assumption 2.4). Later labels are the teacher's exact predictions.
- **Fresh, independent Gaussian covariates every round** (Assumptions
  2.1–2.2). With the same X_t reused, P_t would repeat and the iterates
  would not change after round 1. In the underparameterized regime
  p ≤ n_t, P_t = I and nothing happens (§3.2).
- **Proportional asymptotics** p, n → ∞ with ρ = p/n > 1, τ = ρ − 1;
  uniformly well-conditioned covariances (Assumption 2.3).
- **Ridgeless students** in §3; ridge in §4.
- **Spiked models** (Assumptions 3.1, 3.5): β lies in the spiked
  subspace.

## Key results

- **Theorem 3.2** (single spike, p. 4):
  B*_t = r²s(1 − (s/(s + τ))^{t+1})²;
  V*_t = V*_{t−1}/(1 + τ) + τr² s^{2t+1}/(s + τ)^{2(t+1)},
  V*_0 = σ²/τ + τ s r²/(s + τ)². B*_t → r²s, the risk of β̂ = 0, and
  V*_t → 0 (Cor. 3.3). Checked by Monte Carlo (history).
- **Rate mismatch** (p. 5; App. B): with r = 0, V*_t = σ²/(τ(1 + τ)^t);
  with s = 1, risk is monotone in t, so the U-shape needs anisotropy.
- **Strong spikes** (Cor. 3.4): as s → ∞, B*_t → 0 and
  V*_t → σ²/(τ(1 + τ)^t), and B*_t ≈ r²(t + 1)²τ²/s.
- **Multi-spike** (Theorem 3.6): directions are filtered independently
  at κ_j = s_j/(s_j + τ), so weak signal directions are forgotten with
  the noise: "soft feature selection".
- **General covariances** (Def. 4.1, eq. 10): the filter Q_t =
  (Σ_t + τ_tI)⁻¹Σ_t and propagators Q_{t:h}; Theorem 4.2's concentration
  has probability Cp·exp(−pϵ⁴/C), uniformly over λ ∈ [0, M].
- **Iterated GCV** (eqs. 11–12, Theorem 4.3) is uniformly consistent for
  R(β̂_t) + σ².
- **Experiments**: Σ_ii = 1/i, n = 500, 50 rounds, 10 trials: theory
  matches simulation and the U-shape persists (Fig. 5). Iteration beats
  optimally tuned ridge once s is large (Fig. 3b). ResNet-50 on CIFAR-10
  with symmetric label noise, four rounds on fresh subsets (App. A): at
  noise 0.4 the error falls from 47.7% to 43.6% and rises to 45.0%; at 0.8
  it falls throughout. The main text labels the noise σ, the appendix η.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Risk is systematic error that grows plus stochastic error that decays, in closed form for spiked models | strong | Theorems 3.2, 3.6, 4.2; Monte Carlo agrees (mine and theirs) |
| C2 | The U-shape requires anisotropy | strong | App. B, Corollary B.1 |
| C3 | Self-training acts as a direction-adaptive filter distinct from ridge and can beat optimally tuned ridge for strong spikes | moderate | Theorem 3.6; Fig. 3b numerically, no theorem (§6 leaves it open) |
| C4 | Iterated GCV selects the stopping round from first-round data | strong in the model | Theorem 4.3, Fig. 4 |
| C5 | The trade-off is "a fundamental structural property ... that transcends the linear regime" | weak | one CIFAR-10 experiment, four rounds |

## Method

Algorithm 1: fit β̂_0 by ridge or ridgeless regression on noisy data; for
t ≥ 1 draw fresh X_t, set Y_t = X_t β̂_{t−1}, refit.

## Concepts

- **Signal forgetting** — growth of the systematic error
  β⊤(Q_{t:0} − I)⊤Σ(Q_{t:0} − I)β as the propagated estimate shrinks.
- **Denoising** — decay of the stochastic error inherited from the noisy
  first fit.
- **Spectral filter** — Q_t's action φ_t(λ) = λ/(λ + τ_t) on each
  covariance eigendirection.

## Connections

It contrasts itself with model collapse under recursive training with
fresh label noise (Shumailov; Dohmatob et al.; Gerstgrasser et al.,
LIT-971 and THEORY-289). There noise enters every round and error grows.
Here noise enters once and is filtered out. It relates the mechanism to
weak-to-strong generalization (Burns et al. 2024). Mobahi et al.
(LIT-tmptkqrv) is the same loop on fixed inputs, where the loss comes
from the regularizer.

## Bearing on the record

- **A16's description holds.** "Distinguishes denoising benefits from
  signal forgetting through repeated projections onto changing
  data-dependent subspaces" is exact: the projections are literal
  orthogonal projections, and the change of subspace each round is what
  drives the loss. It confirms A16's idempotence remark: with X_t reused,
  the iterates stop changing after one round (THEORY-tmpp515i).
- **CLAIM-tmpekkm7 (no change needed; an illustration).** Every student
  here fits its teacher exactly on the contexts it was trained on, and
  differs from it everywhere else. The distillation loss on the sample is
  zero, yet risk under the deployment distribution first falls and then
  rises toward the null predictor. That is the claim's "fidelity measured
  in ordinary operation certifies nothing" in its sharpest form: a
  perfect student on the sampled contexts, with no guarantee off them.
- **QUESTION-016.** A precise answer in one model. Iterated
  reconstruction through fresh low-rank views preserves sufficiency for
  tasks carried by high-variance directions and destroys it for
  low-variance ones, at rates s_j/(s_j + τ) per round. In the limit it
  destroys it for every task.
- **CLAIM-081 and CLAIM-270.** The chain forgets its ancestor β̂_0
  entirely, and that is first good and then bad for fidelity to the
  world β. The ancestor contains noise, and the first thing forgotten is
  the noise. "Forgetting the ancestor" and "losing fidelity to the
  source" separate here, and their difference is the U-shape.
- **TERM-097.** Each round is perfect coherence between student and
  teacher on the student's sample, while fidelity to β varies freely.
- **An instruction for ML practice is present** (stop self-training at
  the iGCV minimum). That belongs to the Anthology of the SOTA; the LIT
  keeps the `anthology-candidate` flag.

## Limitations

- **Fresh independent covariates every round** are what make the
  dynamics tractable. They are also what drive the forgetting; the
  authors name reused data and filtered pseudo-labels as open (§6).
- **Linear, Gaussian, proportional asymptotics.** The deep-network
  evidence is one CIFAR-10 experiment of four rounds, without stated
  repetitions.
- **The comparison with ridge** is numerical (Fig. 3b), not a theorem.
- **Proofs not checked** by this reader beyond the spiked Monte Carlo.

## Open questions

- With data reused across rounds, or pseudo-labels filtered, is the
  forgetting slower, absent, or replaced by something else?
- Does a nonlinear student's changing representation stabilize the
  strong directions or let them drift, as the authors ask?
