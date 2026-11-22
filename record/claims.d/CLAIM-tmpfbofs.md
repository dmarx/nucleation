---
status: Proposed
title: 'An effective symmetry or conservation law meets the relata–realization frame''s definition of a constraint, realized by the organization of the level below it and maintained only while that organization holds; a symmetry taken as fundamental is realized only as a specification is, by the processes that obey it, and is maintained by nothing, so it is a candidate for the frame''s second defeater that no physical result can supply, since no result shows a law fundamental, and the frame should say that its recursion is claimed for constraints effective at some level'
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  Any of three. (i) An argument that the record should take a symmetry of
  the current fundamental theories as fundamental for the purpose of the
  frame's defeater (b), so that the defeater is met now for the kinds it
  individuates; that is the reading of CLAIM-tmph783a. (ii) The owner's
  reading of the frame's "realized and maintained by something" as the
  thin sense, a law realized by whatever obeys it, so that defeater (b)
  cannot fire for laws by design. (iii) An effective symmetry or
  conservation law that does individuating work and whose force is shown
  not to vary with any change in the organization below it that realizes
  it. Not defeated by a symmetry for which no level below is known, which
  this claim grants is the common case at the fundamental level.
tags:
- metaphysics
- individuation
- philosophy-of-science
date: '2026-11-22'
line:
- distributed-agency
- pragmatic-transport
answers:
- QUESTION-450
bears_on:
- QUESTION-284
grounds:
- THEORY-158
- THEORY-1323
- THEORY-1078
objects_to:
- CLAIM-tmph783a
complements:
- CLAIM-tmpr0sfe
uses:
- TERM-070
summary: >-
  Alternative 1 of two (leaned to) for [LEAD-195](../leads.d/LEAD-195.md)'s first question:
  does a symmetry or conservation law meet [CLAIM-477](CLAIM-477.md)'s definition, that the
  constraints which partly fix what an entity is "are themselves realized
  and maintained by something"? Split by whether the law is effective. An
  effective one does, and the record holds a worked case with the realizer
  named ([THEORY-158](../theory.d/THEORY-158.md)). A fundamental one does not in the sense
  [TERM-070](../terms.d/TERM-070.md) gives "maintained", so it is the candidate for defeater (b);
  but (b) is stated as a result, and being fundamental is not something a
  result shows, so the candidate is a condition on the claim's scope, not a
  defeat. Alternative 2 is [CLAIM-tmph783a](CLAIM-tmph783a.md). The possibility-fact half is
  [CLAIM-tmpr0sfe](CLAIM-tmpr0sfe.md). The wording is the assistant's (Claude, in this
  session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-tmph783a CLAIM-tmpr0sfe CLAIM-tmp6sa56 — new; the alternatives and the possibility-fact rulings filed with this claim for LEAD-195 -->
<!-- inactive-ok-file: CLAIM-477 CLAIM-478 CLAIM-134 — Proposed; the frame whose definition is at issue, the rate-difference claim's ruling on conservation, and the Wigner discussion -->

# CLAIM-tmpfbofs: An effective symmetry or conservation law meets the relata–realization frame's definition of a constraint, realized by the organization of the level below it and maintained only while that organization holds; a symmetry taken as fundamental is realized only as a specification is, by the processes that obey it, and is maintained by nothing, so it is a candidate for the frame's second defeater that no physical result can supply, since no result shows a law fundamental, and the frame should say that its recursion is claimed for constraints effective at some level

## The question

[CLAIM-477](CLAIM-477.md) holds that what an entity is, is partly fixed by the
constraints on the configurations it can enter, and that "those
constraints are themselves realized and maintained by something". Its
defeater (b) is "A constraint that does individuating work while realized
by nothing, a specification prior to every realization, which would make
constraints prior without qualification for the kinds it individuates."
Its notes of 2026-10-27, 2026-10-29, 2026-10-30 and 2026-11-06 name a
symmetry or conservation law as the candidate and leave it unruled, and
[QUESTION-450](../questions.d/QUESTION-450.md) states it on its own. [LEAD-195](../leads.d/LEAD-195.md) asks for the ruling.

## What the definition asks

The claim uses "realized and maintained" in a thick sense, and says so.
Its read prior art is closure of constraints ([TERM-070](../terms.d/TERM-070.md)): a constraint
acts on a process at a time scale at which its relevant aspects are
conserved, and is produced by processes at another. A10 §7's
role-relativity, which the claim quotes, says the same across levels:
"Constraint at level n ≈ realized organization at level n−1". A8's
recursion is that constraints "are themselves realizations within larger
relational structures". So a constraint meets the definition when
something other than the constraint produces it and its holding depends
on that something continuing. "Maintained by something" is not
"maintained by itself", as the claim's "What it does not say" adds.

There is also a thin sense the claim does not mean: a law is realized by
whatever obeys it, as a specification is by what meets it. That is the
claim's first axis (specification to realization, the table under "Two
axes"), not its recursion. Read thinly, every law is realized by its
instances, defeater (b) could never fire for a law, and "maintained"
would do no work. A defeater that cannot fire is no defeater, so the
thick sense is the one to rule under.

