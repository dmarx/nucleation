---
status: Read
paper: 'LIT-1414'
title: 'Wang, Gao, Zhao, Sun and Dai — Auxiliary-loss-free load balancing for mixture-of-experts'
version: 1
history:
- version: 1
  date: '2026-10-29'
  note: >-
    Read in full on 2026-10-29 from arXiv
    (https://arxiv.org/pdf/2408.15664, v1 of 28 August 2024, the only
    version, 14 pages), text extracted with pdftotext. Read: §§1–6,
    Algorithm 1, Tables 1–6 and Appendices A–D with the leakage bound of
    D.1. Figures were read from captions and text only; no number was
    taken from a chart. Checked: the leakage figure of §5.2 (K·log₂((1 −
    R)/R) per layer with K = 2, N = 16, nine layers gives 50.5 bits);
    the token counts of Appendix B (56,514 steps × 1,728 × 2,048 ≈ 200B
    tokens; 40,000 × 1,152 × 2,048 ≈ 94B, reported as 100B) and the
    validation-set size (≈ 71M tokens both ways). The derivation of the
    leakage bound in D.1 was garbled in extraction and was not checked
    line by line.
date: '2026-10-29'
summary: >-
  Adds a per-expert bias b_i to the routing scores used only for top-K
  selection, not for the gate weights, and after each batch moves b_i by
  u·sign(mean load − load_i), so overloaded experts are selected less.
  On DeepSeekMoE-style models of 1B and 3B parameters trained on 100B
  and 200B tokens it gives slightly lower validation perplexity (9.50 vs
  9.56; 7.92 vs 7.97) and much lower global load violation (0.04 vs 0.72
  and 0.52) than an auxiliary loss with α = 0.001, one run each. Expert
  Choice routing is excluded because it leaks future tokens.
---

# NOTE-tmppnncw: Wang, Gao, Zhao, Sun and Dai — Auxiliary-loss-free load balancing for mixture-of-experts

## Contribution

It removes the load-balancing term from the training objective of a
mixture-of-experts model and balances load instead with a controller
outside the gradient: a bias per expert that shifts which experts win
the top-K selection, updated from the load each expert carried on the
previous batch. The comparison shows better balance and no loss of
perplexity against the usual auxiliary loss, and an argument with a
small experiment that Expert Choice routing, the other loss-free option,
leaks information about future tokens.

## Key insight

Balance is a constraint on selection, not on the model's function, so
it can be enforced on the selection alone. The bias changes which experts
a token is sent to but not how their outputs are weighted, and it is
updated by counting, not by backpropagation, so the language-modelling
gradient is left untouched. It is an integral controller on load.

## Assumptions

- DeepSeekMoE architecture (fine-grained routed experts plus shared
  experts; Table 5 not fully extracted), sigmoid gating in the main
  experiments; softmax in Appendix C.
- Causal language modelling on a DeepSeek-AI multilingual corpus, BPE
  vocabulary 32K.
- The bias uses only the previous batch's loads, which preserves the
  causal constraint.
- Hyperparameters tuned at 1B and transferred to 3B.

## Key results

- **Table 2.** 1B: perplexity 9.50 vs 9.56, MaxVio_global 0.04 vs 0.72.
  3B: 7.92 vs 7.97, 0.04 vs 0.52. Loss-free vs auxiliary loss with
  α = 0.001, chosen from Fig. 2's sweep (α ∈ {10⁻², 10⁻³, 10⁻⁴, 0}).
- **Update rate (Fig. 4).** u = 0.001 best; 10⁻⁴ balances poorly early,
  10⁻² fluctuates late; perplexities 9.50–9.51 across the three.
- **Variants (Tables 3–4).** Proportional update b_i += u·e_i balances
  slightly better (MaxVio 0.028–0.040) with no perplexity gain;
  multiplicative biases are slightly worse (9.52–9.54).
- **Softmax gate (App. C).** Loss-free 9.599 vs 9.604, MaxVio 0.027 vs
  0.937, using the proportional update.
