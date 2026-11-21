---
status: Read
paper: LIT-tmp166hz
title: 'Tenney, Das and Pavlick — BERT and the classical pipeline'
version: 1
history:
- version: 1
  date: '2026-11-21'
  note: >-
    Read on 2026-11-21 by a delegated reader from arXiv 1905.05950v2 (9
    Aug 2019): all text; Figures 1, 2, A.2, A.3 and 3 read from the
    rendered images; Figures A.1 and A.4–A.7 by caption. Running notes on
    the branch claude/readers/tenney-pipeline (ADR-108). Quotations the
    filing leans on rechecked by the filer by script against the
    downloaded text.
date: '2026-11-21'
summary: >-
  Probing frozen BERT finds syntactic information best extracted lower and
  more locally, semantic information higher and spread across many layers;
  the order holds in aggregate and is weak in the middle, where tasks
  overlap and their order changes between metrics and models; individual
  examples revise lower-level decisions from higher-level information.
---
<!-- inactive-ok-file: ADR-108 THEORY-1030 THEORY-104 — Proposed; cited in the readings of 2026-11-21 -->
<!-- inactive-ok-file: CLAIM-tmpcvuyr — Proposed, Deferred or new; filed in this contribution of 2026-11-21 or the ones it builds on -->

# NOTE-tmpb5hqz: Tenney, Das and Pavlick — BERT and the classical pipeline

## Contribution

Two layer statistics (centre of gravity of learned mixing weights; expected layer from cumulative probes), a concentration measure, and per-example traces.

## Key results

1. **The ordering** (§4): "POS tags processed earliest, followed by constituents, dependencies, semantic roles, and coreference".
2. **Weak in the middle** (Fig. 1, A.2): in BERT-large the five pipeline tasks' centres of gravity lie between layers 11.7 and 15.8 of 24; dependencies, entities and SRL change order between the two metrics and between BERT-base and BERT-large. The robust contrast is part of speech and constituents early against coreference late.
3. **Spread** (§4): "information related to semantic tasks is generally spread across the entire network".
4. **Revision from above** (§4.1): "while the pipeline order holds on average … for individual examples the model is free to and often does choose a different order"; "often" rests on selected examples.
5. **Caveat** (Limitations): the observation of a pattern "does not tell us how it is used".

## Assumptions and concepts

Frozen encoder; probe-extractable information counted as encoded; one model family. Concepts: edge probing, scalar mixing, centre of gravity, expected layer, localizability.

## Bearing on the record

- **CLAIM-tmpcvuyr** (qualifies; supports more than it defeats). The ordering is of overlapping regions at which a probe best extracts each kind of information, not a sequence of levels each depending on the last; defeater (b) is not met. Version 2 rewords the claim's sentence on this paper accordingly.
- **Recheck**: THEORY-1030 and THEORY-1033 (Geva and colleagues, held: a shallow-to-semantic gradient across FFN layers, and the residual stream refining the prediction) carry both halves of CLAIM-tmpcvuyr in one reading and are added to its grounds; THEORY-104 (best readout below the top) matches the drop in the last one or two layers.

## Limitations

One architecture; correlational probing; the two metrics disagree; no error bars; anecdotal revision evidence.
