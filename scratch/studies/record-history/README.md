<!-- scratch/studies/record-history/README.md: the first run of LEAD-tmpn6mi2's pilot -->
# The record's history as an event log: first run (2026-11-26)

The pilot the exchange "Alignment consequences brainstorm" proposed (A34,
pilots 1 and 2), filed as LEAD-tmpn6mi2 (the temporal dependency graph) and
LEAD-tmp14mq0 (the stability and generativity view), and started at the
owner's request on 2026-11-26. The code is `scratch/tools/record_history/`;
this directory holds its first run, on `origin/staging` at 95013454.
No change to Luria, `luria.yaml` or any entry: the statistics are a
projection (A33 §12).

## Rerun

From a full clone (`git fetch --unshallow` if shallow), with `fire`,
`loguru`, `omegaconf`, `pyyaml` and `matplotlib`:

    python3 -I scratch/tools/record_history/cli.py run --repo=. --out=OUT --keep_events=True
    python3 -I scratch/tools/record_history/cli.py lead199 --dir=OUT --until=2026-11-22

The first command replays every non-merge commit touching the scheme
directories (about 3,500, four minutes) and writes `events.csv.gz` (about
99,000 events, not committed), `tip.json`, `alias.json`, `profiles.csv` (one
row per entry, not committed: 1 MB), `summary.md` and `phase-CLAIM.png`. The
second writes LEAD-199's three tables, on which `scratch/studies/lead-199/
analyze.py` runs unchanged. `report` re-profiles from a saved event table
without replaying. Tests: `cd scratch/tools && python3 -m pytest -q
record_history/tests` (34).

## What it does

Each touched entry's blob is parsed at each commit and diffed field by
field against the entry's last version, under LEAD-199's normalization
(link markup stripped, codes canonicalized and masked in prose, comments
and the H1 dropped). Event classes are LEAD-tmpn6mi2's: created,
statement, body (outside `## Note of` sections), defeater, note, summary,
role, status, relation added and removed (stated fields only; converse
fields are mechanical), meta, mechanical, deleted. A commit by the bot, or
a sweep (at least 250 entries touched, under 10 % of them created), is
maintenance. Identity runs through renames and `formerly:`; present state
(what is live, what points where) is read from the tip's tree.

## The five checks of LEAD-tmpn6mi2

| check | result |
|---|---|
| 1. Reproduce CASE-307 | **Passes.** In LEAD-199's window, edges: 811 added and 75 removed against 810 and 79 (886 events against 889, 0.3 %). LEAD-199's own `analyze.py` on this extraction: matched-age Mantel-Haenszel ratio 1.49 [1.19, 1.78] against CASE-307's 1.47 [1.22, 1.77]; 858 claims (859), 347 exposed (347), 138 at filing (138); risk-set matching 1.62 (1.62). `lead199/` |
| 2. Classes right (50 events, ≥ 45, no class below 8/10) | **Passes, on the second draw of one class.** Blind reader: revised, status, note and mechanical 10/10 each; relation added 2/10 on the first draw, all eight misses being relations added with the entry's creation (the sheet's fault: the reader was told to call those creations), and 10/10 on a redraw without them. The reader's ambiguities are listed in `handcheck/README.md` and under Limits. |
| 3. Identities resolve | **Passes, with seven exceptions.** Every one of the 11,334 live entries has a `created` event; 7 have two (NOTE-1211 to NOTE-1213, THEORY-1048 to THEORY-1051: deleted in one commit and restored through a merge, which a walk of non-merge commits cannot see). 0.05 % of events name a temporary code (the bar is 1 %). |
| 4. Ten profiles by hand | **Passes.** For 10 claims drawn at random, the blind reader's date of last revision, revision count and inbound count agree with the profile on all 10 (after the fix the reader's count prompted: revisions were counted per event, not per commit). `handcheck/` |
| 5. One command reruns | **Passes**, as above (two commands with the LEAD-199 export). |

Beyond the checks, the replayed present state agrees with the tree on every
live entry and every in-degree (0 mismatches of 11,334; script in the devlog
note's history). The devlog note of 2026-11-26 07:38 records the four wrong
replays found on the way.

## First findings (claims)

These are descriptive, from one run; none is a test of H1.

- **First use comes on the filing day.** Of the 1,207 claims that ever gained
  a dependent, 81 % gained the first on the day they were filed (median
  latency 0 days): CASE-307's filing-day burst, seen on all claims.
- **Most claims are never revised.** 813 of 1,346 (60 %) have no statement,
  body, defeater or role revision after creation; 315 have one.
- **Keeping costs more touches than developing.** Claims received 9,750
  maintenance touches (bot repair, concretization, sweeps, converse fields)
  against 6,011 substantive ones; the median claim, 5 against 3. A first
  measure of U15's cost of persistence.
- **The default quadrants do not discriminate.** Of the 645 claims at least
  14 days old, 590 fall in "established anchor" (a new dependent in 30 days,
  no revision in 14), 31 "dormant", 23 "developing", 1 "churn". On a record
  two months old, growing by hundreds of entries a week, nearly every claim
  gains a dependent within 30 days, so the generativity axis measures the
  record's growth more than the claim's. A34's thresholds therefore do not
  yet separate regimes. LEAD-tmp14mq0 should use rates normalized by the
  record's growth and by age, as its design already asks (age bins,
  generativity as a flow), before H1 (CLAIM-tmpk015q) is tested.

## Limits

- The walk misses changes made only in merge resolutions (the seven double
  creations above; LEAD-tmpn6mi2's caveat). Its extension to first-parent
  merge diffs is the lead's failure branch, not yet needed.
- A retitle that moves the old title into `statement` (the claim-titles
  sweep, e2d3aff8c) is a `statement` event; it is excluded from profiles
  as a sweep, but a smaller retitle of the same form would count as a
  revision. Comparing title and statement together would catch it.
- A sweep that writes the other side of a symmetric relation by hand counts as relation additions, and an edge re-typed from `answers` to `bears_on` (ADR-060) as an addition and a removal (the hand-check's ambiguities).
- Time is author time (the development clock); `promoted_date`, the
  canonical clock, is not yet computed.
- Interaction intensities, per-neighbourhood activity, event entropy and
  status volatility (LEAD-tmpn6mi2's profile, items 6 to 8) are not yet
  computed; this run has counts, windows, latency, reactivation and
  neighbourhood activity summed over one hop.

## Files

- `summary.md`, `phase-CLAIM.png`: the report and the CLAIM plane.
- `lead199/`: `analyze.py`'s output on this extraction (`results_main.json`,
  `analyze_main.txt`); the three tables are regenerated by `lead199`.
- `handcheck/`: the blind sheets' keys and the reader's labels, both rounds,
  and the scoring.
