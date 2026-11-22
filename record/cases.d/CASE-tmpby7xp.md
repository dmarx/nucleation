---
status: Proposed
title: 'Measuring PMI additivity in text8 along WordNet hypernymy and across analogy families'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-147: the
    measurement limb of QUESTION-025 and the measurement QUESTION-178 asks
    for. Scripts, tests and per-item results are under
    scratch/studies/lead-147/.
standing: documented
kind: executed-study
tags:
- representation-learning
- linguistics
date: '2026-11-22'
line:
- pragmatic-transport
bears_on:
- QUESTION-025
- QUESTION-178
illustrates:
- CLAIM-tmpe87cm
summary: >-
  Co-occurrence was counted in text8, about 17M tokens of English
  Wikipedia: 10 000 target words against 5 000 context words, in a window
  of ±5. The PMI was shrunk so that it stays finite at zero counts. Analogy
  families: in each word2vec quadruple, the PMI interaction
  P_a − P_b − P_c + P_d holds a noise-corrected median share of 0.21 to
  0.30 of the quadruple's variation, against 0.33 for random quadruples.
  No family is near additive. But families with less interaction complete
  more often in a rank-300 embedding (Spearman −0.83 over 14 families),
  and within 13 of 14 families the least-interacting third of quadruples
  completes more often than the most-interacting third (0.59 against
  0.31). Hierarchy: 4 315 nouns with 590 WordNet ancestor attributes. A
  held-out-word additive fit explains at most about 2% of the
  double-centred PMI variance (split-half reliability 0.58). It beats the
  same attributes on permuted words at every depth. Linear probes on
  low-rank embeddings reach balanced accuracy of about 0.70–0.80, with no
  fall by WordNet depth. Their false positives fall inside the attribute's
  parent about twice as often as chance. No language-model annotation
  was used. The wording is the assistant's (Claude, in this session);
  adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-tmpe87cm — new, filed today with this case -->

# CASE-tmpby7xp: Measuring PMI additivity in text8 along WordNet hypernymy and across analogy families

## What was done

Data (fetched 2026-11-22, not committed):

- text8, the first 10⁸ characters of an English Wikipedia dump;
- WordNet 3.0 as NLTK packages it;
- the word2vec analogy set.

The sources and every choice are in scratch/studies/lead-147/README.md.
The counts use a symmetric window of ±5. The targets are the 10 000 most
frequent words and the contexts the 5 000 most frequent. The PMI is
log((n + 1)/(E + 1)), where E is the count expected under independence.
The two halves of the corpus were counted separately, to measure noise.

**Analogy families (QUESTION-178).** Each quadruple a:b :: c:d whose four
words are all targets was used, in 14 families with at least 20
quadruples (5 451 quadruples in all). Each word's mean PMI was removed.
The four PMI rows were then split, over the contexts, into a relation
effect, a pair effect and an interaction. The interaction is
(P_a − P_b − P_c + P_d)/2, and additivity makes it zero. Its noise was
estimated from the half-corpora and subtracted. Completion was scored by
3CosAdd, searched over all 10 000 targets, in a rank-300 SVD embedding of
the PMI rows.

**Hierarchy (QUESTION-025).** Nouns are targets whose first WordNet synset
is a noun synset named by the word: 4 315 of them. Their attributes are
all hypernym and instance-hypernym ancestors held by at least 5 nouns and
at most half: 590 attributes, at WordNet depths 1 to 15. The PMI rows
were double-centred, which removes each word's own affine term. Two
tests were run.

- **Additive fit.** A ridge regression of the PMI rows on the attribute
  indicators, scored by 5-fold held-out-word R². Attributes were added by
  depth, and the fit was compared with the same attributes assigned to
  permuted words.
- **Probes.** Class-balanced linear probes for each attribute, on SVD
  embeddings of rank 10, 30 and 100, 5-fold. Each probe's false positives
  were checked: how many fall inside the attribute's nearest attribute
  ancestor (its "parent")?

## What it found

