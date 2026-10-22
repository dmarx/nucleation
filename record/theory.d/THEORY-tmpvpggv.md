---
status: Proposed
promote_when: >-
  An independent replication, on new data, that pairwise or higher-order
  ΦR from resting-state recordings falls under anaesthesia and returns
  with responsiveness in at least two species, with the human arm using a
  drug other than sevoflurane, and the causal arm (thalamic or other
  stimulation that restores responsiveness under continued anaesthetic)
  run in more than two animals with a stimulated control site in more
  than one. It would be strengthened by a dissociation the account must
  survive: ΦR preserved in a state that is unresponsive but shown to be
  conscious (ketamine dreaming with later report, or covert awareness by
  command-following imagery), or lowered in one that is responsive. It is
  in trouble if ΦR falls just as much in such disconnected but conscious
  states as in unconscious ones, which would make it a marker of
  responsiveness only, or if another redundancy function or a
  partition-minimizing ΦR reverses the contrast. More resting-state
  contrasts from the same datasets cannot settle it, nor can model
  simulations.
title: "Across humans, macaques, marmosets and mice, loss of behavioural responsiveness under anaesthesia goes with lower whole-brain pairwise integrated information ΦR in resting fMRI, and its return goes with ΦR's return, including when central thalamic stimulation restores responsiveness during continued anaesthesia; ΦR tracks the macaque arousal score better than the original Φ, causal density, net information flow or functional connectivity"
version: 1
tags:
- consciousness
- neuroscience
- information-theory
date: '2026-10-22'
source:
- LIT-tmpnmv4q
- LIT-949
summary: >-
  Luppi et al. (2026), [LIT-tmpnmv4q](../literature.d/LIT-tmpnmv4q.md), read in full in [NOTE-tmpkgdyu](../notes.d/NOTE-tmpkgdyu.md) from the
  open-access version of record. It extends the same group's 2024 result
  ([LIT-949](../literature.d/LIT-949.md), [THEORY-240](THEORY-240.md)) from human propofol and disorders of consciousness
  to four species and six regimes, and adds a causal reversal in two
  macaques. The sharp edge: the state measured is responsiveness, which
  the authors call "presumably consciousness" and grant is "an imperfect
  marker of unconsciousness"; the measure is pairwise, linear-Gaussian
  and content-free; and one mouse regimen fails the main analysis.
---
<!-- inactive-ok-file: THEORY-240 THEORY-091 THEORY-063 THEORY-497 — Proposed; accounts this one is set beside, not leaned on -->
<!-- inactive-ok-file: CLAIM-tmpdga80 CLAIM-tmp1lvwf — Proposed; the batch's claims, cited as open -->

# THEORY-tmpvpggv: Across humans, macaques, marmosets and mice, loss of behavioural responsiveness under anaesthesia goes with lower whole-brain pairwise integrated information ΦR in resting fMRI, and its return goes with ΦR's return, including when central thalamic stimulation restores responsiveness during continued anaesthesia; ΦR tracks the macaque arousal score better than the original Φ, causal density, net information flow or functional connectivity

## Source

Luppi, Uhrig, Tasserie et al. (2026), *Nature Human Behaviour* 10(4),
[LIT-tmpnmv4q](../literature.d/LIT-tmpnmv4q.md), read in full in [NOTE-tmpkgdyu](../notes.d/NOTE-tmpkgdyu.md): Figs. 2–4 and their text
(pp. 778–784), the robustness section (pp. 790–791), the Discussion's
limitations (pp. 792–793), and Methods on ΦR (pp. 795–796). The
Supplementary Information was not read. Second source: Luppi et al.
(2024), [LIT-949](../literature.d/LIT-949.md), the human propofol and disorders-of-consciousness result
that this one extends.

## What was actually shown

- **The measure.** For each pair of regions, ΦR = Φ2008 + Red→Red: the
  information the pair's past carries about its joint future, minus each
  region's information about its own future, plus back the persistent
  redundancy that the naive sum counts twice. It is computed with the
  Gaussian minimum-mutual-information redundancy and averaged over all
  pairs (pp. 779, 795–796).
