---
status: Proposed
title: "A three-state chain whose survivors settle in a few time units while all of them die out on a time a hundred times longer shows that stable statistics conditioned on survival come apart from persistence"
version: 1
form: existence
grounds:
- CASE-tmpyzdwh
concludes:
- CLAIM-tmp7cpzx
uses:
- TERM-071
tags:
- probabilistic-modeling
- complex-systems
- individuation
date: '2026-11-07'
line:
- distributed-agency
- formal-apparatus
summary: >-
  From A22 §5 of the exchange "Individuation, Possibility, and
  Disposition" (2026-11-06 to 07), answering the owner's U10. The
  inference from the quasi-stationary chain of [CASE-tmpyzdwh](../cases.d/CASE-tmpyzdwh.md) to
  [CLAIM-tmp7cpzx](../claims.d/CLAIM-tmp7cpzx.md). Proposed. The case is coherent: its numbers were
  rerun. It separates exactly what the claim's first part says comes
  apart, stationary and quickly reached survivor statistics against
  certain absorption. The claim's last clause, that the stable statistics
  are "no evidence" of persistence, is a little stronger than one case
  gives: the case shows their stationarity and speed do not vary with the
  hazard, while their values carry a trace of it of order ε/(8k). Filed at
  the owner's review of the filing, which asked for the ARGs it omitted.
  The model and its reading are A's (ChatGPT's). The wording is the
  assistant's (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-tmp7cpzx CASE-tmpyzdwh — filed from the same exchange, Proposed -->

# A three-state chain whose survivors settle in a few time units while all of them die out on a time a hundred times longer shows that stable statistics conditioned on survival come apart from persistence

## The inference

1. [CASE-tmpyzdwh](../cases.d/CASE-tmpyzdwh.md): a continuous-time chain on {A, B, D}. A and B exchange
   at rate k = 1, B fails into D at rate ε = 0.02, and "D has no outgoing
   transition under the model's specified dynamics."
2. Conditioned on survival, the law settles to the quasi-stationary
   distribution ν = (0.5025, 0.4975) on the mixing time, about 0.5, and
   is at ν to four places by t = 5 from a start in A.
3. Survival from ν decays as e^(−0.00995t), so absorption is certain and
   the mean lifetime is about 100.5.
4. So the survivors' statistics are stationary and quickly reached while
   absorption is certain ([CLAIM-tmp7cpzx](../claims.d/CLAIM-tmp7cpzx.md)).

## Critical questions

- **Is the case coherent?** Yes. It is a finite chain with an absorbing
  state reachable from every viable state, and its quasi-stationary
  distribution is the normalized left eigenvector of the generator
  restricted to {A, B}. The reader's script was rerun for this argument.
  It gives eigenvalues −0.00995 and
  −2.01005, ν = (0.50250, 0.49750), mean survival 100.502 and the ratio
  of extinction time to mixing time 21, 201 and 2001 for ε = 0.2, 0.02
  and 0.002, as the case states. The viable states form one communicating
  class, which is what makes ν unique and the convergence to it
  independent of the start.
- **Does it separate the very things the conclusion says can come
  apart?** For the claim's first part, exactly. The claim says the
  survivors' statistics can be stationary and fast while absorption is
  certain, and the case has both at once, with the two times differing by
  a factor of about 4k/ε that grows without bound as ε falls. It also
  separates what [CLAIM-079](../claims.d/CLAIM-079.md)'s note did not: the stationary object is a law
  over survivors, not a deterministic regime.

  The claim's last clause, "so a surviving organization's stable
  statistics are no evidence that it persists", needs more than a
  separation, since "no evidence" is a comparison across hazards. The
  case supplies most of it. Rerun for this argument with ε = 0, 0.002,
  0.02 and 0.2, the gap is 2.0 to 2.01 throughout, so the survivors'
  statistics are equally stationary and equally fast whether the chain
  persists forever (ε = 0) or dies in about a hundred time units. Their
  values are not quite the same: ν is (0.5, 0.5) at ε = 0, (0.5025,
  0.4975) at 0.02 and (0.5249, 0.4751) at 0.2. The deficit in ν_B is of
  order ε/(8k), so an observer who knew k and the hazard-free law could
  in principle read ε off ν. What the case shows is that stationarity and
  speed of settling are no evidence of persistence, and that the values
  are weak evidence at best. The claim's own "What it does not say" is
  close to this ("the hazard has to be estimated separately"). The title
  would be exact with "stable statistics" read as stationarity and speed,
  and not as the values of the distribution.

Proposed. The case is coherent and separates what the claim's first part
says comes apart. The last clause holds of stationarity and speed, and
only nearly of the values.

## What it does not show

- Anything about regeneration. Nothing leaves D, so A22 §5's
  "Regenerative persistence" needs another chain ([CLAIM-456](../claims.d/CLAIM-456.md)).
- That the separation holds when the hazard is comparable to the gap.
  Then the survivors die out before they settle, and the claim's "can be"
  is not met.
