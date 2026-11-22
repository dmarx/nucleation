---
number: 517
status: Open
formerly:
- QUESTION-tmpzlagu
title: 'Do the effective dimensions of one system, the number of its stiff Fisher directions at a given resolution, the dimension of its predictive states, the number of its relevant renormalization-group directions and its fractal dimension, agree, and when do they come apart?'
version: 1
tags:
- information-geometry
- information-theory
- complex-systems
- learning-theory
date: '2026-11-21'
line:
- formal-apparatus
- learned-structure
summary: >-
  A's open question at the close of A19 and the table at A21 §1 of the
  exchange "Rich Get Richer Power Laws": "Is the effective dimensionality
  of a complex system fundamentally determined by how much information is
  required to predict its behavior?", with "several competing meanings of
  effective dimensionality: geometric dimension, the number of important
  Fisher-information eigenvectors, the number of predictive state
  variables, and the number of relevant RG directions. Understanding when
  these quantities agree—and when they diverge" is the task. The record
  holds pieces of each and no comparison; [QUESTION-217](QUESTION-217.md) asks a sibling
  question about orders, not counts. The wording is A's (the other
  assistant in the exchange "Rich Get Richer Power Laws", A19 and A21);
  adopting it is the owner's call.
---
<!-- inactive-ok-file: THEORY-777 — Proposed reading, the relevant-direction count -->
<!-- inactive-ok-file: CLAIM-825 CLAIM-849 TERM-141 — filed with this question from the same exchange, Proposed or Open -->
<!-- inactive-ok-file: SYNTHESIS-084 THEORY-1558 — Proposed, cited as the open state of the RG–information correspondence and of rate-demarcated levels -->
<!-- inactive-ok-file: THEORY-2151 THEORY-2155 — Proposed or Rejected entries filed on 2026-11-21 from the exchange "Rich Get Richer Power Laws" and from the readings of its works, or Deferred works not yet read -->

<!-- inactive-ok-file: THEORY-tmpx26x7 CLAIM-820 TERM-140 TERM-135 — Proposed or new; the 2023 review's reading and the entries that hold the relativity it states -->
<!-- inactive-ok-file: THEORY-tmpttfgp THEORY-tmpl7rgc CLAIM-tmp3ima1 — Proposed or new; the readings of Shalizi and Moore and of Crutchfield and Feldman, 2026-11-22, and the claim and term filed from them -->

# QUESTION-517: Do the effective dimensions of one system, the number of its stiff Fisher directions at a given resolution, the dimension of its predictive states, the number of its relevant renormalization-group directions and its fractal dimension, agree, and when do they come apart?

## Why it is a question

A21 §1 tabulates five quantities that "can legitimately be called its
dimensionality", microstate, parameter, relevant-RG, predictive-state and
fractal, and says "These are not generally equal." The 2D Ising model
shows the spread at once: 2^N configurations, two couplings K and H, two
relevant scalar perturbations, and geometric spin clusters of fractal dimension 187/96
at criticality. "**Simple laws don't imply simple realizations**" (A21
§1).

The record holds a piece of each and no comparison:

- **Stiff Fisher directions**: two stay under decimation of the critical
  Ising model, the field and the T_c gradient ([THEORY-777](../theory.d/THEORY-777.md)); and the count
  resolved grows with the data at a rate set by the spectrum
  ([CLAIM-825](../claims.d/CLAIM-825.md)), so it is a function of resolution, not a number.
- **Parameter count in learning**: (d/2) log n in a regular model, the
  learning coefficient in a singular one ([THEORY-087](../theory.d/THEORY-087.md), [THEORY-1253](../theory.d/THEORY-1253.md)).
- **Predictive states**: the causal states and their entropy
  ([TERM-062](../terms.d/TERM-062.md), [THEORY-756](../theory.d/THEORY-756.md)); predictive information as a function of window
  ([TERM-141](../terms.d/TERM-141.md)), whose growth a Fisher spectrum fixes in one model
  ([CLAIM-849](../claims.d/CLAIM-849.md)).
