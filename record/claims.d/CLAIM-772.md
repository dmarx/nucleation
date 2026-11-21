---
number: 772
status: Proposed
formerly:
- CLAIM-tmpdx6l8
title: 'Forgetting a source and anchoring to it are one contraction, told apart by what each restatement step conserves exactly: a chain that contracts everywhere except on what its steps copy without error ends keeping exactly the start''s value on that conserved part, so it is anchored where the source''s features lie in the part and forgets them where they do not; the record copies content exactly, by code and verbatim reading, and leaves form to contract onto its schema'
version: 3
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
- version: 3
  date: '2026-11-21'
  note: >-
    Revised after the readings of 2026-11-21 of the two semicontraction
    papers (NOTE-2229, NOTE-2231). Version 2 named semicontraction
    as the general form of contraction with a conserved part. The readings
    show semicontraction contracts only off a seminorm's kernel and keeps
    nothing by itself; what a limit keeps is fixed by an exact conserved
    functional. The body now says so, and the readings join grounds. A
    limit names Friedkin and Johnsen's anchoring by re-injection
    (THEORY-1161) as a second route the claim does not cover. Title
    unchanged: it already says the start is kept on what the steps copy
    without error.
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
  description generalizing the other. They are. [CLAIM-635](CLAIM-635.md) holds that a
  feature every step conserves exactly keeps information about the start
  for ever; DeGroot's consensus keeps exactly πF ([THEORY-960](../theory.d/THEORY-960.md)); partial
  contraction keeps what lies along the property it contracts toward
  ([THEORY-2044](../theory.d/THEORY-2044.md)). So anchoring is contraction with the source's features in
  the conserved part, and forgetting is contraction with them outside it.
  "Monotone" does not separate them: distance to the fixed set falls at
  every step in both. The wording is the assistant's (Claude, in this
  session); adopting it is the owner's call.
rests_on:
- CLAIM-635
- CLAIM-107
- CLAIM-779
- CLAIM-068
- CLAIM-191
- CLAIM-181
grounds:
- THEORY-960
- THEORY-2044
- THEORY-2143
- THEORY-2142
uses:
- TERM-132
bears_on:
- QUESTION-006
---
<!-- inactive-ok-file: THEORY-2142 THEORY-2143 — Proposed; cited in the readings of 2026-11-21 -->
<!-- inactive-ok-file: CLAIM-068 CLAIM-191 CLAIM-181 CLAIM-059 CLAIM-180 THEORY-2044 THEORY-2043 — Proposed; open, cited for what each holds -->
<!-- inactive-ok-file: CLAIM-779 TERM-132 ARG-124 — Proposed or Deferred; filed in this contribution of 2026-11-20 -->

# CLAIM-772: Forgetting a source and anchoring to it are one contraction, told apart by what each restatement step conserves exactly: a chain that contracts everywhere except on what its steps copy without error ends keeping exactly the start's value on that conserved part, so it is anchored where the source's features lie in the part and forgets them where they do not; the record copies content exactly, by code and verbatim reading, and leaves form to contract onto its schema

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
  depends only on the steps ([THEORY-2043](../theory.d/THEORY-2043.md), Lohmiller and Slotine:
  "initial conditions are forgotten"). This is attraction toward a
  convention, reached "whatever its start" ([CLAIM-068](CLAIM-068.md), [TERM-027](../terms.d/TERM-027.md)).
- **Contraction with a conserved part keeps exactly that part.** In
  DeGroot's averaging, F⁽ⁿ⁾ = PⁿF, disagreement contracts to nothing, yet
  "πF⁽ⁿ⁾ = πPⁿF = πF at every round, so the consensus can only be πF"
  ([THEORY-960](../theory.d/THEORY-960.md)): the limit keeps one weighted average of the start and
  nothing else. In partial contraction, "what is contracted is the distance
  to the property, and what lies along it is kept", so synchronized
  oscillators keep "a common phase that the initial conditions fix"
  ([THEORY-2044](../theory.d/THEORY-2044.md)). For Markov steps in general, [CLAIM-635](CLAIM-635.md): a feature with
  K f = f at every step keeps information about the start bounded below at
  every generation, so the chain "cannot converge to a law independent of
  its start".
