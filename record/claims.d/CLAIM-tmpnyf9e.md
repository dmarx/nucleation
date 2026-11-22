---
status: Proposed
title: 'A nucleus that repairs the constraint of its own formation without producing it cannot free that constraint from outside supply while any damaged constraint is lost: the outside supply then equals the loss, so repair divides the supply needed by 1 + ρN/λ and lengthens survival after withdrawal, but never to independence, while producing the constraint anew can close the loop'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-093, from the
    runs of CASE-tmpy4orj.
role: thesis
warrant: demonstrated
defeated_if: >-
  A system in which a constraint is damaged at a positive rate, its
  damaged form is lost at a positive rate λ, nuclei restore damaged
  constraint to intact and produce none, nothing else produces it, and
  the constraint nonetheless persists at a positive level with no outside
  supply. Or, for the factor, a steady state of the repair arm of
  CASE-tmpy4orj where the supply needed differs from k_T T/(1 + ρN/λ) by
  more than the integration error. Not defeated by a system whose
  damaged constraint is never lost (λ = 0), which the claim excludes, nor
  by repair that costs material, which changes the factor and not the
  conclusion.
tags:
- complex-systems
- individuation
- mathematics
date: '2026-11-22'
line:
- transient-support
- distributed-agency
grounds:
- CASE-tmpy4orj
corroborates:
- CLAIM-597
- CLAIM-516
bears_on:
- QUESTION-399
summary: >-
  [QUESTION-399](../questions.d/QUESTION-399.md) asks for a nucleus that produces or repairs the
  constraints of its own formation. In the repair arm of [CASE-tmpy4orj](../cases.d/CASE-tmpy4orj.md) the
  two come apart. Repair only conserves what was supplied, so supply must
  match the loss. Production adds to the stock, so it can replace the
  supply. The wording is the assistant's (Claude, in this session);
  adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-tmpy4orj — new; the run this claim is drawn from -->

# CLAIM-tmpnyf9e: A nucleus that repairs the constraint of its own formation without producing it cannot free that constraint from outside supply while any damaged constraint is lost: the outside supply then equals the loss, so repair divides the supply needed by 1 + ρN/λ and lengthens survival after withdrawal, but never to independence, while producing the constraint anew can close the loop

## The claim

**The repair arm.** Let the intact constraint T be damaged at rate k_T
into D. D is lost at rate λ unless a nucleus restores it, at rate ρND.

**The argument.** The total T + D then changes as σ − λD. In steady state
the outside supply σ equals the loss λD. If σ = 0 the total can only fall
while D > 0, and the nucleus formed on it goes too. With T held at the
level that keeps N nuclei, the steady state gives

    σ = k_T T / (1 + ρN/λ),

against k_T T with no repair.

**The runs.** In [CASE-tmpy4orj](../cases.d/CASE-tmpy4orj.md) they reproduce the formula within
2 × 10⁻⁴ (e6).

- **The supply needed.** At λ = 0.05 and N = 2 it falls from 0.115 to
  0.0385, 0.0128, 0.0028 and 0.0004 at ρ = 0.05, 0.2, 1 and 5.
- **Survival after withdrawal.** The time for N to halve rises from 13 to
  25, 48, 163 and 735.
- **The production arm.** There, nuclei make new teachers from material,
  and the loop closes with no outside teacher below a turnover of 0.19.

**Why it matters.** This is [CLAIM-597](../claims.d/CLAIM-597.md)'s split for the constraint
rather than the parts: repair from outside supply frees an organization
from its founding but not from its feeding. It is also [CLAIM-516](../claims.d/CLAIM-516.md)'s
point that a constraint persists only through a productive cycle. A cycle
of repair is not one.

## What it does not say

- **Repair is not useless.** Where loss is slow (small λ) or repair is
  strong, the supply needed can be tiny and survival long, perhaps longer
  than any horizon that matters.
- **No loss is a different case.** Where damage is fully reversible
  (λ = 0), a repaired constraint is conserved and needs no supply. That is
  conservation, not closure.
