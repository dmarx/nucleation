---
number: 697
status: Proposed
formerly:
- CLAIM-tmps7g72
title: 'A learned system''s disposition to succeed at a task is resource-conditional: the admissible ways of eliciting it are largely the affordable compositions of declared operations, so its best success probability is a nondecreasing function of the budget over nested procedure classes; repeated sampling raises a frozen model''s chance that some attempt succeeds from p to 1 − (1 − p)^N with no change to its parameters; and that coverage is not delivery, which needs a selector that recognizes success, so generation, recognition and selection are separate capacities with separate costs'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  A case in which a nested family of admissible procedures yields a best
  success probability that falls as the budget grows, where the extra
  budget can be left unused; or one in which coverage under repeated
  sampling equals delivered accuracy without any selector; or a reading of
  TERM-118 under which a disposition's declared family of conditions
  already includes its resource budget, so that the claim adds nothing.
tags:
- learning-theory
- agency
- operations-research
- anthology-candidate
date: '2026-11-15'
line:
- realizability
- learned-structure
uses:
- TERM-118
complements:
- CLAIM-576
- CLAIM-567
grounds:
- THEORY-1894
summary: >-
  The owner's, from the continuation of the exchange "Explain String
  Theory" (2026-11-15), answering A's condition that a retained capability
  must be realizable under "a declared family of interventions": "isn't
  this family effectively supplied (at least partially) by normal
  constraints of resource boundedness?" And: "there's also a useful
  difference between a model's likelihood of producing an answer when
  sampled once vs if we commit a lot of compute to test time inference ...
  Dispositions can be resource conditional." A's formalization (A25)
  supplies the envelope, the coverage formula and the split between
  generation, recognition and selection, rechecked on filing
  (scratch/formal/reconstruction_channel_checks.py). A's qualification is
  kept: the budget selects affordable compositions, but it does not fix
  the primitive operations or the system's boundary. The idea is the
  owner's; the wording is A's, and adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-754 — Proposed; cited in this filing of 2026-11-19 -->
<!-- inactive-ok-file: CLAIM-576 TERM-118 THEORY-1894 — Proposed or new; the claim this extends, the term it uses, and the claim filed beside it -->

# CLAIM-697: A learned system's disposition to succeed at a task is resource-conditional: the admissible ways of eliciting it are largely the affordable compositions of declared operations, so its best success probability is a nondecreasing function of the budget over nested procedure classes; repeated sampling raises a frozen model's chance that some attempt succeeds from p to 1 − (1 − p)^N with no change to its parameters; and that coverage is not delivery, which needs a selector that recognizes success, so generation, recognition and selection are separate capacities with separate costs

## The claim and its demonstration

Let 𝒪 be the declared primitive operations: sampling, continuing a
reasoning trace, scoring candidates, calling a permitted tool. Let
Π_B = {π ∈ Comp(𝒪) : C(π) ≤ B} be the affordable procedures. The best
success probability is

    𝒞(B) = sup_{π ∈ Π_B} S(π).

- **Monotone envelope.** If Π_{B₁} ⊆ Π_{B₂} whenever B₁ ≤ B₂, because
  extra budget may go unused, then 𝒞(B₁) ≤ 𝒞(B₂). A particular procedure
  need not improve with more compute; the envelope does.
- **Coverage without new parameters.** With independent attempts at
  per-attempt success p, P(at least one success in N) = 1 − (1 − p)^N. At
  p = 0.01 that is 9.6% at N = 10, 63.4% at 100 and 99.3% at 500. About 299
  attempts are needed for 95% coverage (rechecked).
- **Coverage is not delivery.** A correct answer among N candidates is
  delivered only if something selects it. For a binary verifier with
  true-positive rate t and false-positive rate f, the precision of an
  accepted candidate is pt / (pt + (1 − p) f), which is poor when p is
  small. So generation, recognition and selection are separate capacities.

The empirical anchor is Brown et al.'s repeated sampling
([THEORY-1894](../theory.d/THEORY-1894.md)). There, coverage on SWE-bench Lite rose from 15.9% at one sample to
56% at 250, judged by the benchmark's own unit tests. That figure is
coverage, not what an unaided selector delivers.

## What it changes

- **[TERM-118](../terms.d/TERM-118.md).** The term asks for "a declared family of conditions". For a
  learned system, that family is largely the affordable compositions of
  declared operations. A disposition can be practically absent at one
  budget and reliable at another, with nothing about the system changed.
- **[CLAIM-576](CLAIM-576.md).** A frozen model's repertoire is indexed by inference
  resources as well as by architecture. A budget can make a process
  affordable without making a new one possible.
- **[CLAIM-567](CLAIM-567.md).** Coverage under a sampling budget is reachability.
  Delivery at a threshold is reliable attainment.

## What it does not say

- **That nonzero probability is a capability.** With unlimited sampling a
  softmax model emits almost any string. Without a selector, a guess that
  happens to be right is not competence. A: "Nonzero generation
  probability is not sufficient evidence of meaningful task competence."
- **That the budget defines the whole family.** The primitive operations
  and the system boundary are declared separately. A model with a web tool
  is a different system from the model alone, and its achievements belong
  to the composite.
- **That any information supplied at test time is illegitimate.** Content
  derived during inference counts, and content retrieved from outside does
  not count as retained. The provenance of each must be stated ([CLAIM-118](CLAIM-118.md)).

## Note of 2026-11-19: the exchange "Topological protection explained"

(a) At U27 the owner said Large Language Monkeys "takes this in the other direction" from test-time training, and that the PASS@(k,T) paper "ties in here as well", both "filed as read on Nucleation". They are: [LIT-2622](../literature.d/LIT-2622.md) (this claim's anchor, [THEORY-1894](../theory.d/THEORY-1894.md)) and [LIT-2441](../literature.d/LIT-2441.md). (b) A60 §4 and A71 §1 add in-context learning and test-time training to sampling and tool interaction as declared operations on this claim's disposition, alternative ways to spend a budget on one outcome. The record holds the parts: [CLAIM-118](CLAIM-118.md) (context and interpreter), [THEORY-169](../theory.d/THEORY-169.md) (conditioning as a learning step) and [THEORY-439](../theory.d/THEORY-439.md) (test-time updates beat conditioning on the same demonstrations).

(c) A71 §1 introduced this claim's construction, a supremum over affordable procedures of delivered, not merely sampled, success, with "Our theory needs a richer object", and only then said it is "closely aligned" with this claim. It is this claim, the owner's idea. (d) A73 carries coverage against delivery to knowledge: a correct response once in 10,000 samples is "Evidence of generative reach, not by itself knowledge" ([QUESTION-493](../questions.d/QUESTION-493.md)). (e) [CLAIM-754](CLAIM-754.md) takes this claim's set of tasks reliable within a budget as its operational frontier.

No status change.
