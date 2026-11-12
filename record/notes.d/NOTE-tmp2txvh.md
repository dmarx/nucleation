---
status: Read
paper: LIT-tmp5mdsg
title: 'Herrmannsdoerfer, Benz and Juergens — COPE - Automating Coupled Evolution of Metamodels and Models'
version: 1
history:
- version: 1
  date: '2026-11-12'
  note: >-
    Read on 2026-11-12 from
    https://wwwbroy.in.tum.de/publ/papers/ECOOP2009_herrmannsdoerfer_cope_automating_coupled.pdf.
    Read on 2026-11-12. A delegated reader drafted the reading; quotations
    were rechecked by script against the downloaded copy, and any that did not
    match were kept as paraphrase without quotation marks.
date: '2026-11-12'
summary: >-
  When a modeling language's metamodel changes, the existing models must be
  migrated. The paper calls this pairing "coupled evolution". **The
  requirements study.** An earlier study of two industrial metamodel
  histories found: - about half the changes were metamodel-only; - more than
  three quarters of the coupled changes were metamodel-independent, so they
  could be reused; - the rest were metamodel-specific; - none were
  model-specific. This yields two requirements: reuse and expressiveness.
  **COPE's answer.** A language evolves through a sequence of coupled
  transactions, each pairing a metamodel adaptation with its model
  migration.
---
<!-- inactive-ok-file: CASE-tmppm4do — filed from the exchange "luria experiment design", Proposed or Deferred; cited as filed alongside this entry -->

# NOTE-tmp2txvh: Herrmannsdoerfer, Benz and Juergens — COPE - Automating Coupled Evolution of Metamodels and Models

## Contribution

- An incremental, operation-based approach to metamodel/model co-evolution that combines a reusable library with custom migrations.
- A recorded language history that captures intent at the time of change.
- An EMF tool.
- Case evidence that most real changes are covered by reusable operations.

## Key results

- **§1:** "the combination of metamodel adaptation and reconciling model migration is referred to as coupled evolution."
- **§1, the problem with migrators written after the fact:** "the developers of the modeling language have to become clear about the intentions behind these metamodel adaptations."
- **§1, against deprecation:** "deprecation shifts the responsibility for model migration from the developer of the modeling language to its users."
- **§4.1:** "In COPE, such a combination of metamodel adaptation and model migration is called coupled transaction." Migration is captured during adaptation, "thus preventing the loss of intention".
- **§4.1:** "The language history contains enough information to migrate a model from the metamodel version to which it conforms to any subsequent metamodel version."
- **§7:** "while reuse saves a lot of effort, expressiveness is required for the rare, but important cases of complex migrations."

## Assumptions

- Changes are made in the metamodel editor and recorded as operations. Snapshot diffs lose intent.
- The models need no model-specific information during migration; the authors' study found none.
- Validation is by existing migrators (GMF) or by the developers (PCM).

## Concepts

- coupled evolution and coupled transformation
- metamodel-only, metamodel-independent, metamodel-specific and model-specific changes
- coupled transaction, reusable and custom
- language history
- migrator
- downward compatibility vs deprecation vs breaking change with a migrator
- capturing intention at the time of change

## Bearing on the record

A calls COPE/Edapt "the strongest technical competitor" for the coupling of schema change to migration. The reading supports that for the migration half. COPE couples each schema change to an executable migration of existing instances, and records the sequence as a replayable history. In that respect it is close to a luria scheme change with a migration.

What it lacks, or leaves outside its scope:
- any record of *why* a change was made, beyond the operation's name;
- any governance of who may change the metamodel;
- any review or approval step;
- any credence or argument;
- any executable checks beyond conformance. Static checking of conformance preservation is listed as future work.

"Intention" in COPE means the intended *migration*, not the rationale. The LIT's identification of this paper as Edapt's origin needs an external source (see the metadata corrections).

- **QUESTION-tmps5iou** (is the coupling of schema change to recorded decision, migration and checks what distinguishes luria?) — **qualifies and sharpens.**
  - COPE already couples schema change to migration with a recorded history, so migration coupling cannot be luria's distinguishing feature.
  - What remains distinctive, if anything, is the coupling to a recorded decision (rationale, authority) and to a lint/CI regime.
  - COPE also gives empirical priors for a benchmark: most changes are extensions or reusable operations, and custom migrations are rare but necessary.
- **CASE-tmppm4do** (proposed study of governed schema adaptation) — **supplies a baseline and a task taxonomy.**
  - COPE's classification of changes (metamodel-only, metamodel-independent coupled, metamodel-specific coupled) can stratify the study's "schema inadequacy" items.
  - An operation-based history with generated migrators is a natural "explicit migration, informal governance" arm.

## Limitations

- The case study is a retrospective reconstruction by the authors.
- Only two metamodels were studied.
- PCM's intermediate versions were dropped.
- There is no user study of the tool.
