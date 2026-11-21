# Reader notes: LIT-tmp0gbj6 (arXiv 2605.01609)

Acharya, Rimal & Dhakal, "Concepts Whisper: Spectral Anti-Concentration and
the Dual Geometry of Transformer Representations". Read 2026-11-21.

## Provenance and copies located

- **Read:** arXiv PDF https://arxiv.org/pdf/2605.01609 (v2, 29 Aug 2026,
  25 pp.; v1 2 May 2026). Kind: arXiv preprint, the authors' own upload.
  Fetched 2026-11-21, HTTP 200, no obstacle. Read in full: main text §§1-9,
  Limitations, Ethics, appendices A-M with Tables 1-15. Figures read through
  their captions only (images not inspected); reference list skimmed.
- **Located, not read:** ACL Anthology, EMNLP 2026 main,
  https://aclanthology.org/2026.emnlp-main.2362/ (landing page HTTP 200 on
  2026-11-21, title matches; PDF at
  https://aclanthology.org/2026.emnlp-main.2362.pdf not fetched, since arXiv
  v2 postdates acceptance). Not compared with v2; page numbers below are
  arXiv v2's.
- **Supplement read for one passage:** Park, Choe & Veitch (2024), "The
  Linear Representation Hypothesis and the Geometry of Large Language
  Models", arXiv https://arxiv.org/pdf/2311.03658 (v2, 17 Jul 2024), fetched
  2026-11-21, HTTP 200. Read §3.1-3.2 only (Theorem 3.2, eq. 3.2-3.3).
  Already held: LIT-304 (THEORY-018, NOTE-302). Used below for the rival
  reading of the "dual geometry".
- No email address sent anywhere. Downloads in the scratchpad, not the repo.

## Summary

