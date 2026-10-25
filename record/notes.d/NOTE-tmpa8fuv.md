---
status: Read
paper: 'LIT-tmp95a3g'
title: 'Shazeer et al. — Outrageously large neural networks: the sparsely-gated mixture-of-experts layer'
version: 1
history:
- version: 1
  date: '2026-10-24'
  note: >-
    Read in full on 2026-10-24 from arXiv:1701.06538v1 (23 January 2017),
    the only arXiv version, 19 pp., extracted by pdftotext: sections 1–6
    (pp. 1–9) and appendices A–G (pp. 13–19), with every table. Figures
    were read from their captions and the surrounding text. The reference
    list was skimmed. The ICLR 2017 camera-ready was not reached. Page
    numbers below are v1's. Every quotation was checked against the
    extracted text by script.
date: '2026-10-24'
summary: >-
  An engineering paper with large experiments. A sparsely-gated layer of
  up to 131,072 experts raises capacity over 1000-fold at roughly constant
  computation. Read here for one observation and one fix: without
  constraint the gate concentrates on a few experts, which the authors call
  self-reinforcing, and two auxiliary losses that penalize unequal
  importance and load remove it, which in one ablation also improves
  perplexity from 39.8 to 35.6.
---
<!-- inactive-ok-file: THEORY-tmp2p13l — Proposed; filed from this reading, named -->
<!-- inactive-ok-file: CLAIM-277 CLAIM-443 CLAIM-362 QUESTION-132 QUESTION-134 — Proposed, Open or filed in the same pull request; the accounts this reading bears on, named in prose, nothing here rests on them -->

# NOTE-tmpa8fuv: Shazeer et al. — Outrageously large neural networks: the sparsely-gated mixture-of-experts layer

## What the paper does

**The layer.** n feed-forward experts E_i and a gate G whose output is a
sparse n-vector; the layer outputs y = Σ_i G(x)_i E_i(x) (Eq. 1), and
experts with G(x)_i = 0 are not computed. Noisy top-k gating (Eqs. 3–5):
H(x)_i = (x·W_g)_i + StandardNormal() · Softplus((x·W_noise)_i), keep the
top k, softmax over them. The gate is trained by back-propagation with the
rest of the model, unlike earlier REINFORCE-trained gates. For very many
experts, a two-level hierarchy (Appendix B).

**Engineering** (section 3). Experts receive only about kb/n of a batch,
so the paper mixes data and model parallelism to restore expert batch
size, applies the layer to all time steps at once, and makes experts
large enough that computation outweighs network traffic.

**The observation** (section 4, p. 5). "We have observed that the gating
network tends to converge to a state where it always produces large
weights for the same few experts. This imbalance is self-reinforcing, as
the favored experts are trained more rapidly and thus are selected even
more by the gating network." Eigen et al. (2013) describe the same and
avoid it by a hard constraint at the start of training; Bengio et al.
(2015) by a soft constraint on each gate's batch average. This paragraph
is the whole of the paper's treatment of the dynamics. Its evidence is
the no-loss row of Table 6.

**The fix.**
- *Importance loss* (Eqs. 6–7): Importance(X) = Σ_{x∈X} G(x), and
  L_importance = w_importance · CV(Importance(X))², which "encourages all
  experts to have equal importance" (p. 5).
