---
number: 479
status: Active
formerly:
- CLAIM-tmpoe0v5
title: 'In the record a typed relation is more constrained than either of its relata: a claim''s content is open prose, while `rests_on` fixes the scheme at both ends, has `supports` written as its converse and says what retiring its target leaves, and none of that moves when either claim''s content does; so a relation''s rigidity is a fact about the grammar, not evidence that the dependency it records is sound'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  A relation declared in the record's grammar whose endpoints, converse or
  consequence on retirement are left as open as a claim's content is; or a
  check on a claim's content, beyond its required fields and vocabularies,
  as strict as the scheme restriction on `rests_on`.
tags:
- design-rationale
- epistemology
- logic
date: '2026-10-27'
line: nucleating-argument
grounds:
- CASE-131
complements:
- CLAIM-293
- CLAIM-181
summary: >-
  The owner's, U6 of the exchange of 2026-10-27, against A5's "its
  relationships are explicitly represented rather than metaphysically
  primitive": "and yet interestingly, relations like "supports" are less
  flexible than the raw contents of either relata." Shown from luria.yaml,
  which A6 §6 read correctly. The relation's type is determinate where the
  relata's content is not, and that determinacy is no warrant for the
  dependency: [CLAIM-293](CLAIM-293.md) is the demonstrated case. [CASE-131](../cases.d/CASE-131.md) is the instance
  in which the rigidity of a relation outran what its relata meant and the
  grammar was amended.
---
<!-- inactive-ok-file: CLAIM-184 CLAIM-195 CLAIM-419 CLAIM-478 — Proposed; the explanations of the asymmetry, cited as open -->

# CLAIM-479: In the record a typed relation is more constrained than either of its relata: a claim's content is open prose, while `rests_on` fixes the scheme at both ends, has `supports` written as its converse and says what retiring its target leaves, and none of that moves when either claim's content does; so a relation's rigidity is a fact about the grammar, not evidence that the dependency it records is sound

## The claim

A5 §6 had said of the record that "its relationships are explicitly
represented rather than metaphysically primitive". The owner, at U6: "and
yet interestingly, relations like "supports" are less flexible than the
raw contents of either relata."

That is a fact about the grammar, and luria.yaml shows it:

- **A claim's content is open.** A claim's body is prose about anything.
  Its frontmatter has required fields (`role`, a `defeated_if` for a
  thesis, `line`) and closed vocabularies for some of them, and nothing
  checks what the prose says.
- **A relation's endpoints are fixed.** `rests_on` goes from a CLAIM to a
  CLAIM and nothing else; `grounds` goes from a CLAIM to a THEORY, CASE or
  LIT. A6 §6: "`rests_on` relates claims to claims, while `grounds` relates
  claims to external evidential resources".
- **Its converse is not the author's.** `supports` is declared "the
  converse of `rests_on`, written by `luria link --fix`", and is also the
  converse of `grounds` on the evidence's side. Nobody writes a `supports`;
  it is entailed by someone else's `rests_on`.
- **Its consequence is fixed.** `rests_on` is "another of the record's own
  claims this one could not stand without … Retired, it leaves this claim
  needing another route", and it is the spine the `argument` chain walks.
  `corroborates` has the same endpoints and a different consequence: "If
  this one is retired, the other loses support, not its footing"
  ([ADR-044](../decisions.d/ADR-044.md)). What separates the two relations is only what follows from
  them.

Each of these holds whatever either claim says, and survives any rewrite
of either. A6 §6: "The contents of A and B might change substantially while
this relation remains", and "the relation organizes the propagation of
epistemic consequences without being a truth-preserving logical
implication."

## Why the rigidity is not soundness

A6 §7: "the type system can enforce that an edge has allowable endpoints
without establishing that the claimed evidential dependency is actually
sound. So `supports` may be structurally rigid while being epistemically
mistaken." A9 §8: "Two claims can satisfy every structural check in Luria
and still stand in an invalid evidential relationship." The record has
the demonstrated form of this already: two support graphs with the same
edges can carry evidence of different strength and call for different
revisions ([CLAIM-293](CLAIM-293.md), from [CASE-089](../cases.d/CASE-089.md)). So the relation's type is determinate
and its instance can still be wrong; the claim is about the first.

## When the rigidity outran the relata

[CASE-131](../cases.d/CASE-131.md) is the instance the exchange did not find. A claim gave evidence
for another without the other depending on it. The grammar could say this
only as `supports`, and the link fixer then wrote the entailed `rests_on`
onto the other claim: the relation's fixed converse asserted an inference
neither claim made. The fix was in the grammar, not in the claims
([ADR-044](../decisions.d/ADR-044.md) added `corroborates`; [CLAIM-419](CLAIM-419.md) lists it among the amendments).
A7 §4 found the same shape in luria's own record ([LU-DP-016](https://github.com/dmarx/luria/blob/main/docs/design-principles.md#dp-16)): an
`overrides` edge whose target held two claims under one code, where "the
relation constrained the permissible identity of the relatum" and the
target was split. That stronger reading, that a relation can settle how its
relata must be individuated, is [CLAIM-476](CLAIM-476.md)'s, and is interpretive;
this claim is only the asymmetry.

## What it does not say

- **Not that relations are prior to relata in the record.** Every relation
  needs both ends to have codes first; the grammar presupposes its relata,
  as the Yoneda lemma does ([CLAIM-150](CLAIM-150.md)).
- **Not that content is unconstrained.** Prose is checked for unresolved
  references, and a thesis must say what would defeat it.
- **Not that this generalizes.** That the same asymmetry holds outside the
  record, between physical relations and their relata, is part of what
  [CLAIM-477](CLAIM-477.md) claims, and it is interpretive there.

## Note of 2026-10-27 (later): why the relation is rigid

The exchange's later turns offered two explanations of the asymmetry this
claim shows, and the record already holds both. A11 took Wimsatt's generative
entrenchment: "A constraint can acquire practical rigidity because many
downstream processes depend on it", with indexes, chains, validation and
migration all built on a relation type. That is [CLAIM-184](CLAIM-184.md) ("Anchors entrench"),
which A11 did not cite. A12 took rates: the relation's "rigidity might reflect a
disparity in characteristic rates of change, combined with mechanisms that
maintain and enforce them". A relation type changes by decision, on the
grammar's slow time scale ([CLAIM-195](CLAIM-195.md), [CLAIM-419](CLAIM-419.md)), while the prose of its relata
changes at every edit. That is [CLAIM-478](CLAIM-478.md)'s mechanism. Both explain the
rigidity this claim demonstrates; neither is part of it.

## Note of 2026-10-27 (latest): the rigidity in the rates

[CASE-180](../cases.d/CASE-180.md) shows the rigidity this claim demonstrates from the grammar as
a disparity of rates as well. Of 6632 authored relation instances, 149 were
retracted, a median of 0.18 days after they were written, so as drafting
corrections. Relation types have been added on seven days of the history and
none has been redeclared. Prose, once drafting is over, is revised about
once in 22 days. The previous note said a relation type "changes by decision,
on the grammar's slow time scale". The measurement narrows that. The record
does not revise a type; it adds one beside it, as [ADR-044](../decisions.d/ADR-044.md) added `corroborates`
beside `rests_on` after [CASE-131](../cases.d/CASE-131.md). What is slow is redeclaration, not the
grammar's growth.
