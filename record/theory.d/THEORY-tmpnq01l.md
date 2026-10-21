---
status: Active
title: 'In Bala–Goyal network models of unbiased scientists testing a slightly better new action, a propagandist who forwards to Bayesian policy makers only those real results that favour the worse action can leave the policy makers near-certain of the false theory while the scientists converge on the true one; the effect weakens as the policy makers hear more scientists, as the better action''s advantage grows and as each study gets larger'
version: 1
history:
- version: 1
  date: '2026-10-21'
  note: >-
    Filed Active from NOTE-tmp8rwaa, under ADR-047 v3: the title claims no
    more than Weatherall, O'Connor and Bruner's simulations measured, the
    NOTE read the paper in full, and nothing in the record contradicts it.
    The record also re-ran the selective-sharing model from the paper's
    description and found the same direction for each trend; the numbers
    are below.
tags:
- epistemology
- network-science
- philosophy-of-science
date: '2026-10-21'
source:
- LIT-tmpx95z2
answers:
- QUESTION-047
summary: >-
  Weatherall, O'Connor and Bruner (2020; arXiv 2018), LIT-tmpx95z2, read in
  NOTE-tmp8rwaa. No result is fabricated and no scientist is biased; the
  audience is misled because it updates on a selected sample as if it were
  not selected. It is a property of a stylized model, which the authors
  call "how-potentially"; it does not show that any real audience was
  misled this way, nor that an audience aware of the selection would be.
---
<!-- inactive-ok-file: CLAIM-tmpjo2zr THEORY-143 THEORY-146 — Proposed; the claim and accounts this model bears on, cited as open -->
<!-- inactive-ok-file: LIT-751 — Unavailable; Holman and Bruner's unread model, named for contrast -->

# THEORY-tmpnq01l: In Bala–Goyal network models of unbiased scientists testing a slightly better new action, a propagandist who forwards to Bayesian policy makers only those real results that favour the worse action can leave the policy makers near-certain of the false theory while the scientists converge on the true one; the effect weakens as the policy makers hear more scientists, as the better action's advantage grows and as each study gets larger

## Source

Weatherall, O'Connor and Bruner (2020), *BJPS* 71(4), LIT-tmpx95z2, read in
full in NOTE-tmp8rwaa from the arXiv manuscript of August 2018: §3 and its
Figs 2–4.

## What was actually shown

K scientists on a cycle or complete network choose between action A
(success .5, known) and B (.5 + ε, believed .5 ± ε), play B when their
credence in it exceeds .5, run n trials a round and update by Bayes on their
own and their neighbours' results. Policy makers, initially sceptical
(credence uniform on (0, .5)), listen to k scientists and gather nothing.
The propagandist forwards to every policy maker each round's results that
favour A. Runs end at a scientific consensus; those ending in the wrong one
are discarded.

The paper's finding: "while the community of scientists converges on true
beliefs about the world, the policy makers reach near certainty in the
false belief", over many parameter settings, with the effect weaker for
larger k (Fig. 2), larger ε (Fig. 3) and larger n (Fig. 4). Each
comparison could have come out the other way: an audience that hears every
real result might have tracked the community, and larger studies might
have yielded more ammunition rather than less.

**Re-run here,** from the paper's description, 100 runs a setting unless
stated (policy makers' mean final credence in the true theory, B):

| setting | no propagandist | propagandist |
|---|---|---|
| cycle, K = 20, n = 10, p_B = .55, k = 1 | 0.873 | 0.000 |
| same, k = 5 | 1.000 | 0.000 |
| same, k = 10 | 1.000 | 0.039 |
| same, k = 20 | 1.000 | 0.938 |
| complete, K = 10, k = 9, p_B = .55, n = 5 (60 runs) | 0.980 | 0.247 |
| same, n = 20 | 0.988 | 0.755 |
| same, n = 100 | 0.995 | 0.989 |
| cycle, K = 20, n = 10, k = 10, p_B = .51 / .6 / .7 (40 runs, with propagandist) | | 0.000 / 0.981 / 1.000 |

The re-implementation's own choices, not fixed by the paper: each policy
maker hears k scientists drawn at random once per run; scientists update on
each neighbour's result in turn within a round; there are ten policy
makers; a run is capped at 20,000 rounds. Every trend has the paper's
direction. The values are this re-implementation's, not the paper's, whose
plotted values were not seen.

## What this does not say

- **Not that real audiences were misled this way.** The authors: "modeling
  alone cannot establish that this did happen in the case of tobacco
  industry propaganda efforts."
- **Not that a Bayesian who knows of the selection is misled.** The policy
  makers treat forwarded results as unselected draws. A receiver who models
  the sender is THEORY-404's case, a different result.
- **Not that the effect holds whatever the parameters.** It fades when the
  problem is easy, studies are large or the audience hears most scientists.
- **Not about influence on the scientists.** The propagandist never touches
  them; that is Holman and Bruner's setting (LIT-744, LIT-751).
- **Not that more scientists always help or always hurt.** With k fixed,
  more scientists supply more spurious results, "often" but "not always"
  worsening the audience's belief.

## Connections

- **CLAIM-tmpjo2zr.** Its evidence route, with genuine results selected and
  no fabrication, in a model; distinct from THEORY-404's committed design
  and THEORY-146's selective funding.
- **THEORY-tmpg79sv.** The same model's biased-production treatment, and the
  sufficient statistic that explains both.
- **THEORY-143.** The Zollman effect concerns the community's learning; with
  an audience and a propagandist, slow consensus can cost the audience
  (NOTE-tmp8rwaa).
- **QUESTION-047: answers in part.** The audience settles on a belief none of
  the inquirers reasoned to, through selection of their honest outputs.
