---
number: 341
status: Proposed
formerly:
- CASE-tmpnti0m
title: 'Identical operators under four influence rules'
statement: >-
  A population of identical linear operators under four influence rules: all
  differentiate into one specialist per context, a rare one included; with
  no spare operator a rare specialist made rare recovers, at a rate
  independent of its share under a multiplicative contribution rule and
  proportional to it under softmax-gradient routing; with two spare
  operators a removed specialist is replaced and a suppressed one is shut
  out, whether or not it kept its competence
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-016 at the
    coordinator's brief: a reduced run of CASE-117's proposed study.
    Model, tests, script, results and a README are under
    scratch/studies/lead-016/.
standing: documented
kind: executed-study
tags:
- complex-systems
- ecology
- learning-theory
date: '2026-11-22'
bears_on:
- QUESTION-132
- QUESTION-134
- QUESTION-083
- QUESTION-135
- QUESTION-133
draws_on:
- THEORY-134
line:
- distributed-agency
summary: >-
  [LEAD-016](../leads.d/LEAD-016.md) asked for [CASE-117](CASE-117.md) to be run. This is a reduced version on a
  CPU. There are four contexts, one of them rare (p = 0.02), each a linear
  regression with an orthonormal target. K linear operators, identical in
  form and differing only by initialization, mix by context-conditioned
  shares. Four rules update the shares: ordinary mixture-of-experts gating
  (the baseline), the same gating with a load-balancing loss, the same
  gating with a usage bias, and a multiplicative rule driven by the
  collective's loss minus the operator's own. Training follows influence.
  Each rule was run with K = 4 (no spare operator) and K = 6 (two spare),
  in 6 seeds, followed by eleven test arms. Every rule differentiated, with
  a distinct specialist for the rare context in 6 of 6 seeds. With K = 4,
  participation and performance matched across three rules. A rare
  specialist made rare (share 10⁻³, frozen) recovered in 6 of 6 seeds under
  all four rules. Under the multiplicative rule its growth rate did not
  depend on how rare it was made. Under gradient gating it fell with the
  share, and from 10⁻⁵ the specialist did not recover within the window. A
  usage bias recovered it from any share, but also raised an incompetent
  copy to 0.19. With K = 6, a removed specialist was replaced by a spare in
  6 of 6 seeds under every rule. A suppressed specialist then failed to
  return in 23 of 24 rule-seed pairs per arm, whether its training had been
  decoupled from its influence and whether it had kept its competence.
  With K = 4, nothing replaced a removed specialist. A suppressed one
  returned every time, even after weight decay had cost it most of its
  competence and with its parameters frozen. One model class, one size,
  six seeds. The wording is the assistant's (Claude, in this session);
  adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-918 CLAIM-919 — new, filed with this case -->
<!-- inactive-ok-file: CLAIM-885 CLAIM-875 — Proposed, filed 2026-11-22 by LEAD-049 and LEAD-065, cited for comparison; nothing here rests on them -->

# CASE-341: Identical operators under four influence rules

## What was done

[LEAD-016](../leads.d/LEAD-016.md) asks for [CASE-117](CASE-117.md) to be run. The work was scoped to about an hour
of CPU on a shared machine. It covers [CASE-117](CASE-117.md)'s influence-update and
diversity-mechanism dimensions, its specialist-loss and recovery-opportunity
dimensions, its frozen-against-trainable recovery measurement, and its
coupled-against-decoupled exposure comparison ([QUESTION-134](../questions.d/QUESTION-134.md)). It leaves the
rest out (see "What it cannot show").

**The model** (`scratch/studies/lead-016/opmodel.py`, with 12 tests):

- **Contexts.** There are four, with p = (0.33, 0.33, 0.32, 0.02); R
  denotes the rare one. In context c the target is y = β_c·x + 0.1·noise,
  with x ~ N(0, I₈) and the β_c orthonormal. The collective sees the
  context.
- **Operators.** K linear operators a_i = θ_i·x share the fixed features
  x. They are identical in form and differ only by a small random
  initialization. Since one operator cannot fit two orthogonal targets,
  doing well needs differentiation.
