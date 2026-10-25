---
status: Read
paper: 'LIT-tmpjhci7'
title: 'Jacobs, Jordan, Nowlan and Hinton — Adaptive mixtures of local experts'
version: 1
history:
- version: 1
  date: '2026-10-24'
  note: >-
    Read in full on 2026-10-24 from a scan of the published article,
    Neural Computation 3(1): 79–87, posted on Geoffrey Hinton's University
    of Toronto page (https://www.cs.toronto.edu/~hinton/absps/jjnh91.pdf).
    The scan has no text layer, so it was read by OCR (tesseract at 300
    dpi), with the equations and the figure captions checked against the
    page images. Read: all of pp. 79–87, including Table 1 and the captions
    of Figures 1–3. The reference list was skimmed. Every quotation was
    checked by script against the OCR text, so OCR errors in the source
    were tolerated only where the words themselves were clean.
date: '2026-10-24'
summary: >-
  A short paper that founds the mixture of experts. Scoring the error of a
  single, gate-selected expert, or the mixture's negative log-likelihood,
  makes experts compete for cases, and an expert better than the
  gate-weighted average gains responsibility for the case. On a vowel task
  4 or 8 linear experts learned in half the epochs of matched
  backpropagation networks at equal accuracy, divided the task by class
  pair, and left all but 2 or 3 experts with mixing proportion near zero.
---
<!-- inactive-ok-file: THEORY-tmpgtvdv — Proposed; filed from this reading, named -->
<!-- inactive-ok-file: CLAIM-277 CLAIM-443 CLAIM-362 QUESTION-132 QUESTION-134 THEORY-899 — Proposed, Open or filed in the same pull request; the accounts this reading bears on, named in prose, nothing here rests on them -->

# NOTE-tmpau8o0: Jacobs, Jordan, Nowlan and Hinton — Adaptive mixtures of local experts

## What the paper does

**The problem.** A single backpropagation network trained on distinct
subtasks suffers strong "interference effects that lead to slow learning
and poor generalization" (p. 79). A gating network can send each case to
one or a few expert networks so that weight changes stay local. Earlier
systems (Hampshire and Waibel; Jacobs et al. 1990) blended the experts'
outputs linearly, E = ‖d − Σ_i p_i o_i‖², and so made each expert cancel
the residual left by the rest. "This strong coupling between the experts
causes them to cooperate nicely, but tends to lead to solutions in which
many experts are used for each case" (p. 80).

**The change.** Treat the gate as choosing one expert stochastically, with
probability p_i = exp(x_i) / Σ_j exp(x_j), and score the expected error,
E = Σ_i p_i ‖d − o_i‖² (Eq. 1.2). Each expert now produces the whole
output, and another expert's change can alter the responsibilities but
"cannot alter the sign of the error that a local expert senses" (p. 81).
Gradient descent then "tends to devote a single expert to each training
case. Whenever an expert gives less error than the weighted average of
the errors of all the experts (using the outputs of the gating network to
decide how to weight each expert's error) its responsibility for that
case" goes up (pp. 81–82), and an expert worse than the average loses
responsibility.

**The error used.** E = −log Σ_i p_i exp(−½‖d − o_i‖²) (Eq. 1.3), the
negative log probability of the target under a mixture of Gaussians with
the experts' outputs as means. Its gradient for expert i is
−[p_i e^(−½‖d−o_i‖²) / Σ_j p_j e^(−½‖d−o_j‖²)] (d − o_i) (Eq. 1.5), the
posterior responsibility times the error, where Eq. 1.2 gives −2p_i(d − o_i)
(Eq. 1.4). "Equation 1.4 will adapt the best-fitting expert the slowest,
whereas equation 1.5 will adapt it the fastest" (p. 82), when the gate
starts uniform and every error exceeds 1. I re-derived both gradients and
the claim: with equal p_i the step under Eq. 1.4 scales with e_i = ‖d −
o_i‖, smallest for the best expert, and under Eq. 1.5 with e_i
exp(−e_i²/2), which falls with e_i for e_i > 1, so the best expert's is
largest. The condition e_i > 1 matters; below it the ordering can
reverse.

**The second reading** (section 2). Competitive learning is a mixture
model generating output vectors; replace each competing unit by an expert
network whose output is the mean and let a gate set the mixing
proportions from the input. That is the same system, so the procedure is
at once "a modular version of a multilayer supervised network" and "an
associative version of competitive learning" (p. 79).

**The experiment** (section 3). Peterson and Barney's vowels [i], [I],
[a], [Λ] from 75 speakers, first two formants, trained on 50 speakers and
tested on 25. Mixtures of 4 or 8 experts, each able to draw only a linear
decision line, against backpropagation networks with 6 or 12 hidden units
and roughly equal parameter counts. Batch gradient descent, fixed step,
no momentum, trained to mean squared error 0.08, 25 runs per system
(Table 1):

| system | train % | test % | epochs (mean) | SD |
|---|---|---|---|---|
| 4 experts | 88 | 90 | 1124 | 23 |
| 8 experts | 88 | 90 | 1083 | 12 |
| BP, 6 hidden | 88 | 90 | 2209 | 83 |
| BP, 12 hidden | 88 | 90 | 2435 | 124 |

Identical accuracy is, the authors say, because the misclassified cases
are insensitive to small changes in the decision surfaces, and "the test
set is easier than the training set" (p. 85). The mixtures reach
criterion in about half the epochs; 8 experts slightly beat 4, while 12
hidden units are slower than 6 (t tests, 48 df).

**The dynamics** (Figure 3, pp. 86–87). "The system begins in an
unbiased state, with the gating network assigning equal mixing
proportions to all experts in all cases" (p. 86). Every expert then heads
for the single line that best fits all the cases. "Once one or more
experts begin to receive more error from cases in one class pair than
the other, this symmetry is broken" (p. 86), and experts split, one
taking [i]/[I], two sharing [a]/[Λ] as a piecewise-linear fit to its
curved boundary. "This solution is typical — in all simulations with
mixtures of 4 or 8 experts all but 2 or 3 experts had mixing proportions
that were effectively 0 for all cases" (p. 87). Figure 2's caption gives
the reading: "the system tends to use as few experts as it can to solve
a problem" (p. 84).

## What it establishes and what it does not

It establishes a learning rule, derived from a likelihood, under which
cases are allocated to whichever expert fits them better than the
gate-weighted average, and a demonstration on one small, low-dimensional
task with two natural subtasks. It does not report collapse onto one
expert as a problem: the idle experts are surplus capacity on a task
that needs two or three lines. It does not test what happens when the
task changes, whether an idle expert can regain responsibility, or how
the outcome depends on initialization, beyond showing that symmetry
breaks. It gives no theory of the dynamics, only the gradient and one
plotted run.

## How it bears on the record

- **[CLAIM-277](../claims.d/CLAIM-277.md).** The lead read MoE gating collapse as the claim's
  entrenchment loop. In this paper the loop is the claim's first chain,
  not its second: an expert gains responsibility for a case because it
  fits that case better than the weighted average, and what results is a
  division of labour that tracks the task's structure. Authority here is
  earned by relative competence, case by case, and that supports the
  claim's thesis that durable authority need not be a primitive. The
  claim's second chain, early advantage turning into durable authority,
  is not shown: the early phase is symmetric, and the split follows
  differences in error, not a head start. That narrows the lead's
  reading. This paper is the benign case; the collapse that is a failure
  belongs to Shazeer et al. ([LIT-tmp95a3g](../literature.d/LIT-tmp95a3g.md)), where the favoured experts
  win partly because they are trained more.
- **[QUESTION-132](../questions.d/QUESTION-132.md).** The idle experts are exactly the question's
  undecided case. With p_i ≈ 0 everywhere they receive almost no
  gradient (Eq. 1.5 scales with p_i), so under multiplicative allocation
  they are near the absorbing boundary the question warns of. The paper
  never asks whether one, made relevant by a new subtask, would recover.
  So it cannot tell the question's three outcomes apart, and gives no
  recovery exponent. It is the simplest model in which the question's
  ablation, recovery from ε > 0 after the task changes, could be run.
- **[CLAIM-362](../claims.d/CLAIM-362.md) and [QUESTION-134](../questions.d/QUESTION-134.md).** An expert whose gate weight is near
  zero everywhere is a process with no consequential role. Whether it
  keeps the competence to take one back is [QUESTION-134](../questions.d/QUESTION-134.md)'s question; here
  its weights simply stop changing, so it neither learns nor forgets.
- **[CASE-155](../cases.d/CASE-155.md) and [THEORY-899](../theory.d/THEORY-899.md).** The posterior responsibility in
  Eq. 1.5, p_i e^(−½e_i²) / Σ_j p_j e^(−½e_j²), is the case's first result
  per training case: authority reweighted by each expert's likelihood of
  the target, Bayes over experts as hypotheses. The gate learns that
  reweighting as a function of the input, so the mixture of experts is a
  learned, context-dependent version of the case's replicator reading of
  authority.
