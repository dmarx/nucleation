# LEAD-047: literature search for a manipulation of defensive authority with threat belief held fixed

Run on 2026-11-22.

## Criteria (from LEAD-047 and CLAIM-446's test)

A study qualifies if it has all four:

- **C1** an objectively specified threat (a conditioning or avoidance task,
  or an experimenter-set threat probability);
- **C2** an intervention on the defensive process's authority (its
  influence over action, attention or evidence acquisition) or on its
  evidence access;
- **C3** the represented threat probability held fixed (by design, or by
  measurement showing it equal across arms);
- **C4** exploration, approach or later avoidance as an outcome.

## Files

- `search.py`: the queries (Europe PMC REST search with abstracts; Semantic
  Scholar's Graph API, which answered HTTP 429 on its first query and was
  not retried). No email address is sent. `python3 -I search.py` runs all;
  `python3 -I search.py LABEL ...` reruns the named Europe PMC queries and
  merges them into the existing results.
- `screen.py`, `test_screen.py`: keyword flags for C1 to C4 over titles and
  abstracts, used only to rank (`python3 -m pytest -q test_screen.py`).
- `results/hits.jsonl`, `results/counts.tsv`, `results/prescreen.tsv`,
  `results/run*.log`: the retrieved records, the hit count per query, the
  ranked pre-screen and the run logs. `counts_run1.tsv` is the first run.
- `screening.tsv`: the hand coding of every work with all four flags, the
  three-flag works that named a nearest design, and three works found
  outside the queries.

## Counts

Europe PMC hit counts (all retrieved): Q1 instructed 142, Q2 approach-avoidance
conflict with an intervention 20, Q3 costly avoidance 39, Q4 response
prevention 31, Q5 dissociation 230, Q7 defusion or acceptance 61, Q9
instruction with expectancy unchanged 170. Q6 safety behaviour returned 43 on
the first run and HTTP 503 on the two later runs, so its hits are not in the
final `hits.jsonl`; Q8 (drug or lesion in an approach-avoidance conflict
task) returned HTTP 503 each time. Semantic Scholar: HTTP 429 on the first
query, stopped.

467 unique works after deduplication. Pre-screen flags: 26 with all four,
52 with three, 118 with two, 149 with one, 122 with none. All 26 four-flag
works and the relevant three-flag works were screened by hand at abstract
level (`screening.tsv`); two were read in full.

## Result

No study in the screened set meets all four criteria. The nearest designs
fall short in one of three ways: belief is measured and found unchanged but
not held fixed, and the behavioural effect is unreliable (Sridhar et al.
2026); objective threat is fixed and the arbitration is manipulated
(ketamine, lorazepam, lesions), but the represented threat is not measured
(Vestring et al. 2026; Korn et al. 2017, registered and not read, uses the same task); or the cost or availability of
avoidance is manipulated and moves belief with it (Rattel et al. 2017;
Wong et al. 2022; Pittig & Wong 2021).
