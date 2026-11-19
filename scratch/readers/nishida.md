# Reader notes: Nishida et al. 2026, arXiv 2608.13515 (task-agnostic influence across pretraining)

## Copy
- arXiv abs, HTML (v1) and PDF fetched 2026-11-19, all 200, no check. COLM 2026 paper. Read from PDF text (pdftotext), whole paper incl. App. A (Limitations) and B.1-B.5.

## Reading (done)
- Measure: Cont = reduction in squared L2 distance to the run's FINAL params; per-example via SGD decomposition; estimated from Pythia's public checkpoints (Eq. 4). Attribution in an ordinary run, no intervention.
- 18 configs: 6 Pythia-deduped sizes + PolyPythia 160M/410M (seeds 0,1,3; seed 2 omitted) + decoupled 160M data-seed / weight-seed variants.
- "Domains" are NeMo Curator classifier labels (26 semantic topics), NOT Pile components. No Pile-source breakdown anywhere; no mention of Reddit, HackerNews, Ubuntu IRC, StackExchange. "Online Communities" is one of the 26 classes but not discussed in prose.
- App. B.1: the early top-contributor excerpt is classed Hobbies & Leisure and reads as an interview transcript; authors: "the high-contribution example is conversational and closer to natural discourse". One example from a top-10 list.
- No reordering or ablation. App. A: "rather than directly establishing the causal effect of changing the data mixture" ... "require direct intervention-based evaluation".
- Sec. 5.5: supports the late-STEM heuristic "from a trajectory-level perspective"; easy-to-hard curriculum not fully supported (hard texts matter mid-training).
- Doubt: the measure is endpoint-relative; "aligned with the final params early" is not "makes later learning easier".

## Next
- Bearings in the record.

## Bearings searched (done)
- Record holds no LIT for this work (no hit for the arXiv id or the first author).
- CLAIM-756: background at most. No intervention, no cost of a later acquisition measured; "aligned with the endpoint early" is not "lowers the later cost".
- QUESTION-039: bears on it (data-type timing of alignment shifts; size-dependent timing; mid-stage peak), descriptively, from one data order per run.
- THEORY-tmpd6smn (Liu et al.): parallel in direction to late-STEM; tension with "heavy code early helps most". THEORY-tmpk9cmk, THEORY-tmpd6l4a, THEORY-tmp0lbb1: background; Sec. 5.5 itself says easy-to-hard is not fully supported.
- Others: THEORY-2013 (Pythia, its testbed), THEORY-279 (low-order first; parallel), CASE-294 (Pythia checkpoint study; method neighbour), THEORY-tmprqq7k (order within conversation barely matters), CLAIM-758/THEORY-2006 (late-stage rising opponent share; weak parallel only).
- Owner's recollection: NOT this paper's result. Its "conversational" is one excerpt in App. B.1; the domains are classifier topics, no Reddit/forum analysis.
- Quotes verified by script against the downloaded text (whitespace-normalized).
