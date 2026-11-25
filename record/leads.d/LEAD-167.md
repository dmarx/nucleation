---
number: 167
status: Open
formerly:
- LEAD-tmptxwpx
title: 'Compute Bourrat''s individuality measures on a model of an evolutionary transition'
version: 2
history:
- version: 2
  date: '2026-11-22'
  note: >-
    Note of 2026-11-22 added: carried out on a minimal scaffolding model
    (CASE-320, CLAIM-884); what remains is listed. Status and
    stage unchanged.
stage: idea
priority: high
method:
- formal
tags:
- individuation
- information-theory
date: '2026-11-19'
line:
- distributed-agency
advances:
- QUESTION-115
- QUESTION-118
summary: >-
  The curation of 2026-09-26 says another reading cannot settle it. Named
  in the curation entry of 2026-09-26 (063703). Filed by the backlog audit
  of 2026-11-19.
---
<!-- inactive-ok-file: CASE-320 CLAIM-884 LIT-005 LIT-049 THEORY-607 — new, filed 2026-11-22 from LEAD-167's computation, and the Proposed papers and reading it bears on -->
<!-- inactive-ok-file: LIT-1940 — Deferred; Black et al.'s own model, named as not reproduced -->

# LEAD-167: Compute Bourrat's individuality measures on a model of an evolutionary transition

## What it would do

Pick a standard transition model and compute both measures.

Where the record names it:

- The curation entry of 2026-09-26 (063703): "an explicit computation of
  its individuality measure on a model of an evolutionary transition.
  Another reading cannot supply that."

## What would count

Measures that track the transition bear on [QUESTION-115](../questions.d/QUESTION-115.md)'s search
procedure.

## Note of 2026-11-22: carried out on a minimal scaffolding model

**What was done.** Both measures were computed exactly, with numpy, on a
minimal ecological-scaffolding model of 256 states, with pytest tests:

- Bourrat 2024's Â, C1 and C2 ([LIT-005](../literature.d/LIT-005.md)), with Krakauer et al.'s A*, A and
  nC beside them;
- Bourrat 2023's δC and δC|E over all 203 partitions of the cells
  ([LIT-049](../literature.d/LIT-049.md)).

The study is [CASE-320](../cases.d/CASE-320.md), and the finding is [CLAIM-884](../claims.d/CLAIM-884.md). Materials are under
scratch/studies/lead-167/.

**Why this model.** The scaffolding scenario is the one [LIT-005](../literature.d/LIT-005.md) names. Black
et al.'s own model ([LIT-1940](../literature.d/LIT-1940.md)) is unread and has no exact distribution, so
only the scenario's skeleton was built. λ, which moves the patch's cohesion
from the scaffold to the cells, is swept rather than evolved.

**The result.** The two measures agree that the patch partition is the
structure, and they part on the transition:

- C2's variance falls with endogenisation, and Â rises.
- δC|E is exactly zero for the patches before and after.
- C1 passes everything.
- Each measure passes a counterfeit. Â passes the patch with its external
  scaffold. δC|E passes every partition of a common-input population.

**What remains.**

- Black et al.'s own model, once read ([LEAD-176](LEAD-176.md)).
- The transition evolved under collective-level selection, including the
  onset of scaffolding, which this model does not have. Bourrat's sign for
  that onset, I(E1′; Ŝ1) rising, therefore went untested.
- The multi-trait δC.
- Cells that are not exchangeable within a patch.

**The owner's calls.**

- Whether to adopt the CASE and the CLAIM.
- Whether [LIT-005](../literature.d/LIT-005.md)'s and [LIT-049](../literature.d/LIT-049.md)'s Proposed standing changes.
- Whether the cost-priced distributional variant meets [THEORY-607](../theory.d/THEORY-607.md)'s
  promote_when.

The lead's status and stage are left for the owner.
