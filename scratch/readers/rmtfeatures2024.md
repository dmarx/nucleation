# Reader notes: rmtfeatures2024 (LIT-2983, arXiv 2410.18938)

Dandi, Pesce, Cui, Krzakala, Lu and Loureiro, "A Random Matrix Theory
Perspective on the Spectrum of Learned Features and Asymptotic Generalization
Capabilities", arXiv 2410.18938v1 [stat.ML], 24 Oct 2024. Read 2026-11-22.

## Provenance

- **Read:** https://arxiv.org/pdf/2410.18938 (arXiv, the author's preprint;
  lawful). HTTP 200, application/pdf, fetched 2026-11-22, converted with
  pdftotext. The arXiv API (export.arxiv.org, no email sent) lists only v1
  (2024-10-24).
- **Read in full:** abstract, §1 Introduction (with Fig. 1), §2 Notations
  and Setting (Assumptions 2.1–2.3), §3 Asymptotics of the First Gradient
  Step (eq. 4, Lemma 3.1), §4 Main Results (Defs 4.1–4.5, Thm 4.6, Cor 4.7,
  Thm 4.8, Fig. 2, proof sketch), §5 Consequences, §6 Conclusions and
  Limitations, Appendix A (structure), the openings of C (C.1) and F.2.
- **Skipped:** the proofs in Appendices B–F (stochastic domination
  machinery, the two-stage deterministic equivalents, the generalization
  formula's Λκ in E). Not needed for any statement below.
- **Venue:** the LIT says AISTATS 2025 (PMLR 258). The arXiv v1 PDF does not
  state a venue; unverified from this copy.
- **Other copies located:** none sought beyond arXiv; the arXiv copy was
  read. No obstacle met.

## Summary

A two-layer network f(x) = (1/√p) Σ a_j σ(w_jᵀx) on isotropic Gaussian
single-index data y = g(xᵀw⋆) takes one gradient step on the first layer at
the maximal-update learning rate η = Θ(d), on n0 = Ω(d^{1+ε}) samples, then
fits the second layer by ridge on n fresh samples, with n, p, η ∝ d. The
paper proves (Lemma 3.1) that the updated weights are, in operator norm,
the initial weights plus a rank-one spike along the target,
W¹ ≈ W⁰ + u(w⋆)ᵀ, so the network is a spiked random-features model with an
isotropic bulk. For that model it proves a deterministic equivalent of the
(extended) feature covariance resolvent (Thm 4.6), giving the Stieltjes
transform of the bulk spectrum (Cor 4.7) and an exact asymptotic
generalization error (Thm 4.8). It is the rigorous version of the replica
result of Cui et al. 2024 (arXiv 2402.04980), extended to a finitely
supported second-layer initialization with k values.

## Contribution

- Rigour for the maximal-update one-step regime, which earlier RMT work
  (Moniri et al. 2023, η = Θ(d^{1/2+ζ}), ζ < 1/2) did not reach.
- The isotropic-bulk approximation of Cui et al. is justified for
  n0 = Ω(d^{1+ε}); for n0/d = Θ(1) the weight bulk has anisotropic parts
  (§3, App. F.2).
- Learning shows in the feature spectrum chiefly as a **reshaped bulk**
  (wider support, longer tails), plus k Θ(d) outliers from feature means.
- Second-layer variability k enlarges the expressible function class and
  lowers test error (Fig. 2).

## Key results (with quotes)

1. **Weight spike** (§3, eq. 4; Lemma 3.1). "the hidden layer weights after
   one GD step are approximately low rank: W¹ = W⁰ + uvᵀ + ∆"; Lemma 3.1:
   "‖W⁽¹⁾ − (W⁽⁰⁾ + u(w⋆)ᵀ)‖₂ → 0 a.s." for n0 = Ω(d^{1+ε}), with
   u = ηc1c⋆1a⁰/√p. "It is precisely the presence of such correlated
   components that enables the trained model to surpass the Random Features
   performance".
2. **Two scales in the features** (§4, after Def 4.2). "the first term
   varies only along a k-dimensional subspace with variations governed by
   κµ, while the second term contributes to the 'bulk' of the feature
   covariance."
3. **Deterministic equivalent** (Thm 4.6) and **bulk Stieltjes transform**
   (Cor 4.7): "Let µd denote the empirical spectral measure of the bulk
   covariance Φ̃ᵀΦ̃/p … md(z) → β Σq b⋆q(z)."
4. **Generalization** (Thm 4.8): "the generalization error … is given by the
   following low-dimensional, deterministic formula: lim E[εgen] =
   Eκ[Λκ(…)]", functions of V⋆(−λ), ν⋆(−λ), i.e. of the whole deterministic
   equivalent, not of outliers alone.
5. **Spectrum after training** (§5, Fig. 1). "this bulk is modified from the
   unspiked RF spectrum …, displaying in particular a wider support and
   longer tails in this particular instance. The spectrum also exhibits
   outlying eigenvalues of order Θ(d), arising from the means ϕ̄µ, not
   represented in Fig. 1". The k extra spikes are "'spurious spikes' …
   present due to the finite support assumption for the second layer".
   Ties to "previous empirical observations [Martin and Mahoney, 2021, …
   Wang et al., 2024] that heavier tails can emerge after feature
   learning, a behaviour which further tends to correlate with better
   generalization".
