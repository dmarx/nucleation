---
status: Read
paper: 'LIT-tmpqoytq'
title: 'Søgaard et al. — Limits of unsupervised dictionary induction'
version: 1
history:
- version: 1
  date: '2026-10-29'
  note: >-
    Read in full from the arXiv preprint 1805.03620v1 (9 May 2018), 11
    pp. in the arXiv layout, fetched 2026-10-29. The ACL 2018
    proceedings version (pp. 778–788) was not compared. Text extracted
    with `pdftotext -layout` and, for reading order, plain `pdftotext`;
    page numbers are the arXiv copy's. I read the abstract, §§1–6,
    footnotes 1–9, the captions of Figs. 1–4 and Tables 1–5, and the
    reference list. Figs. 1, 3 and 4 did not survive extraction beyond
    their captions; Fig. 2's bar labels survived only partly, so I cite
    its numbers only where the text repeats them. I recomputed the
    correlation of §4.7 from Table 2's eight rows (numpy): Pearson
    −0.889, Spearman −0.905, which matches the reported ρ = 0.89 in
    magnitude; the sign is negative because Δ is a dissimilarity.
date: '2026-10-29'
summary: >-
  The adversarial unsupervised method of Conneau et al. (2018) induces
  bilingual dictionaries only when the two embedding spaces are alike:
  it fails for English paired with Estonian or Finnish, for corpora from
  different domains even within English–Spanish, and for spaces trained
  by different algorithms. A seed of identically spelled words does as
  well or better. A spectral dissimilarity of small nearest-neighbour
  graphs tracks success across eight language pairs (|ρ| = 0.89). The
  failures are partly optimiser instability (some seeds succeed), and the
  method tested is adversarial, not GW.
---
<!-- inactive-ok-file: CLAIM-135 THEORY-tmpox88b — Proposed, Open or Deferred; the entries this reading bears on, cited as open -->

# NOTE-tmpi3f1e: Søgaard et al. — Limits of unsupervised dictionary induction

## Contribution

It tests one fully unsupervised method of bilingual dictionary induction
(BDI), Conneau et al.'s adversarial mapping with Procrustes refinement and
CSLS retrieval, outside the conditions under which that method was
reported. It varies the language pair, the corpus domain, the embedding
algorithm and hyperparameters, and the dimension, and in each case finds
settings where the method fails outright. It also shows that a seed
dictionary of identically spelled words, which is weak and free, is more
robust. Finally it proposes a spectral measure of how alike two
embedding spaces' nearest-neighbour graphs are, and reports that the
measure tracks BDI success.

## Key insight

The unsupervised methods rest on an assumption the paper quotes from
Barone (2016): monolingual embedding graphs are "approximately
isomorphic" (p. 1). The method succeeds where that is close to true and
fails where it is not. What makes it true is not only the languages. It
also depends on the corpora and on the algorithm that embedded them:
"the performance of unsupervised BDI depends heavily on all three
factors: the language pair, the comparability of the monolingual corpora,
and the parameters of the word embedding algorithms" (p. 2). A structural
fit between two spaces therefore partly measures how alike the two
embedding pipelines were.

## Assumptions

- **One method.** Every experiment is on Conneau et al. (2018), the MUSE
  code (§3.2, p. 4). The authors say their "results should extend to
  Barone (2016) and Zhang et al. (2017), which rely on very similar
  methodology" (footnote 1, p. 1). GW ([LIT-tmpprsxm](../literature.d/LIT-tmpprsxm.md)) is a different
  method and is not tested.
- **fastText skip-gram embeddings** on Polyglot Wikipedia by default:
  window 2, 15 negatives, character n-grams 3–6, 300 dimensions, words
  with more than 5 occurrences (§4.1, pp. 4–5).
- **Evaluation**: P@1 with CSLS retrieval on Conneau et al.'s test
  dictionaries, 1,500 pairs per language (p. 4).
