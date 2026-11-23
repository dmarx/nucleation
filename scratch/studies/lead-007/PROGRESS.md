# LEAD-007 progress

- Lead: LEAD-007 (read Lippl and Lindsey on regimes of feature reuse)
- Branch: claude/lead-007-lippl-lindsey (cut from origin/staging)
- Task: register and read Lippl and Lindsey 2024 (arXiv 2310.02396); file a
  NOTE and a THEORY; check whether its regimes already show the same present
  capability with different later learning, outside the special
  initialization Anguita and colleagues generalize (against CLAIM-754);
  file the verdict as Proposed CLAIMs, an objection, alternatives; dated
  notes; changelog fragment.

## Done

- Checked the record: no LIT for arXiv 2310.02396 or Lippl as first author.
- arXiv API answered "Rate exceeded" (not retried); identifiers checked on
  the abstract page. Read the arXiv HTML of v4 (main text, App. A.1, A.2,
  B-F; proofs A.3, A.4 skipped).
- Filed LIT-tmpkuq67 (Active, v2), NOTE-tmpw2i45 (Read), THEORY-tmpw69kb
  (shallow theory), THEORY-tmpfysqg (deep-network results).
- Study (this directory): diagonal-network check that a function-preserving
  rescaling changes full fine-tuning and not readout-only training, and
  that the best c reverses between a nested and a dense main task. 40
  seeds; step-size check. CASE-tmpjn7jc, CLAIM-tmp7n00e.
- Verdict: CLAIM-tmp2tjpt (two learners, the lean), objection and
  alternative CLAIM-tmpew899 (one learner, two procedures; rests on
  CLAIM-tmp2k67n), ARG-tmpbvq7y (existence, concludes CLAIM-754).
- Dated notes: CLAIM-754, CLAIM-675, THEORY-2077 (+ extends), LIT-2861
  (+ extends), CLAIM-tmp2k67n, CLAIM-758, CLAIM-756, CASE-294, LEAD-007.
- Changelog fragment record/changelog.d/lead-007.md.

## Choices

- "Outside the special initialization" read as: does the precursor's own
  setup, without Anguita's relative scale at initialization, show it.
- The paper never compares function-equivalent networks; the equivalence
  is the filer's inference from its stated symmetry, checked numerically.
- Readings filed as alternatives; the lean (two learners) stated.

## Next

- Nothing; report.
