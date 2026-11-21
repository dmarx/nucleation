# Reader notes: LIT-tmpnbl2d, Lau, Furman, Wang, Murfet & Wei, "The Local Learning Coefficient: A Singularity-Aware Complexity Measure", arXiv 2308.12108

Reader: subagent, 2026-11-21. Status of reading: **read in full** (main text and
appendices A to P; reference list skimmed only for the entries cited below).

## Provenance

- **Read**: https://arxiv.org/pdf/2308.12108 (arXiv, the author-deposited
  preprint; lawful, step 5 first route). Fetched 2026-11-21, HTTP 200,
  application/pdf, 2,080,465 bytes. Version **v2, 30 Sep 2024** (stamp on p. 1;
  arXiv API `<updated>2024-09-30`). arXiv comment: "This version contains new
  empirical results and merged content from a related paper (arXiv:2402.03698)".
  Text extracted with pdftotext; pages 8 and 28 rendered to images to read
  Figures 3 and J.2. 37 pages.
- Metadata: arXiv API (export.arxiv.org), no email address sent. The API record
  carries no journal_ref; the PDF footer says "Preprint. Under review." The
  LIT's "AISTATS 2025 (PMLR 258)" is **not confirmed by this copy** (not
  checked elsewhere).
- Skipped: the reference list (pp. 10-13) beyond the entries quoted; the
  in-figure numbers of Figs. 1, K.1, K.2, L.1, M.1, N.1, O.1 (read from captions
  and text only).
- Other copies located: none sought beyond arXiv, since arXiv served the full
  text. No obstacle met.
- Nothing else read; no neighbour needed.

## Summary

The paper defines the local learning coefficient (LLC) λ(w*) of a local minimum
w* of the population loss as the exponent in the volume of its ε-sublevel set,
V(ε) = c ε^λ (−log ε)^(m−1) (Def. 1), adapts Watanabe's free-energy expansion
to a ball around w* (App. B, eq. 21), and proposes an estimator: a localized
WBIC, the expected training loss under a posterior tempered at β* = 1/log n and
tied to w* by a Gaussian of precision γ, sampled by minibatch SGLD (eqs. 10-13,
Alg. 1). It validates the estimator against Aoyagi's exact learning coefficients
for deep linear networks from ~10² to 10⁸ parameters (§5.1, App. J), then uses
it for relative comparisons where no true value is known: ResNet18/CIFAR10
under learning rate, batch size, momentum and L2 (§5.2, App. K), a 3.3M-param
attention-only transformer (App. L), SGD vs entropy-SGD on MNIST (App. N), and
invariance to ReLU rescaling with preconditioned SGLD (App. O).

## Contribution

1. A local, volume-scaling definition of the learning coefficient, with
   multiplicity, and a proof sketch that it governs the local free energy.
2. A scalable estimator (minibatch SGLD, localized, tempered at 1/log n), with
   best-practice tuning (App. H: MALA acceptance as a diagnostic, burn-in).
3. Calibration in DLNs up to 100M parameters; relative comparisons elsewhere.

## Key results (section/page, verbatim)

- **Definition** (§3.1, Def. 1, p. 4): "There exists a unique rational number
  λ(w∗), a positive integer m(w∗) and some constant c > 0 such that
  asymptotically as ϵ → 0, V(ϵ) = cϵ^λ(w∗)(− log ϵ)^m(w∗)−1 + o(...)". "in
  contrast to the regular case, the scaling exponent λ(w∗) depends on the
  underlying data distribution" (p. 5).
- **Local free energy** (App. B, eq. 21, p. 16): "Fn(B(w∗)) = nLn(w∗) +
  λ(w∗) log n − (m(w∗) − 1) log log n + OP(1)", assuming "λ(w∗) ≤ λ(P) if
  P ∈ B(w∗) and L(P) = L(w∗). That is, w∗ is at least as degenerate as any
  nearby minimiser", and relative finite variance.
- **Localization** (§4.2, p. 6): the ball is replaced by "a localizing
  Gaussian prior ... φγ(w) ∝ exp{−γ/2 ||w||²}"; "Large values of γ force the
  posterior distribution in (10) to stay close to w∗."