**Analogy families.** Noise-corrected median interaction share by family
(random quadruples of the same words give 0.32–0.33):

| family | quadruples | 3CosAdd | interaction share |
|---|---|---|---|
| gram6-nationality-adjective | 1161 | 0.64 | 0.212 |
| family | 156 | 0.77 | 0.225 |
| capital-common-countries | 210 | 0.74 | 0.229 |
| capital-world | 200 | 0.63 | 0.230 |
| gram8-plural | 552 | 0.60 | 0.233 |
| gram9-plural-verbs | 240 | 0.43 | 0.243 |
| gram5-present-participle | 552 | 0.33 | 0.246 |
| city-in-state | 420 | 0.27 | 0.256 |
| gram3-comparative | 552 | 0.62 | 0.258 |
| gram7-past-tense | 756 | 0.33 | 0.258 |
| gram4-superlative | 240 | 0.46 | 0.259 |
| gram2-opposite | 42 | 0.40 | 0.282 |
| gram1-adjective-to-adverb | 342 | 0.15 | 0.283 |
| currency | 28 | 0.00 | 0.296 |

- **The PMI is far from additive in every family.** The interaction keeps
  two-thirds or more of the share it has in an unstructured quadruple.
  Noise accounts for only about 28% of the raw interaction.
- **Less interaction goes with completion.** Across families, accuracy
  falls as the interaction share rises (Spearman −0.83, p < 0.001, n = 14).
  Within families, the least-interacting third of quadruples completes
  more often than the most-interacting third in 13 of 14 families (mean
  0.59 against 0.31; the exception is `family`).

**Hierarchy.** The full numbers are in results/summary.txt.

- **The additive fit explains little.** It explains at most 1.8% of the
  double-centred PMI variance, at depth ≤ 3, with ridge penalty 1. The
  split-half reliability of the PMI is 0.58, so most of the reliable
  variation is not carried by these attributes. With more attributes and
  this penalty, the fit overfits: held-out R² turns negative. It stays
  above the permuted-word fit at every depth, by 0.003 at depth 1 and
  0.09 with all attributes. The stronger-penalty refits are in
  results/hierarchy_alpha.jsonl (ALPHA-RESULT).
- **The probes do not lose deep attributes.** Balanced accuracy is about
  0.70–0.77 at rank 10 and 0.73–0.80 at rank 30, at every WordNet depth.
  The derivation's prediction, that a truncated embedding loses deep
  attributes first, is not seen with depth indexed this way.
- **Errors concentrate a little under the parent.** The share of false
  positives inside the parent is 1.8× (rank 10), 2.1× (rank 30) and about
  2.2× (rank 100, partial) the parent's share of negatives. Most false
  positives, about 90%, still fall outside it.

## What it shows, and what it cannot

- **For QUESTION-178:** a measurement of the kind it asks for, with the
  graded form of the "yes" pattern. Additivity varies with completion
  across and within families. But the families do not split into near
  additive and far from it: all are far.
- **For QUESTION-025:** additivity along the hierarchy holds weakly. The
  attributes carry a small, real part of the PMI. CLAIM-tmpe87cm shows
  that along a tree this test reduces to whether words in the same group
  share PMI rows. The probes find directions for attributes at every
  depth, but their errors cluster in the parent only modestly.
- **WordNet depth is not the model's level.** WordNet min_depth is uneven
  across branches, and many deep synsets are as frequent and coherent as
  shallow ones. So the absence of a depth effect does not test the
  claim's truncation clause, which is stated for a balanced tree.
- **Confounds and limits:**
  - one corpus of 17M tokens;
  - one window, and one PMI shrinkage;
  - word frequency, which bears on both the interaction and completion,
    is not controlled;
  - the noun filter keeps a word's dominant sense only.
- Rank-300 probes were dropped for time. The rank-100 probes cover the
  attributes listed in results/hierarchy.jsonl (PROBE-COVERAGE). The
  intervention QUESTION-178 also names was not attempted.
