---
number: 71
status: Proposed
formerly:
- SYNTHESIS-tmp002mq
title: 'Under Markov kernels a symmetry principle can be borrowed but a conservation law has to be derived: an exactly harmonic observable conserves only its mean, only constants are harmonic on a finite irreducible chain, retaining information about the start and staying near the starting law are different properties, and exact conservation of a non-constant observable keeps information about the start at every generation while a bounded defect does not'
version: 1
defeated_if: >-
  A component misstated or misattributed here; an in-force component of
  the conservation-and-retention part of the formal-apparatus line left
  out without a reason given; or a link this account states that no
  component states. Its standing is its components': a component retired
  or demoted takes its clause with it, and nothing here holds the clause
  up.
tags:
- mathematics
- probabilistic-modeling
- information-theory
date: '2026-11-11'
line:
- formal-apparatus
integrates:
- CLAIM-040
- CLAIM-093
- CLAIM-094
- CLAIM-107
- CLAIM-270
- CLAIM-635
---
<!-- inactive-ok-file: ADR-075 CLAIM-068 CLAIM-189 CLAIM-191 CLAIM-635 SYNTHESIS-060 — Proposed; components, decisions and accounts cited with their standing -->
<!-- inactive-ok-file: CLAIM-015 — Superseded; cited as the entry of its time -->
<!-- inactive-ok-file: SYNTHESIS-088 — Proposed; cited with its standing -->

# SYNTHESIS-071: Under Markov kernels a symmetry principle can be borrowed but a conservation law has to be derived: an exactly harmonic observable conserves only its mean, only constants are harmonic on a finite irreducible chain, retaining information about the start and staying near the starting law are different properties, and exact conservation of a non-constant observable keeps information about the start at every generation while a bounded defect does not

*A part account of the formal-apparatus line: one of the line's eleven
small clusters, six entries on what a Markov chain of reconstruction
kernels conserves and what it keeps of its start. The line's account is
built over it and its sibling parts. Five of the six are first in the
pragmatic-transport line, where [SYNTHESIS-060](SYNTHESIS-060.md) sets them out; this account
integrates them again because their `line` includes formal-apparatus, and
adds [CLAIM-270](../claims.d/CLAIM-270.md), which is in formal-apparatus only and which no account
integrates.*

## The account

- **Symmetry is invariance.** [CLAIM-040](../claims.d/CLAIM-040.md) (the owner's, at U37, conceded at
  A105; counter, demonstrated, Active): symmetry is invariance under
  transformation, and Noether's theorem is "the point". Its body adds:
  "The Noether half carries over only in a limited form".
- **The principle borrowed, the law derived.** [CLAIM-093](../claims.d/CLAIM-093.md) (A105's;
  disclaimed, demonstrated, Active): not every invariance of a stochastic
  or communicative process implies a Noether conservation law. A105:
  "What we can borrow immediately is the symmetry principle." Its note of
  2026-10-13 gives an instance in learning dynamics, where a symmetry of
  SGD's minibatch gradients conserves nothing ([THEORY-211](../theory.d/THEORY-211.md)).
- **The discrete criterion.** [CLAIM-107](../claims.d/CLAIM-107.md) (the manuscript's §4, citing Baez
  and Fong; thesis, demonstrated, Active, version 3): if K f = f the
  observable's expectation is invariant, and it drifts by at most Σ ε_i
  when ‖K_i f − f‖∞ ≤ ε_i. Of the distribution it says: "Only its mean
  is." Its note of 2026-10-10 adds that on a finite irreducible chain only
  constants are harmonic, so "a non-trivial exactly conserved observable
  needs reducible dynamics with several closed classes, a restricted
  state space, or time-dependent kernels".
- **Only the mean.** [CLAIM-094](../claims.d/CLAIM-094.md) (from the reading of Baez and Fong, [NOTE-598](../notes.d/NOTE-598.md);
  granted, demonstrated, Active): Baez and Fong's theorem needs the second
  moment too, and their counterexample "conserves the mean for every
  initial state while the second moment moves". So K f = f "is a
  conservation criterion but not the Noether-type one its section heading
  claims".