6. **Bulk–spike recombination** (§5). For non-maximal steps Moniri et al.
   find ℓ spikes beside the RF bulk; "in the maximal step size limit ζ =
   1/2, the corresponding ℓ diverges, and it is largely unclear how the bulk
   and spikes recombine"; "the departure of the bulk from its untrained
   shape can be intuitively seen as a result of the recombination between
   the untrained bulk and some of the spikes" (offered as intuition).
7. **Expressivity** (§5, Fig. 2). "there is a net increase of the
   expressivity of the neural network for larger vocabulary sizes k"; with
   erf and k = 1 only monotone sigmoids in κ are expressible.

## Assumptions

Isotropic Gaussian inputs; single-index target with bounded Lipschitz link,
E g = 0, E g′ ≠ 0; odd Lipschitz activation with bounded σ″, σ‴; one
gradient step on the square loss, second layer frozen during it; n0 =
Ω(d^{1+ε}); proportional n, p, η/d; first layer uniform on the sphere;
second layer from a finite vocabulary of k values (Assumption 2.1); a
non-degeneracy condition (4.3); fresh samples for the ridge step;
asymptotic in d.

## Concepts

Spiked random features model (SRFM); maximal-update (µP) step size;
(conditional) Gaussian equivalence principle; deterministic equivalent;
extended resolvent; shifted Hermite coefficients cℓ(κ, ζ); bulk of the
feature covariance vs Θ(d) "spurious spikes"; bulk–spike recombination.
No BBP threshold, detectability transition or phase transition appears in
the paper.

## Verdict on how the exchange and the LIT characterize it

- LIT-2983's summary: "After a large gradient step, the learned feature
  matrix is a spiked random matrix whose outliers carry the learned
  directions and set the generalization error." **Partly wrong.** The spike
  is in the *weight* matrix (Lemma 3.1); the feature matrix σ(XW¹ᵀ) is a
  nonlinear transform of it. In the *feature* covariance the paper's
  headline is a modified *bulk* (Fig. 1, §5), and its Θ(d) outliers come
  from the feature means and are tied to the finite second-layer support.
  The generalization error is a functional of the full deterministic
  equivalent (Thm 4.8), not of the outliers. Correct to: "after one
  maximal-update gradient step the first-layer weights are a random bulk
  plus a rank-one spike along the target; the paper gives the feature
  covariance's asymptotic spectrum, whose bulk widens and grows longer
  tails, and the exact test error."
- The status note's "spikes in the feature spectrum after a gradient step"
  (A32): half right; spikes in the weights, and in the features Θ(d)
  outliers plus a reshaped bulk.
- CLAIM-799's use (A32 §6: work tying learned features to spiked
  random-matrix models, so "the spectral perspective is not merely an
  analogy", without establishing active matter or criticality): **fair.**
  The paper does tie learned features to a spiked RF model rigorously, and
  says nothing about criticality, dynamics beyond one step, or active
  matter.

## Bearing on named codes

