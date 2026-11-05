---
status: Active
status_note: >-
  read in part 2026-11-05 ([NOTE-tmpusebl](../notes.d/NOTE-tmpusebl.md)) from the JMLR open-access PDF:
  §§1–4 and 7 closely, §§5–6 skimmed, appendices not read. Worth reading
  as a stable, computable summary of multiparameter persistence modules:
  the persistence landscape extended to several parameters, bounded by the
  interleaving distance, and, over its weighted versions, determining the
  rank invariant; and for its plain statement that, unlike one parameter,
  there is no complete discrete invariant. Its main limits: it sees only
  the rank invariant, so features born at incomparable parameter values
  escape it; nothing on direction, paths or the cost of traversal.
  Probably, not certainly, the JMLR 2020 paper the pasted synthesis links.
  Botnan & Lesnick's survey ([LIT-tmp1045q](LIT-tmp1045q.md)) was read beside it.
title: 'Multiparameter Persistence Landscapes'
version: 1
history:
- version: 1
  date: '2026-11-05'
  note: >-
    Registered and read in part on 2026-11-05 from the owner's pasted
    synthesis on resource-bounded realizability (written by another
    assistant, A, in the same exchange as the emergency-readiness
    bibliography, pasted 2026-11-04), whose Response 3 §5 says
    "Multiparameter persistent homology is a developed mathematical field,
    with invariants and stability results" and links
    jmlr2020.csail.mit.edu, naming no work. Identification probable:
    https://jmlr2020.csail.mit.edu/papers/v21/19-054.html serves the same
    page as https://jmlr.org/papers/v21/19-054.html, this paper, whose
    content fits A's sentence; the rest of the JMLR 2020 volume was not
    searched. Citation checked against the arXiv listing and JMLR's own
    BibTeX; JMLR assigns no DOI, so there is no Crossref record to check,
    and OpenAlex was not consulted. Oliver Vipond, sole author (University
    of Oxford), Journal of Machine Learning Research 21 (2020), paper 61,
    pp. 1–38, submitted 1/19, published 3/20, CC-BY 4.0. arXiv:1812.09935,
    v1 2018-12-24, which is `published:`. Not held before. Copy:
    https://jmlr.org/papers/volume21/19-054/19-054.pdf, 38 pp., extracted
    with pdftotext. Status set to Active.
tags:
- mathematics
date: '2026-11-05'
published: '2018-12-24'
arxiv: '1812.09935'
url: 'https://jmlr.org/papers/v21/19-054.html'
first_author: 'Vipond'
keywords:
- 'multiparameter persistence'
- 'persistence landscape'
- 'rank invariant'
- 'interleaving distance'
- 'stability'
- 'topological data analysis'
implementations: []
summary: >-
  Vipond (2018; JMLR 2020). "In this paper we generalise the persistence
  landscape to multiparameter persistence modules providing a stable
  representation of the rank invariant." The landscape λ(k, x) is the
  largest radius over which k features persist in every positive direction
  through x; it restricts on each diagonal line to the one-parameter
  landscape. Its ∞-distance is bounded by the interleaving distance
  (Theorem 30), and the weighted landscapes together determine the rank
  invariant of a finitely presented module (Proposition 36). Being
  Banach-space valued, landscapes admit means, a law of large numbers and a
  central limit theorem. The setting is hard: "there is not an analogous
  complete discrete invariant in the multiparameter setting".
---
<!-- inactive-ok-file: THEORY-tmpwe5km CLAIM-tmpuk8gq NOTE-tmpusebl — Proposed, Skimmed or new; cited from the reading of Vipond (2020) as open -->

# LIT-tmp75waa: Multiparameter Persistence Landscapes

Vipond, O. (2020). Multiparameter Persistence Landscapes. *Journal of Machine Learning Research* 21(61): 1–38. arXiv:1812.09935 (v1 2018).

## Key takeaways

*From the reading, [NOTE-tmpusebl](../notes.d/NOTE-tmpusebl.md). Section and result numbers are the
paper's.*

- **Classification is hard** (§1). "unlike the single parameter case where
  we may associate a persistence diagram to a module, there is not an
  analogous complete discrete invariant in the multiparameter setting."
- **The construction A uses** (Example 1): sublevel sets of f : X → Rⁿ,
  indexed by the vector of thresholds.
- **Stability** (Theorem 30): "the ∞-landscape distance of the
  multiparameter persistence landscapes is bounded by the interleaving
  distance dI", itself "the most discriminating, stable metric on
  multiparameter persistence modules" and "NP-hard to compute" (§2).
- **Injectivity** (Proposition 36): the weighted landscapes preserve
  "almost all the information contained in the rank invariant of finitely
  presented persistence modules" (§4.2).
- **Its limit** (§7): "We have restricted our invariant to the
  discriminating power of the rank invariant."

## Standing in the record

The pasted synthesis on resource-bounded realizability links it for the
claim that multiparameter persistence is a developed field with invariants
and stability. That is right, and understated: no complete discrete
invariant exists, the modules are of wild representation type (Botnan &
Lesnick, [LIT-tmp1045q](LIT-tmp1045q.md), read beside it as an open survey), and the natural
distance is NP-hard to compute. Its Example 1 is A's budget-indexed module
b ⟼ H_k(Q_z(b)); it is the multiparameter version of the one-parameter
construction held in [LIT-tmpbs8e0](LIT-tmpbs8e0.md), and the right object for [CLAIM-tmpuk8gq](../claims.d/CLAIM-tmpuk8gq.md)'s
frontier, though its rank-based summaries cannot be relied on to recover
all of it. Filed from it: [THEORY-tmpwe5km](../theory.d/THEORY-tmpwe5km.md).
