---
status: Read
paper: LIT-247
title: 'Tschannen et al. — On Mutual Information Maximization for Representation Learning'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from the arXiv PDF (1907.13625v2, 23 Jan 2020, the ICLR
    2020 camera-ready, 16 pages), text extracted with pdftotext in
    reading-order and layout modes: abstract, §§1–5, every figure caption
    (1–9), and appendices A–G (the data-processing proposition, the
    adversarial-encoder details, the InfoNCE/K-pair derivation, the
    non-i.i.d. proof, its experimental details, the extra figures and the
    CIFAR10 runs). The figures are plots without a text layer; their
    curves were read from captions and the text, and no number below is
    read off a plot. Replaces the seeded skim NOTE-232.
date: '2026-10-14'
summary: >-
  Four controlled experiments on MNIST image halves (two repeated on
  CIFAR10) show that downstream linear accuracy of InfoNCE- and NWJ-trained
  encoders does not track mutual information. Invertible encoders improve
  while true MI is constant. Higher NWJ bounds from an MLP critic give worse
  features. At matched bound values, ConvNets beat MLPs. The paper also
  proves that InfoNCE is neither a lower nor an upper bound on MI when
  batch pairs are dependent, and recasts it as a multi-class K-pair metric
  learning loss.
---
<!-- inactive-ok-file: THEORY-001 THEORY-006 NOTE-232 — Proposed or Skimmed; the theories that cite or point to this paper, and the skim this reading replaces -->

# NOTE-tmpqr9lw: Tschannen et al. — On Mutual Information Maximization for Representation Learning

## Contribution

Before this paper it was common to explain contrastive representation
learning (CPC, DeepInfoMax, CMC) as InfoMax: the features are good because
the objective maximizes a bound on mutual information between views. The
paper gives controlled counterexamples. Representation quality changes when
true MI cannot. It moves against the bound's value when the critic changes,
and depends on the encoder at a fixed bound value. It also proves that the
InfoNCE bound needs i.i.d. pairs, and offers metric learning (Sohn's
multi-class K-pair loss) as the better description of what InfoNCE does.

## Key insight

MI is invariant under invertible maps, so it says nothing about the geometry
of a representation, and a linear probe depends only on that geometry. What
the estimators actually reward is decided by the inductive biases of the
encoder, of the critic and of the estimator. With a bilinear or inner-product
critic, InfoNCE is a triplet-style metric-learning loss whose MI bound is
"very weak in general".

## Assumptions

- **Setting.** Multi-view objective max_{g1,g2} I_EST(g1(X⁽¹⁾); g2(X⁽²⁾))
  (Eq. 2), with I(g1(X⁽¹⁾); g2(X⁽²⁾)) ≤ I(X; (g1(X⁽¹⁾), g2(X⁽²⁾))) by
  data processing (Prop. 1, App. A).
- **Estimators.** I_NCE (Eq. 3) and I_NWJ (Eq. 4), taken from Poole et al.
  ([LIT-246](../literature.d/LIT-246.md)); expectation over K i.i.d. pairs from p(x,y).
- **Experimental setup (§3).** MNIST, x ∈ [0,1]^784 split into top and
  bottom halves (392 pixels each); g1(x_top) is the representation; linear
  classifier by SAGA (scikit-learn) on all training labels; Adam; bilinear
  critic f(x,y) = xᵀWy unless stated; batch size 128 (so I_NCE ≤
  log 128 ≈ 4.85), learning rate 10⁻⁴; 20 runs, test-set values. Baseline:
  linear classifier on raw x_top, about 85%; supervised MLP or ConvNet about
  94%. §§3.2–3.3 repeated on CIFAR10 (App. G; pixel baseline about 24%).
- **Invertible setting (§3.1).** RealNVP with 30 coupling layers, so
  I(g1(X⁽¹⁾); g2(X⁽²⁾)) = I(X⁽¹⁾; X⁽²⁾) for every parameter value; this MI is
  finite because the halves are not deterministic functions of each other
  (footnote 6).
- **Non-i.i.d. proof (App. D).** Pairs (X_i, Y_i) identically distributed
  but dependent across the batch.

## Key results

- **Invertible encoders, accuracy rises (§3.1, Fig. 1a–b).** "Despite the
  fact that MI is maximized by any instantiation of g1 and g2, I_EST and
  downstream accuracy increase during training". The estimators therefore
  give gradients where true MI has none, and they bias the encoder toward
  linearly separable features. Note that the *estimate* rises; the *true* MI
  is what stays constant.
