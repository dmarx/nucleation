---
status: Active
status_note: 'read 2026-10-05 ([NOTE-tmp09jwk](../notes.d/NOTE-tmp09jwk.md)): read in full from the copy on Cailin O''Connor''s website. Worth reading as the robustness check on the Zollman effect. Over a wider parameter space, sparse networks beat dense ones only where inquiry is hard: small groups, small batches of data, and nearly indistinguishable alternatives. Elsewhere sparsity only slows learning. The authors keep Zollman''s transient-diversity point as robust and read these models as "how-potentially" stories.'
title: 'In Epistemic Networks, Is Less Really More?'
version: 1
history:
- version: 1
  date: '2026-10-05'
  note: >-
    Read in full: the published Philosophy of Science version (84(2):234–252,
    April 2017) as posted by an author ("FINAL-VERSION"), §§1–5, footnotes
    and figure captions. `published:` is the first of
    the issue month, Crossref giving no day. Not held in the Anthology of the
    SOTA: a grep of its literature.d for "Rosenstock" and "Zollman" found
    nothing.
tags:
- epistemology
- network-science
- philosophy-of-science
date: '2026-10-05'
published: '2017-04-01'
doi: '10.1086/690717'
url: 'https://cailinoconnor.com/wp-content/uploads/2015/03/In_Epistemic_Networks_Is_Less_Really_Mor-FINAL-VERSION.pdf'
first_author: 'Rosenstock'
keywords:
- 'epistemic networks'
- 'Zollman effect'
- 'robustness'
- 'how-potentially models'
- 'bandit problems'
- 'agent-based models'
implementations: []
summary: >-
  Rosenstock, Bruner & O'Connor (2017), Philosophy of Science 84:234–252.
  Replicating Zollman's models over wider parameters, the advantage of
  cycles over complete networks vanishes once the better action is
  slightly better (pB ≥ 0.525 at size 10), groups are larger, or agents
  gather more data per round. It persists only where inquiry is hard.
  Kummerfeld and Zollman's results behave the same way. Transient
  diversity is the robust lesson.
corrects:
- LIT-tmp8lzwo
- LIT-tmpkqfje
---
<!-- inactive-ok-file: THEORY-tmpgo526 — Proposed; the network account filed in this batch -->

# LIT-tmphw2gz: In Epistemic Networks, Is Less Really More?

Sarita Rosenstock, Justin Bruner & Cailin O'Connor (2017), *Philosophy of
Science* 84(2):234–252 — DOI-10.1086/690717

## Key takeaways

- **The "Zollman effect"** is the advantage of a cycle over a complete
  network in converging on the better action. Zollman ([LIT-tmp8lzwo](LIT-tmp8lzwo.md), n. 7)
  said the network ordering holds "for any setting of the parameters". This
  paper finds otherwise (§3).
- **Success gap.** With 10 agents and 1,000 trials a round, the effect
  falls below 2% at pB = 0.51 and is zero from pB = 0.525. Zollman used
  0.501 (Figure 2).
- **Data per round.** Fewer trials per round increase the effect: small
  batches let misleading streaks occur (Figure 3).
- **Group size.** The effect fades as networks grow. At 100 agents the
  complete network converged correctly 99.12% of the time against the
  cycle's 100%, in 20 rounds against 1,977 (Figures 4–5).
- **Exploratory agents.** In Kummerfeld & Zollman's ε-greedy models both
  the effect and its reverse (dense networks better when agents explore)
  disappear as the better action becomes easier to identify (§4).
- **Diagnosis** (§5.1). Network structure matters only when inquiry is
  "difficult": similar alternatives, small groups, small batches. There,
  "decreasing connectivity only slows learning without providing any
  benefit" once agents have enough good data.
- **What survives** (§5.2). Zollman's observation that transient diversity
  is necessary ([LIT-tmpkqfje](LIT-tmpkqfje.md)) "holds for all the models discussed". The
  models are "how-potentially" stories, and the authors lower their
  confidence that such network effects regularly occur in real
  communities.
- **A better remedy.** Where data are scarce, stubborn or exploratory
  agents, or standards for how much data a judgment needs, prevent
  premature settling "apart from ignoring good data".

## Standing in the record

Filed on 2026-10-05 at the owner's request, as the robustness check on the
literature an essay's §8.2 cites. It corrects the scope of Zollman's claim,
not its mechanism, and the record's account [THEORY-tmpgo526](../theory.d/THEORY-tmpgo526.md) is stated
with the scope it leaves. Longino's SEP entry ([LIT-tmp8nw3w](LIT-tmp8nw3w.md)) reports this
paper's finding.
