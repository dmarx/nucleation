---
status: Active
title: 'Authority geometry and response geometry: when an organization''s response is the authority-weighted mixture p_π(y | c) = Σ πᵢ pᵢ(y | c), the Fisher metric of its responses is the pullback JᵀD⁻¹J of the categorical (Shahshahani) metric on the shares π and never exceeds it; it vanishes along any redistribution between processes that respond alike under the probes used, so two specialists who both answer yes with probability 0.8 in routine contexts carry no information about their shares there, while a rare context in which they answer 0.9 and 0.1 carries 0.64/(p(1 − p)) per observation, p = 0.1 + 0.8π'
version: 1
history:
- version: 1
  date: '2026-10-25'
  note: >-
    Filed from U28–U31 of the exchange. Amended the same day after the
    reading of Chaloner and Verdinelli (NOTE-tmpj2iwk): choosing probes is a
    nonlinear design problem, and a three-process D-optimal design is
    worked and certified. The inaccessible-probe caveat cites
    THEORY-tmpwtj3m.
standing: stipulated
kind: construction
tags:
- information-geometry
- mathematical-statistics
- self-governance
date: '2026-10-25'
line: distributed-agency
variant_of:
- CASE-152
illustrates:
- CLAIM-450
- CLAIM-444
summary: >-
  From the continuation of the exchange of 2026-10-24 (U28–U31), where it
  appears in four replies (A28 §3, A29's second priority, A30 §6A and
  A31's probe diagnostic); checked when filed. The categorical metric on
  authority shares is the one in which the replicator is a gradient flow
  ([CLAIM-444](../claims.d/CLAIM-444.md)). What an evaluator sees is the response mixture, whose
  Fisher metric is that metric pulled back through the processes' response
  profiles. Redistribution between processes that agree on the probes is
  invisible to them, and a probe on which they disagree restores it. The
  mixture counterpart of [CASE-152](CASE-152.md)'s product model.
---
<!-- inactive-ok-file: CLAIM-450 CLAIM-444 — Proposed; the claims this construction illustrates, nothing here rests on their being settled -->

# CASE-tmplg5jg: Authority geometry and response geometry: when an organization's response is the authority-weighted mixture p_π(y | c) = Σ πᵢ pᵢ(y | c), the Fisher metric of its responses is the pullback JᵀD⁻¹J of the categorical (Shahshahani) metric on the shares π and never exceeds it; it vanishes along any redistribution between processes that respond alike under the probes used, so two specialists who both answer yes with probability 0.8 in routine contexts carry no information about their shares there, while a rare context in which they answer 0.9 and 0.1 carries 0.64/(p(1 − p)) per observation, p = 0.1 + 0.8π

## The case

A stipulated toy. An organization's processes i = 1, …, k hold authority
shares π on the simplex. Under a probe context c, process i would respond
with pᵢ(y | c), and the organization's response is the mixture
p_π(y | c) = Σ πᵢ pᵢ(y | c). That is [CLAIM-444](../claims.d/CLAIM-444.md)'s mixture condition.
The profiles pᵢ are known; only π is to be learned.

- **Authority geometry.** If the evaluator saw which process answered, the
  Fisher metric on π would be the categorical one,
  g(v, w) = Σ vᵢwᵢ/πᵢ on tangent vectors (Σ vᵢ = 0). That is the
  Shahshahani metric, in which the replicator ascends a potential with
  dΦ/dt = Var_π(q) ([CLAIM-444](../claims.d/CLAIM-444.md), [CASE-155](CASE-155.md) part 3).
- **Response geometry.** Seeing only y, the metric is the pullback
  G_resp = Jᵀ diag(p_π)⁻¹ J, where J = ∂p_π/∂π along the simplex. Its
  columns are differences of the processes' profiles.
- **Never more.** The response y is the process index passed through a
  channel that does not depend on π, so G_resp ⪯ G_auth. That is
  [CLAIM-450](../claims.d/CLAIM-450.md)'s garbling inequality, applied to π.
- **Redundancy.** If p₁(· | c) = p₂(· | c) for every probe used, then
  Jv = 0 for v = e₁ − e₂, so g_auth(v, v) > 0 while G_resp(v, v) = 0. With
  π = (0.3, 0.7) the two values are 4.76 and 0.
- **A rare context.** Two specialists both answer yes with probability 0.8
  in routine contexts, and with probabilities 0.9 and 0.1 in a rare one.
  With π the first specialist's share, the routine response stays at 0.8,
  so I_routine(π) = 0. The rare response is p = 0.1 + 0.8π, so
  I_rare(π) = 0.64/(p(1 − p)): 2.56 at π = ½ and 3.33 at π = 0.2 or 0.8,
  against the authority metric's 1/(π(1 − π)) of 4 and 6.25. A31: "No
  number of routine observations can identify π from these responses
  alone. Rare-context observations can."

**Checked when filed**, by script (numpy): the pullback against the
Fisher information computed directly by finite differences of the log
likelihood; zero along the redundant direction; the smallest eigenvalue
of G_auth − G_resp on the tangent space nonnegative on 200 random
three-process, four-response mixtures; and the rare-context values above.

## Three redundancies

A29's table, kept because the record's distinctions need it: "Parameter
redundancy | Different parameter settings of a fitted model";
"Observational redundancy | Different organizations under the current
probe family"; "Functional redundancy | Organizations under all
interventions relevant to a declared task". "These need not coincide."
This case is the second without the first, since the profiles are known
and the model is regular in π. It says nothing about the third.

## Choosing the probes

Choosing a design ξ over contexts to maximize a criterion of
G_ξ = Σ_c ξ(c)G_c is a *nonlinear* design problem in Chaloner and
Verdinelli's sense (NOTE-tmpj2iwk), because the information depends on π.
An optimal design has to be stated at a guess of π or averaged over a prior
on it, and local optimality is the point-mass case (THEORY-tmpg6jfa).
Adaptive probing, which updates the guess between probes, should gain over
a fixed design there, as it does not in the normal linear model
(THEORY-tmpig9py). In the two-specialist case above the answer does not
depend on π: the routine context carries no information, so every
criterion that increases with information puts all mass on the rare one.

A three-process illustration, checked by script. Four contexts with
response profiles (rows contexts, columns processes) (0.8, 0.8, 0.8),
(0.9, 0.1, 0.5), (0.6, 0.6, 0.1) and (0.7, 0.75, 0.72), at
π = (0.5, 0.3, 0.2). The D-optimal design is ξ = (0, ½, ½, 0), all weight on
the two contexts that separate the processes. Its sensitivities
tr(G_ξ⁻¹G_c) are (0, 2, 2, 0.0097), none above the dimension 2 of the
tangent space, which certifies it by the equivalence theorem. Its log det
is −0.42, against −1.80 for the uniform design and −5.02 for a
routine-heavy one (0.85, 0.05, 0.05, 0.05). The values hold at this π
only.

## What it can show

That an organization can reorganize internally while its judgements stay
the same under the probes in use. That the remedy is a different probe,
not a different fit ([CLAIM-305](../claims.d/CLAIM-305.md)). A29: "If the experts differ on a rare
class of questions, the experiment should ask those questions. If they
differ only when given different authority, we need an authority
intervention." And that the geometry in which authority moves is not the
geometry in which evidence about it arrives.

## What it cannot show

- Anything when the profiles pᵢ are themselves unknown. The model is then
  singular where they coincide, and [CASE-152](CASE-152.md)'s analysis applies, not
  this one. A31: "we'd have to analyze the fitted likelihood rather than
  assume singularity implies a particular learning coefficient."
- That choosing probes well removes the problem. Probes on which the
  processes disagree must also be accessible to the evaluator, which is
  [QUESTION-271](../questions.d/QUESTION-271.md)'s failure of bandit feedback. An inaccessible probe is an
  action outside the set D of THEORY-tmpwtj3m, and what the remaining
  probes cannot see stays unlearnable however long they are used.
- That two processes that agree under the probes are the same
  communicative kind, or differ as one ([CLAIM-150](../claims.d/CLAIM-150.md)).
