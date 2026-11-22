# LEAD-030 progress

- Lead: LEAD-030, "Run the laboratory of genres, which separates classes
  inferred, classes used and classes that reshape preferences".
- Branch: `claude/lead-030-genres-laboratory`, cut from origin/staging (15c07a12f).
- Task: build CASE-296's simulated bipartite engagement laboratory as a small
  numpy simulation (arms: classes inferred and never used; classes steering
  recommendation with fixed preferences; classes steering recommendation
  while users adapt; negative control where popularity and exposure alone
  cluster), measure predictive adequacy, stability, closure defect, and the
  intervention arm (randomized cross-class exposure), and test whether the
  laboratory separates the three kinds of class. File a CASE (executed-study)
  and claims as warranted; dated notes on LEAD-030, CASE-296, QUESTION-028,
  CLAIM-762.

## Done

- Step 1: checked the record. No executed study cites CASE-296 or LEAD-030;
  the target is not held.

- Step 2: lab.py (simulation, inference, measures), test_lab.py (10 tests
  pass), run.py (appends one JSON line per run to results.jsonl, skips
  runs already written). Tuning (one-off, seeds 1-2): s_between 0.45 gave
  inference ARI about 0.27 against the planted genres; 0.60 with 5 burn-in
  periods gives about 0.5. Item-level factor model: ridge 2, rank 8 (ridge
  10 or more shrinks to the degree model; 0.3 overfits).
- Step 3 (running): 2 worlds x 5 arms x seeds 0-3, two processes.

## Next

- Summarise results (summarise.py -> results.md), then file CASE, CLAIM(s),
  notes and changelog.

## Choices

- Two worlds: "taste" (planted genres in preferences, popularity-weighted
  exposure) and "exposure" (no taste clusters; exposure channelled through
  6 communities): the second is CASE-296's negative control.
- Five arms: inferred; inferred+adapt (adaptation without use of the
  classes, the control the lead's "only when used" needs); used; used+adapt;
  popular+adapt (where erasure is expected).
- Classes inferred once, from burn-in raw engagement counts, by
  degree-normalized spectral co-clustering with K = 6 (the planted number;
  choosing K is not what is tested), and held fixed while used (CASE-296's
  intervention arm holds the classification fixed).
- Adaptation: users move 10% per period toward the mean of the items they
  engaged with; creators replace the 3% least-engaged items with variants
  of engaged ones, labelled with the parent's class.
- Measures: observational concentration (share of engagements in the
  user's target class); probe gap (in-class minus out-of-class engagement
  rate under uniform random exposure: the intervention arm); conditional
  closure score (share of the item-level model's held-out log-likelihood
  gain over the degree model that the class model keeps), tested on the
  random probe and on a fresh draw of the policy; unconditional Poisson
  gain of the block model on raw counts; stability (ARI of classes
  re-inferred at the end against the start); ground truth (between-class
  share of variance of true preference vectors; true in-class gap).
- "Cost of the task" is read as the closure defect (held-out nats lost by
  predicting from classes rather than items) and the engagement yield; no
  separate cost was modelled.
