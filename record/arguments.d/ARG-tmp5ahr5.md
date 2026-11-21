---
status: Proposed
title: 'Applying the conservation results for contracting chains to the restatement of the record''s entries: CLAIM-635''s retention bound and DeGroot''s conserved average carry over if a session''s restatement of an entry is a Markov step and reading a coded entry verbatim copies its text exactly, which holds for the text and not for its interpretation'
version: 2
history:
- version: 2
  date: '2026-11-21'
  note: >-
    A dated note: the semicontraction readings leave the mapping unchanged
    and strengthen its reliance on exact invariants. No change of status
    or title.
form: formal-application
rests_on:
- CLAIM-635
- CLAIM-107
- CLAIM-tmpw6wkt
grounds:
- THEORY-960
- THEORY-2044
concludes:
- CLAIM-tmpdx6l8
uses:
- TERM-tmp7i7ed
tags:
- design-rationale
- probabilistic-modeling
date: '2026-11-20'
line:
- nucleating-argument
- formal-apparatus
summary: >-
  The application on which [CLAIM-tmpdx6l8](../claims.d/CLAIM-tmpdx6l8.md) stands: results proved for
  Markov chains and linear averaging, applied to sessions restating the
  record's entries. The mapping holds for the stored text, which a
  verbatim read copies exactly, and holds only loosely for interpretation,
  which is where the record's anchoring is weakest. Proposed: the verdict
  is the filer's (Claude, in this session); adopting it is the owner's
  call.
---
<!-- inactive-ok-file: THEORY-tmprwljl THEORY-tmpq3h4k CLAIM-635 — Proposed, Unfetched or new; filed in the readings of 2026-11-21 -->
<!-- inactive-ok-file: CLAIM-635 CLAIM-tmpw6wkt CLAIM-tmpdx6l8 THEORY-2044 CLAIM-191 CLAIM-059 — Proposed; the results applied, the claim concluded, and the term it is stated in -->

# ARG-tmp5ahr5: Applying the conservation results for contracting chains to the restatement of the record's entries: [CLAIM-635](../claims.d/CLAIM-635.md)'s retention bound and DeGroot's conserved average carry over if a session's restatement of an entry is a Markov step and reading a coded entry verbatim copies its text exactly, which holds for the text and not for its interpretation

## The inference

The formal results:

- [CLAIM-635](../claims.d/CLAIM-635.md): under Markov steps K₁, K₂, …, possibly different at each step,
  a feature f with Kᵢ f = f for every i keeps I(S₀; Sₙ) bounded below at
  every n; a bounded defect does not.
- [THEORY-960](../theory.d/THEORY-960.md): under linear averaging, what the step conserves (πF) is
  exactly what the limit keeps.
- [THEORY-2044](../theory.d/THEORY-2044.md): what lies along the property a system contracts toward is
  kept, and set by initial conditions.
- [CLAIM-tmpw6wkt](../claims.d/CLAIM-tmpw6wkt.md): in a linear Gaussian step, a feature copied with error
  forgets as 1/n and a contracted one geometrically.

The mapping: the state is an entry (or an idea not yet filed); a step is a
session's restatement of it; a feature is conserved when the session copies
it rather than reconstructs it. Conclusion, [CLAIM-tmpdx6l8](../claims.d/CLAIM-tmpdx6l8.md): forgetting and
anchoring are one contraction, told apart by the conserved part, and the
record conserves content and contracts form.

## Critical questions

**Does the mapping premise hold?** For the text, yes. A coded entry stored
in a file and read verbatim is copied without error: the kernel restricted
to its text is the identity, which is [CLAIM-107](../claims.d/CLAIM-107.md)'s exact criterion. For an
uncoded idea restated from memory or a summary, the step reconstructs, and
the copy has error. [CLAIM-191](../claims.d/CLAIM-191.md) holds that restatements without anchors drift
toward the collaborators' framings, which is the contracting part.

**Are the model's assumptions met?**

- *Markov.* A session's restatement depends on more than the current
  state: the exchange, its instructions, its training. [CLAIM-635](../claims.d/CLAIM-635.md) allows
  time-dependent kernels, which absorbs much of this, but a session that
  reads earlier versions of an entry, or its history, is a step on an
  enlarged state. Then the result applies to that state, and it is the
  record that enlarges it ([CLAIM-059](../claims.d/CLAIM-059.md)).
- *Exact conservation.* Holds for stored text only. What a session takes
  the text to mean is reconstructed every time. So the anchoring the
  result guarantees is of text, and interpretation sits in the part copied
  with error, or in the contracting part if sessions share framings.
  [CLAIM-031](../claims.d/CLAIM-031.md)'s point, that one changed constraint can change the act with
  observables stable, is about exactly this gap.
- *Linear Gaussian, for the rates.* Only [CLAIM-tmpw6wkt](../claims.d/CLAIM-tmpw6wkt.md)'s rates need it;
  the split between conserved and not conserved does not.

**Is the formal result used for what it shows?** [CLAIM-635](../claims.d/CLAIM-635.md) gives a lower
bound on retention, not a measure of it, and [CLAIM-208](../claims.d/CLAIM-208.md) holds that a step's
constants cannot be estimated from one restatement per step. The
application is qualitative: which part a feature is in, not how fast.

## Verdict

The application holds for text and is an interpretive extension for
meaning. [CLAIM-tmpdx6l8](../claims.d/CLAIM-tmpdx6l8.md) is warranted interpretive for that reason, and its
defeater (a) asks whether coded content in fact drifts less, which is the
part this argument cannot settle.

## Note of 2026-11-21: the semicontraction readings

Read on 2026-11-21, the two semicontraction papers (THEORY-tmprwljl, THEORY-tmpq3h4k) cover deterministic systems only, so they cannot replace this application to restatement. They show that semicontraction keeps nothing by itself and that what a limit keeps is fixed by an exact conserved functional, which is the mapping premise this argument already rests on (CLAIM-635, THEORY-960). The answer to its first critical question stands.
