---
status: Read
paper: 'LIT-tmpqozw7'
title: 'Deriving neural scaling laws from language statistics'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read in full from the arXiv PDF of v3 (arXiv:2602.07488v3, 3 July
    2026, 31 pp., marked "Proceedings of the 43rd International Conference
    on Machine Learning, Seoul, South Korea. PMLR 306, 2026"), text
    extracted with pdftotext and kept as paper.txt in the scratchpad
    download directory dl/reg-c2-2602.07488: abstract, §§1–6, Limitations,
    Appendices A–E and the reference list. The derivation of Appendix A
    (Eqs. 17–43) and the sampling-noise argument of Appendix B (Eqs. 44–55)
    were followed step by step, including the three cases of the excess-loss
    sum (Eq. 39). The error table of App. C.3 was read in full. Figures were
    read from captions, axis labels and text, not from plotted values. v1,
    v2, the PMLR copy and the authors' code were not read. LIT-883 with
    NOTE-687, and LIT-877 with NOTE-677, were read first, so that this note
    places the paper without repeating them.
date: '2026-10-09'
summary: >-
  Predicts the data-limited scaling exponent of language-model test loss
  as γ/(2β), from two measured corpus statistics: the decay with lag of the
  top singular value of the token–token covariance (β), which sets the
  usable context n*(P) ~ P^(1/(2β)), and the decay of next-token
  conditional entropy with context (γ). The derivation rests on assumed
  scaling forms and a fast-learning condition; on TinyStories and
  WikiText-103 transformers match the predicted exponents up to about 10^8
  tokens and horizons of a few tens of tokens.
---
<!-- inactive-ok-file: THEORY-tmpi172b QUESTION-025 THEORY-201 THEORY-195 THEORY-182 THEORY-183 THEORY-186 CLAIM-008 — Proposed or open; cited as what this reading bears on or produced -->

# NOTE-tmp24x8p: Deriving neural scaling laws from language statistics

## Contribution

[LIT-883](../literature.d/LIT-883.md) showed, on a synthetic grammar and on character-level text with
contexts up to 15, that a sample of P sequences resolves token correlations
only out to a distance set by sampling noise, and that this caps the
context a next-token learner can use. This paper turns that cap into a
prediction of the exponent of the data-limited scaling law. It adds a second
corpus statistic, the decay of the conditional entropy with context length,
and writes the loss as the entropy at the usable horizon plus the excess
loss inside it. When the second term is negligible, the exponent is γ/(2β).
It tests this with no synthetic model, on subword-tokenised TinyStories and
WikiText-103, and on GPT-2- and LLaMA-style transformers up to 600M
parameters.

## Key insight

With more data a language model does not mainly predict better from the
context it already uses. It uses more context. How much more is set by
when the correlation between tokens at that lag rises above sampling
noise: P*_n ~ n^(2β). How much each extra token of context is worth is set
by how fast conditional entropy falls with context: n^(−γ). Put together,
the loss falls as (P^(1/(2β)))^(−γ) = P^(−γ/(2β)), and both exponents are
properties of the text, not of the model.

## Assumptions

- **Stationarity** of the token process, so that the differential loss is
  ∆_n = L_n − L_{n−1} (Eq. 23); sequences are random chunks of a
  concatenated corpus.
- **Hypothesis 1 (Eq. 21):** H_n − H_∞ ≍ n^(−γ). Equivalent, by summing, to
  Hilberg's hypothesis for block entropy.
- **Hypothesis 2 (Eq. 25):** ∆_n(P) = (H_n − H_{n−1}) f_n(P/P*_n), with f_n → 0
  below the threshold and 1 − f_n ~ x^(−δ_n) above it. The authors call this
  "really an assumption about" the threshold P*_n. It encodes that lag n
  contributes nothing until P*_n, which is not derived.
- **The threshold (Eqs. 28–30):** P*_n ≍ ‖C(n)‖_op^(−2), i.e. a lag becomes
  usable once the strongest pairwise correlation at that lag is detectable.
  That this minimal requirement is also sufficient is assumed, and it
  ignores dependences not visible in pairwise statistics.
- **Power-law correlations (Eq. 29):** ‖C(n)‖_op ≍ n^(−β).
- **Fast learning within the horizon:** δ = min_n δ_n > γ/(2β), so the excess
  losses do not dominate; and T ≫ n*(P), so the context limit does not bind.
- **Fixed vocabulary** as P grows: the noise constants depend on V (App. B).
- **Models are capacity-sufficient** at each P: for each P, hyperparameters
  are tuned (grid over learning rate, weight decay, epochs, batch size) and
  larger models are checked not to lower validation loss (App. E). The law
  tested is the data-limited one, not a compute-optimal one.

## Key results

- **Eq. 34.** L_AR(P) ≍ H_{n*(P)} + Σ_{n ≤ n*(P)} E_n(P): a boundary term from
  the finite horizon, plus the excess losses within it. *Holds:* given
  Hypothesis 2 and dropping O(1) weights (T − n + 1)/T.
- **Eq. 39–40.** With E_n ≍ n^(−γ−1)(n^(2β)/P)^δ, the excess sum is
  O(P^(−γ/(2β))) when δ > γ/(2β), P^(−δ) log P at equality, and P^(−δ) when
  δ < γ/(2β). So L_AR − H_∞ ≍ P^(−min(δ, γ/(2β))). I checked the sum; the case
  labels as printed are consistent with the stated conclusion.
- **Eq. 43.** L_n − H_∞ ≍ n^(−γ) ℓ(P/n^(2β)), with ℓ(x) ~ const + x^(−δ) for
  x ≫ 1, assuming δ_n and f_n do not vary with n.
- **App. B, Eqs. 50–55.** The empirical covariance differs from the true one
  by a noise matrix of operator norm ≲ (σ_n² log V / P)^(1/2) (matrix
  Bernstein); by Weyl's inequality each singular value moves by at most
  that, so a mode is resolvable only above P^(−1/2). Compared to the
  spiked-matrix (BBP) detectability threshold.
- **Eqs. 11–14.** TinyStories γ = 0.325 ± 0.003 (fit over n = 1 to 16,
  GPT-2 APE, T = 128) and β = 0.88 ± 0.06 (15 lags from 1 to 200).
  WikiText γ = 0.265 ± 0.016 (first three points; error from the first four)
  and β = 0.94 ± 0.16 (6 lags from 1 to 32). The WikiText correlation decay
  is a broken power law with a local peak near n ≈ 10, which is set aside.
- **Fig. 2, 5.** The limiting L_n against n agrees across GPT-2 APE, RoPE,
  LLaMA, Mamba and an infini-gram model (TinyStories), and APE and RoPE
  (WikiText). The fitted γ is therefore taken as a property of the data.
- **Eqs. 15–16, App. C.3.** Predicted α_D: TinyStories 0.185 ± 0.013
  ([0.172, 0.198]); WikiText 0.141 ± 0.025 ([0.116, 0.166]). Fitted to the
  first m points of the lower envelope over context lengths, the 95%
  bootstrap intervals in the table overlap the prediction for every m
  from 5 to 12 on TinyStories and 5 to 8 on WikiText. The TinyStories
  intervals drift downward as m grows (m = 12: [0.149, 0.175]), and the
  text's "up to 10 of the first 12 points" does not match its own table,
  which overlaps for all eight fits.
- **Figs. 1, 4, 8–17.** The n-gram losses collapse under P → P/n^(2β),
  L_n → n^γ L_n for TinyStories (T = 64 to 512, APE, RoPE, LLaMA) and
  WikiText (T = 128, 512, APE and RoPE). The collapse degrades when β is
  moved one standard error or γ moved past [0.31, 0.34] (TinyStories) or
  [0.23, 0.30] (WikiText). LLaMA on TinyStories collapses best at
  β ≈ 0.6–0.7, outside the measured interval, while its scaling exponent
  stays compatible with the prediction; left unexplained.
- **Fig. 6.** GPT-2, T = 128, TinyStories, n ≤ 12: fitting
  L_n = A P^(−δ_n) + H_n to P ≥ 10 P*_n gives δ_n > γ/(2β) for every n, the
  fast-learning condition.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Sampling noise in the lag-n covariance from P tokens is O(P^(−1/2)) in operator norm, so a correlation mode is resolvable only above that | strong | App. B, matrix Bernstein and Weyl, for fixed V |
| C2 | If excess losses within the horizon decay faster than P^(−γ/(2β)), the data-limited loss falls as P^(−γ/(2β)) | moderate | App. A; follows from Hypotheses 1–2 and the threshold, which are assumed |
| C3 | On TinyStories and WikiText-103, β and γ measured from the corpus predict the empirical data-limited exponent with no fitted parameter | moderate | App. C.3: overlapping intervals on two corpora; γ estimated from trained models; P ≤ ~10^8, horizons of tens of tokens |
| C4 | The n-gram learning curves collapse under P/n^(2β) and n^γ L_n | moderate | Figs. 1, 4, 8–17; visual; LLaMA prefers a smaller β |
| C5 | γ is a property of the dataset, not of the architecture | moderate | Figs. 2, 5: five model classes on TinyStories, two on WikiText; all are upper bounds that converge only at small n |
| C6 | Transformers on this data are in the fast-learning regime | weak | Fig. 6: one model, one corpus, n ≤ 12, asymptotes chosen by a grid search on R² |
| C7 | Kernel methods and shallow networks fall outside this "universality class", with worse exponents | weak | §6, by analogy with the Random Hierarchy Model results ([LIT-877](../literature.d/LIT-877.md)); not tested here |

## Concepts

- **Prediction time horizon n*(P)** — the largest lag at which P tokens can
  resolve the top singular value of the lag-n covariance; the paper's name
  for [LIT-883](../literature.d/LIT-883.md)'s effective context window t*(P).
- **Time-dependent data threshold P*_n** — the inverse: the P at which lag n
  becomes usable, ~ n^(2β).
- **Correlation strength ‖C(n)‖_op** — the top singular value of the V × V
  lagged covariance of one-hot tokens. [LIT-883](../literature.d/LIT-883.md) used a root-mean-square over
  entries; the scaling in n is said to be the same for the Frobenius norm,
  and Fig. 3 shows the two tracking each other.
- **n-gram loss L_n** — the model's cross-entropy for the token after n
  tokens of context; its floor is the conditional entropy H_n.
- **Excess loss E_n(P)** — how far the differential loss ∆_n still is above
  its asymptote H_n − H_{n−1}: suboptimal use of the n-th past token.
- **Fast learning within the horizon** — δ > γ/(2β): the model learns to use
  the tokens it can see faster than the horizon grows.

## Connections

The direct predecessor is Cagnetta and Wyart ([LIT-883](../literature.d/LIT-883.md), [NOTE-687](NOTE-687.md)), from
which the horizon argument is taken; behind it is the Random Hierarchy
Model ([LIT-877](../literature.d/LIT-877.md)). The entropy hypothesis is Hilberg's (1990), in Crutchfield
and Feldman's and Takahira, Tanaka-Ishii and Dębowski's forms; the
power-law correlations are attributed to hidden hierarchical structure
after Lin and Tegmark and [LIT-883](../literature.d/LIT-883.md). It sets itself against kernel-limit
accounts of learning-curve exponents (Spigler, Geiger and Wyart; Bordelon,
Canatar and Pehlevan; Bahri et al.) on the ground that LLMs learn features,
and against "quanta" accounts in which power laws come from Zipf-
distributed skills (Michaud et al.), or appear without power-law structure
in the data (Barkeshli et al.; Liu et al.). Dębowski's toy model, from Zipf
through Heaps to Hilberg, is the nearest rival that also starts from
language statistics. Of these, only [LIT-877](../literature.d/LIT-877.md) and [LIT-883](../literature.d/LIT-883.md) are held here.

**The Random Hierarchy Model as a check (this record's inference, not the
paper's).** In [LIT-883](../literature.d/LIT-883.md), the loss with context s^ℓ − 1 is about
log(1/(1 − f)) + v f^ℓ with f = m/v^(s−1), and the correlation at the
matching distance is ∝ m^(−ℓ). With n = s^ℓ these give γ = ln(1/f)/ln s and
β = ln m/ln s, so γ/(2β) = ln(1/f)/(2 ln m): exactly the exponent [LIT-883](../literature.d/LIT-883.md)
composed from its loss steps in its Eq. 13, once that equation's sign slip
([NOTE-687](NOTE-687.md)) is corrected. The new formula is thus the general form of the
old envelope, and [LIT-883](../literature.d/LIT-883.md)'s steps are what its ansätze smooth over.

## Bearing on the record

- **[THEORY-201](../theory.d/THEORY-201.md) ([LIT-883](../literature.d/LIT-883.md)).** This paper is the further test [THEORY-201](../theory.d/THEORY-201.md)'s
  real-text clause called for, on its effective-context part: at subword
  level, at contexts up to 512, on two corpora, with β from the operator
  norm, the n-gram curves collapse under P/n^(2β). It strengthens that
  clause. It does not touch the hierarchical part (hidden symbols learned
  level by level), which it neither models nor probes, and it does not meet
  [THEORY-201](../theory.d/THEORY-201.md)'s `promote_when`, which asks for β to be moved by intervention
  with the grammar fixed. The LLaMA collapse at a β outside the measured
  range is a small strain on the claim that the threshold is set by the
  correlation alone.
- **[THEORY-195](../theory.d/THEORY-195.md) ([LIT-877](../literature.d/LIT-877.md)).** No new evidence. The paper cites the
  Random Hierarchy Model results as reasons to expect shallow learners to
  scale worse, which is [THEORY-195](../theory.d/THEORY-195.md)'s contrast, but tests no shallow learner.
- **[QUESTION-025](../questions.d/QUESTION-025.md).** No answer, and no hierarchy. One observation bears on
  the spectral accounts the question starts from: the lagged token–token
  covariance matrices of real BPE text have "a small number (≲ 10) of large
  singular values, followed by a power-law-decaying bulk" (App. A). That is
  a low-rank-plus-bulk spectrum for positional co-occurrence at each lag. It
  fits [THEORY-182](../theory.d/THEORY-182.md)'s picture of an embedding that learns a few top
  eigenvectors of a co-occurrence deviation, and it is what a measurement
  for [QUESTION-025](../questions.d/QUESTION-025.md) would look into. The paper reports it in one sentence,
  with no figure, and studies only the top singular value's size, never its
  vectors. [THEORY-183](../theory.d/THEORY-183.md)'s premise, that co-occurrence depends on separation
  alone, is the premise of every measurement here, at subword level.
- **[THEORY-186](../theory.d/THEORY-186.md).** Not a stagewise account in its sense: there are no
  discrete stages, only a horizon growing continuously with P.
- **[CLAIM-008](../claims.d/CLAIM-008.md), and the manuscript's argument.** No bearing found. The paper
  says nothing of latents, meaning or translation.
- **New account.** [THEORY-tmpi172b](../theory.d/THEORY-tmpi172b.md), Proposed: the data-limited exponent as
  γ/(2β) under the fast-learning condition, with what it does not say.
- **Practice.** The paper gives no instruction, but its subject, what sets
  the exponent of data-scaling laws, is named in the anthology's
  `training-optimization` blurb, and its statistics are what
  `signal-structure` holds; hence the flag on the LIT. Its closing remark,
  that the exponent marks a limit set by the data that architectures in
  the same class share, is the kind of claim the anthology would test
  against practice.

## Limitations

- **Derived from ansätze.** Hypothesis 2 builds the threshold into the form
  of the per-lag learning curve; that a lag is unusable until its pairwise
  correlation is detectable, and fully usable soon after, is assumed.
  Higher-order dependences that pairwise covariance does not show are
  outside the argument.
- **γ is not measured from text alone.** It is fitted to the n-gram losses
  of the largest trained models, upper bounds on H_n that converge only at
  small n (at WikiText, three points). The claim of "no free parameters"
  holds for the exponent fit, but γ comes from the same kind of model whose
  scaling it predicts, at the largest P. The architecture agreement in
  Figs. 2 and 5 is the paper's answer.
- **Short ranges.** P up to about 10^8 tokens; usable horizons of a few tens
  of tokens; power laws fitted over one to two decades (WikiText β over
  lags 1 to 32, around a peak it sets aside). The authors flag that the
  regime may not hold at trillion-token scale and 10^5-token contexts.
- **Two corpora, one tokeniser** (BPE, 8192), one of them (TinyStories)
  generated by GPT-3.5 and GPT-4, so its statistics are those of a model's
  output, not of natural text.
- **The fast-learning check is narrow.** One model and corpus, n ≤ 12,
  asymptotes picked by maximising R².
- **The universality class is a conjecture.** Which architectures share the
  exponent is posed, not shown; the LLaMA collapse at a smaller β is left
  open.

## Open questions

- An intervention that changes β (say, shuffling text beyond some range
  while keeping short-range statistics) or γ independently, with the
  exponent tracking γ/(2β).
- An estimate of γ from the corpus that does not go through a trained
  neural model, and whether it agrees.
- Whether the formula holds at the scale of current models, where the
  usable horizon reaches thousands of tokens and the WikiText correlation
  decay changes slope.
- What the low-rank part of the lagged covariance is: which token
  directions carry the top singular values, how they change with lag, and
  whether they line up with the embedding directions of [THEORY-182](../theory.d/THEORY-182.md) or the
  Fourier modes of [THEORY-183](../theory.d/THEORY-183.md).
- On hierarchical data with Zipfian rules, whether γ and β come out as
  this record's RHM inference says and the steps smooth into the
  predicted power law.
