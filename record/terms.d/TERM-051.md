---
number: 51
status: Active
formerly:
- TERM-tmpuyzeb
title: 'drive profile'
version: 3
history:
- version: 2
  date: '2026-10-11'
  note: >-
    The name is settled. The owner deferred the choice, and "drive
    profile" is kept over the alternatives, for the reasons under "Why
    this name". The definition is unchanged.
- version: 3
  date: '2026-11-12'
  note: >-
    Draws on THEORY-069 ("circular causality, as an order
    parameter has"), THEORY-133 ("Kim's exclusion worry is met
    system by system") and THEORY-138 ("under the interventionist
    reading"). First application of draws_on (ADR-095). No
    other change.
tags:
- agency
- complex-systems
date: '2026-10-11'
line: distributed-agency
summary: >-
  How the drive of a described system is apportioned, at a time and for a
  stated macro-variable and target, along two axes. Within a level: one
  member drives, the members drive each other, or the drive is diffuse.
  Across levels: aggregate, top-down, bidirectional or emergent, read
  from the information decomposition's downward-causation and
  causal-decoupling terms. A profile is time-indexed.
draws_on:
- THEORY-069
- THEORY-133
- THEORY-138
---
<!-- inactive-ok-file: ADR-095 — Proposed; the decision its history note of 2026-11-12 applies -->
<!-- inactive-ok-file: CLAIM-158 — Proposed; cited in the note of 2026-11-07 -->
<!-- inactive-ok-file: CLAIM-167 — Proposed; the claim that made direction an architecture, open -->
<!-- inactive-ok-file: CLAIM-155 — Proposed; its tier names are why one rejected name would blur, not leaned on -->
<!-- inactive-ok-file: QUESTION-009 — Deferred; the agency question kept apart -->
<!-- inactive-ok-file: THEORY-069 — Proposed; readings the definition borrows its cases from, with their standing as it is -->

# TERM-051: drive profile

## Definition

For a system described at two levels, parts X and a macro-variable V that
supervenes on them, and for a stated target ([CLAIM-152](../claims.d/CLAIM-152.md)), the **drive
profile at time t over a window** is the pair:

- **Within a level: the architecture** ([CLAIM-167](../claims.d/CLAIM-167.md)).
  - *Hierarchical*: one member's state predicts the others' and not the
    reverse.
  - *Peer*: mutual.
  - *Diffuse*: no member predicts the others beyond the rest.
- **Across levels: the kind.** This is read from the information
  decomposition of [LIT-025](../literature.d/LIT-025.md) (Rosas et al.'s ΦID, as reviewed there).
  - *Aggregate*: no synergy. V adds nothing to predicting the future
    beyond X, and V is a resultant.
  - *Top-down*: downward causation D > 0. V predicts individual parts'
    futures beyond what the parts do. It is strongest when the effect does
    not depend on how V is realized ([THEORY-133](../theory.d/THEORY-133.md)).
  - *Bidirectional*: D > 0 while V is itself produced by the parts' joint
    activity. This is circular causality, as an order parameter has in
    [THEORY-069](../theory.d/THEORY-069.md).
  - *Emergent*: causal decoupling G > 0. V predicts its own future in a way
    no subset of parts accounts for. No part drives, and "who drives?" is
    answered "the whole, at this level".

**Time-indexed.** The profile is estimated over a window and can change: a
system can move between kinds, and a member can come to drive and stop. A
sequence of profiles is the system's drive history.

## What it is not

- **Not agency.** A profile says where drive sits. Whether the driver is an
  agent is [QUESTION-009](../questions.d/QUESTION-009.md).
- **Not a metaphysics of levels.** Downward causation here is the
  information-theoretic quantity, under the interventionist reading of
  [THEORY-138](../theory.d/THEORY-138.md). Kim's exclusion worry is met system by system, as in
  [THEORY-133](../theory.d/THEORY-133.md), not settled once.
- **Not free of choices.** The decomposition depends on the macro-variable
  and coordinates ([LIT-025](../literature.d/LIT-025.md) defends this), so profiles are relative to them.

## Why this name

The owner deferred the choice on 2026-10-11: "I'll defer too you on the
nae question." The name is kept.

- **"Drive"** is the question the term answers, "who drives?", in the
  words the owner asked it in.
- **"Profile"** says it is a reading across axes, at a time and for a
  target, not a property the system has once and for all.
- **"Control architecture"** was rejected. "Architecture" already names
  the within-level axis, and "control system" is the lowest tier of
  the nesting in [CLAIM-155](../claims.d/CLAIM-155.md). The name would blur both.
- **"Causal regime"** was rejected. "Regime" is the will paper's
  action-generating regime ([TERM-019](TERM-019.md)), a different thing.

## Note of 2026-11-07: top-down against bidirectional, from the third synthesis review

The summary reads the kinds "from the information decomposition's downward-causation and causal-decoupling terms". Those terms do not separate top-down from bidirectional.

- **Both kinds have D > 0.** Bidirectional adds "D > 0 while V is itself produced by the parts' joint activity".
- **V is always produced by the parts in the predictive sense.** V supervenes on the parts in every kind, and [CLAIM-158](../claims.d/CLAIM-158.md) says top-down "cannot mean that the higher level drives without its parts, because it is realized by them". Since V at t is a function of the parts' state at t, the data-processing inequality gives I(X_t; V_{t+1}) ≥ I(V_t; V_{t+1}): the parts' state always carries at least as much information about V's next value as V's own state does. The reader checked this on 5,000 random Markov chains over three binary parts; the least margin was 0 to rounding.

So the decomposition as stated separates three regions, aggregate, D > 0 and G > 0, not four. Telling bidirectional from top-down needs a criterion this term does not name:

- a named quantity of upward causation; or
- production over time at a declared time resolution, in which case [CLAIM-528](../claims.d/CLAIM-528.md)'s third part makes the boundary between the two move with that resolution.

The definition is unchanged; this note marks what it does not yet fix.
