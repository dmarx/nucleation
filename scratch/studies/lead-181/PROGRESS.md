# LEAD-181 progress

- Lead: LEAD-181 (advances CLAIM-662, CLAIM-657, CLAIM-663, QUESTION-279, QUESTION-456)
- Branch: claude/lead-181-penalties-inquiry (cut from origin/staging)
- Task: build CASE-249's simulated institution (requirements visible and
  hidden, inquiry that discovers hidden ones, an internal evaluator that sees
  only discovered ones, an independent one that sees all), run it with and
  without penalties for newly recognized violations, and measure how much
  inquiry an adaptive institution undertakes. File an executed-study CASE,
  Proposed CLAIMs, dated notes and a changelog fragment.

## Done

- Step 1: checked the record. No simulation of CASE-249 is held: no
  scratch/studies/ directory or entry cites it as run; CASE-249 says "Not
  run"; CASE-290 says no such study is held.

- Step 2: model.py, test_model.py (16 pass), study.py (results.json,
  results.md), sweep.py (sweep.md), README.md. Finding: under the penalty
  the optimal inquiry is 0 in every setting and learners converge near 0;
  scored by the independent evaluator, 5-6 of 10 units. Against an
  internal regime without the penalty (amnesty, none), inquiry is also 0
  when it is costly and has no other value (S1, S3); it is higher than
  under the penalty only when inquiry is costless (S2: tied 0-4 / 0-6,
  learned about 3) or being found out from outside costs (S4, sigma = 3:
  1 against 0). Sweep: at large sigma pen and amnesty agree.

- Step 3: filed CASE-tmp8mk6w (executed study), CLAIM-tmpbbfcj (pathwise
  dominance, demonstrated), CLAIM-tmpjz94s and CLAIM-tmp0bqyu (alternative
  readings of the lead's test, empirical); dated notes on LEAD-181,
  CLAIM-662, CLAIM-657, CLAIM-663, QUESTION-279, QUESTION-456; changelog
  fragment record/changelog.d/lead-181.md.

## Choices made

- "Without penalties" has several readings; five regimes run (amnesty,
  none, disc, ext beside pen). The comparison the lead's test depends on
  is filed as alternatives.
- Surfacing reaches requirements whether or not the institution found them
  (internal knowledge does not shield from sigma); an earlier draft let it
  shield, which made 'none' inquire without fixing. Corrected before the
  reported run.

- Lean: CLAIM-tmp0bqyu (varies only the penalty) as what the result
  means; CLAIM-tmpjz94s as the lead's test taken at its word.

## Next

- Report to the lead. Nothing else pending.
