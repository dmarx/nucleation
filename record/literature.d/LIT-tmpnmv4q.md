---
status: Active
status_note: >-
  read in full 2026-10-22 ([NOTE-tmpkgdyu](../notes.d/NOTE-tmpkgdyu.md)) from the publisher's open-access
  version of record (CC BY 4.0); worth reading as the cross-species,
  causal extension of the same group's synergistic-workspace result
  ([LIT-949](LIT-949.md)): pairwise integrated information ΦR from resting fMRI falls
  under anaesthesia in humans, macaques, marmosets and mice and returns
  with responsiveness, including when central thalamic stimulation
  re-awakens two anaesthetized macaques, and it tracks arousal better than
  the original Φ, causal density or functional connectivity. Its main
  limit is the target: behavioural responsiveness, which the authors call
  "presumably consciousness" and an "imperfect marker". It is also
  pairwise, linear-Gaussian, at rest and content-free, and the causal arm
  rests on two animals. The PVALB and modelling results are correlational
  and model-bound. Filed as [THEORY-tmpvpggv](../theory.d/THEORY-tmpvpggv.md).
title: 'Convergent transcriptomic and connectomic controllers of information integration and its anaesthetic breakdown across mammalian brains'
version: 2
history:
- version: 1
  date: '2026-10-21'
  note: >-
    Filed, not read. Citation checked against Crossref on 2026-10-21: Nature
    Human Behaviour 10(4): 777–802. `published:` is Crossref's online date,
    28 January 2026, which PubMed also gives. No preprint of this study was
    found; the group's bioRxiv "Comprehensive profiling of anaesthetised
    brain dynamics across phylogeny" (2025) is a different study.
- version: 2
  date: '2026-10-22'
  note: >-
    Read in full in NOTE-tmpkgdyu from the publisher's PDF, which
    Unpaywall and OpenAlex list as hybrid open access under CC BY
    (www.nature.com/articles/s41562-025-02381-5.pdf, 37 PDF pages: journal
    pages 777–802, Extended Data Figs. 1–4, Reporting Summary). The paper
    gives received 2 February 2025, accepted 14 November 2025, published
    online 28 January 2026, which confirms `published:`. Unpaywall also
    lists a submitted version on HAL (hal-05482107) and the Copenhagen
    repository; neither was used. The Supplementary Information was not
    read. Status Deferred to Active. The summary is corrected: humans had
    one anaesthetic (sevoflurane), not several; the medetomidine–isoflurane
    mouse regimen is an exception in the main analysis; the thalamic
    reversal rests on two macaques; and the PVALB relation is cortical
    only. The "Not read" paragraph is replaced by Key takeaways.
    THEORY-tmpvpggv filed.
tags:
- consciousness
- neuroscience
- information-theory
date: '2026-10-21'
published: '2026-01-28'
doi: '10.1038/s41562-025-02381-5'
first_author: 'Luppi'
keywords:
- 'information integration'
- 'integrated information decomposition'
- 'anaesthesia'
- 'cross-species neuroimaging'
- 'thalamic deep-brain stimulation'
- 'network control'
- 'PVALB'
implementations: []
summary: >-
  Luppi et al. (2026), Nature Human Behaviour 10(4):777–802. Revised
  integrated information ΦR, computed pairwise from resting-state fMRI by
  integrated information decomposition and averaged over region pairs,
  falls under anaesthesia in humans (sevoflurane, n = 15), macaques,
  marmosets and mice, with medetomidine–isoflurane in the mouse the
  exception in the main analysis. It returns on spontaneous recovery in
  humans, and when central thalamic stimulation restores arousal in two
  propofol-anaesthetized macaques. Network control energy rises under
  anaesthesia and correlates negatively with ΦR. Regional ΦR loss is
  largest in unimodal cortex and follows cortical PVALB expression in
  human, macaque and mouse. Species-specific mean-field models reproduce
  the PVALB effect and the advantage of central over ventrolateral
  thalamic stimulation. The target is behavioural responsiveness.
---
<!-- inactive-ok-file: THEORY-tmpvpggv — Proposed; filed from this reading, named -->
<!-- inactive-ok-file: THEORY-240 THEORY-091 — Proposed; accounts this reading bears on, named, not leaned on -->
<!-- inactive-ok-file: CLAIM-tmpdga80 CLAIM-tmp1lvwf TERM-tmpgqmop — Proposed; the batch's claims and term, cited as open -->

