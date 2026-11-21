<!-- scratch/formal/analytics/README.md -->

# Analytics pipeline

Recomputes the record's derived numbers on demand, as an [Apache Hamilton](https://hamilton.apache.org/) dataflow. Each number is a node, a plain Python function whose parameters name the nodes it depends on, so asking for one figure computes only what that figure needs. Every run writes one JSON that names, under `computed_at`, the commit every figure was read from. Snapshot figures are read from that commit through git, never from the working tree.

Not part of the record. luria does not read `scratch/`.

## Running it

Needs `apache-hamilton` (formerly `sf-hamilton`, the same package under its old name), `fire`, `loguru` and `pyyaml`. The history nodes need full git history. Run from the repository root:

    pip install apache-hamilton fire loguru pyyaml
    python3 -I scratch/formal/analytics/cli.py nodes                     # list the nodes and what each feeds
    python3 -I scratch/formal/analytics/cli.py run --outputs=fast --out=analytics.json
    python3 -I scratch/formal/analytics/cli.py run --outputs=all --out=analytics.json
    python3 -I scratch/formal/analytics/cli.py run --outputs=census_coverage,topic_term_count --out=-
    python3 -I scratch/formal/analytics/cli.py run --rev=09950cdf --outputs=fast --out=at-census.json

- `--outputs`: `all` (every figure), `fast` (all but the nodes tagged `cost=slow`), or node names, comma-separated.
- `--rev` (default `HEAD`): the commit the snapshot is read at.
- `--term_changes_rev` (default `--rev`): how far the term-change audit reads. The manuscript used `09950cdf`.
- `--growth_ref` (default `origin/main`, else `main`) and `--growth_dates` (default the manuscript's four dates): the dated snapshots of §12.5.
- `--census_dir` (default `../decision-census/census`): the hand-coded census.

`fast` takes about 25 s on the current record, almost all of it reading every entry's frontmatter. `all` adds the history replays, which take several minutes.

Output: `{"computed_at": {rev, sha, short, date, subject}, "run_at", "inputs", "values": {node: value}}`. `date` is the commit's committer date. The `analytics.json` in this directory is one such run, kept so the figures can be compared with the next one.

Tests: `python3 -m pytest -q scratch/formal/analytics`. `test_pipeline.py` builds a two-commit record in a temporary git repository and checks each group of nodes on it. `test_manuscript_figures.py` checks that the pipeline reproduces the manuscript's figures at the commits it read. It is skipped without full history.

## Files

| File | What it holds |
|---|---|
| `cli.py` | The `fire` CLI, the Hamilton driver, and a hook logging each node's run time |
| `snapshot.py` | Nodes for the record at one revision |
| `census_nodes.py` | Nodes for the decision census, and for its staleness |
| `history.py` | Nodes read from git history |
| `gitread.py` | Reading a revision through git (reuses `record_rates.Blobs` and `record_rates.split`) |
| `conftest.py`, `test_*.py` | The fixture record and the tests |

Reused, not rewritten: `decision-census/census.py` (now with `load_rows`, `summary` and `agreement`, which `main` prints), `decision-census/term_changes.py` (now with `events`, which `main` writes), `schema_rates.py` and `record_rates.py`. The printed and written outputs of the first two are unchanged.

## Nodes, and the manuscript figures they feed

Section numbers are those of `scratch/manuscripts/from-obstruction-to-reorganization/`.

| Node | Value | Feeds |
|---|---|---|
| `repo_file_count`, `record_file_count` | Files in the tree, and under `record/` | §12.5 |
| `scheme_count`, `vocabulary_count`, `topic_term_count`, `luria_yaml_lines` | The grammar's size | §12.5 |
| `vocabulary_term_counts` | Terms per vocabulary | |
| `entry_count`, `entries_by_scheme`, `entries_by_scheme_status` | Entries, by scheme and status | §13.2, §13.3 (totals) |
| `decision_status_counts` | ADRs by status | §14.1 (114: 70 Active, 37 Proposed, ...) |
| `lit_status_counts` | LITs by status | §13.4 (2,114 Active, 531 Unavailable, 179 Unfetched, 58 Deferred) |
| `case_kind_by_standing` | CASE kind × standing | §13.2 table; Appendix A figure 8 |
| `claim_warrant_by_status` | CLAIM warrant × status | §13.3 table |
| `lead_stage_counts` | LEADs by stage | §14.4 "after" column; Appendix A figure 10 |
| `anthology_candidate_count` | Entries carrying `anthology-candidate` | Manuscript README, open item 2 (the count now) |
| `growth_snapshots` | The §12.5 measures at the last first-parent commit on `growth_ref` by each date | §12.5 table, all 24 cells; Appendix A figure 5 |
| `commit_counts` | Commits reachable from `--rev`: all, non-merge, non-merge by the bot | §12.1 |
| `census_summary` | The census tables: regime, component, operation, residue, outcome, decider, ratification, six fields by period, noticer by regime, migrations, later harm | §13.1, §15.1, §15.3, §15.4, §16.1, §16.3; Appendix A figure 6 |
| `census_agreement` | Agreement and Cohen's κ per field, mean Jaccard for lists | §13.1 agreement table, §15.1 |
| `census_coverage` | Decisions held in `record/decisions.d` against those coded: `uncoded_count`, `uncoded`, `last_coded_date` | Staleness of §§13–16 |
| `census_status_drift` | Coded decisions whose status has changed since coding | Staleness of §14.1 |
| `term_change_summary` (slow) | The term-change audit: events by kind, events with an ADR in their unit, terms with carriers none of which were touched, and every event with its carriers | §15.2 (34 events, 25 reworded, 9 removed, 34 of 34 with a decision; the carrier counts 41/41, 42/42, 12/12, 177 of 345, 13 of 50, 1 of 92, 0 of 237), §13.4 (177 of 345), §16.1; Appendix A figure 9 |
| `schema_rates_report` (slow) | `schema_rates.py`'s report, as lines | §12.6, measured again (see below) |
| `record_rates_report` (slow) | `record_rates.py`'s report, as lines | §12.7, measured again (see below) |

Internal nodes (`computed_at`, `tree_files`, `luria_config`, `entries`, `census_rows`, ...) feed the others. `all` does not write them, but they can be named.

**Staleness.** The census is coded by hand and cannot be recomputed for new decisions. `census_coverage.uncoded_count` says how many decisions the census has yet to code, and `census_status_drift` how many coded decisions have changed status since coding. On 21 November these were 13 (ADR-115 to ADR-127) and 34.

### Checked

At `09950cdf` and the four dated commits, the pipeline reproduces the following exactly (`test_manuscript_figures.py`):

- the §12.5 table;
- §14.1's decision statuses;
- §13.4's LIT statuses;
- the §13.2 and §13.3 tables;
- §14.4's after column;
- §13.1's census counts and agreement.

The figures in §§13.1, 15.1 and 15.4 (ratification, deciders, residue, noticers by period) match the census output.

### Not covered

- **§12.6 and §12.7, exactly.** Those figures are CASE-178's and CASE-180's, run on 27 October over windows of 32 days. `schema_rates.py` and `record_rates.py` read the whole history to `HEAD` and print text, so the nodes give the same measures for the history now, as lines, not the dated figures. They also read `HEAD`, not `--rev`; the CLI warns when the two differ. Making them return data and take a revision and a window would let these nodes reproduce the cases.
- **§12.1's 3,454 commits.** `commit_counts.all` at `09950cdf` is 3,451, and how the manuscript counted is not stated.
- **§14.4's before column (190, 4).** Run the snapshot with `--rev` at the commit before ADR-111.
- **§13.7's line splits** (69 of 79, 93 of 102). These come from `line_parts.py`, which takes syntheses as arguments, and are not wired in.
- **§14.1's "26 of 37 coded as applied"**, and the counts of reviews and promotion audits in §14.2 (79 batches, 308 files, 230 stale, 31 sessions, 168 of 240). These are not scripted.
- **Counts read from decisions' prose** (§§13.3–13.9, for example 453 claims, 42 and 17, 395 firings, 277 of 406), §16.4's night (48, 34, about 400 files), and CLAIM-419's 22 items.

## A workflow, if wanted

Nothing here runs in CI. A workflow could run on a schedule or by hand (`workflow_dispatch`), or after the Promote workflow merges into main. It would:

1. check out with `fetch-depth: 0`, since the history nodes need full history;
2. run `pip install apache-hamilton fire loguru pyyaml pytest`;
3. run `python3 -m pytest -q scratch/formal/analytics`;
4. run `python3 -I scratch/formal/analytics/cli.py run --outputs=all --out=scratch/formal/analytics/analytics.json`;
5. commit the JSON if it changed, or upload it as an artifact.

Whether it should commit, and on which branch, is for the owner. Run on staging, the figures would describe a record whose new codes are still temporary; run after Promote, they describe main.
