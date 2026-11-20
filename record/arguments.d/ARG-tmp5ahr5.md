---
status: Proposed
title: 'Applying the conservation results for contracting chains to the restatement of the record''s entries: CLAIM-635''s retention bound and DeGroot''s conserved average carry over if a session''s restatement of an entry is a Markov step and reading a coded entry verbatim copies its text exactly, which holds for the text and not for its interpretation'
version: 1
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
  The application on which CLAIM-tmpdx6l8 stands: results proved for
  Markov chains and linear averaging, applied to sessions restating the
  record's entries. The mapping holds for the stored text, which a
  verbatim read copies exactly, and holds only loosely for interpretation,
  which is where the record's anchoring is weakest. Proposed: the verdict
  is the filer's (Claude, in this session); adopting it is the owner's
  call.
---
<!-- inactive-ok-file: CLAIM-635 CLAIM-tmpw6wkt CLAIM-tmpdx6l8 TERM-tmp7i7ed THEORY-2044 CLAIM-191 CLAIM-059 — Proposed; the results applied, the claim concluded, and the term it is stated in -->

# ARG-tmp5ahr5: Applying the conservation results for contracting chains to the restatement of the record's entries: CLAIM-635's retention bound and DeGroot's conserved average carry over if a session's restatement of an entry is a Markov step and reading a coded entry verbatim copies its text exactly, which holds for the text and not for its interpretation

## The inference

The formal results:

- CLAIM-635: under Markov steps K₁, K₂, …, possibly different at each step,
  a feature f with Kᵢ f = f for every i keeps I(S₀; Sₙ) bounded below at
  every n; a bounded defect does not.
- THEORY-960: under linear averaging, what the step conserves (πF) is
  exactly what the limit keeps.
- THEORY-2044: what lies along the property a system contracts toward is
  kept, and set by initial conditions.
- CLAIM-tmpw6wkt: in a linear Gaussian step, a feature copied with error
  forgets as 1/n and a contracted one geometrically.

The mapping: the state is an entry (or an idea not yet filed); a step is a
session's restatement of it; a feature is conserved when the session copies
it rather than reconstructs it. Conclusion, CLAIM-tmpdx6l8: forgetting and
anchoring are one contraction, told apart by the conserved part, and the
record conserves content and contracts form.

## Critical questions

**Does the mapping premise hold?** For the text, yes. A coded entry stored
in a file and read verbatim is copied without error: the kernel restricted
to its text is the identity, which is CLAIM-107's exact criterion. For an
uncoded idea restated from memory or a summary, the step reconstructs, and
the copy has error. CLAIM-191 holds that restatements without anchors drift
toward the collaborators' framings, which is the contracting part.

**Are the model's assumptions met?**

- *Markov.* A session's restatement depends on more than the current
  state: the exchange, its instructions, its training. CLAIM-635 allows
  time-dependent kernels, which absorbs much of this, but a session that
  reads earlier versions of an entry, or its history, is a step on an
  enlarged state. Then the result applies to that state, and it is the
  record that enlarges it (CLAIM-059).
- *Exact conservation.* Holds for stored text only. What a session takes
  the text to mean is reconstructed every time. So the anchoring the
  result guarantees is of text, and interpretation sits in the part copied
  with error, or in the contracting part if sessions share framings.
  CLAIM-031's point, that one changed constraint can change the act with
  observables stable, is about exactly this gap.
- *Linear Gaussian, for the rates.* Only CLAIM-tmpw6wkt's rates need it;
  the split between conserved and not conserved does not.

**Is the formal result used for what it shows?** CLAIM-635 gives a lower
bound on retention, not a measure of it, and CLAIM-208 holds that a step's
constants cannot be estimated from one restatement per step. The
application is qualitative: which part a feature is in, not how fast.

## Verdict

The application holds for text and is an interpretive extension for
meaning. CLAIM-tmpdx6l8 is warranted interpretive for that reason, and its
defeater (a) asks whether coded content in fact drifts less, which is the
part this argument cannot settle.
