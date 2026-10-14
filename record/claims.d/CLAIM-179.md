---
number: 179
status: Proposed
formerly:
- CLAIM-tmp6b44r
title: 'When an agent does the filing, the cost of capturing argument falls on the party that would otherwise pay to re-derive it, which removes the disparity that design-rationale systems were abandoned over'
version: 2
history:
- version: 2
  date: '2026-10-14'
  note: >-
    After the readings of LIT-757 (NOTE-tmpdnj1q) and LIT-787
    (NOTE-tmpzvsw5). LIT-757 added to grounds beside the unread LIT-759. A
    note records Grudin's two qualifications: removing the disparity does
    not guarantee use, though the defeater names only the disparity, and
    his issue-based system was abandoned for political reasons (challenge
    3, not 1). Ashby's S. 20/10 added to the note on May as an earlier
    empirical version. LIT-760's seven issues remain unknown, the paper
    being Unavailable. The inactive-ok comments for LIT-930 and
    LIT-759–761 reworded from Deferred to Unavailable. The claim and its
    status are unchanged.
role: thesis
defeated_if: >-
  Agent-filed argument records are abandoned at rates like those of
  IBIS-era systems, for the reason Grudin gives: the people who must
  review, correct or read the record bear a cost that the people who
  benefit from it do not.
tags:
- design-rationale
date: '2026-10-11'
line: nucleating-argument
works:
- luria-nucleating-an-argument
answers:
- QUESTION-037
grounds:
- LIT-930
- LIT-757
- LIT-759
- LIT-761
- LIT-760
complements:
- CLAIM-176
summary: >-
  The answer to the cautionary literature the owner filed before the
  argument schemes were built ([ADR-030](../decisions.d/ADR-030.md)): design rationale goes uncaptured
  because whoever captures it is not whoever benefits. [ADR-032](../decisions.d/ADR-032.md) noted
  that agent filing changes the risk from capture stopping to capture
  flooding. This claim states why. Proposed: the record has run for one
  week.
---
<!-- inactive-ok-file: LIT-930 — Unavailable; no copy could be obtained, cited for what it is standardly cited for, and marked unread in the text -->
<!-- inactive-ok-file: CLAIM-185 — Proposed; open, and cited as open: the theses and objections of the nucleating-argument line are under test, not settled -->
<!-- inactive-ok-file: CLAIM-176 — Proposed; open, and cited as open: the theses and objections of the nucleating-argument line are under test, not settled -->
<!-- inactive-ok-file: LIT-759 LIT-760 LIT-761 — Unavailable; no copy could be obtained, cited for the argument ADR-030 summarises them for, not for a reading here -->
<!-- inactive-ok-file: THEORY-tmpefpin — Proposed; the disparity account filed from the reading of LIT-757, cited in a note and not leaned on -->

# CLAIM-179: When an agent does the filing, the cost of capturing argument falls on the party that would otherwise pay to re-derive it, which removes the disparity that design-rationale systems were abandoned over

## The claim

The design-rationale literature ([ADR-030](../decisions.d/ADR-030.md)) is largely an account of
why capture systems went unused. Grudin ([LIT-759](../literature.d/LIT-759.md), unread; [LIT-757](../literature.d/LIT-757.md), read) identified the disparity:
the work of capture falls on one person and the benefit goes to another.
Buckingham Shum and Hammond ([LIT-761](../literature.d/LIT-761.md)) and Lee ([LIT-760](../literature.d/LIT-760.md)) ask when capture
repays its cost.

