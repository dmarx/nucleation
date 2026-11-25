# LEAD-tmpc0rqa: progress

Branch: claude/recomputation-pass-2026-11-25 (cut from staging at 91e72574).
Worker: a delegated session; the lead commits.

## Task

Rerun, in a session other than the filer's, each entry in the lead's list
(plus CLAIM-tmp6nzs1 and CLAIM-tmpv6tw7), record a dated note of
2026-11-25 on each, promote under the owner's delegation where it
reproduces and every premise is Active (ADR-057), close the leads whose run
is recorded (LEAD-030, 087, 188, 104, 171, 033, 110), write the curation
entry and the changelog fragment.

## Done

Reruns are done from copies in the session scratchpad
(lead-tmpc0rqa/rNNN), with a venv there holding numpy 2.5.3 and scipy
1.18.1 (scipy was missing from the system Python). Nothing written into
the studies' own directories.

- CASE-265: soliton_testbed_checks.py passes; eigenvalues rechecked with numpy. Construction, A's: not promoted.
- CASE-268 / CLAIM-693: maintainer_ladder_check.py passes, gaps 0.1458/0.1458/0.0834/0.0327/0.0104; an independent RK4 (dt 2e-4) gives the same. CLAIM-693 held by its grounds CASE-265, CASE-268 (constructions, Proposed).
- CASE-332: all 1836 cells identical but timings, tables.md byte for byte, 7 tests. Promote.
- CLAIM-646: rebuilt scratch/formal/peak_cumulative_threshold_check.py, passes. Held by CASE-236 (Proposed construction).
- CLAIM-755: rebuilt scratch/formal/scale_separation_arms_check.py, passes. Held by its note of 2026-11-20 (defeater possibly met), not by computation.
- CLAIM-tmp9ia3w: derivation re-read; step 4's "the one maintenance-provenance test" does not follow for A45's fourth test (perturbing the local coupling). Held by CLAIM-364.
- CLAIM-tmp7rl3d: rebuilt scratch/formal/clarification_relief_check.py, passes (3976 consequential cases). Held by CLAIM-tmpm76n5.
- CASE-382: 6 tests pass; the fit not rerun (data must be fetched from OSF, an outside service, held for the owner).
- CASE-362 (lead-087): results.jsonl and summary.txt byte for byte, 6 tests; diagnostics rerunning.
- CASE-410 (lead-188): results.json byte for byte, 8 tests; sensitivity rerunning.

## Next

- Item 1: CASE-265, CASE-268, CLAIM-693, CASE-332, CASE-333, CASE-365, CLAIM-953

## Done (reruns, continued)

- CASE-333: results.jsonl identical to the stored one but `secs` (347 current items), 8 tests; every quoted figure checked. Promote; CLAIM-903 then promotable (its only ground).
- CASE-365 / CLAIM-953: e1-e9 identical but wall times, 11 tests. One figure in CASE-365 wrong: "with the supply kept on it takes 8 to 39" is 8.4 to 105.6 over e4 (106 at sigma 0.01, 56 at 0.02). Hold CASE-365 (correction note); CLAIM-953's own figures match, held by CASE-365.
- CASE-362: results, summary, diagnostics, summary_diag byte for byte; paired contrast 0.021 [0.015, 0.028] recomputed. Promote.
- CASE-410: results.json and sensitivity.jsonl byte for byte; figures match. Testimony half not reread (sources outside). Not promoted.
- CASE-367 (lead-030): 40 runs identical, results.md byte for byte. One statement off: the closure defect is 0.000 [-0.000, 0.002], not negative, in the exposure world's popular+adapt arm. Hold with a note.
- CASE-347 (lead-026): results identical (order differs), summary.txt and calibration.json byte for byte, 11 tests. One statement off: calibration matched "to three decimals in the simulated runs"; B's runs give 0.978, 0.387, 0.895. Hold with a note.
- CLAIM-672: rebuilt scratch/formal/life_form_mechanisms_check.py; all CASE-259/260 figures CLAIM-672 uses reproduce; gliders-away counts for the block-removed guns depend on an unstated criterion. Held by CASE-259, CASE-260 (constructions).
- CLAIM-741: rebuilt scratch/formal/patient_arrangements_check.py, passes. Held by CASE-283 and its own note.
- CLAIM-1114: scratch/formal/critical_path_route_check.py, seed 1114: rule holds on 20000 of 20000; count 1596 (entry 2037, no seed). Promote.
- CASE-225: rebuilt scratch/formal/forced_stuart_landau_check.py, passes (0.03424 against 0.03430). Construction, A's: not promoted.
- CLAIM-1021: lead-015 rerun: e1-e5 identical but seconds, 14 tests. Promote (CLAIM-1000, CASE-401 Active).
- CLAIM-tmp6nzs1: filer's script output byte for byte to the dated output; the review's independent check (on origin/staging only) rerun, matches. Held by CASE-264 (Proposed) as the edge stands.
- CLAIM-tmpv6tw7: filer's script output byte for byte; independent scratch/formal/case189_supply_check.py passes. Promote.

## Done (filing)

- Notes on all 24 items; promotions (history v+1) of CASE-332, CASE-333, CLAIM-903, CASE-362, CLAIM-1114, CLAIM-1021, CLAIM-tmpv6tw7.
- Leads: LEAD-030, LEAD-104, LEAD-171, LEAD-110 Done; LEAD-087, LEAD-188, LEAD-033 narrowed, Open; LEAD-tmpc0rqa blocked_on removed, Open (CASE-382's fit remains).
- Directives naming the seven promoted codes trimmed in 58 files; new excuses on CLAIM-1114, LEAD-tmpc0rqa and the curation entry; ref_status scan: no unused directive.
- Curation record/curation.d/2026/11/25/141302.md; changelog record/changelog.d/recomputation-pass-2026-11-25.md.

## Next (for the lead)

- Commit. CLAIM-tmp6nzs1.md here is origin/staging's version 2 plus this pass's note: on merging staging, take this side.
- After merging staging, trim CASE-362 from SYNTHESIS-tmp4tvbr's directive (staging line 644), which this worktree's older copy does not have.
