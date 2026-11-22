# LEAD-140: CASE-255 on CASE-186's organization

A collective improves its own procedures over generations; an earlier and a
later improver are each applied to the same fresh starting artifact at the
same budget; then the improver's own diagnostic machinery is damaged. Built
on LEAD-048's model (`../lead-048/model.py`), imported and subclassed, not
copied.

- `rsi.py`: the construction, documented in its docstring. The artifact is
  the LEAD-048 organization's procedures (audit interval and size,
  self-check interval, repair time, teacher-correction rate); the improver
  is a hill-climber with settings (candidates per generation, share of
  damage and out-of-family cases in its evaluation suite, whether it reads
  its record, a canary test of its suite) and a record (every move proposed
  and its measured effect). Six lineage arms: `none` (no record read, fixed
  settings), `archive` (fixed settings, reads its growing record), and four
  adaptive arms in which the collective also changes the improver's
  settings, judging a change by `public` (ordinary tasks only), `own` (its
  own current suite), `external` (a fixed outer suite on unseen seeds) or
  `layered` (own, plus an outer veto on any change that weakens
  verification, of the improver or of the artifact).
- `test_rsi.py`: `python3 -I -m pytest -q -p no:cacheprovider test_rsi.py`.
- `study.py`: `python3 -I study.py lineages|transplant|damage|all`. One JSON
  line per item, appended as produced, to `results/<phase>.jsonl`; a rerun
  skips items already written. Two worker processes.
- `analyze.py`: writes `results/tables.md`.

Phases (CPU about 64 minutes in all, on two processes):

1. `lineages`: 6 arms x 12 lineages, 60 generations of 32 episodes, a
   meta-step every 4 generations in the adaptive arms. Each end artifact is
   scored on the frozen held-out battery (24 seeds x 6 kinds: ordinary,
   out-of-family, three undisclosed lesions of the organization's apparatus,
   and an obsolete-instruction reset).
2. `transplant`: per lineage, the starting artifact theta0 improved for 10
   generations by the early improver, the late one, knowledge only (starting
   settings, evolved record) and organization only (evolved settings, empty
   record); the evolved artifact improved by the early and the late one; 2
   replicates on matched seeds.
3. `damage`: per lineage, the late improver applied to the evolved artifact
   for 10 generations with its suite lesioned (generate, admit, score), with
   an obsolete successor, and with the canary removed under generate and
   admit lesions; sham alongside.

The episode schedule is shortened from LEAD-048's 700 steps to 350. An
episode's score is throughput, -(regret + 0.2 x fuel)/350, less 0.3 when
its findings are wrong (S1 and S2 of LEAD-048); without that term, missing
an out-of-family change costs nothing, since regime 0 has no preferred
action.