- **Estimator** (§4.3, Def. 2, p. 6): "λ̂(w∗) := nβ∗[E_{w|w∗,β∗,γ} Ln(w) −
  Ln(w∗)]" with "the inverse temperature ... deliberately set to β∗ = 1/log n";
  "Note that λ̂(w∗) depends on γ but we have suppressed this in the notation."
- **Consistency is conjectured, not proved** (App. D, p. 17): the localized
  WBIC matches Fn(w∗, γ) to two terms with a coefficient λ̃(w∗), "However, it is
  important to understand that we cannot immediately conclude that it is a good
  estimator of Fn(Bγ(w∗)). We conjecture that λ̃(w∗) is equal to the LLC λ(w∗)
  given certain conditions on γ. So far, all our empirical findings suggest
  this. Detailed proof ... will be left as future theoretical work."
- **DLN validation** (§5.1, Fig. 3, p. 8): "Our LLC estimator is able to
  accurately estimate the learning coefficient in DLNs up to 100M parameters",
  also at an SGD-found minimum. Fig. J.2 (p. 28), relative error
  "(λ − λ̂(w∗))/λ": read from the image, most points lie between 0 and +0.75,
  i.e. **underestimates**, with clusters near +0.5 to +0.8 around 10⁴ and
  10⁶-10⁷ parameters; a few negative down to about −0.7. The log-log Fig. 3
  compresses this. Setup (App. J.1, Table 1): realizable, outputs noiseless
  ("effectively means we are setting a very small noise variance σ²"), γ = 1.0,
  n = 10⁵ or 10⁶, 90% burn-in; at 10M and 100M parameters d exceeds n.
- **Tuning matters** (App. H.1, H.2, p. 21-22): "If the step size is too low,
  the sampler may not equilibriate, leading to underestimation"; "a slow upwards
  slope can still be indicative of significant underestimation." Fig. J.3:
  "Those with low acceptance probability may indicate poor λ̂(w∗) estimation
  quality."
- **γ trade-off** (App. H.3, p. 22): "An overly concentrated localizing prior
  (γ too large) can overwhelm the gradient signal coming from the
  log-likelihood ... destroying SGLD's sensitivity to the local geometry";
  recommends "keeping γ small (1.0 to 10.0)". Used γ = 1 (DLN, ResNet, MALA
  test), γ = 100 (MNIST App. N, transformer App. L).
- **Uncalibrated elsewhere** (§5.2, p. 9): "the LLC estimates for ResNet18
  cannot be calibrated as we do not know the true LLC values ... we find value
  in the LLC estimates by comparing their relative values between models with
  shared context." Stronger implicit/explicit regularization goes with lower
  λ̂ and higher test accuracy (Fig. 1, K.1, K.2), 5 seeds each, SGLD settings
  fixed per set.
- **Heat capacity** (App. E, p. 18): "the learning coefficient may be viewed as
  a heat capacity LaMont and Wiggins (2019), and learning coefficient estimation
  corresponds to measuring the heat capacity by molecular dynamics sampling."
- **Finite n** (App. E, p. 19): the learning capacity of Chen, Chang &
  Chaudhari (2023a) "can be viewed as a finite-n version of the learning
  coefficient; the latter only appears in the n → ∞ limit"; it "saturates at
  very small and large n with a sharp transition in between."
- **Laplace vs singular** (App. E, p. 18): the Laplace form (d/2) log n +
  ½ log det H is "ill-defined for neural networks"; "For a very benign type of
  degeneracy, (23) is indeed valid."
- **Model, not task, complexity** (App. F, p. 19): f(x,w) = w⁸f₁ + (1−w⁸)f₂
  gives f₁ λ = ½ and f₂ λ = 1/16; "the LLC is a measure of model complexity,
  not model-independent complexity."
- Transformer (App. L): β set as "1/log(100)", not 1/log n, γ = 100, on a
  validation set; estimates "a small fraction of the 3.3m total parameters".

## Assumptions

Analytic model, compact W, relatively finite variance (App. A.1; automatic when
realizable, "unclear how reasonable" on real data); w* a local minimum of the
population loss and at least as degenerate as nearby minimisers (App. B);
plug-in of the SGD-found ŵ*ₙ (data used twice, §4.3); SGLD at equilibrium.

## Concepts

