---
number: 1008
status: Active
formerly:
- CLAIM-tmp2dr12
title: "Where inquiry of depth k must finish before execution can start within a deadline H, the chance of success p(k)F(H − t(k)) is greatest at an interior depth where the relative gain in finding a suitable response equals the time cost times the relative loss in execution readiness, so the appropriate depth of inquiry depends on the deadline and on the target's response dynamics"
version: 2
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the derivative or in the first-order condition; or a showing
  that, within the model's assumptions, the best depth does not depend on
  the deadline or on the execution-readiness curve F.
tags:
- operations-research
- epistemology
- probabilistic-modeling
date: '2026-11-23'
line:
- readiness
- learning-and-inquiry
bears_on:
- QUESTION-520
rests_on:
- CLAIM-475
- CLAIM-1157
uses:
- TERM-085
summary: >-
  A52 §2–3 of the exchange "Explain First Contact RL" (ChatGPT,
  2026-11-23). A toy model of the shared deadline: more inquiry raises the
  chance of finding a suitable response and lowers the time left to carry
  it out, so an interior depth balances the two. It models [TERM-085](../terms.d/TERM-085.md)'s
  "further search can have negative value". The derivative and the
  condition check (python3 -I); when the optimum moves with the deadline,
  and when it can jump down, is the assistant's [CLAIM-1203](CLAIM-1203.md). The
  wording is A's (ChatGPT, at A52 of the exchange "Explain First Contact
  RL"); adopting it is the owner's call.
history:
- version: 2
  date: '2026-11-25'
  note: >-
    Promoted to Active under the owner's delegation of 2026-11-24
    ("handle the fixes for the twelve ... use your best judgement"),
    as the status pass of 2026-11-24 and the reruns of 2026-11-25
    applied it to independently recomputed demonstrated claims. It was
    rerun by a session other than the filer's on 2026-11-25 (scratch/formal/maintained_nuclei_check.py;
    the curation entry of 2026-11-25 02:20) and reproduced; it was then
    held back only by CLAIM-1114, which the recomputation pass of
    2026-11-25 promoted. ADR-057: it rests on CLAIM-475 and CLAIM-1157, both Active (CLAIM-1157 promoted just before it); it uses TERM-085, Active; no objection targets it; and
    nothing meets its defeated_if.
---
<!-- inactive-ok-file: CLAIM-1070 — Proposed; the claim this rests on, the gap fill, the case filed with it and the claim whose phrase A uses -->

# CLAIM-1008: Where inquiry of depth k must finish before execution can start within a deadline H, the chance of success p(k)F(H − t(k)) is greatest at an interior depth where the relative gain in finding a suitable response equals the time cost times the relative loss in execution readiness, so the appropriate depth of inquiry depends on the deadline and on the target's response dynamics

## The worked example (A52 §2)

A correction must be done within ten days and takes five to carry out.

| Inquiry | Days specifying and investigating | Days left |
|---|---:|---:|
| Rapid | 2 | 8 |
| Extended | 6 | 4 |
| Exhaustive | 9 | 1 |

"Then the extended and exhaustive assessments can discover the correct
remedy yet fail to leave enough time to implement it." A52 adds that the
trade-off "is not strictly monotonic": a better query can find a faster
remedy and lower T_A by more than it raises T_Q.

## The model (A52 §3)

Depth k; p(k), the chance the inquiry finds a suitable response, rising in
k; t(k), its time, rising in k; F(h), the chance that a suitable response
can be carried out in the time h that remains. Then

P(k) = p(k) F(H − t(k)),

P′(k) = p′(k) F(H − t(k)) − p(k) F′(H − t(k)) t′(k),

and at an interior optimum where both factors are positive

p′(k)/p(k) = t′(k) F′(H − t(k)) / F(H − t(k)).

A52: "The proportional informational improvement from further inquiry must
justify the proportional loss of execution readiness caused by its time
cost." And: "It is a toy result, not a universal optimization law; real
inquiry and execution can overlap, interact, and change one another."

## Check

The assistant's, with python3 -I: with p(k) = 1 − e^(−k), t(k) = k and F
the normal distribution function with mean 3 and s.d. 0.7, the grid
maximizer of P at H = 4, 5, 6, 8, 10 and 14 satisfies the condition to
four decimals at every H (at H = 6: k* = 1.900, both sides 0.176). The
table's arithmetic checks.

## What it does not say

- Not where the optimum lies or how it moves. The condition is necessary
  for an interior maximum, not sufficient, and it can have several
  solutions. When the best depth rises with the deadline, and when a
  longer deadline makes a shallower inquiry best, is [CLAIM-1203](CLAIM-1203.md).
- A52 calls this "precisely the kind of relationship we've been calling
  *demand-appropriate temporal organization*". That is [CLAIM-1070](CLAIM-1070.md)'s
  phrase; the model is one instance of it, for the stage before a response
  can start.

## Note of 2026-11-25: rerun, and what holds it back

Rerun on 2026-11-25 by the assistant, a session other than the filer's, at the owner's word ("go ahead with the reruns"; the owner delegated on 2026-11-24 the promotion of demonstrated claims independently recomputed). The filer's script was not kept, so the check was rebuilt from this entry alone as `scratch/formal/inquiry_depth_check.py`, with a negative control, and run with python3 -I. Every computation reproduces. The table's days left are 8, 4 and 1, and only the rapid inquiry leaves the five days. The analytic P′ agrees with a central difference to 10⁻⁷. At H = 4, 5, 6, 8, 10 and 14 the maximizer satisfies the condition to four decimals (0.8602, 0.3897, 0.1759, 0.0362, 0.0073, 0.0003 on both sides), and at H = 6 the grid maximizer is k* = 1.900 with both sides 0.176, as stated. One precision: that k* = 1.900 implies a grid of 0.001, and at that grid's points themselves the two sides agree to within 0.001, not four decimals (0.8606 against 0.8599 at H = 4); the four decimals hold at the maximizer, which the rerun refines from the grid by golden section. The control, k away from the optimum, gives sides that differ by more than 0.05. What holds it back: [ADR-057](../decisions.d/ADR-057.md)'s first criterion. Its premise [CLAIM-1157](CLAIM-1157.md) is Proposed, and that is held by [CLAIM-1114](CLAIM-1114.md) ([CLAIM-475](CLAIM-475.md) is Active). Since the model uses [CLAIM-1157](CLAIM-1157.md) only for its sequential framing, a pass could also read the edge as a borrowed framing and make the claim conditional ([ADR-057](../decisions.d/ADR-057.md), "An inversion"); that is a pass's ruling, not this rerun's. The note is the assistant's (Claude, in this session). No status change.