A collaborator with no memory pays the rediscovery tax every session
([LU-ADR-001](https://github.com/dmarx/luria/blob/main/record/decisions.d/ADR-001.md)). When that same collaborator does the filing, capturing and
benefiting fall to the same party, and the capture is cheap because the
context is loaded at the moment of filing. Luria puts it this way: "Filed
with context loaded it costs a paragraph; re-derived cold it costs a
session" ([LU-DP-008](https://github.com/dmarx/luria/blob/main/docs/design-principles.md#dp-8)).

The disparity does not disappear. It moves. The owner now pays for reading
and correcting the record, rather than for writing it. That is why the
failure mode becomes flooding, and why the second-occurrence throttle
([CLAIM-176](CLAIM-176.md)) matters.

## What it does not say

- It does not say agent filing is accurate. Several workbench entries exist
  to correct what an assistant said about the record.
- It does not say the owner's review costs nothing. A week of operation is
  no evidence that the owner will keep reviewing.

## Note of 2026-10-11: flooding as unused anchors

Under the owner's reframing ([CLAIM-185](CLAIM-185.md)), the cost of capture is the
cost of making things persist, and flooding is persistence without use: a
code that no later entry points at. That makes over-capture measurable as
codes with no inbound references, beyond those that are new. Whether an
anchor goes unused because it was filed too eagerly, or because it is not
discoverable ([QUESTION-038](../questions.d/QUESTION-038.md)), the count alone cannot say.

## Note of 2026-10-11 (later): a size limit on settling

May ([LIT-930](../literature.d/LIT-930.md), unread here) is the classic result that a large system
with random interactions is almost surely stable only below a threshold,
s√(nC) < 1, in its size n, connectance C and interaction strength s. Past
it, more components or more links destabilize. Read across, flooding has a
second cost beyond unused anchors. A record that keeps adding entries and
relations could pass a point past which it no longer settles. The record's
structure is not random, and the debate after May is about which
structures escape the bound, so this is a question to test, not a result
to apply. It is also a further reason for the second-occurrence throttle
([CLAIM-176](CLAIM-176.md)).

*Added 2026-10-14 ([NOTE-tmpzvsw5](../notes.d/NOTE-tmpzvsw5.md)):* Ashby ([LIT-787](../literature.d/LIT-787.md), S. 20/10) is an
earlier, empirical version of May's result. Of random linear systems
sampled up to 4 × 4, the fraction stable fell roughly as 1/2ⁿ, and "large
linear systems should be assumed to be unstable". He also names the
escape: weak joining and many constancies. May ([LIT-930](../literature.d/LIT-930.md)) is now
Unavailable, so the bound is still cited unread.

## Note of 2026-10-14: what the founding paper and Hopfield's model say

- **IBIS reports adoption, not abandonment** ([LIT-758](../literature.d/LIT-758.md), read in
  [NOTE-811](../notes.d/NOTE-811.md)). The founding paper reports "eager acceptance by the
  users" and gives no account of what keeping an IBIS costs. Its operating
  cycle has staff edit issues "in contact with" the participant who raised
  them, so filer and arguer were already separate in the original design,
  as they are with an agent filer. That suggests the disparity Grudin
  describes may depend on who the filer is. It is one sentence of design,
  not evidence.
- **A capacity limit cuts the other way** ([LIT-918](../literature.d/LIT-918.md), read in
  [NOTE-819](../notes.d/NOTE-819.md)). In Hopfield's model spurious states occur at low load
  too, and overload is total loss: it "makes all memory states
  irretrievable unless there is a provision for forgetting old memories".
  Read across, a record past its load would lose access to its old
  entries rather than blur them. The record's rule, retire by status and
  never delete, is a provision against forgetting. This is analogy only.

## Note of 2026-10-14: what Grudin's read article adds

Grudin's 1994 article ([LIT-757](../literature.d/LIT-757.md), read in [NOTE-tmpdnj1q](../notes.d/NOTE-tmpdnj1q.md); [THEORY-tmpefpin](../theory.d/THEORY-tmpefpin.md))
states the disparity as the first of eight challenges, so the premise can
rest on a read paper and not only on the unread 1988 one ([LIT-759](../literature.d/LIT-759.md)). It
qualifies the claim twice.

- **Removing the disparity is not enough.** "Even a net benefit with equal
  costs and benefits for all users will not guarantee groupware success"
  (pp. 96–97): critical mass and freeloading, among others, can sink a
  system the disparity does not. The defeater above names only the
  disparity, so a record abandoned for another of Grudin's reasons would
  not defeat this claim, and would not be explained by it either.
- **The one issue-based system he cites failed for another reason.** It
  was abandoned before use because "the explicit record of opposing
  positions that the application would immortalize was politically
  unacceptable" (p. 97). That is challenge 3, social disruption, not
  challenge 1. It bears on a record that retires by status and never
  deletes.

What Lee's seven issues are ([LIT-760](../literature.d/LIT-760.md)) remains unknown here: the paper is
Unavailable.
