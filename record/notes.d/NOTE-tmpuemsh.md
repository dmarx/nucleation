---
status: Read
paper: 'LIT-tmpbnm77'
title: 'Hossain, Kousar & Tourni — Overcoming scaling limits in on-policy self-distillation'
version: 1
history:
- version: 1
  date: '2026-10-31'
  note: >-
    Read in full from the arXiv preprint 2609.37915v1 (29 September
    2026), 19 pp., fetched 2026-10-31 and extracted with `pdftotext`;
    page numbers are the arXiv copy's. I read the abstract, §§1–6, all of
    Appendix A (proofs, probe protocols, clipping, ablations,
    implementation), Algorithm 1, Tables 1–9 and the captions of Figs.
    1–6; the figures' plotted values did not survive extraction beyond
    the numbers the text repeats. I checked numerically (numpy and scipy,
    my own script) Proposition 1 (the minimiser is the context mixture,
    the minimum equals the conditional mutual information, the entropy
    inequality, and the two-term decomposition for any student) and
    Proposition 2 with the paper's own example (gradient (0.06, −0.08,
    0.02); the step lowers z₃ and raises p₃; the clipped objective is
    already negative, −0.158). The exchange's A16 was compared against
    the text.
date: '2026-10-31'
summary: >-
  On-policy self-distillation from a privileged-context teacher does most
  of its supervising on failed student trajectories, where the teacher's
  advantage depends on the reference the student cannot see; Proposition
  1 gives the forward-KL optimum as the context-averaged teacher with the
  conditional mutual information as irreducible loss. Restricting
  supervision to verified on-policy trajectories and using the student's
  own failed attempt as the teacher's context keeps the gain over the
  base model at 3.2–3.8 points from 1.7B to 8B, where standard OPSD's
  falls to 0.14, in single runs. The trained objective clips each
  vocabulary entry and is not a forward KL.
---
<!-- inactive-ok-file: QUESTION-tmp4b001 THEORY-tmpjz0xp — Open or Proposed; the question this reading bears on and the account it files, cited as open -->

# NOTE-tmpuemsh: Hossain, Kousar & Tourni — Overcoming scaling limits in on-policy self-distillation

## Contribution

On-policy self-distillation (OPSD, Zhao et al. 2026) uses one model twice:
the student sees the problem and samples a solution; the teacher, the
frozen initial policy with a written reference solution in its prompt,
scores the student's trajectory token by token; the student is trained
toward the teacher's distributions. The paper separates two roles that
OPSD couples: the scaffold (which trajectory receives supervision) and
the context (what the teacher is told). It shows that OPSD supervises
mostly failed or truncated trajectories, where the teacher's advantage
comes from the reference. It proposes OASIS: supervise only the shortest
verified rollout, and give the teacher another rollout of the same
problem, usually a failed one, in place of the reference (§§3–4).

## Key insight

A teacher that sees what the student cannot is imitable only where its
behaviour does not depend on the unseen part. Under forward KL the best
student is the teacher averaged over the contexts compatible with what
the student sees (Prop. 1). Where the privileged context matters, that
average is a blurred target the student cannot reach, and supervision
there teaches uncertainty. Where the student's own trajectory already
reaches the answer, the teacher's signal hardly depends on its context.
That supervision is imitable, and a written solution is not needed for
it.

## Assumptions

- **Teacher**: the frozen initial policy π_θ0, thinking mode on, prompt
  u(x, r); **student**: π_θ, thinking off, LoRA rank 64 (Table 9). The
  teacher is the same weights, not the current model.
- **Objective (eq. 3)**: per-vocabulary-entry clipped forward KL,
  Σ_a min(q_a log(q_a/p_a), κ), κ = 0.05, temperature 1.1. Not a
  divergence: entries can be negative, and the training loss is
  negative from the start (App. A.3).
- **Prop. 1's setting**: the unclipped forward KL, at a fixed student
  observation z, with R ∼ P(r | z) carrying information the student
  cannot recover from z. The authors note that the reference is a
  function of the problem, so a capable enough student could in
  principle infer it (App. A.1.1).
- **Data and scale**: math subset of OpenThoughts; Qwen3-1.7B, 4B, 8B;
  100 steps; AIME 2024, AIME 2025, HMMT 2025 (30 problems each);
  single training runs.

## Key results

- **Proposition 1** (§3.5, App. A.1.1). min_p E_{R|z} KL(q(· | z, R) ‖
  p(· | z)) is attained at p* = E_{R|z} q(· | z, R); the minimum is
  I(A; R | Z = z) with A ∼ q(· | z, R); and H(p*) ≥ E H(q). The proof
  expands the KL into E KL(q ‖ q̄) + KL(q̄ ‖ p). Checked.
- **Proposition 2** (App. A.1.2, A.3). For a clipped entry j,
  ∂ℓ/∂z_j = p_j Σ_{a∈U} q_a > 0, so descent lowers z_j although the
  teacher prefers j more than the student does (e_j > κ > 0 implies
  q_j > p_j). At κ = 0.05 the clip removes 97% of positive KL mass on
  verified scaffolds and 94% on failed ones; about 3 tokens in 10 have a
  clipped entry (Fig. 4). Checked on the paper's example.
- **Where OPSD supervises** (§3.2, Table 5): only 28.3% (1.7B) and 30.6%
  (4B) of rollouts reach a correct answer; 62–64% hit the token cap.
- **What the teacher signal is made of** (§3.3, Fig. 2): at 1.7B the
  thinking template accounts for 55.0% of the teacher–student KL gap,
  the reference block 15.4%, reference content 29.6% (17.3% at 4B). On
  verified scaffolds, the student's own failed attempt, an unrelated
  reference, an empty one and the template alone are all within TV
  0.05–0.065 of the gold-context teacher.