- **Relevant directions**: the RG account ([THEORY-777](../theory.d/THEORY-777.md), [THEORY-742](../theory.d/THEORY-742.md)) and the
  question whether information criteria find them ([QUESTION-232](QUESTION-232.md),
  [SYNTHESIS-084](../syntheses.d/SYNTHESIS-084.md)).

[CLAIM-849](../claims.d/CLAIM-849.md) joins two of them in a linear-Gaussian model: there the
resolved Fisher count and the growth of predictive information move
together. Whether that survives where the spectrum comes from
coarse-graining rather than from a prior, whether the relevant-direction
count is the T → ∞ limit of the stiff count under coarse observation, and
whether a fractal dimension of the realizations enters any of them, the
record cannot say.

## What would answer it

One system in which all four are computed under one observation scheme,
with the scheme stated ([LEAD-208](../leads.d/LEAD-208.md) proposes the 2D Ising model), and
either a pattern of agreement with its conditions or a pair that
provably comes apart. A partial answer: a proof that, under a stated
coarse-graining, the number of Fisher eigenvalues that do not decay with
scale equals the number of relevant directions, which [THEORY-777](../theory.d/THEORY-777.md) shows
numerically for one lattice and one family.

## Related

[QUESTION-217](QUESTION-217.md) asks whether orders of refinement, relevance and acquisition
in learning admit one chain; this asks whether counts agree. A21 §10's
further question, whether multiscale complexity lies in the number of
levels or in how freely information moves between them, is held in part
by [THEORY-581](../theory.d/THEORY-581.md), [THEORY-1558](../theory.d/THEORY-1558.md) and [QUESTION-219](QUESTION-219.md) and is not filed separately.

## Note of 2026-11-21: Bialek, Nemenman & Tishby and Transtrum, Machta & Sethna (2010, 2011), read

More effective dimensions the question does not list, and none resolves
it:

- **Bialek, Nemenman and Tishby** ([NOTE-2243](../notes.d/NOTE-2243.md), [THEORY-2151](../theory.d/THEORY-2151.md)) separate
  the parameter count K, a "phase space dimension" d that replaces K when
  the Fisher matrix is degenerate (Eq. 64), and the VC dimension, below
  which the (d/2) log N law does not hold. Their d is the regular-model
  counterpart of a learning coefficient's 2λ.
- **Transtrum, Machta and Sethna 2011** ([NOTE-2247](../notes.d/NOTE-2247.md), [THEORY-2155](../theory.d/THEORY-2155.md))
  count the parameters not evaporated at a best fit, growing as
  log(W₀/σ)/|log ∆| for widths W₀∆ⁿ (Eq. 37), and summarize the manifold by
  "three numbers", W₀, ∆ and N.
- **The 2010 letter** speaks of "few effective degrees of freedom" without
  defining the count ([NOTE-2240](../notes.d/NOTE-2240.md)).

Relations are written from [THEORY-2151](../theory.d/THEORY-2151.md) and [THEORY-2155](../theory.d/THEORY-2155.md).

## Note of 2026-11-22: Quinn, Abbott, Transtrum, Machta & Sethna (2023), read

Read in [NOTE-tmp3keyy](../notes.d/NOTE-tmp3keyy.md) ([THEORY-tmpx26x7](../theory.d/THEORY-tmpx26x7.md), which `bears_on` this question).
It leaves the question open and sharpens what an answer must state.

- **The question asked of the system fixes the count.** §8.2: "sloppiness
  is a property both of the scientific model and the predictions of
  interest. The Ising model is not sloppy, and has no beautiful emergent
  theory, unless one only cares about long length and time scales. And a
  systems biology model is not sloppy if one designs experiments to
  measure one parameter at a time." So the stiff-direction count, and with
  it the relevant-direction count it is to be compared with, belong to a
  system paired with the observables one cares about, as [CLAIM-820](../claims.d/CLAIM-820.md) holds
  for the coming-apart of parameter and behavioural complexity.
- **And so does the precision.** §2: a sloppy model has "an effective
  low-dimensional description if many of its widths are small compared to
  the precision of the predictions demanded. This need not be the case":
  ΛCDM is sloppy and all its parameters are well determined. "Sloppy" and
  "low effective dimension" part here, one more case beside those above.