- **Typology from Table 1** (p. 5): marking (dependent, mixed, double),
  morphological type and number of cases for each language. The
  classification is the authors'.

## Key results

### Isomorphism (§2, pp. 2–3)

- Nearest-neighbour graphs of the 10 most frequent English words and their
  German translations are not isomorphic (Fig. 1); neither are those of
  the 10 most frequent nouns. Of 10 random samples of frequent English
  nouns and their Spanish translations, "only in 1/10 of the samples were
  the corresponding nearest neighbor graphs isomorphic" (p. 2), using VF2.
- The test is exact graph isomorphism of 10-node k-NN graphs. That is far
  stricter than "approximately isomorphic", and the paper's inference, "We
  take this as evidence that word embeddings are not approximately
  isomorphic across languages" (p. 2), does not follow from it alone.

### The eigenvalue measure (§2, p. 3)

- With L₁ and L₂ the Laplacians of the two nearest-neighbour graphs,
  Δ = Σ_{i=1}^{k} (λ₁ᵢ − λ₂ᵢ)² over the k largest eigenvalues, with k the
  smaller of the two values at which the top eigenvalues reach 90% of the
  spectrum's sum.
- The prose and the formula disagree on k: the prose says "the smallest k
  such that the sum of the k largest Laplacian eigenvalues is <90%", while
  the displayed condition is a ratio "> 0.9" (p. 3). The formula is the
  sensible reading.
- Δ is a dissimilarity: "the higher ∆ is, the less similar the graphs"
  (p. 3). Table 2 nonetheless labels the column "Similarity
  (Eigenvectors)", and the measure uses eigenvalues, not eigenvectors.
- The isospectrality argument is one-directional, as the authors note:
  "(approximately) isospectral graphs need not be (approximately)
  isomorphic" (p. 2), citing Gordon, Webb and Wolpert. The "approximately"
  version of the converse is asserted, not shown.

### Language pairs (§4.2, Table 2, pp. 5–6)

- **P@1, unsupervised / identical-word seed / Δ:** EN–ES 81.89 / 82.62 /
  2.07; EN–ET 00.00 / 31.45 / 6.61; EN–FI 00.09 / 28.01 / 7.33; EN–EL
  00.07 / 42.96 / 5.01; EN–HU 45.06 / 46.56 / 3.27; EN–PL 46.83 / 52.63 /
  2.56; EN–TR 32.71 / 39.22 / 3.14; ET–FI 29.62 / 24.35 / 3.98 (Table 2,
  p. 5). For Estonian and Finnish "the method fails completely" (p. 5).
- **Data size is ruled out for Finnish**: with the 1.7B-word Finnish WaC
  corpus, "P@1 equals 0.0" (p. 5).
- **Similar languages can still align**: Estonian–Finnish reaches 29.62.
  The authors conclude that the method "seems challenged when pairing
  English with languages that are not isolating and do not have dependent
  marking" (pp. 5–6; the sentence breaks across the page at "En-glish").
- **Seed instability**: "varying our random seed, performance for
  Estonian, Finnish, and Greek is sometimes (approximately 1 out of 10
  runs) on par with Turkish" (footnote 5, p. 5). So part of the failure is
  the adversarial optimiser, not the absence of a recoverable alignment.
- **Weak supervision**: the identical-word seed is "competitive" for
  similar pairs and "better" for dissimilar ones (p. 6), and this
  "questions the true applicability of fully unsupervised approaches"
  (p. 6).

### Domains (§4.3, Fig. 2, pp. 6–7)

- Corpora are capped at 1.1M sentences each, the size of EMEA, and drawn
  from EuroParl, Wikipedia and EMEA. For English–Spanish, unsupervised BDI
  is good in the three same-domain cases, and "When the two corpora are
  from different domains, performance is close to zero" (p. 6). For
  Finnish and Hungarian it is poor even within a domain. The identical-word
  baseline "achieves decent performance in many set-ups" (p. 6).
