---
status: Active
status_note: 'read in full 2026-09-27 ([NOTE-tmp9hu3e](../notes.d/NOTE-tmp9hu3e.md)); worth reading for §§4–7, a correct and genuinely new result: a complete cohomological test for contextuality on cyclic scenarios, which closes the Hardy and Carù-2017 gaps. Read it knowing that §8''s generalisation, its §8.1 Kochen–Specker example and Conjecture 9.1 are wrong as stated.'
title: 'Towards a complete cohomology invariant for non-locality and contextuality'
version: 2
history:
- version: 2
  date: '2026-09-27'
  note: >-
    Read in full (The full text of arXiv 1807.04203 v1, from the arXiv PDF,
    46 pp.: abstract, §§1–9 (Background; False positives; Joint scenarios
    and joint models; Contextuality of joint models; Cyclic models, paths
    and cycles; Cohomology of cyclic models with the §7.2.1 examples;
    Extension to general models with the §8.1 examples, including the full
    91-equation system for the Kochen–Specker cover; Conclusions and
    Conjecture 9.1), acknowledgements and all 20 references. The paper has
    no appendices. Nothing was skipped. The arXiv abstract page lists one
    version only, v1 (11 Jul 2018, 733 KB; comment "46 pages, 25 figures";
    quant-ph only), with no journal reference and no DOI other than the
    arXiv DataCite one. The PDF's own title is "Towards a complete
    cohomological invariant…" (the arXiv listing says "cohomology").
    `pdftotext` was not available, so I extracted the text with PyMuPDF. The
    bundle diagrams (Figs 1–25) do not survive extraction. I read the tables
    and the linear systems from the text. I did not use the figures for any
    claim I checked; I recomputed those instead. I then implemented the
    paper's joint-model construction and its ℤ/2 obstruction myself, as
    exact linear algebra over GF(2), with GF(1000003) as a stand-in for ℚ. I
    checked every worked example and ran a randomised test of the main
    theorem (details under Key results).); the first NOTE on it, since it
    was seeded from the abstract alone. Status set from the reading: Active.
tags:
- contextuality
- quantum-foundations
- mathematics
date: '2026-09-27'
published: '2018-07-11'
arxiv: '1807.04203'
first_author: 'Carù'
keywords:
- 'Čech cohomology'
- 'strong contextuality'
- 'logical contextuality'
- 'cyclic scenarios'
- 'complete invariant'
implementations: []
summary: >-
  Carù (2018), [ARXIV-1807.04203](https://arxiv.org/abs/1807.04203). For cyclic scenarios, where the contexts'
  intersection graph is a single chordless N-cycle, Carù proves that ℤ/2
  Čech cohomology of the (N−1)-th iterated "joint model" is a complete
  invariant for logical and strong contextuality (Thm 7.7). I confirmed
  this on the Hardy model, on his own 2017 counterexample (detected on all
  22 sections at level 3) and on 659 random contextual cycle models. The
  extension beyond cycles does not hold as stated. Prop 8.2 is false on
  the paper's own Table 5 model. Worse, the one non-cyclic case the paper
  claims to repair, the §8 Kochen–Specker cover of
  Abramsky–Mansfield–Barbosa, is never detected at any level under the
  paper's definitions (my proof and computation). That refutes the paper's
  closing Conjecture 9.1.
extends:
- LIT-279
---

# LIT-tmpujpg7: Towards a complete cohomology invariant for non-locality and contextuality

Carù (2018), *arXiv preprint* — [ARXIV-1807.04203](https://arxiv.org/abs/1807.04203)

## Standing in the record

Filed on 2026-09-27 at the owner's request, as the sequel to [LIT-279](LIT-279.md) on the
line from [LIT-277](LIT-277.md). `published:` is the arXiv v1 date
([ADR-002](../decisions.d/ADR-002.md)). No published version is known.

It was filed `Deferred`, unread. [NOTE-tmp9hu3e](../notes.d/NOTE-tmp9hu3e.md) is the close reading of 2026-09-27, and it placed the work: **Active** — worth reading for §§4–7, a correct and genuinely new result: a complete cohomological test for contextuality on cyclic scenarios, which closes the Hardy and Carù-2017 gaps. Read it knowing that §8's generalisation, its §8.1 Kochen–Specker example and Conjecture 9.1 are wrong as stated.
