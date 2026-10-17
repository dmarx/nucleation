---
status: Read
paper: 'LIT-tmpz9o5z'
title: 'Schreiber — Measuring information transfer'
version: 1
history:
- version: 1
  date: '2026-10-17'
  note: >-
    Read in full from arXiv nlin/0001042v1 (19 Jan 2000), 4 pp.: text,
    Eqs. 1–5, Figs. 1–4 from captions and prose, references [1]–[8].
    Nothing skipped. PDF from arxiv.org/pdf/nlin/0001042, extracted with
    pdftotext. Figure curves were read only through captions and text. I
    rederived the tent-map lowest-order result and the cancellations the
    paper claims for it. I did not compare the PRL version, and did not
    read Kaiser and Schreiber (2002, LIT-tmpfgfsh, Unavailable), the
    continuous-process sequel.
date: '2026-10-17'
summary: >-
  Defines transfer entropy T_{J→I} as the Kullback entropy between I's
  transition probabilities with and without J's past, at history lengths
  k for I and l for J (Eq. 4), which is the conditional mutual
  information I(i_{n+1}; j_n^{(l)} | i_n^{(k)}). It is directional and
  ignores static correlation. A kernel estimator is proposed. Tent-map
  and Ulam-map lattices show it detecting the coupling direction where
  time-delayed mutual information fails; a heart–breath pair shows an
  asymmetry that the author says a common trigger could also explain.
---

# NOTE-tmplm3la: Schreiber — Measuring information transfer

## Contribution

Before this Letter, directional coupling between time series was read off
time-delayed mutual information, which counts shared history and common
input as exchange. After it, there is an information-theoretic measure
built on transition probabilities: zero when the source's past does not
change the target's transitions, positive otherwise, and not symmetric.
It is the quantity every later document in the record calls transfer
entropy.

## Key insight

Generalize the entropy rate, not the entropy. A static measure (mutual
information) cannot see dynamics; a measure of how much J's past changes
I's next-step law can. Written as a Kullback entropy, that is "how many
extra bits I pay for coding I's next state as if J did not matter".

## Assumptions

- **Stationary Markov approximation.** I is approximated by a stationary
  Markov process of order k (p. 2), so that p(i_{n+1} | i_n^{(k)})
  stands in for the full past. For non-Markov systems the limit k → ∞
  is needed, which the paper mentions for the entropy rate only.
- **History lengths k and l are free.** The paper calls l = k or l = 1
  "most natural" and prefers l = 1 for computation (p. 2). Its numerical
  Ulam example uses k = l = 1; the tent-map calculation uses k = l = 1.
- **Source and target are aligned at the same time n.** j_n^{(l)} =
  (j_n, …, j_{n−l+1}) predicts i_{n+1}: a one-step delay is built in.
  There is no separate delay parameter.
- **Coarse-graining.** For continuous systems the states are partition
  cells at resolution ε. The ε → 0 limit is asserted finite and
  partition-independent except for deterministic coupling, where T
  diverges (p. 2). Not proved.
- **Common inputs are excluded only if known.** "The influence of a known
  common driving force Z may be excluded by conditioning … to z_n as well"
  (p. 2). Unconditioned common drivers are not excluded.

## Key results

- **Eq. 3, entropy rate.** h_I = −Σ p(i_{n+1}, i_n^{(k)}) log p(i_{n+1} |
  i_n^{(k)}) = H_{I^{(k+1)}} − H_{I^{(k)}}.
- **Conditional entropy is not directional.** H_{I|J} − H_{J|I} = H_I −
  H_J, so its asymmetry reflects the individual entropies, not flow
  (p. 2).
- **Eq. 4, transfer entropy.** As in the summary. It is non-symmetric
  "since it measures the degree of dependence of I on J and not vice
  versa".