- **Invertible encoders, accuracy falls (§3.1, Fig. 1c, App. B).** An
  encoder of the same RealNVP architecture, trained adversarially against a
  linear classifier (no MI estimator involved), stays invertible, so still
  maximizes MI, yet ends with classification "significantly worse than
  using raw pixels". The PNG thought experiment makes the same point: "The
  information content alone is not sufficient to guarantee a useful
  geometry in the representation space."
- **Bias toward ill-conditioned encoders (§3.1, Fig. 2, Fig. 5).** A
  residual MLP initialized at the identity, with coupled Gaussian noise
  (σ = 0.05) added to both halves so that non-invertible encoders lose MI:
  I_EST and accuracy rise while the Jacobian's condition number
  log(σ1/σ392) grows. The estimators prefer encoders that attenuate part of
  the input over ones that preserve it, i.e. over true MI.
- **Critic capacity (§3.2, Fig. 3, Fig. 6, Fig. 8).** Bilinear, separable
  (40k parameters) and MLP (40k) critics, MLP encoders. MLP critics "barely
  outperform the baseline on pixel space". "While the testing I_NCE value
  is close to the theoretically achievable maximum value for all critics,
  the testing I_NWJ value is higher for the MLP critic … resulting in a
  tighter bound on the MI." So the "tighter bound, worse representation"
  result is shown for I_NWJ. For I_NCE every critic is saturated near
  log K, and only the accuracy differs.
- **Encoder architecture at a matched bound (§3.3, Fig. 4a–b, Fig. 7,
  Fig. 9).** Minimizing L_t = |I_EST − t| for t = 2, 4 so that MLP and
  ConvNet encoders reach the same bound value, "ConvNet encoders lead to
  clearly superior classification accuracy, for both I_NCE and I_NWJ",
  although both architectures reach about 94% when trained supervised.
- **InfoNCE as metric learning (§4, App. C).**
  I_NCE = log K − E[(1/K)Σ_{i=1}^K log(1 + Σ_{j≠i} e^{f(x_i,y_j) − f(x_i,y_i)})].
  With f(x,y) = φ(x)ᵀφ(y) and a shared encoder this is, up to constants and
  sign, the multi-class K-pair loss of Sohn (2016), Eq. 5; asymmetric
  critics give asymmetric variants. "one can view (5) as learning encoders
  with a parameter-less inner product critic, for which the MI lower-bound
  is very weak in general."
- **Non-i.i.d. negatives (§4, App. D, Fig. 4c, App. E).** Poole et al.'s
  proof uses I(X_1:K; Y_i) = I(X_i; Y_i), which needs i.i.d. pairs. With
  identically distributed but dependent pairs, I(X_i; Y_i) ≤ I(X_1:K; Y_i),
  so "the resulting I_NCE estimator is neither a lower nor an upper bound
  on the true MI". In a 2-d Gaussian with a shared Z per batch, both I_NCE
  and I_NWJ exceed the true MI; with i.i.d. batches both stay below it.
  Hénaff et al.'s CPC (negatives from the same image) and CPC on speech
  (same-speaker negatives) violate the assumption.
- **Optimal critics (§2).** "(3) is maximized by f*(x,y) = log p(y|x) and
  (4) by f*(x,y) = 1 + log p(y|x)", cited to Poole et al.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Estimator-driven training improves a linear probe even when true MI is constant | strong | Fig. 1a–b, invertible RealNVP encoders, 20 runs |
| C2 | Some MI-maximizing (invertible) encoders are worse than raw pixels | strong | Fig. 1c, adversarial construction; PNG argument |
| C3 | The estimators push encoders toward ill-conditioned, hard-to-invert maps | moderate | Fig. 2c and Fig. 5; condition number is a numerical proxy for invertibility |
| C4 | A higher (tighter) I_NWJ from a higher-capacity critic can come with worse features | moderate | Fig. 3, Fig. 8; for I_NCE all critics saturate, so not shown for InfoNCE |
| C5 | At a matched bound value, the encoder architecture decides the representation quality | moderate | Fig. 4a–b, Fig. 9; two architectures, two targets |
| C6 | InfoNCE with a symmetric inner-product critic is the multi-class K-pair loss | strong | algebraic identity, App. C |
| C7 | With dependent pairs, I_NCE is neither a lower nor an upper bound on MI | strong | App. D (that the lower bound fails); the exceedance is shown in Fig. 4c |
| C8 | Metric learning is a more plausible account of InfoNCE's success than MI | weak | argued from C4 and C6, not tested |

## Concepts

- **I_EST** — any sample-based MI estimator used as a training objective;
  here I_NCE or I_NWJ.
- **Critic** — f(x,y) scoring pairs; bilinear xᵀWy, separable
  φ1(x)ᵀφ2(y), or MLP on [x,y]. The boundary between critic and encoder is
  "blurry" when features are taken from an intermediate layer.
