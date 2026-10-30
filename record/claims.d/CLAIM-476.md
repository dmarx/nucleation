---
number: 476
status: Proposed
formerly:
- CLAIM-tmpl228b
title: 'Beyond what it does operationally, luria is an apparatus in Barad''s constitutive sense for the objects of a record, and only for them: the record''s objects are constituted, and not only made referable and governable, by the distinctions its grammar enacts, so that the same authored material is a different set of objects under a revised apparatus, and the record''s own inquiry reconstitutes the apparatus that constitutes them'
version: 3
history:
- version: 2
  date: '2026-10-27'
  note: >-
    Split at the owner's review of the pull request. Version 1 was titled
    "Luria is an apparatus in Barad's sense for the objects of a record, and
    only for them: its grammar settles which distinctions among entries are
    determinate and consequential, a split scheme or a promoted vocabulary
    makes one object two or a value an entity, and misfits met in use revise
    the grammar, so a record's objects are constituted relative to an
    apparatus that the record's own inquiry reconstitutes". Its operational
    content is now CLAIM-469, on which this rests; this claim keeps the
    constitutive thesis, which needs an argument the operational facts do
    not supply. Defeater rewritten to match; status, role and warrant
    unchanged.
- version: 3
  date: '2026-10-29'
  note: >-
    Relations corrected by the fifteenth status review (ADR-057,
    ADR-058), at the status review's ruling (the owner delegated these
    rulings). LIT-1653 and LIT-1657 leave grounds: both are Unavailable
    and unread, and the sense of apparatus compared is the exchange's
    account and her readers' quotations, which TERM-087 carries. The
    third defeater read 'Or, on Barad's own terms, that her apparatus
    cannot be carried to a record without the quantum premise she
    grounds it in (the template conception Jaksland finds she rejects;
    the note of the readings below)'; THEORY-1083 shows Barad rejects the
    template reading, which the note of 2026-10-27 (later) already
    conceded by taking it, so the defeater now says the claim stands on
    that reading. Status unchanged.
role: thesis
warrant: interpretive
defeated_if: >-
  A showing that "constituted" adds nothing to CLAIM-469's "made
  referable and governable": that every consequence this claim draws from
  constitution follows from the operational facts alone, so that the
  Baradian description is a redescription. Or a showing that the record's
  objects are individuated independently of its grammar (by its files,
  say), so that the grammar only describes them. Or a showing that
  Barad's concept of an apparatus cannot be detached from the quantum
  premise she grounds it in, so that on the template reading this claim
  takes, which Barad rejects (THEORY-1083), the concept has no content
  left to carry to a record.
tags:
- design-rationale
- epistemology
- metaphysics
date: '2026-10-27'
line: nucleating-argument
rests_on:
- CLAIM-469
- CLAIM-419
- CLAIM-195
- CLAIM-479
grounds:
- CASE-131
complements:
- CLAIM-183
- CLAIM-181
uses:
- TERM-087
summary: >-
  The owner's, U7 of the exchange of 2026-10-27: "oh shit, I think I may
  have inadvertently operationalized this notion of apparatus already,
  check out github.com/dmarx/luria". Split at the owner's review of the
  pull request. What luria demonstrably does, differentiating, retaining,
  enforcing and revising the distinctions that fix a record's objects, is
  now [CLAIM-469](CLAIM-469.md), stated without Barad. This claim keeps the further,
  constitutive thesis: those objects are constituted in Barad's sense, not
  only made governable. That needs an argument the operational facts do
  not supply, and the readings press on it, since Barad rejects carrying
  agential realism as a template. Barad is unread here.
---
<!-- inactive-ok-file: CLAIM-470 TERM-089 LIT-1652 — Proposed, Open, Rejected, Deferred or new; cited in the note of U15–U23, as open -->
<!-- inactive-ok-file: LIT-1665 — Deferred; registered unread -->
<!-- inactive-ok-file: CLAIM-469 CLAIM-419 CLAIM-195 CLAIM-181 CLAIM-183 — Proposed; the claims about the record's grammar this one rests on or sits beside, cited as open -->
<!-- inactive-ok-file: LIT-1653 LIT-1657 LIT-1650 LIT-1661 — Deferred or Unavailable; registered from the same exchange, unread, cited for what they are standardly cited for -->

# CLAIM-476: Beyond what it does operationally, luria is an apparatus in Barad's constitutive sense for the objects of a record, and only for them: the record's objects are constituted, and not only made referable and governable, by the distinctions its grammar enacts, so that the same authored material is a different set of objects under a revised apparatus, and the record's own inquiry reconstitutes the apparatus that constitutes them

## The claim

