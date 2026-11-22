# LEAD-182: a powered Contextuality-by-Default test on pragmatic judgements

Scratch for LEAD-182: the literature check, the estimators and the power
simulation behind CASE-tmpl2va4 (the proposed study) and CASE-tmpjp6vg
(the simulation). No data were collected and the study was not run.

| File | What it is |
|---|---|
| PROGRESS.md | the worker's progress log |
| search.md | the literature check: every query, its hits, and the refusals |
| cbd.py | the CbD estimators for a rank-4 cyclic system: Δ_C with fixed or maximised signs, plug-in or soft-thresholded signalling, bootstrap and delta-method bounds, the pooling helper |
| test_cbd.py | 15 tests, including the reproduction of Lo et al.'s 0.192 and 0.176 and the pooling construction of CLAIM-tmpu482h |
| power.py | the simulation grid; writes results.jsonl a cell at a time and resumes |
| results.jsonl | one line a grid cell |
| absence.py, absence.jsonl | size and power of the conservative absence bound (cbd.absence_upper_bound), 4000 replications a cell, no bootstrap |
| summarize.py | turns results.jsonl into summary.md (the absence table is appended from absence.py's output) |
| summary.md | the tables |

## Rerun

From the repository root, CPU only, numpy and scipy (scipy only for pytest's
environment; the code uses numpy):

    python3 -I -m pytest -q scratch/studies/lead-182/test_cbd.py
    rm scratch/studies/lead-182/results.jsonl   # or keep it to resume
    python3 -I scratch/studies/lead-182/power.py          # about 15 minutes
    python3 -I scratch/studies/lead-182/summarize.py > scratch/studies/lead-182/summary.md
    python3 -I scratch/studies/lead-182/absence.py    # its table is appended to summary.md

Seeds are fixed per cell (cell index × 7919 + 12345), so a rerun of the same
grid reproduces results.jsonl exactly on the same numpy version (2.5.3 here).

## What is simulated

Between subjects: a respondent sees one of an item's four contexts and gives
two binary answers. The true models are (a) Lo, Sadrzadeh and Mansfield's
Table 1 with its correlations kept and, optionally, marginal shifts added,
and (b) a symmetric family with every |E_k| equal, an odd sign pattern
(+, +, +, −), and signalling Δ spread equally over the four contents, at a
true Δ_C of −0.3 to 0.3. A base marginal of 0.15 is a robustness check.