# LIT-tmpnmv4q: Convergent transcriptomic and connectomic controllers of information integration and its anaesthetic breakdown across mammalian brains

Luppi, A. I., Uhrig, L., Tasserie, J., Mediano, P. A. M., Rosas, F. E., Singleton, S. P., Gutierrez-Barragan, D., Gini, S., Castro, P., Signorelli, C. M., Golkowski, D., Ranft, A., Ilg, R., Jordan, D., Muta, K., Hata, J., Okano, H., Liu, Z.-Q., Yee, Y., Destexhe, A., Cofre, R., Menon, D. K., Gozzi, A., Jarraya, B. & Stamatakis, E. A. (2026). Convergent transcriptomic and connectomic controllers of information integration and its anaesthetic breakdown across mammalian brains. *Nature Human Behaviour* 10(4): 777–802. doi:10.1038/s41562-025-02381-5.

## Key takeaways

*From the reading, [NOTE-tmpkgdyu](../notes.d/NOTE-tmpkgdyu.md).*

- **The measure.** ΦR is the original whole-minus-sum Φ with the
  persistent redundancy added back, since the naive sum of the parts
  counts it twice. It is the synergy-containing atoms of integrated
  information decomposition plus the two pure-transfer atoms, computed
  per region pair and averaged (pp. 778–779, 795–796).
- **It falls with responsiveness.** Lower under anaesthesia in four
  species and five of six regimes, with medetomidine–isoflurane in the
  mouse the exception (p. 781), which a six-region check recovers
  (p. 791). It returns on recovery in humans.
- **It returns with thalamic stimulation.** In two macaques under
  continuous propofol, central thalamic stimulation restored arousal and
  ΦR, so ΦR "co-varies with the consciousness-suppressing effect of
  anaesthetics, not with their mere presence in the system" (p. 781).
  Low-intensity stimulation of the control site raised ΦR somewhat
  without restoring arousal.
- **It beats the rivals.** It carries 51% of the explained variance in the
  macaque arousal score. The original Φ is inconsistent and goes
  negative; causal density misses recovery (pp. 781–782, 790–791).
- **Controllability.** The energy to move between successive brain states
  rises under anaesthesia and correlates negatively with ΦR (pp. 782–784).
- **Where and why.** The largest regional losses are in unimodal visual
  and somatomotor cortex, with default-mode losses too (p. 784). They
  follow cortical PVALB expression in three species (pp. 784–786), and
  models show PVALB-shaped inhibition is especially suited to lowering ΦR
  (pp. 787–789).
- **What the authors concede.** Responsiveness is "an imperfect marker of
  unconsciousness" (p. 792); pairwise ΦR is "perhaps best viewed as a
  lower bound" (p. 793); "the consistency was not perfect" (p. 793).

## Why this is here

The owner's exchange of 2026-10-21, "Experience and interpretation", asked whether experience is constituted by interpretation or produced by it. The exchange cited this study for its finding across four species that integration breaks down under anaesthesia, and that thalamic stimulation reverses the breakdown in macaques. The reading confirms that description, with two qualifications: the reversal rests on two macaques, and what breaks down is a content-free statistical integration that goes with responsiveness, not interpretation in [TERM-tmpgqmop](../terms.d/TERM-tmpgqmop.md)'s sense. It measures integration, not the constitution of experience. The record holds the same group's synergistic workspace paper, [LIT-949](LIT-949.md), which this one cites as ref. 45; it half meets [THEORY-240](../theory.d/THEORY-240.md)'s promotion test, restoring ΦR by thalamic stimulation without showing that the restored ΦR is on the gateway side. Bears on [QUESTION-048](../questions.d/QUESTION-048.md), as deficit-and-recovery evidence whose marker is access, and on [CLAIM-tmpdga80](../claims.d/CLAIM-tmpdga80.md) and [CLAIM-tmp1lvwf](../claims.d/CLAIM-tmp1lvwf.md), where integration is one candidate condition. Filed from this reading: [THEORY-tmpvpggv](../theory.d/THEORY-tmpvpggv.md). It carries no instruction for machine-learning practice.
