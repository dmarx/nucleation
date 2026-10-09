---
status: Read
paper: 'LIT-tmphx4s3'
title: 'Probing Latent Hierarchy via Diffusion'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read in full from the arXiv PDF of v2 (arXiv:2410.13770v2, 28 February
    2025; §§1–6 and the references, 13 pp., and Appendices A–D, 17 pp.),
    text extracted with pdftotext and kept as paper.txt in the scratchpad
    download directory dl/reg-c2-iclr25. The ICLR proceedings PDF was
    fetched and compared with v2 by opening text and length only. The
    mean-field construction (App. A.2, Eqs. 20–54) was followed step by
    step; the scaling argument for ξ was checked, and ε* and ν were
    recomputed numerically from Eqs. 22 and 54 at the parameters of
    Fig. 9 (see Limitations). Eqs. 36–43 were followed, not re-derived.
    The Gaussian-field appendix was checked for its logic. Figures were
    read from captions, axis labels and text, not from plotted values.
    v1, the OpenReview reviews (the API refused the forum), the JSTAT
    version and the code were not read. LIT-884 and its reading NOTE-685,
    with THEORY-199, were read first.
date: '2026-10-09'
summary: >-
  In the Random Hierarchy Model with known rules, the tokens changed by
  noising and Bayes-optimal denoising form blocks set by the depth of the
  latent that changed; an annealed mean-field calculation, checked against
  exact belief propagation at one parameter set, gives a correlation
  length diverging as |ε − ε*|^(−ν), ν = log s / log F′(p*), at the class
  threshold, and a susceptibility peak there, which a Gaussian field with
  power-law spectrum lacks. Masked text diffusion and ImageNet diffusion
  show a susceptibility peak at an intermediate noise, over about one
  decade of distance and with no non-hierarchical control.
---
<!-- inactive-ok-file: QUESTION-025 THEORY-199 THEORY-195 THEORY-201 THEORY-194 THEORY-tmpaji42 — Proposed or open; cited as what this reading produced or bears on -->

# NOTE-tmph9awb: Probing Latent Hierarchy via Diffusion

## Contribution

An observable for latent hierarchy that needs no access to the latents:
run a datum forward to noise level t and back, mark which visible tokens
changed, and measure how those changes correlate in space. In a solvable
hierarchical model the paper derives, in the annealed approximation of
[LIT-884](../literature.d/LIT-884.md), that the correlation length of the changes diverges at the noise
level where the class is lost, with an exponent fixed by the branching and
by the slope of the belief map at its unstable fixed point. It shows that
a non-hierarchical field with power-law correlations has no such peak, and
measures a susceptibility peak at an intermediate noise in a text and an
image diffusion model.

## Key insight

In a tree, a token can only change together with another if a latent they
share, or latents on both their paths, changed; the size of a block of
co-changing tokens therefore reads off the depth of the latent that
changed. Below the threshold, the evidence for each latent is amplified on
the way up, so only shallow latents change and blocks are small. Far above
it the evidence is lost within a few levels, so everything above them is
resampled almost surely, and what varies from one trajectory to the next
is again shallow. (The correlations are connected ones, over
trajectories: a change that always happens contributes nothing.) At the
threshold the evidence hovers
undecided for arbitrarily many levels, so latents at every depth can
change and blocks of every size appear: the noise level of the class
transition is a critical point in the usual sense, with a diverging
correlation length. Fourier-style coarse-to-fine resampling has a length
that only grows with noise; the peak is the tree's signature.

## Assumptions

- **Data.** The Random Hierarchy Model of [LIT-877](../literature.d/LIT-877.md) with v symbols per level,
  branching s, depth L, m distinct rules per symbol drawn at random; the
  class is the root. Tree distance ℓ̃ is the number of levels to the
  lowest common ancestor; positional distance r = s^ℓ̃ − 1.
- **Known rules, uniform root prior.** Denoising is exact BP, i.e. a
  diffusion model with the exact score (App. A.1.3). The process is
  class-unconditional.
- **Noise.** The ε-process (leaf belief 1 − ε + ε/v on the true symbol, ε/v
  on the others; Eq. 17), analysed in theory; masking with an absorbing
  state (Eq. 16), studied numerically. The ε-process is the
  trajectory-averaged masking prior with ε = 1 − α_t, but the paper says
  the fluctuations make that identification inaccurate (ε* ≈ 0.74 versus
  t*/T ≈ 0.3).
