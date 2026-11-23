# LEAD-180 progress

- Lead: LEAD-180 (run CASE-108: four governance architectures over
  cooperative, honestly dissenting and adversarial specialists, with an
  oracle and a compromised-evaluator variant).
- Branch: claude/lead-180-robust-governance (cut from origin/staging).
- Task: simulate CASE-108's four architectures (unrestricted,
  reliability-weighted, role-limited, adaptive) in a small numpy
  federated-aggregation model; score attack success, lost legitimate
  capability, suppressed honest minority, cost of safeguards, repair after
  failure; run a compromised-evaluator variant and an oracle comparison;
  file an executed-study CASE, Proposed CLAIMs, dated notes, a changelog
  fragment.

## Done

- Step 1 check: no executed study of CASE-108 on staging (grep of
  record/, changelog.d, scratch/studies). Not held.
- model.py, test_model.py (19 pass), run.py; e1..e5 run (about 4 min);
  results/*.json and results/tables.md committed.

- Filed: CASE-tmpqnoj1 (executed study); CLAIM-tmpxoxys (relabelling,
  demonstrated); CLAIM-tmp26exz (jurisdictional audit, empirical);
  CLAIM-tmpd6gon (compromised evaluators, empirical); CLAIM-tmpf0b31
  (adaptive arm, reading a, lean) and CLAIM-tmp3t5y3 (reading b,
  supposed, objects_to a). Dated notes on LEAD-180, CASE-108,
  QUESTION-090/087/089, CLAIM-359/342 (versions bumped with history).
  Changelog fragment record/changelog.d/lead-180.md.

## Next

- Report. Nothing else outstanding; the owner chooses between the two
  readings and marks the lead.

## Choices

- Not reused: lead-090's model (CASE-363) has two specialists and a
  meaning–influence loop, no attack class or evaluator; lead-190's grant
  model (unmerged branch) is about grant schemes over the same loop. CASE-108
  names federated learning as its testbed, so a new aggregation model was
  written.
- Honest dissent is modelled as a minority with data on a block the
  majority lacks and misjudges (pulls to 0); the mimic attack targets that
  block, so attack and dissent look alike there.
- "Compromise the evaluators" is the same attacker budget across arms: 2 of
  the 7 evaluators (rel-val, role, adaptive); rel-agree and unrestricted
  have no evaluator separate from the proposals, so the variant cannot
  touch them. The monitor's compromise is a separate factor (e4).
- Warrant: the relabelling result is demonstrated (symmetry, checked
  exactly in tests with noise off); the seed-averaged results are empirical.
