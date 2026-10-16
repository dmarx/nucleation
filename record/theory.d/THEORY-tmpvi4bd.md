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
title: "Disinformation incidents labelled with DISARM techniques can be carried in standard STIX 2.1 without extending it, as an intrusion set that uses attack patterns, is attributed to a threat actor and targets locations; the DISINFOX mapping that moved 118 incidents into OpenCTI this way drops their content, narratives, channels, evidence and the confidence of their attribution"
version: 1
tags:
- society-and-governance
date: '2026-10-16'
source:
- LIT-083
summary: >-
  Sánchez González et al. (2025), [LIT-083](../literature.d/LIT-083.md), an unreviewed preprint read in
  [NOTE-028](../notes.d/NOTE-028.md). The mapping is explicit (four STIX object types, three
  relationship types) and was exercised end to end on 118 incidents; the
  reading rates that demonstration strong. Nothing beyond ingestion was
  measured. Attribution is one ungraded edge to an actor, typically a
  nation-state, which is the layer the EEAS's Exposure Matrix grades in
  four tiers. Proposed because the source is an unevaluated preprint and
  its claim of priority is narrower than its abstract says.
---
<!-- inactive-ok-file: LIT-083 — Proposed; the preprint this account rests on, read in full in NOTE-028, and the account is Proposed for that reason -->

# THEORY-tmpvi4bd: Disinformation incidents labelled with DISARM techniques can be carried in standard STIX 2.1 without extending it, as an intrusion set that uses attack patterns, is attributed to a threat actor and targets locations; the DISINFOX mapping that moved 118 incidents into OpenCTI this way drops their content, narratives, channels, evidence and the confidence of their attribution

## Source

Sánchez González et al. (2025), [LIT-083](../literature.d/LIT-083.md), "Toward interoperable
representation and sharing of disinformation incidents in cyber threat
intelligence", a preprint submitted to *Computers & Security*, read in full
in [NOTE-028](../notes.d/NOTE-028.md).

## What was actually shown

**The mapping (§4, Tables 3–4).** An incident becomes a STIX
`IntrusionSet` (name, description, `first_seen`, labels "incident" and
"disinformation"), not STIX 2.1's own stub `incident` object. Its actor
becomes a `ThreatActor` (e.g. `nation-state`), each technique an
`AttackPattern` reused from DISARM's own generated objects, and each
targeted country a `Location`. The relationships are `uses`,
`attributed-to` and `targets`. There are exactly four object types and
three relationship types.

**The pipeline (§5).** A frontend, a backend with a document store, a public
HTTP API and a custom OpenCTI connector. 118 incidents were "modeled,
stored, shared, and consumed successfully" (§6); OpenCTI renders their
techniques against the DISARM matrix.

**Why DISARM (§3, Table 1).** Of five frameworks compared on seven features,
only DISARM has STIX2 codification, staged phases and the ATT&CK analogy.
DISARM "does not explicitly offer actor-focused analysis" (§3.1.2).

**What could have come out otherwise.** DISARM incidents could have needed
STIX extensions to be ingested. They did not, which is the demonstration
the reading rates strong ([NOTE-028](../notes.d/NOTE-028.md), C1).

## What this does not say

- **That STIX cannot carry graded attribution.** The paper does not try.
  Whether STIX's `confidence` property or opinion objects could hold it
  without leaving the standard is open ([NOTE-028](../notes.d/NOTE-028.md), open questions).
- **That sharing helps.** Better correlation, faster exposure and global
  collaboration are motivation (C5), not results. No fidelity check, error
  rate, user study or correlation result is reported.
- **That it is the first such effort.** The paper itself describes the
  OASIS DAD-CDM model (2023) and an existing OpenCTI DISARM connector (C4,
  weak).
- **That the labels are reliable.** Labelling is manual and trusted; the
  dataset mixes three sources and does not say how many incidents the
  authors labelled. Small slips (a `first_seen` a month before the
  narrative's date; "fake research" in one place and "Fake Experts" in
  another) are the kind a hand pipeline propagates.
- **That language models can do the labelling.** One sentence of future
  work (C6), untested.
- **That the reused objects are safe in a shared instance.** They carry
  `source_name: "mitre-attack"`; whether they could collide with genuine
  ATT&CK objects is noted in [NOTE-028](../notes.d/NOTE-028.md) and unverified.

## Connections

- **[THEORY-tmpwx87w](THEORY-tmpwx87w.md)** (the 3rd EEAS FIMI report, [LIT-084](../literature.d/LIT-084.md)). The EEAS says
  all 505 of its 2024 incidents are encoded in STIX and calls for FIMI
  analysis to be integrated with CTI. Its Exposure Matrix sorts channels
  into four evidence-graded tiers of state linkage, which is the layer this
  schema reduces to a single `attributed-to` edge. The EEAS does not
  publish its encoding, so the two cannot be compared field by field.
- The EEAS anticipates attribution "based on recurring attack patterns and
  combinations of STIX objects", as with APTs ([LIT-084](../literature.d/LIT-084.md), p. 19). An
  `IntrusionSet` mapping would support that use; this paper does not
  attempt it.
