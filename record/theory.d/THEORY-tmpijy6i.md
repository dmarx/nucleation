---
status: Active
title: "Transfer entropy is not a measure of information flow, if flow means information in the target attributable solely to the source's past: as a conditional mutual information it equals the source's unique information plus its synergy with the target's past, so it can credit a full bit to a source that carries none alone (Y_t = X_{t−1} ⊕ Y_{t−1}) and report zero from each of two sources that jointly fix the target (Z_t = X_{t−1} ⊕ Y_{t−1}); conditioning on further series, as causation entropy does, has the same fault"
version: 1
tags:
- information-theory
- complex-systems
- causality
date: '2026-10-17'
source:
- LIT-tmpa6og3
summary: >-
  James, Barnett & Crutchfield (2016), LIT-tmpa6og3, read in full in
  NOTE-tmpt2aw8. Both examples are exact and were recomputed. The
  decomposition holds for any PID satisfying the consistency equations.
  The conclusion is relative to the authors' definition of flow; transfer
  entropy as predictive improvement is untouched. The claims about
  directed information, interventional flow and Gaussian systems are
  cited or conjectured.
---

# THEORY-tmpijy6i: Transfer entropy is not a measure of information flow, if flow means information in the target attributable solely to the source's past: as a conditional mutual information it equals the source's unique information plus its synergy with the target's past, so it can credit a full bit to a source that carries none alone (Y_t = X_{t−1} ⊕ Y_{t−1}) and report zero from each of two sources that jointly fix the target (Z_t = X_{t−1} ⊕ Y_{t−1}); conditioning on further series, as causation entropy does, has the same fault

## Source

James, Barnett & Crutchfield (2016), "Information Flows? A Critique of
Transfer Entropies", arXiv 1512.06479v2 (Phys. Rev. Lett. 116, 238701),
LIT-tmpa6og3, read in full in NOTE-tmpt2aw8.

## What was actually shown

**Flow, defined.** Information in Y_t whose cause "can be solely
attributed to X's past" (p. 1).

**Overestimate.** X_t, Y_0 fair bits, Y_t = X_{t−1} ⊕ Y_{t−1}:
T_{X→Y} = 1 bit, while I[Y_t : X_{0:t}] = I[Y_t : Y_{0:t}] = 0 and
I[Y_t : Y_{0:t} | X_{0:t}] = 1. Read one way X's past predicts Y_t, read
the other way Y's past does. The co-information is −1. Recomputed: the
I_min PID gives 1 bit of synergy and nothing else.

**Underestimate.** X, Y fair bits, Z_t = X_{t−1} ⊕ Y_{t−1}:
T_{X→Z} = T_{Y→Z} = 0 and every pairwise information is 0, while
C_{X→Z|(Y,Z)} = C_{Y→Z|(X,Z)} = 1. Recomputed.

**Why.** I[X₁ : Y | X₂] = U₁ + S. Transfer entropy, with the source's past
as X₁ and the target's past as X₂, is unique plus synergistic information.
Conditioning removes redundancy and adds synergy; it is not subtraction.

What could have come out otherwise: Example 1's bit could have been
attributable to one past. It is not, under any PID, because XOR with
independent uniform inputs is pure synergy for every proposed redundancy
measure.

## What this does not say

- **That transfer entropy is wrong as a measure of predictive
  improvement.** The authors say they "do not object" to it as the
  reduction in uncertainty about one series given another. [THEORY-641](THEORY-641.md)
  and THEORY-tmp0xaeq stand.
- **That X has no causal influence on Y in Example 1.** Intervening on
  X_{t−1} changes Y_t. The failure is in localizing the bit to X, not in
  detecting X's influence. That is the record's observation (NOTE-tmpt2aw8),
  and it is separate from CLAIM-tmp6nu4a's point about intervention.
- **How much of a transfer entropy is synergy outside the XOR case.** That
  depends on the redundancy measure, and none is agreed.
- **That directed information or Ay and Polani's interventional flow fail
  the same way.** The first is asserted from its being "essentially a sum
  of transfer entropies"; the second is a conjecture.
- **That unique information measures flow.** Proposed, not shown.

## Connections

- Williams and Beer (2011, THEORY-tmpt4nh7) give the same decomposition
  and call the synergistic part state-dependent transfer. The two accounts
  agree on the mathematics and disagree on whether that part is
  "transfer".
- [THEORY-497](THEORY-497.md)'s ΦID decomposes past→future information into source and
  target atoms, which is the kind of tool that would separate the parts
  this account says transfer entropy conflates.
- [THEORY-257](THEORY-257.md)'s dynamical independence uses transfer entropy from the whole
  micro history at once. Example 2 shows why the pairwise version would
  not do. The record's inference.
- TERM-tmpj9z04 states transfer entropy in the record's words;
  CLAIM-tmpu9ivq is the record's position.
