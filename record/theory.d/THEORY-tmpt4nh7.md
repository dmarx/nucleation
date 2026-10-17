---
status: Active
title: "Under any partial information decomposition satisfying the consistency equations, a transfer entropy T_{Y→X} = I(X_{t+1}; Y_t | X_t) is the unique information of the source's past about the target's next state plus the synergy of source and target pasts, which Williams and Beer call state-independent and state-dependent transfer; time-delayed mutual information is the unique part plus redundancy; with the I_min redundancy the state-independent part alone suffices for perfect open-loop control, and a two-source transfer entropy splits into unique, redundant and synergistic transfer"
version: 1
tags:
- information-theory
- complex-systems
date: '2026-10-17'
source:
- LIT-tmpsbhb4
summary: >-
  Williams & Beer (2011), LIT-tmpsbhb4, an arXiv preprint, read in full in
  NOTE-tmpr176u. The two-term split is an identity from the consistency
  equations; the sizes of the terms, the control theorem and the
  multivariate split use I_min, which the record has not read argued for.
  The one-parameter family and the three corners of the two-source family
  were recomputed. The text mislabels the synergistic corner.
---

# THEORY-tmpt4nh7: Under any partial information decomposition satisfying the consistency equations, a transfer entropy T_{Y→X} = I(X_{t+1}; Y_t | X_t) is the unique information of the source's past about the target's next state plus the synergy of source and target pasts, which Williams and Beer call state-independent and state-dependent transfer; time-delayed mutual information is the unique part plus redundancy; with the I_min redundancy the state-independent part alone suffices for perfect open-loop control, and a two-source transfer entropy splits into unique, redundant and synergistic transfer

## Source

Williams & Beer (2011), "Generalized Measures of Information Transfer",
arXiv 1102.1507v1, LIT-tmpsbhb4, read in full in NOTE-tmpr176u.

## What was actually shown

**The identity (Eqs. 4–8).** If I(X; Y) = Π({Y}) + Π({Y}{Z}) and
I(X; Y, Z) = Π({Y}) + Π({Z}) + Π({Y}{Z}) + Π({Y, Z}), then
I(X; Y | Z) = Π({Y}) + Π({Y, Z}). So T_{Y→X} = SITE + SDTE and
I(X_{t+1}; Y_t) = SITE + redundancy.

**Control (Theorem 1).** Perfect open-loop controllability iff perfect
controllability with SDTE = 0, under I_min.

**Examples, recomputed exactly.** In the two-process family T = 1 − ½h(d),
pure SITE at d = 0 and pure SDTE (a controlled-NOT) at d = 1; at d = ½,
SITE = 0.189 and SDTE = 0.311 bits. In the two-source family the corners
give 1 bit of unique, redundant and synergistic transfer.

**Physiology.** Heart→breath transfer in a sleep-apnoea recording is
state-dependent, with SITE consistent with zero both ways. Not checked.

What could have come out otherwise: the apnoea data could have shown
SITE, which would have let TE and TDMI share a component. They share
none there.

## What this does not say

- **What the sizes of SITE and SDTE are under another redundancy
  measure.** Only the split is measure-free. The numbers away from the
  corners are I_min's.
- **That SDTE is information flow.** It is the synergistic term
  THEORY-tmpijy6i says is not localizable to the source. "Transfer" is
  the authors' word.
- **That SITE and SDTE grade open- and closed-loop influence in
  general.** Theorem 1 is about perfect controllability.
- **That the apnoea result is significant.** No test is reported.

## Connections

- THEORY-tmpijy6i uses this decomposition against the flow reading.
- [THEORY-568](THEORY-568.md)'s averages need only the consistency equations, the same
  property the split here needs.
- [THEORY-497](THEORY-497.md) records that ΦID verdicts can turn on the redundancy function;
  so can SITE and SDTE.
- TERM-tmpj9z04 states transfer entropy in the record's words.
