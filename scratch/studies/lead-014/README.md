# LEAD-014 pilot: curation completeness on four replayed filings

A pilot of the study CASE-251 proposes, run 2026-11-22. Order of work,
with the commit that fixed each step:

1. `01-selection-rule.md`: the rule, written before any candidate was
   opened, and its application (from commit metadata only, by `cands.py`).
2. `02-codebook.md`: units, matching rules and measures, fixed before any
   replay.
3. `accountings/S1.md` … `S4.md`: one replay accounting per filing, from a
   git worktree at the filing's parent commit and the arXiv source,
   following the `read-and-file` skill's steps 2, 9a and 10. Committed in
   b07a1699b before any filing or correction was opened.
4. `scores/S1.md` … `S4.md`: item-by-item scoring against the filing (F)
   and its later corrections (K).

## Departures from the brief and from CASE-251

- **Self-replay, not separate agents.** The Agent tool was not available
  to the worker that ran the pilot, so each replay was done by that worker
  itself, in turn, before it opened the filing. The replayer and the
  scorer are therefore one instance, which saw the four correction commit
  subjects while selecting. Three replay items are marked contaminated and
  excluded (S1 W2 and W5; S3 W30). The replay briefs are reproducible from
  the accountings' headers if the arm is rerun with separate agents.
- **Single works only.** No exchange, synthesis or upload is held in the
  repository (exchange filings cite share links), so all four are arXiv
  readings, not the exchange episodes CASE-251 names.
- **The skill postdates the filings.** None of the parent commits holds the
  `read-and-file` skill or ADR-068; the replay used the current skill's
  accounting step against the record as it stood. So the replay arm is
  "with the skill", the original filings were made without it.
- **Partial reading.** For budget, S1 (an 18,000-word survey) was read
  by section, and S4's appendices were not read beyond their headings.

## Results

| | F recall | K recall | genuine extras | noise or error | contaminated |
|---|---|---|---|---|---|
| S1 symmetry survey | 23/33 = 0.70 | 0/2 | ~9 (3 substantive) | 1 weak | 2 |
| S2 Mehta and Schwab | 22/32 = 0.69 | 0/2 | 0 | 1 | 0 |
| S3 Wang et al. | 30/40 = 0.75 | 0/1 | 2 (1 substantive) | 0 | 1 |
| S4 Lubana et al. | 20/33 = 0.61 | 0/1 | 3 (1 substantive) | 1 error | 0 |
| **pooled** | **95/138 = 0.69** | **0/6** | | | |

By type, pooled: W 30/39, C 36/57, G 17/22, R 12/20. Duplicates 0,
misattributions 0.

What the replays missed of F was mostly what the filer added from its own
work on the source: derivations (S2's ΔF = log Z − log Z_λ, S3's
recomputed measures), open questions, appendix results (S4), later works
that cite the source (S3, S4), and no-bearing judgements.

**None of the six correction items was recovered.** Five needed a work
other than the source: Lin, Tegmark and Rolnick's appendix and the
authors' comment (S2), the journal follow-up's appendix (S3), Neural
Mechanics and Ziyin et al. (S1). The sixth (S4: App. F.3 proves the
converse of the conjecture) is in the source's appendix, which the replay
did not read. So in this sample the record's later corrections of
single-work readings are corrections of accuracy that reading further
found, not omissions of what the source contains; a source-only accounting
cannot be scored against them.

**The replays found things neither the filing nor its corrections hold.**
The substantive ones: S3, the paper's reason why the bus sense of "coach"
is rare runs the wrong way (it is the British sense), still repeated in
NOTE-645; S4, the abstract and §6 state as demonstrated what §5 calls a
conjecture; S1, the bearing of gradient-flow conservation on CLAIM-093
(conservation from symmetry is not Noether's theorem). The ground truth is
a lower bound, as CASE-251 and CLAIM-266 say.

## What this pilot cannot show

- The replayer, the scorer and the original filers are one model family
  (Claude), and here one instance replayed and scored. Agreement and
  disagreement both may reflect shared habits; this is not an independent
  test.
- Scoring was not blind, and the matching judgements are one scorer's.
- Four filings, all single arXiv works, chosen by a rule that required a
  correction naming the entry; not a sample of the record's filings.
- K is tiny (six items) and of one kind (accuracy), so the pilot says
  nothing about the omissions CASE-251 was designed to count.

## To rerun

The worktrees were made with `git worktree add --detach <path> <parent>`
for 4fa4bfaa9, 4da41298e, a90aa7964 and d2aadd3e0; the sources are
arXiv 2506.13018, 1410.3831, 2107.14589 and 2211.08422 (`pdftotext`).
`python3 -I cands.py <repo> <log>` lists candidates, where `<log>` is
`git log origin/staging --format='@@%h|%ad|%s' --date=short --name-status
--no-renames -- record/notes.d record/theory.d record/curation.d`. A
proper run gives each replay to a separate agent that sees only its
worktree, the source and the skill's accounting step, and gives the
scoring to an annotator who is not the replayer.
