---
number: 462
status: Active
formerly:
- THEORY-tmp8bxd9
title: "If commonsense knowledge includes defaults that later evidence displaces, a monotonic logic, in which an added axiom can never remove a theorem, cannot represent that displacement as it stands; Minsky's further claim, that no logistic system, one that separates propositions from general laws of inference, can carry commonsense knowledge even once repaired, is asserted, not shown"
version: 2
history:
- version: 2
  date: '2026-10-30'
  note: >-
    Promoted by the twenty-fourth status review, at the status review's
    ruling (the owner delegated these rulings); ADR-065, ADR-057. The
    first clause holds by definition, and the body sets out the step. The
    second reports how the memo supports its further claim: "I think such
    attempts will continue to fail" (NOTE-337, C7). NOTE-337 read the memo
    in full, and nothing in the record contradicts either clause. The title
    now names the memo's own target, "logistic" systems, which separate
    propositions from general laws of inference. "Consistency-seeking
    logical system" ran C7's target together with C8's separate claim about
    consistency. That was an imprecise statement, and correcting it drops
    nothing (ADR-047, kind 3). The old title: If commonsense knowledge includes defaults that later evidence displaces, a monotonic logic, in which an added axiom can never remove a theorem, cannot represent that displacement as it stands; Minsky's further claim, that no consistency-seeking logical system can carry commonsense knowledge, is asserted, not shown. The old promote_when
    tested the further claim, which the title reports and does not assert:
    "A reading of the non-monotonic formalisms the critique motivated
    (default logic, circumscription and their successors), testing whether
    they represent the memo's cases, defaults displaced by later evidence,
    within a logical system with a stated consequence relation. If they do,
    the memo's further claim, that no logistic system can carry
    commonsense, is refuted, and the account narrows to its first half,
    which holds by definition. If each repair gives up what made the system
    logistic, the further claim is promoted. More examples of human
    inconsistency, or of stereotypes overridden by evidence, cannot settle
    it." The memo asserts the further claim, so it moves with that
    condition, word for word, to THEORY-1239, Proposed, which extends this entry
    (ADR-065 §3; ADR-047, kind 1).
tags:
- logic
- cognition
date: '2026-10-16'
source:
- LIT-410
summary: >-
  Minsky (1974), the frames memo, [LIT-410](../literature.d/LIT-410.md), read in [NOTE-337](../notes.d/NOTE-337.md). Its appendix
  argues that "logistic" systems fail for commonsense on five counts, of
  which monotonicity is a correct observation about classical logic. That
  no repair is possible is asserted ("I think such attempts will continue
  to fail"), and consistency being undesirable is argued by analogy. The
  reading says the memo is a source of hypotheses, not evidence; this
  account takes from it only the half that holds by definition and marks
  the rest as the memo's claim. Active as the definitional half and a
  report of how the memo supports the rest; the further claim is
  THEORY-1239, Proposed.
---
<!-- inactive-ok-file: LIT-334 — Unavailable; Gärdenfors's conceptual spaces, named as a neighbouring account, not leaned on -->
<!-- inactive-ok-file: THEORY-057 THEORY-541 — Proposed; accounts that cite the same memo, named in Connections, not leaned on -->

# THEORY-462: If commonsense knowledge includes defaults that later evidence displaces, a monotonic logic, in which an added axiom can never remove a theorem, cannot represent that displacement as it stands; Minsky's further claim, that no logistic system, one that separates propositions from general laws of inference, can carry commonsense knowledge even once repaired, is asserted, not shown

## Source

Minsky (1974), "A Framework for Representing Knowledge", MIT AI Memo 306,
[LIT-410](../literature.d/LIT-410.md), read in full in [NOTE-337](../notes.d/NOTE-337.md) from an OCR of the scan.

[NOTE-337](../notes.d/NOTE-337.md) says that no THEORY "cites or should cite this memo as evidence.
It is a source of hypotheses, not of support." This account is filed
`Proposed` under the owner's ruling for that case. It states only what the
reading itself supports: that the monotonicity point is "a correct
observation about classical logic" ([NOTE-337](../notes.d/NOTE-337.md), C7), and that the rest is
assertion.

## What was actually shown

**Defaults (§1.11).** A frame's terminals are never stored empty. They
carry "weakly bound default assignments" that new evidence displaces. The
memo argues for this from introspection and worked examples (the cube, the
room, the kite story), not from a program or an experiment (C1, weak).

**The appendix (§6).** "Logistic" systems, which separate propositions
from general laws of inference, fail for commonsense on five counts:
relevancy; **monotonicity**, "each added axiom means more theorems, none
can disappear"; procedure-controlling knowledge, illustrated by the
transitivity of "near"; combinatorial explosion; and consistency, which
"is not necessary or even desirable in a developing intelligent system".
Its one engaged target is McCarthy's Airport problem.

**What holds.** In a monotonic consequence relation an added premise never
removes a conclusion. A default displaced by later evidence is a
conclusion removed by an added premise. So such a logic, as it stands,
cannot represent displacement. That step is definitional, which is why
[NOTE-337](../notes.d/NOTE-337.md) rates the observation correct.

**What is claimed beyond it.** That no repair is possible: "I think such
attempts will continue to fail" (C7, moderate overall, the no-repair half
asserted). That consistency is undesirable, argued by analogy with human
inconsistency and the mathematician who "shall not take that step" (C8,
assertion).

## What this does not say

- **That commonsense knowledge is made of frames.** The frame account is
  the memo's hypothesis, with nothing built or measured, by its author's
  account ("Apology!", p. 2).
- **That logic cannot be repaired.** Non-monotonic logics were developed to
  do exactly this. The record holds no reading of them, so it does not say
  whether they succeed. That claim is [THEORY-1239](THEORY-1239.md), Proposed.
- **How strongly a default is bound.** The memo never says how much
  "strain" a match can bear or when a frame is given up, and it argues
  against numerical scores (§5.5; [NOTE-337](../notes.d/NOTE-337.md), Limitations).
- **That consistency is undesirable.** That is the memo's assertion.

## Connections

- **Context-shifted defaults, measured.** Aerts and Gabora's "pet"
  experiment ([LIT-340](../literature.d/LIT-340.md)) measures the context-shift of exemplar typicality
  that §1.11 builds into displaceable defaults. The memo predicts only the
  direction ([NOTE-337](../notes.d/NOTE-337.md), Bearing on the record; the pairing is that note's).
- **Family resemblance.** [THEORY-057](THEORY-057.md) cites the memo's similarity network
  (C5) for family resemblance without a definition.
- **Hand-coded representations.** Chalmers, French and Hofstadter
  ([THEORY-541](THEORY-541.md)) name frames among the formats whose filling is left
  unexplained.
- **The later programme.** Plain Talk ([LIT-399](../literature.d/LIT-399.md)), K-lines ([LIT-402](../literature.d/LIT-402.md)) and the
  jokes memo ([LIT-408](../literature.d/LIT-408.md)) build on the frame and its defaults.
  Gärdenfors's conceptual spaces ([LIT-334](../literature.d/LIT-334.md), Deferred) are the geometric
  alternative.
