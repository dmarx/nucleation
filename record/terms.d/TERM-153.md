---
number: 153
status: Proposed
formerly:
- TERM-tmp3mop8
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
- TERM-154
- TERM-152
summary: >-
  Filed at the owner's "consider adding a term (or two) for witness",
  2026-11-22, under the dialectic regime, as the second of the pair with
  [TERM-154](TERM-154.md) (witness). The sense follows proof-carrying code (Necula),
  where the certificate is the proof that code meets a policy, shipped
  with the code; it is from the assistant's knowledge, and no source on it
  is held. The record's practice, a claim held with its grounds and
  premises and a reading with its passages, is a practice of certificates
  ([CLAIM-949](../claims.d/CLAIM-949.md)). The wording is the assistant's (Claude, in this
  session); adopting it is the owner's call.
---
<!-- inactive-ok-file: LIT-tmp9cdlq THEORY-tmpqj2d4 — Proposed or Unavailable; the reading of Kleene through van Oosten that the dated note of 2026-11-22 cites -->
<!-- inactive-ok-file: TERM-154 TERM-152 CLAIM-949 — Proposed; the pair filed with this and the entries it is stated against -->

# TERM-153: certificate, of a realization against a specification: a checkable record that it passes each test, carried with it, so relying on the realization means checking the record rather than redoing the search; the evidence half of a proof-relevant answer

## Definition

A **certificate** of a realization against a specification ([TERM-152](TERM-152.md)) is
a record, kept with the realization, from which anyone can check that it
passes each test without finding it again. In type theory it is the
second component p of a pair (x, p) inhabiting Σx:A.φ(x): the derivation
that x satisfies φ. A witness ([TERM-154](TERM-154.md)) shows *that* the specification
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
  accepting check of it. See [TERM-154](TERM-154.md).

## Note of 2026-11-22: Davies and Pfenning, read
<!-- inactive-ok-file: THEORY-2260 — Proposed; filed for LEAD-215 -->

A parallel. In Davies and Pfenning's checker ([THEORY-2260](../theory.d/THEORY-2260.md);
[NOTE-2351](../notes.d/NOTE-2351.md)) types "may, but need not be carried at runtime" (p. 2), and
ascriptions are erased (p. 7): the checking derivation is found and then
discarded, a witness kept without its certificate. No change.

## Note of 2026-11-22: Rondon, Kawaguchi and Jhala, read
<!-- inactive-ok-file: THEORY-2262 — Proposed; filed for LEAD-215 -->

A contrast (no edge). Liquid types ([THEORY-2262](../theory.d/THEORY-2262.md); [NOTE-2353](../notes.d/NOTE-2353.md)) are
proof-irrelevant, as Freeman and Pfenning's are: the solver's validity
checks are made and not kept, no derivation is stored, and DSOLVE writes
the inferred types to .annot files "as documentation" (p. 167). Still, an
inferred assignment has this term's shape. Given the types, each
subtyping constraint is one validity check, while finding them is the
iterative-weakening search, so the assignment could be rechecked cheaply
and not rebuilt. The paper neither keeps it for that nor says so; the
reading is the filer's. Program verification's loop invariants, which
predicate abstraction finds, are certificates in that sense.

## Note of 2026-11-22: Kleene, read through van Oosten

A contrast, not support. Kleene's realizer ([THEORY-tmpqj2d4](../theory.d/THEORY-tmpqj2d4.md), read in
[NOTE-tmpajfia](../notes.d/NOTE-tmpajfia.md) for the unread [LIT-tmp9cdlq](../literature.d/LIT-tmp9cdlq.md)) has no certificate component:
realizability "is designed to handle “information” about formulas rather
than proofs" (van Oosten, p. 4), and Kleene set Heyting's proof
interpretation aside to build it. A true atomic sentence is realized by 0:
where the test is decidable and cheap, the realizer carries nothing and the
test is run again. That is this term's own asymmetry from the other side:
a certificate earns its place where checking from scratch is expensive,
not where a test can simply be rerun. The nearest counterparts in the
realizability literature are glued realizability with P the provable
sentences, a realizer kept with the fact of provability (p. 6), and the
proof-to-realizer translation behind soundness. The proof-relevant pair
(x, p) the definition cites comes from typed realizability and type
theory, not Kleene 1945. No edge; no status changes.

## Note of 2026-11-22: Kolmogorov, read
<!-- inactive-ok-block: THEORY-tmpdsft8 — Proposed; the reading of 2026-11-22, its argument and the claim it was read for -->

Kolmogorov 1932 ([THEORY-tmpdsft8](../theory.d/THEORY-tmpdsft8.md), read in [NOTE-tmpmkrpn](../notes.d/NOTE-tmpmkrpn.md)): a parallel, no edge. Logical
and mathematical problems have "die spezielle Eigenschaft der
Allgemeingültigkeit ihrer Lösungen" (p. 61): a solution can be presented
so that it must be recognized as correct by any able hearer. That is what a
certificate is for, but Kolmogorov makes it a property of the domain, of "einigermaßen idealen Charakter",
not a record kept with the solution. Unchanged.

## Note of 2026-11-25: Martin-Löf, read
<!-- inactive-ok-file: THEORY-tmp62cvo NOTE-tmp60upv ARG-tmpneexr CLAIM-tmp01pyt — Proposed or Skimmed; filed for LEAD-215 -->

Borne out, with two refinements, from Martin-Löf ([THEORY-tmp62cvo](../theory.d/THEORY-tmp62cvo.md);
[NOTE-tmp60upv](../notes.d/NOTE-tmp60upv.md); [ARG-tmpneexr](../arguments.d/ARG-tmpneexr.md)). The second component of a Σ pair is the
certificate, and in the set of a ∈ A such that B(a) it is carried with
every element, "the witnessing information" (p. 53): the first reading
under [LEAD-215](../leads.d/LEAD-215.md) that keeps it.

- **Construction against derivation.** The book reserves "construction"
  for a proof of a proposition, the element b, and keeps it apart from a
  proof of the judgement b ∈ B(a), a derivation (p. 6). This term's
  definition calls the certificate "the derivation that x satisfies φ",
  which is the second; the pair's component is the first. Which one the
  record's certificates are (a claim's grounds look like the first, a
  lint pass like the second) is for the owner; the definition is not
  changed here.
- **Used, not only checked.** The book's certificate does work beyond
  being checked: "Only by means of the proof q(c) do we know how far to go
  for the approximation desired" (p. 54). Where the certificate is used,
  it cannot be dropped ([CLAIM-tmp01pyt](../claims.d/CLAIM-tmp01pyt.md)).
