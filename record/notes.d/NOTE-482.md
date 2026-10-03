---
number: 482
status: Read
formerly:
- NOTE-tmpsl3ae
paper: 'LIT-611'
title: 'Gemma Scope: Open Sparse Autoencoders Everywhere All At Once on Gemma 2'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read in full from arXiv 2408.05147v2 (26 pages) through PyMuPDF text
    extraction: Sections 1–5 and Appendices A (inference
    reparameterisation), B (transcoders) and C (further evaluations).
    Figures were read from captions and text; plotted values were not
    recovered, so no number below comes from a plot unless the text states
    it. The JumpReLU training method and the interpretability ratings are
    from Rajamanoharan et al. (2024b) and are taken as this report
    summarises them.
date: '2026-10-03'
summary: >-
  JumpReLU SAE: f(x) = z ⊙ H(z − θ), z = W_enc x + b_enc, x̂ = W_dec f + b_dec,
  loss ‖x − x̂‖² + λ‖f(x)‖₀, with θ trained by straight-through estimators
  (bandwidth ε = 0.001). Released on all layers and sublayers of Gemma 2
  2B and 9B and three layers of 27B, at widths 2¹⁴–2²⁰. Evaluated by delta
  LM loss and FVU against L0. Residual SAEs cost the most loss; base-model
  SAEs transfer to the IT model; wider SAEs split latents. No agreed SAE
  quality metric exists.
---

# NOTE-482: Gemma Scope: Open Sparse Autoencoders Everywhere All At Once on Gemma 2

## Contribution

An open, comprehensive suite of sparse autoencoders on a modern open-weight
language model: every layer and sublayer of Gemma 2 2B and 9B, plus
selected layers of 27B and of the instruction-tuned 9B, each at several
sparsities. With it come the training recipe, the infrastructure needed to
train at this scale, and standard evaluations. Before it, comprehensive SAE
suites existed only for small or proprietary models. The research
contribution is the release; the method is Rajamanoharan et al.'s
JumpReLU.

## Key insight

A JumpReLU SAE separates two decisions that a ReLU-plus-L1 SAE couples:
whether a latent is active, decided by a learned per-latent threshold θ_i,
and how strongly, given by the pre-activation itself. The objective then
charges a flat price λ for every active latent, regardless of its
magnitude. An SAE is therefore a dictionary with a hard, learned inclusion
rule and a counting penalty. How to choose that price, and the dictionary's
size, is left to Pareto curves.

## Assumptions

- **The linear-features premise** (§1): a significant fraction of LM
  activations are sparse linear combinations of meaningful directions,
  citing Elhage et al. 2022 and others. The SAE is built on it, not a test
  of it.
- **Training data** from the Gemma 1 pretraining distribution, excluding
  BOS, EOS and padding tokens, shuffled in buckets of about 10⁶ activations
  (§3.1). Activations are normalised by a fixed scalar to unit mean squared
  norm.
- **Sites** (Fig. 1): attention head outputs before W_O (concatenated across
  heads), MLP outputs after RMSNorm, and the post-MLP residual stream.
- **Hyperparameters** (§3.2): ε = 0.001, learning rate 7 × 10⁻⁵ with cosine
  warmup over 1,000 steps, Adam with (β₁, β₂) = (0, 0.999), batch 4,096, λ
  warmed up linearly over 10,000 steps, decoder columns renormalised to unit
  norm, θ initialised at 0.001, W_enc initialised as W_decᵀ but untied.
- **Token budgets** (§3.1): 4B tokens for 16.4K-width SAEs, 16B for
  1M-width, 8B otherwise.

## Key results

- **Architecture (§2, Eqs. 1–4).** As in the summary. The JumpReLU is z ⊙
  H(z − θ), H the Heaviside step. Large ε gives biased, low-variance
  threshold gradients and sparse but less faithful SAEs; small ε gives
  high-variance gradients and thresholds that fail to train (footnote 5).
- **Scale (§1, Table 1).** More than 400 SAEs in the main release, more
  than 2,000 counting sparsity variants, more than 30 million latents,
  over 20% of GPT-3's training compute, about 20 PiB of activations.
  Storing activations for 10–100 days was at least an order of magnitude
  cheaper than regenerating them once (§3.3.2).