- Smaller corpora alone hurt: English–Spanish on Wikipedia drops "from
  81.19% to 46.52%" (p. 6).

### Algorithms and hyperparameters (§4.4, Table 3, pp. 6–8)

- With skip-gram on both sides, changing the window or the n-gram range
  costs little (81.89 to 80.15). With English skip-gram against Spanish
  CBOW, every setting gives 0.00–0.13 (Table 3, p. 8): "unsupervised BDI
  fails (even) for EN - ES when the two monolingual embedding spaces are
  induced by two different algorithms" (p. 6). The authors checked that
  the Spanish CBOW space is not simply worse: monolingual similarity
  Spearman ρ ≈ 0.7 (footnote 9, p. 6).

### Dimension, part of speech, frequency, homographs (§§4.5–4.6, pp. 7–8)

- At 40 dimensions, Spanish, Hungarian, Polish and Turkish get worse
  (50.33, 21.81, 20.11, 22.03), but Estonian (13.53), Finnish (15.33) and
  Greek (24.17) get better than at 300 (p. 7). The authors' reading,
  over-fitting "to some of the rarer peculiarities of these languages"
  (p. 7), is a hypothesis.
- Verbs are hardest (Table 4, p. 8). EN–FI is 0 at every frequency rank
  (p. 8). Words whose translations are homographs score lower than others
  (Table 5, p. 8).

### Predicting success (§4.7, Fig. 4, p. 9)

- "The correlation between BDI performance and graph similarity is strong
  (ρ ∼ 0.89)" (p. 9), over the eight rows of Table 2. Recomputed from the
  table: Pearson −0.889, Spearman −0.905. The magnitude matches; the sign
  is negative because Δ grows as the graphs differ. The paper reports the
  magnitude without the sign. Leaving out the three near-zero pairs, the
  Pearson correlation over the remaining five is −0.86.
- Δ is computed on "10 randomly sampled source language nearest neighbor
  subgraphs of 10 nodes and the subgraphs of their translations" (Table 2
  caption, p. 5), which uses the gold dictionary. As a diagnostic for
  whether unsupervised BDI will work, it needs the translations that BDI
  was meant to find.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Conneau et al.'s unsupervised BDI fails (P@1 ≈ 0) for English–Estonian and English–Finnish, and not because of corpus size | strong | Table 2; the 1.7B-word fiWaC control (p. 5) |
| C2 | It fails across corpus domains, even for English–Spanish | moderate | Fig. 2g; capped corpora, three domains, one run each |
| C3 | It fails when the two spaces are trained by different algorithms (skip-gram vs CBOW) | strong | Table 3, with a check on the CBOW space's quality (footnote 9) |
| C4 | A seed of identically spelled words is as good or better, and more robust | strong | Table 2, Fig. 2d–f |
| C5 | The failure is a property of non-isomorphic spaces rather than of the optimiser | weak | contradicted in part by footnote 5: about 1 in 10 seeds succeed for ET, FI, EL |
| C6 | Word embeddings are not approximately isomorphic across languages | weak | exact VF2 tests on 10-node graphs (p. 2) test exact, not approximate, isomorphism |
| C7 | A Laplacian-spectrum dissimilarity of small NN graphs predicts BDI success (|ρ| = 0.89) | moderate | eight pairs; recomputed; Δ uses gold translations; sign misreported |
| C8 | The failing languages are those that are not dependent-marking and not isolating | weak | three failing languages (ET, FI mixed; EL double), confounded with Wikipedia size and script; Hungarian, agglutinative but dependent-marking, succeeds |

## Concepts

- **Approximately isomorphic** — the assumption behind unsupervised BDI:
  monolingual embedding graphs are isomorphic "after removing a small set
  of vertices (words)" (p. 1).
- **Dependent marking** — "marks agreement and case more commonly on
  dependents than on heads" (footnote 3, p. 4).
