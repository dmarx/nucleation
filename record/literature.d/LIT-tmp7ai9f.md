---
status: Active
status_note: 'read 2026-10-03 ([NOTE-tmpqfhaa](../notes.d/NOTE-tmpqfhaa.md)); worth reading as a layer-wise information profile of fine-tuned language models: a matrix-based Rényi estimate of I(Zℓ; Y), between the last-token hidden state at layer ℓ and the input embedding of the true next token, rises through the early layers, peaks in the upper-middle layers and falls in the last few, the "generalization ridge". On a synthetic arithmetic task with GPT-2 Small the peak (0.27 at layer 10 of 12) is where OOD early-exit accuracy is best (56.9%) while ID accuracy keeps rising to 93.2% at layer 12. Learned residual scales put less weight on the final layers when fitted on OOD data. The estimator is a kernel-alignment quantity, not Shannon mutual information: at layer 12 it falls to 0.019, near its layer-6 value, where the same layer decodes the target with 93% ID accuracy.'
title: 'The Generalization Ridge: Information Flow in Natural Language Generation'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read from arXiv v6 (21 August 2026, 22 pages; v1 7 July 2025), which
    carries the header "Published as a conference paper at COLM 2026". The
    reading is of v6; earlier versions may differ. Main text read in full;
    Appendices A–E read for the estimator, datasets, residual scaling and
    the confidence intervals. Not held in the Anthology of the SOTA: a grep
    of its record for "2507.05387", "Generalization Ridge" and "InfoRidge"
    found nothing.
tags:
- representation-learning
- learning-theory
- anthology-candidate
date: '2026-10-03'
published: '2025-07-07'
arxiv: '2507.05387'
first_author: 'Chang'
keywords:
- 'generalization ridge'
- 'InfoRidge'
- 'predictive information'
- 'incremental information gain'
- 'matrix-based mutual information'
- 'Rényi entropy'
- 'residual scaling'
- 'intermediate layers'
- 'memorization'
- 'natural language generation'
extends:
- LIT-tmpt61ew
implementations: []
summary: >-
  Chang, Deng & Chen (2025), COLM 2026. InfoRidge estimates, layer by layer
  and through fine-tuning, the matrix-based mutual information between a
  transformer's last-token hidden state and the embedding of the target
  token, and between each block's residual update and that target. In GPT-2
  Small and Medium, Qwen-2.5 0.5B and Llama 3.1 8B on CLUTRR, ECQA and a
  synthetic arithmetic task, it rises, peaks in the upper-middle layers and
  falls. On the synthetic task the peak coincides with the best OOD
  early-exit accuracy while ID accuracy keeps rising. Middle blocks add the
  most information, attention to task tokens peaks there, and residual
  scales fitted on OOD data downweight the last layers. The profile
  persists over 50 decoding steps on CNN/DailyMail.
---

<!-- inactive-ok-file: THEORY-035 — Rejected; named as the record's verdict on the compression account of generalization, which this paper's vocabulary echoes -->

# LIT-tmp7ai9f: The Generalization Ridge: Information Flow in Natural Language Generation

Ruidi Chang, Chunyuan Deng and Hanjie Chen (2025), *COLM 2026* — [ARXIV-2507.05387](https://arxiv.org/abs/2507.05387)

## Key takeaways

- **A non-monotonic information profile across depth.** The estimated
  predictive information I(Zℓ; Y) accrues slowly in early layers, peaks in
  the mid-to-upper layers, then falls in the last few (Section 4.1, Figure
  2). For GPT-2 Small on the synthetic task it reaches 0.2721 at layer 10
  and drops to 0.0188 at layer 12 (Table 1).
- **The peak is where OOD early-exit accuracy is best.** In Table 1, OOD
  accuracy is 56.90% at layer 10 and falls to 52.67% and 50.00% at layers
  11 and 12, while ID accuracy climbs to 79.17% and 93.17%. The authors read
  the final layers as memorizing.
- **Middle blocks add the most.** The incremental gain I(ΔZℓ; Y) of each
  residual update is largest in the middle and small or negative at the end
  (Section 4.2, Figure 3).
- **Two supporting probes.** Attention to "signal" tokens peaks in mid-to-
  late layers and falls in the last (Qwen-2.5 0.5B on ECQA: 0.2307 at layer
  17, 0.0104 at the final layer; Table 2). Scalars βℓ on each residual
  block, fitted with all weights frozen, put relatively less weight on the
  last layers when fitted on OOD data than on ID data (Figure 4).
- **It persists in generation.** Over 50 decoding steps on CNN/DailyMail,
  the profile's level rises with the step but its shape, peaking early to
  mid and declining late, stays the same (Section 5).

## Standing in the record

Filed on 2026-10-03 with the owner's batch ([ADR-027](../decisions.d/ADR-027.md)), among its papers on
where in a network generalization lives.

**It extends Uselis and Oh ([LIT-tmpt61ew](LIT-tmpt61ew.md)).** That paper found, for image
classifiers under distribution shift, that intermediate layers support
better OOD probes than the penultimate one. This paper cites it three times
for that finding, and asks how the effect emerges during training and
whether it holds for transformers generating text. It answers with an
information profile, early-exit accuracy and residual scaling. Its
"generalization ridge" is the language-model counterpart of Uselis and Oh's
best intermediate layer.

**Against the record's information-bottleneck verdict.** The vocabulary
here, a "compression" of representations in the final layers traded
against generalization, is the information-bottleneck vocabulary of
Shwartz-Ziv and Tishby ([LIT-324](LIT-324.md), [ANTH-LIT-508](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-508.md)), which the paper cites. The
record rejects the compression account of generalization ([THEORY-035](../theory.d/THEORY-035.md)), on
Saxe et al.'s evidence ([LIT-372](LIT-372.md)). This paper's claim is different. It is
about information with the target, not with the input, and across depth,
not across training time. But it shares the measurement problem Saxe et
al. exposed: the conclusion rests on what the estimator measures. The
estimator is a Gaussian-kernel, matrix-based Rényi quantity with bandwidth
1 on ℓ2-normalized vectors, and the paper's own Table 1 shows it parting
from decodable information. At GPT-2 Small's last layer the estimate is
0.0188, close to its layer-6 value, while that layer's early exit predicts
the target with 93.17% in-distribution accuracy. Shannon information about
the target cannot be near zero where the target is decoded that well, so
the "decline" is a fall in kernel alignment between the hidden states and
the target embeddings, not a loss of information. The paper does not raise
this. The point is mine, and the NOTE gives it.

**Against the anthology.** The depth profile sits beside the anthology's
measurement that middle transformer layers tolerate deletion and
reordering while the first and last do not ([ANTH-THEORY-020](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/theory.d/THEORY-020.md)), and its
logit-lens holding ([ANTH-LIT-570](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-570.md)). The early-exit accuracies here are a
probe of the same kind. It carries an implied practice (exit or read out at
the ridge layer under shift), so `anthology-candidate`.