- **Sparsity–fidelity (§4.1, Fig. 2, Appendix C.1).** Delta LM loss is
  consistently higher for residual-stream SAEs than for MLP and attention
  SAEs, while FVU is roughly comparable across sites. The authors' account:
  each sublayer is a small part of the residual stream, so its errors matter
  less downstream.
- **Position (§4.2, Fig. 3).** Reconstruction loss rises from near zero over
  the first few tokens. For attention and residual SAEs it keeps rising
  (attention's flattens after about 100 tokens); for MLP SAEs it peaks
  near the tenth token and then declines slightly.
- **Width (§4.3, Figs. 4–5).** Wider SAEs reconstruct better at fixed L0.
  Their firing-frequency mode shifts lower, but a cluster of ultra-high-frequency
  latents persists, as in TopK and unlike Gated SAEs. Feature splitting
  suggests wide SAEs may spend capacity on compositions of existing features
  rather than new ones.
- **Interpretability (§4.4, Figs. 6–7, reproduced).** Human raters and
  LM-simulated activations find little difference between JumpReLU, TopK
  and Gated SAEs at width 131K on Gemma 2 9B.
- **Base to IT transfer (§4.5, Fig. 8, Appendix C.4).** SAEs trained on the
  base model raise loss on IT rollouts almost as little as SAEs trained on
  the IT model. FVU shows a larger gap. The authors' hypothesis is that
  fine-tuning re-weights old features and adds chat features that matter
  little for next-token loss. Splicing base SAEs into the IT model can even
  lower loss on user prompts, which post-training does not train the model
  to predict.
- **Data subsets (§4.6, Fig. 9).** Best on DeepMind mathematics, worst on
  Europarl, which the authors attribute to mostly English training data.
- **Precision (§4.7, Fig. 10).** bfloat16 inference has negligible impact.
- **Transcoders (Appendix B, Fig. 11).** Worse than MLP-output SAEs at fixed
  L0 on Gemma 2 2B, reversing the GPT-2 Small finding of Dunefsky et al.
  Four possible causes are listed, including implementation error.
- **Uniformity of active latent importance (Appendix C.3, Eqs. 12–14).**
  With attribution-weighted activations y = f(x) ⊙ W_decᵀ∇_x L normalised to
  a distribution p, r_L0 = e^(S(p))/‖y‖₀ is the effective number of active
  latents over the actual number. It falls as more latents are active,
  most for residual SAEs.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | JumpReLU SAEs with a direct L0 penalty and STE-trained thresholds train stably across all layers and sites of Gemma 2 with one shared bandwidth and learning rate | strong (demonstrated at scale) | §3, Appendix C.1 |
| C2 | Residual-stream SAEs cost more LM loss than sublayer SAEs at comparable FVU | moderate: consistent across layers, explanation conjectural | Fig. 2, Fig. 13 |
| C3 | SAEs trained on a base model transfer to its instruction-tuned version | moderate by delta loss; weaker by FVU | §4.5, Figs. 8, 19–22 |
| C4 | JumpReLU, TopK and Gated SAEs are about equally interpretable | moderate: reproduced from another paper, one width, one model | Figs. 6–7 |
| C5 | There is no consensus metric for SAE quality | a statement about the field, with citations | §4 |

## Concepts

- **latent**: an SAE dictionary direction d_i (a column of W_dec), as
  opposed to the conceptual "feature" it may or may not capture. The paper
  uses this distinction on purpose (footnote 4).
- **JumpReLU**: z ⊙ H(z − θ), a ReLU with a learned per-latent jump.
- **L0**: the mean number of active latents per token; the sparsity axis.
- **delta LM loss**: the increase in the LM's cross-entropy when the SAE's
  reconstruction is spliced into the forward pass.
- **FVU**: reconstruction error divided by the error of predicting the mean.
- **feature splitting**: a latent in a narrow SAE becoming several more
  specific latents in a wider one.
- **transcoder**: a sparse replacement for an MLP, trained to map the MLP's
  input to its output rather than to reconstruct its input.

## Connections

- **Elhage et al., *Toy Models of Superposition* ([LIT-323](../literature.d/LIT-323.md)).** The premise
  SAEs act on: more features than dimensions, recoverable when sparse.
- **Engels et al. ([LIT-322](../literature.d/LIT-322.md)).** Multi-dimensional circular features found by
  clustering SAE latents. The report names capturing them efficiently, and
  the "dark matter" of truly non-linear features, as open problems (§5).
- **Nanda et al. ([LIT-345](../literature.d/LIT-345.md)).** Lieberum is a co-author. A network
  interpreted in a basis known in advance, Fourier modes. SAEs are the
  attempt to find such a basis without knowing it.
- **Anthology.** Kantamneni et al. ([ANTH-LIT-568](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-568.md)) use Gemma Scope SAEs and
  find them of little use for probing. Gao et al. ([ANTH-LIT-571](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-571.md)) is the TopK
  baseline. Chen et al. ([ANTH-LIT-544](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-544.md)) connect superposition to Bayesian
  phase transitions in singular learning theory.

## Bearing on the record

The owner filed this beside Fisher-spectrum block structure and
evidence-based model comparison, which are being filed in parallel, and
the phrase "the object being thresholded". What follows is my reading; the
paper does not frame SAEs this way.

- **A threshold on features, not on a spectrum.** The spectral papers in
  this batch threshold eigenvalues of a fixed operator, an orthogonal basis
  ordered by size. A JumpReLU SAE thresholds coefficients in a learned,
  overcomplete, non-orthogonal dictionary, per input. Both cut a
  representation down to the components that pay for themselves. The
  difference is that an eigenbasis has a canonical order and the SAE
  dictionary does not, which is one reason feature splitting has no analogue
  in the spectral case.
- **λ‖f‖₀ is a per-component price.** The objective charges every active
  latent the same λ. That is the form of an information criterion that
  charges a fixed cost per parameter, such as AIC or BIC, applied per token.
  The report sets λ by sweeping and reading Pareto curves (§4.1), and offers
  no criterion for the width M. Choosing the width and λ is a model
  comparison problem, and the evidence-based methods the owner is
  collecting (Savage–Dickey ratios, Bayesian model reduction, singular free
  energy) are candidates for it. The report's open problem of "how much"
  narrow SAEs miss (§5) is the same question.
- **r_L0 is an effective-dimension measure.** e^(S(p)) in Appendix C.3 is
  the exponential of an entropy, the same construction as participation
  ratios and effective ranks of spectra. It is applied here to attribution
  mass over active latents rather than to eigenvalues.
- **No THEORY is filed.** A candidate is in the report to the owner.
- **ML practice.** The engineering advice (sharding, storage, precision) is
  practice and would belong to the anthology if anyone wanted it there.

## Limitations

- **No ground truth.** The SAEs are evaluated by reconstruction and loss,
  not against known features; the authors say there is no consensus on
  what makes an SAE good (§4).
- **Interpretability evidence is borrowed** from Rajamanoharan et al.
  (2024b), on one model and one width.
- **The transcoder result is unexplained**, and one listed cause is
  implementation error.
- **Data are from one distribution**, the Gemma 1 pretraining mix; the Pile
  results show weaker performance off it, notably on multilingual text.
- **Shuffling was imperfect** (buckets of about 10⁶), and its effect was
  not checked (§3.1).

## Open questions

The report's own list (§5) is long. Those nearest this record:

- Do SAEs find the "true" concepts in a model, and do they learn spurious
  compositions of independent features to improve sparsity?
- How should SAEs capture multi-dimensional features such as Engels et
  al.'s circles, and what is the "dark matter" of non-linear features?
- Can feature splitting be understood, and can one measure how much a
  narrow SAE misses?

## Corrections

- none to a seeded skim (there was no seed)
- **Caption slip in the source.** Fig. 18 (Gemma 2 9B) says "Note Gemma 2
  2B has 42 layers"; it is the 9B model that has 42 layers, as Table 1
  gives. Table 1 also labels the small model "2.6B PT", where the text
  calls it Gemma 2 2B.
