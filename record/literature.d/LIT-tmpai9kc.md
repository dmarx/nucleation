---
status: Active
status_note: >-
  read 2026-10-20 ([NOTE-tmpzc5m1](../notes.d/NOTE-tmpzc5m1.md)) in full, from the authors' PostScript copy on Chorin's Berkeley page; worth reading for the generalized Langevin identity of the resolved variables, with conditional expectation under an invariant measure as the projection (Markovian term R(A) = E[LA|A], memory K(s, A) = E[LS⊥ˢF|A], noise S⊥ᵗF with zero conditional mean), for first-order optimal prediction as its Markovian part, and for the renormalized Hamiltonian −log∫e^{−H} in the canonical case. Read it knowing that its claim that no m-equation Markovian model beats first-order optimal prediction in mean square holds only for the instantaneous rate, that it states no fluctuation–dissipation relation and no criterion for when memory may be dropped, and that its one demonstration (m = 0, perturbative, kernels cut off at a time chosen to give a reasonable decay) shows the decay of the mean but not a faithful mean after t ≈ 2.
title: 'Optimal prediction and the Mori–Zwanzig representation of irreversible processes'
version: 2
history:
- version: 1
  date: '2026-10-19'
  note: >-
    Filed, not read. Citation checked against Crossref, OpenAlex and arXiv on 2026-10-19. `published:` is Crossref's date, 28 March 2000. No arXiv copy was found. Not held in the Anthology of the SOTA: a grep of its record/ (clone of 2026-10-19, commit d1573d2) for the authors, title and identifiers found nothing.
- version: 2
  date: '2026-10-20'
  note: >-
    Read in full (NOTE-tmpzc5m1) from the authors' PostScript copy on Chorin's Berkeley page, made on 1999-12-16, the acceptance date. The PMC PDF was behind a reCAPTCHA, pnas.org and Europe PMC returned 403, and NCBI's XML carries the front matter only. Status Deferred → Active. The open-copy URL is added. The summary was right in substance and is sharpened. It now names the projection (conditional expectation under an invariant measure), the setting (any flow with an invariant measure, not only a Hamiltonian one) and the example.
tags:
- mathematics
- natural-sciences
- probabilistic-modeling
date: '2026-10-19'
published: '2000-03-28'
doi: '10.1073/pnas.97.7.2968'
url: 'https://math.berkeley.edu/~chorin/CHK.ps'
first_author: 'Chorin'
keywords:
- 'Mori–Zwanzig'
- 'optimal prediction'
- 'projection operators'
- 'irreversibility'
implementations: []
summary: >-
  Chorin, Hald & Kupferman (2000). For any flow with an invariant measure, writes the resolved variables' exact evolution as Zwanzig's generalized Langevin equation, with conditional expectation as the projection: a Markovian term E[LA|A], a memory integral and a noise with zero conditional mean. First-order optimal prediction is the Markovian term alone. In a perturbative nonlinear Schrödinger example, keeping the memory recovers the decay of the conditional mean that the Markovian scheme misses.
supports:
- CLAIM-tmpmonrv
---
<!-- inactive-ok-file: THEORY-257 — Proposed; open claims and readings named for context, nothing here rests on their being settled -->
# LIT-tmpai9kc: Optimal prediction and the Mori–Zwanzig representation of irreversible processes

Chorin, A. J., Hald, O. H. & Kupferman, R. (2000). Optimal prediction and the Mori–Zwanzig representation of irreversible processes. *Proceedings of the National Academy of Sciences* 97(7): 2968–2973. doi:10.1073/pnas.97.7.2968. Open copy: PMC16175.

Read in full 2026-10-20 ([NOTE-tmpzc5m1](../notes.d/NOTE-tmpzc5m1.md)), from the authors' copy at
https://math.berkeley.edu/~chorin/CHK.ps.

## Why this is here

A3 and A5 put Mori–Zwanzig first among the physics readings: it says what becomes of eliminated degrees of freedom, which come back as memory and noise. Bears on [QUESTION-tmpxapb2](../questions.d/QUESTION-tmpxapb2.md) and [THEORY-257](../theory.d/THEORY-257.md).
