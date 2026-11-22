# LEAD-053 progress

- Lead: LEAD-053, "Find a non-arbitrary way to choose the constraint set for an agent's regulatory capacities"
- Branch: claude/lead-053-maintenance-rule (cut from origin/staging)
- Task: propose a rule for choosing the maintenance constraints K that ARG-007's mapping premise needs, and test it on the record's cases (CASE-036 at least, the ground of ARG-007). File the rule as a CLAIM, the test as a CASE or dated notes; file alternatives where a reading is the owner's call; dated notes on CLAIM-099, ARG-007 and LEAD-053.

## Step 1 (target already held?)

Checked: grep for LEAD-053, "maintenance constraint", "constraint set", "non-arbitrary", "mapping premise". Not held. Nearest: CLAIM-195 (for an argument K is fixed by an amendable decision; explicitly "does not answer ARG-007's mapping premise for agents"), NOTE-719 (Di Paolo's adaptive closure as "a lead, not an answer"), THEORY-134 ("K is not supplied by the theory"), TERM-070 (closure of constraints).

## Choices so far

- The lead names no cases beyond ARG-007 (ground CASE-036) and its training
  note (CLAIM-367). Tested also on CASE-111, CASE-112, CASE-227, the formal
  cases ARG-007's premises cite or that carry the same separation.
- The rule (dependence rule): membership of K by production dependence of the
  constraints realizing the named capacity (TERM-070's "depends on");
  threshold of each at the least level at which what depends on it is still
  produced, at the top the capacity's exercise level; union over
  substitutable routes. Threshold at the separatrix rejected (makes K the
  basin, collapses K into the kernel, empties CLAIM-079); threshold at
  "any positive level" rejected (b -> 0 asymptotically never leaves {b > 0}).
- The owner's call: the boundary reading, whether constraints the capacity
  depends on but produced outside the agent belong to K (wide) or are
  conditions/parameters (narrow). Verdicts differ on CLAIM-367's network and
  CASE-227 with outside supply. Filed as two alternative claims resting on
  the core rule.
- Stipulated K (the agent's own standard, CLAIM-195's transfer) tested and
  not proposed: on CASE-036 it is the lock-in's own standard and sees
  nothing. Reported in the test CASE, not filed as a claim.

## Done

- Step 1: target not held.
- Computation: maintenance_rule.py + tests (8 pass), results.txt.

## Next

- File: core CLAIM, two alternative CLAIMs, test CASE (executed-study).
- Dated notes: ARG-007, CLAIM-099, LEAD-053, CLAIM-195.
- Changelog fragment record/changelog.d/lead-053.md.
