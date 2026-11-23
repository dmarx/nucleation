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

## Next

- File: executed-study CASE, CLAIMs (relabelling symmetry; jurisdictional
  audit moves the trade-off; compromise relocates the single point of
  failure to the thinnest jurisdiction; adaptive arm as alternatives A/B),
  dated notes on LEAD-180, CASE-108, QUESTION-090/087/089, CLAIM-359/342,
  changelog fragment.

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