- **Annealed mean field.** All BP messages and conditional probabilities
  are replaced by their averages over rule draws; fluctuations around
  them are neglected (Eqs. 20, 32–51). Averages depend only on level, not
  position.
- **Regime of a transition.** The divergence needs the class threshold of
  [THEORY-199](../theory.d/THEORY-199.md): L → ∞ and s m (v − 1)/(v^s − 1) < 1 (Eq. 28).
- **Change of a continuous token** is the norm of its embedding change,
  σ_i = ‖x_0,i − x̂_0,i(t)‖, for images.

## Key results

- **Defs. 1–3.** σ_i(t) = +1 if token i changed, −1 if not;
  C_ij(t) = ⟨σ_iσ_j⟩ − ⟨σ_i⟩⟨σ_j⟩ over trajectories, then averaged over
  x_0; χ(t) = Σ_ij C_ij / Σ_i C_ii.
- **Eq. 5 / 51.** Mean-field pair statistics for tokens at tree distance ℓ̃:
  P(σ_i, σ_j) = T^(ℓ̃−1) C^(ℓ̃−1) T^(ℓ̃−1)ᵀ, with T the 2 × 2 matrix of
  reconstruction probabilities of a leaf given whether its ancestor at
  level ℓ̃ − 1 was reconstructed (Eqs. 47–50, from the map with q fixed to
  1 or 0), and C the joint reconstruction of the two children of the
  common ancestor (Eqs. 36–46).
- **Main result / Eq. 54.** Linearising p_ℓ = F(p_{ℓ−1}) about the
  repulsive fixed point p*, the depth to escape it is
  ℓ̃ ∼ −log|ε − ε*| / log F′(p*), so ξ ≃ s^ℓ̃ ∼ |ε − ε*|^(−ν),
  ν = log s / log F′(p*). *Holds in:* annealed approximation, L → ∞,
  Eq. 28 satisfied; a scaling argument, not a theorem.
- **Fig. 2a, 9.** v = 32, m = 8, s = 2, L = 9, 256 data × 256 trajectories:
  BP and mean-field C(r, ε) agree; C(r, ε*) ∼ r^(−a) with a = 1 fitted at
  ε* ≈ 0.74; χ(ε) peaks at ε*; curves for ε from 0.60 to 0.90 collapse when
  r is rescaled by ξ from Eq. 54, with ν ≃ 1.78 quoted.
- **Fig. 2b, 10.** Masking diffusion, same parameters: C(r, t) and χ(t) peak
  near t* ≈ 0.3 T; at L = 10 the root's reconstruction drops from 1 to 1/v
  near t ≈ 0.2–0.3 T while leaves decline smoothly.
- **Fig. 8.** BP sampling and step-by-step backward diffusion with the BP
  score give the same C and χ (L = 8).
- **App. B, Fig. 11.** Gaussian random field, spectrum ∼ ‖k‖^(−a), 0 < a < d:
  modes with κ < κ* = (1/α_t − 1)^(−1/a) are kept, the rest resampled;
  E[z(u)z(0)] ∼ r^(a−d) for r ≪ 1/κ*, cut off beyond; ξ ∼ 1/κ*(t) grows
  monotonically, and χ is maximal at t = T.
- **Fig. 4.** MDLM on WikiText-2 (300 passages × 128 tokens, 50 maskings per
  fraction): correlation length grows to about 7–8 tokens at t* ≈ 0.6 T,
  then falls; χ, integrated over r ≤ 10, peaks there.
- **Figs. 5, 6, 13.** Unconditional ImageNet 256 × 256 iDDPM, images
  cropped to 224 and read as 7 × 7 CLIP ViT-B/32 last-layer patch
  embeddings (344 images × 128 trajectories): χ peaks at t* ≈ 0.6–0.7 T,
  where the cosine similarity of a ConvNeXt-Base's logits to the
  original's drops sharply (10k images).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | In the RHM with exact BP denoising, co-changing tokens form blocks whose size reflects the depth of the changed latent | strong (qualitative) | tree structure; Fig. 3 illustration; BP numerics |
