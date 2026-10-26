---
number: 125
status: Active
formerly:
- CASE-tmpdc0tl
title: 'A hidden governance bit: an output that is fresh fair noise whatever a fixed hidden bit K is, until an intervention h makes the output read K, so the output alone is exactly informationally closed under ordinary operation and keeps nothing about the response to h'
version: 2
history:
- version: 2
  date: '2026-10-21'
  note: >-
    From the readings of 2026-10-21 of the causal-abstraction papers:
    the case also separates governance-response sufficiency from exact
    transformation and τ-abstraction (CLAIM-399). The case is
    unchanged.
standing: fictional
kind: construction
tags:
- causality
- information-theory
- self-governance
date: '2026-10-21'
line: will-organization
illustrates:
- CLAIM-122
- CLAIM-407
- CLAIM-409
summary: >-
  A16 §3–4 of the exchange of 2026-10-20, from A15 §2's deterministic
  form, and A17's Proposition 1. A fair hidden bit K, fixed in time; under
  ordinary operation the output Y is fresh fair noise; under the
  intervention h = 1 it reads K. The output is exactly closed, and with
  h = 1 drawn with probability ρ its deficiency for the response to h is
  ρ bits, no better than a constant. It is the first instance with
  parameters of [CLAIM-122](../claims.d/CLAIM-122.md)'s supervisory test, which the exchange of
  2026-10-17 gave only in words. Fictional by construction; K is a
  mechanism parameter, not an agent's governance.
supports:
- CLAIM-407
- CLAIM-399
variants:
- CASE-tmpwxgtj
---
<!-- inactive-ok-file: CLAIM-122 — Proposed; the will paper's claim this case illustrates, open, and the case bears no weight for it -->
<!-- inactive-ok-file: CLAIM-336 — Proposed; named as the test this case cannot be, open -->

# CASE-125: A hidden governance bit: an output that is fresh fair noise whatever a fixed hidden bit K is, until an intervention h makes the output read K, so the output alone is exactly informationally closed under ordinary operation and keeps nothing about the response to h

## The case

A16 §3: "Let an underlying system have a hidden governance type K ∈ {0,1},
and an observable output Y_t ∈ {0,1}." K is a fair bit, fixed in time and
independent of the output. Under ordinary operation (h = 0),
Y_{t+1} = U_{t+1}, with U fresh fair noise. Under the intervention h = 1,
Y_{t+1} = K. The micro state is S_t = (K, Y_t), and the behavioural
description keeps Z_t = Y_t.

A15 §2's deterministic form is the same case without the noise. Two systems
have proposals u₁ = 0 and u₂ = 1, with authority held by operator 1, and an
authorization input h that in the first system transfers authority to
operator 2 and in the second is disconnected: "Their ordinary behavioral
laws can be identical, while P(Y=1 | do(h=1)) differs." Under h = 0 both
output 0; under do(h = 1) the first outputs 1 and the second 0. That is
Y = K, with K the bit "h is connected".

Computed exactly on 2026-10-21, from the joint law of (K, Y_t, h, Y_{t+1}):

- **Closure under ordinary operation.** I(S_{≤t}; Y_{t+1} | Y_{≤t}) = 0
  with one, two and three steps of history.
- **The deficiency** Γ(T) = I(S; Y′ | T(S), h) ([CLAIM-407](../claims.d/CLAIM-407.md)), with h = 1
  drawn with probability ρ independently of S:

  | ρ(h = 1) | T = Y_t | T = constant | T = K | T = (K, Y_t) |
  |---|---|---|---|---|
  | 0 | 0 | 0 | 0 | 0 |
  | ¼ | 0.25 | 0.25 | 0 | 0 |
  | ½ | 0.5 | 0.5 | 0 | 0 |
  | 1 | 1 | 1 | 0 | 0 |

  A16's "Γ = ½(0) + ½(1) = 0.5 bits" is the row ρ = ½.

## What it can show

That a description exactly closed under a process's ordinary dynamics can
keep nothing about the response to an intervention on the mechanism. The
behavioural description does no better than the trivial one for that
target (Γ(Y_t) = Γ(constant)), and K alone suffices (Γ(K) = 0). That is
[CLAIM-122](../claims.d/CLAIM-122.md)'s supervisory test ("Hold the competing action proposals fixed,
intervene on the governance relations, and measure whether the operative
action changes"), with numbers. It meets the condition the exchange of
2026-10-17 set itself for [QUESTION-086](../questions.d/QUESTION-086.md)'s pair, "explicit parameters and a
full input-output equivalence argument for the selected observational
regime", for a stipulated hidden parameter. It is a case where [QUESTION-093](../questions.d/QUESTION-093.md)'s
predictive and interventional autonomy come apart. It is also a
refinement chain, constant ⪯ Y_t ⪯ (K, Y_t), on which Γ falls 0.5, 0.5, 0,
as [CLAIM-409](../claims.d/CLAIM-409.md) says it must.

It also separates governance-response sufficiency from causal abstraction
as Rubenstein et al. and Beckers and Halpern define it. Written as a
structural model with interventions on h only, dropping K is an exact
transformation and a τ-abstraction, and its approximate-abstraction
distance is 0, because the coarse model's noise can carry K
([THEORY-848](../theory.d/THEORY-848.md), [THEORY-849](../theory.d/THEORY-849.md), [THEORY-843](../theory.d/THEORY-843.md)); the coarse state still
keeps nothing of the response to h ([CLAIM-399](../claims.d/CLAIM-399.md)).

What it cannot show, given its standing:

- **Not agency or will.** A16: "Nor does the example establish agency.
  \(K\) is simply a hidden mechanism parameter." [CLAIM-116](../claims.d/CLAIM-116.md) holds.
- **Not a measure of anything about the system.** The 0.5 bit is set by the
  declared ρ.
- **Not self-governance.** It does not tell self-maintained from externally
  maintained governance, so it does not answer [QUESTION-086](../questions.d/QUESTION-086.md) or
  [QUESTION-092](../questions.d/QUESTION-092.md). The intervention separates the pair only because the
  hidden difference was stipulated to be the mechanism it acts on.
- **Not [CLAIM-336](../claims.d/CLAIM-336.md)'s test.** A15 offered the construction as that claim's
  "next substantive test". It has no meaning state, so it cannot show the
  joint prediction [CLAIM-336](../claims.d/CLAIM-336.md)'s `defeated_if` asks for.
- **Not ergodic.** (K, Y) is stationary, but K never changes. [THEORY-820](../theory.d/THEORY-820.md)
  needs stationarity only.
