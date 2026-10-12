---
status: Active
title: 'The intertwining defects are defined on unobservable interpretive-state spaces, so they are not identified from judgement data, and the commutator identity bounds observed order effects only with a further, unstated readout-intertwining defect'
version: 2
history:
- version: 2
  date: '2026-10-10'
  note: >-
    Conceded on 2026-10-10. CLAIM-tmpfzcik bounds the observed order
    effect by observational distortions alone, and CLAIM-117 v2 is
    stated on observed responses.
role: counter
tags:
- mathematics
- philosophy-of-science
date: '2026-10-10'
line: pragmatic-transport
rests_on:
- CLAIM-046
objects_to:
- CLAIM-117
- CLAIM-063
undercuts:
- ARG-006
uses:
- TERM-007
summary: >-
  Found in the record's audit of the line on 2026-10-10 (formal lens); no
  turn of the exchange raises it. The commutator identity is correct, but
  Φ, A and A′ act on interpretive states. [CLAIM-046](CLAIM-046.md) says hidden-state
  models that give identical observations can differ, and a worked case
  shows two such models with defects 0 and the largest possible, so the
  defect is not a function of the data. What is observed is responses,
  and the identity reaches the observed order effect only through a
  readout defect between outcome spaces, which no draft names. It is
  distinct from [CLAIM-011](CLAIM-011.md), which is about collapse: this is about
  identification.
---
<!-- inactive-ok-file: CLAIM-117 CLAIM-063 — Proposed; open, and cited as the claims this objection is to -->
<!-- inactive-ok-file: CLAIM-046 CLAIM-127 — Proposed; the observational-equivalence claim this objection rests on and the causal layer it cites, open -->

# CLAIM-tmpvmzx9: The intertwining defects are defined on unobservable interpretive-state spaces, so they are not identified from judgement data, and the commutator identity bounds observed order effects only with a further, unstated readout-intertwining defect

## The objection

**The identity holds.** [CLAIM-117](CLAIM-117.md) gives the manuscript's §9: with
E_A = ΦA − A′Φ and E_B = ΦB − B′Φ,

Φ[A,B] − [A′,B′]Φ = E_A B + A′E_B − E_B A − B′E_A.

Re-derived: ΦA = A′Φ + E_A, so ΦAB = A′ΦB + E_A B = A′B′Φ + A′E_B + E_A B.
In the same way ΦBA = B′A′Φ + B′E_A + E_B A. Subtracting gives the
identity. For Markov operators on distributions, with the total-variation
norm, each of A, B, A′ and B′ has norm at most 1, so
‖Φ[A,B] − [A′,B′]Φ‖ ≤ 2(‖E_A‖ + ‖E_B‖).

**The defects are not identified.** A, A′ and Φ act on interpretive
states. [TERM-007](../terms.d/TERM-007.md): "Φ maps source interpretive states to target ones".
[CLAIM-046](CLAIM-046.md) says "different hidden-state models may produce identical
observations", and that fidelity "should be defined on observable
responses before any equivalence of internal states is assumed". Two
models that are equal on every observation can carry different defects.

A worked case. Take a target model with states S′, framing operators A′
and B′, readout O′, and a correspondence Φ with E_A = 0. Build a second
target model from it:

- its states are pairs (s′, b), with b a hidden bit;
- its operators act on s′ as before, and Ã′ also flips b;
- its readout ignores b;
- its correspondence is Φ̃(s) = (Φ(s), 0).

Every sequence of framings gives the same distribution of responses in
both models, because the readout never sees b. So the data cannot tell
them apart. But Φ̃Aμ puts b at 0, while Ã′Φ̃μ = (A′Φμ, b = 1) =
(ΦAμ, b = 1) puts it at 1. The two distributions have disjoint supports,
so they are at total-variation distance 1, the largest possible, for every
starting distribution μ. One model has defect 0 and the other the largest
defect there is. Choosing Φ̃(s) = (Φ(s), b uniform) instead would make the
defect 0 again. So the defect depends on the hidden-state model and on the
choice of Φ, and not on the data.

**The identity does not reach observed order effects.** What is observed
is a response distribution, not a state. In the source the observed order
effect is O[A,B]μ, with O the source readout. In the target it is
O′[A′,B′]Φμ. From the identity,

O′[A′,B′]Φμ = O′Φ[A,B]μ − O′(E_A B + A′E_B − E_B A − B′E_A)μ.

The first term equals the source's observed order effect only when
O′Φ = O. But O and O′ map to the response spaces of two different studies,
with their own questions and possibly their own languages. Even stating
the condition needs a correspondence of outcome spaces, a kernel K with
KO = O′Φ. That is the outcome-level transport ([CLAIM-tmp6xxbf](CLAIM-tmp6xxbf.md)) meeting the
state-level Φ. With E_O = O′Φ − KO,

‖O′[A′,B′]Φμ − K O[A,B]μ‖ ≤ ‖E_O [A,B]μ‖ + 2(‖E_A‖ + ‖E_B‖).

The readout defect E_O is a third defect. No draft names it.

The causal layer does not supply the missing step. [CLAIM-127](CLAIM-127.md): A129's
equations "have one step, so K_bK_a needs time-indexed states, which it
does not write". What can be estimated is a dynamical distortion stated on
observed responses: [TERM-043](../terms.d/TERM-043.md)'s D_dyn, "Differences in subsequent
interpretation and reconstruction trajectories".

**What it hits.** [CLAIM-063](CLAIM-063.md)'s defeat condition is stated on "measured order
effects", which are responses, and bounded by defects that are not. [ARG-006](../arguments.d/ARG-006.md)
infers from intertwining "each framing operation" to preserved
noncommutativity. Its first critical question, whether the premises hold,
cannot be answered from data, because the premises are about operators
the data do not identify.

This is not [CLAIM-011](CLAIM-011.md)'s point. [CLAIM-011](CLAIM-011.md) says an uninformative Φ makes
intertwining vacuous or lossy. Here Φ may be as informative as one likes,
and the defects are still not fixed by the observations.

## What it does not say

- It does not say the identity is wrong. It is algebra, and holds.
- It does not say dynamics do not matter for fidelity ([CLAIM-117](CLAIM-117.md)). It says
  the bound that would show it is stated in quantities the data do not
  identify.

## What would answer it

- [CLAIM-063](CLAIM-063.md)'s bound restated on observed responses, with an explicit
  readout term E_O and the outcome correspondence K that it needs.
- Or a result that the defects are identified under stated restrictions:
  for instance, a minimal-realization theorem for the model class, under
  which observationally equivalent models are related by a known
  equivalence that leaves the defect norms fixed.
