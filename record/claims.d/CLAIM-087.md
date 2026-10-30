---
number: 87
status: Proposed
formerly:
- CLAIM-tmpovy47
title: 'Cross-modal reconstruction often improves a receiver''s access to an implicit communicative relation beyond the text-only baseline, as when posture or expression conveys solidarity better than the source text''s literal content, though a rendering made without the situation is a garbling and cannot improve what an ideal receiver could do'
version: 3
history:
- version: 2
  date: '2026-10-10'
  note: >-
    Restated on 2026-10-10 after CLAIM-238 and CLAIM-225.
    Version 1's title read: 'Cross-modal reconstruction can improve
    access to an implicit communicative relation, as when posture or
    expression conveys solidarity better than the source text's
    literal content', and its condition: 'In text→image→text chains,
    judged access to the source's interpersonal relation never rises
    above the text-only baseline at any stage.' The improvement is to
    a receiver's usable information (CLAIM-199); version 1's
    'never rises … at any stage' was a universal negative.
- version: 3
  date: '2026-10-19'
  note: >-
    Title restated on 2026-10-19 by the promotion audit, batch 034
    (ADR-047). Version 2 made the defeat condition a prevalence test
    after CLAIM-238 but left the title saying "can improve", which
    one item settles and no rate defeats. The first clause now
    states the prevalence the condition tests; the garbling bound
    (CLAIM-225) and the defeat condition are unchanged. Version 2's
    title began: 'Cross-modal reconstruction can improve a
    receiver's access to an implicit communicative relation, as
    when'. Status and warrant unchanged.
role: thesis
warrant: interpretive
defeated_if: >-
  In text→image→text chains whose captioners are blind to the source's
  situation, the share of items on which receivers' task-indexed access
  to the source's interpersonal relation rises above the text-only
  baseline by more than a margin fixed in advance is no greater than a
  rate fixed in advance.
tags:
- compositionality
- probabilistic-modeling
- philosophy-of-language
date: '2026-10-08'
line: pragmatic-transport
summary: >-
  A97 §6 and A100 §11.10, recovered. The manuscript treats a change of
  medium only as a risk to relational fidelity (§7), though §11 allows
  that an adapted receiver may recover an implicit relation.
complements:
- CLAIM-076
- CLAIM-199
objected_by:
- CLAIM-238
rests_on:
- CLAIM-225
---
<!-- inactive-ok-file: CLAIM-105 — Proposed; open, and cited as open: the claim, argument or reading is under test, not settled -->
<!-- inactive-ok-file: CLAIM-199 — Proposed; the reconciliation this restatement follows, cited as open -->

# CLAIM-087: Cross-modal reconstruction often improves a receiver's access to an implicit communicative relation beyond the text-only baseline, as when posture or expression conveys solidarity better than the source text's literal content, though a rendering made without the situation is a garbling and cannot improve what an ideal receiver could do

## The claim

A97 §6: a cross-modal chain may improve as well as degrade; "an image might
convey solidarity through posture or facial expression more effectively than the
source text's literal content alone." A100 §11.10 kept it as "visual realization
improving access to an implicit relation".

## Where it went

Manuscript §7 frames the medium change as where "relational fidelity is
indispensable" and a generator can fail "precisely the higher-order
communicative constraint". The opposite possibility is not stated. It bears on
[QUESTION-012](../questions.d/QUESTION-012.md), and it is the cross-modal case of [CLAIM-105](CLAIM-105.md)'s reverse: a transport that
adds a distinction.

## Note of 2026-10-15: split under [ADR-043](../decisions.d/ADR-043.md)

[ADR-043](../decisions.d/ADR-043.md)'s full classification found this claim compound: the
improvement of a receiver's access through an image is a hypothetical
example with an empirical test proposed and none run, which is
interpretive, while the bound in its last clause, that a rendering made
without the situation is a garbling and cannot improve what an ideal
receiver could do, is demonstrated. That bound is already stated and
derived in [CLAIM-225](CLAIM-225.md) (Active, demonstrated): with a generator whose
channel T(v | u) does not depend on the situation z, P(V | Z) is T
applied to P(U | Z), so by Blackwell's theorem the image is no better
than the text for any bounded decision problem about the situation. No
new claim was drafted. No relation was added either: [CLAIM-225](CLAIM-225.md) already
rests on this claim, so this claim cannot rest on it without a cycle,
and the two are already linked. This claim keeps the improvement for a
given receiver as its conclusion, with the bound as the condition that
scopes it, and its warrant stays interpretive. The title is kept.

## Note of 2026-10-19: the title restated as prevalence

The promotion audit's batch 034 found the title's first clause behind
its own defeat condition. Since version 2 the condition tests the share
of items on which access rises above the text-only baseline by a margin,
after [CLAIM-238](CLAIM-238.md). The title still said reconstruction "can" improve
access, which one item settles. It now says "often", and "beyond the
text-only baseline", which is what the condition measures. The bound in
the last clause still scopes it: the improvement is for a given receiver
([CLAIM-199](CLAIM-199.md)), never past what an ideal receiver could do ([CLAIM-225](CLAIM-225.md)). The
warrant stays interpretive, because no chain has been run.

## Note of 2026-10-27: rests on [CLAIM-225](CLAIM-225.md)

The status review of this date ([ADR-057](../decisions.d/ADR-057.md)) found the dependence the body's note on a cycle worried about running one way only. [CLAIM-225](CLAIM-225.md) does not need this claim, and its dilemma holds either way. This claim's garbling bound uses [CLAIM-225](CLAIM-225.md)'s result, so it now rests on [CLAIM-225](CLAIM-225.md).

## Note of 2026-10-30: what holds it back

The first clause is a prevalence, "often", and no text→image→text chain
has been run: [CASE-009](../cases.d/CASE-009.md) is stipulated, and [CASE-062](../cases.d/CASE-062.md)'s documented gains are
on content probes, not on the interpersonal relation. The defeat
condition's margin and rate are still not fixed ([CLAIM-238](CLAIM-238.md)), so even a
chain that was run could not yet meet or miss it.
