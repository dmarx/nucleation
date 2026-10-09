---
status: Active
status_note: 'read 2026-10-09 ([NOTE-tmp0w9bg](../notes.d/NOTE-tmp0w9bg.md)); worth reading as the dynamic-semantic statement of the performative/constative distinction: an informative update removes indices from a context set (Stalnaker), a performative update changes them minimally so that a proposition holds (after Szabolcsi 1982), and so can add indices the context did not contain. A declaration is a pure performative update; an assertion is a performative update (the speaker publicly guarantees the proposition) followed by an informative update that the addressee may refuse. The same declarative sentence is structurally ambiguous between the two. Read it as a formal proposal argued from linguistic evidence (hereby, hedges, tense across languages), not as a tested theory, and note that commitment spaces, which carry the negotiation, are Krifka''s other papers, not this one.'
title: 'Performative updates and the modeling of speech acts'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read in full on 2026-10-09 (NOTE-tmp0w9bg) from the publisher's
    open-access PDF (CC BY 4.0, 31 pages), extracted with pdftotext; the
    diagrams (8)–(16) and (40) did not survive extraction and were read
    from their captions and the surrounding text. Citation checked
    against Crossref: Manfred Krifka, Synthese 203(1), article 31,
    published online 12 January 2024 (received 13 April 2022, accepted
    18 September 2023). `published:` is that online date. The
    manuscript's "Krifka 2024" is this paper: the title the exchange
    gave ("Performative Updates and the Modeling of Speech Acts") matches.
    Not held in the Anthology of the SOTA: a grep of its record/ (clone
    of 2026-10-09, commit d8b5ba5) for "Krifka", "performative update"
    and the DOI found nothing.
tags:
- pragmatics
- philosophy-of-language
- linguistics
date: '2026-10-09'
published: '2024-01-12'
doi: '10.1007/s11229-023-04359-0'
first_author: 'Krifka'
keywords:
- 'speech acts'
- 'assertions'
- 'declarations'
- 'dynamic interpretation'
- 'explicit performatives'
implementations: []
summary: >-
  Krifka (2024), Synthese 203:31. Adds to Stalnaker's informative update,
  which filters a context set, a performative update that changes each
  index minimally so a proposition becomes true. Declarations are purely
  performative; assertions are a performative guarantee by the speaker
  followed by a negotiable informative update; commissives, directives,
  exclamatives, optatives, definitions and the locutionary act itself are
  modelled as index changes, and hereby marks a proposition made true by
  the utterance.
---
<!-- inactive-ok-file: THEORY-tmp5ncrn — Proposed; filed from this reading with two others -->
<!-- inactive-ok-file: LIT-785 LIT-tmpnhioh LIT-tmpeftz9 — Deferred; unread here, named as the predecessors this paper cites and not leaned on -->

# LIT-tmpuclkg: Performative updates and the modeling of speech acts

Manfred Krifka (2024), *Synthese* 203, article 31 (31 pp.), open access
— DOI-10.1007/s11229-023-04359-0

## Key takeaways

- **Two kinds of update.** Informative update restricts a context set c to
  the indices where φ holds, c + inform(φ) = {i ∈ c | φ(i)}, always a
  subset of c and empty if φ is not a live option. Performative update
  replaces each index by its minimal φ-changed successor,
  c + perform(φ) = {i′ | ∃i ∈ c, i′ ∈ i + φ}, which is not in general a
  subset of c and is typically applied when φ is false throughout c. The
  difference is Searle's direction of fit, made formal.
- **Index change is coherent.** Szabolcsi's functional version (the unique
  later index differing only in φ) fails for simultaneous independent
  changes and for disjunctive φ. Krifka places it in branching time, with
  the changed index starting a new, cotemporaneous history, and adopts a
  relational version (a set of minimally different indices), parallel to
  Lewis's counterfactuals against Stalnaker's.
- **Declarations versus assertions.** A declaration is [ActP · TP]: the
  performative operator applied to a proposition, defined only where the
  speaker has the authority. An assertion is [ActP · [ComP ⊢ TP]]: a
  performative update making it true that the speaker guarantees φ (the
  illocutionary act, which the addressee cannot reject, only ask to be
  withdrawn), followed by an informative update with φ (the primary
  perlocutionary act, which the addressee can refuse). The same sentence,
  *citizens can apply for travel abroad*, can be either; evidence that
  declarations lack the commitment layer is that they reject *certainly*,
  *apparently*, and cannot answer questions.
- **Every speech act is performative.** Commissives create a speaker
  obligation, imperatives an addressee obligation, exclamatives and
  optatives display an attitude rather than vouch for it, definitions and
  *let x be prime* impose a fact, and "proxitives" (*grins*, lol) stand in
  for an act. The locutionary act is itself a sequence of index changes,
  and the illocutionary change happens at its end; *hereby* marks that the
  host proposition becomes true through the utterance, which is why it
  never occurs with assertions.

## Standing in the record

Filed on 2026-10-09 at the owner's request from the manuscript
bibliography of 2026-10-09 (work `what-survives-translation`), which
considered this paper and dropped it from the final reference list. See
the curation entry of that day.

Read on 2026-10-09 ([NOTE-tmp0w9bg](../notes.d/NOTE-tmp0w9bg.md)). It is the record's only formal account
of speech acts. Its two named predecessors are filed beside it: Stalnaker's
"Assertion" ([LIT-tmpeftz9](LIT-tmpeftz9.md)), whose context-set update is the informative
half, and Searle's *Speech Acts* ([LIT-tmpnhioh](LIT-tmpnhioh.md)), whose F(p) form the
operator · instantiates. Austin's lectures ([LIT-785](LIT-785.md)) are the source of the
constative/performative distinction it formalises.

With the Heim and Veltman readings of the same day it is a source of
[THEORY-tmp5ncrn](../theory.d/THEORY-tmp5ncrn.md).
