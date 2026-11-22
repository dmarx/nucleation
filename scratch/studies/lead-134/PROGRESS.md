# LEAD-134 progress

- Lead: LEAD-134 -- "Run the imagined owner": build CASE-114's distributed-control
  system with a centralized self-model, log the self-model's reports of what
  caused what against the true causes.
- Branch: claude/lead-134-distributed-self-model (from origin/staging)
- Advances: CLAIM-355 (Proposed), QUESTION-061 (Open). Operationalizes CASE-114.

## Task as understood
Build in numpy two systems with EQUIVALENT distributed control and similar
behaviour. One has a self-model representing the actual division of labour; the
other a self-model that attributes control to a single centralized owner. The
two self-models are MATCHED IN CAPACITY (same parameter count, equal predictive
fit on the aggregate outcome) so any divergence is wrong-about-control, not
merely-coarser (CASE-114's main threat). Record the true causes of errors apart
from the self-model's reports and compare on A27's four measures: authorship,
explanation of mistakes, component-cause identification, governance revision
after error. Phase 1 open-loop (self-model narrates, control held fixed and
provably identical across systems); Phase 2 closed-loop (self-model feeds
governance -- A27 section 12 loop, which the case warns breaks the held-fixed
equivalence; that divergence is the fourth measure). pytest for nontrivial fns.

## Design choices made (mine; said why in the CASE)
- Scalar-aggregate inverse problem: self-model sees the integrated error, infers
  per-component causes from its causal prior. Accurate prior = K independent
  components (true graph); centralized prior = star graph, one owner command
  driving all effectors in fixed proportion. This is where equal capacity +
  divergent attribution falls out cleanly.
- Owner's calls (NOT taken): whether this answers Drayson unconditionally and
  whether CLAIM-355 is promoted; marking the lead Done/stage. Filed as Proposed
  CLAIM + dated notes only.

## Done
- Read CLAUDE.md, design principles, run-lead skill, LEAD-134, CASE-114,
  CLAIM-355, QUESTION-061, docs/record.md field defs. Confirmed target not held.
- Branch cut; PROGRESS.md pushed.

## Next
- Write model + sim (model.py), pytest (test_model.py), run, write results JSON.
- File: CASE (executed-study) illustrating CLAIM-355, variant_of CASE-114;
  CLAIM (Proposed) with the finding; dated notes on CLAIM-355, CASE-114,
  QUESTION-061, LEAD-134; changelog fragment; study README.
