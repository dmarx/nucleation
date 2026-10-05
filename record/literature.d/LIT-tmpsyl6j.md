---
status: Active
status_note: 'read 2026-10-05 ([NOTE-tmpikmaq](../notes.d/NOTE-tmpikmaq.md)): in full, from the publisher''s PDF in ANU Open Research, the co-author''s institutional repository, marked open access. Worth reading for a mechanism by which an outside funder biases a scientific community without corrupting anyone: given methodological diversity, a merit-based system and turnover, funding researchers whose methods already favour a product makes them more productive and more likely to train newcomers. An independent funder helps only if it discounts industry-funded work; funding on merit alone makes things worse. Limits: one historical case and a 20-agent simulation at a few parameter settings; run counts and network are not reported, and robustness to network structure rests on a footnote.'
title: 'Experimentation by Industrial Selection'
version: 1
history:
- version: 1
  date: '2026-10-05'
  note: >-
    Read in full: the publisher's PDF deposited in ANU Open Research
    (handle 1885/162769), printed pp. 1008–1019 with footnotes 1–6 and
    references, plus a final notice page; Figures 1 and 2 read from
    rendered page images, so values taken from them are approximate. The
    record names Bruner as an ANU author, is marked "Open Access" and
    "Published Version", and cites the publisher's permission for
    repository deposit. The last page carries an aggregator notice that the
    content "may not be copied or emailed to multiple sites or posted to a
    listserv" without permission, but "users may print, download, or email
    articles for individual use"; the copy was used for individual reading
    only. The text extraction renders σ as "j" and "=" as "5". `published:`
    is the first of the issue month, Crossref giving December 2017 and no
    day (its 2022 online date is the move to Cambridge Core). Not held in
    the Anthology of the SOTA: a grep of its literature.d for "Holman" and
    "Industrial Selection" found nothing.
tags:
- philosophy-of-science
- epistemology
- network-science
date: '2026-10-05'
published: '2017-12-01'
doi: '10.1086/694037'
url: 'http://hdl.handle.net/1885/162769'
first_author: 'Holman'
keywords:
- 'industry funding'
- 'conflicts of interest'
- 'industrial selection'
- 'network epistemology'
- 'methodological diversity'
- 'social epistemology'
- 'medical research'
implementations: []
summary: >-
  Holman & Bruner (2017), Philosophy of Science 84:1008–1019. Industry can
  bias a scientific community without corrupting anyone, by funding
  researchers whose methods already favour its product, so that they are
  more productive and train more newcomers. Shown in a bandit-model
  simulation with methodological diversity and turnover, after the
  antiarrhythmic drug case. An independent funder helps only if it
  discounts industry-funded work.
---
<!-- inactive-ok-file: LIT-tmpyzyje — Deferred; cited for context or as the source of this reading, nothing here rests on its being settled -->
<!-- inactive-ok-file: THEORY-tmpm45lu — Proposed; cited for context or as the source of this reading, nothing here rests on its being settled -->

# LIT-tmpsyl6j: Experimentation by Industrial Selection

Bennett Holman & Justin Bruner (2017), *Philosophy of Science*
84(5):1008–1019 — DOI-10.1086/694037

## Key takeaways

- **The thesis** (p. 1008). "Given methodological diversity and a
  merit-based system, industry funding can bias a community without
  corrupting any particular individual."
- **The case** (pp. 1010–1012). In the antiarrhythmic drug disaster,
  industry funded researchers who already measured efficacy by arrhythmia
  suppression, a quick surrogate endpoint, and cancelled Winkle's
  contracts when he found deadly side effects. Morganroth and others
  "were not hacks": their views were the same before and after funding.
  Their productivity made them influential, and their method became the
  community's default.
- **The model** (pp. 1012–1015). Zollman's bandit model of network
  inquiry with three changes: agents differ in productivity, in
  methodological bias (their measured success rates are drawn around the
  true ones with variance σ²), and they leave and are replaced, newcomers
  inheriting a method in proportion to its holder's productivity (a Moran
  process). Industry adds F trials a round to anyone whose method
  overstates the drug by more than T.
- **Results.** More methodological diversity alone lowers the chance of
  converging on the better action. Industry funding lowers it further, and
  more so as F grows; without diversity, industrial selection "does not
  occur" (p. 1015).
- **Countermeasures** (pp. 1016–1018). An independent funder that funds on
  productivity makes things worse, since industry-funded researchers
  qualify twice. One that ignores industry-funded trials when assessing
  merit improves the community. Integrity safeguards, even perfectly
  followed, do not address the effect.

## Standing in the record

Filed on 2026-10-05 at the owner's request, as a supplement to the essay on
organizational will. It is the read substitute for the authors' 2015 paper
([LIT-tmpyzyje](LIT-tmpyzyje.md)), whose repository copy is embargoed. It builds on the
network-epistemology models the record holds: Zollman's ([LIT-tmp8lzwo](LIT-tmp8lzwo.md),
[LIT-tmpkqfje](LIT-tmpkqfje.md)) and Rosenstock et al.'s ([LIT-tmphw2gz](LIT-tmphw2gz.md)). The account is
[THEORY-tmpm45lu](../theory.d/THEORY-tmpm45lu.md).

It bears on the essay's §8.2. A community can meet norms of open
criticism, with dissenters at the conferences and regulators overseeing,
and still be steered, because what is selected is methods, not opinions.
