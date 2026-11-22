---
status: Proposed
title: 'witness, to a specification: a realization exhibited that passes it, showing by example that what it admits is not empty; the existence half of a proof-relevant answer, apart from the evidence that it passes'
version: 1
tags:
- logic
- epistemology
date: '2026-11-22'
line:
- formal-apparatus
- record-as-apparatus
complements:
- TERM-tmp3mop8
- TERM-tmp94y6v
- TERM-134
draws_on:
- THEORY-tmpdsft8
summary: >-
  Filed at the owner's "consider adding a term (or two) for witness",
  2026-11-22, under the dialectic regime, with [TERM-tmp3mop8](TERM-tmp3mop8.md) (certificate) as its pair.
  [CLAIM-783](../claims.d/CLAIM-783.md) already argues by witness, that descriptors never conflict
  because the entry passes them all, and [CLAIM-tmpnookt](../claims.d/CLAIM-tmpnookt.md) uses the word for
  Kleene's realizer; neither defines it. The sense is the logician's (the
  object that makes an existential true); the record's readings of
  Kleene and Martin-Löf ([LEAD-tmp3xevc](../leads.d/LEAD-tmp3xevc.md)) will test it. Filed as two terms
  rather than one with two senses because the two come apart (below); one
  term with two senses is the alternative, and the owner chooses. The
  wording is the assistant's (Claude, in this session); adopting it is the
  owner's call.
---
<!-- inactive-ok-file: TERM-tmp3mop8 TERM-tmp94y6v TERM-134 CLAIM-tmpnookt — Proposed; the pair filed with this and the entries it is stated against -->

# TERM-tmp7s2aa: witness, to a specification: a realization exhibited that passes it, showing by example that what it admits is not empty; the existence half of a proof-relevant answer, apart from the evidence that it passes

## Definition

A **witness** to a specification ([TERM-tmp94y6v](TERM-tmp94y6v.md)) is a realization put forward
that passes every test the specification holds. Exhibiting one shows the
specification satisfiable: the set of admissible realizations is not empty.
In logic it is the object that makes "there is an x such that φ(x)" true;
in type theory, the first component of a pair (x, p) inhabiting
Σx:A.φ(x).

The record already argues this way. Predicates an entry passes when they
are added (descriptors, [TERM-134](TERM-134.md)) never conflict, because the entry itself
is a witness to all of them at once ([CLAIM-783](../claims.d/CLAIM-783.md)). An imposition has no
witness until the entry has been moved to pass it, and may never have one:
an empty intersection is the conflict the record files as an objection.

## Witness and certificate

A witness is the *what*; its certificate ([TERM-tmp3mop8](TERM-tmp3mop8.md)) is the *why it
passes*. They come apart both ways:

- **Witness without certificate**: an example that does pass, with no
  record of the check. Anyone who wants to rely on it must check it again.
- **Certificate without witness**: a proof that some realization passes,
  with none exhibited (by counting, by contradiction). Classical, not
  constructive; it settles satisfiability and hands over nothing to use.

A proof-relevant answer, in the sense of [CLAIM-tmpnookt](../claims.d/CLAIM-tmpnookt.md), carries both.

## Not to be confused with

- **A witness in the evidential sense**: a source testifying to an event.
  The record's sources are grounds; a witness here is a realization, not a
  testimony.
- **Warrant**: a claim's warrant ([ADR-043](../decisions.d/ADR-043.md)) classifies the kind of
  support it has. A witness is one realization, not a kind of support.
- **NP's witness or certificate**: complexity theory uses the two words as
  synonyms for the string a verifier checks. Here they are split: the
  string is the witness, the verifier's accepting run its certificate.

## Note of 2026-11-22: Kolmogorov, read
<!-- inactive-ok-block: THEORY-tmpdsft8 — Proposed; the reading of 2026-11-22, its argument and the claim it was read for -->

Kolmogorov 1932 ([THEORY-tmpdsft8](../theory.d/THEORY-tmpdsft8.md), read in [NOTE-tmpmkrpn](../notes.d/NOTE-tmpmkrpn.md)) gives the witness's sense for
existence. Brouwer's existence statement splits into "das objektive Element
(die Aufgabe) und das subjektive (ihre Lösung)" (p. 65): the problem "in
der Menge K ein Element mit der Eigenschaft A zu finden", and its solution,
the element found. Nothing is left over to be an existence statement
proper. The witness is that element; Kolmogorov adds that its having been
found is a subjective fact (p. 61), which the term's "exhibited" keeps. The
term now `draws_on` the reading. Unchanged otherwise.