- **Retention is not drift.** [CLAIM-270](../claims.d/CLAIM-270.md) (the assistant's restatement of
  [CLAIM-081](../claims.d/CLAIM-081.md)'s general content, split under [ADR-040](../decisions.d/ADR-040.md); thesis, demonstrated,
  Active): I(U_0; U_n) and the divergence of P(U_n) from P(U_0) "come
  apart in both directions". Its note of 2026-10-19 constructs all four
  combinations on two states, "so neither quantity is a function of the
  other".
- **Exact conservation keeps the start.** [CLAIM-635](../claims.d/CLAIM-635.md) (the assistant's
  wording; thesis, demonstrated, Proposed): an observable conserved
  exactly at every step and not constant on the start's support bounds
  I(S_0; S_n) below independently of n, so such a chain cannot converge to
  a law independent of its start; a bounded defect does not prevent
  forgetting. It is admitted by derivation and says of itself: "It joins
  the line's two inquiries."

## The components

- [CLAIM-040](../claims.d/CLAIM-040.md), the owner's at U37, counter, demonstrated, Active; first line
  pragmatic-transport; objects to [CLAIM-015](../claims.d/CLAIM-015.md).
- [CLAIM-093](../claims.d/CLAIM-093.md), A105's, disclaimed, demonstrated, Active; first line
  pragmatic-transport; complements [CLAIM-107](../claims.d/CLAIM-107.md); grounds on [THEORY-211](../theory.d/THEORY-211.md).
- [CLAIM-094](../claims.d/CLAIM-094.md), from the reading of Baez and Fong, granted, demonstrated,
  Active; first line pragmatic-transport; objects to [CLAIM-107](../claims.d/CLAIM-107.md).
- [CLAIM-107](../claims.d/CLAIM-107.md), the manuscript's §4, thesis, demonstrated, Active; first line
  pragmatic-transport; complements [CLAIM-093](../claims.d/CLAIM-093.md); uses [TERM-027](../terms.d/TERM-027.md).
- [CLAIM-270](../claims.d/CLAIM-270.md), the assistant's restatement, thesis, demonstrated, Active;
  formal-apparatus only; grounds on [CASE-017](../cases.d/CASE-017.md).
- [CLAIM-635](../claims.d/CLAIM-635.md), the assistant's, thesis, demonstrated, Proposed; first line
  pragmatic-transport; rests on [CLAIM-107](../claims.d/CLAIM-107.md) and [CLAIM-270](../claims.d/CLAIM-270.md); bears on
  [QUESTION-006](../questions.d/QUESTION-006.md).

## Links the components state, and where

Eight pairs are linked, all inside the cluster:

- **The concession and its limit.** [CLAIM-040](../claims.d/CLAIM-040.md)'s body names [CLAIM-093](../claims.d/CLAIM-093.md) for
  the limit and [CLAIM-107](../claims.d/CLAIM-107.md) and [CLAIM-094](../claims.d/CLAIM-094.md) for where the Noether half holds.
  [CLAIM-093](../claims.d/CLAIM-093.md) complements [CLAIM-107](../claims.d/CLAIM-107.md), and its body cites [CLAIM-107](../claims.d/CLAIM-107.md) "qualified by
  [CLAIM-094](../claims.d/CLAIM-094.md)".
- **The objection taken in.** [CLAIM-094](../claims.d/CLAIM-094.md) objects to [CLAIM-107](../claims.d/CLAIM-107.md); [CLAIM-107](../claims.d/CLAIM-107.md)'s
  version 2 narrowed its title to mean conservation, and its "What it does
  not say" now cites [CLAIM-094](../claims.d/CLAIM-094.md) for both points. [CLAIM-107](../claims.d/CLAIM-107.md)'s "Where it came
  from" names [CLAIM-040](../claims.d/CLAIM-040.md) and [CLAIM-093](../claims.d/CLAIM-093.md).