- **The fall.** Mean ΦR is lower under anaesthesia than awake in humans
  (sevoflurane, n = 15), macaques (sevoflurane, propofol, ketamine; five
  animals), marmosets (sevoflurane, propofol, isoflurane; four animals)
  and mice (halothane), "except for medetomidine–isoflurane in the mouse"
  (p. 781). A six-region bipartition version also finds the
  medetomidine–isoflurane fall (p. 791).
- **The return.** Human ΦR rises again on spontaneous recovery. In two
  macaques under continuous propofol, central thalamic stimulation at 3 V
  and 5 V restored arousal and raised ΦR. High-intensity stimulation of the
  ventrolateral thalamus, one animal, restored neither (p. 781).
- **Against rival measures.** In a dominance analysis of the macaque
  arousal score, ΦR carries 51% of the explained variance (R² = 0.57),
  and 46% with functional connectivity added (15%). Φ2008 does not track
  anaesthesia consistently and goes negative; causal density misses
  recovery (pp. 781–782, 790–791).

What could have come out otherwise: ΦR could have stayed up under some
drug, or in some species; it could have stayed down when stimulation
restored arousal under continued propofol, which would have tied it to
the drug, not to the state; and one of the rival measures could have
tracked arousal as well. Apart from the one mouse regimen in the main
analysis, none of these happened.

## What this does not say

- **Not that ΦR tracks experience.** The target is responsiveness. The
  authors: "Behavioural unresponsiveness is an imperfect marker of
  unconsciousness since it can also occur as a result of sensory
  disconnection or motor impairment, neither of which is the same as
  unconsciousness" (p. 792). No condition here separates the two.
- **Not that ΦR is integrated information in IIT's sense.** The authors'
  intention is "'not' to test integrated information theory" (p. 796).
  ΦR is a pairwise, linear-Gaussian whole-minus-sum quantity, a "lower
  bound" in their words (p. 793).
- **Not a regional claim.** The averaged ΦR says nothing about which
  regions carry the change. The regional maps put the largest losses in
  unimodal visual and somatomotor cortex, with default-mode losses too
  (p. 784). So this THEORY does not carry [THEORY-240](THEORY-240.md)'s gateway claim.
- **Not that low ventrolateral stimulation is null.** It raised ΦR, less,
  without restoring arousal (p. 781). The account tolerates this only if
  a partial rise below the behavioural threshold is allowed, which the
  authors propose and do not test.
- **Not the mechanism.** The PVALB correlations and the models are left
  out. They show sufficiency within models, not how anaesthetics act.
- **Not about contents.** Resting state, no stimulus, no report. Nothing
  here concerns what is integrated or for whom.

## Connections

No `answers:` relation is declared. The question this bears on most,
[QUESTION-048](../questions.d/QUESTION-048.md), asks what such evidence can establish about experience as
opposed to access, and this result is about responsiveness, so it adds a
case to that question without answering it. It is [THEORY-091](THEORY-091.md)'s limit
again: a capacity lost with consciousness is lost with access too.

- **[THEORY-240](THEORY-240.md)** is the regional, gateway-side claim from [LIT-949](../literature.d/LIT-949.md). This
  THEORY is the whole-brain claim it rests beside, now cross-species and
  with a causal arm. It half meets [THEORY-240](THEORY-240.md)'s promotion test (restoration
  by thalamic stimulation) without the regional half.
- **[THEORY-063](THEORY-063.md)**'s promotion test asks for a computed integration measure
  across anaesthesia. ΦR is one, but it measures the amount of pairwise
  integration, not the presence of one dominant cluster.
- **[THEORY-497](THEORY-497.md).** ΦR is mostly synergy-containing atoms, so this is a fall
  in the synergy [THEORY-497](THEORY-497.md) describes, under the same redundancy choice.
- **[CLAIM-tmpdga80](../claims.d/CLAIM-tmpdga80.md)** and **[CLAIM-tmp1lvwf](../claims.d/CLAIM-tmp1lvwf.md).** Integration is one of the
  candidate conditions the exchange named. This gives it a measured form
  that falls with responsiveness. It is not a measure of interpretation,
  and it gives no case that separates conscious from unconscious
  processing within a waking brain.
