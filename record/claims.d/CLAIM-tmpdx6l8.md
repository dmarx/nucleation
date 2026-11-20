---
status: Proposed
title: 'Forgetting a source and anchoring to it are one contraction, told apart by what each restatement step conserves exactly: a chain that contracts everywhere except on what its steps copy without error ends keeping exactly the start''s value on that conserved part, so it is anchored where the source''s features lie in the part and forgets them where they do not; the record copies content exactly, by code and verbatim reading, and leaves form to contract onto its schema'
version: 2
history:
- version: 2
  date: '2026-11-20'
  note: >-
    Rewritten before merging, at the owner's U5: "Are you sure these are
    different things? I'm wondering if maybe it's the same phenomenon, and
    maybe one description generalizes the other. Isn't stabilization just
    monotone contraction?" Version 1 held that constraint and contraction
    are different mechanisms acting on different terms of CLAIM-056's
    bound, constraint on the per-step discrepancy and the reference, and
    that constraint "does not make the transmitter less contractive". The
    second half was wrong: copying a feature exactly sets that feature's
    sensitivity to one and its discrepancy to zero, so it changes the step,
    not only what the step injects. Version 1's title: "Constraint and
    contraction narrow an entry through different terms of the drift
    bound: contraction is the later steps' sensitivity, pulling each
    restatement toward the transmitters' own fixed point and forgetting
    the start, while constraint bounds what each step can inject and
    supplies the reference transport departure is measured from; the
    record relies on contraction for form, by making its schema the
    convention restatements converge on, and on constraint for content".
    The division of labour between form and content is kept, restated as
    which part of the step each lies in.
role: thesis
warrant: interpretive
defeated_if: >-
  Either of two results. (a) In the record's exchanges, coded content
  that sessions read verbatim drifts across restatements toward the
  collaborators' framings as fast as uncoded content does, so that exact
  copying does not conserve it. (b) The form of filed entries (fields,
  vocabulary, voice markers, prose conventions) does not converge across
  sessions toward the schema faster than uncoded content converges toward
  the collaborators' framings, so that form and content are not divided
  between the contracting and the conserved part.
tags:
- design-rationale
- epistemology
- complex-systems
date: '2026-11-20'
line:
- nucleating-argument
- pragmatic-transport
- record-as-apparatus
summary: >-
  The owner asked at U2 how stabilization relates to the record's account
  of contraction, and at U5 whether they are one phenomenon, one
  description generalizing the other. They are. CLAIM-635 holds that a
  feature every step conserves exactly keeps information about the start
  for ever; DeGroot's consensus keeps exactly πF (THEORY-960); partial
  contraction keeps what lies along the property it contracts toward
  (THEORY-2044). So anchoring is contraction with the source's features in
  the conserved part, and forgetting is contraction with them outside it.
  "Monotone" does not separate them: distance to the fixed set falls at
  every step in both. The wording is the assistant's (Claude, in this
  session); adopting it is the owner's call.
rests_on:
- CLAIM-635
- CLAIM-107
- CLAIM-tmpw6wkt
- CLAIM-068
- CLAIM-191
- CLAIM-181
grounds:
- THEORY-960
- THEORY-2044
uses:
- TERM-tmp7i7ed
bears_on:
- QUESTION-006
---
<!-- inactive-ok-file: CLAIM-635 CLAIM-068 CLAIM-191 CLAIM-181 CLAIM-059 CLAIM-180 THEORY-2044 THEORY-2043 — Proposed; open, cited for what each holds -->
<!-- inactive-ok-file: CLAIM-tmpw6wkt TERM-tmp7i7ed ARG-tmp5ahr5 LIT-tmpavt0i LIT-tmpru0xs — Proposed or Deferred; filed in this contribution of 2026-11-20 -->

# CLAIM-tmpdx6l8: Forgetting a source and anchoring to it are one contraction, told apart by what each restatement step conserves exactly: a chain that contracts everywhere except on what its steps copy without error ends keeping exactly the start's value on that conserved part, so it is anchored where the source's features lie in the part and forgets them where they do not; the record copies content exactly, by code and verbatim reading, and leaves form to contract onto its schema

## The claim

The owner, at U2: "relate that account of stabilization to the record's
account of contraction". At U5, of the assistant's first answer, that the
two do different jobs: "Are you sure these are different things? I'm
wondering if maybe it's the same phenomenon, and maybe one description
generalizes the other. Isn't stabilization just monotone contraction? maybe
there's a formalization we could lean on that would make this clearer for
me."

