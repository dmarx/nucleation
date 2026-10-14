---
number: 180
status: Proposed
formerly:
- CLAIM-tmp7vmnc
title: 'Drift is retrieval failure outside a critical distance: a restatement close enough to an idea retrieves it, one that has drifted too far is taken for new, and a code bypasses retrieval by content altogether'
version: 2
history:
- version: 2
  date: '2026-10-14'
  note: >-
    After the reading of LIT-787 (NOTE-tmpzvsw5) and the copy hunt that
    left LIT-928 Unavailable. A Connections line adds Ashby's separate
    stores and similarity-driven interference. The text and inactive-ok
    comment note that Kanerva's book is Unavailable, so the
    critical-distance point stays unchecked against it. The claim is
    unchanged.
role: thesis
defeated_if: >-
  In the reconstructed exchanges, re-derivations "as though new" turn
  out not to be the restatements furthest from their originals: close
  paraphrases are re-derived as often as distant ones. Or coded items
  are re-derived about as often as uncoded ones, so that an address
  gives no protection that content does not.
tags:
- design-rationale
- epistemology
date: '2026-10-11'
line: nucleating-argument
works:
- luria-nucleating-an-argument
answers:
- QUESTION-038
rests_on:
- CLAIM-177
- CLAIM-182
grounds:
- LIT-269
- LIT-928
- LIT-918
- LIT-921
summary: >-
  Proposed by the assistant on 2026-10-11, when the owner raised sparse
  distributed memory and Hebbian learning after [CLAIM-182](CLAIM-182.md), and filed
  at the owner's request. It reads the drift of [CLAIM-177](CLAIM-177.md) through
  SDM's critical distance (read in [NOTE-242](../notes.d/NOTE-242.md)) and Hopfield's basins of
  attraction (unread when filed; read 2026-10-14 in NOTE-819). The analogy is the claim; whether restatement
  distance predicts re-derivation has not been measured.
---
<!-- inactive-ok-file: CLAIM-024 CLAIM-177 CLAIM-179 CLAIM-182 — Proposed; open, and cited as open: the theses and objections of the nucleating-argument line are under test, not settled -->
<!-- inactive-ok-file: ARG-004 — Rejected; cited as an analogy that came back after it was rejected, which is the point -->
<!-- inactive-ok-file: LIT-928 — Unavailable; Kanerva's book, no copy obtainable, named as where the critical distance comes from, not leaned on beyond that -->
<!-- inactive-ok-file: THEORY-tmp9yigf — Proposed; the account filed from LIT-787, named in Connections and not leaned on -->
<!-- inactive-ok-file: THEORY-272 — Proposed; the Hopfield account filed from LIT-918, cited for its corrections -->

# CLAIM-180: Drift is retrieval failure outside a critical distance: a restatement close enough to an idea retrieves it, one that has drifted too far is taken for new, and a code bypasses retrieval by content altogether

## The claim

In sparse distributed memory a cue retrieves a stored pattern only from
within a critical distance: "the largest query–target distance from which
iterated reads still converge to the target" ([NOTE-242](../notes.d/NOTE-242.md), reading
[LIT-269](../literature.d/LIT-269.md)). The critical distance comes from Kanerva's book ([LIT-928](../literature.d/LIT-928.md),
unread, and now Unavailable, so the point stays unchecked against the
book), not from Hopfield or from Kanerva's report ([LIT-921](../literature.d/LIT-921.md)), which has
only the signal-to-noise optimum ([NOTE-779](../notes.d/NOTE-779.md), 2026-10-14). Hopfield's
network ([LIT-918](../literature.d/LIT-918.md), read in [NOTE-819](../notes.d/NOTE-819.md)) has the same shape in
dynamical form. A cue inside a memory's basin of attraction settles into
it, and one outside settles elsewhere, possibly into a spurious state.

A collaborator with no memory retrieves by content. When an idea comes up
again, the only way to connect it to its earlier statement is that the
two read alike. A restatement close to the original is recognized as the
same idea. One that has drifted is taken for new, and re-derived. That is
the failure [CLAIM-177](CLAIM-177.md) records: the permissiveness objection re-derived
six or more times as though new, the passive/active distinction restated
without citation, the relativity analogy brought back after it was
rejected. Each restatement read differently enough that it was not
retrieved.

A code changes the retrieval. Pointing at [CLAIM-024](CLAIM-024.md) or [ARG-004](../arguments.d/ARG-004.md) does not
depend on rewording the idea closely enough to be recognized; the address
names it. That is why addressability, not storage, makes an anchor
([CLAIM-182](CLAIM-182.md)). Hopfield's model has no addresses. The contrast is in
Kanerva's report ([LIT-921](../literature.d/LIT-921.md), [NOTE-779](../notes.d/NOTE-779.md)): an SDM with radius zero and
complete addresses is an ordinary RAM, which returns exactly what was
written at an exact address and nothing for any other cue. Stored content can be reached only by a cue near it. An
addressed item can be reached by its name from anywhere.

Two further points follow from the models, both untested here:

- **Capacity.** A Hopfield network past its load develops spurious states
  and loses retrieval. A record that leans on content alone, with many
  near-duplicate statements, should show the same: merged and confused
  ideas. That bears on flooding ([CLAIM-179](CLAIM-179.md)).
  *Corrected 2026-10-14 ([NOTE-819](../notes.d/NOTE-819.md), [THEORY-272](../theory.d/THEORY-272.md)).* In Hopfield's
  model, fusion comes from two memories being close, closer than about a
  tenth of N, at any load. Overload does not merge memories: it loses
  every memory at once, unless old ones are forgotten. Spurious states
  occur far below capacity too. "Many near-duplicate statements" names
  the closeness failure, not the load one.
- **Silent redefinition.** A cue just outside one memory's basin can
  settle into a neighbouring memory. Read across, a restated term can be
  taken for a nearby, different term, and the argument continues on the
  wrong one without noticing.

## What it does not say

- It does not say a collaborator's memory is an SDM or a Hopfield network.
  The models give a precise picture of retrieval by content and its limit,
  and the claim uses that picture.
- "Taken for new" has no Hopfield analogue ([NOTE-819](../notes.d/NOTE-819.md)). The network
  never treats a cue as new: a cue far from every memory settles
  elsewhere, or, with a threshold, into a state that signals
  unfamiliarity. The nearest analogue of re-derivation is failing to
  recognise. Whether a duplicate is then written is outside the model.
- It does not say codes make retrieval free. A code must itself be
  remembered or found ([QUESTION-038](../questions.d/QUESTION-038.md)), and luria's generated views and
  indexes are how it is found.
- The test it proposes is not run. It needs a measure of how far a
  restatement is from its original, and the reconstructed exchanges
  give the cases to measure.

## Connections

- Ashby ([LIT-787](../literature.d/LIT-787.md), Ch. 16, S. 16/14; [THEORY-tmp9yigf](../theory.d/THEORY-tmp9yigf.md), read in
  [NOTE-tmpzvsw5](../notes.d/NOTE-tmpzvsw5.md)): separate stores for separate situations, with
  interference that grows with the similarity of the situations, because
  similar inputs use the same parts. Read across, a close restatement is
  the one most likely to overwrite its earlier form, the converse of this
  claim's concern that a distant one is taken for new. Both follow from
  retrieval by content, and a code avoids both. Analogy only.
