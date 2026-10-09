---
status: Active
status_note: 'read 2026-10-09 (NOTE-tmpb9fuk); worth reading as the programmatic statement of update semantics: the meaning of a sentence is the change it makes to an information state, and an update system is "additive", so reducible to static propositions, exactly when updates are total, idempotent, persistent, monotone and strengthening. "Might" and "presumably" fail persistence: they are tests on a state, not information about the world. Its second half is a theory of defaults in which priority between conflicting rules ("more specific wins", the Nixon diamond left open) follows from a coherence and an applicability criterion rather than being stipulated. Read the default theory as one formalisation the author himself hopes will be bettered; the framework is the lasting part.'
title: 'Defaults in Update Semantics'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read in full on 2026-10-09 (NOTE-tmpb9fuk) from the author's copy on
    his University of Amsterdam staff page
    (staff.science.uva.nl/f.j.m.m.veltman/papers/FVeltman-dius.pdf, 43
    pages in the author's own typesetting, not the journal's), extracted
    with pdftotext. Citation checked against Crossref: Journal of
    Philosophical Logic 25(3), June 1996, DOI 10.1007/BF00248150; the
    pages, 221–261, are from the UvA repository (DARE) record and the
    Philosopher's Annual reprint, as Crossref gives none. `published:` is
    1 June 1996: Crossref gives only the month. Earlier versions exist as
    DYANA report 2.5.A (1990) and ILLC report LP-1991-02. Not held in the
    Anthology of the SOTA: a grep of its record/ (clone of 2026-10-09,
    commit d8b5ba5) for "Veltman", "update semantics" and the DOI found
    nothing.
tags:
- logic
- philosophy-of-language
- linguistics
date: '2026-10-09'
published: '1996-06-01'
doi: '10.1007/BF00248150'
first_author: 'Veltman'
keywords:
- 'dynamic semantics'
- 'defaults'
- 'epistemic modalities'
implementations: []
summary: >-
  Veltman (1996), J. Philos. Logic 25(3):221–261. Defines an update
  system (a sentence's meaning is an operation on information states),
  proves it reduces to static propositions exactly when it is additive,
  and shows epistemic "might" and "presumably" are non-persistent tests.
  Builds a decidable non-monotonic logic of default rules ("if φ, normally
  ψ") in which specificity and other priorities between conflicting
  defaults follow from coherence and applicability conditions on
  expectation frames.
---
<!-- inactive-ok-file: THEORY-tmp5ncrn — Proposed; filed from this reading with two others -->
<!-- inactive-ok-file: LIT-tmpeftz9 — Deferred; unread here, named as the origin the paper credits -->

# LIT-tmpi254m: Defaults in Update Semantics

Frank Veltman (1996), *Journal of Philosophical Logic* 25(3):221–261
— DOI-10.1007/BF00248150

## Key takeaways

- **The slogan and the test.** "You know the meaning of a sentence if you
  know the change it brings about in the information state of anyone who
  accepts the news conveyed by it." An update system ⟨L, Σ, [ ]⟩ is
  additive (each sentence has a static content 0[φ], and σ[φ] = σ + 0[φ])
  iff updates are total and satisfy Idempotence, Persistence, Monotony and
  Strengthening (Proposition 1.2). Only where one of these fails does the
  dynamic view say anything the static view cannot.
- **Tests are not information.** σ[might φ] is σ if φ is consistent with
  σ, and the absurd state otherwise. "Might φ" adds nothing about the
  world; it checks the state, so it can be accepted and later rejected
  ("Maybe it's John… It's Mary… Maybe it's John" is incoherent). There
  are no "might-φ worlds".
- **Three validities.** Updating the minimal state with the premises
  (valid₁), any state (valid₂), or classical acceptance-preservation
  (valid₃) coincide in additive systems and come apart otherwise. Valid₁
  is non-monotonic and is characterised by Sequential Monotony,
  Sequential Cut and Reflexivity.
- **Defaults.** "Normally ψ" refines an expectation pattern (a preorder of
  worlds by normality) and is persistent; "presumably ψ" tests whether ψ
  holds in the optimal worlds. Restricted rules "if φ, normally ψ" need a
  frame of patterns, one per domain. Coherence (every domain has a normal
  world) and applicability (a default applies within s if no domain above s
  has all its normal worlds violating it) make more specific rules win,
  leave the Nixon diamond undecided, validate a defeasible modus tollens
  and keep Independence (an exception in one respect is normal in
  others), where Reiter, Delgrande, Asher and Morreau, and the inheritance
  algorithm of Horty, Thomason and Touretzky each differ somewhere.

## Standing in the record

Filed on 2026-10-09 at the owner's request from the manuscript
bibliography of 2026-10-09 (work `what-survives-translation`), which
considered it and dropped it from the final reference list, as one of the
dynamic-semantics works (with Stalnaker and Heim) the exchange named. See
the curation entry of that day.

Read on 2026-10-09 (NOTE-tmpb9fuk). `logic` is primary because the paper
is a logic of default reasoning; `philosophy-of-language` and
`linguistics` hold the update-semantic account of meaning and of epistemic
modals. Its footnote 1 traces the dynamic notion of meaning to Stalnaker
(LIT-tmpeftz9 is his "Assertion"), Kamp, Heim's dissertation
(LIT-tmpvhtrs) and Gärdenfors, and its direct inspiration to Groenendijk
and Stokhof's dynamic predicate logic, which the record does not hold.

With the Heim and Krifka readings of the same day it is a source of
THEORY-tmp5ncrn.
