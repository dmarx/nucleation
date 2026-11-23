---
status: Proposed
title: 'A pretrained diagonal linear network and its function-preserving rescaling, read as two learners with one function that fine-tuning sends apart, are an existence case of equal operational frontiers with different developmental frontiers and of a ranking that reverses with the declared later task'
version: 1
history:
- version: 1
  date: '2026-11-23'
  note: >-
    Filed by the lead run of 2026-11-23, for the support its verdict gives
    the three-frontier claim, which the objection filed with it contests.
form: existence
rests_on:
- CLAIM-tmp2tjpt
- CLAIM-tmp7n00e
grounds:
- THEORY-tmpw69kb
- CASE-tmpjn7jc
concludes:
- CLAIM-754
tags:
- learning-theory
- representation-learning
date: '2026-11-23'
line:
- learned-structure
summary: >-
  The support the lead run of 2026-11-23 finds for CLAIM-754 in Lippl and
  Lindsey: an existence case, in a solvable model, of two learners whose
  operational frontiers are equal and whose developmental frontiers under
  one procedure differ, with the better of them depending on the declared
  later task. It carries the divergence clause only on CLAIM-tmp2tjpt's
  reading; on CLAIM-tmpew899's it carries only the indexing by procedure.
  Nothing on the frontiers moving in opposite directions over training.
  Proposed. The wording is the assistant's (Claude, in this session);
  adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-754 CLAIM-tmp2tjpt CLAIM-tmp7n00e CLAIM-tmpew899 CASE-tmpjn7jc THEORY-2077 — Proposed; the conclusion, the claims and case filed by the lead run of 2026-11-23, and the reading it is compared with -->

# ARG-tmpbvq7y: A pretrained diagonal linear network and its function-preserving rescaling, read as two learners with one function that fine-tuning sends apart, are an existence case of equal operational frontiers with different developmental frontiers and of a ranking that reverses with the declared later task

## The inference

1. P₁ is a two-layer diagonal linear network pretrained from small
   weights on a sparse auxiliary task; P_c has first layer c·w and
   auxiliary readout v/c. They compute the same function
   (CLAIM-tmp7n00e).
2. Their operational frontiers are equal for any declared family of
   tasks the auxiliary function answers, and for readout-only training as
   the operating procedure, which reaches the same function from both
   (CLAIM-tmp7n00e, CASE-tmpjn7jc).
3. Under full fine-tuning by gradient descent, the same procedure in
   each network's own weights, they converge to different solutions with
   few main-task samples: Lippl and Lindsey's penalty with |β^aux|
   replaced by c²|β^aux| (THEORY-tmpw69kb), confirmed numerically
   (CASE-tmpjn7jc).
4. On a main task using a sparse subset of the pretrained features a
   shrunk network generalizes better; on one using all of them with
   varied coefficients the unshrunk one does.
5. If P₁ and P_c are two learners (CLAIM-tmp2tjpt), then equal
   operational frontiers leave different developmental frontiers within
   one class of learners and tasks, which is what CLAIM-754's
   `defeated_if` says would defeat it if it never happened; and no
   ranking of P₁ against P_c holds before the later task is declared.

## Critical questions

- **Is the case real, not stipulated?** It is a derivation from the
  paper's Corollary 2 and the network's symmetry, and a run on CPU, in a
  solvable model; nothing in it is assumed beyond the paper's setup.
- **Is it of the kind the claim speaks of?** Only on CLAIM-tmp2tjpt's
  reading. On CLAIM-tmpew899's, P_c is P₁ under a preconditioned
  procedure, and the case shows only that the developmental frontier is
  indexed by procedure, which CLAIM-754 already allows. The assistant
  leans to the first reading; the owner chooses.
- **Does it reach beyond the special initialization of Anguita and
  colleagues (THEORY-2077)?** Yes on the first reading: the rescaling
  acts on any converged network, not only on one started at a chosen
  relative scale. On the second reading the only history-made case is
  still theirs.
- **Does it bear on the opposite-direction clause?** No. Pretraining is
  always to convergence, so nothing here moves the operational frontier
  up while the developmental one moves down.