A6 had given Barad's apparatus as "an open-ended, dynamic configuration
of material practices through which particular differences become real
and intelligible", productive rather than receptive, inside the
phenomenon rather than outside it, and itself historically constituted,
and the agential cut as the differentiation it enacts ([TERM-087](../terms.d/TERM-087.md)).
The owner, at U7: "oh shit, I think I may have inadvertently
operationalized this notion of apparatus already, check out
github.com/dmarx/luria".

A7 read luria and agreed in a qualified form. Its split:
"**Demonstrable:** Luria constitutes and maintains distinctions *within a
governed knowledge system*. **Philosophical hypothesis:** Such mechanisms
are instances of a more general process through which entities and their
boundaries become ontologically determinate." Version 1 of this claim took
the first, under Barad's name. At the owner's review the first was split out
as [CLAIM-469](CLAIM-469.md), the operational claim, in [TERM-089](../terms.d/TERM-089.md)'s sense. This claim
now holds what goes beyond it. The record's objects are constituted by the
apparatus in Barad's sense: what the record is about changes with the
apparatus, and not only what it can register. That remains short of A7's
general ontological hypothesis, since it is restricted to a record's objects.

The three points below are the operational facts this claim rests on, as
[CLAIM-469](CLAIM-469.md) states them. The constitutive reading of them is in A7 §6's
formalization and in [CLAIM-195](CLAIM-195.md).

Three things make luria an apparatus for a record's objects, and not a
description of objects individuated without it.

