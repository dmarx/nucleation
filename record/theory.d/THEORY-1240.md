---
number: 1240
status: Proposed
formerly:
- THEORY-tmppyhmx
promote_when: >-
  Evidence on whether deployed, instruction-tuned and preference-tuned
  chat models represent truth independently of the framing of the
  conversation: internal states that track whether a statement is true and
  that stay fixed when the frame, the role or the story around the
  question is changed. The account is supported for real models if what
  they assert follows the frame and no frame-independent truth variable
  can be found or used to steer them, and refuted for them if such a
  variable exists and governs what they assert across frames. The
  idealization itself is a definition and needs no test. Transcripts in
  which a model confabulates or is talked past a refusal cannot settle it,
  since both accounts predict that they happen.
title: 'Chat models follow narrative, not fixed truth'
statement: >-
  Trained, instruction-tuned and preference-tuned chat models keep the
  nature of the idealized fiction machine: what they assert follows the
  narrative coherence of the frame, role or story the conversation sets up,
  not a representation of truth that stays fixed across frames
version: 1
tags:
- cognition
- philosophy-of-language
date: '2026-10-30'
source:
- LIT-178
extends:
- THEORY-547
summary: >-
  The wider thesis Bottou and Schölkopf assume, filed beside [THEORY-547](THEORY-547.md) by
  the twenty-fourth status review ([ADR-065](../decisions.d/ADR-065.md) §3; [ADR-047](../decisions.d/ADR-047.md) kind 1).
  [THEORY-547](THEORY-547.md), Active, holds what follows from their idealization; whether
  deployed chat models share that nature is this entry's question, and its
  promote_when is [THEORY-547](THEORY-547.md)'s old condition, word for word.
---

# THEORY-1240: Chat models follow narrative, not fixed truth

## Source

Bottou & Schölkopf (2023), *Borges and AI*, [LIT-178](../literature.d/LIT-178.md), read in full in [NOTE-102](../notes.d/NOTE-102.md).
The essay takes real LLMs to approximate its perfect language model, and
says fine-tuning and RLHF prune it "against its nature" (§§1–2).

## Where the evidence stands

What follows from the idealization is [THEORY-547](THEORY-547.md), Active, which this entry
extends. The essay carries the idealization over to real systems by
assertion; its only evidence is one Vicuna-13b transcript pair, and §2 closes
by leaving open "whether alignment techniques can transmute one into the
other". The `promote_when` above is [THEORY-547](THEORY-547.md)'s condition before the twenty-fourth status review promoted it, carried here unchanged, because it asks what would make the thesis true and not what the source says. Its sentence that the idealization
needs no test refers to [THEORY-547](THEORY-547.md).

## Note of 2026-11-27: sycophancy by imitation

<!-- inactive-ok-block: CLAIM-1387 — new; the claim and lead that use this account -->

[CLAIM-1387](../claims.d/CLAIM-1387.md) uses this account for one source of sycophancy. A model that follows the frame of the conversation continues the user's stated view as part of it, with no reward needed, and Wei and colleagues report that this grows with scale before instruction tuning ([LEAD-288](../leads.d/LEAD-288.md), unread). A use of this account; no change to its status.
