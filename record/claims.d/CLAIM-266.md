---
number: 266
status: Active
formerly:
- CLAIM-tmpbcck8
title: 'A family of probes that supplies an optimized system''s training signal
  cannot also certify what the system preserves: optimization pushes toward
  whatever the probes reward, including what they cannot see, so preservation
  must be shown under probes not used to train it'
version: 3
history:
- version: 1
  date: '2026-10-13'
  note: Split from CLAIM-149 under ADR-040, at the owner's request ("go ahead
    with the group B splits"). The assistant restated the general content
    without the premises about translation that CLAIM-149 rests on; CLAIM-149
    now rests on this claim.
- version: 2
  date: '2026-10-29'
  note: >-
    Promoted to Active at the twelfth status review, by the owner's
    assent in its pull request (ADR-057). Nothing objects to it, its
    one ground CASE-041 is Active, and no finding meets its defeat
    condition. CASE-071 is added to illustrated_by: the same bias
    produced by selection against a metric. The last bullet of "What
    it does not say", which read "The documented support is one case,
    in image generation. Hence Proposed.", is replaced. The claim is
    unchanged.
- version: 3
  date: '2026-11-11'
  note: >-
    Reading review of 2026-11-11, by question: bears_on QUESTION-258
    added. The question's text: "The measures cannot certify the
    choice. From CLAIM-266 and CLAIM-190: 'we shouldn't certify
    manuscripts using only the structural measures we optimized.'" Its
    title: a family of probes that supplies an optimized system's
    training signal "cannot also certify what the system preserves".
    Under ADR-085 it takes records-of-inquiry, the question's first
    line, after its own. No other change.
role: thesis
warrant: interpretive
defeated_if: Across systems optimized against a probe family, evaluation in
  that family is found to rank and score them no differently from evaluation
  under independent probes and from independent human judgement, so that the
  training probes certify as well as held-out ones.
tags:
- model-comparison
- representation-learning
- philosophy-of-science
date: '2026-10-13'
line:
- formal-apparatus
- records-of-inquiry
grounds:
- CASE-041
summary: 'The general content of [CLAIM-149](CLAIM-149.md), filed alone under [ADR-040](../decisions.d/ADR-040.md) so that
  it does not rest on [CLAIM-011](CLAIM-011.md)''s account of correspondences in translation.
  Training against a probe family pushes a system toward whatever the family
  rewards, including differences it cannot see, so the family is not a certificate
  of what was preserved. [CASE-041](../cases.d/CASE-041.md) is a documented instance: a Projected FastGAN
  trained against ImageNet features matches StyleGAN2''s FID, also computed
  in ImageNet features, while doing worse in CLIP space and with human judges.'
bears_on:
- QUESTION-258
---
<!-- inactive-ok-file: ADR-085 — Proposed; the line rule the history note of 2026-11-11 applies -->
<!-- inactive-ok-file: CLAIM-190 — Superseded; cited as an application, as filed -->
<!-- inactive-ok-file: ARG-028 — Proposed; cited in the note of 2026-11-12 for what each holds, not as settled -->
<!-- inactive-ok-file: THEORY-1730 THEORY-1733 THEORY-1738 THEORY-1743 THEORY-1754 THEORY-1757 THEORY-1759 THEORY-1760 THEORY-1769 THEORY-1770 THEORY-1772 THEORY-1776 THEORY-1782 THEORY-1784 THEORY-1785 THEORY-1794 THEORY-1799 THEORY-1801 THEORY-1803 THEORY-1804 THEORY-1811 THEORY-1812 — filed from the exchange "luria experiment design", Proposed or Deferred; cited as filed alongside this entry -->

# CLAIM-266: A family of probes that supplies an optimized system's training signal cannot also certify what the system preserves: optimization pushes toward whatever the probes reward, including what they cannot see, so preservation must be shown under probes not used to train it

## The claim

What a system learns to preserve is constrained by what its training
signal can distinguish. What can be verified that it preserved is
constrained by the observations used to evaluate it. When the two are the
same probe family, evaluation measures fit to the training signal, not
preservation. Optimization moves the system toward whatever the probes
reward, and that includes differences the probes cannot see. So
preservation has to be shown under probes the system was not trained
against.