- **Estimator (Eq. after 4).** p̂_r(x_{n+1}, x_n, y_n) = (1/N) Σ_{n′}
  Θ(r − ‖(x_{n+1} − x_{n′+1}, x_n − x_{n′}, y_n − y_{n′})‖), a step kernel
  with maximum norm, dynamically correlated pairs excluded. The order-2
  correlation-integral generalization is rejected because it would give
  up positivity.
- **Tent-map lattice (Eq. 5, Fig. 1).** x^m_{n+1} = f(εx^{m−1}_n +
  (1 − ε)x^m_n), binary partition at 0.5. At small ε, p(0|0,0), p(0|1,1),
  p(1|0,1), p(1|1,0) rise by a factor 1 + αε and the others fall. Then
  T_{I^{m−1}→I^m} = α²ε²/ln 2 + O(ε⁴), T in the other direction is zero,
  and M(τ) is zero. A fit to 10 runs of 10⁵ iterates on 100 sites gives
  α = 0.77. *Checked:* the marginal transition p(i_{n+1} | i_n) stays ½,
  and p(i^m_{n+1}, i^{m−1}_n) stays ¼, so delayed MI is zero to this
  order, as claimed. My lowest-order evaluation of Eq. 4 gives α²ε²/(2 ln
  2) bits, half the stated value: with p(i′|i, j) = ½(1 ± αε) and p(i, j)
  = ¼, the inner sum is ½[(1+x)ln(1+x) + (1−x)ln(1−x)] ≈ x²/2 nats, x =
  αε. Since α is fitted, the factor changes the fitted α by √2 and
  nothing qualitative.
- **Ulam-map lattice (Fig. 2).** f(x) = 2 − x², 100 sites, 10⁴ iterates,
  correlation sums at r = 0.2, k = l = 1, neighbours within 100 steps
  excluded. Both T and delayed MI are larger in the coupling direction.
  In the period-two window near ε = 0.18 delayed MI is 1 bit and T is
  zero; at the fixed point near ε = 0.82 both are zero. T against the
  coupling stays "consistent with zero for all couplings".
- **Heart and breath rates (Figs. 3–4).** Santa Fe data set B, 2 Hz.
  Delayed MI is "almost symmetric"; T(heart → breath) exceeds T(breath →
  heart) over a range of r, falling to zero at small r for finite-sample
  reasons. "Certainly, both signals could instead be responding to a
  common external trigger."

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | T_{J→I} (Eq. 4) is zero iff I's transitions at histories k, l do not depend on J's past, and is otherwise positive | strong | definition as a Kullback entropy; standard |
| C2 | Time-delayed MI fails to separate exchanged information from common history and input | moderate | argued p. 1–2; Ulam period-two window (Fig. 2) |
| C3 | T is designed to ignore static correlations due to common history or common input | moderate for history, weak for input | conclusion; common input only if known and conditioned on (p. 2) |
| C4 | For coarse-grained continuous systems the ε → 0 limit of T is finite and partition-independent unless coupling is deterministic | assertion | p. 2, by analogy with mutual information; no proof |
| C5 | In the tent-map lattice T = α²ε²/ln 2 + O(ε⁴) and delayed MI is zero | moderate | lowest-order argument p. 3, α fitted; my evaluation gives half the coefficient |
| C6 | T reflects the unidirectional coupling through the Ulam lattice's bifurcations and outperforms delayed MI | moderate | Fig. 2, one lattice, k = l = 1, one radius |
| C7 | Information flows more from heart rate to breath rate than the reverse in the apnoea data | weak | Fig. 4; the author concedes a common trigger |
| C8 | Conditioning on common history resolves the superluminal-velocity paradox of delayed-MI transport speeds | weak | "preliminary results" (p. 4), not shown |

## Method

1. Embed: form i_n^{(k)} and j_n^{(l)}.
2. Estimate p(i_{n+1}, i_n^{(k)}, j_n^{(l)}) and its marginals, by a box
   partition or by the step-kernel correlation sum at radius r.
