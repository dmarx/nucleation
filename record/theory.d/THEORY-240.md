---
number: 240
status: Proposed
formerly:
- THEORY-tmp2cqie
promote_when: >-
  An independent replication, on new propofol and disorders-of-consciousness
  data, of the shared decrease in pairwise ΦR between medial prefrontal
  and posterior default-mode regions, with gateway and broadcaster classes
  derived afresh, and with the shared-effect test published in full. The
  account is strengthened if the same asymmetry appears with a directed
  decomposition or in task data with report, and if restoring
  consciousness by intervention (central thalamic stimulation, for
  example) restores gateway ΦR. It is in trouble if the decrease
  disappears in other cohorts or other anaesthetics, or if it tracks
  sedation or responsiveness rather than consciousness: for example, if
  it is present in disconnected but conscious participants, or absent in
  unresponsive patients shown to be covertly aware. What cannot settle
  it: more resting-state contrasts from the same datasets, or the
  non-robust increases.
title: 'Loss of consciousness under propofol and in chronic disorders of consciousness goes with reduced pairwise integrated information between default-mode regions that rank as gateways of a synergy-defined workspace, not between its broadcasters'
version: 1
tags:
- consciousness
- neuroscience
- information-theory
date: '2026-10-14'
source:
- LIT-949
summary: >-
  Luppi et al. (2024), [LIT-949](../literature.d/LIT-949.md), read in [NOTE-799](../notes.d/NOTE-799.md). In resting-state
  fMRI, the regions where synergistic interactions outrank redundant ones
  split by rank into gateways (mainly default mode) and broadcasters
  (mainly fronto-parietal). Pairwise ΦR, the whole-minus-sum Φ plus
  redundancy, falls between default-mode gateways in propofol
  anaesthesia, in 22 DOC patients, and against post-anaesthetic recovery.
  The original Φ shows no common decrease. The finding is correlational,
  pairwise and content-free. The gateway/broadcaster split is imposed by
  the method; only where its two classes fall is measured.
---
<!-- inactive-ok-file: QUESTION-061 CLAIM-003 THEORY-096 THEORY-098 — Deferred or Proposed; the set-aside question and claim this bears on, and the accounts it is compared with, cited as open -->

# THEORY-240: Loss of consciousness under propofol and in chronic disorders of consciousness goes with reduced pairwise integrated information between default-mode regions that rank as gateways of a synergy-defined workspace, not between its broadcasters

## Source

Luppi, Mediano, Rosas et al. (2024), *eLife* 12:RP88173, [LIT-949](../literature.d/LIT-949.md), read
in [NOTE-799](../notes.d/NOTE-799.md): Results (Figs. 2, 4, 5 and their robustness
analyses), Discussion and its limitations, and Methods (Eqs. 4–8, the
participation-coefficient split, and the network-based statistic with the
composite shared-effect test).

## What was actually shown

**The workspace and its two sides (HCP, N = 100).** Pairwise synergy and
redundancy were computed between 454 regions with Gaussian MMI-ΦID.

- **Workspace.** The regions whose synergy rank exceeds their redundancy
  rank by nodal strength. This definition is taken from the authors'
  earlier paper.
- **The split.** Within the workspace, regions whose participation
  coefficient ranks higher for synergy than for redundancy are gateways;
  the rest are broadcasters.
- **The measured result.** Gateways lie mainly in the default mode
  network, and broadcasters mainly in the executive control network,
  with lateral prefrontal cortex prominent. This replicates at a second
  parcellation and with data-driven modules.

**The consciousness contrast.** Pairwise
ΦR = I(past; future) − I(X_past; X_future) − I(Y_past; Y_future) + Red
was compared across three contrasts:

- propofol at Ramsay 5 against pre-induction wakefulness;
- propofol against post-anaesthetic recovery;
- 22 DOC patients against awake controls.

A shared-effect test required all three contrasts to change. The
edges whose ΦR consistently fell link bilateral precuneus, medial
prefrontal and inferior parietal cortex, with some left temporal cortex.
All of these regions are gateways in the HCP classification. The
decreases in medial prefrontal and posterior cingulate or precuneus
survive a coarser parcellation and stricter thresholds. The net sum of
F-scores over significant edges is −25.37.

**What could have failed.** The consistent decreases could have fallen
on broadcasters, or on no workspace region. The original whole-minus-sum
Φ, on the same data, found no common decrease at all.

## What this does not say

- **Not that consciousness is gateway integration.** The authors
  disclaim that ΦR "represent[s] a direct cause of consciousness, or
  [is] identical to it". The result is a correlation in resting-state
  BOLD.
- **Not that the workspace has an input side and an output side.** Every
  workspace region is assigned to one class by the sign of a relative
  rank difference, so a two-part workspace is guaranteed by the method.
  What is measured is where the classes fall and which class carries the
  change.
- **Not anything about the access of a content.** No stimulus, report or
  per-consumer measure is involved. It cannot show that a content reaches
  some systems and not others, the result [QUESTION-061](../questions.d/QUESTION-061.md) asks for.
- **Not that broadcasters gain integration in unconsciousness.** The
  increases near lateral prefrontal cortex are not robust: "no region
  consistently showing increases".
- **Not IIT's Φ.** The measures are pairwise between regional time series,
  undirected, and built on IIT 2.0's Φ. They are not the integrated
  information of the whole system.
- **Not a clean contrast of conscious and unconscious states.** The DOC
  group includes minimally conscious patients. The authors concede that
  some propofol participants may have been "disconnected but still
  conscious". Resting state may overweight the DMN against the FPN.
- **Not fully specified.** The shared-effect test's details are deferred
  to a future publication. The propofol sample is given as both N = 15
  and n = 16.

## Connections

- **[QUESTION-061](../questions.d/QUESTION-061.md)** (Deferred). The result bears on the question only by
  showing that, at rest, the workspace is not uniform with respect to the
  state of consciousness: the consistent loss is on the input side. It is
  not evidence about content access. No `answers:` relation is filed.
- **[THEORY-096](THEORY-096.md)** (GNW). It agrees that lateral prefrontal cortex acts as a
  broadcaster. It locates the consciousness-tracking change in default-mode
  gateways instead, and it does not test ignition or exclusivity.
- **[THEORY-098](THEORY-098.md).** The reductions under propofol in thalamic, auditory and
  somatomotor regions fit the authors' reading of thalamocortical
  isolation: a loss of input to the core. That is a state effect, and it
  does not bear on sensory recurrence as the basis of experience.
- **[CLAIM-003](../claims.d/CLAIM-003.md)** (Deferred). It does not bear: the measure is undirected and
  content-free.
- **[LIT-025](../literature.d/LIT-025.md)** reviews the ΦID framework whose pairwise measures are used
  here.
