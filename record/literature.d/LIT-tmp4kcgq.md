---
status: Active
status_note: >-
  read 2026-11-03 (NOTE-tmpi46fq), main text, online methods and
  references, from the scan of the published article on gwern.net, at the
  owner's direction; the supplementary material was not read. Worth
  reading as the measurement of how large, and how small, ephaptic effects
  are at physiological field strengths: fields like the LFP's shift spike
  timing and synchronize nearby neurons without changing spike counts. It
  explains them by Kirchhoff's laws, so it is not evidence against
  micro-level description.
title: 'Ephaptic coupling of cortical neurons'
version: 3
history:
- version: 1
  date: '2026-11-02'
  note: >-
    Filed, not read. Citation checked against Crossref on 2026-11-02 (no
    email address sent, ADR-008): dated 2011-01-16. The summary says why it
    is here, not what it shows.
- version: 2
  date: '2026-11-03'
  note: >-
    Looked for and not read (ADR-041): OpenAlex (no email sent,
    ADR-008), Unpaywall (noreply@anthropic.com), Europe PMC, the
    CaltechAUTHORS and EPFL Infoscience records, and a web search. The
    repositories hold no public file. A gwern.net copy was located and
    fetched, but this session's permission check refused reading it, so
    it was deleted unread. Status Deferred → Unavailable. Nothing here
    reports the paper's findings.
- version: 3
  date: '2026-11-03'
  note: >-
    Read at the owner's direction ("go ahead and read the gwern copy"),
    from the scan of the published article at
    gwern.net/doc/psychology/neuroscience/2011-anastassiou.pdf, whose
    licence is not stated; the owner ruled on it under ADR-064. Text
    extracted with pypdf; pp. 217–223 and the online methods read, figure
    panels from their captions; the supplementary material, on Nature's
    site, not read. Status Unavailable → Active. The summary is replaced
    by one from the text. One THEORY is filed (THEORY-tmpvy87o).
tags:
- neuroscience
date: '2026-11-02'
published: '2011-01-16'
doi: '10.1038/nn.2727'
first_author: 'Anastassiou'
keywords:
- 'ephaptic coupling'
- 'extracellular fields'
implementations: []
summary: >-
  Anastassiou, Perin, Markram & Koch (2011), Nature Neuroscience 14:
  217–223. In rat cortical slices with synaptic transmission blocked, a
  12-pipette setup applied and measured LFP-like extracellular fields at
  layer 5 pyramidal somata. Fields of 0.7–6 mV/mm induced membrane
  oscillations under 0.5 mV, undiminished to 100 Hz. With spiking driven
  by current injection, the fields left spike counts unchanged but shifted
  spike timing: phase locking was significant at 1 Hz from 0.74 mV/mm, at
  8 Hz, and at 30 Hz only for the largest field. Up to four nearby neurons
  were synchronized by a common field. The authors explain the effect by
  Kirchhoff's circuit laws and a threshold model.
---

# LIT-tmp4kcgq: Ephaptic coupling of cortical neurons

Anastassiou, C. A., Perin, R., Markram, H., Koch, C. (2011). Ephaptic coupling of cortical neurons. *Nature Neuroscience, 14(2), 217-223*. doi:10.1038/nn.2727.

## Key takeaways

- Ephaptic coupling at physiological strengths changes when neurons fire,
  not whether they fire: membrane effects under 0.5 mV, no extra spikes,
  phase locking to slow fields.
- Slow fields work best. Entrainment was strongest at 1 Hz, weaker at 8 Hz,
  and at 30 Hz needed fields nearly ten times larger.
- The fields were applied by an electrode. The paper shows neurons respond
  to fields of the LFP's size, not that the fields neurons generate feed
  back on them in vivo.

## Standing in the record

Registered as Jennings's evidence against weak emergence (LIT-tmpasemk, p.
35). The paper supports her quotation, that "groups of cells change their
local electric environment, which in turn feeds back onto the electric
activity of all of its members" (p. 217). It does not support her
inference, that "brain activity cannot be described simply through local
interactions": the authors call the potentials "a simple consequence of
Kirchhoffs' circuit laws" (p. 221). It is also the second appearance of
ephaptic coupling in the record, after LIT-388's hypothesis about sentience,
on which it is silent.
