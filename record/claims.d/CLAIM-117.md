---
number: 117
status: Proposed
formerly:
- CLAIM-tmpx6akp
title: 'Pragmatic fidelity requires preserving the dynamics of interpretation, not only final judgements: a good transport approximately intertwines source and target framing operations under a correspondence anchored to independently measured distinctions'
version: 3
history:
- version: 2
  date: '2026-10-10'
  note: >-
    Restated on 2026-10-10 after CLAIM-238 and CLAIM-253.
    Version 1's condition read: 'Renderings that match on static
    judgement distributions never diverge in how later framings act on
    their readers, so intertwining defects add nothing to the
    prediction of fidelity judgements beyond distribution matching.'
    Its 'never diverge' was a universal negative, and its intertwining
    defects are not identified from data. Stated on observed responses
    (CLAIM-231). The manuscript's §9 identity quoted below is
    unchanged.
- version: 3
  date: '2026-10-29'
  note: >-
    Eleventh status review (ADR-057, ADR-059). CLAIM-011, granted on
    2026-10-08, is written in: intertwining with an uninformative
    correspondence is vacuous or lossy, so the title now names an
    anchored correspondence and 'What it does not say' gives the two
    limits. The old title read: 'Pragmatic fidelity requires
    preserving the dynamics of interpretation, not only final
    judgements: a good transport approximately intertwines source and
    target framing operations'. The defeat condition, on observed
    responses since version 2, uses no Φ and is unchanged.
role: thesis
warrant: interpretive
defeated_if: >-
  Among renderings matched, within a margin fixed in advance, on static
  judgement distributions, differences in observed responses to later
  framings (the order effects of sequence contexts, CLAIM-231) add
  less than a margin fixed in advance to the prediction of receivers'
  task-indexed fidelity verdicts on held-out renderings.
tags:
- philosophy-of-language
- mathematics
date: '2026-10-08'
line: pragmatic-transport
works:
- what-survives-translation
rests_on:
- CLAIM-052
uses:
- TERM-007
- TERM-024
summary: >-
  A30's commuting diagram for pragmatic fidelity, developed in the
  manuscript §9 as intertwining defects and the commutator-distortion
  identity.
objected_by:
- CLAIM-011
- CLAIM-253
illustrated_by:
- CASE-022
- CASE-017
complements:
- CLAIM-231
- CLAIM-298
- CLAIM-063
---

# CLAIM-117: Pragmatic fidelity requires preserving the dynamics of interpretation, not only final judgements: a good transport approximately intertwines source and target framing operations under a correspondence anchored to independently measured distinctions

## The claim

A30: "If interpretation is path-dependent, then pragmatic equivalence between
translations may need to preserve not just distributions of final judgments but
the *dynamics of interpretation*": T_τ(f) Φ ≈ Φ T_f ([TERM-007](../terms.d/TERM-007.md)). Manuscript §9:
"If ΦA≈A'Φ and ΦB≈B'Φ, compare Φ[A,B] with [A',B']Φ", with E_A = ΦA − A'Φ,
E_B = ΦB − B'Φ and Φ[A,B] − [A',B']Φ = E_A B + A'E_B − E_B A − B'E_A. "It makes
preservation of the effects of future frames distinct from agreement on a single
static pragmatic judgment."

## What it does not say

That intertwining under any correspondence counts. A Φ that collapses every
state makes the intertwining vacuous, and a non-injective one makes it lossy
([CLAIM-011](CLAIM-011.md), granted). So the correspondence is one that keeps independently
measured distinctions apart, admissible in [CLAIM-077](CLAIM-077.md)'s sense, and is
estimated on tasks other than those it is evaluated on.

That noncommutativity ([TERM-024](../terms.d/TERM-024.md)) is quantum ([CLAIM-041](CLAIM-041.md)). The identity is algebra (checked in the
workbench entry of 2026-10-09); the claim that the defects matter for fidelity
is empirical and untested.

## Note of 2026-10-15: split under [ADR-043](../decisions.d/ADR-043.md)

[ADR-043](../decisions.d/ADR-043.md)'s classification found this claim compound: the
commutator-distortion identity quoted from the manuscript's §9,
Φ[A,B] − [A',B']Φ = E_A B + A'E_B − E_B A − B'E_A, is algebra and
demonstrated, while the claim that intertwining matters for pragmatic
fidelity is untested and, with no observation under it, interpretive.
The identity is already filed on its own as [CLAIM-063](CLAIM-063.md) (demonstrated), so
no new claim was drafted; this claim now complements it. This claim keeps
the rest, its main conclusion, that pragmatic fidelity requires
preserving the dynamics of interpretation and that a good transport
approximately intertwines framing operations, and stays interpretive.
The identity is quoted above as what the claim was developed into, not
as part of what it states. Its title is unchanged.

## Note of 2026-10-29: what holds it back

It rests on [CLAIM-052](CLAIM-052.md), which is Proposed. No study has yet tested its defeat
condition: whether, among renderings matched on static judgement
distributions, observed order effects add to the prediction of receivers'
fidelity verdicts.
