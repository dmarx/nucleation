---
status: Read
paper: LIT-tmp4de8g
title: 'Kramár, Lieberum, Shah and Nanda — AtP*, attribution patching and its failure modes'
version: 1
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Read in full on 2026-10-26 from the arXiv PDF, 2403.00745v1 (1 March
    2024, the only version; 46 pages), text extracted with pdftotext.
    Read: §§1–6 (introduction, the contribution problem, AtP and its two
    failure modes with the QK fix and GradDrop, the diagnostic, the
    baselines, the experimental setup and results, the discussion and
    recommendations, related work, conclusion), Appendix A (the
    subsampling proofs, Blocks and Hierarchical pseudocode, the efficient
    key correction, GradDrop's desiderata, the diagnostic algorithm),
    Appendix B (the distributions, cancellation, additional results,
    metrics, hyperparameters) and Appendix C.1 (layer normalization); the
    rest of Appendix C (edge AtP) and Appendix D (effect distributions)
    were not read. The method
    comparisons are given only as figures: Figures 1, 2 and 9 were read
    from page renderings (pp. 3 and 16), the others from captions and
    text, so the relative costs below are read off log-scale bar charts
    and are approximate. Nanda's 2023 post on attribution patching, the
    method's origin, was consulted for its date and acknowledgements only.
date: '2026-10-26'
summary: >-
  Attribution patching (AtP) estimates every node's activation-patching
  effect at once from two forward passes and one backward pass, by a
  first-order Taylor expansion. On Pythia models from 410M to 12B, using
  it to order which nodes to verify by real patching finds the
  largest-effect nodes far more cheaply than unordered patching or
  sampling-based search. Its false negatives come from saturated attention
  softmaxes and from direct and indirect effects that nearly cancel; AtP*
  recomputes the softmax for queries and keys and averages gradients with
  one layer dropped at a time. A subsampling test gives an upper
  confidence bound on the size of any nodes it still misses.
---
<!-- inactive-ok-file: THEORY-tmpq26u7 THEORY-802 THEORY-tmpoirdq — Proposed; the wider thesis filed from this reading and neighbouring accounts, cited as open -->

# NOTE-tmpz2cvc: Kramár, Lieberum, Shah and Nanda — AtP*, attribution patching and its failure modes

## Contribution

It is the first systematic test of attribution patching, the gradient
approximation to activation patching that Nanda proposed in a 2023 post,
against exhaustive ground truth on models up to 12B parameters. It finds
where the approximation fails, fixes the two failure modes it finds, and
adds a statistical check on what remains. Before it, attribution patching
was a fast heuristic whose misses were unknown; after it, its misses have
named causes and a bound.

## Key insight

Do not trust the approximation; use it to choose the order of exact
checks. A false positive costs one verifying forward pass, a false
negative is never found, so the quality that matters is recall at a
given cost. And the misses are not random: a linear approximation fails
exactly where a non-linearity sits between the node and everything else,
the attention softmax, or where large opposing effects sum to a small
total.

## Assumptions

- **Contribution.** c(n) = |I(n)|, I(n) = E_{(x_clean, x_noise)∼D}
  [L(M(x_clean | do(n ← n(x_noise)))) − L(M(x_clean))]: the absolute
  expected change in the metric when one node is noised with its value on
  a reference prompt. Zero and mean ablation are excluded by construction
  (footnote 1). Noising, following causal scrubbing (LIT-tmpqtkua) and the
  IOI work; denoising is briefly compared.
- **AtP.** Î_AtP(n) = (n(x_noise) − n(x_clean))ᵀ ∂L/∂n at x_clean, with the
  absolute value taken inside the expectation over prompt pairs. Cost:
  two forward passes and one backward pass per prompt pair for all nodes.
- **Nodes.** AttentionNodes: the query, key, value and per-head output at
  each token position. NeuronNodes: each MLP neuron's post-activation at
  each position. Coarser nodes (layers, residual streams) are out of
  scope.
- **Models and metric.** Pythia 410M, 1B, 2.8B and 12B; the metric is the
  negative log probability of the clean prompt's next token.
- **Settings.** Three single prompt pairs, IOI-PP (attention nodes),
  CITY-PP (neurons, factual recall) and RAND-PP (a random Pile prompt);
  and two small distributions, IOI on six names (120 pairs, attention
  nodes) and A-AN, an indefinite-article task (100 pairs, neurons).
- **The measure of a method** is the cost, in forward passes, of verifying
  the top K true nodes when nodes are verified in the method's order,
  summarized as an inverse-rank-weighted geometric mean relative to an
  oracle ordering (1 is perfect).
- **Baselines** were tuned over 5 seeds per setting and the best kept;
  AtP and its variants have no hyperparameters.

## Key results

- **Failure 1, attention saturation (§3.1.1, Figures 3–4).** When a
  query or key patch moves an attention weight across a flat region of the
  softmax, the gradient badly predicts the change, giving false negatives
  concentrated among keys and queries with large attention differences.
  The QK fix computes the patched attention weights exactly (combining
  noise queries with clean keys, and an O(T²) algorithm for keys) and
  applies the gradient only from the attention weights on; it costs less
  than two forward passes.
- **Failure 2, cancellation (§3.1.2, Figure 5).** When a node's direct
  and indirect effects nearly cancel, small errors in each can make the
  estimate orders of magnitude too small. GradDrop runs L extra backward
  passes, each zeroing the gradient through one layer's residual
  contribution, and averages the absolute estimates (scaled by 1/(L−1)).
  The three largest neuron false negatives it corrected had direct-effect
  ratios of 5.35, 12.2 and 0, against a median of 0.77 among nodes with a
  direct effect.
- **Comparison (Figures 1, 2, 8, 9; read off the charts).** AtP's
  relative cost is about 2 to 50 across models and settings, below the
  iterative, subsampling, blocks and hierarchical baselines in every one
  (those range from about 5 to over 1,000). On single prompt pairs AtP*
  is lowest or near lowest (CITY-PP about 2 to 5; IOI-PP about 3 to 6).
  On the distributions it is not: on IOI, AtP with the QK fix alone is
  cheapest (about 2), and on A-AN plain AtP (about 3), because GradDrop's
  upfront cost buys little once averaging over prompts dilutes
  cancellation. The authors' recommendation follows that pattern.
- **Diagnostic (§3.2, Figure 6).** Patching random subsets of the nodes
  outside AtP*'s top 1,024 and comparing subsets with and without each
  node gives, by a one-sided Welch test and the maximum p-value over
  nodes, an upper confidence bound on the effect of any missed node. In
  one setting it finds the largest remaining false negative early; in the
  other, with none, the bound tightens as samples grow.
- **Subsampling** is unbiased under node additivity, with bias p times the
  total pairwise interaction effect under a pairwise interaction model
  (Appendix A.1.1).
- **Robustness (Appendix B.4).** Rank plots are similar for three metrics
  on IOI; AtP* "looks notably worse" under denoising, which the authors
  cannot yet explain.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Ordering verification by AtP finds the top nodes far more cheaply than unordered or sampling-based search | strong for the five settings and four models | Figures 1, 2, 8, 9 |
| C2 | AtP's false negatives come mainly from attention saturation and from cancellation of direct and indirect effects | moderate | Figures 3–5; direct-effect ratios of three nodes |
| C3 | The QK fix and GradDrop reduce false negatives | strong for single prompt pairs; GradDrop adds little on distributions | Figures 1, 4, 5, 9 |
| C4 | The subsampling diagnostic bounds the size of remaining false negatives | demonstrated under its normality and additivity assumptions | §3.2, A.3, Figure 6 |
| C5 | AtP will transfer to other model families and larger models | conjecture, flagged as such | §5.1 |

## Concepts

- **Activation patching (noising)**: replace one node's activation on the
  clean prompt with its value on a reference prompt and measure the
  metric's change.
- **Attribution patching (AtP)**: the first-order estimate of that change
  for every node from one backward pass.
- **Verification**: patching nodes one at a time in estimated order, which
  removes false positives.
- **Cost of verified recall**: forward passes needed to verify the top K
  true nodes.
- **QK fix, GradDrop, AtP***: the two corrections and their combination.

## Connections

Attribution patching was introduced by Nanda in a 2023 post, from work
done at Anthropic in early 2022; ACDC's HISP baseline (LIT-tmpoku9b,
Appendix D.2) is the same estimate up to an absolute value, and Syed,
Rager and Conmy's edge attribution patching combines it with ACDC. The
edge version with integrated gradients is the method behind LIT-tmpf4hwb
and MIB's circuit track (LIT-tmprlq7z). The noising convention comes
from causal scrubbing (LIT-tmpqtkua). The authors place causal
abstraction (DAS, LIT-tmpsavwt) apart: it asks what low-level variables
mean, they ask which ones matter.