**One phenomenon.** Treat restating an entry as a chain: each session's
restatement is a step applied to the current state. The record already
holds what such a chain keeps.

- **Global contraction forgets.** If every step brings any two states
  closer by a factor below one, all chains reach one fixed point, which
  depends only on the steps (THEORY-2043, Lohmiller and Slotine:
  "initial conditions are forgotten"). This is attraction toward a
  convention, reached "whatever its start" (CLAIM-068, TERM-027).
- **Contraction with a conserved part keeps exactly that part.** In
  DeGroot's averaging, F⁽ⁿ⁾ = PⁿF, disagreement contracts to nothing, yet
  "πF⁽ⁿ⁾ = πPⁿF = πF at every round, so the consensus can only be πF"
  (THEORY-960): the limit keeps one weighted average of the start and
  nothing else. In partial contraction, "what is contracted is the distance
  to the property, and what lies along it is kept", so synchronized
  oscillators keep "a common phase that the initial conditions fix"
  (THEORY-2044). For Markov steps in general, CLAIM-635: a feature with
  K f = f at every step keeps information about the start bounded below at
  every generation, so the chain "cannot converge to a law independent of
  its start". The control literature calls a system contracting except on
  a subspace semicontracting (LIT-tmpavt0i, LIT-tmpru0xs, not yet read).

So a chain is **anchored** to its source on the features its steps copy
exactly, and **forgets** it on the rest. Stabilization and contraction are
not two mechanisms; they are one contraction, and which features of the
source survive is fixed by the conserved part of the step.

**Exactly, not approximately.** CLAIM-635: "a bounded conservation defect
does not prevent forgetting". CLAIM-tmpw6wkt gives the rates: a contracted
feature forgets geometrically, a feature copied with any error forgets as
1/n while it random-walks, and only a feature copied exactly keeps its
start. A paraphrase is a copy with error. That is a mechanism for
CLAIM-180's finding that a restatement drifted far enough is taken for new,
and for CLAIM-191's that a code restores continuity: reading a code and its
file verbatim is the record's exact copy.

**The record's design, restated.** Each feature of an entry lies in one of
four parts of the step (TERM-tmp7i7ed):

| Part | Step does | Over many restatements | On the record |
|---|---|---|---|
| contracting | pulls toward the step's own fixed point | start forgotten; settles on the convention | form: fields, vocabulary, voice, prose conventions |
| conserved | copies exactly | start kept | coded content read verbatim |
| neutral, copied with error | copies with error | random walk; start forgotten as 1/n | uncoded content: the entry's local degrees of freedom |
| expansive | magnifies | amplifies | needs an enlarged state (CLAIM-059) |

The record puts content in the conserved part, by giving it a code and
having sessions read it rather than reconstruct it, and leaves form in the
contracting part: the schema is the convention, and lint makes the
contraction onto it fast. TERM-027's attractor, "a shared decoding
convention rather than a preserved historical object", is for form what the
record designs it to be. CLAIM-181 holds that the record fixes the
grammar an argument is expressed in; this claim says by what dynamic the
grammar is kept and the content is not lost to it.

**Monotone does not separate them.** Distance to the fixed set falls at
every step in both cases. Read as nested admissible sets, C₀ ⊇ C₁ ⊇ …, the
answer is the same: the limit lies in the intersection, and the source is in
it exactly when every constraint was one the source satisfies, that is, when
the constraints were written from the source and not from the transmitter's
habits.

## What it does not say

- Not that the source is kept in full. Only its value on the conserved part
  is kept. CLAIM-094 marks the same limit for a harmonic observable: it
  conserves its mean and is not thereby a symmetry. The text of a coded
  entry is conserved; how a session interprets it is not, and CLAIM-031's
  point, that one changed constraint can change the act while observables
  hold, applies to interpretation.
- Not that the record's restatements are Markov or linear. CLAIM-635 needs
  only Markov steps, possibly different at each step; the table's rates are
  CLAIM-tmpw6wkt's linear Gaussian model. ARG-tmp5ahr5 answers whether the
  mapping holds.
- Not that the constants can be estimated. CLAIM-208 stands: a single
  restatement per step does not identify a step's sensitivity.
- Not that the record cannot amplify. The record is an enlarged state, which
  CLAIM-059 says amplification needs; whether it enables an expansive part
  is left open.