A symmetry or conservation law is a constraint in the claim's sense. It
restricts which configurations and transitions are admissible, and it
individuates kinds: Wigner's classification makes a particle kind an
irreducible representation of the Poincaré group ([CLAIM-134](CLAIM-134.md)'s partial
reply). So the only question is whether it is realized and maintained.

## An effective symmetry or conservation law meets it

The record holds a case with the realizer named. In a finite Markov
process an observable is conserved, its mean and variance alike in every
state, exactly when it is constant on each connected component of the
transition graph ([THEORY-158](../theory.d/THEORY-158.md), Baez and Fong, re-derived here). Which
quantities are conserved is then fixed by which transitions the dynamics
realizes. Add one transition between two components and a conservation
law is gone; it holds exactly as long as the barrier between components
holds. That is the definition met: the law is produced by an
organization other than itself, and maintained by that organization's
persisting.

Two further cases are of the same kind.

- **Yang and Abanin** ([THEORY-1323](../theory.d/THEORY-1323.md), read in [NOTE-1534](../notes.d/NOTE-1534.md)): under weak noise
  the conserved sector is what an observable comes to over a window set
  by the noise and the system's chaos. [CLAIM-478](CLAIM-478.md)'s note of 2026-11-02
  ruled that "an exact conservation law is the limit of slowness". The
  limit is reached as the noise that would break the law goes to zero, so
  how far the law holds is set by the dynamics realizing it.
- **[CLAIM-480](CLAIM-480.md)**: the boundary coupling a composite leaves when its
  interior is eliminated is a constraint realized by the interior and
  changing with it.

And the record holds one historical case. Parity invariance was taken as
a principle and "refuted in just that way" ([THEORY-1078](../theory.d/THEORY-1078.md), the paper's
footnote 1). Where parity holds, it holds of some interactions and not
others, which is how an effective constraint behaves.

## A symmetry taken as fundamental does not, and that is not yet a defeat

Suppose a symmetry has no organization below it: the Poincaré symmetry
of the current fundamental theories, if it is final.

- **Realized only thinly.** The particles realize the kinds the symmetry
  fixes. They do not realize the symmetry. It is realized only in the thin
  sense, by everything that obeys it. To say that spacetime geometry
  realizes it moves the question to the geometry, which nothing is known
  to maintain either.
- **Maintained by nothing.** It is conserved at every time scale and
  produced at none, so it meets the first half of [TERM-070](../terms.d/TERM-070.md)'s condition
  and not the second.

So the claim's recursion does not reach a fundamental law, and such a law
would be defeater (b)'s case. But (b) is written as a result, and two
things stand between the candidate and a result.

1. **No result shows a law fundamental.** Physics can show that a
   symmetry is effective, by finding what breaks it or what it emerges
   from. It cannot show that nothing lies below a symmetry, only that
   nothing below is known. The one case the record holds went the other
   way.
2. **A fundamental law individuates while "realized by nothing" only on
   one metaphysics of laws.** On a reading where a law is something over
   and above the processes it holds of, it is realized by nothing. On a
   reading where it is a pattern in those processes, it is realized by
   them, thinly. The record has not ruled between these, and the claim
   should not wait on that ruling.

So no symmetry or conservation law meets defeater (b) as things stand,
and none could by physics alone. The candidate is not dismissed. It
becomes a condition on the claim's scope, which the claim should state.

## What it changes in [CLAIM-477](CLAIM-477.md)

A revision, proposed in a dated note there and not applied. "What it
does not say" would gain one bullet: the recursion is claimed for
constraints effective at some level, which are all the claim's cases; of
a law that is fundamental, if any is, the claim says only that the
processes obeying it realize it as a specification, not that anything
maintains it. Defeater (b) would add that a symmetry or conservation law
shown fundamental, read as more than its instances, would meet it, and
that having no known realizer below it is not that result. The claim's
last clause, "neither ... prior without qualification", would then stand
for every kind whose constraints are effective, and be silent on kinds
fixed by a fundamental law.

## What it does not say

- **That no symmetry is fundamental.** It says only that no result shows
  one is.
- **That a fundamental law is realized by its instances.** It says the
  claim should not depend on whether it is.
- **That an effective law is less real.** [CLAIM-477](CLAIM-477.md)'s realized
  constraints are real constraints, and so is an effective conservation
  law.
- **Anything about identity.** Wigner's classification fixes kinds, not
  which member is which ([CLAIM-134](CLAIM-134.md)). Defeater (b) counts kinds, so this
  does not affect the ruling.

## Alternative

[CLAIM-tmph783a](CLAIM-tmph783a.md) reads the record's physics at face value: the
symmetries of the current fundamental theories are fundamental, so (b) is
met now for elementary particle kinds, and [CLAIM-477](CLAIM-477.md) holds only above
them. The two differ on whether a defeater about laws may be met by the
best current theory or needs a result. Choosing is the owner's. The
possibility-fact rulings, [CLAIM-tmpr0sfe](CLAIM-tmpr0sfe.md) and [CLAIM-tmp6sa56](CLAIM-tmp6sa56.md), can be
combined with either.