- **Linear evaluation protocol** — a linear classifier trained on frozen
  features with all labels; the paper's measure of representation quality.
- **i.i.d. vs non-i.i.d. negatives** — whether the batch's pairs are
  independent draws from p(x,y); not whether negatives come from the batch.

## Connections

The estimators and the InfoNCE proof are Poole et al. ([LIT-246](../literature.d/LIT-246.md)), and this
paper's App. D restates that proof to locate the i.i.d. step. The
metric-learning reading uses Sohn's multi-class N-pair loss. The looser-bounds
observation is set beside Rainforth et al. on VAEs ("Tighter variational
bounds are not necessarily better") and Alemi et al. ("Fixing a broken
ELBO"). Arora et al. (2019) and Ma & Collins (2018) are cited on the number
of negatives. The conclusion points to F-information (Xu et al.) and the
Wasserstein dependency measure as alternatives.

## Bearing on the record

- **[THEORY-006](../theory.d/THEORY-006.md) misstates the first experiment.** It says Tschannen et al.
  "show experimentally that representations can improve while the MI
  estimate does not". The paper shows the opposite about the estimate: in
  Fig. 1 the I_EST value *increases* along with accuracy; it is the *true*
  MI that stays constant, because the encoders are invertible. The sentence
  should read "while the true MI does not change".
- **[THEORY-006](../theory.d/THEORY-006.md)'s "tighter bounds can give worse representations"** is
  supported for I_NWJ (§3.2, Fig. 3). For I_NCE, the bound [THEORY-006](../theory.d/THEORY-006.md) is
  about, every critic reached nearly log K, so the paper does not show a
  tighter InfoNCE bound giving worse features. It shows that the critic
  changes accuracy at nearly equal InfoNCE values. That is a weaker
  statement, and [THEORY-006](../theory.d/THEORY-006.md) should either say I_NWJ or say this.
- **[THEORY-006](../theory.d/THEORY-006.md)'s caveat about in-batch negatives.** This paper is the
  source for what the InfoNCE bound does not cover, and it draws the line at
  dependence between pairs, not at in-batch negatives as such. Its Eq. 3,
  like Poole et al.'s Eq. 10, takes the negatives from the other i.i.d.
  pairs of the batch. [THEORY-006](../theory.d/THEORY-006.md) should cite App. D for the failure under
  non-i.i.d. batches. Hénaff et al.'s CPC, with same-image negatives, is the
  paper's own example of an implementation outside the bound.
- **[THEORY-006](../theory.d/THEORY-006.md) summary.** "tightening the bound does not explain what makes
  the representations good" is a fair summary of §3 as a whole.
- **[THEORY-001](../theory.d/THEORY-001.md)'s pointer** ("Tschannen et al. on why the MI story is not
  the explanation") is accurate. The paper does not discuss density ratios
  or Radon–Nikodym derivatives. It bears on [THEORY-001](../theory.d/THEORY-001.md) only through the
  point that the optimal critic says nothing about which encoder features
  are good: at matched bound values the encoder decides.
- **An index slip inherited from Poole et al.** The paper's Eq. 3
  normalizes over y_j for fixed x_i and states the maximizer as
  f* = log p(y|x). For that indexing the maximizer is log p(y|x)/p(y) plus
  any function of x, which is log p(y|x) only up to a y-dependent term.
  The paper's own App. D and §4 use the other indexing
  (Σ_j e^{f(x_j,y_i)}), for which log p(y|x) is a maximizer. Nothing in its
  experiments depends on this.
- The paper carries ML-practice recommendations (co-design critic, encoder
  and evaluation; treat negative sampling as central). That part is the
  anthology's kind of material; the `anthology-candidate` flag stands.

## Limitations

- Small-scale: MNIST halves, with CIFAR10 for §§3.2–3.3 only. The authors
  call it "a minimal set of easily reproducible empirical experiments".
- Representation quality is measured only by linear probes; the paper
  notes other protocols (§5) but does not run them.
- Two estimators (I_NCE, I_NWJ), three critic types and two encoder types;
  results are trends in plotted curves, with no tabulated numbers or
  significance tests beyond averaging over 20 runs.
- The metric-learning account is an identity plus an argument; it is not
  tested against the MI account by any experiment that separates them.
- Fig. 1c's poor encoder is trained adversarially without any MI estimator,
  so it shows such encoders exist, not that MI estimators find them.

## Open questions

- A notion of information that accounts for the geometry of the
  representation, or for the observer's computational limits (F-information
  is suggested, §5).
- What the right negative-sampling distribution is, given Ma & Collins's
  consistency for any K and Arora et al.'s result that more negatives can
  hurt (§4).
- Whether critic, encoder and evaluation protocol can be co-designed with a
  theory behind them (§5).
