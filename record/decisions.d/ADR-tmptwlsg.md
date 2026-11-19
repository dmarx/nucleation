---
status: Proposed
title: 'An ARG may conclude a TERM, as an explication: that the definition does its declared job better than its predecessor and rivals, judged by Carnap''s adequacy conditions; the verdict is the argument''s and adoption stays the term''s status, and the term''s `argued_by` is derived'
version: 1
tags:
- record
- mechanism
date: '2026-11-19'
summary: >-
  A TERM could reach upstream only to readings (`draws_on`, [ADR-095](ADR-095.md)) and
  to a broader term (`refines`, [ADR-046](ADR-046.md)). The claims and cases that fixed
  where a definition draws its lines were cited in its prose and nowhere
  else, so revising one of them found nothing built on it. The owner asked
  on 2026-11-19, after the definition of learning ([TERM-tmp1ix99](../terms.d/TERM-tmp1ix99.md)) took most
  of the exchange "Topological protection explained" to reach, whether
  TERMs should conclude ARGs. They now may, in one new form, `explication`,
  whose critical questions are Carnap's adequacy conditions (similarity to
  the paradigm cases, exactness, fruitfulness, simplicity) and the rivals
  it is judged against. Its verdict is on fit to the term's job
  ([ADR-056](ADR-056.md)), not on truth, which is [CLAIM-472](../claims.d/CLAIM-472.md)'s point that a cut is open
  to evaluation and not only to verification. The term's `argued_by` is
  derived. Rejected: a twin adequacy CLAIM for each term; widening
  `draws_on` to claims and cases; leaving it to prose.
---
<!-- inactive-ok-file: CLAIM-472 TERM-tmp1ix99 — Proposed; the record's ground for the form, and the term of its first application -->
<!-- inactive-ok-file: THEORY-tmpai35t THEORY-1797 — Proposed; the readings that carry the form's provenance -->

# ADR-tmptwlsg: An ARG may conclude a TERM, as an explication: that the definition does its declared job better than its predecessor and rivals, judged by Carnap's adequacy conditions; the verdict is the argument's and adoption stays the term's status, and the term's `argued_by` is derived

## Context

A TERM says what job its definition does ([ADR-056](ADR-056.md)), and it can be
Proposed, rival another or narrow one ([ADR-046](ADR-046.md)). What it could not say is
why its lines fall where they do. Its upstream edges were `draws_on`, to
the readings its sense is fixed by ([ADR-095](ADR-095.md)), and `refines`, to a broader
term. The record's own claims and cases that a definition answers to,
the counterexamples that forced an exclusion and the claims that only
became statable once it was fixed, were cited in its prose and carried no
relation.

The definition of learning filed from the exchange "Topological
protection explained" ([TERM-tmp1ix99](../terms.d/TERM-tmp1ix99.md)) is the case that raised it. It took
most of the exchange to reach (A46, revised at A71, corrected at
ChatGPT's review), and its exclusions lean on the record's claims: a
lookup table that passes for a model over a finite horizon ([CLAIM-519](../claims.d/CLAIM-519.md)),
and a population whose norms are set by what selection keeps ([CLAIM-288](../claims.d/CLAIM-288.md)).
Nothing machine-readable tied the term to either. The owner asked on
2026-11-19 whether TERMs should conclude ARGs.

## Decision

1. **An ARG may conclude a TERM.** `concludes` takes CLAIM or TERM. A
   TERM's `argued_by` is its converse, derived by `luria link --fix`.
2. **It does so in one form, `explication`.** The argument is that the
   definition does its declared job better than its predecessor and its
   rivals. Its critical questions are Carnap's requirements for an
   explicatum (*Logical Foundations of Probability*, 1950, chapter I;
   [LIT-tmpkck45](../literature.d/LIT-tmpkck45.md), read in [NOTE-tmpgrtgu](../notes.d/NOTE-tmpgrtgu.md), account [THEORY-tmpai35t](../theory.d/THEORY-tmpai35t.md); the SEP
   entry's report of them is [THEORY-1797](../theory.d/THEORY-1797.md)), with the comparison made
   explicit:
   - Is the explicandum clear: which uses was the word meant to cover,
     and which not, shown by examples? Carnap puts this before any
     explicatum is judged.
   - Is it similar enough: does it apply in most cases where the word was
     used, and is each departure, a paradigm case it excludes or a
     contested case it decides, paid for by fruitfulness? Carnap permits
     "considerable differences".
   - Is it exact enough to apply?
   - Is it fruitful: what becomes statable that was not?
   - Is it as simple as the other requirements allow?
   - Which predecessor and rivals is it judged against? For Carnap the
     question is whether one explication is "more satisfactory than
     another", not whether it is right.
3. **The verdict is on fit, not truth.** A definition is not true or
   false. [CLAIM-472](../claims.d/CLAIM-472.md) (Proposed) holds that choosing a distinction is open
   to evaluation and not only to verification; this is that evaluation
   given a place. The ARG's status is the verdict on the inference, as on
   every ARG ([ADR-061](ADR-061.md)). Adopting the term remains its own status, the
   owner's call: an Active explication does not make a term Active.
4. **Premises are as on any ARG.** Claims go in `rests_on`; cases,
   readings and works in `grounds`; terms the inference is stated in, in
   `uses`. A counterexample is a CLAIM that undercuts the ARG, or a
   Rejected explication saying which question fails.
5. **Nothing is required.** A term with no explication is not in
   breach. One is filed where a definition's lines were argued for, or
   are disputed.

The first application is the explication of [TERM-tmp1ix99](../terms.d/TERM-tmp1ix99.md), filed with
this decision.

## Alternatives considered

- **A twin CLAIM per term ("this definition is adequate"), argued by an
  ordinary ARG.** Needs no change to the configuration, but doubles the
  entries, and a claim's status is credence in its truth, which is the
  wrong question for a definition.
- **Widening `draws_on` to CLAIM and CASE.** Cheaper, but `draws_on`
  says where a term takes its sense, not what justifies its lines. It has
  no form, no critical questions, no verdict and nothing for an objection
  to attach to.
- **Letting an ARG conclude a TERM in any form.** The existing forms'
  critical questions ask whether a conclusion holds. Without its own
  questions an argument for a definition would be judged as if it were
  true or false.
- **Status quo.** The development of a definition stays in prose, and a
  revision of a claim it answers to finds nothing that depends on it.

## Consequences

- A TERM's page shows the explications that argue for it, and a claim's
  `supports` shows the explications that rest on it, so revising a claim
  finds the definitions that answer to it.
- The `arg-forms` vocabulary gains `explication`; `concludes` is no
  longer CLAIM only. Any tool or view that assumes an ARG concludes a
  claim needs checking. Whether luria derives `argued_by` on both
  schemes from a reference naming two is confirmed by the pull request's
  `docs-check` run.
- An explication's verdict and its term's status can disagree, as an
  ARG's and its conclusion's can. That is intended.
