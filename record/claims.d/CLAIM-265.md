---
number: 265
status: Proposed
formerly:
- CLAIM-tmpavkxk
title: 'Local descriptions that disagree are not thereby incompatible: whether
  they obstruct a joint description is decided only relative to a specified class
  of admissible correspondences between their observations, and a correspondence
  admitted only because it removes the disagreement decides nothing'
version: 2
history:
- version: 1
  date: '2026-10-13'
  note: Split from CLAIM-143 under ADR-040, at the owner's request ("go ahead
    with the group B splits"). The assistant restated the general content
    without the premises about translation that CLAIM-143 rests on; CLAIM-143
    now rests on this claim.
- version: 2
  date: '2026-10-19'
  note: Title and defeat condition restated relative to a class of admissible
    correspondences (promotion audit, batch 040, carrying batch 035's finding
    on CLAIM-143). The singular "only once the correspondence is fixed" was
    too strong, since a disagreement can survive every member of a class with
    no one member fixed; and the proviso held only for correspondences
    admitted because they remove the disagreement. The derivation is in the
    note of 2026-10-19, so the warrant moves to demonstrated under ADR-043
    v2. Status unchanged.
role: thesis
warrant: demonstrated
defeated_if: A case in which two local descriptions are shown to obstruct
  a joint description, or shown to be compatible, with no class of admissible
  correspondences between their observations specified. Or an argument that a
  correspondence admitted only because it removes a disagreement is evidence
  that the descriptions were compatible.
tags:
- mathematics
- philosophy-of-science
- contextuality
date: '2026-10-13'
line:
- formal-apparatus
grounds:
- CASE-039
summary: The general content of [CLAIM-143](CLAIM-143.md), filed alone under [ADR-040](../decisions.d/ADR-040.md) so that
  the order of tests does not rest on [CLAIM-011](CLAIM-011.md), [CLAIM-004](CLAIM-004.md) and [CLAIM-035](CLAIM-035.md),
  which are about translation. Disagreement between local descriptions sorts
  into a coordinate difference, a structural transformation or a global obstruction,
  and the sort cannot be made until a class of admissible transition maps is given. Inertial
  frames ([CASE-039](../cases.d/CASE-039.md)) show disagreement with no obstruction once the maps are
  known.
supports:
- CLAIM-143
---
<!-- inactive-ok-file: CLAIM-004 CLAIM-143 — Proposed; cited for what each holds or applies, open, not settled -->

# CLAIM-265: Local descriptions that disagree are not thereby incompatible: whether they obstruct a joint description is decided only relative to a specified class of admissible correspondences between their observations, and a correspondence admitted only because it removes the disagreement decides nothing

## The claim

Two local descriptions can assign different values to what look like the
same observables. That alone shows no incompatibility. There are three
cases, and they should not be conflated:

- **Coordinate difference:** compatible transition maps reconcile the
  descriptions. Inertial frames that disagree about temporal order are the
  example ([CASE-039](../cases.d/CASE-039.md)).
- **Structural transformation:** the descriptions stay comparable but are
  no longer equivalent.
- **Global obstruction:** they cannot be jointly extended under the stated
  compatibility conditions, as in sheaf contextuality.

Which case holds can be decided only relative to a specified class of
admissible correspondences between the descriptions' contexts and
outcomes, each coherent with restriction. The order of tests is the
claim: specify the class, then ask whether what remains is a
transformation or an obstruction. A single correspondence is one such
class; a verdict can also hold over a whole class without any one member
being fixed (note of 2026-10-19).

**The proviso.** A correspondence admitted only because it makes the
disagreement disappear decides nothing. The class must be justified or
validated independently of the disagreement it is used to assess.

## Where the record applies it

[CLAIM-143](CLAIM-143.md) applies the order of tests to source and target judgements in
translation, where the correspondence is the context part of a transport.
It rests on [CLAIM-011](CLAIM-011.md), [CLAIM-004](CLAIM-004.md) and [CLAIM-035](CLAIM-035.md) for that application, and
now on this claim for the order of tests.

## What it does not say

- It does not say every domain has transition maps. Relativity has them;
  that another domain does is a separate question.
- It does not say any map that removes a disagreement shows a mere change
  of description. The map has to be anchored first.

## Note of 2026-10-19: why the verdict is relative to a class

Promotion audit, batch 040. Write V(D1, D2, C) for the verdict on two
local descriptions D1 and D2 under a class C of correspondences between
their contexts and outcomes, each coherent with restriction. D1 and D2 are
compatible relative to C if some member of C carries D1 onto a
description that agrees with D2 on every shared context. They obstruct
relative to C if no member does.

1. **Disagreement does not entail incompatibility.** The inertial frames
   of [CASE-039](../cases.d/CASE-039.md) assign different simultaneity relations, and the Lorentz
   maps carry one onto the other. One case settles a negated entailment.
2. **The verdict varies with the class.** Take one shared context with
   two outcomes. D1 assigns (1/2, 1/2) and D2 assigns (1/3, 2/3). Let C be
   the bijections of outcomes. Both bijections carry D1 to (1/2, 1/2),
   which is not (1/3, 2/3), so D1 and D2 obstruct relative to C. Let C' be
   all maps of outcomes, applied to both descriptions, including the map
   onto a single outcome. That map carries both to (1), so D1 and D2 are
   compatible relative to C'. The same pair gets opposite verdicts, so
   there is no verdict until a class is specified.
3. **No single correspondence need be fixed.** The obstruction in step 2
   holds for every member of C at once, and no one bijection was chosen.
   So "only once the correspondence is fixed", in the singular, is
   stronger than what holds. A fixed correspondence is the special case of
   a class with one member.
4. **The proviso.** Relative to the class of all maps, every pair of
   descriptions is compatible, by the map onto a single outcome. That a
   reconciling correspondence exists therefore says nothing about a given
   pair unless the class was specified first, independently of the
   disagreement. Inside a class so specified, finding a reconciling member
   is the compatibility verdict for that class. So the proviso holds for
   correspondences admitted only because they remove the disagreement, and
   no further.

Steps 1 to 4 establish the title as restated. They leave the three-way
classification and its application to translation ([CLAIM-143](CLAIM-143.md)) as
they were.
