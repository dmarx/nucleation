# LEAD-093 progress

- Lead: LEAD-093, "Construct a nucleus that, once formed, takes part in producing or
  repairing the constraints of its own formation, and measure when the loop closes".
- Branch: `claude/lead-093-closing-nucleus` (cut from origin/staging).
- Task: build in numpy a nucleus that speeds formation and, once formed, produces or
  repairs its own formation constraints (extending CASE-190 so the student becomes a
  teacher, or Life eaters); measure the constraint turnover it survives, the outside
  supply it still needs, and when the loop closes (sustains its formation constraints
  without outside supply). File a CASE (executed-study) and claims; dated notes on
  QUESTION-399, QUESTION-361, CASE-190, LEAD-093.

## Done

- Step 1: not already held. No entry cites LEAD-093 but the curation note; no executed
  study cites CASE-190 / QUESTION-399 / QUESTION-361 with such a construction. Neighbours:
  CASE-265 (mutual maintenance c<->r on standing supply), CASE-tmplsvee (scaffold forms
  a nucleus, withdrawn), CASE-tmpfktyl (Life block and eater repair), CLAIM-604.

- Model `closing.py` (produce arm, repair arm, defective nuclei eps, generation-resolved
  version, Gillespie version); 11 tests pass (`test_closing.py`).
- Experiments `experiments.py` e1-e9, results per item in `results/*.jsonl`. e1-e8 and
  e4b done (e6 rerun after adding a repair cost `rcost`, default 0, sensitivity 1:
  first version charged a full unit per repair, which made N non-monotone in sigma and
  broke the bisection). e9 (Gillespie) running, python PID 31790.

## Choices made

- Built a new kinetic model rather than literally extending CASE-190's equations or
  using Life eaters: CASE-190's equations are not all stated in the record (A18's
  fuel demand is missing), and the Life eater repairs only the strike it is shaped
  for (CASE-tmpfktyl) and has no turnover rate to vary. The model closes CASE-190's
  three named gaps (two-way coupling, succession, a non-stipulated teacher).
- Base parameters J=1, delta=0.1, a0=1e-6, a1=0.1, K=2, d=0.1, beta=0.02, kT=0.1:
  chosen so the base point is bistable (founding needed) with a margin of about 2
  in turnover before closure is lost. Illustrative, invented.
- Formation is cooperative in the teacher (Hill 2) so that a founding is needed
  (nucleation); with linear templating the loop self-ignites from any seed.
- "Closed" = a stable maintained state exists with sigma = 0 and N >= 50x the
  spontaneous background; "closed at time t" = withdrawing sigma at t for good leaves
  the nucleus maintained.

- e9 done (python PID 31790 exited).
- Filed: CASE-tmpy4orj (executed-study); CLAIM-tmpocjfb, -tmpnyf9e, -tmpk6abl,
  -tmppgdad (demonstrated theses); CLAIM-tmp1qqso / -tmps1ll3 (alternative readings,
  closure vs autocatalysis, owner's choice); dated notes on LEAD-093, QUESTION-399,
  QUESTION-361, CASE-190; changelog fragment record/changelog.d/lead-093.md.

## Next

- Report to the lead. Owner: choose between the two readings; statuses and stage.
