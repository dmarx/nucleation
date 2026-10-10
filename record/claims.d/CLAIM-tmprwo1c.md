---
status: Active
title: 'Under Contextuality-by-Default, a deterministic context-wise recoding can make a noncontextual signalling source maximally contextual, or turn a contextual source into pure signalling, so per-content signalling is not monotone under such maps and the quantity to bound is joint overlap discrepancy'
version: 1
role: granted
tags:
- contextuality
- mathematics
date: '2026-10-10'
line: pragmatic-transport
grounds:
- THEORY-174
- THEORY-177
- LIT-777
- LIT-851
objects_to:
- CLAIM-125
summary: >-
  Found in the record's audit of the line on 2026-10-10 (formal lens); no
  turn of the exchange raises it. Two worked rank-2 systems answer
  [NOTE-654](../notes.d/NOTE-654.md)'s open question negatively: [THEORY-177](../theory.d/THEORY-177.md)'s per-content
  signalling can rise under deterministic recodings, once the source
  signals, and CbD contextuality can be created or removed by them. By
  data processing, the joint overlap discrepancy cannot rise, so that is
  the quantity [CLAIM-125](CLAIM-125.md)'s second part should name. Granted, because the
  examples are elementary. It does not say [THEORY-174](../theory.d/THEORY-174.md) is wrong, which is
  about no-signalling models.
---
<!-- inactive-ok-file: CLAIM-125 — Proposed; open, and cited as the claim this objection is to -->
<!-- inactive-ok-file: THEORY-174 THEORY-177 THEORY-168 — Proposed; cited as the readings whose simulations, signalling measure and representation-dependence the examples use, not as settled -->
<!-- inactive-ok-file: CLAIM-105 — Proposed; cited for the reading of its headline these examples bear on, open -->
<!-- inactive-ok-file: CLAIM-tmpbvk4j — Proposed; a companion objection from the same audit, cited for its neighbouring point -->

# CLAIM-tmprwo1c: Under Contextuality-by-Default, a deterministic context-wise recoding can make a noncontextual signalling source maximally contextual, or turn a contextual source into pure signalling, so per-content signalling is not monotone under such maps and the quantity to bound is joint overlap discrepancy

## The objection

[CLAIM-125](CLAIM-125.md)'s second open part is how transport "extends to signalling
data". It proposes a quantity for it: "The paper also gives a quantity a
transport could be asked to preserve or bound ([THEORY-177](../theory.d/THEORY-177.md)). That quantity
is each content's least direct influence of context in a canonical causal
model, which equals the total-variation distance between the content's two
marginals. Whether classical simulations ([THEORY-174](../theory.d/THEORY-174.md)) can increase it is
not addressed by any work read here." [NOTE-654](../notes.d/NOTE-654.md) holds the same question
open: "Whether minimal direct influence, as a per-content total-variation
distance, is monotone under the simulations of [THEORY-174](../theory.d/THEORY-174.md)."

It is not monotone, and two small systems show it.

**The setting.** A rank-2 cyclic system has two contents, each measured in
both of two contexts c1 and c2, with values ±1. CbD's signalling is
Δ = Σ over contents of |⟨R⟩_c1 − ⟨R⟩_c2| ([THEORY-177](../theory.d/THEORY-177.md)), and a content's
share Δ* is half its term, the total-variation distance between its two
marginals. By the cyclic criterion of [LIT-777](../literature.d/LIT-777.md), as [NOTE-654](../notes.d/NOTE-654.md) states it for
rank 2, the system is contextual exactly when s_odd > Δ, where
s_odd = |⟨product⟩_c1 − ⟨product⟩_c2|, the difference of the two
contexts' correlations.

**The maps.** Each target content is computed by one deterministic
function of the source contents, the same function in both contexts. The
function reads only source contents measured together in that context.
These are the context-wise deterministic recodings that [THEORY-174](../theory.d/THEORY-174.md)'s
simulations are built from, applied to signalling data, which is the
extension [CLAIM-125](CLAIM-125.md)'s second part asks for.

