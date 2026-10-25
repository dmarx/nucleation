---
status: Active
title: 'Authority geometry and response geometry: when an organization''s response is the authority-weighted mixture p_π(y | c) = Σ πᵢ pᵢ(y | c), the Fisher metric of its responses is the pullback JᵀD⁻¹J of the categorical (Shahshahani) metric on the shares π and never exceeds it; it vanishes along any redistribution between processes that respond alike under the probes used, so two specialists who both answer yes with probability 0.8 in routine contexts carry no information about their shares there, while a rare context in which they answer 0.9 and 0.1 carries 0.64/(p(1 − p)) per observation, p = 0.1 + 0.8π'
version: 1
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
  [QUESTION-tmpdicvf](../questions.d/QUESTION-tmpdicvf.md)'s failure of bandit feedback.
- That two processes that agree under the probes are the same
  communicative kind, or differ as one ([CLAIM-150](../claims.d/CLAIM-150.md)).
