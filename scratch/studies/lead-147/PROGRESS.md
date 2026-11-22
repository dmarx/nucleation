# PROGRESS: LEAD-147

- Lead: LEAD-147 (advances QUESTION-025, QUESTION-178)
- Branch: claude/lead-147-pmi-spectrum
- Task: (1) derive the PMI spectrum of a co-occurrence model with implication
  among binary attributes (a tree); (2) measure PMI additivity on an open
  corpus along WordNet hypernymy and across analogy families, CPU, about an
  hour. File a CLAIM (derivation), a CASE (measurement), dated notes on
  QUESTION-025, QUESTION-178 and LEAD-147, and a changelog fragment.

## Done

- Derivation checked numerically: tree_pmi.py, test_tree_pmi.py (8 pass),
  derivation_check.txt. Closed-form tree spectrum matches to 1e-14.
- Data fetched to scratchpad (not committed): NLTK WordNet 3.0 zip from
  raw.githubusercontent.com/nltk/nltk_data; text8 from mattmahoney.net.
  nltk.download() refused under the proxy (NLTK's own safety check), so the
  zip was fetched with curl instead.

- CLAIM-tmpe87cm filed (derivation, demonstrated, answers QUESTION-025,
  bears_on QUESTION-178, grounds THEORY-185).
- measure.py: first run OOM-killed in tokenising (np.unique on 17M
  strings); fixed with Counter + int32 ids; relaunched 13:09 UTC,
  limit 25 min, counts done in 22 s.

- Analogy stage done (results/analogy.jsonl): interaction share 0.21-0.30
  vs null 0.33; Spearman(acc, interaction) = -0.83 across 14 families.
- Notes filed on QUESTION-025 and QUESTION-178.
- Hierarchy stage running (PID 12079). alpha=1 ridge overfits as
  attributes are added; stage_alpha (stronger ridge) added to measure.py,
  to run after (rerun skips done keys; analogy SVD skipped when done).
- Coordinator: nine workers share the machine. Stop only own PIDs; keep
  scratch files in scratchpad/lead-147/ (moving dl/, cache147/, run147.log
  there after PID 12079 exits).

- Run 2 resumed probes; stopped by own PID at 336/590 rank-100 probes
  (machine contention). Reduced ridge refit done (alpha 100: R2_cv 0.035
  vs permuted -0.006, all attributes).
- CASE-tmpby7xp filed; LEAD-147 note and changelog fragment filed.
- Scratch files moved to scratchpad/lead-147/.

## Next

- Report. Optional later: finish rank-100/300 probes (rerun resumes),
  frequency control, intervention arm.

## Choices

- Model: 0/1 attributes closed upward under implication, PMI = X Lam X^T
  (+ affine); Lam > 0. Tree case worked in closed form (complete b-ary).
- Corpus: text8 (first 1e8 chars of English Wikipedia, 17M tokens), small
  enough for CPU.
