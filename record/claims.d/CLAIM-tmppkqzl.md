---
status: Proposed
title: 'Where an inquiry keeps its sources and each step reads the stored source rather than the last restatement of it, re-reading is not a second route beside conservation but conservation on the state enlarged by the source; on that structure an interpretation does not drift but settles on a fixed offset from the source toward the reader''s prior, the same at every reading, which no reader sharing that prior can see, and drift is confined to the chains of derived texts'
version: 2
history:
- version: 2
  date: '2026-11-21'
  note: >-
    Restated in general terms at the owner's ruling of 2026-11-21 on the
    promotion pull request, asked whether the objection should stay a
    record-local instance of CLAIM-tmp1xigl: "general terms". The
    argument is unchanged; the record becomes one instance of an inquiry
    that keeps its sources. Version 1's title: "Re-reading a fixed source
    each time is not a second route beside conservation but the same one
    on the state enlarged by the source: the record anchors mainly by
    having each session read the stored entry, not by passing a
    restatement along a chain, and on that structure an interpretation
    does not drift but settles on a fixed offset from the source toward
    the reader's prior, the same at every reading, which no reader sharing
    that prior can see".
role: counter
warrant: interpretive
defeated_if: >-
  Either of two results. (a) An error in the augmentation: a step that
  re-injects a fixed input at every round and is not a chain with that
  input as an exactly conserved coordinate, or an interpretation step of
  the form given whose limit does not depend on the reader's prior. (b)
  Evidence, in an inquiry that keeps its sources (this record among
  them), that readings of a stored source by readers who share a framing
  disagree with each other as much as readings by readers who do not; or
  that its restatements mostly pass from restatement to restatement
  without the source being read, so that its anchoring is chain-like
  after all.