- **Influence.** The shares π_ci = softmax(Z_c + b)_i are
  context-conditioned. The collective outputs Σ_i π_ci a_i.
- **Influence rules:**
  - **moe**: Jacobs-style gating. The logits follow the gradient of the
    mixture log-likelihood. This is the baseline.
  - **moe_aux**: moe plus a load-balancing loss, 0.01·K·Σ u_i² on the
    batch usage. This is balancing imposed inside the gradient.
  - **moe_bias**: moe plus a per-operator bias, stepped toward equal
    usage. This is balancing imposed outside the gradient, after
    auxiliary-loss-free balancing ([LIT-1414](../literature.d/LIT-1414.md)). Here the bias enters the
    dense mixing weights, since there is no top-k selection.
  - **rep**: each sample adds η(ℓ̂ − ℓ_i) to Z_ci, the collective's loss
    minus operator i's own. This is a multiplicative, context-sensitive
    contribution rule.
  - **uniform**: equal shares, a reference.
- **Training.** Each operator trains on its own squared loss, weighted by
  its exposure. Exposure is the posterior responsibility under the moe
  rules and the share under rep. Either way it is coupled to influence.
- **Competence** is analytic held-out risk on the generating distribution,
  (|θ_i − β_c|² + σ²)/(1 + σ²), relative to predicting zero. No sample the
  loop saw enters it. This is the independent evaluation distribution
  [QUESTION-134](../questions.d/QUESTION-134.md) asks for.

**Protocol** (`study.py`). Each rule ran with K = 4, one operator per
context, and K = 6, two spare. There were 6 seeds; the run was cut from 12
because the machine was shared. Each run differentiated for 40,000
minibatches of 8, about 6,400 rare samples. The rare context's specialist is
the operator with the largest share in R. From that snapshot, each test ran
20,000 steps, about 3,200 rare samples, with no further intervention unless
stated:

- **rare** (frozen or trainable): the specialist's share in R set to ε =
  10⁻², 10⁻³ or 10⁻⁵. This is [QUESTION-132](../questions.d/QUESTION-132.md)'s recovery test from a small
  positive start.
- **sham**: the same, with the specialist's parameters replaced by a frozen
  copy of a common context's specialist. That copy is as incompetent in R
  as the residents, so any recovery it shows does not come from
  competence.