- *Load loss* (Appendix A, Eqs. 8–11): equal importance can still hide
  unequal numbers of examples ("one expert may receive a few examples with
  large weights, and another may receive many examples with small
  weights", p. 6). The number of examples is discrete, so the paper
  estimates it smoothly: P(x, i) is the probability, over a fresh draw of
  expert i's noise, that i stays in the top k, which is Φ of its clean
  score minus the k-th highest other score, over the noise scale.
  Load(X)_i = Σ_x P(x, i), and L_load = w_load · CV(Load(X))². "This is
  the purpose of the noise term in the gating function" (p. 13).
- *Initialization*: W_g and W_noise start at zero, "which yields no signal
  and some noise" (p. 13), so load is nearly equal from the start, because
  "the soft constraints need some time to work".

**The ablation** (Table 6, p. 13). One architecture, MoE-256, trained 10
epochs on 1 billion words:

| w_importance | w_load | test perplexity | CV(importance) | CV(load) | max/mean load |
|---|---|---|---|---|---|
| 0.0 | 0.0 | 39.8 | 3.04 | 3.01 | 17.80 |
| 0.2 | 0.0 | 35.6 | 0.06 | 0.17 | 1.47 |
| 0.0 | 0.2 | 35.7 | 0.22 | 0.04 | 1.15 |
| 0.1 | 0.1 | 35.6 | 0.06 | 0.05 | 1.14 |
| 0.01 | 0.01 | 35.7 | 0.48 | 0.11 | 1.37 |
| 1.0 | 1.0 | 35.7 | 0.03 | 0.02 | 1.07 |

"All the combinations containing at least one the two losses led to very
similar model quality, where having no loss was much worse" (p. 14). One
seed per row is implied; no variance is given.

**Scale results.** At about 8 million operations per time step, test
perplexity on 1 billion words falls from 45.0 (4 always-active experts)
to 34.1 (4096 experts), 24% lower than the matched baseline (Table 7). On
100 billion words, 65,536 experts (68 billion parameters) give 39% lower
perplexity than the baseline, and 131,072 are worse, "possibly a result
of too much sparsity" (p. 8). WMT'14 En→Fr 40.56 BLEU and En→De 26.03,
above the GNMT baselines; a multilingual model beats multilingual GNMT on
11 of 12 pairs. Experts specialize: Table 9 shows an expert for
contexts of innovation, one for a verb taking "a" before a word of
importance or leadership, and one for speed.

**A detail.** Bengio et al.'s third loss, for diversity of gate values,
is not used: "we find that the gate values naturally diversify as the
experts specialize (in a virtuous cycle)" (footnote 1, p. 5).

## What it establishes and what it does not

It establishes, for one architecture and training run per setting, that
the unconstrained gate concentrates load heavily (one expert at nearly 18
times the mean) and that either balancing loss removes it and improves
perplexity by about 4 points. It states the mechanism, favoured experts
trained more and so chosen more, but does not test it: there is no
trajectory of gate weights, no comparison of initializations, and no
check of whether the neglected experts were less able or merely less
trained. It does not show that the balanced experts are equally
competent, only that they are equally used. The losses are a penalty on
unequal use, set by hand, not a mechanism that discovers which experts
deserve use.

## How it bears on the record

- **[CLAIM-277](../claims.d/CLAIM-277.md) and [CLAIM-443](../claims.d/CLAIM-443.md).** This is the entrenchment loop in a
  working system, with the mechanism stated by its builders: allocation
  determines training, training determines competence, competence
  determines allocation. It is [CLAIM-277](../claims.d/CLAIM-277.md)'s second chain and
  [CLAIM-443](../claims.d/CLAIM-443.md)'s warning that naive Hebbian learning entrenches,
  observed rather than conjectured, though only as an observation with one
  table behind it. Two details matter for the claims. The imbalance here
  is in use (importance and load), and the paper does not show whether
  the starved experts' competence fell or merely never grew, which is
  [QUESTION-134](../questions.d/QUESTION-134.md)'s distinction. And the imbalance cost performance (39.8
  against 35.6), so the entrenched allocation was not the competent one,
  which is the claim's failure regime and not merely a stable one.
- **Protected access versus imposed diversity.** The lead read load
  balancing and noisy gating as protected access. The reading corrects
  that. The losses make every expert equally important and equally loaded
  regardless of what it is good at. That is [QUESTION-132](../questions.d/QUESTION-132.md)'s second
  outcome, imposed diversity, "a programmed load balancer", not its first,
  and not [CLAIM-362](../claims.d/CLAIM-362.md)'s protection, in which "a process that rarely decides
  keeps access to the roles in which it is consequential". A rare
  specialist is exactly what an equal-load penalty pushes against: it is
  supposed to receive few examples. The noise term is mainly there to make
  the load estimate differentiable; it also gives a near-threshold expert
  some chance of selection, which is closer to exploration, but the paper
  does not measure that effect separately.
- **The fix's cost.** Under an equal-use penalty, competence alone does
  not set an expert's share. This is a floor and a ceiling on influence,
  set from outside the dynamics. The record's question is whether an
  organization can keep a specialist recoverable without such a
  constraint; this paper's answer, for its system, is that it used one.
- **[CASE-155](../cases.d/CASE-155.md).** The case's lock-in needs a score that rises with a
  process's own share. Here the share raises training, and training raises
  the score, so c > 0 arises through learning, not through the scoring
  channel. The initialization at zero, which keeps early shares equal, is
  the case's advice to start below the threshold; the losses lower the
  effective c throughout training.
