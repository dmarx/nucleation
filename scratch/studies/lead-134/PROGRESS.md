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
- model.py + test_model.py (8 tests pass). Grid run (60 configs, 2.4s):
  results.jsonl + summary.json + README.md written and committed.
- RESULT: both self-models reconstruct the outcome exactly (recon err ~0) with
  equal params/inputs -> coarseness threat defeated. Localization: accurate
  0.94 vs centralized 0.21 (~chance). Governance collateral: accurate 0.34 vs
  centralized 0.46 (60/60); cumulative err 54/60. The centralized self-model
  misdescribes control in a predictable direction; the error is in the
  attribution. Answers Drayson's horn unconditionally FOR THIS MODEL.

## Next
- File record entries: CASE (executed-study, standing documented) variant_of
  CASE-114, illustrates CLAIM-355; CLAIM (Proposed, thesis/counter, warrant
  demonstrated) with the finding; dated notes on CLAIM-355, CASE-114,
  QUESTION-061, LEAD-134; changelog fragment. Do NOT change statuses/stage.
