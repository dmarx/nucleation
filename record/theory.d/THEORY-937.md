---
number: 937
status: Active
formerly:
- THEORY-tmpgtvdv
title: 'When a mixture of experts is trained on the error of a single expert chosen stochastically by the gate, or on the negative log-likelihood of the mixture, the gradient raises the gate''s logit for an expert that fits a case better than the gate-weighted average and lowers it for one that fits worse; on a four-class vowel task, mixtures of 4 or 8 linear experts learned in about half the epochs of backpropagation networks of roughly equal parameter count, at equal accuracy, and divided the task by class pair, leaving all but 2 or 3 experts with mixing proportions effectively zero'
version: 2
history:
- version: 2
  date: '2026-10-30'
  note: >-
    Promoted by the twenty-third status review, at the status review's
    ruling (the owner delegated these rulings; ADR-065). The title's first
    clause is a derivation: NOTE-1147 and this entry re-derived it when
    filed, and the review checked it as a second checker, step by step
    and by finite differences with controls (note below; the script is
    re-run by another reader before the ruling, ADR-065 §5). The rest
    reports what one study read in full measured, with its hedges, and
    nothing in the record contradicts it. Narrowed first, two
    mis-statements (ADR-047 kind 3, note below): "gains responsibility"
    holds for the gate's logit, while with more than two experts the
    mixing proportion of a better-than-average expert can fall; and the
    backpropagation networks had "roughly equal parameter counts", not an
    equal size. The old title: "When a mixture of experts is trained on
    the error of a single expert chosen stochastically by the gate, or on
    the negative log-likelihood of the mixture, an expert that fits a case
    better than the gate-weighted average gains responsibility for it; on
    a four-class vowel task, mixtures of 4 or 8 linear experts learned in
    about half the epochs of backpropagation networks of equal size, at
    equal accuracy, and divided the task by class pair, leaving all but 2
    or 3 experts with mixing proportions effectively zero". What the
    condition asked beyond the title, a second study on another task,
    moves to QUESTION-tmpxiomw (ADR-065 §3). The old promote_when: "A checked
    derivation, recorded here, that under the error of Eq. 1.3 the
    gradient for each expert is its posterior responsibility for the case
    times its error, and that with a uniform gate and every error above 1
    the best-fitting expert takes the largest step and under Eq. 1.2 the
    smallest (made when filed, from NOTE-1147); together with a second
    study, on another task, in which mixtures trained this way leave most
    experts with near-zero mixing proportions while matching a dense
    network of equal size. It is refuted if the gradients differ from
    those stated, or if the vowel result does not replicate. Whether the
    idle experts could regain responsibility is a separate question, and a
    result about it neither promotes nor refutes this."
tags:
- learning-theory
- probabilistic-modeling
date: '2026-10-24'
source:
- LIT-1514
summary: >-
  Jacobs, Jordan, Nowlan and Hinton (1991), read in full in [NOTE-1147](../notes.d/NOTE-1147.md)
  from a scan of the published article. The gradients of Eqs. 1.4 and 1.5
  were re-derived when filed. The task is small (two formants, 75
  speakers, 25 runs per system) and has two natural subtasks; the idle
  experts are read by the authors as economy, and their recovery is not
  tested.
corroborates:
- CLAIM-467
bears_on:
- QUESTION-tmpxiomw
---
<!-- inactive-ok-file: QUESTION-tmpxiomw — Open; the replication its condition asked for -->

# THEORY-937: When a mixture of experts is trained on the error of a single expert chosen stochastically by the gate, or on the negative log-likelihood of the mixture, the gradient raises the gate's logit for an expert that fits a case better than the gate-weighted average and lowers it for one that fits worse; on a four-class vowel task, mixtures of 4 or 8 linear experts learned in about half the epochs of backpropagation networks of roughly equal parameter count, at equal accuracy, and divided the task by class pair, leaving all but 2 or 3 experts with mixing proportions effectively zero

## Source

Jacobs, Jordan, Nowlan & Hinton (1991), [LIT-1514](../literature.d/LIT-1514.md), read in
[NOTE-1147](../notes.d/NOTE-1147.md): Eqs. 1.2–1.5 (pp. 80–82), Table 1 and Figures 2–3
(pp. 84–87).

## What was actually shown

- **The rule.** With E = −log Σ_i p_i exp(−½e_i²), e_i = ‖d − o_i‖, the
  gradient for expert i is its posterior responsibility h_i = p_i
  exp(−½e_i²) / Σ_j p_j exp(−½e_j²) times (d − o_i). The gradient on the
  gate's logit for expert i is p_i − h_i, so descent raises that logit
  exactly when the expert's likelihood is above the p-weighted average.
  Re-derived when filed, and checked again on 2026-10-30 (note below).
- **The speed.** 1124 and 1083 mean epochs to criterion for 4 and 8
  experts against 2209 and 2435 for 6 and 12 hidden units, 25 runs each,
  with 88% train and 90% test accuracy for all four.
