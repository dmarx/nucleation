---
status: Proposed
title: 'Adding a predicate to an entry is adding a constraint on its revisions: each field filled, relation drawn, status set, defeater stated and passage quoted is a test its later versions must pass, so as they accrue the revisions still open to it are an intersection that only shrinks, toward what the predicates say, which its filers chose; the inductive prior an entry develops is that intersection weighted by how hard each predicate is enforced, from prose convention to lint rule, and narrowing it is not good in itself'
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  Either of two results in the record's own history. (a) Revisions that
  fail one of an entry's filed predicates, without a change of status or a
  revision announced in its history, occur no less often for entries with
  many predicates than for entries of the same age with few, so that
  predicates do not constrain what revisions an entry takes. (b) Entries
  with more predicates converge, across revisions, on the schema's defaults
  rather than on the values their predicates were filed with, so that the
  narrowing is not toward what the predicates say.
tags:
- design-rationale
- epistemology
- complex-systems
date: '2026-11-21'
line:
- nucleating-argument
- record-as-apparatus
rests_on:
- CLAIM-tmp8v75o
- CLAIM-778
- CLAIM-772
grounds:
- THEORY-1335
uses:
- TERM-tmp7m4at
- TERM-132
summary: >-
  The owner's reframe, 2026-11-21: "maybe it works better if I say
  'stabilization' instead of 'contraction'. my suggestion here is a reframe
  of how adding predicates to an item is a manifestation of adding
  constraints", with the pointer that the record maps predicates to test
  functions. [CLAIM-778](CLAIM-778.md) explains an entry's narrowing by what restatement
  copies; this explains it by what the entry says about itself, and gives
  "toward desired outcomes", which [CLAIM-778](CLAIM-778.md) declined, a reading. The
  wording is the assistant's (Claude, in this session); adopting it is the
  owner's call.
---
<!-- inactive-ok-file: CLAIM-778 CLAIM-772 CLAIM-184 CLAIM-068 CLAIM-119 TERM-132 — Proposed; the claims this restates in terms of predicates, and the risks it keeps -->
<!-- inactive-ok-file: CLAIM-tmp8v75o TERM-tmp7m4at — Proposed; filed in this contribution of 2026-11-21 -->

# CLAIM-tmpj4fzn: Adding a predicate to an entry is adding a constraint on its revisions: each field filled, relation drawn, status set, defeater stated and passage quoted is a test its later versions must pass, so as they accrue the revisions still open to it are an intersection that only shrinks, toward what the predicates say, which its filers chose; the inductive prior an entry develops is that intersection weighted by how hard each predicate is enforced, from prose convention to lint rule, and narrowing it is not good in itself

## The claim

Everything filed on an entry is a predicate of it ([TERM-tmp7m4at](../terms.d/TERM-tmp7m4at.md)): its
fields and their values, its `rests_on` and `grounds`, its status, its
`defeated_if`, the passages it quotes, the codes that cite it. Each is a
test a later version must pass to be a revision of this entry rather than a
change to it that announces itself. So the predicates are constraints, and
an entry's life cycle is their accrual: the revisions still open to it are
the versions that pass every one, an intersection that shrinks as they
arrive ([CLAIM-tmp8v75o](CLAIM-tmp8v75o.md), part 1).

**Why "toward desired outcomes" holds here.** [CLAIM-778](CLAIM-778.md) declined the
phrase: the contracting part goes to the schema's convention and the
conserved part keeps whatever the source said, neither chosen for the
outcome. A predicate is chosen. A filer writes `rests_on: CLAIM-772`
because the entry needs that premise, and a `defeated_if` because that is
the result that should defeat it. The intersection narrows toward what the
predicates say, and what they say is what the filers meant the entry to be.

**The prior.** The prior over an entry's next revision is the intersection
weighted by enforcement: a hard predicate excludes what fails it, a soft one
makes it costly. [CLAIM-tmp8v75o](CLAIM-tmp8v75o.md), part 4, puts the two on one scale, a
penalty of strength λ. [DP-3](../../docs/design-principles.md#dp-3)'s ladder, prose to convention to mechanism to
guarantee, is the record raising λ on its own norms, and the same ladder
applies to an entry's predicates. So [CLAIM-778](CLAIM-778.md)'s inductive prior is not only
an analogy: it is this weighted intersection.

**How it meets contraction.** Enforcing a predicate is the contracting part
and preserving one is the conserved part ([CLAIM-tmp8v75o](CLAIM-tmp8v75o.md), part 5). Schema
predicates are enforced, since lint holds every entry to them, and so carry
nothing of a particular entry's start. Content predicates differ across
entries and are preserved, by codes that resolve and readings copied
verbatim. The features no predicate bounds are [TERM-132](../terms.d/TERM-132.md)'s local degrees of
freedom. So [CLAIM-772](CLAIM-772.md)'s one contraction is the dynamics, and the predicates
say where it goes.

**Juarrero.** [THEORY-1335](../theory.d/THEORY-1335.md) holds that constraints take a system away from
equiprobability and from independence. Schema predicates do the first to an
entry's form; relations do the second, tying it to other entries. Version 1
of [CLAIM-778](CLAIM-778.md) said this in prose; this claim restates it with the predicates
as tests.

## On the word "stabilization"

The owner proposed "stabilization" for this, in place of "contraction". In
the record "stabilized" already names attraction toward convention under
transmission ([CLAIM-068](CLAIM-068.md)), which is the enforced, contracting case. Here the
narrowing is named by its mechanism, constraint by predicates, and
stabilization is left to what the predicates produce: an entry whose open
revisions have stopped shrinking. Whether "stabilization" should be fixed
in this sense is the owner's call, and would take a TERM.

## What it does not say

- **Not that narrowing is good.** Predicates filed early can lock an entry
  in ([CLAIM-184](CLAIM-184.md)), and the record keeps chosen features free on purpose:
  Proposed status, `promote_when`, `defeated_if`. That a predicate was
  chosen makes the narrowing directed, not right.
- **Not that the intersection only shrinks.** It shrinks under addition.
  Retiring an entry by status withdraws its predicates' force, and a
  revision that announces itself can drop one. Identity stays open by
  status, as [CLAIM-778](CLAIM-778.md) says.
- **Not that predicates never conflict.** An empty intersection is an
  objection to settle, and the record files it as one.
- **Not formal concept analysis.** The likeness to a concept lattice
  ([CLAIM-119](CLAIM-119.md)), more attributes and fewer things that fit them, is noted, not
  relied on.

## Tests

The defeaters are counts on the record's history. [LEAD-199](../leads.d/LEAD-199.md) already counts
revisions against inbound references for [CLAIM-778](CLAIM-778.md); defeater (a) widens
its count from inbound references to all filed predicates. Defeater (b)
needs a retention measure against the filed values, of the kind [LEAD-201](../leads.d/LEAD-201.md)
plans against the originating turn.
