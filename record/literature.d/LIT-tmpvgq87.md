---
status: Active
status_note: 'read 2026-10-23 ([NOTE-tmpsj4fq](../notes.d/NOTE-tmpsj4fq.md)): in full, from the publisher''s CC BY PDF as deposited in Aarhus University''s repository (pure.au.dk), checked against the University of Amsterdam deposit. A deep active-inference model of valence. A precision term γ sets how far the agent''s preference-driven action model, rather than a habitual prior, governs policy selection. Its update, "affective charge", is positive when outcomes raise confidence in the action model and negative when they lower it. A second, slower level infers a binary valence state from affective charge and sends priors on γ back down. Simulated in a T-maze with reversal, the agent with the valence level adapts faster than one without it. "Felt" means explicitly represented, which the authors take as necessary for self-reportable experience of valence. Filed for the record''s candidate that a valence regime is felt when the system models its own potential ([CLAIM-tmpz8lli](../claims.d/CLAIM-tmpz8lli.md)).'
title: 'Deeply Felt Affect: The Emergence of Valence in Deep Active Inference'
version: 1
history:
- version: 1
  date: '2026-10-23'
  note: >-
    Read in full: the published article (Neural Computation 33(2):398–446,
    CC BY 4.0) as deposited by Aarhus University (pure.au.dk, file
    307231113/neco_a_01341.pdf, 49 pp.), text extracted with pdftotext.
    The MIT Press PDF returned a 403 to this client. The University of
    Amsterdam deposit (pure.uva.nl, 60962725) is the same final version
    with a cover page. The PubMed Central page (PMC8594962) returned a
    bot-check page, and the PsyArXiv preprint (doi:10.31234/osf.io/62pfd)
    was not compared. The supplementary appendixes A1–A4 are not in the
    PDF and were not read. Details checked against Crossref (DOI
    10.1162/neco_a_01341): Casper Hesp, Ryan Smith, Thomas Parr, Micah
    Allen, Karl J. Friston and Maxwell J. D. Ramstead, issued 1 February
    2021. A grep of record/literature.d and record/notes.d for "Hesp",
    the title and the DOI found it cited in NOTE-785, NOTE-958 and others
    but not filed. Brouillet and Friston's reading (NOTE-785) names it as
    their nearest formal neighbour for valence, "neither held in the
    record".
tags:
- emotion-and-affect
- probabilistic-modeling
- consciousness
- behavioral-integration
date: '2026-10-23'
published: '2021-02-01'
doi: '10.1162/neco_a_01341'
url: 'https://pure.au.dk/portal/en/publications/303912f7-c5c8-4f33-bc65-be822547eb08'
first_author: 'Hesp'
keywords:
- 'active inference'
- 'valence'
- 'affective charge'
- 'expected precision'
- 'subjective fitness'
- 'parametric depth'
- 'implicit metacognition'
implementations:
- 'https://github.com/CasperHesp/deeplyfeltaffect'
summary: >-
  Hesp, Smith, Parr, Allen, Friston & Ramstead (2021), Neural Computation
  33(2):398–446. Valence is a state of self, inferred at a hierarchically
  deeper level from changes in the expected precision γ of one's action
  model, which weights preference-driven expected free energy against a
  habitual prior in policy selection. The update to γ, affective charge,
  is positive when outcomes raise confidence in the action model and
  negative when they lower it. The valence level sends priors on γ back
  down. A simulated rat in a T-maze with context reversal infers negative
  and then positive valence, and adapts better than an agent without that
  level.
supports:
- CLAIM-tmpe0iew
- CLAIM-tmptd5us
---
<!-- inactive-ok-file: CLAIM-tmpz8lli THEORY-662 — Proposed; the account and candidate this work bears on, and the fluency reading that cites it, cited as open -->

# LIT-tmpvgq87: Deeply Felt Affect: The Emergence of Valence in Deep Active Inference

Casper Hesp, Ryan Smith, Thomas Parr, Micah Allen, Karl J. Friston & Maxwell
J. D. Ramstead (2021), *Neural Computation* 33(2):398–446 —
DOI-10.1162/neco_a_01341

## Key takeaways

- **Valence is inferred from confidence in one's action model.** "agents
  infer their valence state based on the expected precision of their
  action model—an internal estimate of overall model fitness (“subjective
  fitness”)" (p. 399).
- **Affective charge (AC)** is the update to that precision. It "lends a
  sign to otherwise unsigned divergences between predictions and outcomes"
  (p. 399). It is zero when policies go as expected and positive or
  negative as outcomes raise or lower confidence (pp. 409–410).
- **What γ does.** "higher γ values afford a greater influence of the
  expected free energies of each policy entailed by one’s current action
  model" (p. 408), against a fixed habitual prior over policies. With low γ
  the agent will "fall back on her baseline prior over policies" (p. 420).
- **The deep level.** A second level, slower and across trials, holds a
  binary valence state. It takes AC as evidence and sets the lower level's
  prior on γ (pp. 416–420). The authors stress that they "do not equate
  this notion of expected precision (or confidence) with valence directly"
  (p. 426).
- **"Felt" means explicitly represented.** "Presumably this type of
  explicit valence representation is also a necessary condition for
  self-reportable experience of valence" (p. 429). And "it is an open
  question which level or subset of levels may be privileged with respect
  to its contribution to affective phenomenology" (p. 433).
- **A simulation, not data.** A T-maze over 64 trials with reversal at
  trial 33. The valence level speeds re-adaptation and attenuates repeated
  AC. Before reversal, "their behaviors were indistinguishable" (p. 425).
- **Its own hardest problem.** It names "the strongest and most important
  challenge" (p. 430): dopamine, a candidate carrier of AC, is tied to
  "wanting" rather than pleasure.

## Standing in the record

Filed on 2026-10-23 for the record's candidate that a valence regime is
felt when the system models its own potential ([CLAIM-tmpz8lli](../claims.d/CLAIM-tmpz8lli.md)), after
Brouillet and Friston ([NOTE-785](../notes.d/NOTE-785.md), [THEORY-662](../theory.d/THEORY-662.md)), who cite this paper for
valence. Structurally, it is the nearest existing model of that
candidate. γ is the weight of one ordering against another in policy
selection, and the deep level models it. But it identifies valence with
the self-model, not with the potential. And it makes negative valence a
*weakening* of the preference ordering's potential. Read in
[NOTE-tmpsj4fq](../notes.d/NOTE-tmpsj4fq.md).