- **Conservation joined to retention.** [CLAIM-635](../claims.d/CLAIM-635.md) rests on [CLAIM-107](../claims.d/CLAIM-107.md) and
  [CLAIM-270](../claims.d/CLAIM-270.md). Its admission: "no entry joins conservation to retention". Its
  "What it does not say" cites [CLAIM-094](../claims.d/CLAIM-094.md): only the observable's conditional
  mean is kept. It notes the bound holds under each of the three escapes
  [CLAIM-107](../claims.d/CLAIM-107.md)'s note of 2026-10-10 names, and is empty on an irreducible chain.

[CLAIM-270](../claims.d/CLAIM-270.md) is linked to the rest only through [CLAIM-635](../claims.d/CLAIM-635.md).

## Links to other parts, stated

None. No member names a member of the line's other part accounts or of the entries the line account ([SYNTHESIS-088](SYNTHESIS-088.md)) integrates directly, and none of them names a member here. Outside the line, the
cluster reaches [QUESTION-006](../questions.d/QUESTION-006.md) ([CLAIM-635](../claims.d/CLAIM-635.md) bears on it), [CLAIM-081](../claims.d/CLAIM-081.md), [CLAIM-189](../claims.d/CLAIM-189.md)
and [CLAIM-191](../claims.d/CLAIM-191.md) (which rest on [CLAIM-270](../claims.d/CLAIM-270.md)), [TERM-027](../terms.d/TERM-027.md) (which [CLAIM-107](../claims.d/CLAIM-107.md) uses) and
[CLAIM-068](../claims.d/CLAIM-068.md) ([CLAIM-635](../claims.d/CLAIM-635.md)'s "What it adds to the line").

## Where else these entries are integrated

[SYNTHESIS-060](SYNTHESIS-060.md) (pragmatic-transport) integrates [CLAIM-040](../claims.d/CLAIM-040.md), [CLAIM-093](../claims.d/CLAIM-093.md),
[CLAIM-094](../claims.d/CLAIM-094.md), [CLAIM-107](../claims.d/CLAIM-107.md) and [CLAIM-635](../claims.d/CLAIM-635.md). No account integrates [CLAIM-270](../claims.d/CLAIM-270.md).

## Not stated on the record

Tested by [ADR-075](../decisions.d/ADR-075.md)'s step 5 at this review and not filed:

- **Exact conservation fixes retention and leaves drift free.** That
  under exact conservation of a non-constant observable, retention is
  bounded away from zero ([CLAIM-635](../claims.d/CLAIM-635.md)) while the drift of the law can be as
  large as an absorbing walk makes it ([CLAIM-107](../claims.d/CLAIM-107.md)'s "What it does not
  say"). Both halves are held; together they are a conjunction, and
  [CLAIM-635](../claims.d/CLAIM-635.md)'s own "What it does not say" already keeps only the conditional
  mean. Fails as adding nothing.
- **A consequence of symmetry never recovers it.** Set beside the
  readout cluster's [CLAIM-385](../claims.d/CLAIM-385.md) (degeneracy does not identify a symmetry),
  [CLAIM-094](../claims.d/CLAIM-094.md)'s point reads as one pattern. As "can", it is two held
  instances. As a general law it is false on the record: for finite
  continuous-time processes, conservation of mean and second moment for
  every initial law is equivalent to commuting with the generator
  ([THEORY-158](../theory.d/THEORY-158.md), cited in [CLAIM-107](../claims.d/CLAIM-107.md)). That is a realistic separating case
  and shows the general sentence false. Not filed.

## What it does not say

- That real serial reconstruction is Markov, or that any pragmatic
  observable is conserved exactly by actual kernels; [CLAIM-635](../claims.d/CLAIM-635.md) and
  [CLAIM-270](../claims.d/CLAIM-270.md) both disclaim these.
- Anything about [CLAIM-635](../claims.d/CLAIM-635.md)'s standing: it is Proposed, and its clause
  stands or falls with it.
