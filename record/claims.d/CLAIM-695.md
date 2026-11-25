---
number: 695
status: Proposed
formerly:
- CLAIM-tmp36o5i
title: 'RLVR can sharpen without expanding'
statement: >-
  Reinforcement learning on verifiable rewards can make a disposition the
  base model already had cheaper to realize, by moving probability toward
  successful trajectories the base reaches under enough sampling, which
  amortizes part of a search into the policy without enlarging what the base
  reaches at large budgets; whether a given run sharpened or expanded is an
  empirical question per run, settled by matched-budget coverage curves and
  causal tests on the tokens where the two models diverge
version: 1
role: thesis
warrant: empirical
defeated_if: >-
  Matched-budget comparisons in which RL-trained models generally exceed
  their base models' coverage at large k on the same tasks, so that the
  low-budget gain is not reallocation; or causal token-swap tests showing
  that the gain does not localize to the positions where base and trained
  distributions diverge; or a reading of the idealized tilt π* ∝ π0·e^{r/β}
  under which reweighting can create modes the base lacks.
tags:
- learning-theory
- agency
- anthology-candidate
date: '2026-11-15'
line:
- realizability
- learned-structure
rests_on:
- CLAIM-697
complements:
- CLAIM-576
grounds:
- THEORY-1880
- THEORY-1899
- THEORY-1896
summary: >-
  The owner's: "I feel like this also connects to the interpretation of RL
  post-training as distribution-sharpening". The claim is A's
  elaboration (A26), checked against readings filed with it. Yue et al.
  find base models overtaking RLVR models at large pass@k. Meng et al.
  find the gain carried by a few divergent tokens. Balasubramanian and
  Kasiviswanathan show that an exponential tilt reweights modes but does
  not create them. ProRL is the counter-case, with new strategies under
  prolonged RL that has diversity-preserving design, from a distilled
  start, at k up to about 128, and with narrowed boundaries on math. The
  claim keeps the disagreement as "per run". The record holds the agent-RL
  version of the dispute ([CLAIM-663](CLAIM-663.md), [ARG-093](../arguments.d/ARG-093.md)). The idea is the owner's;
  the wording is A's, and adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-697 CLAIM-663 ARG-093 THEORY-1880 THEORY-1899 THEORY-1896 THEORY-1908 — Proposed or new; the claim this rests on and the held entries on the same dispute -->

# CLAIM-695: RLVR can sharpen without expanding

## The claim

In [CLAIM-697](CLAIM-697.md)'s terms, RL post-training can shift a disposition's
resource–reliability curve to the left without raising its plateau. Under
the idealized KL-regularized objective, the optimum is an exponential
reward tilt of the base, π*(y|x) ∝ π0(y|x)·e^{r(x,y)/β}. That is not
temperature sharpening, which rescales whatever was already probable. A
tilt raises whatever is rewarded, however rare. If a correct trajectory
has base probability 1% and the tilt raises it to 20%, one sample from the
trained policy is worth about 22 from the base (rechecked). That holds
only if a verifier exists to recognize success in the base's samples.

## What the readings show

- **Yue et al.** ([THEORY-1880](../theory.d/THEORY-1880.md)) find that RLVR raises small-k success while base models
  match or overtake at large k, "consistently" in the paper's words. That is
  reallocation in their settings.
- **Meng et al. (Sparse but Critical)** ([THEORY-1899](../theory.d/THEORY-1899.md)). Injecting RL-sampled tokens at
  the positions where the two distributions diverge most recovers much of
  the RL model's accuracy with few interventions: "fewer than 4% RL-sampled
  tokens per sequence on average" in one setting, under 8% in others. The
  change is local, at a few decision points.
- **Balasubramanian and Kasiviswanathan** ([THEORY-1896](../theory.d/THEORY-1896.md)). In a setting they call
  "intentionally minimal", a two-mode mixture, their Lemma 3.2 shows that
  the target of their objective with disjoint supports "only Weights
  Existing Mode Mass": it reweights modes and does not create them. Post-training's losses separate into mass lost on old modes
  and drift within them.
- **ProRL, against** ([THEORY-1908](../theory.d/THEORY-1908.md)). Prolonged RL with diversity-preserving choices
  improves high-budget coverage and finds strategies not seen from the
  base. The qualifiers: the start is already a distilled reasoner, "extensive
  sampling" is k up to about 128, and on math the paper too reports
  narrowed boundaries.

So the claim is per run. Matched coverage curves across a wide range of k,
with prompt format, temperature and decoding held equal, decide which
happened.

## An illustration of the crossing

Take two problems. The base succeeds per attempt with (0.05, 0.005), a
sharpened policy with (0.50, 0.0001). Mean coverage is:

| k | 1 | 10 | 100 | 500 |
|---|---|---|---|---|
| base | 2.75% | 22.51% | 69.42% | 95.92% |
| sharpened | 25.01% | 50.00% | 50.50% | 52.44% |

(Rechecked.) It is A's construction and models no real system. The ideal
per-prompt tilt with a perfect binary reward cannot produce it, since that
tilt raises every prompt. Crossings point to shared parameters, imperfect
optimization or reward mismatch.

## What it does not say

- **That RL only sharpens.** ProRL is a counter-case, and repeated success
  may itself build a more efficient mechanism.
- **That a vanishing alternative is lost.** A strategy whose probability
  falls may be suppressed, may have drifted, or may be gone. Telling these
  apart takes causal tests, not coverage alone.
