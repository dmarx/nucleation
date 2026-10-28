---
number: 298
status: Proposed
formerly:
- CLAIM-tmp9snb1
title: A frame can change a judgement by changing which of an interpreter's stored
  distinctions are reachable, without supplying any evidence about what is being
  judged
version: 2
history:
- version: 2
  date: '2026-10-16'
  note: >-
    Grounds add THEORY-697, the SDM–attention correspondence filed from
    LIT-269 in the THEORY backfill, with its local window and fitted
    temperature. The claim is unchanged.
role: thesis
warrant: interpretive
defeated_if: >-
  A design whose measure of retrieval is first shown sensitive (it detects direct
  priming), which holds memory and evidence fixed, varies a frame, and finds judgements
  shift while what is retrieved does not, across the communicative tasks the line
  studies. Harris et al. (2019) found a judgement shift with no detected retrieval
  change, but with a measure that also missed direct priming, so it does not meet
  this condition.
tags:
- cognition
- pragmatics
- information-retrieval
date: '2026-10-15'
line: pragmatic-transport
rests_on:
- CLAIM-315
grounds:
- LIT-269
- THEORY-335
- THEORY-697
complements:
- CLAIM-199
- CLAIM-117
summary: >-
  A20's proposed claim, after the owner tied addressing to anchoring at U20, and
  A19's "addressing conditions". Its psychological form is the selective-accessibility
  account of anchoring, and the readings of 2026-10-15 weaken it: Strack and Mussweiler
  (1997, read) infer accessibility from moderations and latencies without measuring
  it, and their model lets the same retrieved knowledge push a judgement either
  way; Harris et al. (2019, read) find the most direct measure of the accessibility
  step does not replicate and cannot detect priming at all. The retrieval step is
  inferred, not shown. The mechanism the record holds, attention as sparse distributed
  memory ([LIT-269](../literature.d/LIT-269.md)), is a model, not evidence about judges. The extension to communication
  in general is the record's and is not shown.
bears_on:
- QUESTION-096
---
<!-- inactive-ok-file: LIT-1078 — Unavailable; held without a reading, cited for what it would be read for, not leaned on -->
<!-- inactive-ok-file: CLAIM-117 CLAIM-184 CLAIM-199 — Proposed; open claims and accounts cited as open, nothing here rests on their being settled -->

# CLAIM-298: A frame can change a judgement by changing which of an interpreter's stored distinctions are reachable, without supplying any evidence about what is being judged

## The claim

A20 §1: with memory M, evidence E and a cue q(E, a) that an anchor a
helps set, the judgement is J = δ(Retrieve(M, q(E, a)), E). "The anchor
can change the judgment without adding any valid evidence about the
target." A19 §6: "communication changes not only what information a
receiver is given, but the addressing conditions under which existing
information becomes recoverable."

The psychology is not new, though its retrieval step is inferred rather than measured (note of 2026-10-15). Strack and Mussweiler ([LIT-1064](../literature.d/LIT-1064.md)) and Mussweiler and
Strack ([LIT-1078](../literature.d/LIT-1078.md)) hold that considering an anchor makes anchor-consistent
knowledge more accessible to the later judgement. A20: "The new
contribution we might pursue isn't 'anchoring affects retrieval.'" What
is the record's is placing it in the pragmatic-transport line: a
rendering's effect on a receiver includes what it makes reachable, not
only what it carries.

The record holds the mechanism A19 reached for. [LIT-269](../literature.d/LIT-269.md) (Bricken and
Pehlevan, read in [NOTE-242](../notes.d/NOTE-242.md)) shows attention approximates Kanerva's sparse
distributed memory, so a change of query changes what is read out from an
unchanged store.

## What it bears on

- [CLAIM-199](CLAIM-199.md): usable information is relative to the rules a receiver can
  apply. This adds the cue that selects which apply.
- [CLAIM-117](CLAIM-117.md): A20 §6 noted that if a frame changes what is accessible,
  frame A then B may differ from B then A, "a possible mechanism for order
  effects". It "does not, by itself, establish noncommutativity in the
  specific empirical sense proposed by the claim."
- [CLAIM-184](CLAIM-184.md): an anchor that is easy to reach is reached often.
  "accessibility is not the same as warrant."

## What it does not say

Not that all anchoring is selective accessibility. A20 named
insufficient adjustment and response effects as rival pathways, and said
they need not exclude one another.

## Note of 2026-10-15: what the anchoring readings leave standing

Three readings bear on the psychological form this claim cites.

- **Strack and Mussweiler 1997** ([LIT-1064](../literature.d/LIT-1064.md), [NOTE-877](../notes.d/NOTE-877.md)). With the
  anchor number fixed, the anchor's effect depended on what the comparison
  made available and whether it applied to the later judgement. But no
  study measures retrieval. And their model has two stages: accessibility
  is "not sufficient to guarantee its use and determine the direction of
  its influence", and Study 2 turned the same activated knowledge into
  contrast. So a frame acts on retrieval and on evaluation, and these
  designs do not separate the two. The defeat condition is restated so
  that it does not assume they can be.
- **Harris et al. 2019** ([LIT-1067](../literature.d/LIT-1067.md), [NOTE-876](../notes.d/NOTE-876.md)). Five preregistered
  replications (N = 128 each) of Mussweiler and Strack's lexical-decision
  test of accessibility found large anchoring and no accessibility effect,
  and the same tasks failed to detect direct picture priming. The authors
  conclude the method is unfit as a test, not that the theory is false,
  and that the earlier evidence from it "is not a strong part of the
  evidence base". Their leading account of durable anchoring is a
  provisional answer formed at the comparison and recalled later, which
  sits exactly on this claim's unresolved split: if the carrier is a
  recalled number, the frame acts on what is answered, not on what is
  reachable.
- **Mussweiler and Strack 1999** ([LIT-1078](../literature.d/LIT-1078.md)) could not be fetched.

The claim stays Proposed. Its psychological form is a theory with
indirect support, and the communicative extension rests on it.

## Note of 2026-10-15: split under [ADR-043](../decisions.d/ADR-043.md)

[ADR-043](../decisions.d/ADR-043.md)'s pilot found this claim compound: an empirical claim about
anchoring in judgement tasks, and the record's interpretive extension to
communication in general. The empirical half is now [CLAIM-315](CLAIM-315.md), on
which this claim rests, and this claim is marked interpretive. Its title
already states the general form, so it was kept; what changed is that its
psychological support is a separate claim with its own warrant and
standing.
