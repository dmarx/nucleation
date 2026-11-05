---
status: Unfetched
status_note: >-
  filed 2026-11-05, not read. No NOTE is filed, and it stays Unfetched
  until it is read, not on merit. A lawful free copy is located: Crossref
  lists an Elsevier open-archive user licence from 2013-07-17 and OpenAlex
  marks the article bronze open access at ScienceDirect, at
  https://www.sciencedirect.com/science/article/pii/S0024379501006085/pdf,
  which on 2026-11-05 returned HTTP 403 with an "Are you a robot" captcha,
  so the reader stopped and did not retry the host. The Elsevier API
  (api.elsevier.com, PII S0024379501006085) gave no full text (400
  INVALID_INPUT); the University of Northern Iowa repository record
  (scholarworks.uni.edu/facpub/3391) has the abstract only, its full-text
  link pointing back to the DOI; the authors' pages (toroidalsnark.net,
  mars.wne.edu, thomashull.com) did not connect through the session's
  proxy. A human reader can likely open the ScienceDirect copy. A
  neighbour was read and filed in its place: LIT-tmpj5g19 (Akitaya et al.
  2020) restates the paper's loop condition in global form, citing it,
  with when it is necessary and when sufficient, but not the paper's
  derivation, ordering convention, affine treatment or sufficiency
  discussion.
title: 'Modelling the folding of paper into three dimensions using affine transformations'
version: 1
history:
- version: 1
  date: '2026-11-05'
  note: >-
    Filed, not read. Registered on 2026-11-05 from the owner's pasted
    synthesis on FACT, rigidity, compliant mechanisms and origami, written
    by another assistant (A) and pasted by the owner on 2026-11-04, which
    cites only "Belcastro & Hull loop-closure condition R1(θ1)…Rk(θk)=I"
    at ScienceDirect, as O5. Identified by the reader through Crossref's
    bibliographic search, one confident match, confirmed by three later
    papers of Hull's that cite it for the condition: sarah-marie belcastro
    (the authors and Crossref write the name in lower case, not A's
    "Belcastro") and Thomas C. Hull, Linear Algebra and its Applications
    348(1–3), 273–282, June 2002, journal article. `published:` is the
    original publication date the UNI repository gives, 2002-06-15, the
    earliest exact date found. A's guessed title, venue and year are
    correct. Not held before (no hit for the DOI, the title words,
    "Belcastro" or "affine transformations"). Set Unfetched the same day
    (see the status note). Neighbour LIT-tmpj5g19 registered and read in
    its place at the owner's request.
tags:
- mathematics
date: '2026-11-05'
published: '2002-06-15'
doi: '10.1016/S0024-3795(01)00608-5'
first_author: 'belcastro'
keywords:
- 'origami'
- 'crease pattern'
- 'piecewise isometry'
- 'rotation matrices'
- 'foldability'
implementations: []
summary: >-
  belcastro & Hull (2002). Unread; from the abstract as served by the UNI
  repository, unverified until read. Folding is modelled by piecewise
  isometries from R² to R³, generalizing the necessary conditions known for
  flat folding: if a crease pattern folds, the product of the rotation
  matrices of the creases, in a non-intuitive order, is the identity. The
  condition holds locally in a multi-vertex crease pattern and can be
  adapted to a global one. Sufficient conditions are known only for the
  two-dimensional single-vertex case.
---

# LIT-tmphy9wm: Modelling the folding of paper into three dimensions using affine transformations

belcastro, s.-m. & Hull, T. C. (2002). Modelling the folding of paper into three dimensions using affine transformations. *Linear Algebra and its Applications* 348(1–3): 273–282. doi:10.1016/S0024-3795(01)00608-5.

Not read: the open-archive copy at ScienceDirect answered with a captcha (see the status note). What follows is the abstract, quoted from the UNI repository record.

## Key takeaways

*From the abstract only; unverified until read.*

- **Necessity**: if the crease pattern is foldable, "the product (in a
  non-intuitive order) of the associated rotational matrices is the
  identity matrix".
- **Local to global**: the condition "holds locally in a multiple vertex
  crease pattern and can be adapted to a global condition".
- **Sufficiency open**: sufficient conditions "are not known except in the
  two-dimensional single-vertex case".

## Standing in the record

The pasted synthesis on constraint architectures cites the loop-closure
condition and reads it as holonomy; the identification and the notation
are right as far as the neighbours show. Akitaya et al. (2020),
LIT-tmpj5g19, stands in for it in part: it states the condition, citing
this paper, for any simple closed vertex-avoiding curve, as necessary but
not sufficient because the paper may cross itself, and as sufficient near
the flat state. Foschi, Hull and Ku (2022), LIT-tmpegvxm, state its
single-vertex form. Neither gives the paper's derivation, its
"non-intuitive order", its affine bookkeeping of translations for loops
around several vertices, or its discussion of sufficiency; for those the
paper itself is needed.

A compares the condition with CLAIM-495, calling the full origami closure
condition "stronger than the partial fixed-subspace compatibility studied
in CLAIM-495". As a comparison that is true, since trivial holonomy on
every loop implies full fixed-subspace compatibility, but it is at a
different level: CLAIM-495 takes the transports as given and solves for
sections, while closure constrains the transports themselves, the fold
angles being the unknowns. Loop closure is also necessary, not
sufficient, for a folding. A's gloss of THEORY-171 for this part, as
local-to-global gluing, does not connect it to loop closure: THEORY-171 is
about causal contextuality and is unrelated. The reading of the neighbour,
NOTE-tmpd0dln, gives the full verdict.
