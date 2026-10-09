---
number: 201
status: Proposed
formerly:
- THEORY-tmpyaqz7
promote_when: >-
  A result in which the usable context, or the depth of hidden structure a
  next-token learner represents, is moved by changing how fast token
  correlations decay while the grammar's size stays fixed: for instance, a
  hierarchical grammar with non-uniform production probabilities, or a
  real corpus whose long-range correlations are weakened by an
  intervention that keeps its n-gram statistics up to some range, with
  the training-set size at which each level is learned, or at which the
  loss for a given context saturates, tracking the predicted detection
  threshold. Or a proof that gradient descent on a deep network learns the
  level-ℓ hidden variables of such data from about the number of samples
  at which their correlations exceed sampling noise. More collapses of
  learning curves on the uniform Random Hierarchy Model cannot settle it,
  because there the detection threshold and the counting of the grammar
  are the same expression.
title: 'In next-token prediction on hierarchically generated sequences, the correlation between two tokens falls by about a factor m per level of their common ancestor, so a training set of P sequences resolves correlations only out to a distance t*(P) at which they meet sampling noise; learners come to represent the hidden symbols up to that depth, giving loss steps at about v m^(2ℓ−1) examples, and on character-level text the context at which the loss saturates grows as P^(1/(2β)) with β the measured correlation decay'
version: 1
tags:
- learning-theory
- representation-learning
- compositionality
date: '2026-10-09'
source:
- LIT-883
- LIT-877
summary: >-
  Cagnetta and Wyart (2024), [LIT-883](../literature.d/LIT-883.md), extending [LIT-877](../literature.d/LIT-877.md) from labels to
  masked tokens: the correlation plateaus and the noise floor are derived
  for the Random Hierarchy Model in the large-v, large-m limit; the loss
  steps and the representation probes are measured in small transformers
  and CNNs; the link between them is argued, not proved; and the
  real-text evidence, from two character-level corpora, tests the
  effective context window, not the hierarchy.
---
<!-- inactive-ok-file: THEORY-195 THEORY-182 THEORY-183 THEORY-186 QUESTION-025 — Proposed or open; cited as the accounts this one is set beside and the question it does not answer -->

# THEORY-201: In next-token prediction on hierarchically generated sequences, the correlation between two tokens falls by about a factor m per level of their common ancestor, so a training set of P sequences resolves correlations only out to a distance t*(P) at which they meet sampling noise; learners come to represent the hidden symbols up to that depth, giving loss steps at about v m^(2ℓ−1) examples, and on character-level text the context at which the loss saturates grows as P^(1/(2β)) with β the measured correlation decay

## Source

Cagnetta and Wyart (2024, NeurIPS 2024), [LIT-883](../literature.d/LIT-883.md), Eqs. 6–16, Figs.
1–9, Appendices D–G, as read in [NOTE-687](../notes.d/NOTE-687.md). It extends Cagnetta et
al. ([LIT-877](../literature.d/LIT-877.md)), whose classification result is [THEORY-195](THEORY-195.md).

## What was actually shown

**The statistics.** Sequences are the leaves of a Random Hierarchy Model
tree: L levels of v symbols, each rewriting to m distinct s-tuples, no tuple
with two parents. The covariance between the masked last token and a token
whose lowest common ancestor with it is at level ℓ has zero mean over
draws of the grammar and root-mean-square size
((1 − m/v^(s−1))/(v³ m^(2ℓ−1)))^(1/2), asymptotically in v and m (App. D).
Against distance this is roughly t^(−β), β = ln m/ln s. Estimated from P
samples it saturates at (v²P)^(−1/2) (App. E), so P resolves correlations
only out to t*(P). Correlations of the target with whole tuples, and their
noise, both shrink by √m, so the thresholds P_ℓ = v m^(2ℓ−1)/(1 − m/v^(s−1))
hold for them too (App. F). These could have come out otherwise: the
empirical correlation functions of Fig. 1 might not have followed the
derived plateaus, or might not have saturated at the predicted floor.

**The learning.** Attention-only transformers and tree-matched CNNs trained
to predict the last token show loss steps near P_ℓ, down to plateaus near
the loss of conditioning on the last s^ℓ − 1 tokens; with the context cut,
the steps stop where the theory says (Figs. 2, 6). In CNNs, the first two
steps collapse on P_1 and P_2 = vm³ across m (Figs. 7, 8), and the layers
above ℓ become insensitive to redrawing the subtree below a level-ℓ symbol
near P_ℓ (Fig. 3). The networks could have learned at sample sizes
unrelated to the correlation thresholds, or generalised without such
invariance.

**The real-text test.** On character-level tiny-Shakespeare and
WikiText-103, the correlation decays as t^(−β) (β ≈ 1.4, 1.55). The
exponent z = 2β is read from the collapse of the empirical correlation
functions, then used to rescale the losses of transformers with contexts
t = 1 to 15. They collapse as L = t^(−αz) f(P/t^z) (Figs. 4, 5). This
could have failed: the loss could have saturated at a P unrelated to the
correlation decay.

## What this does not say

- **Not that trained networks find the hidden variables by detecting
  correlations.** That route is an argument (§4.1). The coincidences are
  measured, and the authors say a proof needs a theory of deep training
  dynamics that does not yet exist (§6).
- **Not that the thresholds are exact for every architecture.** CNNs reach
  the third step before P_3, which the authors attribute to weight sharing
  and would scale as m^(ℓ+1); P_1 grows with the context length, which the
  analysis does not capture (App. G).
- **Not that language is generated by such a tree, or that its scaling
  exponents come from one.** The real-text test needs only correlations
  that decay with distance. It says nothing of hidden variables, and it
  was run at character level on two small corpora with contexts up to 15.
  The steps of the model come from its uniform, unambiguous, fixed-shape
  rules, which text does not have.
- **Not that the power-law learning curve is derived.** Eq. 13 composes the
  steps after dropping every factor that does not depend on ℓ. As printed,
  its exponent has the wrong sign.
- **Not anything about embeddings or directions.** The correlation
  function is a norm over the vocabulary. The model's hierarchy shows in
  co-occurrence as equal correlations for tuples with one parent, and as
  strength falling with depth. Whether that gives linear directions for
  ancestors is [QUESTION-025](../questions.d/QUESTION-025.md), and this work does not test it.
- **Not a rule for building language models.** How much context or data a
  model should be given is an ML-practice question, and this account does
  not answer it.
