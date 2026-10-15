---
status: Active
title: 'Within one fixed measurement scenario, two no-signalling empirical models can agree on all but one of their contexts and on every single-observable marginal while their contextual fractions are 1 and 0, so keeping most local judgement distributions does not fix their global compatibility'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the construction: a global distribution on {A, B, C} whose
  pairwise marginals are the parity triangle's (S_AB = S_BC = {(0,0), (1,1)},
  S_AC = {(0,1), (1,0)}, each allowed outcome at 1/2), or a failure of the
  modified model, with S_AC = {(0,0), (1,1)}, to extend to the distribution
  with 1/2 on (0,0,0) and 1/2 on (1,1,1). The claim is a construction, so
  only an error in it defeats it; the absence of such pairs in documented
  reconstruction chains does not.
tags:
- contextuality
- mathematics
date: '2026-10-15'
line: pragmatic-transport
grounds:
- CASE-037
- LIT-265
- THEORY-165
summary: >-
  Split from [CLAIM-105](CLAIM-105.md) under [ADR-043](../decisions.d/ADR-043.md): the possibility that claim's headline
  needs, shown by the pair it lost and recovered in [CASE-037](../cases.d/CASE-037.md). On the cover
  {AB, BC, AC} with binary outcomes, the parity triangle at 1/2 per allowed
  outcome is no-signalling and strongly contextual, with contextual
  fraction 1. Change only S_AC to {(0,0), (1,1)}: two contexts and every
  marginal are unchanged, and the model now extends to a global
  distribution, with fraction 0. It is an existence result by
  construction, and the weights are stipulated. It does not say
  reconstruction chains do this, which is [CLAIM-105](CLAIM-105.md)'s thesis and
  interpretive, and the context that changes moves by a total-variation
  distance of 1.
complements:
- CLAIM-tmp9fgji
supports:
- CLAIM-105
---
<!-- inactive-ok-file: CLAIM-105 — Proposed; the claim this was split from, cited as open -->
<!-- inactive-ok-file: THEORY-165 — Proposed; continuity of the contextual fraction, cited for what it implies here, not as settled -->
<!-- inactive-ok-file: CLAIM-201 — Proposed; the narrowing of CLAIM-105's headline, cited as open -->

# CLAIM-tmpbogw2: Within one fixed measurement scenario, two no-signalling empirical models can agree on all but one of their contexts and on every single-observable marginal while their contextual fractions are 1 and 0, so keeping most local judgement distributions does not fix their global compatibility

## The claim

This is the possibility [CLAIM-105](CLAIM-105.md)'s headline needs, stated on its own so
that its warrant can be. A78 asked: "Can communicative reconstruction
preserve most local pragmatic judgments while substantially changing their
global compatibility structure?" A84's planned Appendix F example was "Two
locally similar empirical models with different global compatibility".
The manuscript dropped it; [CASE-037](../cases.d/CASE-037.md) recovers it.

On X = {A, B, C} with the cover {AB, BC, AC} and binary outcomes, take the
supports S_AB = S_BC = {(0,0), (1,1)} and S_AC = {(0,1), (1,0)}, each
allowed outcome at 1/2. Every single-observable marginal is uniform, so
the model is no-signalling. No global assignment satisfies all three
supports, because A = B = C contradicts A ≠ C, so the model is strongly
contextual and its contextual fraction is 1. Change S_AC to
{(0,0), (1,1)}, still at 1/2 each. Two of the three contexts are
unchanged, and so is every single-observable marginal. The new model is
the marginal of the global distribution with 1/2 on (0,0,0) and 1/2 on
(1,1,1), so its contextual fraction is 0.

So within one scenario the fraction falls from 1 to 0 while most of the
local tables are kept. The two AC tables have disjoint supports, a
total-variation distance of 1 in that context, so the jump is consistent
with [THEORY-165](../theory.d/THEORY-165.md)'s Lipschitz bound: the fraction does not jump within a
fixed scenario, and here one context moved as far as it can.

## What it does not say

- That reconstruction chains, or pragmatic judgements, behave this way.
  The weights are stipulated ([CASE-037](../cases.d/CASE-037.md): "This parity example demonstrates
  an obstruction, not a claim about actual judgments"). That documented
  chains do so is [CLAIM-105](CLAIM-105.md)'s thesis, which is interpretive; [CLAIM-201](CLAIM-201.md)
  holds the form the data read so far leave open.
- That global compatibility can change at small local distortion
  everywhere. The pair keeps two contexts exactly and changes the third
  completely; by [THEORY-165](../theory.d/THEORY-165.md), within a fixed scenario a large change of
  the fraction needs a large change in some context.
- That the pair is one step of a transport. By Theorem 2 of [LIT-265](../literature.d/LIT-265.md) a
  free operation cannot raise the fraction, so the step from 0 to 1 is
  not a free operation, and Δ_CF is undefined at any step that signals.
