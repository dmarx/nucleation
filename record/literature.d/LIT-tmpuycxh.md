---
status: Active
status_note: 'read 2026-10-09 ([NOTE-tmp9scdr](../notes.d/NOTE-tmp9scdr.md)); worth reading as the short programmatic statement, by the lab behind the olfactory and hippocampal hyperbolic findings, of why hyperbolic geometry should be expected in neural circuits, and as a map of the literatures it joins: hyperbolic random graphs and greedy routing, Zipf''s law and statistical criticality, and maximally informative representations. Its own argument is a chain of analogies, not a derivation. Zipf''s law is rewritten as a count of states growing exponentially with energy (−log probability), and exponential growth of states is a hallmark of trees and of hyperbolic space, so the two are said to be connected; but exponential growth of states holds for any system with extensive entropy, and what singles out Zipf (unit slope) plays no part in the step to geometry. A rigidity argument for three dimensions cites Mostow''s theorem, which concerns finite-volume hyperbolic manifolds of every dimension ≥ 3 and says nothing about point clouds. The one piece of data, a 3D Poincaré-ball embedding of fruit odorants with a pleasantness gradient, is reproduced from Zhou, Smith & Sharpee (2018).'
title: 'An argument for hyperbolic geometry in neural circuits'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Filed at the owner's request on 2026-10-09 from the link
    https://doi.org/10.1016/j.conb.2019.07.008 alone. Identification and
    bibliography checked against Crossref (title, sole author Tatyana O.
    Sharpee, Current Opinion in Neurobiology 58:101–104, issue dated
    October 2019, 46 references), PubMed (PMID 31476550: received 10
    April 2019, accepted 25 July 2019, epub 30 August 2019, print October
    2019) and Europe PMC (same). `published:` is 30 August 2019, the
    online date PubMed and Europe PMC give; Crossref gives only the month
    for print and issue (its 30 August `created` is a deposit date and
    not used), so per ADR-002 the earlier, exact date is taken. Full text:
    not in PubMed Central (the PMC ID converter and Europe PMC both report
    it absent), no preprint on arXiv (title and author searches) or
    bioRxiv, the Salk lab's publication list links only to PubMed, and
    ScienceDirect returned a bot challenge (HTTP 403) though Unpaywall and
    OpenAlex call it free to read at the publisher. Read in full from the
    publisher's PDF deposited in the NSF Public Access Repository
    (par.nsf.gov/biblio/10120231, funded under NSF IIS-1724421), whose
    metadata name this DOI. Not held in the Anthology of the SOTA: a
    grep of its record/ (clone at commit d8b5ba5, which may be stale)
    for the author, DOI, PMID and title found nothing.
tags:
- neuroscience
- complex-systems
- mathematics
date: '2026-10-09'
published: '2019-08-30'
doi: '10.1016/j.conb.2019.07.008'
first_author: 'Sharpee'
keywords:
- 'hyperbolic geometry'
- 'Zipf''s law'
- 'criticality'
- 'maximally informative representations'
- 'olfaction'
- 'network navigability'
- 'neural circuits'
implementations: []
summary: >-
  Sharpee (2019 online), Curr. Opin. Neurobiol. 58:101–104. A four-page
  review arguing that neural and other biological circuits should have
  hyperbolic geometry, because hyperbolic space approximates trees,
  hyperbolic networks are navigable, and Zipf's law, read as states
  growing exponentially with log-improbability and taken as the mark of
  maximally informative, latent-driven systems, shares that exponential
  growth. Its evidence is the olfactory embedding of Zhou, Smith &
  Sharpee (2018) and earlier perception work; the Zipf-to-hyperbolic link
  is an analogy, not a derivation.
---

# LIT-tmpuycxh: An argument for hyperbolic geometry in neural circuits

Tatyana O. Sharpee (2019), *Current Opinion in Neurobiology* 58:101–104,
themed issue on computational neuroscience — DOI-10.1016/j.conb.2019.07.008;
the publisher's PDF is deposited in the NSF Public Access Repository
(par.nsf.gov/biblio/10120231)

## Key takeaways

- **The thesis.** Hyperbolic geometry should apply broadly to neural and
  other biological circuits. The reasons given: hyperbolic space is the
  continuous approximation of tree-like hierarchies (exponential growth of
  states with radius, after Krioukov et al. 2010); networks on a hidden
  hyperbolic metric are navigable by greedy routing and robust to adding
  and removing nodes; and Zipf's law, ubiquitous in biology, is said to be
  a signature of the same geometry.
