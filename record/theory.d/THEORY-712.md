---
number: 712
status: Active
formerly:
- THEORY-tmpt4nh7
title: "Under any partial information decomposition satisfying the consistency equations, a transfer entropy T_{Y→X} = I(X_{t+1}; Y_t | X_t) is the unique information of the source's past about the target's next state plus the synergy of source and target pasts, which Williams and Beer call state-independent and state-dependent transfer; time-delayed mutual information is the unique part plus redundancy; with the I_min redundancy the state-independent part alone suffices for perfect open-loop control, and a two-source transfer entropy splits into unique, redundant and synergistic transfer"
version: 2
history:
- version: 2
  date: '2026-10-17'
  note: >-
    Connections: the split under I_ccs (THEORY-714), unchanged for the coupled pair, a third value for the bystander example.
tags:
- information-theory
- complex-systems
date: '2026-10-17'
source:
- LIT-1176
summary: >-
  Williams & Beer (2011), [LIT-1176](../literature.d/LIT-1176.md), an arXiv preprint, read in full in
  [NOTE-942](../notes.d/NOTE-942.md). The two-term split is an identity from the consistency
  equations; the sizes of the terms, the control theorem and the
  multivariate split use I_min, which the record has not read argued for.
  The one-parameter family and the three corners of the two-source family
  were recomputed. The text mislabels the synergistic corner.
supports:
- CLAIM-335
---


# THEORY-712: Under any partial information decomposition satisfying the consistency equations, a transfer entropy T_{Y→X} = I(X_{t+1}; Y_t | X_t) is the unique information of the source's past about the target's next state plus the synergy of source and target pasts, which Williams and Beer call state-independent and state-dependent transfer; time-delayed mutual information is the unique part plus redundancy; with the I_min redundancy the state-independent part alone suffices for perfect open-loop control, and a two-source transfer entropy splits into unique, redundant and synergistic transfer

## Source

Williams & Beer (2011), "Generalized Measures of Information Transfer",
arXiv 1102.1507v1, [LIT-1176](../literature.d/LIT-1176.md), read in full in [NOTE-942](../notes.d/NOTE-942.md).

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
  [THEORY-707](THEORY-707.md) says is not localizable to the source. "Transfer" is
  the authors' word.
- **That SITE and SDTE grade open- and closed-loop influence in
  general.** Theorem 1 is about perfect controllability.
- **That the apnoea result is significant.** No test is reported.

## Connections

- Under Ince's I_ccs ([THEORY-714](THEORY-714.md)) the coupled pair is again unchanged.
  Harder, Salge and Polani's bystander example gives a third value at
  d = 0.75, 0.392/0.157, and a negative state-independent part at
  d = 0.25 ([NOTE-968](../notes.d/NOTE-968.md)).

- The coupled pair's split is the same under Harder, Salge and Polani's
  I_red ([THEORY-708](THEORY-708.md)) and Bertschinger et al.'s unique information
  ([THEORY-705](THEORY-705.md)), at every d checked. Elsewhere the split depends on
  the measure: in Harder, Salge and Polani's bystander example at d = 0.75
  it is 0/0.549 under I_min and 0.411/0.138 under I_red ([NOTE-944](../notes.d/NOTE-944.md)).

- [THEORY-707](THEORY-707.md) uses this decomposition against the flow reading.
- [THEORY-568](THEORY-568.md)'s averages need only the consistency equations, the same
  property the split here needs.
- [THEORY-497](THEORY-497.md) records that ΦID verdicts can turn on the redundancy function;
  so can SITE and SDTE.
- [TERM-057](../terms.d/TERM-057.md) states transfer entropy in the record's words.
