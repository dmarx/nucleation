---
number: 732
formerly:
- CLAIM-tmpi68s2
status: Proposed
title: 'A protected objection is effective only if six achievements hold together, its becoming formulable, legible, taken up by an authorized channel, sustainable by the objector, corrected and maintained, so an objection can fail at any of them while its formal standing is unchanged, its chance of success is no greater than that of its weakest stage, and a reform that raises one stage''s success can lower the whole'
version: 2
history:
- version: 2
  date: '2026-11-18'
  note: >-
    Carries rightful-power after its own line(s) under ADR-085, taking
    part in its argument: bears_on QUESTION-480. No other change.
role: thesis
warrant: interpretive
defeated_if: >-
  A case of an effective objection in which one of the six achievements
  failed, showing it unnecessary; or an argument that two of them cannot
  fail apart, so that the decomposition counts one achievement twice; or a
  showing that reforms of complaint channels cannot in practice raise one
  stage's conditional success while lowering another's, so that the
  composition failure is a formal possibility with no instances. Not
  defeated by the arithmetic, which holds for any events; the claim is
  about which events an objection needs.
tags:
- society-and-governance
- probabilistic-modeling
- agency
date: '2026-11-17'
line:
- dependence-and-domination
- will-organization
- rightful-power
rests_on:
- CLAIM-523
complements:
- CLAIM-403
- CLAIM-632
- CLAIM-724
uses:
- TERM-092
- TERM-085
bears_on:
- QUESTION-480
summary: >-
  A's, A79 §10 of the exchange "Assess Depp Heard Abuse" (2026-11-16), "The
  lifecycle of a protected objection", sharpened A81 §2 and §9
  (2026-11-17) and proposed for the record in A81 §14 as "Distributed
  failure of effective objection". [CLAIM-523](CLAIM-523.md) holds three achievements a
  discrepancy needs to change what an organization does; this extends them
  upstream to formulation ([CLAIM-475](CLAIM-475.md), [TERM-092](../terms.d/TERM-092.md)) and downstream to the
  objector's sustaining the process and the correction's maintenance
  ([CLAIM-422](CLAIM-422.md)). The bound is [CLAIM-632](CLAIM-632.md)'s upper bound for a reserve; the
  composition failure is A81 §9's numbers, checked. A's further
  "Adversarial control over contestability" is [TERM-124](../terms.d/TERM-124.md) restricted to
  contest and is not filed apart. The wording is A's; adopting it is the
  owner's call.
---
<!-- inactive-ok-file: CLAIM-632 TERM-124 TERM-086 CLAIM-686 — Proposed; the record's nearest entries, cited with their standing -->
<!-- inactive-ok-file: CLAIM-724 TERM-130 — filed from the same exchange, Proposed or new -->

# CLAIM-732: A protected objection is effective only if six achievements hold together, its becoming formulable, legible, taken up by an authorized channel, sustainable by the objector, corrected and maintained, so an objection can fail at any of them while its formal standing is unchanged, its chance of success is no greater than that of its weakest stage, and a reform that raises one stage's success can lower the whole

## The claim

A79 §10 of the exchange "Assess Depp Heard Abuse"
(https://chatgpt.com/share/6afcb46d-83a8-83e9-9c85-4a0c3604405b) treats
"the entire lifecycle of a justified objection as an organizational
process", with six events for a corrective objective J under a justified
standard N: F, the objection is formulable within available resources;
L, it is legible and receives uptake; A, an authorized channel can act on
it; S, the challenger can sustain the process; R, a fitting correction
becomes effective; M, the correction or capability is maintained. By the
chain rule, exactly and with no independence assumed (A81 §2: "This
factorization is exact for the defined events and conditioning; it does
not assume independent stages"),

    Pr(F ∩ L ∩ A ∩ S ∩ R ∩ M) = Pr(F) Pr(L | F) Pr(A | F, L) ··· Pr(M | F, L, A, S, R).

Since effective correction needs all six, its probability is at most the
least of Pr(F), …, Pr(M). A81 §2: "**The reliability of the complete
corrective process cannot exceed the reliability of any genuinely
necessary component.**"

A81 §9 gives a composition failure, with stipulated conditional
probabilities. Arrangement A: 0.8, 0.8, 0.9, 0.8, 0.8, 0.9, product
0.3318. Arrangement B, an easier reporting system with heavier
documentation: 1.0, 0.9, 0.9, 0.35, 0.8, 0.9, product 0.2041 (both
rechecked). B is better at formulation and legibility and worse overall:
"The institution could accurately report improved complaint access while
its actual capacity to correct justified grievances has deteriorated."

The claim: these six are separate achievements each of which an
objection needs; any can fail while the others and the objector's
standing hold; the weakest bounds the whole; and a change that improves
one can lower the product. The arithmetic is immediate. What is claimed is
the decomposition, and that reforms of the kind in A81 §9 occur. A81 §9:
"What requires empirical investigation is whether a particular reform
produces those changes."

## How it sits with the record

- **[CLAIM-523](CLAIM-523.md)** (Active): legibility, volitional efficacy and
  correctability. L is legibility; A and R split volitional efficacy and
  correctability between the authorized channel and the correction. This
  claim adds F, S and M.
- **[CLAIM-475](CLAIM-475.md)** (Active, the owner's) and **[TERM-092](../terms.d/TERM-092.md)**: formulating a
  question is itself a resource-bounded realization. F is that, for an
  objection. A79 §2 draws the link; it is noted on [CLAIM-475](CLAIM-475.md).
- **[CLAIM-403](CLAIM-403.md)** (Active): admission, recognition, credibility, uptake and
  revision of standards are separable. It is the same staging inside one
  inquiry; this claim follows an objection through to remedy.
- **[CLAIM-422](CLAIM-422.md)** (Active): a corrective act, a procedure and a maintained
  capacity differ. M is the last of these.
- **[CLAIM-632](CLAIM-632.md)** (Proposed) bounds a reserve's readiness between the sum of
  its capacities' probabilities less n − 1 and the weakest. The upper
  bound is the bottleneck here.
- **[TERM-086](../terms.d/TERM-086.md)** (Proposed): A81 §2 cites it for "Corrective adequacy is a
  property of the organized sequence of capabilities".
- **[CLAIM-686](CLAIM-686.md)** (Proposed) and **[TERM-124](../terms.d/TERM-124.md)** (Proposed): A79 §10's
  "Adversarial control over contestability", an actor's capacity to
  influence any of the six stages, is [TERM-124](../terms.d/TERM-124.md)'s domination restricted to
  contest. It is not filed as a separate term. Its robust measure is
  [CLAIM-724](CLAIM-724.md); the institutional property built on it is
  [TERM-130](../terms.d/TERM-130.md).

## What it does not say

- Not that success is the only metric. A81 §2: "A properly rejected,
  unfounded objection can demonstrate an adequate adjudicative process
  even though the requested remedy is not obtained."
- Not that the stages occur in this order in every institution. A79 §10:
  "formulation, recognition, and intervention can overlap, and one stage
  may feed back into an earlier one."
- Not that influence over a stage is wrongful. A79 §10: "That capacity is
  not necessarily wrongful."