Local learning coefficient λ(w*), local multiplicity m(w*); volume scaling;
local free energy Fn(Bγ(w*)); localizing prior φγ; localized WBIC; β* = 1/log n;
SGLD-based estimator; MALA acceptance diagnostic; reparameterization
invariance; model vs model-independent complexity.

## What the paper does NOT contain (checked)

- **No variation of the inverse temperature.** β is fixed at 1/log n (or
  1/log 100 in App. L). The paper never estimates at several β or studies
  λ̂ as a function of β.
- **No study of γ-dependence**: γ is chosen per experiment set (1 or 100);
  App. D leaves the γ conditions open; App. H.3 gives qualitative failure modes.
- **No treatment of near-degenerate (small but nonzero curvature) directions**
  or of finite-n bias beyond the remarks above; nothing on sloppy models.
- Nothing on training dynamics or stages, except the Outlook pointing to Chen
  et al. (2023b) and Hoogland et al. (2024).

## Reader's derivation (not the paper's; checked by hand)

With Z̃(β) = ∫ exp{−nβ(Lₙ(w) − Lₙ(w*))} φγ(w − w*) dw, d log Z̃/dβ =
−n(E_β[Lₙ] − Lₙ(w*)), so λ̂ = β*·(−d log Z̃/dβ) = **−d log Z̃(t)/d log t at
t = nβ* = n/log n** (Z̃ depends on n and β only through t, data held fixed).
So the estimator is the free-energy slope in log effective sample size, at
effective size n/log n, with the localizer playing the prior. For a
quadratic direction ½e x² it contributes ½ · te/(te + γ): about 0 when
e ≪ γ log n / n, about ½ when e ≫ γ log n / n. Hence a direction too sloppy for
t = n/log n against a localizer of precision γ counts like a flat one, and
**both β and γ move the cut-off**.

## Verdict on how the exchange and the record characterize the work

- Exchange (A37, per the LIT): the LLC "as a measure of degeneracy". Fair:
  "lower LLC means a less complex, and thus more degenerate, neural network"
  (p. 3).
- LIT summary: "estimated by SGLD, as a measure of a trained network's effective
  complexity". Correct. Venue "AISTATS 2025" not confirmed by the arXiv copy.
- CLAIM-tmpcg4uu: "what a local learning-coefficient estimate at an inverse
  temperature of order n measures". **Inaccurate in wording**: the paper's
  inverse temperature is β* = 1/log n; the effective sample size nβ* is
  n/log n. On the reader's derivation the estimate is the slope at t = n/log n
  with the localizer as prior, which supports the substance of the claim's
  identification, but the paper itself only says "heat capacity" (App. E).
- LEAD-tmpfrw11: "Estimate the learning coefficient (Lau et al.) at two or more
  inverse temperatures". The proposal is the record's, not the paper's; the
  paper offers no multi-β protocol and no evidence on β-dependence. Should not
  be read as attributed to Lau et al.

## Bearing on named codes

- **CLAIM-tmpcg4uu** (sloppy directions count like flat ones at finite n):
  **leaves open, with qualified support.** The paper neither states nor tests
  the claim. Its App. E heat-capacity remark and the estimator's form (reader's
  derivation) fit the claim's reading of λ̂ as a finite-scale slope; Fig. J.2's
  systematic underestimates in DLNs (relative error mostly 0 to +0.75) are
  consistent with unresolved directions but the paper attributes
  underestimation to sampler non-equilibrium (H.1-H.2), so it does not
  discriminate. Adds that **γ is a second cut-off** besides β, which the claim
  and its "What it does not say" omit; and its wording of the inverse
  temperature should be corrected (above).
- **LEAD-tmpfrw11** (estimate at several inverse temperatures): **leaves open /
  background.** The estimator admits β as a parameter (eq. 10) but the paper
  fixes it; consistency (App. D) is only argued at β* = 1/log n. The lead
  should also vary γ, and must hold SGLD settings fixed across compared
  checkpoints (App. K practice) and check equilibration (App. H), since
  underestimation from poor mixing mimics a lower coefficient.
- **QUESTION-tmp7d1ws** (proportional regime; does the estimate track the
  stratum): **qualifies / partial evidence.** DLN runs at 10M and 100M
  parameters have d > n (n = 10⁶, Table 1) and estimates still track Aoyagi's
  λ to within the J.2 errors, so in one realizable, noiseless linear family
  with d ≳ n the estimate tracked the theoretical coefficient. It is not a
  proportional-limit theory, the outputs are noiseless, and widths were not
  varied with d/n fixed, so neither part of the question is answered.
