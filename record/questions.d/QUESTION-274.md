---
number: 274
status: Open
formerly:
- QUESTION-tmpidxeb
title: 'Do two dictionaries of equal fidelity, trained on the same model with different seeds or widths, give the same validated circuit for the same prompt and behaviour, or is a feature circuit fixed only relative to the dictionary that supplies its units?'
version: 2
history:
- version: 1
  date: '2026-10-27'
  note: >-
    Filed when the circuits works read on 2026-10-26 at the owner's
    request raised it twice: the sparse-autoencoder readings found
    features to be a resolution set by dictionary width, and the
    circuit-tracing reading found its authors conceding that their
    dictionary is not guaranteed parsimonious. Neither tests it. A thing
    gets a code the second time it turns up.
- version: 2
  date: '2026-10-27'
  note: >-
    A dated note added: an observation of dictionary-relativity from
    Marks et al., registered and read on 2026-10-27, where the
    dictionary's training data decided whether the features of
    interest came out separate. The question is unchanged.
tags:
- representation-learning
- causality
- philosophy-of-science
date: '2026-10-27'
line: learned-structure
summary: >-
  Feature circuits (sparse feature circuits, transcoder circuits,
  attribution graphs) are stated over the units of a learned dictionary.
  The dictionaries are not unique: features split and merge as the
  dictionary grows, and which concepts get a feature depends on their
  frequency relative to its size. Whether the circuit found for a
  behaviour survives a change of dictionary at equal fidelity is the
  question [THEORY-802](../theory.d/THEORY-802.md) asks of alignments, asked of dictionaries. No work
  the record holds has run the comparison.
---
<!-- inactive-ok-file: THEORY-802 THEORY-1016 THEORY-1014 — Proposed; the thesis this is the dictionary-level form of, and the circuits readings' accounts it is raised by, cited as open -->

# QUESTION-274: Do two dictionaries of equal fidelity, trained on the same model with different seeds or widths, give the same validated circuit for the same prompt and behaviour, or is a feature circuit fixed only relative to the dictionary that supplies its units?

## Why it is a question

Three of the circuits works read on 2026-10-26 build circuits over the
features of a learned dictionary: sparse autoencoders in Marks et al.'s
sparse feature circuits ([LIT-1532](../literature.d/LIT-1532.md)), per-layer transcoders in Dunefsky
et al. ([LIT-1554](../literature.d/LIT-1554.md)), and cross-layer transcoders in Ameisen et al.'s
attribution graphs ([LIT-1552](../literature.d/LIT-1552.md)). Each validates its circuit by
interventions on those features. None asks whether another dictionary of
the same fidelity would have given the same circuit.

The record has two reasons to doubt that it would.

- **The units are a resolution.** In Towards Monosemanticity and Scaling
  Monosemanticity, features split and merge as the dictionary widens, so
  "the number of features is not well-posed" ([THEORY-1016](../theory.d/THEORY-1016.md)), and
  whether a concept gets a dedicated feature depends on its training
  frequency relative to the dictionary's size ([THEORY-992](../theory.d/THEORY-992.md)).
- **The authors concede the choice.** Ameisen et al. say features split
  with the size of the cross-layer transcoder and that "there's no
  guarantee that the CLT features are the most parsimonious way to split
  up the computation" ([NOTE-1185](../notes.d/NOTE-1185.md)).

Against that, Towards Monosemanticity's features agree across two seeds
better than neurons do (median activation correlation 0.72 against 0.46,
[NOTE-1191](../notes.d/NOTE-1191.md)), but that compares features by their activations, not the
circuits built over them.

It is [THEORY-802](../theory.d/THEORY-802.md)'s thesis moved from alignments to dictionaries.
[THEORY-802](../theory.d/THEORY-802.md) says interchange interventions can leave the mediating
direction fixed only relative to a decomposition into units; here the
decomposition is the dictionary, and the question is whether the circuit,
not only the units, is relative to it.

## What would answer it

- **Invariance.** For a stated behaviour and model, dictionaries trained
  with different seeds, or at different widths matched for fidelity
  (reconstruction loss, or the replacement model's agreement with the
  model under perturbation, [THEORY-994](../theory.d/THEORY-994.md)), give circuits that map onto
  each other: the same pathways, with features matched by their effects,
  up to splitting and merging stated in advance.
- **Relativity.** The same comparison gives circuits that differ in their
  pathways, not only in how finely the features are cut, each validated
  by its own interventions. Then the circuit is a fact about the
  model-and-dictionary pair.

A natural first case is subject–verb agreement across a relative clause,
where sparse feature circuits find several converging pathways
([THEORY-1014](../theory.d/THEORY-1014.md)): whether those pathways survive a change of dictionary
is the question in one behaviour.

## What would not answer it

- Agreement of features across seeds by activation alone, which is what
  the record already holds.
- A single dictionary's circuit validated more thoroughly. The question
  is about the comparison.
- A difference in circuits between dictionaries of unequal fidelity,
  which the fidelity gap could explain.

## Note of 2026-10-27: a case from the hidden-objectives audit

Marks, Treutlein et al. ([LIT-tmpx8s6k](../literature.d/LIT-tmpx8s6k.md), [NOTE-tmp8fmhx](../notes.d/NOTE-tmp8fmhx.md)), read on
2026-10-27, report an observation of the kind this question asks about,
though not a test of it. In their model organism, a 1M-feature SAE trained
on the pretraining corpus alone gave better reward-model-bias features
than one trained with chat data: by their account (footnote 18), even a
small amount of chat-formatted data made such features merge into
undifferentiated "Assistant" features. Here a dictionary's training data,
not its width or seed, decided whether the units an audit relied on came
out separate. It is one observation, reported in a footnote, with no
circuit compared across the two dictionaries.