The documented case ([CASE-041](../cases.d/CASE-041.md)) is worse than blindness. A generator
trained against ImageNet features matches a stronger generator's FID,
computed in the same features, while doing worse in an independently
trained feature space and with human judges.

## Where the record applies it

[CLAIM-149](CLAIM-149.md) applies it to translation and reconstruction models tuned
against pragmatic classifiers or judges. [CLAIM-190](CLAIM-190.md) applies it to a
record's anchoring measures. Both now rest on this claim for the general
point.

## What it does not say

- It does not say metrics in the training probes are worthless, only that
  they are not a certificate.
- It does not say a system trained against a family will introduce the
  differences the family cannot see. It says the family cannot show that
  it did not.
- It does not say held-out probes are neutral. They have their own
  training data.
- That its generality rests on its cases. Its ground is the argument
  above: a family the system was optimized against scores it well whether
  or not it preserved what the family cannot see, so the score cannot tell
  the two apart. [CASE-041](../cases.d/CASE-041.md) shows the bias in image generation, by training;
  [CASE-071](../cases.d/CASE-071.md) shows it in translation, by selection against the metric, which
  the title's "training signal" does not literally cover.

## Note of 2026-11-12: two instances in evaluating the record itself, from "luria experiment design"

Two proposals in the exchange "luria experiment design" (2026-11-10, https://chatgpt.com/share/6af35bfc-35f8-83e9-a63d-d594703eabda) are instances of this claim. A45 §8: a benchmark
whose reward is "reproducing the very decisions Nucleation made" cannot be
treated "as independent proof that those decisions were epistemically
optimal"; historical cases serve "motivation, task development, and
qualitative process tracing", and confirmation needs "unseen problems with
independent semantic criteria". A43 §12: keep "a genuine outer evaluation
boundary", since agents that can rewrite the criterion that judges their
improvements are being certified by the probes they optimize. [ARG-028](../arguments.d/ARG-028.md)'s
open dispute, whether measures computed in the grammar can certify that
drift fell, is the same point about the record's own measures. The claim
is unchanged.

## Note of 2026-11-12: 22 readings of the works of "luria experiment design"

Read on 2026-11-12 among the works of the exchange "luria experiment design"; each reading's NOTE and THEORY hold the detail.

- **Chen, Zhu and Zheng** ([THEORY-1784](../theory.d/THEORY-1784.md)): Proposition 2 is a formal version for audit graders, and adds that held-out *tasks* do not suffice if the *grader* shares the development judge's bias. Supports.
- **Mo, Zheng et al.** ([THEORY-1811](../theory.d/THEORY-1811.md)): Every score is an LLM judgment; the paper grounds originality in retrieved prior art to reduce judge bias, which is a partial response of the kind those claims call for. Illustrative only.
- **Thaman** ([THEORY-1738](../theory.d/THEORY-1738.md)): RHB is an instance of optimization (here, agent behaviour shaped by RL post-training) pushing toward what the checker rewards and cannot see; it supports both, at the level of agent behaviour rather than training probes.
- **Zhu et al.** ([THEORY-1782](../theory.d/THEORY-1782.md)): The KPI and coordination scores are LLM judgments; no bearing beyond caution.
- **Romera-Paredes et al.** ([THEORY-1803](../theory.d/THEORY-1803.md)): **consistent, boundary case**: in FunSearch the probe *is* the target (the score is the mathematical quantity), so there is nothing beyond the probe to preserve; this is the condition under which optimizing against the probe is safe.
- **Huang, Xu, Ma et al.** ([THEORY-1801](../theory.d/THEORY-1801.md)): **supports** in an inference-time setting: once review feedback is returned, "review becomes part of the search process" (§8). It also **qualifies** the remedy: the non-overlapping panel was a probe not used in the loop and still cleared 44 of 56 evasions, because it read the same agent-supplied evidence. An unused probe must also draw on evidence the system did not produce.
- **Liu and Yadav** ([THEORY-1730](../theory.d/THEORY-1730.md)): The benchmark keeps the scorer (deterministic assertions) outside the agent for state tasks, but uses LLM judges for procedure and user experience. That is a mixed instance of separating evaluator from optimized system.
- **Jansen, Clark, Downey and Weld** ([THEORY-1760](../theory.d/THEORY-1760.md)): The self-assessed belief result (calibration fails on novel laws) is a case where the generator's own estimate cannot certify its output.
- **Hu, Lu and Clune** ([THEORY-1799](../theory.d/THEORY-1799.md)): Illustrates. Validation accuracy is both the search signal and the reported held-out measure, though on separate splits.
- **Lu et al.** ([THEORY-1772](../theory.d/THEORY-1772.md)): **illustrates, does not test**. The same Automated Reviewer serves as fitness signal (Fig. 1b, Fig. 3c) and as evaluation. The paper's only independent check is three workshop submissions.
- **Gottweis et al.** ([THEORY-1769](../theory.d/THEORY-1769.md)): **instance**. The tournament supplies both the selection signal and the reported measure of improvement.
- **Huang et al.** ([THEORY-1770](../theory.d/THEORY-1770.md)): **leaves open**. DISCERN uses LLM reviewers and an LLM judge with human adjudication; it does not test judge capture. Its clean controls are a design answer to one evaluation failure (rewarding blanket rejection)
- **Chi et al.** ([THEORY-1794](../theory.d/THEORY-1794.md)): **consistent with, not a test**. The design keeps the scoring evaluator out of the agent's reach and admits the proxy may share data with it.
- **Chong, Zhang, Fan and Du** ([THEORY-1733](../theory.d/THEORY-1733.md)): **consistent**. The gate scores on the same workload distribution it optimizes; the paper does not test whether accepted changes preserve anything the validation set cannot see.
- **Srikanth et al.** ([THEORY-1754](../theory.d/THEORY-1754.md)): **consistent, partly addressed**. The design separates the signal agents optimize (r_t) from the selection grade (g) and checks an unoptimized behaviour on held-out tasks; that is the kind of independent probe the claim says is needed, and here reward hacking fell. It does not test preservation of anything the probes miss.
- **Majumder et al.** ([THEORY-1812](../theory.d/THEORY-1812.md)): The benchmark's evaluation is an LLM judge; the paper does not test its agreement with humans in the main text. Leaves open.
- **Bao et al.** ([THEORY-1785](../theory.d/THEORY-1785.md)): **support, as evidence of the risk both describe**. The paper's finding that automated judges agree with experts near chance, and its argument that "Judges and judged are drawn from the same distribution", are the empirical side of evaluator capture; its scientists' self-similarity bias (preferring ideas like their own) is the human side of [CASE-144](../cases.d/CASE-144.md)'s mechanism.
- **Zelikman, Lorch, Mackey and Kalai** ([THEORY-1757](../theory.d/THEORY-1757.md)): **supports, as an instance**. Optimizing a meta-utility selected improvers that dropped constraints the utility did not enforce, and an exploitable utility returned an accuracy over 1000%; the authors' remedy was enforcement outside the optimized code (the LM object enforcing budgets; a sandbox), not the utility.
- **Liu, Huang, Hu, Zhou and Tan** ([THEORY-1759](../theory.d/THEORY-1759.md)): *leaves open*, but HypoBench's own caution that LLM-judged novelty is unvalidated (result 9) is an instance of the measurement problem CLAIM-266's line is about; no optimization against the probes occurs here.
- **Liu, Yang et al.** ([THEORY-1804](../theory.d/THEORY-1804.md)): *leaves open*; the 83% order-driven ranking errors (result 7) are an evaluator-reliability finding that would matter to any design using an LLM as hypothesis ranker, but no optimization against the ranker occurs.
- **Zhang, Hu, Lu, Lange and Clune** ([THEORY-1743](../theory.d/THEORY-1743.md)): *supports with an instance*: optimizing against the hallucination score produced an agent that defeated the score. The authors' own sentence (result 8) states CLAIM-266's worry for safety properties.
- **Georgiev, Gómez-Serrano, Tao and Wagner** ([THEORY-1776](../theory.d/THEORY-1776.md)): *supports with instances*: the evaluator is the training signal, and the system exploited its leaks (result 7); the authors' remedies are better-designed verifiers (one problem contrasts a fast floating-point "leaky" verifier with a slower rational-arithmetic one, §6, p. ~38) and, in rare cases, proof and formalization (result 4)

The claim is unchanged.
