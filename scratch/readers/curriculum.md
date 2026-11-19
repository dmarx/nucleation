# Reader notes, in flight: curriculum (removed when filed)

## 2026-11-19: copies located
- Crossref (no mailto): DOI 10.1145/1553374.1553380 confirmed; Bengio, Louradour, Collobert, Weston, "Curriculum learning", ICML 2009 (Proc. 26th ICML), pp. 41-48.
- Semantic Scholar API: openAccessPdf status CLOSED.
- ronan.collobert.com/pub/matos/2009_curriculum_icml.pdf: 200, 8-page PDF (pdfTeX, May 2009), on co-author Collobert's own site. Author's page: lawful (ADR-074). Being read.
- iro.umontreal.ca/~lisa/pointeurs/BengioCurriculum.pdf: 404.
- qmro.qmul.ac.uk handle: empty reply from server; not pursued.

## 2026-11-19: read in full (8 pp., pdftotext; figures viewed as rendered pages)
- Four experiments: 4.1 convex toy (easy-only SVM, 16.3% vs 17.1% error); 4.2 Perceptron, 200 updates, error at end of a fixed budget, curriculum vs random vs anti-curriculum (anti-curriculum appears only in Figure 1's legend, not in the text); 5 shapes, 2-stage BasicShapes -> GeomShapes, final test error by "switch epoch"; 6 language model, growing vocabulary 5k -> 20k, final log-rank 2.78 vs 2.83.
- Measure is mostly final performance (shapes, LM) or error at a fixed small budget (perceptron). No time-to-level or examples-to-level number anywhere.
- Figure 5: the curriculum model is WORSE on the target distribution until "about 1 billion updates"; the speed claim does not hold for the LM in update count.
- Mechanism: continuation method (sec. 3) and an apparent regularizer (sec. 1, 7). Ordering that hurts: anti-curriculum in Fig. 1 (worse than random at some input dimensions); Krueger & Dayan's fixed-resource result cited in sec. 7; Rohde & Plaut "useless for some tasks".
- Doubt: Fig. 1 and Fig. 3 values are read off plots, approximate, not quotable.
