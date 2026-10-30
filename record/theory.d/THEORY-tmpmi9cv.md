---
status: Proposed
promote_when: >-
  Two results, of different kinds. For the representation: an independent
  round-trip test of the DISINFOX mapping (incidents in, STIX out, back
  in) that reports what is preserved and lost, and a comparison with the
  OASIS DAD-CDM model on the same incidents. For the use: a deployment
  study in which analysts in several organisations consume the shared
  incidents, measuring whether correlation, exposure or reuse of labels
  improves. The first kind promotes the representational half; only the
  second can bear on whether sharing in this form helps. A further count
  of incidents ingested cannot settle either.
title: 'Disinformation incidents carried in STIX 2.1 as the DISINFOX mapping carries them are an interoperable representation that survives exchange between organisations, and sharing them in this form improves analysts'' correlation and exposure of incidents and their reuse of labels'
version: 1
tags:
- society-and-governance
date: '2026-10-30'
source:
- LIT-083
extends:
- THEORY-651
summary: >-
  The thesis Sánchez González et al. motivate, filed beside [THEORY-651](THEORY-651.md) by
  the twenty-fourth status review ([ADR-065](../decisions.d/ADR-065.md) §3; [ADR-047](../decisions.d/ADR-047.md) kind 1).
  [THEORY-651](THEORY-651.md), Active, holds the mapping and its demonstration; nothing
  beyond ingestion was measured, so whether the representation is faithful
  and whether sharing helps is this entry's question, with [THEORY-651](THEORY-651.md)'s
  old condition.
---
<!-- inactive-ok-file: LIT-083 — Proposed; the preprint this thesis comes from, read in full in NOTE-028 -->

# THEORY-tmpmi9cv: Disinformation incidents carried in STIX 2.1 as the DISINFOX mapping carries them are an interoperable representation that survives exchange between organisations, and sharing them in this form improves analysts' correlation and exposure of incidents and their reuse of labels

## Source

Sánchez González et al. (2025), [LIT-083](../literature.d/LIT-083.md), read in full in [NOTE-028](../notes.d/NOTE-028.md). Better
correlation, faster exposure and global collaboration are the paper's
motivation (C5), not its results.

## Where the evidence stands

The mapping and the ingestion of 118 incidents are [THEORY-651](THEORY-651.md), Active, which
this entry extends. No round-trip fidelity check, comparison with DAD-CDM,
user study or correlation result is reported. The `promote_when` above is [THEORY-651](THEORY-651.md)'s condition before the twenty-fourth status review promoted it, carried here unchanged, because it asks what would make the thesis true and not what the source says.
