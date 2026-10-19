---
number: 623
status: Active
formerly:
- THEORY-tmpr96be
title: "In the two tests of contextuality in language data that the record has read, the contextuality is put there by the experimenter or not secured: meaning-selection models of ambiguous phrases estimated from corpora are all signalling and their two Contextuality-by-Default verdicts are plausibly noncontextual by their own bootstrap, while BERT's 52 million anaphora models have a support fixed by the sentence schema, so whether each counts as contextual depends only on how uncertain the model's three referent choices are"
version: 1
tags:
- contextuality
- linguistics
- pragmatics
date: '2026-10-16'
source:
- LIT-844
- LIT-842
summary: >-
  Lo, Sadrzadeh & Mansfield (2024), [LIT-844](../literature.d/LIT-844.md), read in [NOTE-648](../notes.d/NOTE-648.md), and Wang,
  Sadrzadeh, Abramsky & Cervantes (2021), [LIT-842](../literature.d/LIT-842.md), read in [NOTE-645](../notes.d/NOTE-645.md). Both
  readings recomputed the criteria. That 71.1% CbD-contextual measures
  BERT's uncertainty is [NOTE-648](../notes.d/NOTE-648.md)'s derivation from the stipulated support
  (CNT1 = 2 − Δ). The only possibilistically contextual phrase model has
  hand-set supports. Neither study uses human judgements, so neither
  bears on whether people's interpretations are contextual.
---

<!-- inactive-ok-file: THEORY-013 — Proposed; the account these studies bear on and the follow-up's account, cited as open -->
<!-- inactive-ok-file: CLAIM-009 CLAIM-037 CLAIM-044 — Proposed; named for what these readings bear on, cited as open -->

# THEORY-623: In the two tests of contextuality in language data that the record has read, the contextuality is put there by the experimenter or not secured: meaning-selection models of ambiguous phrases estimated from corpora are all signalling and their two Contextuality-by-Default verdicts are plausibly noncontextual by their own bootstrap, while BERT's 52 million anaphora models have a support fixed by the sentence schema, so whether each counts as contextual depends only on how uncertain the model's three referent choices are

## Source

Lo, Sadrzadeh & Mansfield (2024), "Quantum-Like Contextuality in Large
Language Models", arXiv 2412.16806v1, [LIT-844](../literature.d/LIT-844.md), read in full in [NOTE-648](../notes.d/NOTE-648.md).
Wang, Sadrzadeh, Abramsky & Cervantes (2021), "On the Quantum-like
Contextuality of Ambiguous Phrases", [LIT-842](../literature.d/LIT-842.md), read in full in [NOTE-645](../notes.d/NOTE-645.md),
with its journal follow-up for comparison.

## What was actually shown

**Ambiguous phrases ([LIT-842](../literature.d/LIT-842.md)).** Each ambiguous word is a measurement,
its selected meaning the outcome, a two-word phrase a context.

- *Hand-set supports (§5.2).* {tap, box} × {pitcher, cabinet} is
  possibilistically non-signalling and contextual, of Hardy type: two
  global assignments exist, but the locally possible (tap = touch,
  pitcher = baseball player) extends to neither.
- *Corpus estimates (§6).* Every model is signalling, e.g. P(box = put in
  boxes) is 2/3 in "box leaves" and 7/74 in "box can". The sheaf
  criterion cannot be applied to any.
- *Contextuality-by-Default (§8.1).* Two noun–verb pairs read in both
  grammatical orders, adopt/boxer and throw/pitcher, come out contextual,
  with measures 1/30 and 7/30 (recomputed in [NOTE-645](../notes.d/NOTE-645.md)). The paper's own
  parametric bootstrap puts the probability that each is noncontextual
  above .56 and above .08. The counts have denominators of 3 to 30.

**Anaphora in BERT ([LIT-844](../literature.d/LIT-844.md)).** A three-sentence schema ("the same one",
"the other one") gives every instance the support of the PR prism,
which no global assignment fits. Only one marginal per context comes
from BERT; the joints are stipulated. With SF the signalling fraction
and Δ the CbD direct influence, an instance is sheaf-contextual iff SF <
1/6 and CbD-contextual iff Δ < 2 (CNT1 = 2 − Δ, [NOTE-648](../notes.d/NOTE-648.md)'s check). Of
51,966,480 instances, 0.148% are sheaf-contextual and 71.1%
CbD-contextual. If the three probabilities are equal at p, Δ = 2|2p − 1|,
below 2 for every p strictly between 0 and 1. The tie to embedding
distance is the softmax identity ε = tanh((p·Δx + Δb)/2), with
correlations of 0.06 to 0.20.

What could have come out otherwise: the corpus models could have been
non-signalling, and the CbD verdicts could have survived the bootstrap.
Neither happened.

## What this does not say

- **That language is not contextual.** No study here uses human
  judgements with adequate counts. The proposed tests (Wang and
  Sadrzadeh's 2023 human-judgement data; Lo et al.'s crowdsourced
  Winograd schemas) are not held.
- **That BERT is contextual in any sense about BERT.** The parity
  contradiction is in the sentences. Any uncertain resolver yields
  formally contextual data on this schema.
- **That the two signalling-aware criteria agree.** On the same data they
  give 0.148% and 71.1%, and whether the sheaf test of Vallée et al. is
  necessary as well as sufficient is not settled, so 0.148% may be a
  lower bound.
- **That ambiguity is contextuality.** press/box has several readings and
  global assignments for all of them; ambiguity is the outcome set, not
  the obstruction.

## Connections

- [THEORY-013](THEORY-013.md) holds that behavioural, social and word-meaning data
  published as contextual show none once signalling is separated. These
  two studies are its first language cases. Neither meets its
  `promote_when` as a robust counterexample.
- [CLAIM-037](../claims.d/CLAIM-037.md) (formal contextuality needs Contextuality-by-Default when
  marginals shift) is supported: every corpus model and every BERT
  instance not at P = ½ signals. [CLAIM-044](../claims.d/CLAIM-044.md) holds here only for strong
  contextuality: the Hardy-type tap/box model keeps two global
  assignments. [CLAIM-009](../claims.d/CLAIM-009.md) is not tested: these are lexical selections and
  a model's resolutions, not people's pragmatic judgements.
- The journal follow-up ([LIT-851](../literature.d/LIT-851.md), [THEORY-177](THEORY-177.md)) measures direct influence
  across 90 noun–verb systems and reports no new contextual system.
