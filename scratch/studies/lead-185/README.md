<!-- scratch/studies/lead-185/README.md: the materials of LEAD-185's study -->
# LEAD-185: contested and accepted open-source successions, timed

The study filed as the executed-study CASE that carries out LEAD-185
(2026-11-23), on CASE-223's design.

- `CODING.md`: the sampling frame, the arms, the event kinds and case codes,
  the measures, and the changes made to the rules after coding began.
- `cases.csv`: one row per case (11), with the arm, whether the
  maintainers moved (and the source), the outcome by 2026-11-23 and whether
  the recognized continuation carries the original name.
- `events.csv`: one row per dated event (51), each with its source URL,
  whether the source was fetched and read on 2026-11-23, and for responses
  the act (statement, or statement with a move), the independence of the
  speaker from the founders, and the stated reason.
- `timings.py`: computes the lags and counts; writes `results.json` and
  `summary.md`. Rerun: `python3 -I timings.py`.
- `test_timings.py`: 14 tests, on the functions and on the coded data's
  vocabularies. Run: `python3 -m pytest -q test_timings.py`.

No downloaded text is committed. Pages were read on 2026-11-23 through the
session's proxy; obstacles met are listed in PROGRESS.md.