- **CLAIM-799** (geometric separation, decodability, spectral detectability
  distinct; BBP marks estimator detectability): **background, and
  qualifies §6's citation.** It supports the narrow point that the spiked
  picture is theorem, not analogy, for one step (Lemma 3.1). It does not
  touch BBP or detectability thresholds. It adds a nuance the claim lacks:
  here learning is visible spectrally not only as a separated outlier but
  as a change in the *shape of the bulk* ("wider support and longer
  tails"), so "spectral detectability" in the outlier sense is not the only
  spectral signature of learned structure. Its outliers (Θ(d), from means)
  are far above any BBP-type threshold; the paper is silent on a
  sub-threshold regime.
- **TERM-tmpf5ymd** ("bulk" by count vs by weight): **supports the
  by-count sense as RMT usage, with a worked example.** The paper uses
  bulk by count throughout: "a random bulk (F0) and a spike", "the
  'bulk' of the feature covariance", Fig. 1 "Bulk spectrum". Its spectrum
  is a case where the senses split: the k Θ(d) outliers (few, carrying the
  largest eigenvalues) are bulk by weight; the continuum is bulk by count.
  Also of use: the bulk by count is itself what learning changes (longer
  tails), so "bulk" ≠ "unlearned noise" here.
- **CLAIM-tmp2r6ur** (most informative signal in a truncated band; top
  directions carry common, weakly discriminating structure): **leaves
  open, with a contrast.** The top outliers here do come from the
  features' *means* (common structure, in a sense), but those means are the
  functions c0(κ, ζq) of the target projection κ, and the gain in test
  error with k comes through them (Fig. 2, §5). So in this model the top
  directions carry task signal, not stop-word-like structure. The paper
  measures no per-direction discriminativeness, and has no near-zero floor
  analogue; it neither tests nor refutes the band claim.

## Limitations

One step only; Gaussian isotropic data; single-index target; two layers;
finite second-layer support (the paper's own listed limit, and the source of
the "spurious" spikes); asymptotic; the heavier-tails link to
generalization is cited as empirical (Martin–Mahoney, Wang et al. 2024) and
shown in "this particular instance" (Fig. 1), not proved in general; the
bulk–spike recombination is intuition. The anisotropic regime n0 = Θ(d) is
characterized only in the weights (App. F.2), not in the main theorems.

## Candidate THEORY

Sentence: "Dandi and colleagues prove that after one maximal-update gradient
step on Gaussian single-index data, with n0 = Ω(d^{1+ε}) samples, a two-layer
network's first-layer weights are a random bulk plus a rank-one spike along
the target, and they give the resulting feature covariance's asymptotic
spectrum, whose bulk widens and lengthens its tails beside k outliers of
order d from the feature means, and the exact test error of the ridge-fitted
readout."

promote_when: "An independent reading or replication confirms, for the
stated setting, the rank-one spike approximation of Lemma 3.1, the
deterministic equivalent of Theorem 4.6, and that its bulk spectrum and test
error match simulation as in Figures 1 and 2."

## Recheck (grep after reading)

Searched record/ for: maximal update / µP, lazy / feature learning, random
features, Gaussian equivalence, deterministic equivalent, heavy tails /
Martin–Mahoney, conjugate kernel, Ba et al. 2022 (2205.01445), Moniri
(2310.07891), Cui (2402.04980), Dandi 2023 (2305.18270), single-index.
None of the four cited arXiv works is held. Held entries the first search
missed:

- **THEORY-2133** (Yang and Hu, abc-parametrizations: features learned
  when the smallest exponent is zero) and **CLAIM-775** (a parametrization
  allocates rates): background. The paper's η = Θ(d) is the Maximal Update
  parametrization; it is the regime where these say features are learned,
  and the one-step result is a concrete instance.
- **THEORY-2135** (Chizat, Oyallon and Bach, lazy training): contrast; the
  paper's point is leaving the lazy/RF regime, which it cites.
- **THEORY-106** (random-features ridge, double descent): background; the
  paper's baseline is that RF model (the dashed initialization spectrum).
- **THEORY-283** (hierarchical multi-index targets, weak recovery):
  parallel; same Gaussian multi-index family, different question.
- **THEORY-813** (lazy training does not collapse features): parallel;
  learned structure only off the kernel regime.
- **THEORY-420** (random-matrix null for weight spectra) and **LIT-856**
  ("Small Singular Values Matter"): contrast. Here learning reshapes the
  bulk and adds outliers; it says nothing about the bottom of the spectrum.
- **LIT-857** (Boncoraglio et al., single-head attention, weights spectra,
  overlapping group): parallel, the same RMT programme applied to attention.
- **CLAIM-798** (active matter weak/strong): A32 §6 cites this paper against
  the strong reading; consistent, the paper is one step and no dynamics.
- **THEORY-078**, **CLAIM-164**, **CLAIM-827**, **CLAIM-804**, **CASE-301**:
  already named in CLAIM-799; no new bearing beyond the bulk-shape nuance
  above.
- **LIT-2984** (Wang, Wu and Fan, nonlinear spiked covariance, 2402.10127):
  the paper does not cite it; a sibling reading.

## Neighbours

Not needed: the work itself was read.

Note for the filer: the paper cites, and the record does not hold, Ba et al.
2022 (arXiv 2205.01445), Moniri et al. 2023 (2310.07891), Cui et al. 2024
(2402.04980) and Wang et al. 2024 ("Spectral evolution and invariance in
linear-width neural networks", NeurIPS 36). Not read here.