| C2 | In the annealed approximation, the correlation length of changes diverges at the class threshold as \|ε − ε*\|^(−ν), ν = log s / log F′(p*) | moderate | scaling argument from linearising the map (Eqs. 52–54); one data collapse at one parameter set (Fig. 9) |
| C3 | The mean-field C(r, ε) and χ(ε) match exact BP | moderate–strong | Fig. 2a, one parameter set (v = 32, m = 8, s = 2, L = 9) |
| C4 | Masking diffusion on the RHM shows the same peak, at the class transition | moderate | Figs. 2b, 10; numerical only, no theory for masking |
| C5 | A Gaussian random field with power-law spectrum has a monotone correlation length and χ maximal at t = T | strong for the stated model | App. B: analysis, with the score exact, plus numerics |
| C6 | Masked text diffusion and ImageNet diffusion show a susceptibility peak at an intermediate noise | moderate | Figs. 4, 6; one model per modality, about one decade of distance |
| C7 | These peaks are evidence of a latent hierarchy in language and images | weak | analogy with C2–C5; the only non-hierarchical control is C5's field, and no control is run on real models |

## Method

Exact BP on the RHM factor tree from noisy leaf priors, with posterior
sampling top-down (App. A.1); repeated forward–backward runs from each
starting datum to estimate C_ij and χ. Theory: the annealed average of
[LIT-884](../literature.d/LIT-884.md) extended from single-node marginals to pairs, by conditioning the
leaf-level reconstruction on whether an intermediate ancestor was
reconstructed (setting the downward message at that level to 1 or 0) and
computing the joint reconstruction of two sibling subtrees under a common
parent; then a linearisation of the upward map about its unstable fixed
point for the scaling of ξ. Real data: off-the-shelf diffusion models,
with token changes read directly (text) or as CLIP patch-embedding
displacements (images).

## Concepts

- **forward–backward (U-turn) experiment** — noise x_0 to inversion time t
  by the forward process, then sample x̂_0(t) from the backward process.
- **token change σ_i(t)** — a ±1 spin marking whether token i differs after
  the round trip; for continuous tokens, the size of the change.
- **dynamical correlation function C_ij(t)** — connected correlation of two
  tokens' changes over trajectories, averaged over starting data.
- **dynamical susceptibility χ(t)** — the sum of C_ij normalised by the sum
  of autocorrelations: the typical number of tokens that change together.
- **correlation length ξ** — the distance beyond which C(r) falls faster
  than its critical power law; ξ ≃ s^ℓ̃ with ℓ̃ the number of levels the
  evidence stays near p*.
- **ε-process** — [LIT-884](../literature.d/LIT-884.md)'s simplified noise acting directly on leaf
  beliefs.

## Connections

It is [LIT-884](../literature.d/LIT-884.md) continued: the model, the BP denoiser and the annealed map
are taken from there, and the class threshold of [THEORY-199](../theory.d/THEORY-199.md) is the point
everything is organised around. Its new object is the two-point function
of changes, borrowed from the physics of glasses (Donati, Franz, Glotzer
and Parisi; Toninelli, Wyart, Berthier, Biroli and Bouchaud), where a
growing dynamical correlation length signals cooperative rearrangement.
The exponent formula ν = log s / log F′(p*) has the textbook form of a
real-space renormalisation-group exponent, ν = log b / log λ for a block
factor b and relevant eigenvalue λ: the level-by-level BP map is read as a
coarse-graining flow with an unstable fixed point. That reading is mine;
the paper does not use RG language. It sets its peak against the
speciation or critical-window accounts of mixtures (Biroli et al.;
Ambrogioni; Li and Chen), which have a class change but no growing length,
and against the coarse-to-fine reading of image diffusion through
power-law Fourier spectra (Rissanen et al.; Wang and Vastola), which its
App. B formalises and calls complementary: geometric versus semantic
hierarchy. Mei's U-Nets as BP and Garnier-Brun et al.'s transformers
implementing BP are cited as reasons a trained model might approximate the
ideal denoiser.

## Bearing on the record

- **[LIT-884](../literature.d/LIT-884.md) / [THEORY-199](../theory.d/THEORY-199.md).** Supports and extends. Fig. 10 adds a second
  noise process (masking, numerically) with the class drop of [THEORY-199](../theory.d/THEORY-199.md)
  at s f ≈ 0.5, and the main result adds a consequence of the threshold:
  a diverging length of co-change. It inherits [THEORY-199](../theory.d/THEORY-199.md)'s limits: the
  rules are known, the approximation is annealed, and the threshold
  itself is not proved. It produces [THEORY-tmpaji42](../theory.d/THEORY-tmpaji42.md), Proposed, stated for
  the model and the Gaussian-field contrast only.
- **[THEORY-201](../theory.d/THEORY-201.md) ([LIT-883](../literature.d/LIT-883.md)).** Different object. [THEORY-201](../theory.d/THEORY-201.md) is about static
  token–token correlations in hierarchical data, falling by a factor
  about m per level; this paper's §3.3 argues that static correlations
  alone do not make a χ peak, and its critical C(r, ε*) ∼ r^(−1) is a
  property of changes, not of the data. No conflict.
