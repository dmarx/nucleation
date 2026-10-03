---
status: Active
status_note: 'read in full 2026-10-03 ([NOTE-tmp9rypf](../notes.d/NOTE-tmp9rypf.md)); worth reading as single-unit evidence that brief co-occurring ~90 Hz ripples in distant human forebrain sites (up to about 220 mm, across hemispheres) mark windows of raised cross-region co-firing, about 30% above no-ripple periods and beyond what firing rates alone predict, that this scales with working-memory load, and that stimulus-specific co-firing from encoding recurs more often inside co-ripples at retrieval, most of all on fast trials. One reanalysed open dataset (35 patients, one Sternberg task, load 1 versus 3), clinically placed electrodes, and correlational throughout: nothing perturbs the ripples.'
title: 'Cross-region neuron co-firing mediated by ripple oscillations supports distributed working memory representations'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read in full from the publisher's open-access PDF (CC BY-NC-ND 4.0,
    https://www.nature.com/articles/s41593-026-02403-z.pdf, 33 pages
    including Extended Data). Main text, Figs. 1–6, Discussion, Methods
    and the Extended Data captions read; figure panels read from captions
    and text, since the text layer does not recover plotted data.
    Crossref confirms authors, Nature Neuroscience 29(10):2566–2577,
    online 12 August 2026. A bioRxiv preprint (10.1101/2025.09.04.674061,
    v1 6 September 2025, four authors, without Cheng) exists and was not
    read; `published:` is the journal's online date, as for LIT-615. Not
    held in the Anthology of the SOTA: a grep of its record for the DOI,
    "Verzhbinsky" and the title found nothing.
tags:
- neuroscience
- cognition
- network-science
date: '2026-10-03'
published: '2026-08-12'
doi: '10.1038/s41593-026-02403-z'
first_author: 'Verzhbinsky'
keywords:
- 'ripple oscillations'
- 'co-ripples'
- 'co-firing'
- 'working memory'
- 'Sternberg task'
- 'single units'
- 'intracranial recordings'
- 'reinstatement'
- 'long-range synchrony'
- 'coupled oscillators'
implementations: []
summary: >-
  Verzhbinsky, Daume, Cheng, Rutishauser & Halgren (2026), Nature
  Neuroscience 29:2566–2577. In 1,373 single units from hippocampus,
  amygdala, vmPFC, ACC and preSMA of 35 epilepsy patients doing a
  Sternberg task, ripples (70–100 Hz) co-occur between bundles up to about
  220 mm apart with no decline beyond the local bundle, and cross-region
  unit co-firing rises about 30% during co-ripples. That rise exceeds a
  rate-only null (STTC 117% higher), grows with memory load, and
  co-ripples hold more repetitions of a stimulus's encoding co-firing at
  retrieval, more on fast trials.
---

<!-- inactive-ok-file: LIT-385 — Deferred: Damasio's convergence-zone proposal is unread; named as the older account this finding resembles, no relation claimed -->
<!-- inactive-ok-file: THEORY-063 — Proposed; named as the record's account of unity this work does not test, no support claimed -->
<!-- inactive-ok-file: LIT-tmpqw727 — Deferred, paywalled; the traveling-wave review filed in the same batch, named for contrast, not leaned on -->

# LIT-tmp8o0fr: Cross-region neuron co-firing mediated by ripple oscillations supports distributed working memory representations

Ilya A. Verzhbinsky, Jonathan Daume, Sophia Cheng, Ueli Rutishauser and Eric Halgren (2026), *Nature Neuroscience* 29(10):2566–2577 — DOI-10.1038/s41593-026-02403-z

## Key takeaways

- Ripples, brief (about 70 ms) oscillations near 90 Hz, occur at about 0.5 per second in all five recorded regions. Between bundles they co-occur at a median 5%, and that rate barely changes with fibre-tract distance from 71 to 223 mm, ipsilateral or contralateral. Unit pairs co-fire (spikes within 25 ms) a median 34% more during co-ripples than when neither site ripples, about as much for distant pairs as for pairs in one bundle.
- The extra co-firing is not just extra spikes. Against an independent-firing null it is 56% higher during co-ripples than during no-ripple periods, and the rate-corrected spike time tiling coefficient is 117% higher (Extended Data Fig. 3).
- Co-rippling and co-ripple co-firing scale with load. Load 3 versus load 1 raises co-ripple co-firing 13% in maintenance and 19% at retrieval, against about zero in no-ripple periods (Fig. 5). Ripple-band co-occurrence is load-modulated in 12 of 15 region pairs at retrieval, low gamma in 2 and non-oscillatory very high gamma in none (Fig. 3).
- At retrieval, a cell pair that co-fired when a stimulus was encoded co-fires again for that stimulus in 0.29% of cell-pair trials during co-ripples against 0.14% in duration-matched no-ripple periods. On load 3 match trials the rate is 0.36% for fast responses and 0.23% for slow ones (Fig. 6).

## Standing in the record

Filed on 2026-10-03 at the owner's request, in a batch of four works on
large-scale neural dynamics: this paper, the spiral-wave study of Xu et
al. ([LIT-tmpkkvdo](LIT-tmpkkvdo.md)), the traveling-wave review of Muller et al.
([LIT-tmpqw727](LIT-tmpqw727.md)) and Vishne et al. on sustained perception ([LIT-tmppqcvc](LIT-tmppqcvc.md)).
No anthology topic holds a study of human single units, and it carries no
instruction for machine-learning practice.

It is the batch's mechanism for coordination by *synchrony*: brief,
zero-lag-coupled bursts at distant sites, with timing and not direction
of travel as the carrier. Xu et al. and Muller et al. put the carrier in
*propagation* instead, waves whose phase gradient moves across a sheet of
cortex. The record holds no paper that sets the two against each other,
and this one does not test propagation.

Its strongest bearing on the record is on accounts that need distributed
neuronal integration. The authors themselves say the "general lack of
evidence for integration of neuronal firing over wide expanses of
association cortex" has been a serious challenge to workspace-type
theories, and offer this as evidence for "an essential component of that
process" (Discussion). That is a claim about working memory, not about
experience. It bears on [THEORY-063](../theory.d/THEORY-063.md), which takes the unity of experience to
be the integration of one global world-model into a single functional
cluster, only in showing that one candidate integrating mechanism exists
at the single-neuron level. Nothing here measures whether co-ripples go
with experience being unified, so no support is claimed.

The retrieval result reads as a measured version of the older proposal
in Damasio's convergence-zone paper ([LIT-385](LIT-385.md), unread), that recall is the
time-locked re-enactment across regions of the activity laid down at
encoding. The paper does not cite Damasio, so this is my connection, and
[LIT-385](LIT-385.md) is unread, so no relation is declared.

Its coupled-oscillator reading, distant sites locking at zero lag despite
long conduction delays because several pathways join them, is argued in
the Discussion from cited models and is not tested here. That is the
`network-science` question of synchronization; the record's nearest
treatment of coupled phase oscillators is Kelso's account of HKB and its
Kuramoto generalization ([LIT-601](LIT-601.md)), which concerns relative phase in
coordination, not ripple co-occurrence, and no relation is claimed.

No relation is declared. The paper compares itself with earlier
LFP-only and short-range co-ripple studies, none of which the record
holds.