- **Semicontraction is the forgetting half only.** The control literature
  calls a system contracting except on a subspace semicontracting. Read on
  2026-11-21, it contracts what lies off a seminorm's kernel and keeps
  nothing by itself: trajectories may diverge along the kernel
  ([THEORY-2143](../theory.d/THEORY-2143.md), Jafarpour and colleagues), and only the part off the
  kernel contracts, differences along it may persist or grow
  ([THEORY-2142](../theory.d/THEORY-2142.md), De Pasquale and colleagues). Where their examples fix
  the limit, an exact conserved functional fixes it, vᵀx with v the
  dominant left eigenvector, as πF in DeGroot. So the part this claim calls
  conserved is not a seminorm's kernel but the functionals each step
  conserves exactly; the kernel may also hold neutral or expansive
  directions.

So a chain is **anchored** to its source on the features its steps copy
exactly, and **forgets** it on the rest. Stabilization and contraction are
not two mechanisms; they are one contraction, and which features of the
source survive is fixed by the conserved part of the step.

**Exactly, not approximately.** [CLAIM-635](CLAIM-635.md): "a bounded conservation defect
does not prevent forgetting". [CLAIM-779](CLAIM-779.md) gives the rates: a contracted
feature forgets geometrically, a feature copied with any error forgets as
1/n while it random-walks, and only a feature copied exactly keeps its
start. A paraphrase is a copy with error. That is a mechanism for
[CLAIM-180](CLAIM-180.md)'s finding that a restatement drifted far enough is taken for new,
and for [CLAIM-191](CLAIM-191.md)'s that a code restores continuity: reading a code and its
file verbatim is the record's exact copy.

**The record's design, restated.** Each feature of an entry lies in one of
four parts of the step ([TERM-132](../terms.d/TERM-132.md)):

| Part | Step does | Over many restatements | On the record |
|---|---|---|---|
| contracting | pulls toward the step's own fixed point | start forgotten; settles on the convention | form: fields, vocabulary, voice, prose conventions |
| conserved | copies exactly | start kept | coded content read verbatim |
| neutral, copied with error | copies with error | random walk; start forgotten as 1/n | uncoded content: the entry's local degrees of freedom |
| expansive | magnifies | amplifies | needs an enlarged state ([CLAIM-059](CLAIM-059.md)) |

The record puts content in the conserved part, by giving it a code and
having sessions read it rather than reconstruct it, and leaves form in the
contracting part: the schema is the convention, and lint makes the
contraction onto it fast. [TERM-027](../terms.d/TERM-027.md)'s attractor, "a shared decoding
convention rather than a preserved historical object", is for form what the
record designs it to be. [CLAIM-181](CLAIM-181.md) holds that the record fixes the
grammar an argument is expressed in; this claim says by what dynamic the
grammar is kept and the content is not lost to it.

**Monotone does not separate them.** Distance to the fixed set falls at
every step in both cases. Read as nested admissible sets, C₀ ⊇ C₁ ⊇ …, the
answer is the same: the limit lies in the intersection, and the source is in
it exactly when every constraint was one the source satisfies, that is, when
the constraints were written from the source and not from the transmitter's
habits.

## What it does not say

- Not that anchoring means only this. Friedkin and Johnsen's "anchoring on
  initial positions" ([THEORY-1161](../theory.d/THEORY-1161.md)) re-injects the start as a persistent input
  at every step; the record also does that when a session rereads the
  originating turn. That is a second route to keeping the source, by a
  constant drive rather than by conservation, and the claim does not cover
  it.

- Not that the source is kept in full. Only its value on the conserved part
  is kept. [CLAIM-094](CLAIM-094.md) marks the same limit for a harmonic observable: it
  conserves its mean and is not thereby a symmetry. The text of a coded
  entry is conserved; how a session interprets it is not, and [CLAIM-031](CLAIM-031.md)'s
  point, that one changed constraint can change the act while observables
  hold, applies to interpretation.