- **THEORY-087** (complexity penalty λ log n): **parallel/extends**: eq. 21 is
  its local version under the extra "at least as degenerate as nearby" condition.
- **THEORY-1253** (learning capacity as heat capacity): **supports the
  connection** the CLAIM draws: App. E names LaMont & Wiggins and calls LLC
  estimation measuring heat capacity. Not a derivation.
- **THEORY-975 / THEORY-967** (refined LLC per head, LIT-1535): **background**:
  this paper is the base estimator LIT-1535 refines; App. L's 2-layer
  attention-only transformer is the same architecture family; nothing bears on
  head roles.

## Recheck (grep of record/ after reading)

Terms: local learning coefficient, WBIC, learning capacity, Chaudhari, Aoyagi,
deep linear, entropy-SGD, SGLD, Dinh, rescaling symmetry, flat minima,
PAC-Bayes, relatively finite variance, real log canonical, saddle-to-saddle,
Skalse, simplicity bias. Entries the first search missed:
- **THEORY-1275** (Active; Chen, Lau, Mendel, Wei & Murfet 2023b, LIT-1894,
  NOTE-1462): uses this estimator; NOTE-1462's Table K.1 records λ̂ at n = 5000
  overstating the 5⁺-gon (9.91) against theory 8.5 and the 6-gon 9.03 against
  8.5, with negative λ̂ at high-loss points. **Qualifies** the DLN validation:
  outside DLNs, in a model with known λ, errors of order 15% and wrong ordering
  of equal-λ phases. NOTE-1462 says "Lau et al. (2023) for the LLC estimator;
  not held here", now registered as LIT-tmpnbl2d.
- **LIT-616 / NOTE-473** (Watanabe's WBIC): the estimator is its localized
  form; App. D extends its proof. Background; the LIT and NOTE should cite it.
- **THEORY-108** (Proposed; flatness/connectivity vs endpoint curvature):
  **parallel**: App. E's critique of Hessian flatness (log det H ill-defined;
  PAC-Bayes Gaussian posterior wrong for singular models).
- **CLAIM-tmpgzb8v**, **CLAIM-tmpp83vc**, **QUESTION-tmp82zpm**,
  **SYNTHESIS-034**: cite LLC change as a transition signature; the paper's
  only dynamical content is the Outlook. Background.
- **CLAIM-188** (Active; Gaussian Occam term overcharges singular candidates):
  **parallel** to App. E eq. 23 vs eq. 8.
- Chen, Chang & Chaudhari (2023a), "Learning Capacity": **not held** (no hit for
  title or authors). A possible future neighbour for the finite-n question;
  not read.
- No hit for Skalse, entropy-SGD, relatively finite variance.

## Limitations

Consistency of the practical estimator is a conjecture (App. D). Calibration
only in realizable, noiseless DLNs, one global minimum per network, γ = 1;
relative errors up to ~0.75 hidden by log scale. Elsewhere only relative
comparisons at fixed sampler settings, 5 seeds; real-data relative finite
variance unverified. Single β throughout; γ chosen ad hoc (1 vs 100). Data used
twice at ŵ*ₙ. No error bars on the DLN calibration beyond scatter.

## Candidate THEORY

Title: Lau et al. define the local learning coefficient at a local minimum as
the volume-scaling exponent of its low-loss set and estimate it as nβ*(E[Lₙ] −
Lₙ(w*)) under a posterior tempered at β* = 1/log n and tied to w* by a Gaussian
of precision γ, sampled by minibatch SGLD; that the estimate converges to the
coefficient is conjectured, with the conditions on γ left open, and it is
calibrated only in noiseless deep linear networks of 10² to 10⁸ parameters,
where it tracks Aoyagi's exact values with relative errors up to about 0.75,
mostly underestimates; elsewhere the authors claim only relative comparisons at
fixed sampler settings.

promote_when: The relative errors read off Fig. J.2 confirmed against the
paper's released data or a reproduction of the DLN calibration at one scale or
more, with γ and β as stated; status of the App. D conjecture confirmed as
unproved in the paper's latest version (or a proof cited, which would change
the sentence).