- **The division.** From equal mixing proportions, experts first converge
  on the one-line average solution, then split by class pair once their
  errors differ; in every run all but 2 or 3 experts end with mixing
  proportions effectively zero.

## What this does not say

That the concentration on a few experts is entrenchment rather than
economy: the task needs two or three lines, and the split follows
differences in error, not a head start. That an idle expert could regain
responsibility if the task changed; this was not tested. Or anything
about large mixtures, where Shazeer et al. ([LIT-1507](../literature.d/LIT-1507.md)) report the
imbalance as a failure. Or that every expert fitting better than the
average gains mixing proportion: with more than two experts it can lose
some (note below).

## Note of 2026-10-30: the derivation, checked, and the title narrowed

Checked by the twenty-third status review as a second checker (ADR-065
§5). Write p = softmax(x) for the gate's proportions and x for its
logits, e_i = ‖d − o_i‖, L_i = exp(−½e_i²), S = Σ_j p_j L_j and
h_i = p_i L_i / S, and use ∂p_j/∂x_i = p_j(δ_ij − p_i).

1. **Eq. 1.3, experts.** ∂E/∂o_i = −(p_i/S) ∂L_i/∂o_i =
   −(p_i L_i/S)(d − o_i) = −h_i(d − o_i), which is Eq. 1.5.
2. **Eq. 1.2, experts.** The derivative of Σ_j p_j e_j² with respect to
   o_i is −2p_i(d − o_i), which is Eq. 1.4.
3. **Eq. 1.3, gate.** ∂E/∂x_i = −(1/S) Σ_j L_j p_j(δ_ij − p_i) =
   −(p_i L_i − p_i S)/S = p_i − h_i. Descent moves x_i by η(h_i − p_i),
   up exactly when L_i > S: when the expert's likelihood is above the
   gate-weighted average.
4. **Eq. 1.2, gate.** ∂E/∂x_i = Σ_j e_j² p_j(δ_ij − p_i) =
   p_i(e_i² − Σ_j p_j e_j²). Descent raises x_i exactly when e_i² is below
   the gate-weighted mean squared error, as the paper says (pp. 81–82).
5. **The proportion.** A step Δx changes p by J Δx to first order, with
   J = diag(p) − ppᵀ, so Δp_i = p_i(Δx_i − Σ_j p_j Δx_j). With two experts
   Δx_2 = −Δx_1 under both errors, so Δp_1 has the sign of Δx_1 and the
   rule holds for the proportion too. With more experts it need not. An
   exact case, under Eq. 1.3: p = (0.15, 0.60, 0.25) and
   L = (0.50, 1.00, 0.95). Then S = 73/80 = 0.9125 and
   h = (6/73, 48/73, 19/73). Expert 3 fits better than the average
   (0.95 > 0.9125), and its logit rises: Δx_3 ∝ h_3 − p_3 = 3/292. But
   Σ_j p_j(h_j − p_j) = 393/14600 ≈ 0.02692 exceeds it, so
   Δp_3 ∝ 0.25 × (3/292 − 393/14600) = −243/58400 ≈ −0.00416: its
   proportion falls. In random draws the rule held for every proportion
   in 1,000 of 1,000 cases with two experts, 685 with three, 485 with four
   and 171 with eight, and the best-fitting expert's proportion fell in 6
   to 16% of draws with three or more. So the old title's "gains
   responsibility" was a mis-statement for the mixing proportion. It
   holds for the gate's logit, and the title now says so (ADR-047 kind 3).
6. **NOTE-1147's ordering.** With equal p_i, |∂E/∂o_i| is proportional to
   e_i under Eq. 1.4 and to e_i exp(−e_i²/2) under Eq. 1.5. The second
   falls with e_i for e_i > 1, so the best expert takes the smallest step
   under Eq. 1.4 and the largest under Eq. 1.5; below 1 the ordering
   reverses.

Steps 1–4 and 6 were checked by central finite differences on 200 random
mixtures of 2 to 8 experts with outputs of dimension 1 to 3. Every
analytic gradient matched. Two wrong forms, p_i in place of h_i and the
gate gradient with its sign flipped, were rejected in all 200. The
ordering held in 200 of 200 draws with every error above 1, and reversed
in 200 of 200 with every error below 0.9, the control. Step 5's counts and
the case above were checked against a real small softmax step. The
scripts, numpy only, are moe_check.py, moe_check_p.py and
counterexample.py in the status review's working directory. A second
person re-ran moe_check.py and moe_check_p.py on 2026-10-30 and got the
same counts.

The backpropagation networks had "roughly equal parameter counts"
(NOTE-1147), so "of equal size" became "of roughly equal parameter count"
(ADR-047 kind 3). The replication the condition asked for is
QUESTION-tmpxiomw.
