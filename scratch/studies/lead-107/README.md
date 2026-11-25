# LEAD-107: restatement distance and re-derivation in the workbench reconstructions

Advances CLAIM-180, CLAIM-182 and CLAIM-191 (bears on QUESTION-038). Codes
the restatement events that the record's reconstructions of exchanges
report, by rule, and runs the three comparisons the lead names: re-derivation
of coded against uncoded items; re-derivation of the same item before and
after it got a code; and a restatement's lexical distance from its coded
original against whether it was re-derived as new.

## Rerun

    python3 -I scratch/studies/lead-107/restatement.py --root . \
        --out scratch/studies/lead-107/results_v1.json \
        --events scratch/studies/lead-107/events_v1.jsonl
    python3 -I scratch/studies/lead-107/restatement.py --root . --rules v2 \
        --out scratch/studies/lead-107/results_v2.json \
        --events scratch/studies/lead-107/events_v2.jsonl
    python3 -I -m pytest -q -p no:cacheprovider scratch/studies/lead-107/test_restatement.py

CPU only, no network, about a second. Reads `record/workbench.d/` and the
entries it cites; writes only the four result files.

## Files

- `CODEBOOK.md`: the rules, fixed before the comparisons, and the v2
  deviation written after the first run.
- `restatement.py`, `test_restatement.py`: the coder and its tests.
- `results_v1.json`, `results_v2.json`: tallies, before/after rows, distance
  rows. `events_v*.jsonl`: one coded sentence per line (text cut to 160
  characters), for audit.
- `AUDIT.md`: the coder's check of its own rules on random samples.
- `PROGRESS.md`: the run's progress log.

## Results (rules v2; v1 in brackets where it differs)

- Corpus: 48 reconstructions of exchanges, 2026-10-04 to 2026-11-06.
- 265 [292] restatement sentences: 76 [85] re-derived as new, 1 [5]
  retrieved by citation, 2 conflicting, 186 [200] neutral.
- (reconstruction, item) units: coded items 159 new, 1 retrieved, 6
  conflict, 137 neutral; uncoded items 44 new, 0 retrieved, 130 neutral.
  P(new | new or retrieved) is 0.99 coded and 1.0 uncoded; the comparison is
  degenerate because retrieval is almost never reported.
- Coded content re-derived as new: 159 units in 20 of the 48
  reconstructions.
- Before/after: 21 items were re-derived before they had a code; 12 of them
  were followed by 9 or more later reconstructions; 4 of the 21 (TERM-072,
  CLAIM-414, QUESTION-271, CASE-156) are reported re-derived again after
  the code existed, and none is reported cited.
- Distance: 16 events quote the restatement and name one code; 3 are `new`,
  0 `retrieved`, so the test cannot be run.