3. Evaluate Eq. 4 with transition probabilities as ratios of joints.
4. Report T as a function of r or ε, or at a fixed resolution.

## Concepts

- **Transfer entropy T_{J→I}** — Eq. 4. Equivalently, the conditional
  mutual information I(i_{n+1}; j_n^{(l)} | i_n^{(k)}); the paper does
  not use that form.
- **Generalized Markov property** — p(i_{n+1} | i_n^{(k)}) = p(i_{n+1} |
  i_n^{(k)}, j_n^{(l)}): "in the absence of information flow from J to
  I, the state of J has no influence on the transition probabilities on
  system I".
- **Transinformation** — the Kullback entropy of independence of two
  processes' joint rates; symmetric, so rejected.
- **Information transfer / exchange / flow** — used interchangeably for
  T. The paper offers no definition of flow beyond Eq. 4.

## Connections

- **Builds on** Shannon's entropy, Kullback's relative entropy and the
  correlation-integral estimators of Grassberger, Schreiber and
  Schaffrath; compares itself with time-delayed MI (Kaneko, Vastano and
  Swinney) and with synchronization measures [2].
- **Barnett, Barrett and Seth (LIT-tmpmi22s, NOTE-tmp2veo7).** Their Eq.
  10 is Eq. 4 with Z conditioned on, multivariate and with lags p, q, r.
  Its Gaussian form equals half Geweke's Granger causality.
- **Barnett and Bossomaier (LIT-048, NOTE-053).** Their T is Eq. 4 with
  l = k. Their plug-in estimator for finite states is Eq. 4 with
  empirical frequencies.
- **Das, Manikandan and Banerjee (LIT-947, NOTE-788).** TE_{x→y}(τ) =
  I(y_{t+τ}; x_t | y_t) is Eq. 4 with k = l = 1 at τ = 1. For τ > 1 it
  conditions on y_t, not on y_{t+τ−1}, so it is a delayed variant the
  Letter does not define. My reading.
- **Kaiser and Schreiber (LIT-tmpfgfsh)** carries the definition to
  continuous processes; not read.
- **James, Barnett and Crutchfield (LIT-tmpa6og3)** argue that the
  quantity Eq. 4 measures is not a flow. The Letter supplies the
  vocabulary they object to: "transfer", "exchange", "transport".

## Bearing on the record

- Filed as THEORY-tmp1jjkw.
- The record's documents disagree on k and l only in the sense that
  Schreiber leaves them open. NOTE-053 (l = k) and NOTE-788 (k = l = 1)
  are both within Eq. 4. NOTE-788's τ > 1 form is not, and NOTE-788
  credits it to Schreiber; that is worth an annotation there.
- TERM-tmpj9z04 should state the definition with k and l explicit, and
  note that the Letter's guarantee of excluding common input holds only
  for an input that is conditioned on.
- For CLAIM-tmpu9ivq: the Letter calls T "information transfer" without
  defining flow; C1 is all it shows. Positive T means J's past changes
  I's transition law given I's own past, nothing more localized than
  that.
- **For the Anthology of the SOTA:** no instruction for ML practice.

## Limitations

- The examples are designed to have a known direction; the one empirical
  case has an acknowledged confounder.
- k and l are not chosen by any criterion; results at k = l = 1 may not
  survive longer histories, and nothing tests that.
- No sampling distribution, bias analysis or significance test is given.
  Finite-sample bias appears only as the small-r deflection in Fig. 4.
  Barnett and Bossomaier (NOTE-053) later supply a χ² null under a
  parametric model.
- The ε → 0 claim is by analogy; the kernel estimator works at a fixed r,
  so the results are resolution-dependent by construction.
- The tent-map coefficient appears to be off by a factor of 2 (my
  calculation; see Key results).

## Open questions

- The velocity-of-information-transport problem, left "to be concluded at
  a later time" (p. 4).
- How T behaves as k grows for non-Markov targets, which the Letter
  mentions only for the entropy rate.
