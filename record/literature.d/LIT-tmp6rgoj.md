---
status: Active
status_note: >-
  read 2026-10-20 (NOTE-tmpinykd) in full, from arXiv:q-bio/0403030v1; worth reading for the record's only open statement of Simon and Ando's (1961) theorem (Theorems 2.1, 2.2a and 2.2b: block-diagonal A* plus εC, the four time windows T0 < T1 < T2 < T3, and the aggregate Â_IJ = Σ_{i∈I}Σ_{j∈J} A_ij ν*_jJ), for its four-stage account of when a nearly decomposable system is decomposable, aggregable or both, and for its conclusion that quasi-equilibrium, symmetry (equitable partitions) and linkage equilibrium are independent routes to a dynamically sufficient aggregate. Read it knowing that the theorem is quoted without proof and states no rate in ε and no bound on aggregation error; that the landscape "Simon–Ando condition" is an entrywise proxy, met trivially at low mutation rate even on a flat landscape where there is no time-scale separation; that its leading-eigenvector statement fails when block leading eigenvalues coincide, the stochastic case it invokes; and that (6.2b) is wrong for radius κ ≥ 2. Published as Theory in Biosciences 123(2):139–180 (2004), doi:10.1016/j.thbio.2004.04.001.
title: 'Simon-Ando Decomposability and Fitness Landscapes'
version: 2
history:
- version: 1
  date: '2026-10-20'
  note: >-
    Filed, not read. Found by a title search during the copy hunt for Simon & Ando (LIT-1127) on 2026-10-19. Citation from the arXiv abstract page: arXiv:q-bio/0403030, v1 submitted 22 March 2004, no journal reference listed. `published:` is arXiv v1, per ADR-002. Its authors differ from LIT-tmp6vpg9's by Altenberg in place of Hermisson, and its subject is the near-decomposable (Simon–Ando) case that LIT-tmp6vpg9 leaves to work "in preparation"; it may be that work. Not held in the Anthology of the SOTA: a grep of its record/ (clone of 2026-10-19, commit d1573d2) for the identifier, the title and "Shpak" found nothing.
- version: 2
  date: '2026-10-20'
  note: >-
    Read in full (NOTE-tmpinykd) from arXiv:q-bio/0403030v1. Status Deferred → Active. The journal version was found on 2026-10-20 by a Crossref title and author search, and confirmed in OpenAlex and in PubMed (18236097, which lists the four authors): Theory in Biosciences 123(2):139–180, issue date 9 September 2004, doi:10.1016/j.thbio.2004.04.001. The DOI is added. arxiv stays the source, and `published:` stays the arXiv v1 date, the earlier appearance, per ADR-002. It is very probably the "Shpak et al., in preparation" of LIT-tmp6vpg9: it has the same first three authors, it takes the question that reference names, and it appeared in the next issue of the same volume. Neither text says so outright. The summary is corrected: what landscapes meet at low mutation rate is an entrywise proxy for the Simon–Ando condition, not the spectral condition.
tags:
- complex-systems
- philosophy-of-biology
- mathematics
date: '2026-10-20'
published: '2004-03-22'
arxiv: 'q-bio/0403030'
doi: '10.1016/j.thbio.2004.04.001'
first_author: 'Shpak'
keywords:
- 'Simon–Ando decomposability'
- 'fitness landscapes'
- 'fast–slow dynamics'
- 'mutation and recombination'
implementations: []
summary: >-
  Shpak, Stadler, Wagner & Altenberg (2004). States Simon and Ando's theorem on nearly decomposable linear systems, without proof and without rates, as four time windows separating within-block relaxation, block quasi-equilibrium, aggregate cross-block dynamics and global equilibrium. It applies an entrywise version of the condition to mutation–selection and recombination on fitness landscapes. Point mutation meets it at low mutation rates, trivially, and recombination rarely does. It concludes that Simon–Ando aggregation is one route to a dynamically sufficient aggregate, independent of exact aggregation by symmetry and of character aggregation under linkage equilibrium.
---
<!-- inactive-ok-file: LIT-1127 — Unavailable; the theorem this work applies, cited as not yet read -->
# LIT-tmp6rgoj: Simon-Ando Decomposability and Fitness Landscapes

Shpak, M., Stadler, P. F., Wagner, G. P. & Altenberg, L. (2004). Simon-Ando Decomposability and Fitness Landscapes. arXiv:q-bio/0403030 (22 March 2004). Published in *Theory in Biosciences* 123(2): 139–180 (2004). doi:10.1016/j.thbio.2004.04.001.

Read in full in NOTE-tmpinykd, from the arXiv copy.

## Why this is here

The near-decomposable case that its companion, [LIT-tmp6vpg9](LIT-tmp6vpg9.md) (read in [NOTE-tmpl2r9w](../notes.d/NOTE-tmpl2r9w.md)), only paraphrases: Simon and Ando's criteria applied, with their timescale separation, which is what [THEORY-661](../theory.d/THEORY-661.md) rests on and what [QUESTION-tmpt64jh](../questions.d/QUESTION-tmpt64jh.md) asks to bound. With Simon & Ando itself Unavailable ([LIT-1127](LIT-1127.md)), it is the nearest open statement of the theorem's conditions the record has found. The abstract's closing remark, that the formalism is unlikely to extend to other kinds of decomposition and aggregation in evolutionary systems, bears on [QUESTION-tmplru2n](../questions.d/QUESTION-tmplru2n.md).
