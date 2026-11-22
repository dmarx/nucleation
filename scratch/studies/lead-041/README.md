# LEAD-041: the procedure, and its application to the FOMC's record

## Files

- `procedure.py`: the procedure, generic over any record of contests
  (QUESTION-268's seven steps, in the ordinal form of CLAIM-434 and
  TERM-077/078, with LEAD-041's additions; see its docstring).
- `test_procedure.py`: twelve synthetic cases. `python3 -I -m pytest -q test_procedure.py`.
- `fetch.py`: downloads the public sources to a directory outside the repository.
- `fomc.py`: builds the record of conduct and runs the procedure under
  3 channel specifications x 2 decision readings x 3 windowings.
- `power.py`: how many contested decisions a window needs, at the record's own noise.
- `summarize.py`: writes `results/summary.md` from `results/*.json`.

## Rerun

    python3 -I fetch.py <dl>
    python3 -I fomc.py <dl> results      # about 3 minutes
    python3 -I power.py > results/power.txt   # about 3 minutes
    python3 -I summarize.py

Seeds are fixed. CPU only.

## Choices (the assistant's; each is the owner's to change)

- **Record.** The FOMC's policy-rate decisions, 1966Q1 to 2026Q3, quarterly:
  the change in the monthly effective federal funds rate (H.15) from the
  last month of one quarter to the last month of the next; hike above
  +0.25, cut below -0.25, else hold. A second reading uses the change in
  the real rate (funds rate less 12-month CPI inflation as known then).
- **Perspectives.** The dual mandate's two channels, each ranking
  {cut, hold, hike} from data known at the time (Philadelphia Fed
  real-time vintages): inflation against pi* (2, or a trailing ten-year
  mean), unemployment against u* (a trailing ten-year mean, or its
  twelve-month change). Band 0.5 points either way; inside it, a channel
  is indifferent. No CBO natural rate: www.cbo.gov returned 403 on
  2026-11-22. CPI vintages begin in 1994Q3; earlier quarters use the
  1994Q3 vintage cut at the information date.
- **Contest** is strict opposition of the two channels' rankings, read
  from the rankings, never from the decisions. A channel that is
  indifferent contests nothing.
- **Candidates** scored for alignment: each channel's ordering, and
  inertia (hold on top).
- **Ambivalence** in a window: the record's misfit to the best candidate
  is larger than every candidate, with the record's own departure profile
  on uncontested quarters, would produce (p < 0.05, largest p over the
  candidates' orderings).
- **Prevails**: the leading candidate's alignment exceeds every rival's
  in at least 95% of bootstrap resamples of the contested quarters.
  Otherwise, with no ambivalence shown, **indeterminate**.
- **Sign** (neutral, positive, negative) only for a prevailing channel:
  its gap closed per year against the mean rate over windows it leads.
- **Windows**: two-year blocks, four-year blocks, and chairs' tenures.

## Obstacles, 2026-11-22 (not retried)

- fred.stlouisfed.org/graph/fredgraph.csv: HTTP/2 stream reset, then an empty reply.
- api.bls.gov v1: "daily threshold for total number of requests ... reached".
- download.bls.gov/pub/time.series/: 403 Access Denied.
- www.cbo.gov/data/budget-economic-data: 403.

## Result

See `results/summary.md`, and the CASE filed for this lead.
