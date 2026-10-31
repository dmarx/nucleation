---
number: 1259
status: Active
formerly:
- THEORY-tmpfm1ma
title: 'When a teacher''s next-token distribution depends on a context the student cannot observe, the forward-KL-optimal student is the teacher averaged over the contexts compatible with the student''s observation, the loss it cannot remove is the conditional mutual information between the teacher''s output and the hidden context, and the optimal student is at least as uncertain as the teacher is on average; the self-distillation objectives actually trained may not be forward KL at all'
version: 1
tags:
- learning-theory
- information-theory
date: '2026-10-31'
source:
- LIT-1883
summary: >-
  Hossain, Kousar and Tourni (2026), [LIT-1883](../literature.d/LIT-1883.md), Proposition 1; read
  in [NOTE-1479](../notes.d/NOTE-1479.md). Active: elementary and checked numerically. This is
  the published statement of the limit [QUESTION-361](../questions.d/QUESTION-361.md) starts from. It
  holds for the unclipped forward KL; the OPSD objective the paper trains
  clips each vocabulary entry, which the paper shows reverses the
  gradient on the teacher's most preferred tokens.
---
<!-- inactive-ok-file: QUESTION-361 — Open; the question this account bears on, cited as open -->

# THEORY-1259: When a teacher's next-token distribution depends on a context the student cannot observe, the forward-KL-optimal student is the teacher averaged over the contexts compatible with the student's observation, the loss it cannot remove is the conditional mutual information between the teacher's output and the hidden context, and the optimal student is at least as uncertain as the teacher is on average; the self-distillation objectives actually trained may not be forward KL at all

## Source

Hossain, Kousar and Tourni (2026), [LIT-1883](../literature.d/LIT-1883.md), §3.5 and Appendix A.1
(Propositions 1 and 2), pp. 5 and 12–14 of arXiv 2609.37915v1; read in
[NOTE-1479](../notes.d/NOTE-1479.md).

## What was actually shown

Fix the student's observation z and let R ∼ P(r | z) be the context only
the teacher sees. For any p,

E_{R|z} KL(q(· | z, R) ‖ p) = E_{R|z} KL(q(· | z, R) ‖ q̄) + KL(q̄ ‖ p),
with q̄ = E_{R|z} q(· | z, R).

So the minimiser is p* = q̄. The minimum, E KL(q ‖ q̄), is I(A; R | Z = z)
for A drawn from the teacher. Concavity of entropy gives H(q̄) ≥ E H(q).
Checked numerically (six tokens, four contexts): the optimiser found q̄ to
10⁻⁸, the minimum equalled the mutual information to 10⁻¹⁵, and the
two-term split held for an arbitrary p.

The objective actually trained in OPSD and OASIS is Σ_a min(e_a, κ) with
e_a = q_a log(q_a/p_a) and κ = 0.05. For a clipped entry j the logit
gradient is p_j Σ_{a unclipped} q_a > 0: descent lowers z_j, although
e_j > κ means the teacher prefers j more than the student does
(Proposition 2; checked on the paper's example). At κ = 0.05 the clip
removes 94–97% of the positive KL mass (Fig. 4).

## What this does not say

- **That a calibrated teacher is needed.** The bound concerns the
  teacher's output. It equals the predictive information I(Y; R | Z)
  about the world only if the teacher is calibrated, as [QUESTION-361](../questions.d/QUESTION-361.md)
  assumes.
- **That OPSD minimises this objective.** The paper says Proposition 1
  "should not be read as an exact characterization of the implemented
  OPSD objective" (App. A.1.1).
- **That the gap is permanent.** The proposition treats z as all the
  student has. A student that learns to infer R from the problem
  shrinks it, and the paper notes that the reference is a function of
  the problem.
- **Anything new as mathematics.** It is the familiar mixture optimum of
  forward KL, stated for privileged context. Its value here is as the
  published locus and for the entropy consequence: supervision where the
  teacher's advantage is privileged makes the student less certain.
- **Anything about MTP self-distillation.** In Teoh's DeepSeek-style heads
  ([LIT-1896](../literature.d/LIT-1896.md)) the student sees what its teacher sees, and the
  irreducible term is zero ([THEORY-1274](THEORY-1274.md)).