- **Eigenvector similarity Δ** — in fact a sum of squared differences of
  Laplacian eigenvalues; zero for isospectral graphs (p. 3).
- **Identical-word supervision** — seed pairs of identically spelled words
  "without employing any additional transliteration or
  lemmatization/normalization methods", followed by Procrustes refinement
  (§3.3, p. 4).

## Connections

- The method tested is Conneau et al. 2018 (MUSE). The GW method of
  [LIT-tmpprsxm](../literature.d/LIT-tmpprsxm.md), published three months later, compares with that method;
  its Table 2 shows the same weak pair (Finnish).
- The structural premise it attacks is shared by the GW and
  global-invariance OT methods ([LIT-tmpprsxm](../literature.d/LIT-tmpprsxm.md), [LIT-tmpbs68a](../literature.d/LIT-tmpbs68a.md)). All of them
  find the best fit of one structure to another, so all of them depend on
  the two structures being alike.
- Later work on graph-matching and isometry measures for embedding spaces
  is not cited here, as it postdates the paper.

## Bearing on the record

- **[CLAIM-135](../claims.d/CLAIM-135.md): support for the gap between reconstruction and
  identification, with a sharper cause.** A good fit is not established
  identity. More than that, whether a fit exists depends on factors that
  have nothing to do with meaning: the corpus domain, and skip-gram
  against CBOW (Table 3). Two spaces built from the same words with
  different algorithms fail to align at all. So structural resemblance
  between two embeddings partly measures how alike the pipelines were. It
  is not a pure fact about the languages, still less about kinds.
- **[CASE-tmph0fxi](../cases.d/CASE-tmph0fxi.md): two design points.** First, the case's correspondence
  arm compares response matrices from different communities. The
  readers, probes and scoring pipeline should be the same in each
  community, or any failure to align is uninterpretable; this paper's
  Table 3 shows how large the effect of a pipeline difference can be.
  Second, a diagnostic of structural similarity that is to be read before
  fitting must not use the gold correspondence, as this paper's Δ does
  (Table 2 caption).
- **[THEORY-tmpox88b](../theory.d/THEORY-tmpox88b.md)**: filed from this reading together with
  [LIT-tmpprsxm](../literature.d/LIT-tmpprsxm.md)'s Table 2.
- **[CLAIM-046](../claims.d/CLAIM-046.md)**: neutral. The paper is about whether two observation
  structures coincide, not about latent states.
- **An instruction for ML practice is present**: "it might often be better
  to rely on available weak supervision" (p. 6). That belongs to the
  Anthology of the SOTA; the LIT carries the `anthology-candidate` flag.

## Limitations

- **One unsupervised method, adversarial.** Whether a non-adversarial
  method such as GW fails in the same places is not tested. The seed
  instability (footnote 5) means the reported failures mix cases where no
  alignment exists with cases where the optimiser did not find one.
- **Single runs** are reported throughout, except for the remark in
  footnote 5.
- **The typological conclusion rests on three failing languages**, and
  those differ from English in other ways too (Wikipedia size, script for
  Greek).
- **The isomorphism test is exact and tiny**, and the eigenvalue measure is
  computed on gold-translated subgraphs of 10 nodes.
- **Reporting slips**: the sign of ρ, "similarity" for a dissimilarity,
  "eigenvector" for eigenvalue, and the prose and formula for k disagree
  (p. 3).
- The figures' data did not survive extraction; I cite Fig. 2 only where
  the text gives its numbers.

## Open questions

- Does GW, which has no adversarial step, fail on the same pairs, domains
  and algorithm mismatches? [LIT-tmpprsxm](../literature.d/LIT-tmpprsxm.md)'s Table 2 suggests yes for
  Finnish (18.3 vs 33.5 for self-learning). A run of GW on this paper's
  settings would say.
- Does a structural dissimilarity computed without gold translations,
  such as the GW value itself, predict BDI success as well as Δ does?
