# Reader notes: goudar (Goudar et al. 2023, Nat Neurosci, doi:10.1038/s41593-023-01293-9)

## 2026-11-19 copies
- Europe PMC fullTextXML (ADR-101 route) for PMC11559441: HTTP 500 twice (record is an NIH author manuscript, isOpenAccess N).
- PMC article page https://pmc.ncbi.nlm.nih.gov/articles/PMC11559441/ (author manuscript NIHMS2033356): full HTML received, read in full (main text + Methods). Text kept in reader scratchpad, not here.
- Supplementary PDF on PMC: "Preparing to download" JS challenge page -> stopped, not read. Europe PMC supplementaryFiles API: error bean. bioRxiv preprint 10.1101/2021.09.02.455707 exists (Europe PMC PPR390513), not fetched.

## 2026-11-19 reading (main text + Methods, in full)
- Setup: one 100-unit rate RNN, trial-by-trial SGD (Adam, BPTT), 2-stimulus -> 2-response delayed association problems, criterion = mean loss < 0.005 over 50 trials, then a new problem; up to 1,000 problems; 30 seeds for the L2L fit, 10 for most analyses.
- (a) Later cost with/without earlier learning: yes, in trials to criterion. Problem 1 "a few thousand trials", problem 2 "a few hundred", plateau ~20; exp fit time const 47.52 ± 26.22, asymptote 21.33 ± 3.85 (30 nets). Also 2-mapping -> 3-mapping problem vs naive 3-mapping.
- (b) Matched first stage: every problem trained to the same criterion, so first-stage performance is matched by construction; but no comparison of different organizations at matched performance (no memorizer/shortcut arms).
- (c) Intervention: yes, but on the READOUT's access to the schema subspace, after problem 1 only. Output weights rotated off the decision subspace and frozen (D->S): second problem "as slowly as naive networks learning their first problem". Controls: frozen readout, S->S permutation. 50 perturbations x 10 nets. Not an ablation/reinit/transplant of the recurrent representation itself; no intervention at later L2L stages.
- Monkey comparison: no monkey data in paper; "(Peysakhovich et al., unpublished)" plus ref 19 (15-20 trials when well trained). Comparison is qualitative.
- Progressive speedup mechanism (accumulated weight changes suppress needed weight-driven VFC) is analysed, not intervened on.
- Supplement not read (PMC challenge page).

## Bearings searched
- No LIT for the work on main or on claude/read-task-composition. Bearings: LEAD-tmphfbq0 (closest prior design so far for parts a and c, in a toy RNN), CLAIM-756 (corroborates premise in cost terms, earlier cost counted only in the sense that problem 1 is in the series), QUESTION-397/CLAIM-596/TERM-117 (parallel: reuse vs head start), CLAIM-754, CLAIM-758, THEORY-1358 (Kemp schema), THEORY-2034/2046/2053 (meta-learning contrast), THEORY-tmpmy98s (weight-shuffle intervention parallel).
