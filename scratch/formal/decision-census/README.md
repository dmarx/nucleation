<!-- scratch/formal/decision-census/README.md -->

# Decision census and term-change audit

The data and scripts for the executed-study CASE filed on 2026-11-20 ("Who changes the record's grammar, how, and with what result"). Not part of the record; luria does not read `scratch/`.

- `census/CODEBOOK.md`: the codebook, fixed before coding.
- `census/batch-1.json` … `batch-4.json`: ADR-001 to ADR-114, coded.
- `census/recode.json`: the second coder's random 30 (seed 20261120).
- `census.py`: tables and agreement. Run: `cd scratch/formal/decision-census && python3 -I census.py census`. Output in `census_report.md`.
- `term_changes.py`: every reworded or removed vocabulary term, with carrying entries touched in the same unit. Needs full git history and `scratch/formal/schema_rates.py`. Run from the repository root: `python3 -I scratch/formal/decision-census/term_changes.py . 09950cdf`. Output in `term_changes.json`.
- Tests: `cd scratch/formal/decision-census && python3 -m pytest -q`.