tags:
- epistemology
- design-rationale
- complex-systems
date: '2026-11-21'
line:
- records-of-inquiry
- pragmatic-transport
- nucleating-argument
- record-as-apparatus
objects_to:
- CLAIM-772
rests_on:
- CLAIM-635
- CLAIM-182
- CLAIM-191
grounds:
- THEORY-1161
- THEORY-960
summary: >-
  [CLAIM-772](CLAIM-772.md) models anchoring as a chain whose steps copy the source's
  features exactly, and sets aside Friedkin and Johnsen's re-injection of
  the start as a second route it does not cover. On the state enlarged by
  the source the two are one route. It is the route of any inquiry that
  keeps its sources, where each step goes back to the stored text, data
  or specimen rather than to the last account of it; this record, whose
  sessions read the stored entry, is one. For interpretation that changes
  the picture. A
  reading anchored this way does not random-walk away from the source; it
  settles on an offset toward the reader's prior, bounded and repeated at
  every reading. Raised in the owner's exchange of 2026-11-21 ("I'm not
  convinced we've got it quite right"). The wording is the assistant's
  (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-772 CLAIM-182 CLAIM-191 — Proposed; the claim objected to and the anchoring claims it rests on -->

# CLAIM-tmppkqzl: Where an inquiry keeps its sources and each step reads the stored source rather than the last restatement of it, re-reading is not a second route beside conservation but conservation on the state enlarged by the source; on that structure an interpretation does not drift but settles on a fixed offset from the source toward the reader's prior, the same at every reading, which no reader sharing that prior can see, and drift is confined to the chains of derived texts

## The objection

[CLAIM-772](CLAIM-772.md) treats the restatement of an entry as a chain, each session's
restatement a step applied to the last, and holds that the chain keeps
exactly what its steps copy without error. The objection is general: it
concerns any inquiry that keeps its sources. The record is the instance
that raised it. It sets aside Friedkin and
Johnsen's anchoring, which re-injects the start at every step
([THEORY-1161](../theory.d/THEORY-1161.md)), as "a second route … the claim does not cover". Three
points.

**1. The two routes are one.** Friedkin and Johnsen's step is
x(t+1) = ΛW x(t) + (I − Λ) u, with u = x(0). Enlarge the state to (x, u)
and let the step copy u exactly: u(t+1) = u(t). That is a chain with an
exactly conserved coordinate, [CLAIM-635](CLAIM-635.md)'s case, and the start is kept
because it is in the conserved coordinate. Conversely, a chain with a
conserved part re-injects that part into everything else at every step. So
re-injection is conservation on the state enlarged by the source, not
beside it.

**2. An inquiry that keeps its sources uses the enlarged structure.** A
laboratory rereads its notebook and reruns its stored samples; a court
reads the precedent, not the last brief's paraphrase of it; a scholar
returns to the edition. Each step takes the stored source (the conserved
coordinate) and produces a reading or a derived text from it. The topology
is a star around the source, not a chain from it. [CLAIM-182](CLAIM-182.md) says this from
another side: addressability, not storage, is what anchors, because an
address is what lets every step reach the source rather than the last
copy. The chains such an inquiry does have are its derived texts:
summaries, citations from memory, reviews, textbook restatements. Those
are where [CLAIM-191](CLAIM-191.md)'s drift should be looked for. In this record the
stored entry is read by each session, and the derived texts are its
summaries, titles quoted from memory, accounts and manuscripts.

**3. On that structure interpretation is offset, not drift.** Let a
reading y be formed from the text u and the reader's prior p, keeping a
share of any earlier reading:

y(t+1) = a·y(t) + b·u + c·p, with a + b + c = 1 and a < 1.

Its limit is y* = (b·u + c·p)/(b + c), at a distance c·|p − u|/(b + c) from
the source. For a reader with no memory of earlier readings (a = 0) it is
reached at once. So:

- The error is bounded and does not grow with the number of readings. This
  is what anchoring buys, and it is more than [CLAIM-772](CLAIM-772.md)'s table gives
  interpretation, which it places in the part copied with error, where a
  feature random-walks.
- It is not removed by reading again. It is zero only where the reader
  gives the prior no weight or the prior agrees with the source.
- It is the same at every reading by readers who share p. Their readings
  agree with each other and with themselves, so a check of consistency
  among them cannot find it. Stability is not fidelity, in a form that
  says which instrument can see the difference: a reader whose prior
  differs.

**A bearing.** The record's own recent work fits this. Two independent
fact-checks of the manuscript of 2026-11-20 found 9 and then 37 errors in
its restatements of coded entries, which the drafter had cited and read.
The audit of its ten principles struck six links, and each went beyond its
components in the same direction, toward a stronger or more general
statement than they make: an "only", an identification, a universal. That
is the direction of the drafter's thesis. These are derived texts, and the
errors were found by readers briefed independently. That is one study, not
a test.

**What it changes in [CLAIM-772](CLAIM-772.md).**

- Its carve-out of re-injection is the main case, not a side one.
- Its table's row for interpretation should say "offset toward the reader's
  prior, bounded" where readings return to the stored text, and "copied
  with error" only along chains of derived texts.
- Its defeater (a), that coded content read verbatim drifts as fast as
  uncoded content, cannot fire as stated: stored text read verbatim does
  not change at all. The test that can fire compares derived texts that
  cite coded entries with derived texts that do not.

## What it does not say

- Not that the record has no chains. Its derived texts are chains, and
  some of them copy text exactly, which [CLAIM-tmp0kqq4](CLAIM-tmp0kqq4.md) takes up.
- Not that the linear form of a reading is right. It is the simplest form
  in which the reader's prior enters; the point that a prior enters every
  reading, and so enters its limit, does not need it.
- Not that [CLAIM-772](CLAIM-772.md)'s identity of forgetting and anchoring as one
  contraction fails. This sharpens where the conserved part sits; it does
  not deny that there is one.

## Reframings

**2026-11-21, the owner on the promotion pull request.** Asked whether this objection should be restated in general terms or stay a record-local instance of [CLAIM-tmp1xigl](CLAIM-tmp1xigl.md): "general terms". Before: a claim about how this record anchors its entries. After: a claim about any inquiry that keeps its sources, with the record as the instance that raised it. The argument and its bearing are unchanged.
