# LEAD-119 pilot: public postmortems against CSB reports, coded by organizational level

Files:

- `codebook.md`: codes, sampling rule and decision rule, committed before any coding.
- `sample_log.jsonl`: every internal-arm candidate tried, in sampled order, with its result (append-only; a later line for a URL supersedes an earlier one).
- `coded.jsonl`: one coded item per line, append-only (30 internal `P..`, 10 independent `I..`).
- `results.md`: the summary table, produced by `summarize.py`.
- `sample.py`, `append.py`, `summarize.py` and their tests.

Rerun (downloads go to a scratch directory, never the repository):

    python3 -I sample.py <Dan Luu README.md> <download dir> sample_log.jsonl
    python3 -I append.py coded.jsonl <batch.json>
    python3 -I summarize.py coded.jsonl > results.md
    python3 -m pytest -q

The CSB reports were fetched from the PDF links on each investigation's page at
csb.gov and read with `pdftotext`; only the cause statement, the executive
summary's findings and the recommendations' addressees were coded.

## Clarification made during coding

After P10, one rule of the codebook was sharpened and applied to all items
from then on, consistent with the codes P01 to P10 already had: an action item
is coded A = 3 for re-prioritisation only when it shifts resources away from
other work (a freeze, moving engineering functions, a change to the roadmap or
staffing plans, a company-wide investment programme). Saying that repair items
are "prioritised" or "highest priority" is coded 2.

## Limits

One coder (Claude, Opus 5.5), the same model family that wrote CLAIM-750 and
this codebook, knowing the prediction; no second coder, no agreement measure.
Internal postmortems were coded from keyword-located passages of the stripped
page text, not read end to end; CSB reports from their summary sections only.
web.archive.org was unreachable from the session (HTTP 000), and github.com/blog
returned 403 once; both were logged as exclusions and not retried.
