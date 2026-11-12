---
status: Read
paper: LIT-tmpp8mb7
title: 'Chesñevar et al. — Towards an argument interchange format'
version: 1
history:
- version: 1
  date: '2026-11-12'
  note: >-
    Read on 2026-11-12 from
    https://ri.conicet.gov.ar/server/api/core/bitstreams/2a5fd086-d679-4cbc-8cc2-0c31ce3bb7f1/content.
    **Read** (sections 1-3 and 6 in full; section 4 use cases and section 5
    reifications skimmed). A delegated reader drafted the reading; quotations
    were rechecked by script against the downloaded copy, and any that did not
    match were kept as paraphrase without quotation marks.
date: '2026-11-12'
summary: >-
  The paper presents a draft, consensus "abstract model" for an Argument
  Interchange Format so that argumentation tools and multi-agent systems can
  exchange arguments. It is organized as core ontology plus extensions, an
  abstract model plus several concrete reifications. The core has three
  groups: argument networks, communication (locutions, protocols) and
  context (participants, dialogue type, commitment stores, theory).
---
<!-- inactive-ok-file: TERM-tmp8deza — filed from the exchange "luria experiment design", Proposed or Deferred; cited as filed alongside this entry -->
<!-- inactive-ok-file: CLAIM-179 LIT-755 LIT-759 LIT-761 — Proposed, Unavailable; cited for what each holds, not as settled -->

# NOTE-tmpr9b6m: Chesñevar et al. — Towards an argument interchange format

## Contribution

The I-node/S-node core that later AIF work builds on, and a statement of the design principles
(core plus extensions, evolving by consensus) for an argument interchange standard.

## Key results

- Abstract: AIF "represents a consensus ‘abstract model’ established by researchers across fields of argumentation, artificial intelligence and multi-agent systems."
- Sec. 2: "the core will evolve over time as consensus changes on what is central and applications generate experience", and extensions "would be shared amongst large groups of users (potentially also being merged into the core)."
- Sec. 3.1: "we will not take a position on the precise definition of the notion of “argument” itself".
- Sec. 3.2.2: "There are two kinds of nodes, namely information nodes (I-nodes) and scheme application nodes or scheme nodes (S-nodes)".
- Sec. 3.2.2: three scheme types, "inference schemes, preference schemes and conflict schemes"; Walton's presumptive schemes "constitute a subset of the set of possible inference schemes."
- Sec. 3.2.3: node attributes such as creator, creation date, evaluation and acceptability "may vary and are not part of the core ontology."
- Sec. 3.2.4: "I-to-I edges are forbidden, because I-nodes cannot be connected without an explanation for why that connection is being made."
- Sec. 3.2.5: "rebut, undercut, attack, defeat and defend can in principle be derived from the concepts" of the core.
- Sec. 3.5.1: context includes "Commitment stores: This is a data structure that allows agents to add and remove commitments during their dialogues (Hamblin 1970)."
- Sec. 6, open issue 3: "How should the community of users around the AIF organize themselves to agree on core concepts and extensions?"

## Assumptions

- Interchange between software is the aim; machine-readable syntax and explicit semantics.
- The model should accommodate many formalisms, so it allows cycles and does not fix acceptability.
- Arguments are analysed as finished structures; nothing in the core models an argument's
  development over time, retraction or change of standing.

## Concepts

Argument network; I-node, S-node; RA-, PA-, CA-node; data, conclusion and warrant edges;
meta-reasoning via S-to-S edges; derived concepts (rebut, undercut, defeat); core vs. extension
ontology; abstract model vs. reification; communication (locutions, protocols, commitment stores,
commitment rules); context (participants, dialogue type, background theory, domain ontologies).

## Bearing on the record

A cited it for explicit premises, conclusions, support, attack and argument schemes, “a particularly
close match to Nucleation's ARG and CLAIM relations”. **Mostly accurate.** Premises and conclusions
are edges into and out of S-nodes; support is inference application; argument schemes are the
schemes S-nodes apply. "Attack" is not a core concept: conflict is a CA-node and attack, rebut and
undercut are derived. The "close match" holds best for ARG (an ARG is close to an RA-node, a reified
inference with premises, a conclusion and a form), less for CLAIM relations: the record's `rests_on`
links claim to claim directly, which AIF forbids (no I-to-I edges), and the record's status and
standing are outside AIF's core.

- ADR-061 (an ARG is any claim about support; a claim about what a source says is a THEORY):
  **corroborates the move, with a difference.** AIF's S-node is the reified inference that ADR-061's
  ARG is: a judgement that something supports something, which can itself be attacked (an undercut
  on an RA-node is a CA-node pointing at it, sec. 3.3.1 item 6). But AIF requires an S-node for
  every connection between claims, whereas the record lets `rests_on` connect claims without one.
- ADR-032 (the argument schemes QUESTION, CLAIM, CASE, TERM, ARG): **already engages AIF, from
  memory.** ADR-032 names AIF among the structures the design began from, and rejects "An ARG for
  every claim (AIF's information and inference nodes throughout)" and "A full argumentation ontology
  (AIF, Carneades)", since "These are built to analyse finished arguments. This record develops
  unfinished ones." The reading confirms both premises of that rejection: the I-to-I prohibition is
  what "an ARG for every claim" means, and the paper's core has no notion of development, revision
  or standing. It supports ADR-032's description of AIF.
- QUESTION-tmps5iou (is the coupling of schema change to recorded decision, migration and checks
  what distinguishes luria?): **bears on the governance side.** AIF expects its core to "evolve over
  time as consensus changes" and extensions to be merged into the core, and leaves open how the
  community should "organize themselves to agree on core concepts and extensions". So a standard
  that anticipates schema evolution by consensus, with no mechanism stated: the gap luria's
  recorded decisions fill. Leaves the question open.

Searched the record for Argument Interchange, AIF, Chesñevar, the DOI, Walton, argument
scheme, Toulmin, Dung, Araucaria, IBIS, Compendium, Hamblin. Not held as a LIT (no duplicate); named
only in ADR-032's prose. Missed by the first search:
- CLAIM-179 (when an agent files, the capture cost falls on the party who would otherwise
  re-derive; design-rationale abandonment) and LIT-755 / LIT-759 / LIT-761 (design-rationale
  literature, Unavailable): ADR-032 rejected AIF-everywhere for the capture-cost reason these hold;
  CLAIM-179 is the claim that would reopen that rejection when agents file.
- TERM-tmp8deza and LIT-tmpir70i (Singh, same batch): AIF's commitment stores and commitment rules
  (Hamblin) are a second predecessor for public commitments with rules for changing them.
- ADR-043 (warrant on a CLAIM): AIF's S-to-S "warrant" edges and Toulmin translation are a
  different sense of warrant (the inference licence), not the record's demonstrated/empirical/
  interpretive kind; the shared word should not be conflated.

## Limitations

A draft specification by consensus, explicitly not definitive; no formal semantics for the core;
manuscript read, not the typeset article; use cases and reifications only skimmed.
