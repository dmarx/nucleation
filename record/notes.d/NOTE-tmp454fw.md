---
status: Read
paper: LIT-2967
title: 'Xu — The smallest singular directions of the unembedding matter disproportionately for next-token prediction'
version: 1
history:
- version: 1
  date: '2026-11-21'
  note: >-
    From the arXiv PDF of 2605.17084v2 (stamped 3 Nov 2026, "Preprint.
    November 4, 2026"), 23 pp., fetched 2026-11-21 from arxiv.org without
    obstacle and converted with pdftotext. Read in full: main text
    pp. 1–10 and Appendices A–G; the references skimmed; figures read from
    captions and prose, so every number here is from the prose. v1
    (2026-05-16) not read and not compared. Read by a reader subagent;
    filed by a second one, which rechecked every quote used here against
    the arXiv HTML rendering of v2 (the PDF's two-column text breaks
    phrases). No email address sent.
date: '2026-11-21'
summary: >-
  At a language model's final hidden state, the directions the centred,
  norm-folded unembedding amplifies least (its bottom 5% of singular
  directions) move the logits less than equal-length random changes but
  change the next-token distribution and the loss several times more, in
  ten trained models. Per unit of logit distance the prediction change is
  near random over most of the spectrum and peaks at the bottom band,
  because the leading candidates' contrast lies there. In total, removing
  the top band costs as much loss or more in nine of the ten.
---
<!-- inactive-ok-file: THEORY-tmpu3iio CLAIM-835 ARG-139 THEORY-286 LIT-tmpuh2lr LIT-tmp9yy1o LIT-tmpgptvp — Proposed or new; the account this reading files, the entries it bears on, and works registered from it, Deferred -->

# NOTE-tmp454fw: Xu — The smallest singular directions of the unembedding matter disproportionately for next-token prediction

## Contribution

An equal-length test, with prespecified comparisons and bootstrap
intervals, that the logit metric G = WᵀW and the predictive Fisher metric
pulled back to the final hidden state, F̄ = E_x[WᵀΣ_pW] with
Σ_p = diag p − ppᵀ, disagree most along the unembedding's smallest singular
directions, in ten trained models, with the disagreement traced to the
contrast between the two leading candidate tokens.

## Key insight

For a single singular direction "the singular value drops out of the
ratio" of prediction change to logit distance (§2.3, Eq. 8): F/D =
½Var_p(a_i). A direction can be amplified little and still decide between
the tokens that are actually in contention.

## Assumptions

- The site is the final hidden state u after the final norm, with the norm
  weight folded into the unembedding, the vocabulary centred and the
  LayerNorm mean direction removed: W = C_V W_out diag(γ) R (Eq. 1). The
  bands are 20 equal slices of W's right singular directions.
- The intervention is on the state, not the weights: "We change the final
  hidden state within one band b by replacing its component in that band
  with the calibration mean" (§2.3), against 8 random subspaces of equal
  rank rescaled to equal length ‖δu‖²; the norm's scale is held fixed
  (natural path as a check).
- "Small" is in the logit metric, "the Aitchison metric" pulled back
  (App. B), with every token pair weighted equally. The Euclidean inner
  product on u fixes both the singular directions and "equal length"; raw
  and uncentred bases are checked, arbitrary invertible maps are not.
- Ten base models (Pythia 70M–6.9B final checkpoints, Llama-3.1-8B,
  Qwen3-1.7B-Base, Qwen3-8B-Base), two post-trained ones; 1,536 OpenWebText
  documents of 128 tokens, also code and earlier positions; float32.
- The null: "changes of equal length need not produce states that occur
  naturally" (Limitations).

## Key results

- **Equal length** (§3.1): the bottom band's changes "move the logits less
  than their references ... Nevertheless, in every model, their prediction
  change and their loss change are several times as large". Prose values:
  Qwen3-8B and Qwen3-1.7B K ratios 3.5 and 4.1 (App. E.1). Per document,
  the bottom band exceeds its references per unit logit distance in 83–93%
  of documents, in total prediction change in only 47–68% (§3.1); the
  median per-document loss excess is −0.13 to 0.02 nats (App. E.2).
- **The consequence spectrum** (§3.2): "Across most of the spectrum, the
  prediction change per unit of logit distance stays within about a factor
  of two of that of random changes"; the excess appears over the last few
  bands, largest at the bottom band in every model.
- **U-shaped, not a reversal** (App. D, Fig. 5): per unit of squared
  length the logit distance falls along the spectrum, "whereas the Fisher
  term per unit ... is lowest over the middle bands and rises above random
  at both ends"; their quotient rises to the bottom band.
- **The top band in total** (App. E.2): "Removing the top band's component
  increases the loss as much as removing the bottom band's, or more, in
  nine of the ten models, by 0.96 to 1.75 nats against 0.17 to 1.23 nats".
- **Loud in variance** (App. D): at late residual states, "the bottom band
  holds on average 1.5 to 6.6 times its share of the directions in
  variance and the top band 1.3 to 3.4 times".
- **Mechanism** (§4.1): the leading pair's contrast share and the
  consequence spectrum's logarithms "correlate at 0.95 to 0.98 across the
  ten models"; pair-versus-rest and within-pair parts account for 85–99%
  of the excess (§4.2).
- **Truncation** (§5.1): "truncating the unembedding by singular value
  changes the logits less than random truncation but increases the loss
  more"; whitened and consequence-ranked truncation do better, so "The
  cost therefore lies in ranking by the singular values alone, not in
  truncation as such".
- **Training origin, untested** (§7): from Thrampoulidis (2024) and Zhao
  et al. (2024), the part of the output weights that sets odds among
  plausible tokens stays finite while exclusion grows; "If this separation
  maps onto the singular directions, it places the distinctions among
  plausible candidates at the bottom of the spectrum". "Testing this
  origin would require tracking the organization during training".
- **Robust** (App. E.1) to reference scaling, donor replacement, the
  natural path, raw and uncentred bases, with one exception (Pythia-70M in
  the raw basis, K ratio 0.71).

## Concepts

- **Logit distance D = ‖δℓ‖²**, **prediction change K = KL(p‖p′)**,
  **Fisher term F = ½Var_p(δℓ)**.
- **Consequence spectrum C_b**: F/D by band, relative to random.
- **ρ(v) = vᵀF̄v / vᵀGv** (App. B), "the per-direction form of the
  consequence spectrum", a quotient of two metrics whose generalized
  eigenvectors are invariant under invertible maps of u, as the singular
  ranking is not.
- **Contrast share**; **consequence-ranked truncation**.

## Connections

D is, up to the vocabulary size, the squared length under Park, Choe and
Veitch's causal inner product (App. B; LIT-304), the stipulated inner
product of THEORY-018. Xu cites Staats et al. (THEORY-420) for the same
divergence inside the network, and Cancedda (2024; LIT-tmpuh2lr) as the
closest prior observation. Thrampoulidis (2024; LIT-tmp9yy1o) and Zhao et
al. (2024; LIT-tmpgptvp) supply §7's training origin, parallel to the
record's THEORY-738 and THEORY-286. All three are registered from this
reading. The same spectrum, up to scale and ridge, is the one Concepts
Whisper measures in (NOTE-tmpwvltp).

## Bearing on the record

Filed as THEORY-tmpu3iio. Dated notes of 2026-11-21 on each entry below.

- **CLAIM-835**: supports the thesis that the metrics disagree, in
  trained models: "the two geometries disagree most along the directions
  that the unembedding amplifies least" (§7). Corrects the claim's
  attribution of a systematic reversal: the peak at the bottom band is in
  the ratio F/D; F per unit length is U-shaped; the top band costs as much
  total loss in nine of ten models (corrected there; ARG-139).
- **ARG-139**: supports its premise. Xu's metric is the state-space
  pullback, not a parameter Fisher; it bears on no hyperribbon.
- **QUESTION-511**: leaves open, and bears against one candidate answer.
  Final checkpoints only. The bottom band is quiet in the logit metric and
  loud in representation variance, so A41's "spectrally quiet subspace"
  does not describe it. §7's origin is testable on Pythia's checkpoints,
  which the paper did not use.
- **THEORY-018**: qualifies the reading. The singular ranking and "equal
  length" depend on the Euclidean inner product on u, which softmax
  training does not fix; the quotient ρ does not.
- **THEORY-420**: parallel and contrast. A state component at the output
  removed, not weight singular values inside blocks; the bottom singular
  values "decline smoothly", with no gap below a bulk.
- **THEORY-738, THEORY-286**: parallel to §7's origin (no edge).

Nothing here is filed as an instruction for machine-learning practice.

## Limitations

- One site, at most 8B parameters, at most 128 tokens, no chat formatting;
  equal-length changes may be off-distribution; truncation without
  retraining (author-stated, p. 10).
- The main comparison's sizes are mostly in figures; the effect is
  heavy-tailed per document, with median loss excess near zero.
- "Smallest" is relative to a Euclidean metric fixed by the architecture's
  normalization. The paper names the invariant generalized eigenproblem
  of (F̄, G) and ranks by singular value anyway.
- Single author; AI assistance acknowledged for code and revision.
