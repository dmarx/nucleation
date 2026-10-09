---
status: Read
paper: 'LIT-tmp55jc0'
title: 'Small Singular Values Matter'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read in full from the arXiv PDF of v3 (6 November 2025, 29 pages,
    NeurIPS 2025 camera-ready), via a text extraction: Sections 1–7, the
    Limitations, Appendices A–J and Tables 1–5 read; page 9 (the
    random-matrix model, Eqs. 10–13) read from a rendered image because
    the extraction garbled the formulas. The figures' plotted values are
    not recoverable from the text and were read through their captions
    and the prose. The derivation of Eq. 13 is followed as far as the
    paper takes it (Appendix F); its key step, the "blue function"
    relation for the outlier, is quoted from an unpublished Leipzig
    master's thesis (Forner 2024) and was not checked. The NeurIPS
    checklist was skimmed. The anthology's reading (ANTH-NOTE-263) was
    read after this one was drafted, to compare, not as a source.
date: '2026-10-09'
summary: >-
  Uses the Marchenko–Pastur law as a null model for trained transformer
  weights and finds departures at both ends of the spectrum, the lower
  end only in rectangular matrices, whose null has a positive lower
  edge. In the MLP up and gate projections the below-bulk directions
  align with the input activations' principal directions, and in
  rectangular matrices the smallest decile is never the least important
  to remove. A Gaussian teacher–student ensemble shows one way it can happen: the loss
  suppresses noise along a learned direction, a negative spike that
  holds a weak signal below the bulk. Overlap and ablation importance
  disagree for several matrix types, so "departs from the null" and
  "carries information" are not shown to coincide in general.
---
<!-- inactive-ok-file: LIT-369 — Proposed; named as a neighbour in the random-matrix reading of trained weights, not leaned on -->
<!-- inactive-ok-file: THEORY-078 — Proposed; named for the bulk-edge convention this reading qualifies, not as settled -->

# NOTE-tmp8r19k: Small Singular Values Matter

## Contribution

Before this paper, random-matrix readings of trained weights looked for
learning in the outliers above the Marchenko–Pastur bulk, or in the heavy
upper tail, and low-rank compression discarded the bottom of the spectrum
as the cheapest part to lose. This paper points out that a rectangular
matrix's null spectrum ends above zero, so "below the bulk" is a departure
from the null too. It measures such departures in three trained
transformers, shows that in the MLP up and gate projections their singular
vectors line up with the principal directions of the matrix's input, shows
that removing them costs more than removing most larger singular values,
and gives one solvable model in which a learned direction ends up below the
bulk.

## Key insight

What locates information in a learned matrix is distance from the null
spectrum, not size. Under the i.i.d. null, the singular values of a
rectangular matrix fill an interval [ν₋, ν₊] with ν₋ > 0; a learned
direction can leave that interval at either end. Magnitude order, which
Frobenius-optimal truncation follows, is the right order only when the null
reaches zero, as it does for square matrices; and there the paper's
ablations do fall monotonically with magnitude.

## Assumptions

- **The null.** Entries i.i.d., zero mean, finite variance; m, n → ∞ with
  q = n/m fixed (n ≥ m). Then the singular-value density is Eq. 4 on
  [ν₋, ν₊], ν± = σ̃(1 ± √(1/q)), σ̃ = σ√n. The variance of each empirical
  matrix is estimated by Azadkia's method, not fitted to the bulk.
- **Finite size.** BERT and Pythia matrices have a smaller dimension of 768
  and 1024, Llama 4096. Outlier counts (Table 3) depend on where the finite
  matrix's edge is drawn; no finite-size correction or edge-fluctuation
  scale (Tracy–Widom) is used, so "outlier" means "outside the asymptotic
  support".
- **Overlap.** O_k = max_j (v_k · f_j), v_k the k-th right singular vector,
  f_j the eigenvectors of the covariance of the activations entering the
  matrix, estimated on WikiText (BookCorpus in Appendix B). As printed it
  has no absolute value, so it depends on the arbitrary signs of v_k and
  f_j; an absolute value is presumably meant. The 3σ reference band is for
  a random unit vector.
- **Ablation.** Zero one decile of the rank-ordered singular values (Eq. 9)
  in every matrix of one type, or (RULER, BERT) of all types at once, and
  reconstruct from the original singular vectors. No re-fitting.
