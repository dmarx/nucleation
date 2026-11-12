---
status: Skimmed
paper: LIT-tmphmnau
title: 'Lebo, Sahoo and McGuinness (eds.) — PROV-O: The PROV Ontology'
version: 1
history:
- version: 1
  date: '2026-11-12'
  note: >-
    Skimmed on 2026-11-12 from https://www.w3.org/TR/prov-o/. **Skimmed** (the
    whole specification is public; read in full: front matter, status,
    abstract, sections 1-2, the qualified-term pattern in section 3, and the
    definitions of the core and expanded classes and properties; the per-term
    cross-reference examples in section 4, the OWL-RL profile appendix and the
    change logs C-E were skimmed, not read term by term). A delegated reader
    drafted the reading; quotations were rechecked by script against the
    downloaded copy, and any that did not match were kept as paraphrase
    without quotation marks.
date: '2026-11-12'
summary: >-
  PROV-O is the OWL2 encoding of the PROV Data Model: classes and properties
  to represent and interchange provenance, i.e. which entities were
  generated, used, derived, revised, quoted or invalidated by which
  activities, and which agents were responsible (attribution, association,
  delegation). Terms come in three tiers: Starting Point (Entity, Activity,
  Agent, wasGeneratedBy, used, wasDerivedFrom, wasAttributedTo, ...),
  Expanded (Bundle, Plan, Person, wasRevisionOf, wasQuotedFrom,
  hadPrimarySource, wasInvalidatedBy, ...) and Qualified terms, which reify
  a binary influence so further attributes (role, plan, time) can be
  attached. It is designed to be specialized for domain provenance
  ontologies.
---
<!-- inactive-ok-file: CLAIM-189 CLAIM-250 — Proposed; cited for what each holds, not as settled -->

# NOTE-tmpqtavm: Lebo, Sahoo and McGuinness (eds.) — PROV-O: The PROV Ontology

## Contribution

An interoperable vocabulary for the origin and derivation history of things, including of
provenance records themselves (Bundle), so that heterogeneous systems can exchange it.

## Key results

- Abstract: PROV-O "provides a set of classes, properties, and restrictions that can be used to represent and interchange provenance information generated in different systems and under different contexts."
- Sec. 1: "PROV-O is a lightweight ontology that can be adopted in a wide range of applications."; "With the exception of five axioms, PROV-O conforms to the OWL-RL profile".
- Sec. 3 (Agent): "An agent is something that bears some form of responsibility for an activity taking place, for the existence of an entity, or for another agent's activity."
- Sec. 3 (Entity): "An entity is a physical, digital, conceptual, or other kind of thing with some fixed aspects; entities may be real or imaginary."
- Sec. 3 (Attribution): "Attribution is the ascribing of an entity to an agent."
- Sec. 3 (Revision): "A revision is a derivation for which the resulting entity is a revised version of some original."
- Sec. 3 (Invalidation): "Invalidation is the start of the destruction, cessation, or expiry of an existing entity by an activity."
- Sec. 3 (Bundle): "A bundle is a named set of provenance descriptions, and is itself an Entity, so allowing provenance of provenance to be expressed."
- Sec. 3 (Plan): "A plan is an entity that represents a set of actions or steps intended by one or more agents to achieve some goals."
- Sec. 3, qualification: "Consuming applications should recognize both qualified and unqualified forms, and treat the qualified form as implying the unqualified form."
- Negative finding: a search of the whole text for "evidence", "trust", "justif", "belief" and "valid" finds no term for evidential support, credence, acceptance or standing; the only "invalid*" terms are prov:wasInvalidatedBy / invalidatedAtTime, which mark the end of an entity's existence by an activity, not its rejection on evidence.

## Assumptions

- Provenance is modelled as entity-activity-agent influences in time; anything about whether a
  statement is supported or accepted is left to domain extensions.
- Open-world OWL semantics; consumers must accept both qualified and unqualified forms.

## Concepts

Entity, Activity, Agent; generation, usage, derivation, revision, quotation, primary source,
invalidation; attribution, association, delegation; plan; role; bundle (provenance of
provenance); qualified influence pattern.

## Bearing on the record

A said PROV-O is a standard that distinguishes the origin of a statement from its evidential
support or current standing. **Partly inaccurate.** PROV-O models origin (generation,
derivation, revision, attribution, primary source, quotation) and nothing else; it has no
vocabulary for evidential support or for current standing. It "distinguishes" them only in the
sense that it covers one and is silent on the others, leaving them to domain extensions. Its
nearest term to standing, invalidation, is ending of existence by an activity. "A natural
interoperability reference" is fair: it is a W3C Recommendation designed to be specialized, and a
record's entries, their versions (wasRevisionOf), sources (hadPrimarySource, wasQuotedFrom) and
contributors (wasAttributedTo) map onto it directly.

- [CLAIM-299](../claims.d/CLAIM-299.md) (decision sufficiency, historical accountability and correctness are three properties,
  each can hold while the others fail): **supports by illustration**, not by argument. A complete
  PROV-O description of a record secures the historical-accountability property (who produced what
  from what, and revised it how) while saying nothing about the other two: the vocabulary has no
  term for whether a derived statement is supported or correct. That a mature standard for
  provenance carries no support or standing vocabulary is consistent with treating accountability
  as a separable predicate. It does not exhibit the separations itself.

Searched the record for PROV-O, PROV-DM, W3C PROV, prov:, provenance, nanopublication,
micropublication. PROV is not held (no LIT by URL or title; not a duplicate). Missed by the first
search:
- [TERM-100](../terms.d/TERM-100.md) (provenance of a capacity or organization: formation, maintenance or source provenance)
  and [TERM-084](../terms.d/TERM-084.md) (descent: provenance, lineage, common ancestry, causal descent): PROV's
  generation/derivation/primary-source split is a standard against which these senses could be
  set; PROV-O's "source" sense is closest to hadPrimarySource and wasDerivedFrom. Bears, does not
  settle.
- [CLAIM-189](../claims.d/CLAIM-189.md) (what a record can secure is traceability) and [CLAIM-250](../claims.d/CLAIM-250.md) (what should be preserved is
  the accountability structure: what was asserted, why, how challenged, what justified revision):
  PROV-O provides the what was asserted, by whom, from what, revised from what part, not the
  "why" or "what justified" part. Qualifies: it shows which part of [CLAIM-250](../claims.d/CLAIM-250.md)'s structure an
  existing standard covers.
- [QUESTION-225](../questions.d/QUESTION-225.md) (why- and where-provenance in Buneman, Khanna and Tan): a database-provenance line
  distinct from PROV's workflow provenance; PROV-O does not address query provenance.

## Limitations

A vocabulary standard, not an argument: it makes no empirical claim. Section 4's term-by-term
examples and the appendices were skimmed. The negative finding (no support or standing terms) is
from a text search of this document only; PROV-DM and PROV-CONSTRAINTS were not read, though the
family overview lists no document about evidence or trust.
