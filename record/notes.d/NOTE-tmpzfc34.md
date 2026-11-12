---
status: Read
paper: LIT-tmpka8bp
title: 'Orzechowski, Tawfiq and Kosciolek — What Does an Ontology Catch? Curated, LLM-Generated and Data-Derived Ontologies as Checkers of LLM Agents over Knowledge Graphs'
version: 1
history:
- version: 1
  date: '2026-11-12'
  note: >-
    Read on 2026-11-12 from https://arxiv.org/pdf/2610.37809. **Read** (body
    in full; appendices skimmed). A delegated reader drafted the reading;
    quotations were rechecked by script against the downloaded copy, and any
    that did not match were kept as paraphrase without quotation marks.
date: '2026-11-12'
summary: >-
  LLM agents answering questions over knowledge graphs with SPARQL are often
  wrapped in checks derived from the graph's ontology. The authors make the
  checker the object of study: they compare checks from a curated ontology,
  LLM-generated ontologies (including ones written from a summary with
  identifiers masked) and a data-derived ontology, used as prompt context,
  as a check (a flag triggers one retry), or both, across seven open-weight
  and proprietary models, with confirmatory comparisons pre-registered on
  UniProt and exploratory results on other graphs. Every verdict is scored
  against a known correct answer, so catches, misses, false alarms and
  corruptions of correct answers are all counted, and every check is
  compared with a baseline that simply retries empty results.
---
<!-- inactive-ok-file: CASE-tmppm4do — filed from the exchange "luria experiment design", Proposed or Deferred; cited as filed alongside this entry -->

# NOTE-tmpzfc34: Orzechowski, Tawfiq and Kosciolek — What Does an Ontology Catch? Curated, LLM-Generated and Data-Derived Ontologies as Checkers of LLM Agents over Knowledge Graphs

## Contribution

A measurement of the checker's own error profile, not just end accuracy; evidence that a curated
schema is an unreliable judge when it does not describe its own data; a released fault set and a
protocol for measuring any check's catches and false alarms.

## Key results

- Abstract: "a checker can be wrong as well: it can miss errors, and it can flag correct answers and push the agent into “fixing” them."
- Abstract / RQ1: "On real agent answers, its flags are only marginally more precise than random flags." (the curated ontology's).
- RQ1: the curated ontology "raises more false alarms than both the data-derived ontology and the LLM-generated ontologies built from a summary with masked identifiers."
- RQ1: "On the artificial faults, no single ontology catches as many faults as the retry on empty results, which raises no false alarm".
- RQ1: retrying with the curated check's feedback "corrects more than a quarter of the flagged wrong answers but corrupts about one in a hundred flagged correct answers".
- RQ1, comparators: an LLM judge "catches more wrong answers than either the curated or the data-derived ontology" at a similar false-alarm rate, but "retries informed by the judge’s reason corrupted more flagged correct answers than they fixed wrong ones".
- RQ2: false alarms come from "domain and range axioms and its requirement that every term be declared, and each curated ontology we studied disagrees with its own data"; the ontologies "catch none of the changes of meaning among the artificial faults."
- RQ3: "combining the two checks shows no net gain in detection, and passing the check’s specific message to the agent no gain in accuracy".
- Discussion: "An ontology is a reliable check only if it declares every term its data uses and its axioms are satisfied by that data."
- Discussion: "a check earns its place only on errors that running the query does not already reveal".
- Conclusion: "An ontology used to check an LLM agent’s answers is itself a judge that can be wrong".

## Assumptions

- Ground truth is known for every question (the authors note real use lacks it).
- The empty-result retry is the right floor; the data-derived ontology is built from the graph
  checked and the type-swap faults from its co-occurrence graph, which the authors say favours it.
- LLM-generated ontologies come from a single model in the confirmatory arm.

## Concepts

Checker as judge; catch rate, false alarm, precision vs. a random flag at the same rate; corruption
of correct answers by acting on flags; artificial vs. real faults; changes of meaning (errors that
leave queries well-formed and non-empty); curated vs. data-derived vs. LLM-generated schema;
pre-registered confirmatory vs. exploratory comparisons.

## Bearing on the record

A cites it for ontology-based checkers of agent workflows that flag correct answers while missing
important errors, A's reason not to score schema changes with one LLM judge. **Accurate on the
checker** (false alarms on correct answers; changes of meaning missed entirely). **Qualified on the
inference about LLM judges**: the paper's LLM judge was a comparator, and it caught more errors
than the ontology checks with similar false alarms; its failing was that acting on its flags did
more harm than good. So the paper supports no single checker, ontology or LLM, should be trusted
without measuring its false alarms and the harm of acting on them, which is the lesson [CASE-tmppm4do](../cases.d/CASE-tmppm4do.md)
draws, but it is evidence about ontology checks and one LLM-judge comparator on SPARQL answers, not
about judging schema changes.

- [CASE-tmppm4do](../cases.d/CASE-tmppm4do.md) (a proposed study of governed schema adaptation, scored on semantic correction
  without regressions by hidden assertions, not by one LLM judge): **supports the scoring design**.
  The paper shows a schema-derived checker missing exactly the class of error [CASE-tmppm4do](../cases.d/CASE-tmppm4do.md) cares
  about (changes of meaning), and checks whose flags corrupt correct work when acted on, which
  argues for the case's hidden-assertion oracle with known ground truth and for counting
  regressions. It also supplies a design lesson the case can adopt: compare every checker with a
  trivial baseline and with a random flag at the same rate.

Searched the record for 2610.37809, Orzechowski, LLM judge, SHACL/ShEx/SPARQL, false
alarm/false positive, self-correction. Not held (no duplicate). Missed by the first search:
- [CLAIM-520](../claims.d/CLAIM-520.md) (the value of a corrective capacity is conditional: an audit with cost and error rate
  epsilon is worth keeping only under conditions): the paper measures exactly such an audit with a
  nonzero false-alarm rate, where acting on it sometimes corrupts more than it fixes (the LLM
  judge) and sometimes nets a small gain (the curated check). Corroborates the conditionality
  empirically, in one domain.
- [CLAIM-149](../claims.d/CLAIM-149.md) (a probe family that trains a transformation cannot certify what it preserves): a
  parallel lesson; the paper's caution that using the same ontology as context and as check is
  "associated with fewer catches (exploratory)" is a case of a check sharing a blind spot with what
  it checks. Illustrates; exploratory only.
- [CLAIM-419](../claims.d/CLAIM-419.md) and [QUESTION-tmps5iou](../questions.d/QUESTION-tmps5iou.md): the finding that a curated schema "disagrees with its own data"
  is the schema-misfit situation [CLAIM-419](../claims.d/CLAIM-419.md) describes from the record's side; the paper's remedy
  (validate the ontology against a data-derived summary before each release) is a governance step.

## Limitations

Confirmatory claims only for UniProt's frozen questions, faults and ontologies; Rhea's faults not
reported; the private graph not reproducible; one LLM for the generated ontologies; ground truth
known, unlike deployment. A preprint, not yet peer reviewed.