- **remove**: the specialist deleted.
- **suppress**: the specialist's share in R clamped at 10⁻³ for 20,000
  steps, then released at 10⁻³. There are five variants:
  - exposure coupled to the clamped influence, or decoupled, kept at its
    pre-suppression level ([QUESTION-134](../questions.d/QUESTION-134.md)'s control);
  - with or without weight decay of 10⁻⁴ a step in the test window, a
    maintenance cost;
  - one coupled-with-decay variant whose parameters are frozen at release.

## Result

Full tables are in `scratch/studies/lead-016/results/summary.md`. Medians
over 6 seeds; counts are seeds out of 6.

**Differentiation.** Every rule except uniform differentiates. Each common
context gets one specialist, and the rare context gets its own distinct
specialist (held-out risk 0.010) in 6 of 6 seeds. Uniform shares give no
differentiation, with risk 0.68 in the common contexts and 1.28 in R. At
K = 4, moe, moe_aux and rep match on participation, with I(operator;
context) = 1.17 nats, usage entropy 1.17 and the same per-context shares.
They also match on performance, with risk 0.0103. moe_bias is close, at
usage entropy 1.19. At K = 6 the rules part:

- moe and moe_aux leave the two spares idle, with share at most 0.002.
- rep lets a spare co-learn the rare specialist's job. Their parameter
  vectors have cosine 0.998.
- moe_bias pushes the spares into use, with usage entropy 1.60.

**Recovery when rare, K = 4 (the matched comparison).**

| rule | λ per R sample, ε = 10⁻² / 10⁻³ / 10⁻⁵ | R samples to share 0.5 | recovered from 10⁻⁵ | sham final share |
|---|---|---|---|---|
| moe | 0.010 / 0.0033 / 0.00075 | 362 / 896 / — | 0/6 | 0.0010 (stays at ε) |
| moe_aux | 0.0098 / 0.0034 / 0.00075 | 337 / 896 / — | 0/6 | 0.0010 |
| moe_bias | 0.023 / 0.015 / 0.0095 | 206 / 402 / 906 | 6/6 | 0.19 |
| rep | 0.036 / 0.042 / 0.044 | 116 / 190 / 283 | 6/6 | 7 × 10⁻¹² |

- **Recovery rate under rep.** It does not depend on how rare the
  specialist was made. The time to recover grows only with log(1/ε).
- **Recovery rate under softmax-gradient gating.** With or without the
  balancing loss, it falls with the share. From 10⁻⁵ the specialist ends
  the window at 8 × 10⁻⁴. [CLAIM-918](../claims.d/CLAIM-918.md) gives the reason: the logit
  gradient of a softmax share is proportional to that share. The
  load-balancing loss changes nothing at this coefficient, because its
  gradient is also proportional to the share.
- **The usage bias.** It recovers the specialist from any share. It also
  lifts the incompetent sham to 0.19 of the rare context.
- **The sham under rep.** rep drives the incompetent sham out.
- **Frozen against trainable.** The two arms give identical results. What
  recovers is the retained capability.

**Removal.**

- **K = 4.** Nothing refills the niche in 0 of 6 seeds, under every rule.
  The rare context's risk stays at 1.3 to 1.8. The resident specialists
  stay with their own contexts, and none takes on the rare one.
- **K = 6.** A spare refills it in 6 of 6 seeds under every rule. Risk
  returns to 0.0104, with no cost to the common contexts.

**Suppression ([QUESTION-134](../questions.d/QUESTION-134.md)).** Access is the specialist's mean exposure per
rare sample during suppression. Competence is its held-out risk in R,
starting at 0.0104. Recovery counts are given for moe, moe_aux, moe_bias
and rep.

| K | arm | access | competence at release | competence at end | recovered | rival's risk at release |
|---|---|---|---|---|---|---|
| 4 | coupled, no decay | 0.001–0.045 | 0.010 | 0.010 | 6, 6, 6, 6 | 1.75–1.97 |
| 4 | coupled, decay | 0.001–0.04 | 0.17 (moe), 0.73 (rep) | 0.014 | 6, 6, 6, 6 | 1.74–1.96 |
| 4 | coupled, decay, frozen at release | same | 0.17, 0.73 | 0.17, 0.73 | 6, 6, 6, 6 | same |
| 4 | decoupled, decay | 0.97–1.0 | 0.013 | 0.014 | 6, 6, 6, 6 | same |
| 6 | coupled, no decay | 0.001–0.012 | 0.010 | 0.010 | 0, 0, 1, 0 | 0.010 |
| 6 | decoupled, no decay | 0.97–1.0 | 0.010 | 0.010 | 0, 0, 1, 0 | 0.010 |
| 6 | coupled, decay | 0.001–0.01 | 0.73–0.95 | 0.96–1.06 | 0, 0, 1, 0 | 0.013 |
| 6 | decoupled, decay | 0.97–1.0 | 0.013–0.015 | 0.76–0.96 | 0, 0, 1, 0 | 0.013 |

- **Loss of access costs competence only with a maintenance cost.** With
  no decay, a specialist whose access fell to 0.1% kept its competence
  through 20,000 steps. The model has no interference, since an operator
  with no exposure is not trained at all. With decay, coupled access cost
  it most of its competence, and decoupled access preserved it.
- **With no spare, lost competence did not stop recovery.** Even a frozen
  specialist at risk 0.73 regained the niche, because no rival was any
  better (risk 1.75). Competence is judged against the residents.
- **With spares, kept competence did not secure recovery.** A spare took
  the niche during suppression and became as competent as the specialist
  (0.010–0.013). The returning specialist, with its competence intact
  because its exposure had been decoupled, then had no advantage. Its
  share stayed near 10⁻³. Afterwards, with exposure coupled again, it lost
  its competence: from 0.013 at release to 0.76 at the end. Loss of
  competence followed the exclusion and did not cause it.

**Residual direction ([QUESTION-135](../questions.d/QUESTION-135.md)).** `residual.py` measures, at the
snapshot, the rare specialist's squared distance d² from the span of the
other operators' normalized parameter vectors.

| rule, K | d² | recovery exponent at ε = 10⁻³ |
|---|---|---|
| any rule, K = 4 | 1.0 | positive |
| rep, K = 6 | 0.000 | 6 × 10⁻⁵, neutral |
| moe, K = 6 | 0.18 | negative |

So recovery tracks the specialist's own residual direction. That is the
quantity [CLAIM-885](../claims.d/CLAIM-885.md)'s Theorem B puts in its lower bound, n_i d_i², for
fixed features. Under rep at K = 6 the spare had already co-learned the
rare job before the test. Under moe at K = 6 the spare learned it during the window, faster
than the specialist's share-limited recovery.

## What it can show

- **Matched participation, different mechanism.** [CASE-117](CASE-117.md)'s decisive
  comparison can be made in this class. moe, moe_aux and rep end with the
  same context-conditioned participation, task performance and budget.
  They differ in recovery dynamics:
  - rep: the recovery exponent stays the same however rare the
    specialist is made;
  - softmax-gradient gating: the exponent shrinks with the share;
  - the usage bias: it recovers what is rare whether or not it is
    competent.

  So the difference [CASE-117](CASE-117.md) names, between imposed balance and recovery
  that comes from competence, can be measured here. The sham arm is the
  measurement.
- **Removal and refill.** Spare capacity decides between them. With
  capacity, the role is regenerated and the particular specialist is
  shut out. This resembles [CLAIM-875](../claims.d/CLAIM-875.md)'s Reading B, role regeneration
  by interchangeable holders, now in a model whose operators have
  functions. Without capacity, nothing refills a lost niche, and the
  specialist that held it keeps a claim on it.
- **[QUESTION-134](../questions.d/QUESTION-134.md).**
  - The three losses separate. Loss of access did not by itself cost
    competence. With a maintenance cost it did, and decoupling prevented
    that.
  - The decisive result [QUESTION-134](../questions.d/QUESTION-134.md) asks for was not found. A specialist
    with competence lost through deprivation that does not return, while a
    decoupled control does, did not appear. Where the specialist failed to
    return, the decoupled control failed too, by pre-emption.
  - Competence loss came after exclusion, through renewed coupling.
  - These results are filed as [CLAIM-919](../claims.d/CLAIM-919.md).

## What it cannot show

- **Not attempted.** These [CASE-117](CASE-117.md) conditions were not run:
  - learned features;
  - historical-grant influence ([CLAIM-277](../claims.d/CLAIM-277.md));
  - an authority-update rule the organization revises;
  - abrupt distribution shifts and recurring dormancy;
  - internally maintained exploration;
  - the compatibility-complex measurement for [QUESTION-133](../questions.d/QUESTION-133.md);
  - any parameter sweep for [QUESTION-125](../questions.d/QUESTION-125.md).
- **Scope.** There is one model class: linear operators with orthogonal
  targets, so an operator can serve one context well. There is one size,
  d = 8 and C = 4, and there are 6 seeds. A 20,000-step window means that
  "not recovered" is bounded by about 3,200 rare samples. The moe
  recoveries from 10⁻⁵ may come later.
- **Self-constitution.** Positive results here do not show it. The
  objectives are the modeller's ([CLAIM-288](../claims.d/CLAIM-288.md)).
- **Implementation choices.** The moe_bias variant puts its bias into the
  mixing weights. [LIT-1414](../literature.d/LIT-1414.md) puts it into top-k selection only, so this
  variant is an analogue, not a reproduction. The aux coefficient was not
  swept.
- **Suppression design.** Suppression clamps the share by intervention, so
  it is an external marginalization, not one the population produced.