- **The Zipf step, and how far it goes.** With P(s) ∝ 1/r(s) and energy
  E = −log P(s), E = log r(s), so the number of states below energy E grows
  as e^E. Exponential growth of states is the hallmark of trees and of
  hyperbolic space, hence the claimed link. The argument shows a shared
  exponential, not a shared geometry: any system with extensive entropy
  has exponentially many states, and the unit slope that makes a
  distribution Zipfian is not used. The paper offers no model in which a
  hyperbolic metric produces Zipf's law or the reverse. (The sign of E is
  written loosely in the text.)
- **Zipf as maximal informativeness.** Following Schwab, Nemenman & Mehta
  (2014), Aitchison, Corradi & Latham (2016) and Cubero et al. (2019),
  Zipf's law arises when internal states are narrowly distributed for a
  fixed latent variable but their mean moves strongly with it, and the
  most informative representations of a latent variable are the ones that
  show it. This is cited, not derived; the paper sets it beside the
  navigability results as an "echo".
- **The only data shown** is a figure from Zhou, Smith & Sharpee (2018):
  monomolecular odorants from tomato and strawberry samples, with distances
  from their co-variation across samples, fall near the surface of a 3D
  Poincaré ball under hyperbolic non-metric MDS (after a topological test
  that ruled out Euclidean and spherical geometry), and the map has a
  region of odorants correlated with human pleasantness ratings. The paper
  reads this as orderly topography where early olfactory coding looks
  random.
- **Why three dimensions.** Three dimensions recur (odour statistics,
  odour perception, phylogenetic-tree visualisation), and the paper
  proposes that 3D is the lowest dimension in which a hyperbolic
  representation is robust to noise, citing Mostow rigidity. Mostow's
  theorem fixes the geometry of finite-volume hyperbolic manifolds of
  dimension ≥ 3 by their fundamental group; it is not a statement about
  noisy embeddings, and it does not single out 3 except as its lowest case.
- **Low-dimensional manifolds versus exponentially many states.** The
  closing argument: neural and behavioural data lie on low-dimensional
  manifolds, yet behaviour has exponentially many hierarchically organised
  states, and a low-dimensional hyperbolic space holds both.

## Standing in the record

Filed at the owner's request on 2026-10-09, in the second part of the
batch on hierarchy and hyperbolic geometry that the owner asked for after
the record opened [QUESTION-025](../questions.d/QUESTION-025.md). The first part was Cagnetta et al.'s random
hierarchy model ([LIT-tmpz5v25](LIT-tmpz5v25.md)), Krioukov et al. 2010 ([LIT-tmp0u9c9](LIT-tmp0u9c9.md)), Sala et
al. 2018 ([LIT-tmpt10fk](LIT-tmpt10fk.md)), Lin et al. 2023 ([LIT-tmpjwrpt](LIT-tmpjwrpt.md)), Zhang, Rich, Lee &
Sharpee ([LIT-tmpvydv3](LIT-tmpvydv3.md)), Yang et al. 2023 ([LIT-tmpocqly](LIT-tmpocqly.md)) and Ganea, Bécigneul &
Hofmann 2018 ([LIT-tmp5o7bs](LIT-tmp5o7bs.md)).

Read on 2026-10-09 ([NOTE-tmp9scdr](../notes.d/NOTE-tmp9scdr.md)). It sits between two of its siblings by
the same lab: it reproduces the olfactory embedding of Zhou, Smith &
Sharpee 2018 ([LIT-tmpp74b9](LIT-tmpp74b9.md)) as its evidence, and it states the programme that
Zhang et al. ([LIT-tmpvydv3](LIT-tmpvydv3.md)) later tested in hippocampal recordings. Its geometric
background is Krioukov et al. ([LIT-tmp0u9c9](LIT-tmp0u9c9.md)), its ref. 8. Its machine-learning
citation (ref. 9) is Ganea, Bécigneul & Hofmann's *Hyperbolic Neural
Networks* (NeurIPS 2018), not the same authors' entailment-cones paper
held as [LIT-tmp5o7bs](LIT-tmp5o7bs.md). No THEORY is filed: its claims are a perspective's
conjectures, and its one empirical finding belongs to the 2018 paper.

It is not a reading for the anthology: no machine-learning practice is
involved.