- **[THEORY-195](../theory.d/THEORY-195.md) ([LIT-877](../literature.d/LIT-877.md)).** No bearing: no learning, no sample sizes.
- **[THEORY-194](../theory.d/THEORY-194.md) and the RG works ([LIT-873](../literature.d/LIT-873.md), [LIT-882](../literature.d/LIT-882.md)).** A worked case of a
  coarse-graining map whose unstable fixed point produces a diverging
  length with the RG exponent formula, in a model of data rather than of
  a lattice spin system. It is an analogy of form, not evidence for those
  accounts.
- **[QUESTION-025](../questions.d/QUESTION-025.md).** No bearing on the question asked. The hierarchy is
  constituency, the tokens are positions, and no co-occurrence matrix,
  attribute direction or lattice is measured. It offers an instrument:
  the scale of co-change under forward–backward diffusion as a measure
  of latent depth that does not presuppose linear directions.
- **Practice.** No instruction is given beyond a remark in the
  conclusion that such analyses might help fine-tuning; the subject is
  diffusion models of text and images, which the anthology's
  `generative-modeling` and `signal-structure` topics hold, hence the flag
  on the LIT.

## Limitations

- **The divergence is a scaling argument.** Eq. 54 linearises the upward
  map about p* and equates the correlation length with the depth spent near
  it; the full mean-field C(r, ε) is computed, but the exponent's
  agreement with it is shown by one collapse at one parameter set, and the
  critical decay exponent a = 1 is fitted, not derived. Nothing is proved
  for quenched rules.
- **A number I could not reproduce.** Iterating Eq. 22 at the parameters
  of Fig. 9 (v = 32, m = 8, s = 2, f = 255/1023) gives ε* ≈ 0.731 (the paper
  reports ≈ 0.74 from data, consistent) and F′(p*) ≈ 1.44, so
  ν = log 2 / log 1.44 ≈ 1.89; the caption quotes ν ≃ 1.78. Finite depth
  (L = 9) or another way of extracting ν may explain it; the paper does
  not say how 1.78 was obtained. This is my recomputation, not checked
  against the authors' code.
- **Real-data ranges are short.** Images give a 7 × 7 grid, so r spans 1 to
  about 8; text is integrated to r = 10. A "system-spanning power law" over
  one decade does not discriminate a power law from other slow decays.
- **No non-hierarchical control on real models.** The only contrast is the
  analytic Gaussian field. A flat mixture of many classes would also have
  a class transition at an intermediate noise, and the variance of a
  class flip, which is largest when the flip probability is near one half,
  could give χ a peak there without any intermediate scales; that case is
  neither analysed nor run. (My objection, not tested.) The RHM's own
  signature is the power-law C(r) across scales, which the real-data
  ranges can barely show.
- **The image token is not local.** CLIP ViT last-layer patch embeddings
  have mixed information across the whole image through attention, so
  correlated changes of patch embeddings can partly come from the encoder
  rather than the image. Not discussed.
- **Language has no class.** For text, the "phase transition" is inferred
  from the χ peak alone; nothing plays the role of the class drop that
  locates t* for the RHM (Fig. 10) and images (Fig. 13). The main text puts
  the text peak at t* ≈ 0.6 T, App. C speaks of "the phase transition at
  t/T = 0.5".
- **Small slips.** App. B.2 and B.5 have inequality typos (high-frequency
  modes said to have "SNR > 1"; "for ‖k‖ > κ*, the errors decay"); the
  masking t* is 0.3 T in Fig. 2 and 0.2–0.3 T in Fig. 10 (different L).
- **One parameter set, s = 2.** All RHM numerics use s = 2, v = 32, m = 8.

## Open questions

- A derivation of ν and of the critical decay C(r, ε*) ∼ r^(−a) beyond the
  linearised escape-time argument, and a test at other (v, m, s), where a
  mismatch with log s / log F′(p*) could show.
- Whether a non-hierarchical model with many classes (a flat mixture, a
  Markov chain over tokens) gives a χ peak at its class transition, and
  whether its C(r) at the peak is a power law; that is the control the
  hierarchical reading needs.
- Whether the blocks that change together in text align with syntactic
  constituents, as the authors propose for future work, and whether CLIP
  patch changes survive replacing the encoder by a local one.
