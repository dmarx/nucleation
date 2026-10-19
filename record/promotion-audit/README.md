<!-- record/promotion-audit/README.md -->
# Promotion audit

The working ledger for [ADR-047](../decisions.d/ADR-047.md): finding entries whose
evidence has outgrown their status, a few at a time, so that any session can
pick up where the last one stopped.

| File | What it holds | Who writes it |
|---|---|---|
| `queue.yaml` | Every triaged candidate with its rubric score and state, the per-wave yield, and the `handoff` block | updated in every batch; bump `version`, append to `history` |
| `decisions/<CODE>.yaml` | One review: disposition, accepted and excluded scope, evidence, blockers, `reviewed_revision`, next action | written once, when the review is reached |
| `batches/batch-NNN.yaml` | What one batch reviewed, its outcomes, its yield, and what it learned | one per batch |
| `NOTES.md` | Working notes: patterns, traps, open threads | append freely |
| `check.py` | Fails if the queue and the decision files disagree | run before every commit |
| `triage.py` | Scores wave-1 candidates by the rubric, from metadata | run on a freshly fetched origin/main when re-triaging |

## Resuming

Read `queue.yaml`'s `handoff`, then `NOTES.md`. If `in_review` names a
candidate, finish that one first. Then follow `next_step`. A continuation
prompt that works on its own:

> Continue the Nucleation promotion audit from record/promotion-audit/queue.yaml.
> Review the next five pending candidates in queue order, write one decision
> file per candidate as each is reached, update the queue and its hand-off,
> run check.py, commit, and stop. Do not change any entry's status without a
> decision file that calls for it.

## A batch, step by step

1. Set `handoff.batch` and mark the first candidate `in_review`. Commit.
2. Review it: read the entry in full and the records it rests on, at most
   two rounds of retrieval. Decide one of `promote`, `narrow-and-promote`,
   `split`, `retain-proposed`, `needs-correction` or `defer`. Every
   disposition but a promotion names a specific blocker.
3. Write `decisions/<CODE>.yaml`, set the candidate to `decided` with its
   disposition, and move `in_review` on. Commit after each decision when a
   session might end.
4. After at most five, write `batches/batch-NNN.yaml`, update the wave
   counts, bump the queue's `version`, rewrite `handoff`, and run
   `python3 check.py`. Commit and stop.

Promotions are separate pull requests of at most three entries. Each cites
the decision file it carries out. A decision is stale once the entry has
changed since its `reviewed_revision`.

## The guard

`python3 -m pytest record/promotion-audit/test_check.py` fires `check.py`
against a consistent ledger and against each kind of drift. It was also
fired once against the real ledger on 2026-10-19 (DP-4): with
`decisions/CLAIM-270.yaml` moved away, it reported "CLAIM-270 is decided in
the queue but has no decision file" and exited 1. With the file restored it
passed.
