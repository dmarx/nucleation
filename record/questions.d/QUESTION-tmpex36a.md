---
status: Open
title: 'In networks trained on relational-rule tasks under varied data diversity, does the emergence of role abstraction (a quotient of inputs by token relabelling) coincide with balanced-partition (fibration) structure among the network''s units, or can either occur without the other?'
version: 1
tags:
- representation-learning
- network-science
- learning-theory
date: '2026-11-19'
line:
- learned-structure
summary: >-
  The owner's, from U9 of the exchange "Topological protection explained"
  (2026-11-18): "I have a hunch this fibration approach relates nicely to"
  Li and Webb's study of what drives symbolic mechanisms ([LIT-tmpqgxkn](../literature.d/LIT-tmpqgxkn.md)).
  The fibration approach is the balanced-partition theory of synchrony the
  record holds as [THEORY-1065](../theory.d/THEORY-1065.md) and [THEORY-1059](../theory.d/THEORY-1059.md), which the owner had just
  met in Gili et al. ([LIT-tmp8nrv2](../literature.d/LIT-tmp8nrv2.md)). A21 sharpened the hunch: both are
  quotients that keep the operations that matter, one of inputs by
  relabelling, one of units by equal input trees. Li and Webb, read, say
  nothing at the level of units or partitions, so the link is untested.
  The question's wording is the filer's; the hunch is the owner's.
---
<!-- inactive-ok-file: CLAIM-tmpj540o — Proposed; cited in this filing of 2026-11-19 -->
<!-- inactive-ok-file: THEORY-tmp8my3p THEORY-tmpmtmq7 — Proposed; cited in this filing of 2026-11-19 -->

# QUESTION-tmpex36a: In networks trained on relational-rule tasks under varied data diversity, does the emergence of role abstraction (a quotient of inputs by token relabelling) coincide with balanced-partition (fibration) structure among the network's units, or can either occur without the other?

## Why it is a question

The owner, at U9 of the exchange "Topological protection explained"
(https://chatgpt.com/share/6afe6dd0-9d78-83ea-9782-f55680665dcf):

> I have a hunch this fibration approach relates nicely to this [arXiv 2611.13270]

Two quotients are in play. Role abstraction identifies inputs that differ
only by which arbitrary tokens fill the roles: Li and Webb's rule
representation is what stays invariant when the vocabulary is
relabelled ([THEORY-tmpmtmq7](../theory.d/THEORY-tmpmtmq7.md), [CLAIM-113](../claims.d/CLAIM-113.md)). A balanced partition identifies
units that receive equivalent inputs, so any admissible dynamics keeps
them synchronized ([THEORY-1065](../theory.d/THEORY-1065.md)), and the network can be run on the
quotient ([THEORY-1059](../theory.d/THEORY-1059.md)). A21 put the bridge as commuting maps: a rule
extractor that factors through the input quotient, against
F_A(Cy) = C F_B(y) for a fibration. They are different quotients; an
input-relabelling quotient is not a graph fibration.

## A route between them

At zero role-token bias the training distribution is invariant under
relabelling. [THEORY-981](../theory.d/THEORY-981.md) holds that when data is invariant under a group
the network is equivariant to, population gradient descent stays in the
weight subspace the group fixes; weight symmetry gives orbit synchrony
among units ([THEORY-276](../theory.d/THEORY-276.md)); balanced partitions generalize that synchrony
beyond symmetry ([THEORY-1065](../theory.d/THEORY-1065.md)). Checked on 2026-11-19 ([CLAIM-tmpj540o](../claims.d/CLAIM-tmpj540o.md)),
the route holds only where the relabelling group permutes the network's
units, and it cannot permute them nontrivially when the vocabulary
exceeds the width, as in most of Li and Webb's runs. So in their models
any coincidence of role abstraction with balanced structure would be
learned, not forced by symmetry, and that is the form the question
takes.

## What would answer it

In Li and Webb's pure MLP, compute approximate balanced colourings of the
hidden units' weight graph. Exact ones are trivial for generic trained
weights, so a tolerance is needed. Then ask whether the rule direction
lies in the span of the partition's synchrony subspace more than chance
would give. Compare high-diversity models with full-bias models and
random-initialization models ([THEORY-1002](../theory.d/THEORY-1002.md)'s control), and track the
measure across the late rise in flip rate at small vocabularies. If the
hunch holds, the partition coarsens and aligns with the role direction as
the flip rate rises. Velarde, Parra, Hashemi and Makse (LIT registered
from this exchange, unread) report fibrations and coverings emerging in
trained networks and are the evidence on the fibration side.

## Bearing so far

- Li and Webb ([THEORY-tmpmtmq7](../theory.d/THEORY-tmpmtmq7.md)): silent at the level of units.
- Gili et al. ([THEORY-tmp8my3p](../theory.d/THEORY-tmp8my3p.md)): balanced partitions inferred from
  synchrony in brains, not from trained networks.

## Note of 2026-11-19: readings for the exchange "Topological protection explained"

Velarde, Parra, Hashemi and Makse (THEORY-tmpz825j), read: narrows the question and leaves it open. Quasi-fibers and quasi-covers grow in training, and gradient descent only merges exact covers (Theorem 1): balanced structure among units with no data symmetry to force it. But each input coordinate starts in its own colour, so units in a fiber agree "for any input x": redundant copies, not a quotient of inputs by relabelling, and no rule task is run. Their tolerance-based colouring (Methods 4.15) is still to be run on Li and Webb's models.

DeVille and Lerman (THEORY-tmp31d9a), read: leaves the question open. They give the fibration side of the bridge as maps of dynamical systems, h ∘ ϕt = ψt ∘ h, the commuting-map form A21 used, and call the surjections induced by injective fibrations "abstractions" in the computer-science sense. The paper covers continuous-time systems on unweighted graphs and says nothing about learning or inputs.

Geiger and colleagues (THEORY-tmp1cus0), skimmed; the reader's observation, not the paper's: their alignment (Definition 31) is a quotient of units, a partition with value maps. A fibration base merges units with equal activity on every input, a variable merge with identity value maps that keeps the forward computation exact (THEORY-tmpz825j). Neither paper connects the two. A test of the hunch could ask whether the alignment cells of a role-level algorithm are unions of quasi-fibers. Their worked task, hierarchical equality, is a relational rule of the kind the question names.

No status change.
