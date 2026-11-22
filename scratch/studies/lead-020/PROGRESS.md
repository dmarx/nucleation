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

## Next

- Model + tests + runs.
- Filing.

## Choices made

(added as they are made)
