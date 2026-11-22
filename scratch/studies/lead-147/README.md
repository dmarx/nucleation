# LEAD-147: PMI spectrum under implication, and PMI additivity in text8

## Derivation (CLAIM filed with this study)

- `tree_pmi.py` builds the model: 0/1 attributes closed upward under an
  implication order, with PMI = X diag(λ) Xᵀ. It gives the closed-form
  spectrum for a balanced b-ary tree and checks the readouts.
  `python3 -I tree_pmi.py` prints `derivation_check.txt`.
- `test_tree_pmi.py` tests the closed form, exact full-rank readout for
  random implication DAGs, and the truncation statement, including the
  readout value below the cut. Run it with `python3 -m pytest -q`.

## Measurement (CASE filed with this study)

Data, fetched 2026-11-22 to the session scratchpad and not committed:

- text8: the first 10⁸ characters of an English Wikipedia dump, about 17M
  tokens, from https://mattmahoney.net/dc/text8.zip.
- WordNet 3.0, as NLTK packages it, from
  https://raw.githubusercontent.com/nltk/nltk_data/gh-pages/packages/corpora/wordnet.zip
  (Princeton WordNet licence). `nltk.download()` refused to fetch through
  the session proxy, as an NLTK safety check, so the same file was fetched
  with curl.
- The word2vec analogy set `questions-words.txt` (Apache 2.0), from
  https://raw.githubusercontent.com/tmikolov/word2vec/master/questions-words.txt.

Run:

    python3 -I measure.py TEXT8 NLTK_DATA_DIR QUESTIONS_WORDS CACHE_DIR

Counts are cached in CACHE_DIR. Results are appended item by item to
`results/analogy.jsonl` (one line per analogy family) and
`results/hierarchy.jsonl` (summary, one line per nested-depth fit, and one
line per rank and attribute). A rerun skips the keys already written.
`test_measure.py` tests the counting, the 2 × 2 decomposition and the
cross-validated fit.

Choices:

- Targets are the 10 000 most frequent words. Contexts are the 5 000 most
  frequent, in a symmetric window of ±5.
- The PMI is shrunk: log((n + 1)/(E + 1)), with E the count expected under
  independence. It is finite at zero counts.
- The two half-corpora give split-half reliability and the noise in each
  analogy interaction.
- Hierarchy: a noun is a target whose first WordNet synset is a noun synset
  named by the word. Its attributes are all hypernym and instance-hypernym
  ancestors held by between 5 nouns and half of them. PMI rows are
  double-centred, which removes each word's own affine term. The
  additive model is ridge (α = 1), scored by 5-fold held-out-word R². It is
  compared with the same attributes assigned to permuted words, and fitted
  nested by attribute depth (WordNet min_depth).
- Probes: on rank 10, 30, 100 and 300 SVD embeddings of the noun rows, a
  class-balanced least-squares readout, 5-fold. Each probe records its
  balanced accuracy and the share of its false positives that fall inside
  the attribute's nearest attribute ancestor ("parent"), against that
  parent's share of all negatives.
- Analogy: for each quadruple a:b :: c:d, the 2 × 2 decomposition over
  contexts gives the relation effect, the pair effect and the interaction
  (P_a − P_b − P_c + P_d)/2. The interaction is noise-corrected from the
  half-corpora. Completion is 3CosAdd on a rank-300 SVD embedding of the
  target rows, searched over all 10 000 targets.