## Bearing on the record

- **THEORY-802 and QUESTION-234.** Not directly. The paper localizes
  effects to units fixed in advance (neurons, heads' queries, keys and
  values) and says that whether neurons are the right units is "out of
  scope". Its rankings are relative to that choice, which is THEORY-802's
  point in another setting.
- **THEORY-tmpoirdq.** That account's circuits are found with an
  edge-level descendant of this method. AtP's misses are concentrated in
  keys and queries behind saturated softmaxes, so a circuit drawn by
  plain attribution can lose attention edges for reasons of
  approximation, not of the model. That is a further reason, beside the
  budget effect that account records, for caution in reading circuit
  changes from such methods.
- **QUESTION-tmpivbso.** A cheap way to rank node effects at every
  checkpoint in models of Pythia's size, which do release checkpoints;
  the paper does not use them.

No instruction for machine-learning practice is recorded; the authors'
recommendations are the anthology's business (`anthology-candidate`).

## Limitations

- **Ground truth is single-node noising.** Effects that only appear when
  several nodes are patched together, and nodes whose effect is
  compensated downstream, count for less; the authors say direct effect
  and total effect "often significantly disagree".
- **Rank only.** It does not assess how close AtP's magnitudes are, nor
  false positives, nor agreement with circuits found by hand.
- **Few settings.** Three prompt pairs and two small distributions, one
  family (Pythia), one metric for the comparisons.
- **The headline numbers are only in charts.** No table gives the relative
  costs.
- **A dating slip.** The paper cites the attribution-patching post as
  "Nanda, 2022"; the post was published on 4 February 2023, describing
  work done in February–March 2022.

## Open questions

- Why is AtP* worse under denoising on IOI?
- Does the diagnostic's normality assumption hold for the heavy-tailed
  effect distributions of larger models?