- **Expert parallelism (Fig. 5).** Balance per computation batch improves
  with batch size under loss-free balancing and plateaus under the
  auxiliary loss.
- **Expert Choice leakage (§5.2, App. D).** A bound of more than
  K·log₂((1 − R)/R) bits per token per layer; with chunk size 512 an
  "abnormal loss drop" of about 10%, removed by shuffling tokens across
  chunks.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Bias-based selection control balances load far better than an α = 0.001 auxiliary loss | moderate | Table 2, two sizes, one run each |
| C2 | It does so without loss of perplexity, and slightly improves it | weak | differences of 0.05–0.06 perplexity, no seeds or intervals |
| C3 | The auxiliary loss's gradients are what impair performance | weak | inferred from Fig. 2's trade-off; not isolated |
| C4 | Expert Choice leaks future-token information in causal LMs | moderate | counting bound App. D.1 and the chunk-size experiment |

## Method

Algorithm 1: initialize b_i = 0; for each batch, route with
top-K over s_i,t + b_i, weight outputs by the unbiased s_i,t, count
tokens c_i per expert, and set b_i ← b_i + u·sign(c̄ − c_i), raising the
bias of under-loaded experts as the text describes (the overbar in
Algorithm 1's e_i was lost in extraction, so which term carries it was
not read from the algorithm itself). MaxVio = max_i(Load_i −
mean)/mean.

## Concepts

- **Routing collapse**: the router settling on a few experts, which then
  get all the training.
- **Interference gradients**: the auxiliary loss's gradients, which the
  authors hold conflict with the language-modelling objective.
- **MaxVio_global / MaxVio_batch**: the largest relative overload of an
  expert, over the validation set or within a training batch.
- **Future token leakage**: information about later tokens carried by
  routing decisions that depend on the whole chunk.

## Connections

Its baseline is the auxiliary loss of Switch Transformers ([LIT-1412](../literature.d/LIT-1412.md)) and
GShard; its exclusion of Expert Choice (Zhou et al. 2022) is argued here,
not borrowed. Routing collapse is from Shazeer et al. ([LIT-1507](../literature.d/LIT-1507.md)). The
same group's DeepSeekMoE supplies the architecture.

## Bearing on the record

- **[CASE-117](../cases.d/CASE-117.md).** The LIT records that the exchange cited this as "a
  contribution-based control of influence, one of the regimes [CASE-117](../cases.d/CASE-117.md)
  compares". The reading does not support "contribution-based". The bias
  responds to load, the count of tokens an expert was selected for, and
  to nothing about how much the expert's output helped; it lowers the
  access of busy experts and raises that of idle ones regardless of
  quality. In [CASE-117](../cases.d/CASE-117.md)'s terms it is a usage-based quota on access, a
  regime of imposed balance that, unlike an auxiliary loss, does not
  enter the gradient. It does have the property the case cares about,
  that an excluded expert is brought back: an expert receiving few tokens
  has its bias raised until it is selected. The paper does not measure
  whether experts specialize.

The paper is machine-learning practice and belongs to the anthology; it
carries the anthology-candidate flag.

## Limitations

- One run per configuration, no variance; perplexity differences are
  small. Only one auxiliary-loss coefficient is compared in Table 2.
- One architecture family and corpus, both the authors' own.
- **Errors and slips.** (i) The conclusion says the 3B model was trained
  on 300B tokens; the abstract, §1, §4.1 and Appendix B say 200B, and
  B's step count gives 200B. (ii) Algorithm 1 numbers two steps 4.
  (iii) "Addative", "casual language
  models". (iv) Footnote 2 equates 2048 tokens with "a sentence", i.e.
  one training sequence.

## Open questions

- Does removing the auxiliary gradient change what experts specialize in,
  or only how evenly they are used?
- Is the sign update stable in general, or does u need retuning with
  scale? The 3B run inherits the 1B setting without a sweep.
