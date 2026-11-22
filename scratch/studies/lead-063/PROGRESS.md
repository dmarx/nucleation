# LEAD-063 progress

- Lead: LEAD-063 (advances QUESTION-046)
- Branch: claude/lead-063-integration-measure
- Task: apply one integration / dynamic-core measure, with one anti-nesting
  rule, by the same procedure to a model of a modular mind and to a model of
  a group, and compare the verdicts. numpy + pytest. File a CASE
  (executed-study), a CLAIM if warranted, dated notes on QUESTION-046 (and
  entries advanced) and on LEAD-063.

## Done

- Step 1: target not already held. No CASE or CLAIM computes an integration
  measure for a modular mind and a group; QUESTION-046 stays Open, its notes
  (2026-11-01, 2026-11-12) say no measure is computed; THEORY-043's
  promote_when still asks for it.
- phi.py (measure, models, exclusion verdict), test_phi.py (10 pass).
- run.py launched (sweep -> results.jsonl, resumable; PID in scratchpad
  lead-063/run.pid).

- check_mind.py done (complex_check.jsonl): exhaustive exclusion over all
  subsets of the 9-unit mind. Where the level verdict says "mind", the
  main complex crosses every module (whole or whole minus one unit); where
  it says "module", the complex is a module, except width 1, c=0.12, where
  it is the three linked units [0,3,6], a cross-module core.
- check_small_group.py launched (small_group.jsonl): exhaustive exclusion on
  a 12-unit group (2 members x 2 modules x 3 units), to see whether a
  complex ever crosses members without being the whole.
- Created stubs CASE-tmp5fglr and CLAIM-tmpfoatc (to be filled).

## Next

- Commit results.jsonl; summarise (summarise.py); README.
- File CASE, CLAIM (if warranted), notes on QUESTION-046, THEORY-043?
  (no: lead advances only QUESTION-046; THEORY-043 is a held account —
  a dated note there is allowed and its promote_when names this exactly),
  LEAD-063; changelog fragment.

## Choices

- Measure: Barrett & Seth's Phi_AR (whole-minus-parts self-information of a
  linear Gaussian VAR(1)), at the size-normalized minimum information
  bipartition. Why: the simplest integration measure that is exact in
  closed form for a model, so nothing is sampled; it is the Phi the
  record's THEORY-043 names, in its tractable Gaussian form.
- Anti-nesting rule: IIT's exclusion postulate (of nested candidates, the
  one with the larger Phi is the subject). Why: it is the anti-nesting rule
  THEORY-043 names; it needs Phi at every level, so applying it computes
  the measure for both models.
- Models: modular mind = 3 modules x 3 units, dense inside (w=0.12),
  `width` reciprocal links of weight c between each pair of modules.
  Group = 3 members, each that modular mind (c=0.15, width 3, a unified
  mind by the rule), linked member to member by `width` links of weight g.
  Why: the group is the same construction one level up, so one procedure
  and one parameter (coupling x bandwidth between parts) cover both.
- Group MIB searched over cuts along module seams (255), checked against
  200 random cuts by test.
- Sensitivity: unnormalized MIB as well.
