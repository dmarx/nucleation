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

## Next

- Measurement script, test, run
- File CLAIM, CASE, notes, changelog

## Choices

- Model: 0/1 attributes closed upward under implication, PMI = X Lam X^T
  (+ affine); Lam > 0. Tree case worked in closed form (complete b-ary).
- Corpus: text8 (first 1e8 chars of English Wikipedia, 17M tokens), small
  enough for CPU.