- **The model** (Section 6). Inputs ξ ~ N(0, 𝟙); teacher uᵀλξ, ‖u‖ = 1;
  student vᵀWξ with v fixed and normalised, W ∈ ℝ^{K×N}, q = K/N < 1.
  Weights are drawn from the Gibbs ensemble
  P(W) ∝ exp[−Nβε_g(W) − (N/2α) Tr WᵀW], β the inverse temperature (in an
  annealed approximation, examples per input dimension) and α a Gaussian
  prior or L2 strength. A linear network, one rank-one rule, one fixed
  second layer.

## Key results

- **Spectral shape** (Figure 1, Table 3). Initialized matrices agree with
  Eq. 4. Trained ones show outliers above the bulk in all matrix types and
  below it in rectangular ones: Llama-3.1-8B, layer 9, Up-Projection 120
  below and 253 above; Query 0 below, as it must be. Below-bulk counts are
  2–6.5% of singular values in the up and down projections (Appendix H),
  with no clear trend across the three model sizes.
- **Overlap** (Figures 2–4, 8–9, 12). Above-bulk outliers overlap the
  activation-covariance eigenvectors beyond the 3σ band in Query, Key and
  Value. Below-bulk outliers do so in Pythia's Up- and Down-Projection and
  Llama's Up- and Gate-Projection. Not in Attention-Output (any model), not
  in Llama's Down-Projection, and not for the below-bulk end of Llama's Key
  and Value although those are rectangular. Over Pythia's pretraining
  (Figure 10) above-bulk overlap appears within 1,000 steps; below-bulk
  overlap in the projections appears late.
- **Perplexity** (Figure 5; Figure 11 on BookCorpus). Removing the largest
  decile always hurts most. In square matrices damage decreases
  monotonically down the deciles; in rectangular ones the smallest decile
  outranks some larger ones, and for the Down-Projection it is second.
- **Benchmarks** (Llama-3 8B). GSM8K 3-shot, baseline 43.2% (Table 1):
  Down-Projection deciles 1 to 10 leave 2.0, 30.2, 28.0, 27.1, 26.2, 22.0,
  11.0, 15.0, 5.0 and 0.0%; Attention-Output decile 1 leaves 40.0%; Query
  40.3%; Gate-Projection 34.1%, the fourth most damaging. HumanEval,
  baseline 32.32% (Table 5): Down-Projection decile 1 leaves 0.0%, as do
  deciles 9 and 10. RULER at 8192 tokens, all matrix types at once
  (Table 2): decile 1 scores 0.0 on all five tasks, as does decile 10;
  decile 9 scores 0.0 on four and decile 8 on three.
- **Layers** (Table 4, BookCorpus perplexity, baseline 6.0045). Removing a
  decile from one layer barely matters except layer 0, where the top decile
  gives 62,355.6 and the bottom decile 6.3161, the second largest.
- **Fine-tuning order** (Figure 6, BERT, all matrices, 3σ from six unpruned
  runs). Prune decile 1 then fine-tune: BoolQ recovers, RTE and SST-2 lose
  a little but significantly. Fine-tune then prune: all three lose
  significantly.
- **The model** (Eqs. 11–13, Appendix F). Completing the square gives
  W = W₀ + X with W₀ = αβλ/(1 + αβ) vuᵀ and X Gaussian with columns
  uncorrelated and row covariance Σ = α𝟙 − α²β/(1 + αβ) vvᵀ (Eq. 12): the
  noise variance along v drops from α to α/(1 + αβ). For
  0 < (1 + αβ)⁻¹ < 1, X has a singular value below its bulk, and for
  λ < √(α(1 − q)) this stabilises a below-bulk outlier of W at ⟨ν_min⟩
  (Eq. 13), which as β → ∞ tends to λ√(1 − αq/(α − λ²)), the teacher's λ
  shifted by level repulsion. The outlier merges with the bulk at
  β_bulk = α²(1 − √(α² − 4√q αλ²))/2λ². The expected generalisation error
  is α/2(1 + βα) + λ²/2(1 + βα)² (Eq. 23), smallest where the outlier is
  farthest from the bulk. Numerically (Figure 7; α = 1, λ = 0.2, N = 2048,
  K = 512, 100 draws) the overlaps of the outlier's singular vectors with u
  and v fall from their maximum at perfect learning to chance at the
  merger.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Initialized transformer matrices follow the Marchenko–Pastur law; trained ones depart from it | strong | Figure 1, all three models |