- **Two explanations.** The review says hyperribbons in renormalizable
  physics and in least-squares fitting have explanations that "seem
  completely different" (§8.2). That is a reason to expect the
  relevant-RG count and the stiff count to agree in the first kind of
  system and to need a separate argument in the second.

**Whether the question-relativity needs an entry of its own.** The
assistant considered filing "sloppiness, and the effective dimension it
gives, belongs to a model paired with a set of observables and a demanded
precision" as a claim, and did not: the record already holds it in
[TERM-140](../terms.d/TERM-140.md) ("Relative to a design"), [TERM-135](../terms.d/TERM-135.md) (condition 1) and [CLAIM-820](../claims.d/CLAIM-820.md)
(relative to the observables fitted, and now to the precision demanded,
version 3). For this question it means that "What would answer it" must
name the observables and the precision as well as the observation scheme.
The review's further suggestion, "Perhaps it is caring about the answers
to the right questions that makes science possible?", is a speculation
with no argument behind it, and stays in the reading. The note is the
assistant's (Claude, in this session).

## Note of 2026-11-22: Shalizi and Moore, read

Read in [NOTE-tmpunt6q](../notes.d/NOTE-tmpunt6q.md) ([THEORY-tmpttfgp](../theory.d/THEORY-tmpttfgp.md), which `bears_on` this question).
It **leaves the question open and supplies one datum on the
predictive-state side**. The paper reports entropies, not a dimension,
and they move with the observation and the time step: argon's
macrostate predictive efficiency E/Cµ is 0.87 at a 1 ms step, "essentially
one" at matched resolution, and the microstate's "essentially zero" at
the macro time-scale (§IV.A). That fits this question's own remark,
after [CLAIM-825](../claims.d/CLAIM-825.md), that such a dimension is "a function of resolution, not
a number". No comparison with Fisher or
renormalization-group counts is made.

**Whether the relativity of these dimensions needs an entry of its own:
two alternatives, filed both; the owner chooses.**

- **(a) The lean: yes, as a claim.** [CLAIM-tmp3ima1](../claims.d/CLAIM-tmp3ima1.md) (Proposed, the
  assistant's): coarse-graining, sloppiness and emergence are each defined
  relative to a chosen set of observables and a demanded precision, and
  the dynamics fix the rest, on Quinn and colleagues ([THEORY-tmpx26x7](../theory.d/THEORY-tmpx26x7.md): the
  Ising sentence of §8.2 and ΛCDM) and Shalizi and Moore ("Nature has no
  preferred questions"). It widens what the record held for sloppiness to
  the macrostates and the emergence relation the question's
  predictive-state dimension depends on.
- **(b) No: this note is the alternative.** The previous filer's view,
  recorded in the note of 2026-11-22 on Quinn and colleagues above: the
  question-relativity is already held in [TERM-140](../terms.d/TERM-140.md) ("Relative to a
  design"), [TERM-135](../terms.d/TERM-135.md) (condition 1) and [CLAIM-820](../claims.d/CLAIM-820.md) (relative to the
  observables fitted and to the precision demanded), and needs no entry;
  for this question it means only that "What would answer it" must name
  the observables and the precision as well as the observation scheme.
  On this reading Shalizi and Moore add a parallel for causal states,
  already target-relative in [TERM-062](../terms.d/TERM-062.md), and no new claim.

Either way, an answer must name, for each of the four dimensions, the
observables and the precision it is computed at. The note is the
assistant's (Claude, in this session).

## Note of 2026-11-22: Crutchfield and Feldman, read

Read in [NOTE-tmpe86ty](../notes.d/NOTE-tmpe86ty.md) ([THEORY-tmpl7rgc](../theory.d/THEORY-tmpl7rgc.md)). **Background, with a caution for
the predictive-state dimension.** The excess entropy and its finite-L
estimates are defined there; "unlike in one dimension where the various
expressions for the excess entropy are equivalent, they yield different
results when extended to two dimensions" (§VIII). So a predictive-state
dimension for a two-dimensional system, such as [LEAD-208](../leads.d/LEAD-208.md)'s Ising lattice,
must say which definition it uses. The paper also warns that an observer
who stops at a finite block length converts unseen memory into apparent
randomness (Props. 13–15), which bears on any finite-window estimate of
predictive information.