**Creation.** Source contents q and r.

- In c1, q = +1 always, and r is +1 or −1 with probability 1/2 each.
- In c2, q = −1 always, and r is +1 or −1 with probability 1/2 each.

Then ⟨q⟩ is +1 in c1 and −1 in c2, ⟨r⟩ is 0 in both, so Δ = 2 + 0 = 2.
⟨qr⟩ is 0 in both contexts, so s_odd = 0, which is not greater than 2.
The source is noncontextual, and it signals.

Target contents x = r and y = q·r.

- In c1′, y = r = x, so ⟨xy⟩ = 1.
- In c2′, y = −r = −x, so ⟨xy⟩ = −1.

Both x and y are +1 or −1 with probability 1/2 in both contexts, so Δ = 0.
s_odd = |1 − (−1)| = 2 > 0. The target is CbD-contextual, with s_odd at
its largest possible value in rank 2. A deterministic recoding has created
contextuality.

**Conversion.** Source contents q and r, each +1 or −1 with probability
1/2 in both contexts.

- In c1, q = r.
- In c2, q = −r.

Then Δ = 0 and s_odd = |1 − (−1)| = 2 > 0. The source is contextual.

Target contents x = q·r and y = q.

- In c1′, x = +1 always, and y is +1 or −1 with probability 1/2.
- In c2′, x = −1 always, and y is +1 or −1 with probability 1/2.

⟨xy⟩ = x⟨y⟩ = 0 in both contexts, so s_odd = 0. Δ = |1 − (−1)| + 0 = 2,
and Δ*(x) = 1, the largest possible. The target is noncontextual and
signals as much as a content can. In this example per-content signalling
rose from 0 to 1 under the map.

**What does not rise.** In both examples the joint distribution of the two
source contents differs between the contexts at total-variation distance 1,
and so does the target's. The joint discrepancy is unchanged; only its
split between signalling and contextuality moved. That is general. If one
kernel K is applied to the jointly measured contents in both contexts, then
TV(K#P_c1, K#P_c2) ≤ TV(P_c1, P_c2), by data processing. For Proposition
1's natural kernel families, with τ(C) ∩ τ(F) = τ(C ∩ F), [CLAIM-121](CLAIM-121.md)'s checked
proof gives the target marginals on τ(D) as K_D applied to the source
marginals on D. So

TV(K_D#(e_C|D), K_D#(e_F|D)) ≤ TV(e_C|D, e_F|D):

the discrepancy on a mapped overlap cannot exceed the source's. The
quantity a transport can be asked to bound is this joint overlap
discrepancy, on sets of contents, not [THEORY-177](../theory.d/THEORY-177.md)'s per-content Δ*. The
recodings above read several contents at once, and per-content
consistency ignores that.

**What it bears on.** Any CbD reading of [CLAIM-105](CLAIM-105.md)'s headline, and of
[QUESTION-004](../questions.d/QUESTION-004.md)'s "measured contextual dependence", now depends on how
contents are coded. A chain step that only recodes can change both
measures. [CLAIM-tmpbvk4j](CLAIM-tmpbvk4j.md) raises the neighbouring question, whether
[CLAIM-105](CLAIM-105.md)'s headline is about contextuality at all.

## What it does not say

- It does not say [THEORY-174](../theory.d/THEORY-174.md) is wrong. Its results are for no-signalling
  models in the sheaf framework. The first source signals, and both
  systems are read under CbD, where two contexts can measure the same
  contents with different distributions; in the sheaf framework a context
  is a set of measurements, so two such contexts would be one.
- It does not say CbD is inconsistent. [THEORY-168](../theory.d/THEORY-168.md) already holds that its
  verdicts depend on how a system is represented. This adds that a
  recoding along a transport is one such change of representation.
- It does not close [CLAIM-125](CLAIM-125.md)'s second part. It says which quantity is
  monotone, not how transport between scenarios extends to signalling
  data.
