---
number: 205
status: Active
formerly:
- CLAIM-tmp6gb7c
title: 'Functional and relevance-theoretic accounts of translation, as Nida, Nord and Gutt state them, need not fix one context or a static stance profile of the rendering'
version: 3
history:
- version: 2
  date: '2026-10-28'
  note: >-
    Split under ADR-061. The title was "A win over the static pragmatic
    profile shows that context matters, not that the transport formalism
    contributes: functional and relevance-theoretic accounts need not fix
    one context, so the rival the incremental thesis must beat is a strong
    contextual baseline of rich context-response profiles and supervised
    prediction". The verdict on support is now ARG-031, from CASE-055
    to CLAIM-202, Proposed; this claim keeps what the rival accounts are
    committed to, and undercuts that argument in place of objecting to
    CLAIM-202.
- version: 3
  date: '2026-10-30'
  note: >-
    Narrowed and promoted at the status review's ruling (the owner
    delegated these rulings; ADR-057, ADR-047). The title was
    'Functional and relevance-theoretic accounts of translation need not
    fix one context or a static stance profile, so their strongest
    operationalization is a rich contextual baseline of context-response
    profiles and supervised prediction'. Its blocker note said what the
    rival accounts license rested on no reading. Nord's article
    (LIT-1863, NOTE-1448) and Nida's chapter (LIT-1864,
    NOTE-1451) are read in full, and Gutt's thesis (LIT-1845,
    NOTE-1435) is skimmed through its account of faithfulness. Each
    makes what a translation should keep relative to an audience, a
    purpose or a cognitive environment, and they join grounds. The
    dropped clause, the interlocutor's proposal for operationalizing the
    rivals, is CLAIM-504, Proposed (ADR-047's kind 2). The claim
    still undercuts ARG-031, which is Rejected in the same change.
role: counter
warrant: interpretive
tags:
- philosophy-of-science
- translation
- philosophy-of-language
date: '2026-10-12'
line: pragmatic-transport
grounds:
- LIT-1863
- LIT-1864
- LIT-1845
undercuts:
- ARG-031
summary: >-
  From the interlocutor's reading of PR [#121](https://github.com/dmarx/nucleation/issues/121) and its reconciliation,
  relayed by the owner on 2026-10-12. It accepts [CLAIM-202](CLAIM-202.md) as the
  line's principal empirical thesis and objects to its rival set.
  Narrowed and promoted on 2026-10-30, when Nida, Nord and Gutt were read;
  the baseline it proposed is CLAIM-504.
---
<!-- inactive-ok-file: ARG-031 — Rejected; the argument this claim undercuts, defeated by it -->
<!-- inactive-ok-file: CLAIM-202 — Proposed; cited as open positions and readings the interlocutor's reading addresses, not as settled -->
# CLAIM-205: Functional and relevance-theoretic accounts of translation, as Nida, Nord and Gutt state them, need not fix one context or a static stance profile of the rendering

## The objection

The reading endorses [CLAIM-202](CLAIM-202.md) "with one qualification": "The current comparison risks underestimating the competing theories by operationalizing them through relatively impoverished static ratings. A relevance-theoretic or functional account need not be committed to only one context or a static stance profile."

[CLAIM-202](CLAIM-202.md) compares three predictors: semantic similarity, the static pragmatic profile, and the transport structure. It justifies the second as the rival by saying that each rival account "fixes a profile of the rendering as read once". The reading denies that premise for relevance theory and proposes a fourth row between the static profile and the transport model: a "strong contextual baseline" of "rich context-response profiles, supervised predictive methods".

"What matters is whether transport structure adds predictive or explanatory power over the strong contextual baseline, not merely over static pragmatic judgments. Otherwise, an empirical victory may establish that context matters without establishing that the transport formalism makes a distinctive contribution."

## What would answer it

The incremental thesis restated against a strong contextual baseline, specified in advance, with the margin fixed as [CLAIM-202](CLAIM-202.md) already requires. Or an argument that the static profile is the strongest rival the functional and relevance-theoretic accounts license. [QUESTION-074](../questions.d/QUESTION-074.md) names the test the reading takes to be distinctive of the formalism.

## What it does not say

It does not say the transport structure will fail the stronger test, or that [CLAIM-202](CLAIM-202.md) should not be the principal empirical thesis. The reading favours making it so.

It does not say every such account varies context. Gutt's direct translation fixes one, the cognitive environment envisaged for the original (p. 254).

## Note of 2026-10-28: split under [ADR-061](../decisions.d/ADR-061.md)

The old title said both what a win would show and what the rival accounts
are committed to. The first is a verdict on support, and is now
[ARG-031](../arguments.d/ARG-031.md), from [CASE-055](../cases.d/CASE-055.md) to [CLAIM-202](CLAIM-202.md), form evidence, Proposed, with
"An empirical victory may establish that context matters" as its answer to
"does it tell the hypothesis apart from its rivals?". This claim keeps the
second, and undercuts that argument. The text above is unchanged.

## Note of 2026-10-30: the accounts read, and narrowed

Nord ([LIT-1863](../literature.d/LIT-1863.md)) translates for "a particular target audience from
among various possible audiences" (p. 17), and the brief decides between
instrumental and documentary translation (pp. 26–27). Nida ([LIT-1864](../literature.d/LIT-1864.md))
makes the translation depend on the message, the purposes and an audience
that varies in decoding ability and interest (pp. 127–128), and calls the
rules "probabilistic" (p. 134). Gutt's thesis ([LIT-1845](../literature.d/LIT-1845.md)) makes
faithfulness "determined for each occasion by the principle of relevance
and the cognitive environment mutually shared" (p. 63). None fixes a
profile of the rendering as read once. None proposes an
operationalization, so the old title's second clause moves to
[CLAIM-504](CLAIM-504.md).