- Not that the record's restatements are Markov or linear. [CLAIM-635](CLAIM-635.md) needs
  only Markov steps, possibly different at each step; the table's rates are
  [CLAIM-779](CLAIM-779.md)'s linear Gaussian model. [ARG-124](../arguments.d/ARG-124.md) answers whether the
  mapping holds.
- Not that the constants can be estimated. [CLAIM-208](CLAIM-208.md) stands: a single
  restatement per step does not identify a step's sensitivity.
- Not that the record cannot amplify. The record is an enlarged state, which
  [CLAIM-059](CLAIM-059.md) says amplification needs; whether it enables an expansive part
  is left open.

## Reframings
<!-- inactive-ok-file: ADR-120 — Proposed; the decision this section follows, 2026-11-21 -->

**2026-11-20, the owner at U5 of the session ([ADR-120](../decisions.d/ADR-120.md)).** "Are you sure
these are different things? I'm wondering if maybe it's the same phenomenon,
and maybe one description generalizes the other. Isn't stabilization just
monotone contraction?" Before: constraint and contraction were two
mechanisms acting on different terms of [CLAIM-056](CLAIM-056.md)'s drift bound, constraint
bounding what a step injects and contraction forgetting the start. After:
one contraction, with forgetting and anchoring told apart by what each step
copies exactly. It changed the account and the title, in version 2; the
division of labour between form and content was kept, restated as which
part of the step each lies in.

## Admission

Audited at the synthesis review of 2026-11-21 ([ADR-075](../decisions.d/ADR-075.md), step 5) by a reader briefed neutrally, with the two objections of that day ([CLAIM-789](CLAIM-789.md), [CLAIM-793](CLAIM-793.md)) read.

**What the general half adds: nothing.** "One contraction, anchored on what is copied exactly, forgetting elsewhere" is [CLAIM-635](CLAIM-635.md) with [CLAIM-779](CLAIM-779.md)'s rates. [CLAIM-635](CLAIM-635.md)'s note of 2026-11-20 already records the application.

**What the record-design half adds, by the separating-case route.** The sentence is: in this record, content lies in the conserved part of the restatement step and form in the contracting part. A realistic case separates it from its premises: the fact-checks of the manuscript of 2026-11-20, which found errors in restatements of coded entries that the drafter had read ([CLAIM-793](CLAIM-793.md)). Every premise holds there, and coded content was still not in the conserved part of those restatements. The case does not meet defeater (a), which needs a rate for uncoded content, so it separates the claim and does not show it false.

**A narrower sentence that passes:** "In this record, the form of filed entries converges across sessions onto the schema faster than uncoded content converges toward the collaborators' framings, and derived restatements of coded entries depart from the stored entry less than restatements of uncoded content do." It needs two fixes, which are the owner's call:
- fix where uncoded content sits, neutral or contracting (the table and defeater (a) disagree);
- drop defeater (a)'s appeal to verbatim-read text, which cannot drift.

## Note of 2026-11-21: what the audit found misstated

- **The title overstates [CLAIM-635](CLAIM-635.md).** "Ends keeping exactly the start's value on that conserved part" holds only for noiseless copying. [CLAIM-635](CLAIM-635.md) keeps the conditional mean and bounds the information retained ("only its conditional mean is kept"). [CLAIM-107](CLAIM-107.md)'s absorbed walk is the counterexample: f is harmonic, yet f(S_n) spreads to the endpoints.
- **[CLAIM-779](CLAIM-779.md)'s 1/n** is stated in the body as general. [CLAIM-779](CLAIM-779.md) holds it in the linear Gaussian model only.
- **"Global contraction forgets"** omits [CLAIM-779](CLAIM-779.md)'s condition: noiseless contraction does not forget in the information sense.
- **[CLAIM-191](CLAIM-191.md) and [CLAIM-181](CLAIM-181.md) are stretched.** [CLAIM-191](CLAIM-191.md)'s code gives descent, not "the record's exact copy". [CLAIM-181](CLAIM-181.md) is a counter, used here as support.

No change of status or title. A retitle is for the owner.
