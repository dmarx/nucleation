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

## Note of 2026-11-22: Freeman and Pfenning, read
<!-- inactive-ok-file: THEORY-tmp1mruk ARG-tmptph3p — Proposed; filed for LEAD-tmp3xevc -->

Freeman and Pfenning's refinement types ([THEORY-tmp1mruk](../theory.d/THEORY-tmp1mruk.md); [NOTE-tmpew427](../notes.d/NOTE-tmpew427.md)) use the
witness argument without the word: a term that has σ and τ has σ ∧ τ, and
its value inhabits it (p. 3). They sharpen one condition. Their soundness
theorem holds only "if e evaluates to v" (p. 7), and a term that does not
terminate can have ⊥, the empty refinement, so a witness is a realized
value, not anything that has the type. The definition's "a realization
exhibited" already says so. The system carries no certificate: that a
term has a refinement is a derivation found and not kept, a witness
without certificate in the sense above ([ARG-tmptph3p](../arguments.d/ARG-tmptph3p.md)). No change.

## Note of 2026-11-22: Rondon, Kawaguchi and Jhala, read
<!-- inactive-ok-file: THEORY-tmp01mu6 — Proposed; filed for LEAD-tmp3xevc -->

A parallel, from the other side (no edge). Liquid inference
(THEORY-tmp01mu6; NOTE-tmpnd1kd) types a function's inputs as the
strongest supertype of the arguments the program passes. With no calls,
its neg example gets {0 ≤ ν ∧ 0 ≥ ν} → {0 ≤ ν ∧ 0 ≥ ν}, "useless but
sound" (p. 167): the strongest description the qualifiers state, true of
no argument ever given. A description with nothing to witness it can be
as strong as the vocabulary allows. The record's descriptors are written
from an entry that exists, which is what this term's witness rules out.