| C2 | Rectangular trained matrices have outliers below the bulk; square ones cannot | strong (the second half is the null's geometry; the first is counted) | Eqs. 4–5, Table 3 |
| C3 | Directions that depart from the null align with the input's principal directions | moderate, and not uniform: holds for above-bulk outliers and for the up and gate projections' lower outliers, fails for Attention-Output, Llama's Down-Projection and the lower end of Key and Value | Figures 2–4, 8–9, 12 |
| C4 | In rectangular matrices the smallest decile is more important to keep than some larger deciles; in square ones importance falls with magnitude | strong for the perplexity and GSM8K ablations | Figure 5, Tables 1 and 5, Figure 11 |
| C5 | The singular values that depart from the null are what matter in that decile | weak | the decile is 10% of the spectrum while lower outliers are 2–6.5%; no ablation of the outliers alone |
| C6 | Fine-tuning writes task information into the small directions | moderate, for one model | Figure 6, BERT, three datasets |
| C7 | Noise suppressed along a learned direction can place that direction below the bulk, with information growing with distance from it | moderate within the model: an exact ensemble, with the outlier location quoted from an unpublished thesis and checked numerically | Section 6, Appendix F, Figure 7 |
| C8 | This is the mechanism in real networks | not supported | the authors say the noise covariance of real weights would need many training runs to estimate |

## Method

Two measurements and a model. The spectrum of each weight matrix is
compared with the Marchenko–Pastur density at an estimated variance; each
right singular vector is projected on the eigenbasis of the activation
covariance at the matrix's input and its largest coefficient recorded. Then
deciles of the spectrum are zeroed across all matrices of a type and the
damage measured by perplexity and benchmark accuracy. The model is a
Gibbs (Gaussian) posterior over the first layer of a two-layer linear
student; the loss and the prior combine into a Gaussian whose mean is the
rule and whose covariance is the prior's isotropic noise with one direction
squeezed.

## Concepts

- **zero-information hypothesis**: the i.i.d. random matrix whose spectrum
  is Marchenko–Pastur; agreement with it is read as "nothing learned here".
- **bulk** and **outlier**: the asymptotic support [ν₋, ν₊], and a singular
  value outside it, at either end.
- **activation covariance matrix**: C = ⟨(h_i − h̄)(h_i − h̄)ᵀ⟩ over tokens i,
  for the activations h entering one matrix (Eq. 6).
- **overlap O_k**: the largest coefficient of the k-th right singular vector
  in that covariance's eigenbasis (Eq. 7). M_k (Appendix C) is the same in
  the standard basis, a localisation measure.
- **decile**: a tenth of the rank-ordered singular values, decile 1 the
  smallest.
- **lazy regime**: training that leaves weights near initialisation, and so
  near the null; offered as the reason Attention-Output shows little overlap
  (Appendix D).

## Connections

The method is the authors' own earlier programme, random-matrix filtering of
weight matrices (Thamm, Staats and Rosenow 2022 and 2023, Phys. Rev. E),
which follows Martin and Mahoney's reading of trained spectra and Papyan's
class structure in deep-learning spectra. The upper outlier is the BBP
transition (Baik, Ben Arous and Péché; Benaych-Georges and Nadakuditi). The
lower outlier of Section 6 is, in my reading, the same transition at the
lower edge for a noise with one reduced covariance direction, the
sample-covariance case of a spike below one; the paper does not name it so.
The empirical target is Eckart and Young's theorem, which the paper cites
for the view that small singular values are the cheapest to lose. The
fine-tuning experiment is aimed at Hsu et al. (weighted low-rank
factorisation) against Sharma et al. (LASER).

## Bearing on the record

- **[LIT-330](../literature.d/LIT-330.md)** (Eckart and Young). The theorem is untouched: the best rank-r
  Frobenius approximation is still the magnitude truncation. What this
  reading adds is that Frobenius distance weights a direction by its singular
  value squared, while the function of a trained rectangular matrix does
  not; Table 1's Down-Projection loses 41 points of GSM8K to the 10% of its
  spectrum that Eckart–Young treats as cheapest. The record's reading of
  Eckart and Young ([NOTE-301](NOTE-301.md)) already says the theorem fixes a truncation of
  one matrix and nothing more; this is a measured case of that limit.
- **[THEORY-078](../theory.d/THEORY-078.md)** (the Fisher's top C eigenvalues stand clear of the bulk and
  a cut at the bulk edge keeps the span of the class means). A different
  matrix, the Fisher rather than a weight, so nothing here changes it. But
  the convention of cutting at the upper bulk edge is one-sided, and this
  paper shows that for a rectangular matrix, information can also sit below
  the lower edge. Whether the Fisher's Gram form has such lower outliers is
  not asked anywhere in the record.
- **[LIT-672](../literature.d/LIT-672.md), [LIT-369](../literature.d/LIT-369.md), [LIT-617](../literature.d/LIT-617.md), [LIT-619](../literature.d/LIT-619.md).** The same line of random-matrix
  readings of trained networks: Martin and Mahoney's statistical mechanics,
  the HTSR tail exponent in the grokking study, and Papyan's bulk-and-outlier
  Hessians. All of them read the upper end; this paper is the record's first
  reading of the lower end.
- **The anthology's reading** ([ANTH-LIT-517](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-517.md), [ANTH-NOTE-263](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/notes.d/NOTE-263.md)). It reads the
  paper for low-rank-plus-quantization practice, and its account matches
  this one on the numbers. One point it states more broadly than the paper
  supports: its key results put the lower-end overlap "in Up/Down/Gate
  projections of Pythia and Llama", while the paper finds none in Llama's
  Down-Projection (the anthology's own limitations note this) and none for
  Llama's rectangular Key and Value (not noted there). Its reading of RULER,
  decile 1 scoring the same as decile 10, is right, and it means Table 2
  cannot rank decile 1 second, as the paper's text does. Neither the
  anthology's reading nor the paper notes the decile-versus-outlier gap
  (C5). Reported per [ADR-013](../decisions.d/ADR-013.md), not fixed from here.
- **The manuscript's argument.** No claim on the pragmatic-transport line is
  about weight spectra. The only echo is with the task-relative view of
  preservation ([CLAIM-088](../claims.d/CLAIM-088.md), [QUESTION-016](../questions.d/QUESTION-016.md)): a reduction optimal under a
  task-blind distortion here discards what the task needed. That is an
  analogy, not evidence for those claims.
- **Practice.** The paper's guidance for SVD pruning is ML practice and
  belongs to the anthology, which holds it.
- No THEORY filed. The measurements are of three models and already read in
  the anthology. The model's lower-outlier result rests on a formula quoted
  from an unpublished thesis, and the general random-matrix fact behind it,
  that a covariance spike below the bulk produces a lower outlier, is older
  than the paper and not established by it.

## Limitations

- **The ablation does not test the outliers.** Lower outliers are 2–6.5% of
  the spectrum; the smallest decile is 10%, so it mixes them with the lower
  bulk. The claim that RMT-violating values matter more than bulk values is
  therefore inferred, not measured; ablating exactly the below-bulk values,
  and an equal number of lower-bulk values, would test it.
- **Overlap and importance come apart.** Llama's Down-Projection has no
  lower-end overlap yet the most damaging smallest decile; Llama's Key and Value have
  hundreds of lower outliers (Table 3) and no lower-end overlap.
  Attention-Output has no overlap anywhere; Appendix D reads its averaged
  spectrum as having far fewer outliers than Query, yet Table 3 still counts
  hundreds per layer (723 in Llama's layer 0). The paper offers GLU placement,
  localisation (M_k) and lazy training as speculations.
- **Single runs.** The perplexity and benchmark ablations report no
  repetitions; RULER is visibly non-monotone (on the needle tasks decile 6
  scores about 99 while deciles 4 and 7 score 0–13). Only the BERT fine-tuning has a 3σ
  band.
- **Removed norm is not controlled.** A higher decile removes more Frobenius
  norm than a lower one; damage per unit of removed norm is not reported,
  though it would make the paper's case stronger, not weaker.
- **The model is linear, two-layer, rank-one, Gaussian, with a fixed second
  layer.** It shows a lower outlier can arise and carry information; the
  authors say themselves that showing it does so in an LLM needs the noise
  covariance of real weights, which needs many training runs.
- **Three models**, differing in size, data and architecture; Appendix H
  declines to read a scaling trend from them.

## Open questions

- Ablate the below-bulk outliers alone, against an equal number of values
  from the lower bulk, with seeds: does the importance follow the departure
  from the null, or just the smallest decile?
- Does the information measured by overlap with the teacher in the model
  correspond to anything measurable in a real matrix, for example the
  overlap gap between below-bulk and lower-bulk vectors?
- Why do Key and Value (rectangular under grouped-query attention, by my
  reading of Llama's shapes) have lower outliers without overlap? Is the
  lower edge populated there by finite-size effects rather than learning?
- Do Gram-type matrices in the record, the Fisher of [THEORY-078](../theory.d/THEORY-078.md) among them,
  have structure below their lower bulk edge when they are rectangular in
  the relevant sense?
