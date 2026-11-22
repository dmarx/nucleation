# LEAD-020 progress

- Lead: LEAD-020 (advances QUESTION-121)
- Branch: claude/lead-020-nonlockin-ablation (cut from origin/staging)

## Task as understood

QUESTION-121 asks for "a loop that does not lock in, with action held fixed,
and a demonstration that removing a given candidate makes it lock in". Build
a single-mind judgement-observation loop in simulation (numpy, pytest) in
which action is held fixed (the agent cannot change the world or choose when
its inputs arrive), implement the question's five candidates each with its
stated "Against", show the full loop tracks a switching world, then ablate
each candidate alone and report which removals produce lock-in. File a CASE
(executed-study), a CLAIM if warranted, dated notes on QUESTION-121 and
LEAD-020 (and on entries the result bears on), and a changelog fragment.

## Step 1 check (target already held?)

Not held. A grep of record/ for QUESTION-121 and LEAD-020 finds CASE-106 /
CLAIM-340 (candidate 3 in the linearization, via QUESTION-239), CLAIM-342,
CLAIM-339, CLAIM-413, SYNTHESIS-050, LEAD-092 and readings; none builds a
non-lock-in loop with action fixed or ablates candidates. No remote branch
for this lead.

## Done

- Step 1 check.
- loop.py (model), test_loop.py (11 tests pass), run.py (factorial x
  one-at-a-time parameter grid, resumable JSONL to results.jsonl).
- Exploratory finding at defaults: full loop never locks in; no single
  removal from the full loop makes it lock in (redundancy); minimal loops
  without lock-in exist in which removing commitment, processing signals
  or exogenous capture produces lock-in; removing an evidence channel
  (sense, body, others) only ever blinds or rescues; adding the body to
  sense+capture produced lock-in (0.77).
- Background run started (PID in scratchpad/lead-020/run.pid), ~35 min.

## Next

- analyse.py over results.jsonl; README; CASE, CLAIM, notes, changelog.

## Choices made

- Model: CASE-099's (m, a) loop made nonlinear and bounded, inside one mind.
  Authority shapes interpretation by a direct push (beta) and by attention
  that attenuates readings favouring the other hypothesis (the loop
  selecting its own evidence without action). Action held fixed = the
  world's state sequence and input arrival never depend on the loop
  (tested).
- Each candidate is implemented with QUESTION-121's "Against" built in:
  readings bent by the interpretation (kappa), attenuable by attention,
  trust in testimony learned by agreement, disfluency computed only on
  attended inputs, commitment scored against evidence as read (CASE-106).
- Candidate 1 is split in two switches: the channel (sense) and exogenous
  capture (capture), since the question names both and they behave
  differently.
- "Removing commitment" has two readings: scoring against the dominant
  interpretation (Regime A, the default) or revising predictions after the
  evidence (posthoc, no score, CLAIM-340). Both are run.
- Default eta = 0.5, chosen so that the bare loop (sense only, Regime A)
  locks in for every seed: a loop that would lock in without anchors.
- Lock-in = failing, within a 300-step block, to hold sign(m) = h for 20
  consecutive steps after a switch away from the held interpretation.
  Configurations that never track even the first block are "blind", not
  locked in.
