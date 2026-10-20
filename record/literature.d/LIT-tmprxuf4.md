---
status: Active
status_note: >-
  read 2026-10-20 ([NOTE-tmpi1i5f](../notes.d/NOTE-tmpi1i5f.md)), skimmed, from arXiv:1608.08301v2: the introduction, the statement of the theorem, the Main Lemma and its three sublemmas, the gluing construction and the convex-integration ansatz, and the whole proof of the theorem from the Main Lemma; the long estimates of §§9–10 and 17 and the appendix were not checked. Worth reading for the negative half of Onsager's conjecture: for every α < 1/3 there is a nonzero weak solution of the 3D incompressible Euler equations on the periodic box, Hölder-continuous with exponent α in space and time, that vanishes outside a finite time interval and so does not conserve energy ([THEORY-tmpy2pkj](../theory.d/THEORY-tmpy2pkj.md)). With Constantin, E and Titi ([LIT-tmpeyk8p](LIT-tmpeyk8p.md)) it fixes 1/3 as the threshold. Read it knowing that its solutions gain energy from zero and lose it again, so they are not dissipative (admissible) solutions, which came later (Buckmaster, De Lellis, Székelyhidi and Vicol 2019); that they are built by convex integration from the zero solution and so also show non-uniqueness, not that turbulent or vanishing-viscosity limits are of this kind; that the endpoint 1/3, two dimensions and finite-energy solutions on R³ are left open; and that the arXiv v2 copy read is a 2024 revision, not compared with the Annals text.
title: 'A proof of Onsager''s conjecture'
version: 2
history:
- version: 1
  date: '2026-10-20'
  note: >-
    Registered on 2026-10-20 as a follow-up named by the reading of Constantin, E and Titi (NOTE-tmpqux8d), which found that the record held only the positive half of Onsager's conjecture and named this paper for the negative half. Citation from the arXiv API and Crossref: arXiv:1608.08301, v1 submitted 30 August 2016 (v2 22 July 2024); published as Annals of Mathematics 188(3):871–963, issue date 1 November 2018, doi:10.4007/annals.2018.188.3.4 (Crossref's `created` date, 19 October 2018, is a deposit date and is not used). `published:` is the arXiv v1 date, the earliest, per ADR-002. Not held in this record or in the Anthology of the SOTA: a grep of both record/ trees (the anthology clone at commit d1573d2) for "Isett", the arXiv id and the DOI found only this record's citations of it as unread (LIT-tmpeyk8p, NOTE-tmpqux8d, THEORY-tmp99aof, QUESTION-tmpmz64i).
- version: 2
  date: '2026-10-20'
  note: >-
    Skimmed (NOTE-tmpi1i5f) from arXiv:1608.08301v2, the author's revision of 2024: the introduction, Parts II and III to the end of §8, §§11–16 and §18 were read, and the estimates of §§9–10 and 17 and the appendix were not. Status Deferred → Active. THEORY-tmpy2pkj filed Proposed. The summary is written from the reading.
tags:
- mathematics
- natural-sciences
date: '2026-10-20'
published: '2016-08-30'
arxiv: '1608.08301'
doi: '10.4007/annals.2018.188.3.4'
first_author: 'Isett'
keywords:
- 'Onsager''s conjecture'
- 'incompressible Euler equations'
- 'weak solutions'
- 'convex integration'
- 'energy conservation'
implementations: []
summary: >-
  Isett (2016; Annals 2018). For every α < 1/3 it constructs a nonzero weak solution of the 3D incompressible Euler equations on R × T³, with velocity in C^α and pressure in C^{2α} in space and time, that is identically zero outside a finite time interval, so its kinetic energy is not constant. This is the negative half of Onsager's conjecture; the positive half, conservation above 1/3, is Constantin, E and Titi's. The construction iterates a Main Lemma that adds high-frequency corrections built from Mikado flows, after a new "gluing" step that rearranges the error so that it lives on short, separated time intervals and the corrections never interact.
---
<!-- inactive-ok-file: NOTE-tmpi1i5f — Skimmed; this work's own reading, partial -->
<!-- inactive-ok-file: THEORY-tmpy2pkj — Proposed; the account this reading files, cited as its outcome -->
# LIT-tmprxuf4: A proof of Onsager's conjecture

Isett, P. (2018). A proof of Onsager's conjecture. *Annals of Mathematics* 188(3): 871–963. doi:10.4007/annals.2018.188.3.4. arXiv:1608.08301 (30 August 2016).

Skimmed in [NOTE-tmpi1i5f](../notes.d/NOTE-tmpi1i5f.md), from the arXiv copy. The theorem, and what it
implies for the coarse-grained energy flux, is filed as [THEORY-tmpy2pkj](../theory.d/THEORY-tmpy2pkj.md).

## Why this is here

The negative half of Onsager's conjecture, which the reading of Constantin, E
and Titi ([NOTE-tmpqux8d](../notes.d/NOTE-tmpqux8d.md), [THEORY-tmp99aof](../theory.d/THEORY-tmp99aof.md)) found missing. A3 had cited "Onsager's
1/3" for the point that the regularity of a field decides whether the
unresolved scales vanish in the limit, and [QUESTION-tmpmz64i](../questions.d/QUESTION-tmpmz64i.md) carries it.
Constantin, E and Titi show the flux into vanishing scales must die above
1/3. This paper shows that below 1/3 it need not: there are rough solutions
for which it survives.
