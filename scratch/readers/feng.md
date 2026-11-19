# Reader notes: feng (arXiv 2412.15285)

## Copy
- 2026-11-19: arXiv PDF https://arxiv.org/pdf/2412.15285 (v1, 18 Dec 2024), 16 pp, fetched without challenge; text extracted to the reader's scratchpad (not committed).
- Title from text: "Maximize Your Data's Potential: Enhancing LLM Accuracy with Two-Phase Pretraining". Authors: Steven Y. Feng*, Shrimai Prabhumoye*, Kezhi Kong, Dan Su, Mostofa Patwary, Mohammad Shoeybi, Bryan Catanzaro (NVIDIA, Stanford, Boston U.).

## Read
- Full body (sec. 1-7, Limitations, Ethics) read; appendices A-E read for setup, tables skimmed.
- Setup: 8B Megatron model, 1T tokens on data downsampled by f = 1/15 (so epochs match a 15T run on full data). Scale-ups: 8B at 1.7T (downsampled), 25B at 1T, 8B at 15T full data.
- Order comparison at fixed tokens and fixed blend weights: BASE-RO (same weights, random order) vs two-phase. Table 4: Avg 51.12 vs 52.86 ("3.4%" is relative). BASE-ND 45.17.
- The two-phase row in Table 4 equals the P2 = 40% row of Table 14, i.e. the best of six P2 durations picked on the same downstream evals. One run per config; no seeds reported.
- LR: P1 cosine targeted to end of full run; P2 starts from the intermediate LR and re-anneals with cosine to 3e-6 (App. A). BASE-RO's schedule not stated -> phase is confounded with an end-of-run anneal on high-quality data.
- Doubt: Table 14's P2 = 0% row (Avg 37.68) is the mean of the four category scores, unlike the other rows (per-task mean), and shares MMLU/GSM8K/Code values with the "P1-only" row of Table 28 (900B model, different code metric). Not comparable; the proper P1-only comparison is Table 7 (P1-Blend4 alone 48.40 vs 52.28).
- No result stated as a saving in data or compute; no exchange rate between phases. The second phase reuses the same data pool (more epochs of high-quality data), so it is an allocation-and-order result, not a cost-of-later-learning result.

## Bearings searched (2026-11-19)
- No LIT for 2412.15285 on record; only LEAD-tmpjdtrl lists it ("Feng and colleagues on two-phase pretraining"), accurately.
- Caution: CLAIM-756's note of 2026-11-19 says "Feng and colleagues" meaning Feng, Goodman and Frank (THEORY-tmprqq7k, child-directed speech). Same first author, different work; the filer should disambiguate.
- CLAIM-756: background at most. No cost-to-threshold, no saving in data or compute, phase-1 cost never separated; the comparison is order of one fixed pool at fixed tokens, measured by final accuracy.
- QUESTION-039: parallel/background (order matters for final accuracy, P2 timing 40% best), not about when structure is acquired.
- THEORY-tmpd6l4a (Chen): qualifies its "sequential no better than random" in a different sense: here phased-by-quality beats random order by 1.74 points (one run each).
- THEORY-tmpd6smn (Liu): contrast; here high-quality/code concentrated late helps, there heavy code late hurt fine-tuning. Different targets (final evals vs post-fine-tuning loss).
- THEORY-tmp0lbb1 (Bengio): parallel (general then target-like at fixed budget), but no ease ordering.
- THEORY-tmpk9cmk (Hu): contrast in kind: Hu counts cost to threshold; Feng does not.
- THEORY-tmplutfz: parallel (domain-relevant data last helps).
- THEORY-2006, CLAIM-758: weak parallel: P2 over 40% degrades, authors suggest overfitting.
- CLAIM-596: methodological parallel: final scores cannot separate head start from lowered later cost.
- All 28 quotes checked by script against the extracted text.