The authors set out to test whether whitening by the "causal inner product"
of Park et al. helps cross-lingual Procrustes transport (WCA). It does not:
with Haar-random eigenvectors and the true eigenvalues ("fake WCA"), results
are the same (50.3% vs 51.0% win rate, p = 0.95; §4), so any benefit is
spectral regularization. Inspecting the eigenbasis then showed that concept
directions taken from activations put little of their Euclidean energy in
the top eigendirections of the unembedding second moment ("anti-
concentration"), while the same concepts taken as differences of
unembedding rows put more there ("dual geometry"). Steering and POS probing
give partial functional readings.

## Definitions (checked)

- **Which spectrum.** Not an activation covariance and not a Gram of
  representations. Eq. (1), p. 2: "the regularized uncentered second moment
  of the unembedding rows, ΣL = (1/|L|) Σ_{w∈L} γ(w)γ(w)ᵀ + τI", τ = 0.1,
  L by default a language subset of the vocabulary. "For brevity we refer to
  ΣL as the unembedding covariance throughout, though as defined it is an
  uncentered second moment". So ΣL = W_Lᵀ W_L/|L| + τI: its eigenvectors are
  the right singular vectors of the (sub-)unembedding matrix and its
  eigenvalues σᵢ²/|L| + τ. It is the d×d dual of the |L|×|L| Gram W_L W_Lᵀ,
  and up to scale and ridge it is G_logit = WᵀW of CLAIM-tmppkdjz. Variants
  (full vocabulary, centered, frequency-weighted, input embeddings; Table 2)
  all give the same sign. Limitations, p. 9: "activation-covariance spectra
  may reveal additional structure" — i.e. not measured.
- **The statistic.** §3, p. 3: fractional energy Eᵢ = (vᵀuᵢ)²/‖v‖², cumulative
  C(k) plotted "against cumulative variance V(k) = Σ_{i≤k} λᵢ/Tr(Σ)"; "Gini
  deviation is the signed area between C(·) and the uniform baseline
  (negative = anti-concentration)"; SCM = the V(k) at which C(k) = 0.5. The
  baseline is uniform in variance, not in index, so a random direction in an
  anisotropic spectrum already scores negative: "random unit vectors
  evaluated in these spectra are themselves negative (−0.16 to −0.28), so the
  raw statistic cannot separate the two" (§5, p. 4).
- **Concept directions.** Activation side: difference of means of final-layer
  pooled residual activations over counterfactual word pairs; SAE decoder
  columns (Gemma Scope, Llama Scope); L2 logistic-probe weights. Vocabulary
  side: mean of γ(w⁺) − γ(w⁻). 27 word-level concepts (Park et al.'s pairs
  from BATS) plus 15 more semantic BATS categories. Whether the final norm's
  gain is folded into W_U is not stated.
- "Anti-concentration" here is this energy-vs-variance statistic, not the
  probabilistic term of art (small-ball/Littlewood–Offord).

## Key results

1. **Anti-concentration, raw.** §5, p. 3: "the mean Gini deviation is −0.282
   and all 17 models are negative (one-sample t = −11.5, p = 3.8 × 10⁻⁹,
   n = 17)". Same for the expanded semantic set (−0.278).
2. **Against the right null, smaller.** §5, p. 3: "concept directions are
   more tail-aligned than their matched nulls in 13 of 17 models, with a mean
   true-minus-null Gini gap of −0.082; Llama 3.2 (1B and 3B), Mistral-7B-v0.3,
   and OLMoE are the exceptions". Table 8: Llama-3.2-3B concept SCM 0.771 =
   random 0.771; OLMoE gap −0.116.
3. **Three methods agree.** Table 4, p. 5: SAE features Gini −0.19 to −0.28
   (p down to 10⁻²⁸, "across concepts within a model"); probes on Llama-3.2-3B
   (−0.167) and Qwen2.5-3B (−0.185); probes "failed on gemma-2-9b".
4. **Depth, not training.** §5, p. 4: "near-neutral at the embedding layer
   (mean Gini −0.009) and tail-aligned from the early transformer layers
   onward (−0.17 at layer 0, deepening to −0.30 near mid-depth)". No
   training checkpoints are examined anywhere.
5. **Dual geometry.** §7, p. 5: unembedding contrasts "concentrate in
   high-variance eigendirections (positive Gini), the opposite sign of
   activation-space directions"; against 1,000 random token-pair differences,
   "Random pairs mildly anti-concentrate (mean Gini ≈ −0.10); concept pairs
   concentrate (mean ≈ +0.07); p < 10⁻⁴" on four models (Table 10); mean
   +0.090 over 11 models (App. H). Interpretation, p. 5: the unembedding
   places contrasts "along high-variance directions, where they maximally
   influence logit differences", while activations "encode the same concepts
   in the spectral tail".
6. **Steering.** §8, Table 5: injecting the top-10% component ("shouting")
   raises perplexity more than the bottom-10% ("whispering") in 4 of 5 models
   inside a post-hoc window ("both arms stay below a +1000% perplexity
   increase"; "the window is post-hoc"). "whether it preserves
   concept-manipulation strength is untested here" (§9, p. 7).
7. **POS probing.** Table 6: top-k beats bottom-k in 6/8 models by 1.6-5.2
   points; both Qwen 2.5 reverse; on Chinese both Qwen models reverse. Top-k
   holds 26-40% of variance, bottom-k 1.5-2.6% (App. L), yet "the accuracy
   gaps are modest".
8. **WCA null.** §4: "any observed benefit of WCA is attributable to spectral
   regularization ... rather than to semantically meaningful causal
   eigendirections."

## Contribution

An empirical, 17-model measurement of where activation-space concept
vectors sit in the right-singular basis of the unembedding, a negative
result for the causal inner product's eigendirections in transport, and a
sign flip between activation-side and vocabulary-side concept vectors.

## Assumptions

Euclidean norm on the residual stream is meaningful (energy fractions are
Euclidean); ΣL from one matrix (the LM head) is the right basis for every
layer; word-level single-token counterfactual pairs; base decoder-only
models; final-layer pooling.

## The "dual geometry": a rival reading (the reader's, flagged)

The paper presents the sign flip as evidence that "the forward pass rotates
concept information from the vocabulary geometry into the low-variance
activation subspace" (App. E) and as "incompatible with a pure anisotropy
account" (§5). It does not mention the result of the paper it builds on:
Park et al.'s Theorem 3.2 (arXiv 2311.03658, p. 4) says the causal inner
product's Riesz map sends a concept's unembedding representation to its
embedding representation, ⟨γ̄_W, ·⟩_C = λ̄_Wᵀ, and with their choice
M = Cov(γ)⁻¹ (eq. 3.3) that is λ̄_W ∝ Cov(γ)⁻¹ γ̄_W. Multiplying by Σ⁻¹
divides the i-th eigencomponent by λᵢ, moving energy to the tail. So, to the
extent Park et al.'s unification holds, a dual geometry with this sign is
expected, not a separate discovery, and "rotation" is not needed (it is a
rescaling in a fixed eigenbasis). A toy check (python3 -I, d = 512,
λᵢ = 1/i + 0.1, 500 draws, Gini as 2×signed area of C against V): random
directions −0.084; contrasts drawn with covariance Σ −0.003; their Σ⁻¹
images −0.127. Qualitative only; the paper's area normalization is not
given. Whether the measured activation vectors match Σ⁻¹γ̄ was not tested
by the paper.

## Verdict on how the exchange characterized it

- LIT summary ("Concept information ... lives in low-variance spectral
  directions as well as high ones"): too weak in one way, wrong in another.
  The paper says activation concept *directions* sit disproportionately in
  the low-*eigenvalue* directions of the *unembedding* second moment; it does
  not measure "information" (no decoding from the tail subspace except POS
  probing, which favours the head), and not representation variance.
- CLAIM-tmppkdjz ("concept directions sit in the low-variance tail of the
  unembedding covariance"): accurate, with the caveats that "covariance" is
  the paper's shorthand for an uncentered second moment and that against a
  matched random null the effect is −0.082 and fails in 4 of 17 models.
- ARG-tmpjx3ww maps the paper to "representation variance" set against
  "concept separation". Both halves are off: the spectrum is the
  unembedding's (≈ WᵀW, the "logit amplification" metric the ARG gives to
  Xu), and the measured quantity is the Euclidean energy of a concept
  vector, not a separation. The finding belongs beside Xu's under
  G_logit, not as a separate "representation variance" instance.
- U25/QUESTION framing "during learning": the paper has no training
  dynamics; its only trajectory is through depth.

## Bearing on the named codes

- **CLAIM-tmppkdjz** — *qualifies; weak support at most.* It is about one
  metric (G_logit up to scale) and where concept vectors point in it. That
  concept-defining vectors put their energy where ‖Wv‖ is small is a case of
  "small under the logit metric, carrying a distinction" only if pointing
  there counts as importance. The paper's own effect measures run *with*
  G_logit, not against it: head injection disrupts perplexity more (Table 5)
  and the head carries more POS information (Table 6). It shows no reversal
  of the kind the claim constructs (a predictive metric ranking a small
  direction above a large one); concept-manipulation strength of tail
  steering is "untested". Supports the weaker point that a direction's rank
  depends on which vector of a concept you measure (activation vs
  vocabulary side) — the dual geometry is itself a metric/representation
  dependence, and under Park's map it is exactly the Σ vs Σ⁻¹ duality.
- **ARG-tmpjx3ww** — *qualifies.* Its verdict stands (none of the findings
  measures the parameter-space predictive Fisher, so nothing here bears on a
  hyperribbon), but its first critical question misdescribes this work's
  spectrum and measure (see verdict). Count it under the logit metric with
  Xu, so the four findings are three distinct spectra, not four.
- **QUESTION-tmp82zpm** — *leaves open; background.* Confirms the QUESTION's
  note that none of the works tracks a direction through learning: "Our
  layer-wise analysis is descriptive" (Limitations, p. 9), and the only
  trajectory is through depth (−0.009 → −0.17 → −0.30). Instruction tuning
  on two models leaves the Gini unchanged (App. D) — the nearest thing to a
  before/after, and not a learning curve. Relevant to the QUESTION's
  reparametrization caution: the statistic is Euclidean in h and in the
  eigenbasis of WᵀW, and is not invariant under h ↦ Ah, W ↦ WA⁻¹ (which
  leaves the logits unchanged, THEORY-234/THEORY-018); vᵀΣv is invariant,
  the energy fraction is not.
- **TERM-tmpol232** — *parallel/contrast.* The paper uses Park et al.'s
  "causally separable concepts" (p. 1), a fourth sense the TERM does not list
  — closest to its excluded "separability of a joint law" (Park's
  Assumption 3.3 is independence of λ̄_Wᵀγ and λ̄_Zᵀγ under a random word).
  The probe results (accuracy > 0.99, §6) are sense 2 (class separation with
  a linear readout) in the full space; the subspace POS probes are sense 2
  restricted to head or tail. Nothing here is sense 3 (no outlier detaching
  from a bulk is studied). Anti-concentration is not a separation in any of
  the three senses: it is a placement of a direction relative to a spectrum.

## Limitations

Word-level concepts only; one unembedding-derived basis applied to
residual activations; raw statistic confounded with anisotropy (the paper
says so); matched-null effect modest and absent in 4/17; steering window
post-hoc with uncorrected p across 30 configurations; POS gaps of a few
points and reversed in Qwen 2.5 and in Chinese; base models; no training
dynamics; final-norm gain treatment unstated; dual geometry not compared
with Park's Σ⁻¹ prediction.

## Candidate THEORY

"Acharya, Rimal and Dhakal find that, in 17 decoder-only language models,
word-level concept directions taken from final-layer activations put less
of their Euclidean energy in the top eigendirections of the unembedding's
regularized second moment (the right singular basis of the unembedding)
than the uniform-in-variance baseline, and more in its tail than
norm-matched random directions in 13 of the 17, while differences of the
same concepts' unembedding rows lean the other way."

promote_when: an independent replication, or the authors' released code
run on at least the four models of Table 10, reproduces both the
activation-side anti-concentration against the norm-matched random null in
most models and the opposite sign for unembedding-row contrasts against
random token pairs.

## Recheck (record/ searched again, 2026-11-21)

Terms searched: causal inner product, linear representation hypothesis,
Park et al., anisotropy, unembedding, outlier/rogue dimensions, whitening,
steering vector, superposition, Ethayarajh, LASER, spectral tail. Held
entries the first search (by the exchange's words) missed:

- **LIT-304 / NOTE-302 / THEORY-018** (Park, Choe & Veitch, the causal inner
  product) — *background and a rival reading.* THEORY-018: the inner product
  is fixed by a stipulation (D = I) and is not intrinsic. Bears twice: the
  paper's WCA null fits it (no special eigendirections), and Park's Theorem
  3.2 predicts the sign of the dual geometry (above).
- **THEORY-234** (Marconato et al., LIT-950: equivalence up to invertible
  linear maps) — *qualifies* the statistic's coordinate-dependence; bears on
  QUESTION-tmp82zpm's reparametrization caution.
- **THEORY-420** (Staats et al.) — already cited; this paper cites Staats
  too ("show small singular values carry information", p. 2).
- **LIT-tmp4det7** (Xu, unread) — same spectrum up to scale (WᵀW); the two
  works should be read together under G_logit.
- LASER (Sharma et al., arXiv 2312.13558), cited by the paper, is not held
  as a LIT; it is mentioned in passing in NOTE-659/NOTE-661 and LIT-855-859
  (bodies, not checked further). Background only.
- NOTE-2219 (tuned lens) mentions outlier dimensions — background.
- No held entry on whitening sentence embeddings (Su et al., Huang et al.)
  was checked; "whiten" hits are mostly other senses.
