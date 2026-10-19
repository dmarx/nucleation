---
number: 806
status: Read
formerly:
- NOTE-tmps2bys
paper: LIT-233
title: 'Sefidgaran & Zaidi — Data-Dependent Generalization Bounds via Variable-Size Compressibility'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from the arXiv v3 PDF (arxiv.org/pdf/2303.05369, 28 pp.,
    11 Jun 2024, "accepted for publication in IEEE Transactions on
    Information Theory"), text extracted with pdftotext, with pages 4, 8,
    9 and 10 rendered as images to check where square roots end and to
    read Figure 1: §§I–VI, Appendices A–D, and every proof in Appendix E
    (E-A to E-K). The proofs were followed step by step. In E-I (the
    O(1/n) bounds for Haghifam et al.'s example) the order of each term
    was followed, but the constants were not re-derived. The IEEE Xplore
    version was not read. The skim note filed with the paper is NOTE-216.
date: '2026-10-14'
summary: >-
  If the number of codewords allowed for covering a block of experiments
  may depend on the realised sample and output, generalisation bounds
  can be data-dependent. The general bounds are change-of-measure
  inequalities that cover tail, PAC-Bayes and in-expectation forms. With
  the rate set to log dP_{W|S}/dP(W) for a fixed prior P, the tail bound
  is the disintegrated PAC-Bayes bound. A new trajectory bound is
  data-dependent except for a coupling term, and its experiment drops
  that term.
---
<!-- inactive-ok-file: NOTE-216 — Superseded; the skim of this paper, whose open questions this reading answers -->

# NOTE-806: Sefidgaran & Zaidi — Data-Dependent Generalization Bounds via Variable-Size Compressibility

## Contribution

The earlier rate-distortion bounds ([LIT-236](../literature.d/LIT-236.md)) have a fixed rate, set by
the joint law P_{S,W}, so they cannot be computed from one sample. This
paper lets the size of the hypothesis book depend on the realised blocks,
through Σ_i R_{S_i,W_i}. The resulting bounds depend on the sample at
hand. In this form PAC-Bayes, mutual-information, rate-distortion and
some intrinsic-dimension bounds are special cases of one family of
change-of-measure inequalities. It adds a lossy PAC-Bayes bound
(Proposition 1), finite for deterministic algorithms with continuous
parameters, and a bound on the average generalisation error along an
optimisation trajectory in terms of the trajectory's rate-distortion
function (Theorem 7).

## Key insight

A fixed-rate code pays the same number of bits for every block. A
variable-rate code pays more for the samples on which the algorithm's
output is surprising. The bound then follows the actual sample's
surprise, not its average. In the PAC-Bayes case the rate is exactly the
pointwise information density log (dP_{W|S}/dP)(W). That is how many more
nats it costs to code the output with a fixed prior P than with the
algorithm's own posterior. It is a Shannon code length relative to a
chosen prior, in the line of Blum and Langford's PAC-MDL. It is not a
Kolmogorov or two-part code of the sample.

## Assumptions

- **Setting.** S = (Z_1, …, Z_n) i.i.d. from μ; a possibly stochastic
  algorithm P_{W|S}; gen(s, w) = L(w) − L̂(s, w).
- **Loss.** σ-subgaussian for every w (Theorem 1); in [0, 1] for
  Theorems 6 and 7; L-Lipschitz in a distortion ρ on W for Theorem 7.
- **Rates.** R_{s,w} ≥ 0 with R_max = sup R_{s,w} < ∞ (Def. 2).
- **Finite S × W** for Theorem 2, which proves compressibility by
  method-of-types coding. The general Theorems 3–5 need no finiteness.
  Their proofs are variational.
- **Theorem 7** needs the coupling coefficient M := exp(sup_{ν_S ∈ G^δ_S}
  E_{π_S} log dπ_S/d[π_S ν_S]_{W^T}) to be finite. G^δ_S is the KL ball
  of radius log(1/δ) around μ^{⊗n}, so M depends on the unknown μ.

## Key results

- **Distortion (eq. 10).** d(w, ŵ; s) = gen(s, w)² − gen(s, ŵ)². The
  variable-size scheme compresses squared generalisation error.
- **Theorem 1.** If A is (R_{S,W}, ε, δ; d_m)-compressible (Def. 2), then
  with probability ≥ 1 − δ, gen(S, W) ≤ √(4σ²(R_{S,W} +
  log(√(2n)/δ))/(2n − 1) + ε). ε sits inside the root. The extra
  log √(2n) comes from E exp(λ gen²/(2σ²/n)) ≤ 1/√(1 − λ) with
  λ = (2n−1)/(2n).
- **Theorem 2 (finite S × W).** A is compressible with rate R_{S,W} if,
  for every ν_{S,W} in the KL ball G^δ_{S,W},
  inf_{p_{Ŵ|S}} inf_{q_Ŵ} {D_KL(p_{Ŵ|S}ν_S ‖ q_Ŵ ν_S) − D_KL(ν_{S,W} ‖
  P_{W|S}ν_S)} ≤ E_ν[R_{S,W}], over p_{Ŵ|S} within distortion ε (eqs.
  12–13). The statement prints the compressibility triple with σ where δ
  is meant.
- **PAC-Bayes as a case.** With R_{S,W} := log (dP_{W|S}/dP)(W) for a
  fixed prior P, condition (12) holds at ε = 0. "The resulting tail bound
  recovers the PAC-Bayes bound of [Catoni], [Blanchard–Fleuret]", the
  disintegrated form of McAllester's.
- **Theorem 3 (general tail bound for any f(S, W)).** f(S, W) ≤ Δ(S, W)
  with probability ≥ 1 − δ if, for every ν in F^δ_{S,W} (the KL ball
  intersected with the event f > Δ), eq. 17 holds, or for α > 1 its
  Rényi form eq. 19. The proof (E-C) is Lemma 1, a change of measure to
  P conditioned on the bad event, plus Donsker–Varadhan. Coding is not
  used. The compressibility reading is commentary on it.
- **Theorem 4 (tail bound on E_{W∼π} f, for all π at once).** With λ = 1
  and a fixed, possibly data-dependent prior q_{W|S}, eq. 29: for all π,
  E_π f(S, W) ≤ D_KL(π ‖ q_{W|S}) + log E_{P_S q_{W|S}} e^{f(S,W)} +
  log(1/δ). This equals Rivasplata et al.'s Theorem 1.ii, which Clerico et
  al. note contains most PAC-Bayes bounds.
- **Theorem 5 (in expectation).** E f(S, W) ≤ inf (1/λ)[D_KL(p_{Ŵ|S}P_S ‖
  q_{Ŵ|S}P_S) + log E e^{λg}] + ε. With Ŵ = W, q the marginal of W and
  λ = √(2nI(S;W)/σ²) it is Xu–Raginsky's Theorem 1.
- **Fast rate (§IV-A).** With f = n·kl(L̂‖L), with probability ≥ 1 − δ,
  gen ≤ √(L̂(S, W)·C/n) + C/n, where C = 4σ²(sup_{ν ∈ G^δ} I(S; W) +
  log(2√n/δ)). This is O(1/n) when L̂ = 0, but C depends on μ.
- **Proposition 1 (lossy PAC-Bayes, new).**
  - (i) For all π, E_π f(S, W) ≤ D_KL(p_{Ŵ|S,π} ‖ q_{Ŵ|S}) + log E e^{g} +
    log(1/δ) + ε, for any p_{Ŵ|S,π} within ε.
  - (ii) f(S, W) ≤ E_{p_{Ŵ|W}} log(dp*_{Ŵ|S}/dq_{Ŵ|S}) + log E e^{g} +
    log(1/δ) + ε.
  - For W the mean of n vectors in R^d, with a loss Lipschitz in the
    squared distance, classical PAC-Bayes bounds are infinite. (ii) gives
    √(2σ²(2√(L·d·Σ_j(Σ_i Z_{ij}/n)²) + log(1/δ))/n), using Gaussian
    noise as the surrogate.
- **Theorem 6 (trajectory, data-independent).** For loss in [0, 1], with
  probability ≥ 1 − δ, for all π, E_{W^T∼π} gen(S, W^T) ≤
  √((sup_{ν_S ∈ G^δ_S} RD(ν_S, ε; π) + log(1/δ))/(2n)) + ε. Here
  gen(S, W^T) is the average of gen(S, W^t) over iterations t ∈ T.
- **Theorem 7 (trajectory, "data-dependent").** For an L-Lipschitz loss
  in [0, 1], with probability ≥ 1 − δ, E_{W^T∼π_S} gen(S, W^T) ≤
  √((RD(S, ε; π_S) + log(√(2n)M/δ))/(2n − 1) + 4Lε). RD(s, ε; π_s) is
  the rate-distortion function of the trajectory law for the given
  sample (eq. 34). In the proof (E-H, steps d–e) the chain rule splits
  I(W^T; S, Ŵ^T) into I(W^T; Ŵ^T | S), which becomes the data-dependent
  RD term, and I(W^T; S), which is absorbed into M. So the trajectory's
  dependence on the sample enters only through M.
- **Recovered dimension bound (App. B).** Şimşekli et al.'s Hausdorff
  dimension bound on sup_t |gen(S, W^t)| for continuous-time SGD comes
  out of Corollary 1 (Theorem 3 with algorithmic randomness U), with the
  same coupling constant M.
- **Haghifam et al.'s counterexample (App. A).** For the stochastic convex
  problem in which Xu–Raginsky's bound is Ω(1) while E gen = O(1/√n),
  Theorem 5 gives E gen = O(1/n) and Proposition 1 gives gen = O(1/n)
  with probability ≥ 1 − δ. The surrogate Ŵ is a two-point quantisation
  built from the closed-form GD iterates (Lemma 18 of [59]).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | A sample-dependent coding rate gives tail bounds that depend on the realised (S, W), not only on P_{S,W} | strong | Theorem 1, proved; Theorem 2 constructs the codes for finite alphabets |
| C2 | The disintegrated PAC-Bayes bound is the case R_{S,W} = log dP_{W|S}/dP(W) | strong | Theorem 2 with ε = 0 (finite alphabets); Theorems 3–4 in general |
| C3 | Most PAC-Bayes, MI and rate-distortion bounds are instances of Theorems 3–5 | moderate | recovers Rivasplata et al. Thm 1, Bégin et al., Xu–Raginsky and [LIT-236](../literature.d/LIT-236.md) Thm 10; the rest by Clerico et al.'s observation |
| C4 | A lossy PAC-Bayes bound stays finite for deterministic continuous-parameter algorithms | strong | Proposition 1, with a worked example |
| C5 | Average generalisation error along a trajectory is bounded by the trajectory's rate-distortion function for the given sample, plus a coupling term | moderate | Theorem 7, proved; M depends on μ and is not estimated |
| C6 | More compressible trajectories go with smaller generalisation error across learning rates on CIFAR-10 | weak | Figure 1: two networks, about seven learning rates, M and 4Lε dropped, bound on a separate axis |
| C7 | Rate-distortion bounds escape Haghifam et al.'s limitation on MI bounds, at O(1/n) | moderate | App. A and E-I, with a surrogate tailored to the known GD solution |

## Method

Def. 2 replaces the fixed hypothesis book of e^{mR} entries with one in
which only the first e^{Σ_i R_{S_i,W_i}} entries may be used to cover a
given block. Theorem 1's proof sums Chernoff bounds over book entries j,
with weight e^{−log j}, which gives a harmonic sum of about mR_max. That
is where variable size costs only a vanishing term. Theorem 2 builds
books per joint type within the KL ball and orders them so that each
type uses only its own share. The general theorems drop coding. They
condition P_{S,W} on the bad event (Lemma 1) and apply Donsker–Varadhan,
or its Rényi generalisation, to a surrogate.

The experiment (§V, App. D): FCN4 (6.3 M parameters) and CNN4 (1.07 M) on
CIFAR-10, SGD with batch 50 at seven learning rates in [5e−5, 1e−3],
trained to 100% training accuracy. Ten further epochs of normalised
weights are stored as the "trajectory". The rate-distortion function
under RMSE is estimated with NERD on random sub-blocks of each layer,
scaled to the model's size, and √(R(D)/(2n − 1)) at D = 6.5 is plotted on
a second axis beside the test-estimated generalisation error.

## Concepts

- **Variable-size compressibility (Def. 2).** Covering failure decays
  like δ^m when the usable book size is e^{Σ_i R_{S_i,W_i}}.
- **Data-dependent bound.** One computable from a single sample without
  knowing P_S (§III). Bounds that depend on P_{S,W}, such as [LIT-236](../literature.d/LIT-236.md)'s,
  are data-independent in this sense.
- **G^δ_X.** The set of laws within KL log(1/δ) of P_X (eq. 4).
- **Coupling coefficient M.** As above. It is akin to Şimşekli et al.'s
  Definition 5 and bounded by I_∞(S; W^T).
- **Rate-distortion of a process (eqs. 33–34).** The least I(S; Ŵ^T) or
  I(W^T; Ŵ^T) with average per-iteration distortion ≤ ε. Its limit per
  iteration, over log(1/ε), is the rate-distortion dimension of the
  process.

## Connections

It generalises [LIT-236](../literature.d/LIT-236.md) and recovers its Theorem 10 (§IV-A). It recovers
Xu–Raginsky ([LIT-347](../literature.d/LIT-347.md)) and, for one example, answers Haghifam et al.'s
critique of mutual-information bounds. The PAC-Bayes link extends Blum
and Langford's PAC-MDL, which made it only for Littlestone–Warmuth
compression. Chu and Raginsky (2023) unify MI and PAC-Bayes bounds by a
simpler route, and the authors say it loses constants. §VI names
compressibility of latent representations as an extension and cites the
same group's [LIT-245](../literature.d/LIT-245.md).

## Bearing on the record

- **[THEORY-028](../theory.d/THEORY-028.md) needs updating.** "Lossy and data-dependent refinements
  ([LIT-236](../literature.d/LIT-236.md), [LIT-233](../literature.d/LIT-233.md)) exist but are Deferred and unread" is now stale. On
  this paper it should say that Theorem 5 recovers [LIT-347](../literature.d/LIT-347.md)'s bound as
  the lossless, in-expectation case of a general change-of-measure
  inequality. The data-dependent versions are PAC-Bayes bounds, with the
  information term replaced by a pointwise log-density ratio against a
  prior. That removes the μ-dependence. It does not remove vacuity for
  real networks, which no bound here is computed for.
- **[NOTE-306](NOTE-306.md)** says the paper "makes such bounds data-dependent (empirical
  measure) rather than μ-dependent". True of Theorems 1, 4 and 7's rate
  term and of Proposition 1. Theorem 6, the fast-rate constant C, and
  Theorem 7's M still depend on μ.
- **[NOTE-216](NOTE-216.md)'s open questions** are answered here.
  - Is the variable rate MDL in disguise? In the PAC-Bayes case it is a
    Shannon code-length difference against a chosen prior, as in PAC-MDL.
    It is not Kolmogorov complexity and not a two-part code of the
    sample. No bound is stated in Kolmogorov terms.
  - How much empirical support survives dropping the coupling term? The
    term dropped is the one that carries the trajectory's dependence on
    the sample. What survives is a co-movement of two curves on separate
    axes. For FCN4 the plotted approximation is about 3, above any
    possible 0–1 generalisation error, so the bound is vacuous there.
- **[NOTE-241](NOTE-241.md)** groups this paper with [LIT-236](../literature.d/LIT-236.md) as lossy compressibility of
  the output relative to its effect on the loss. That is accurate.
- **[THEORY-238](../theory.d/THEORY-238.md)** ([LIT-245](../literature.d/LIT-245.md)) is the representation-level application named
  in §VI.
- The learning-rate observation in §V is descriptive, not an
  instruction. Nothing for the anthology from this reading.

## Limitations

- **Data-dependence is partial.** The conditions of Theorems 2–4 range
  over a KL ball around P_{S,W}, and Theorem 7's M depends on μ through
  G^δ_S. A bound is computable from one sample only when the chosen rate
  or prior is, as in the PAC-Bayes case.
- **The coding interpretation is proved only for finite S × W**
  (Theorem 2). The general results are variational inequalities to which
  the paper gives a compression reading.
- **The experiment does not test the bound.** It drops M and 4Lε, uses a
  surrogate loss for training and 0–1 for evaluation, estimates RD on
  subsampled weights with a neural estimator, and plots against a second
  axis. Only the ordering over learning rates is compared.
- **Theorem 7 is about the average generalisation error along the last
  part of the trajectory,** not about the final model. The authors relate
  the two only by an ergodicity remark.
- **The O(1/n) result in App. A** uses a quantiser designed from the known
  closed-form GD solution of that example, so it shows the framework can
  be tight, not that a generic surrogate would be.

## Open questions

- Can M be estimated or bounded from one sample, so that Theorem 7 is
  data-dependent in full?
- Does the rate-distortion function of a stored trajectory, estimated
  with a valid bound rather than NERD, give a non-vacuous value for a
  real network?
- §VI asks whether low communication cost and good generalisation can be
  had together, since both are now functions of compressibility. The
  paper leaves it open.
