---
number: 200
status: Superseded
superseded_by:
- ARG-tmp928rv
formerly:
- CLAIM-tmp0stxa
title: "The procedure-level fidelity thesis's title says observational fidelity is not defined for a single rendering of a single item, which is more than it shows: one source–target pair does not identify the procedure-level score, and a single rendering can still be judged, as a sample of its procedure or by another measure stated as such, as its own body says"
version: 2
history:
- version: 2
  date: '2026-10-28'
  note: >-
    Moved to ARG-tmp928rv under ADR-061: the claim says what CLAIM-228's
    derivation does and does not show, which is a verdict on support. The
    argument, from CLAIM-207, CLAIM-011 and CLAIM-381 to CLAIM-228, is
    Active as to CLAIM-228's version 2 and records that the inference to
    version 1's title failed. The text below is unchanged.
role: granted
warrant: demonstrated
tags:
- probabilistic-modeling
- translation
date: '2026-10-10'
line: pragmatic-transport
summary: >-
  The interlocutor's second refinement at U62 (A240), checked against
  [CLAIM-228](CLAIM-228.md)'s text and granted on 2026-10-10. Version 1's title ended
  "for a single rendering of a single item it is not defined"; its body
  says only that this measure does not judge a single rendering, and
  that one is judged as a sample of its procedure or by another measure.
  Granted because it can be checked by reading. Repaired in
  [CLAIM-228](CLAIM-228.md)'s version 2, which changes the title only. It does not
  touch the derivation or the defeat condition.
---
<!-- inactive-ok-file: CLAIM-228 — Proposed; the claim this objection is to, repaired at version 2 and still open on its defeat condition -->
<!-- inactive-ok-file: ADR-061 — Proposed; the decision under whose migration this entry was filed or revised -->

# CLAIM-200: The procedure-level fidelity thesis's title says observational fidelity is not defined for a single rendering of a single item, which is more than it shows: one source–target pair does not identify the procedure-level score, and a single rendering can still be judged, as a sample of its procedure or by another measure stated as such, as its own body says

## The objection

At U62 the owner asked "how would you suggest we update or modify the
theses?" The assistant's answer (A240) recommended for [CLAIM-228](CLAIM-228.md):
"Retain as a methodological proposition, not the definition of all
fidelity", because "Its procedure-level observational score is well
motivated, but single-token evaluations can still have meaning under other
metrics". Its second refinement:

> **Second, distinguish a procedure-level transport claim from an
> item-level fidelity judgment.** A family of stochastic kernels fitted
> across source items can be tested for generalization. But it does not
> follow that an individual translated utterance has no fidelity
> properties. It means only that the proposed *procedure-level
> distributional score* is not identified by one isolated pair.

and its reason: "That prevents a repair to one metric from turning into an
unnecessarily broad metaphysical assertion."

**Against the title as written, it is right.** Version 1's title ended: "for
a single rendering of a single item it is not defined". The subject of that
clause is observational fidelity, not the measure, so read alone it denies
that a single rendering has the property at all.

The body says less, three times:

- "So it is not defined as a measure."
- "A single rendering such as Henley's Villon ([CASE-010](../cases.d/CASE-010.md)) is judged as a
  sample of the procedure that produced it, or by another measure stated as
  such".
- "It does not say a single translation cannot be judged, only that this
  measure does not judge it."

The objection it answers says the same: [CLAIM-230](CLAIM-230.md)'s remedy is "For
single renderings, a different measure, stated as such." So the derivation
shows only what A240 says it shows: one source–target pair does not
identify the procedure-level score, because for one pair a kernel can make
the per-item term zero ([CLAIM-207](CLAIM-207.md)).

Granted because the point is checked by reading the entry against its own
title. The repair is [CLAIM-228](CLAIM-228.md)'s version 2, which restates the title
and leaves the derivation, the defeat condition and the body unchanged.

## What it does not say

- It does not say the procedure-level score is wrong, or that the
  constant-kernel argument fails for one pair. Both stand.
- It does not say any per-item measure exists or is any good. It says the
  title should not deny one.
- It does not take up A240's wider phrase, "not the definition of all
  fidelity". The claim was always scoped to observational fidelity as D_obs
  measures it; the overreach was the title's "not defined".

## Note of 2026-10-28: moved to [ARG-tmp928rv](../arguments.d/ARG-tmp928rv.md)

This objection was about what [CLAIM-228](CLAIM-228.md)'s derivation shows: that one
source–target pair does not identify the procedure-level score, and not
that a single rendering lacks fidelity. Under [ADR-061](../decisions.d/ADR-061.md) that is the argument
[ARG-tmp928rv](../arguments.d/ARG-tmp928rv.md), from [CLAIM-207](CLAIM-207.md), [CLAIM-011](CLAIM-011.md) and [CLAIM-381](CLAIM-381.md) to [CLAIM-228](CLAIM-228.md). It is
Active for the repaired title, and its body records that the inference to
version 1's title failed, as this claim said.