- **The grammar settles what counts as a distinct object.** Whether two
  propositions are one entry or two, whether a work and a recommendation
  drawn from it can carry different standing, whether a word is a value
  or an entity, is fixed by the schemes, vocabularies and relations, and
  luria's guide to designing a record (docs/modeling.md, as A7 read it)
  makes that its central question. A7 §2: "The cut
  doesn't bring the paper or recommendation into physical existence. But
  it constitutes them as differently governable epistemic objects." Its
  strongest example is promotion ([LU-ADR-124](https://github.com/dmarx/luria/blob/main/record/decisions.d/ADR-124.md)): a vocabulary that needs to
  say more becomes a scheme, and a value with a label becomes an entry with
  its own status, history and relations. "The system has changed what kind
  of thing the value is permitted to be."
- **The distinctions are consequential.** A distinction the grammar holds
  is checked, propagated along declared relations and visible in
  generated views; one held only in prose is not. A7: "What does it mean
  for a distinction to exist if nothing in the system can register,
  enforce, or act upon that distinction?" The typed relation is the
  load-bearing case ([CLAIM-479](CLAIM-479.md)).
- **Use revises the apparatus.** This is what A7 called the Baradian part
  and named "a reflexive epistemic apparatus": friction met in filing is
  read as a defect of the grammar and answered by amending it. Luria
  states it as a principle ([LU-DP-016](https://github.com/dmarx/luria/blob/main/docs/design-principles.md#dp-16), "An awkward structure is reporting a
  distinction the model has stopped expressing"). This record states it as
  a finding about itself ([CLAIM-419](CLAIM-419.md), from the owner's U18 of 2026-10-22:
  "when we've encountered representational challenges, we've generally
  interpreted those as a symptom of a represntational weakness of the
  record"), with five amendments as evidence, and [CASE-131](../cases.d/CASE-131.md) as the one in
  which a fixed relation misrepresented its relata. [CLAIM-195](CLAIM-195.md) is why the
  result is constitutive and not only descriptive: the constraint set a
  claim's persistence is relative to "defines what the objects are", and
  is fixed by an amendable decision.

A7 §6 put it formally. With the apparatus at time t as A_t = (O_t, M_t,
E_t), ontology, governing rules and executable machinery, and the
authored material D_t, findings and judgment feed back, (A_t, D_t) → F_t →
J_t → A_{t+1}, and Obj(A_t, D_t) need not equal Obj(A_{t+1}, D_t): the same
material decomposes into different objects under a revised apparatus. That
is the claim's "constituted relative to an apparatus that the record's own
inquiry reconstitutes."

## What it does not say

- **Not that luria enacts Barad's intra-action.** A7: "The formalization
  presupposes a representation of D_t, the authored material. In that
  sense, it does not enact Barad's strongest claim that relata have no
  determinate existence prior to intra-action." A5 §6: the record "still
  uses independently addressable claim records".
- **Not that it reproduces quantum measurement, or supports Barad's
  reading of it.** A10 §3: "an institutional and computational example of
  enacted differentiation—not evidence that Luria has reproduced quantum
  measurement." Faye and Jaksland ([LIT-1672](../literature.d/LIT-1672.md)) dispute that quantum
  mechanics supports agential realism at all; the comparison here borrows
  the notion of an apparatus, not the interpretation.
- **Not that physical or biological individuation works so.** That is the
  epistemology-to-ontology step the record keeps apart ([CLAIM-150](CLAIM-150.md)), and
  the general frame is [CLAIM-477](CLAIM-477.md)'s.
- **Not that the record is self-maintaining.** A9 §6: luria's ability to
  revise its schema "is not sufficient to make it autopoietic. Its
  operation depends on maintainers, computers, institutions, and
  surrounding infrastructure." [CLAIM-195](CLAIM-195.md) says the same: the grammar "is
  maintained from outside, in luria's repository and by the owner." In A9's
  regimes it is adaptive, not organizationally closed.
- **Not that every misfit is caught, or that the distinctions are the right
  ones.** [CLAIM-419](CLAIM-419.md)'s limit stands: a move forced silently into a wrong
  shape leaves no decision behind. An apparatus that constitutes objects
  can constitute the wrong ones.
- **Not Barad's own reading.** Barad is unread here ([LIT-1653](../literature.d/LIT-1653.md),
  [LIT-1657](../literature.d/LIT-1657.md)); the sense of apparatus compared is A4 and A6's account
  of her.

## What would test it beyond the record

A7 §7 and A9 §13 proposed the same experiment: one corpus filed under two
apparatuses, for instance two propositions held as one claim in one and as
two linked claims in the other, or untyped citations against typed
dependencies with separate standing and warrant. "The crucial variable
isn't merely the number of files or generated graph nodes. It's whether
the different ontology yields **different trajectories of inquiry**":
which contradictions become visible, which claims are split, which errors
are kept. A9: "The crucial empirical test would be whether changing the
apparatus causes differences in subsequent inquiry that cannot be
explained simply as alternate visualizations of unchanged information."
That would test Hacking's second, looping effect ([LIT-1650](../literature.d/LIT-1650.md)), that the
classification changes the inquiry classified. This claim asserts only the
first, constitutive effect, which the record's amendments already show.
The experiment is not built.

## Note of 2026-10-27 (later): the comparison is on the conception Barad rejects

Jaksland 2024 ([LIT-1673](../literature.d/LIT-1673.md), read in [NOTE-1230](../notes.d/NOTE-1230.md)) separates three
conceptions of agential realism: analogy, a template that quantum mechanics
and other domains each instantiate, and naturalized metaphysics applied
once to the one reality. Barad holds the third and rejects the other two
([THEORY-1083](../theory.d/THEORY-1083.md)): "I am not interested in drawing analogies between
particles and people" (2007, 24), and a template would stratify ontology
into realms, where "the universe is not broken up into two separate
domains" (2007, 85).

This claim compares luria with Barad's apparatus by structure, which is
the template conception; Jaksland attributes that reading to Hollin et al.
(note 21). So "in Barad's sense" means the sense of her concept, not her
way of applying it. On her own conception luria would be an apparatus
outright, since agential realism covers all of reality; but that holds only
if agential realism is correct quantum mechanics, which Faye and Jaksland
([LIT-1672](../literature.d/LIT-1672.md), read in [NOTE-1220](../notes.d/NOTE-1220.md)) show quantum mechanics does not
entail ([THEORY-1071](../theory.d/THEORY-1071.md)). The claim's footing is therefore the template
reading, with its usual cost: the concept's application to a record needs
the record's own warrant, which is what [CLAIM-419](CLAIM-419.md), [CLAIM-195](CLAIM-195.md) and
[CLAIM-479](CLAIM-479.md) supply. Nothing in the claim's argument rested on Barad's
quantum credentials, and the title and status stand.

The reading also gives Barad's own definition, through Faye and Jaksland's
quotation (2007, 148): "apparatuses are the material conditions of
possibility and impossibility of mattering; they enact what matters and
what is excluded from mattering." The first half matches the claim's
"settles which distinctions among entries are determinate and
consequential"; the second is [CLAIM-472](CLAIM-472.md)'s.

## Note of 2026-10-27 (later still): Rheinberger, second-order observation, and rates

Three of the exchange's later turns bear on this claim.

- **Rheinberger ([LIT-1665](../literature.d/LIT-1665.md), unread).** A11's "leading recommendation,
  particularly because of Luria": epistemic things, the objects still under
  investigation, and technical objects, the stabilized means of investigating,
  can turn into one another. A11 saw this in luria: a typed relation that
  served as an instrument became, when its limits showed, an object of
  inquiry, and the revised relation went back to being an instrument. [CASE-131](../cases.d/CASE-131.md)
  and [ADR-044](../decisions.d/ADR-044.md) are a record of exactly that turn. It is closer to this claim
  than Barad's apparatus, since it is about practice and needs no quantum
  premise. A11's caveat: Rheinberger "is discussing laboratory systems with
  material experimental objects".
- **Second-order observation.** A11's "What makes this count as support?", a
  question about the apparatus's own distinction, is [CLAIM-419](CLAIM-419.md)'s
  "second-order corrigible", from A18 of 2026-10-22, which A11 did not cite.
- **Rates, not yet measured.** A12 and A13 read luria's layers (prose edits,
  validation, standing changes, schema revision) as processes on different
  time scales and its durable rules as constraints over faster activity,
  "**storage plus operational uptake**". A12 warned that "There's no guarantee
  these processes possess numerically well-separated timescales. That would
  need measurement." The record's own commit and decision history could
  supply it. It was measured the same day; see the note below.

## Note of 2026-10-27 (latest): the rates measured

[CASE-180](../cases.d/CASE-180.md) measures them over the record's first fifty days. Once an
entry's first day is past, its prose is revised about once in 22 days, its
status once in 128, its authored relations gained or lost once in 132 and
retracted once in about 600, and no relation type in luria.yaml has been
redeclared. So the layers A12 and A13 named are ordered as they said, by one
to two orders of magnitude. Two of their layers do not separate. Validation,
the bot's repair, runs at the rate of the edits it follows (τ 11 d against
13 d), since every push triggers it. And in an entry's first day every layer
moves at once. "Storage plus operational uptake" fits the settled record,
not the record being written. The grammar grows often, on nine of 32 days,
and is revised never, so what is slow is a type once declared, not the
grammar.

## Note of 2026-10-27 (last): how the apparatus is reconstituted

[CASE-178](../cases.d/CASE-178.md) measured when and how luria's grammar is revised in this record.
The claim says misfits met in use revise the grammar. The measurement agrees,
and it is specific about how. 94% of the vocabulary terms added after the
scaffold were used by a document changed in the same pull request, and nine in
ten of the pull requests that added a term, field, vocabulary or scheme also
added an ADR, against one in six of all pull requests. So the apparatus is
reconstituted in the act of filing, by a decision taken there, at the lowest
level that holds the misfit. Its rate of reconstitution fell during the month
while the rate of filing rose.

## Note of 2026-10-27 (U15–U23): inquiry as specification, and a weaker apparatus

The exchange's later turns bear on this claim in three ways.

- **The general form.** The owner's U15, "inquiry is a form of specification",
  is filed as [CLAIM-470](CLAIM-470.md). It complements this claim. Any inquiry
  specifies, its stable products are specifications, and it can revise
  what an answer could be. This claim is the case where the inquiry is a
  record's and the specification is luria's grammar. A16 §11 found luria's
  own docs already stating the two levels. Luria's governance page writes a
  record as K = (O, M, R, E): ontology, governing knowledge, subject
  records and executable machinery (luria docs/concepts/governance.md,
  checked 2026-10-27). Editing a record and revising its schema are
  "working within an inquiry regime and investigating the regime itself".
- **A sense of "apparatus" that needs no argument.** [TERM-089](../terms.d/TERM-089.md) proposes the
  operational sense: an organization that differentiates, retains, enforces
  and revises distinctions. Luria has all four functions. This claim uses
  Barad's sense, which A23 §VII said dynamical stabilization "does not
  derive". The claim could be split along that line. That luria is an
  apparatus in the operational sense is close to demonstrated. That it is
  one in Barad's constitutive sense, for a record's objects, is the part
  still argued. The claim is not split here; that is the owner's call.
- **CEGAR as the formal neighbour of DP-016.** A16 §6 read luria's DP-016
  ([CLAIM-419](CLAIM-419.md) here) as counterexample-guided abstraction refinement
  ([LIT-1652](../literature.d/LIT-1652.md)). A failure under a specification leads to a missing
  distinction and then to refinement. It also gave the limit: CEGAR refines
  within a fixed property and cannot find the property misguided. A21 §6
  gave the failure that revision by consistency alone invites: a schema
  that makes every record valid by weakening its rules. A22 §10: "a
  successful schema should preserve distinctions that matter for subsequent
  use."

## Note of 2026-10-27 (evening): the readings of the U15–U23 works

CEGAR ([NOTE-1231](../notes.d/NOTE-1231.md)) gives A7's Obj(A_t, D_t) ≠ Obj(A_{t+1}, D_t) an exact
counterpart: the same model under a refined abstraction yields a different
abstract structure (p. 5). But the concrete states are individuated before any
abstraction (§2, p. 4), so the apparatus constitutes only the abstract
objects. That is the part of this claim A7 called demonstrable, and the
reading supports nothing beyond it.

## Note of 2026-10-29: what holds it back

Its first defeater is unanswered: no consequence of "constituted" has been
shown that does not follow from CLAIM-469's operational facts, and the
CEGAR reading (NOTE-1231) supports only those; QUESTION-284, which asks
for a criterion telling constitution from characterization, is Open, and
the two-apparatus experiment above is unbuilt. It is also stated in
TERM-087's agential sense, which waits on a reading of Barad herself.