- **Where the teacher knows more** (§3.4, Table 1): from prefixes of
  failed rollouts at 1.7B the gold-context teacher recovers the answer
  in 77% of continuations against 37% for the student (Δ = +0.40; +0.17
  at 4B); from verified prefixes, 99% against 95% (Δ = +0.04).
  Unrelated or empty references give no gain.
- **Outcomes** (Table 2): gain over base, OPSD 3.05 / 1.98 / 0.14 and
  OASIS 3.64 / 3.84 / 3.19 at 1.7B / 4B / 8B; OASIS − OPSD +0.59 / +1.86
  / +3.05. The authors call the 1.7B difference inconclusive. GRPO with
  the same verifier gains 0.23–0.60. With about a quarter of the
  supervised problems and no written solutions, OASIS matches OPSD
  trained on 12.8K solved problems (Table 4), at about 16 times the
  generated tokens.
- **Training behaviour** (§5.3, Table 5): at 1.7B OPSD's student entropy
  rises 0.40 → 0.70 and its top-1 agreement with the teacher falls 0.932
  → 0.888; OASIS holds agreement (0.929 → 0.931). At 4B both drift.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Under forward KL with privileged context, the optimal student is the context-averaged teacher and the irreducible loss is the conditional mutual information of the teacher's output and the hidden context | strong | Prop. 1, elementary, checked |
| C2 | Per-entry clipping reverses the logit gradient on tokens the teacher most prefers | strong | Prop. 2, checked; prevalence in Fig. 4 |
| C3 | The teacher's privileged advantage is concentrated on failed trajectories | moderate | Table 1, 200 scaffolds per cell, two scales |
| C4 | That advantage shrinks with scale | weak to moderate | two scales (1.7B, 4B); not measured at 8B |
| C5 | OPSD's falling gains with scale are explained by supervision on non-imitable states | weak | correlational; clipping is offered as a second, independent cause |
| C6 | OASIS keeps self-distillation effective as models scale | moderate | Table 2, single runs; Table 3 evaluation seeds only |

## Method

OASIS (Algorithm 1): sample K = 8 rollouts per problem; mask problems
with none verified; scaffold y* = shortest verified rollout; context
r = shortest unverified rollout, else another verified one; train with
OPSD's unchanged clipped loss against the frozen teacher.

## Concepts

- **Scaffold** — the trajectory along which supervision is applied.
- **Context** — what the teacher is told (r).
- **Privileged imitation gap** — the irreducible forward-KL loss
  I(A; R | Z) left when the teacher's next-token distribution depends on
  context the student cannot observe (§3.5).
- **Imitable supervision** — supervision at states where the teacher's
  behaviour can be reproduced from the student's observation (§4).

## Connections

It places OPSD in learning with privileged information (Pechyony &
Vapnik 2010) and the imitation gap with unobserved contexts (Swamy et al.
2022; Weihs et al. 2021). It agrees with Ichihara et al. (2026) that
reference content matters less than OPSD assumes. Teoh (LIT-tmpu9af8)
names OPSD as a setting for his KL gradient-recovery trick.

## Bearing on the record

- **A16's statement holds, with two qualifications.** A16 said the
  forward-KL projection and its "irreducible privileged-information gap"
  are "treated explicitly" here. They are: Proposition 1 states the
  mixture optimum, the conditional-mutual-information minimum and the
  entropy inequality, and its proof is A15's two-term decomposition
  (THEORY-tmpfm1ma). The qualifications: the authors say the proposition
  is not an exact characterization of the objective they train, which
  clips each entry and removes 94–97% of the positive KL mass (C2); and
  the teacher is the frozen initial model, not the evolving one.
- **QUESTION-tmp4b001: what distillation can carry.** The question's
  limit has its published statement here, with the consequence the
  question does not draw. Distillation on states where the teacher's
  advantage is privileged makes the student less certain (the entropy
  inequality, and OPSD's rising entropy, Table 5). Inheritance from a
  better-informed predecessor transmits that predecessor's knowledge only
  where the successor can see what it rests on. Elsewhere it transmits a
  blurred average (THEORY-tmpjz0xp).
- **QUESTION-tmp4b001: teacher and student "belong to one model".** Here
  they share weights but not time: the teacher is π_θ0 throughout. That is
  closer to inheritance from a fixed ancestor than to a model teaching
  itself.
- **TERM-097.** OASIS supervises with a teacher conditioned on the
  student's own failed attempt. Coherence with a teacher that knows
  nothing the student lacks still helps, once the scaffold is selected by
  an outside verifier. The verifier, not the teacher, supplies the
  contact with the world.
- **An instruction for ML practice is present** (supervise verified
  scaffolds; prefer per-token to per-entry clipping). That belongs to the
  Anthology of the SOTA; the LIT keeps the `anthology-candidate` flag.

## Limitations

- **Single training runs** at every scale; evaluation-seed variance only
  at 4B (Table 3). AIME and HMMT have 30 problems each.
- **One model family and one domain** (Qwen3, competition mathematics).
- **The privileged-advantage measurements stop at 4B**; the 8B
  explanation is extrapolated.
- **Prop. 1 describes an objective that is not the one trained.** The
  clip's effect is analysed separately and not removed in any run.
- **OASIS costs about 16 times the generated tokens** of OPSD.

## Open questions

- With the clip removed or applied per token, does OPSD still fade with
  scale? That would separate C4–C5 from C2.
- Does the gold-context advantage on failed prefixes keep shrinking at
  8B and beyond?
- Is the entropy rise under OPSD proportional to the measured
  I(A; R | Z), as Proposition 1 suggests?
