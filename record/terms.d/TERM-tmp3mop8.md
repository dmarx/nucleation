---
status: Proposed
title: 'certificate, of a realization against a specification: a checkable record that it passes each test, carried with it, so relying on the realization means checking the record rather than redoing the search; the evidence half of a proof-relevant answer'
version: 1
tags:
- logic
- epistemology
date: '2026-11-22'
line:
- formal-apparatus
- record-as-apparatus
complements:
- TERM-tmp7s2aa
- TERM-tmp94y6v
summary: >-
  Filed at the owner's "consider adding a term (or two) for witness",
  2026-11-22, under the dialectic regime, as the second of the pair with
  [TERM-tmp7s2aa](TERM-tmp7s2aa.md) (witness). The sense follows proof-carrying code (Necula),
  where the certificate is the proof that code meets a policy, shipped
  with the code; it is from the assistant's knowledge, and no source on it
  is held. The record's practice, a claim held with its grounds and
  premises and a reading with its passages, is a practice of certificates
  ([CLAIM-tmpnookt](../claims.d/CLAIM-tmpnookt.md)). The wording is the assistant's (Claude, in this
  session); adopting it is the owner's call.
---
<!-- inactive-ok-file: TERM-tmp7s2aa TERM-tmp94y6v CLAIM-tmpnookt — Proposed; the pair filed with this and the entries it is stated against -->

# TERM-tmp3mop8: certificate, of a realization against a specification: a checkable record that it passes each test, carried with it, so relying on the realization means checking the record rather than redoing the search; the evidence half of a proof-relevant answer

## Definition

A **certificate** of a realization against a specification ([TERM-tmp94y6v](TERM-tmp94y6v.md)) is
a record, kept with the realization, from which anyone can check that it
passes each test without finding it again. In type theory it is the
second component p of a pair (x, p) inhabiting Σx:A.φ(x): the derivation
that x satisfies φ. A witness ([TERM-tmp7s2aa](TERM-tmp7s2aa.md)) shows *that* the specification
is met; the certificate shows *why*, in a form that can be checked.

Its point is the asymmetry between finding and checking: a certificate is
cheap to check even when the realization was expensive to find. That is
what makes stored work ([CLAIM-475](../claims.d/CLAIM-475.md), [CLAIM-761](../claims.d/CLAIM-761.md)) reusable: a later inquiry
checks the certificate instead of repeating the search.

## In the record

- A CLAIM's `grounds` and `rests_on`, with its `warrant`, are its
  certificate: what a reader checks to rely on it.
- A NOTE's quoted passages, with section and page, are the certificate of
  a reading; [ADR-068](../decisions.d/ADR-068.md)'s step that the filer rechecks every quote is the
  check.
- A lint pass is a certificate the tooling issues: the tree passes the
  tests the configuration states.

A certificate goes stale when what it certifies changes. An entry revised
after its grounds were checked carries a certificate for an earlier
version.

## Not to be confused with

- **Warrant** ([ADR-043](../decisions.d/ADR-043.md)): the *kind* of support (demonstrated, empirical,
  interpretive). A certificate is the support itself, for one realization.
- **NP's certificate**: there a synonym for the witness string; here the
  accepting check of it. See [TERM-tmp7s2aa](TERM-tmp7s2aa.md).

## Note of 2026-11-22: Kolmogorov, read
<!-- inactive-ok-block: THEORY-tmpdsft8 — Proposed; the reading of 2026-11-22, its argument and the claim it was read for -->

Kolmogorov 1932 (THEORY-tmpdsft8, read in NOTE-tmpmkrpn): a parallel, no edge. Logical
and mathematical problems have "die spezielle Eigenschaft der
Allgemeingültigkeit ihrer Lösungen" (p. 61): a solution can be presented
so that it must be recognized as correct by any able hearer. That is what a
certificate is for, but Kolmogorov makes it a property of the domain, of "einigermaßen idealen Charakter",
not a record kept with the solution. Unchanged.
