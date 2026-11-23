---
number: 132
status: Open
formerly:
- QUESTION-tmp0885h
title: 'Under what conditions do initially equivalent adaptive operators differentiate into functionally complementary specialists that each have positive recovery growth when rare, rather than into roles kept in place by external load balancing or by persistent authority asymmetries?'
version: 8
history:
- version: 2
  date: '2026-10-21'
  note: >-
    Note of 2026-10-21 added, from the exchange of 2026-10-20 on effective
    description, agency and legibility: A19 §5 asked this question's
    alternative of institutions. The question is unchanged.
- version: 3
  date: '2026-10-29'
  note: >-
    Note of 2026-10-29 added, from the readings of Hofbauer and
    Schreiber, Chizat and Bach, Marsland et al., Power et al. and
    Letten et al. The question is unchanged.
- version: 4
  date: '2026-10-29'
  note: >-
    Note of 2026-10-29 added: in the symmetric potential case the
    invasion graph is acyclic (THEORY-1168); Ito and Kaneko a
    candidate case, not evidence; Chesson 1990 Unfetched and 1994
    Unavailable. The question is unchanged.
- version: 5
  date: '2026-11-22'
  note: >-
    Note of 2026-11-22 added: LEAD-065 run; Ito and Kaneko's core is
    refilled when removed and recovered when made rare (CASE-313,
    CLAIM-875). The question is unchanged.
- version: 6
  date: '2026-11-22'
  note: >-
    Note of 2026-11-22 added: LEAD-049's restricted theorem
    (CLAIM-885) and counterexample (CLAIM-886), checked in
    CASE-322. With residents frozen, recovery is assured under the
    theorem's conditions; against residents that re-adapt it can fail.
    The question is unchanged.
- version: 7
  date: '2026-11-22'
  note: >-
    Note of 2026-11-22 added: LEAD-016's run of CASE-117
    (CASE-341); the recovery exponent at rarity under
    softmax-gradient routing (CLAIM-918); refill pre-empts
    recovery (CLAIM-919). The question is unchanged.
- version: 8
  date: '2026-11-22'
  note: >-
    Note of 2026-11-22 added: Chesson (2011), the stand-in for Chesson
    1990, read (NOTE-tmp6d961, THEORY-tmpac7iw). Stable coexistence is
    recovery from low density; in the potential case the two-component
    recovery test is Chesson's criterion (CLAIM-tmpv65bg). The question
    is unchanged.
tags:
- complex-systems
- ecology
- self-governance
date: '2026-10-18'
line: distributed-agency
refines:
- QUESTION-083
summary: >-
  The central mathematical question of the synthesis the owner relayed on
  2026-10-18. [QUESTION-083](QUESTION-083.md) asks whether operators sharing one update rule
  can come to hold differentiated authority. This asks the coexistence
  version: does the differentiation produce stabilizing negative frequency
  dependence, meaning every specialist recovers when rare (Chesson's
  stabilizing mechanisms, [LIT-1219](../literature.d/LIT-1219.md), unread)? Or is it held in place
  from outside, or by one process's entrenched advantage? An answer is a
  population model that derives the interaction structure from learned
  contributions, states recovery criteria, and finds the regimes of
  coexistence and exclusion. Heterogeneous embeddings, unequal routing
  weights or persistent expert identities do not answer it.
---
<!-- inactive-ok-file: THEORY-tmpac7iw CLAIM-tmpv65bg — Proposed, filed by the lead run of 2026-11-22 and cited in the note of that date -->
<!-- inactive-ok-file: CASE-341 CLAIM-918 CLAIM-919 — Proposed, filed 2026-11-22 by LEAD-016's study and cited in the note of that date -->
<!-- inactive-ok-file: CLAIM-885 CLAIM-886 CASE-322 — Proposed, filed 2026-11-22 by LEAD-049 and cited in the note of that date -->
<!-- inactive-ok-file: CASE-313 CLAIM-875 — Proposed, filed 2026-11-22 by LEAD-065's study and cited in the note of that date -->
<!-- inactive-ok-file: CLAIM-362 — Proposed or Deferred; open claims, readings and works cited as open, nothing here rests on their being settled -->
<!-- inactive-ok-file: LIT-1219 — Unavailable since 2026-10-29; Chesson's stabilizing mechanisms, cited as the source of the first outcome's name, not reached, nothing here rests on it -->
<!-- inactive-ok-file: LIT-1826 LIT-1827 — Unfetched and Unavailable since 2026-10-29; Chesson 1990 and 1994, cited in the note of that date as not read, nothing here rests on them -->

# QUESTION-132: Under what conditions do initially equivalent adaptive operators differentiate into functionally complementary specialists that each have positive recovery growth when rare, rather than into roles kept in place by external load balancing or by persistent authority asymmetries?

## Why it is a question

Differentiation that is merely present does not show coexistence. Three
outcomes look alike from usage statistics and differ in kind:

1. **Stabilizing coexistence.** Each specialist, made rare, recovers
   because the resident organization leaves its niche open. This is
   Chesson's stabilizing mechanism ([LIT-1219](../literature.d/LIT-1219.md), unread).
2. **Imposed diversity.** Specialists persist because a programmed load
   balancer or a floor on influence keeps them from vanishing.
3. **Entrenched asymmetry.** One or a few processes hold authority
   through early advantage, the [CLAIM-277](../claims.d/CLAIM-277.md) loop, and the rest persist as
   residue.

**A recovery exponent.** Suppose operator i has influence w_i(t) and
contribution F_i(c_t, w_t), with ẇ_i = w_i F_i(c_t, w_t). Here w_i is an
unnormalized participation intensity. If influence is a normalized share,
the dynamics are of replicator type and F_i is measured against the
population mean ([CLAIM-369](../claims.d/CLAIM-369.md), "Two boundaries of application"). While the others
follow a resident regime and i is very rare, its long-run recovery
exponent is

  λ_i = lim_{T→∞} (1/T) ∫₀ᵀ F_i(c_t, w_{−i}(t)) dt,

when the limit exists along the resident dynamics. With discrete
multiplicative updates it is the average log growth factor. λ_i > 0 means
the rare specialist recovers from small positive influence. λ_i < 0 means
the resident organization drives it toward exclusion. It is a statement
about recovery, not about equal weights: a specialist can hold little
influence most of the time and still have λ_i > 0.

**A wrinkle.** A specialist useful only during rare events can have
negative average growth over the full context distribution and still be
critical when the event comes. Two quantities are worth separating:
λ_i^resident, the long-run recovery exponent, and λ_i^conditional(C), the
recovery exponent during a specified context class C. The second is not a
substitute for the ecological invasion rate. It may better capture what
[CLAIM-362](../claims.d/CLAIM-362.md) cares about, a process keeping access to consequential roles
when its contexts recur. A process may not merit continuous presence in
the active coalition and still merit preservation as a dormant
capability.

**An ablation the answer needs.** Because zero is absorbing under
multiplicative dynamics, recovery should first be tested from small
positive abundance or influence, n_i(0) = ε > 0. The specialist then
recovers or declines under the resident dynamics with no continuing
intervention. That is how an invasion exponent is normally evaluated.
Externally supplied reintroduction and internally maintained exploration
are distinct interventions. The first cannot establish endogenous
maintenance. The second may be an organizational mechanism of
persistence, and so may be one of the achievements under study, but its
origin, resource cost and causal role must be established independently.
The first filing said testing recovery "needs some reintroduction" and
put the supplying mechanism outside the organization. The owner's review
corrected both: the endogenous protection of rare specialists should not
be defined away before it is studied. A model does not exhibit
coexistence merely because a programmed lower bound on influence keeps
every operator above zero. Uniformity-promoting objectives
([THEORY-306](../theory.d/THEORY-306.md), the equal-cluster prior of joint-embedding objectives) are
the representation-learning version of imposed diversity. A specialist
useful 1% of the time need not be active 20% of the time because there
are five specialists.

**Three ways to keep a specialist.** Recovering influence when the context
returns is one achievement. The organization might instead:

1. maintain the specialist through **active participation**;
2. maintain it as a **dormant but recoverable** capability, kept without
   being continuously activated;
3. **reconstruct** a lost specialist through later learning.

These can differ greatly in cost and resilience. Dormant preservation is
the analogue of memory, organizational archives and protected minority
expertise. It is also why positive long-run invasion growth need not be
the only criterion of valuable coexistence. Whether retention without
activation is possible when training follows influence is
[QUESTION-134](QUESTION-134.md)'s question.

**Recovery of a retained specialist against adaptation during recovery.**
A returning specialist may regain influence because its old capability
is still useful, or because new training during the recovery makes it
useful again. Both are interesting, and they are different achievements.
The first is retention, which is the dormant case above. The second is
re-adaptation, which lies between dormancy and reconstruction. A recovery
measurement must say whether the specialist's parameters are frozen or
trainable while recovery is measured. With them frozen, a positive
recovery exponent shows that the retained capability is still valued.
With them trainable, it shows only that the specialist can become valued
again.

**Nonlinear transitions.** Coexistence and exclusion can change abruptly
with parameters, which bears on the open nonlinear-transition questions
([QUESTION-125](QUESTION-125.md); [CLAIM-330](../claims.d/CLAIM-330.md) on the coupled loop; [THEORY-136](../theory.d/THEORY-136.md) on what evidence
shows alternative stable states). A model with positive feedback and
exclusion is not thereby bistable, and it need not have a cusp. That has
to be shown in the model, not inferred from the ingredients.

## What would answer it

A population model in which:

- the interaction structure is derived from the operators' learned
  contributions, not assumed;
- the recovery criteria λ^resident and λ^conditional are stated;
- the parameter regimes of each of the three outcomes are found.

In the potential case [CLAIM-369](../claims.d/CLAIM-369.md) gives the recovery test as a marginal
value, s_i = −∂_i L. A restricted theorem would be a natural first
target. For symmetric competitive interactions and bounded niche
adaptation, find sufficient conditions under which a differentiated
equilibrium is locally asymptotically stable and every active specialist
has positive growth when reintroduced into the resident equilibrium
without it. Then ask which conditions fail when symmetry is relaxed,
adaptation is delayed ([THEORY-548](../theory.d/THEORY-548.md)), or training opportunities depend on
current influence ([QUESTION-134](QUESTION-134.md)). With more than two operators,
coexistence should be judged by invasion graphs (Hofbauer and Schreiber
2022), not pairwise tests.

## What would not answer it

Heterogeneous embeddings, unequal routing weights or persistent expert
identities. Mixture-of-experts routing already produces specialization,
and an answer must show more than it does ([QUESTION-083](QUESTION-083.md)'s note of
2026-10-18).

## Note of 2026-10-21: asked of institutions

A19 §5 of the exchange of 2026-10-20: "Symmetry breaking is not inherently
a failure ... We can distinguish desirable specialization from
problematic entrenchment only after specifying criteria beyond the
symmetry-breaking dynamics themselves". This is this question's
alternative, asked of institutions ([CLAIM-408](../claims.d/CLAIM-408.md)). A20's close ("may
also reflect genuine learning, merited expertise, and beneficial
specialization") is [QUESTION-100](QUESTION-100.md)'s and [QUESTION-087](QUESTION-087.md)'s.

## Note of 2026-10-29: invasion graphs, the mean-field flow, and three more readings

Hofbauer and Schreiber's invasion graphs, which "What would answer it"
names, are [LIT-1233](../literature.d/LIT-1233.md), now read ([NOTE-1379](../notes.d/NOTE-1379.md)). This question's λ_i is
exactly their r_i(µ), and the reading adds two conditions the question
should carry.

- Positive recovery at one resident regime is not enough. It must be
  positive at every −i community, which may be a much smaller community
  than all the others.
- Signs decide only if the invasion graph is acyclic. With cyclic
  replacement among operators, rock–paper–scissors among roles, every
  recovery exponent can be positive and coexistence still fail.

Chizat and Bach, [LIT-1232](../literature.d/LIT-1232.md) ([NOTE-1367](../notes.d/NOTE-1367.md)), give the question a hard
precondition in their model. Gradient flow transports mass and never
creates it, so recovery from rarity is available only where some mass
already sits. Units that start identical, at a single point rather than
spread over a separating set, cannot differentiate under gradient flow
alone. Their experiments show the cost: initialized on {1} × Θ, the flow
fails with 15 particles and succeeds with 30.

Three more readings bear.

- Marsland, Cui and Mehta, [LIT-1230](../literature.d/LIT-1230.md) ([NOTE-1352](../notes.d/NOTE-1352.md)): under symmetric
  resource competition, differentiated specialists that each recover from
  rarity are exactly the binding constraints, and assembly cannot undo an
  invasion except by killing species. Revision of authority in an
  analogue built on that class needs an external removal or an
  asymmetry.
- Power et al., [LIT-1235](../literature.d/LIT-1235.md) ([NOTE-1368](../notes.d/NOTE-1368.md)): the long-run breakdown, one
  attractor outcompeting the other, is an instance of the third outcome,
  entrenched asymmetry, emerging from initially balanced memory.
- Letten, Ke and Fukami, [LIT-1237](../literature.d/LIT-1237.md) ([NOTE-1377](../notes.d/NOTE-1377.md)), locate Chesson's
  stabilizing mechanism in impacts: an operator that limits itself more
  than others through what it does to a shared resource. Divergent
  requirements alone mostly equalize.

Chesson, [LIT-1219](../literature.d/LIT-1219.md), which the summary and the first outcome cite as
unread, is now Unavailable. The question is unchanged and stays Open.

## Note of 2026-10-29: acyclic in the potential case, a candidate case, and Chesson registered

- **The potential case.** [THEORY-1168](../theory.d/THEORY-1168.md) (Active), from Serván and
  Allesina, [LIT-1824](../literature.d/LIT-1824.md) ([NOTE-1422](../notes.d/NOTE-1422.md)): with a symmetric interaction
  matrix, rᵀx strictly increases along every edge of Hofbauer and
  Schreiber's invasion graph, so the graph has no cycles. In that class
  the second condition the earlier note of this date adds, that signs
  decide only if the invasion graph is acyclic, is met automatically.
  Cycles among roles need asymmetry, or a resource that can be excluded
  (the chapter's §3.5.4).
- **Ito and Kaneko**, [LIT-1842](../literature.d/LIT-1842.md) ([NOTE-1414](../notes.d/NOTE-1414.md)). Identical chaotic
  units with similarity-reinforced, normalized attention split into a core
  and a periphery. That looks like the third outcome, entrenched
  asymmetry, more than stabilizing coexistence: membership in the core is
  absorbing, and the core does not depend on the periphery (2 of about
  1,344 possible links run from periphery to core). But the paper measures
  no recovery when rare, no perturbation and no removal of a core unit. So
  it is a candidate case for this question's classification, not evidence
  for one outcome. Removing core units and seeing whether the periphery
  refills the core would decide it cheaply.
- **Chesson.** His 1994 paper, [LIT-1827](../literature.d/LIT-1827.md), whose "−i community" Hofbauer
  and Schreiber make rigorous, is registered and Unavailable. His 1990
  paper on MacArthur's consumer–resource model, [LIT-1826](../literature.d/LIT-1826.md), is
  registered and Unfetched: the author's reprint is located and could not
  be fetched. The first outcome's name still rests on no reading of
  Chesson.

The question is unchanged and stays Open.

## Note of 2026-11-04: a dormant specialist with negative recovery growth, from "Organizational Nucleation and SLT"

This question already separates a specialist kept active from one kept "dormant but recoverable". [CASE-117](../cases.d/CASE-117.md) measures recovery with frozen parameters. A8's Proposal D, answering the owner's U8, adds explicit numbers:

- A specialist useful in a rare context, of probability 0.01, has active intensity multiplied by 0.99 in ordinary contexts and by 2 in its own.
- Its long-run growth exponent is λ = 0.99 log 0.99 + 0.01 log 2 ≈ −0.00302. The reader checked it.
- So it declines when rare.
- An organization that keeps an archive of the capability and a reactivation channel keeps it recoverable.

A8: "What is missing is an explicit construction where **the ecological recovery exponent is negative while task-relevant organizational recoverability remains positive**." And: "A demand might concern the organization's **capacity to produce a response when needed**, rather than the uninterrupted activity of a particular specialist."

A8 states the costs such a comparison must charge: the archive, the detector and the reactivation mechanism, and "which processes maintain them". A8 also asks a question of individuation: "when a dormant specialist is reconstructed rather than reactivated, what continuity of capacity or organizational history remains?"

The example restates this question's dormant case with numbers. It is not filed as a CASE.

No status changes.

## Note of 2026-11-19: Hessel, Tan and Lee, read
An analogy only ([NOTE-2164](../notes.d/NOTE-2164.md)): Hessel, Tan and Lee's "complementary rather than competitive" spinoffs concern individual users' short-term activity, not recovery when rare or coexistence in the ecological sense.

## Note of 2026-11-22: the candidate case tested

The note of 2026-10-29 left Ito and Kaneko ([LIT-1842](../literature.d/LIT-1842.md)) as a candidate
case and named a cheap test, which [LEAD-065](../leads.d/LEAD-065.md) has now run ([CASE-313](../cases.d/CASE-313.md),
12 seeds at the paper's parameter point).

- Delete the whole core, and former periphery units form a new one of
  the same size, 17.2 ± 0.8 against 17.0 ± 1.1 in a same-sized control.
  The new core has the same one-way structure.
- Cut the core's influence to 10⁻³, with no further intervention, and its
  own members regain it.

So the asymmetry is not held by its first holders' early advantage.
[CLAIM-875](../claims.d/CLAIM-875.md) files two readings for the owner. In one, this is the first
outcome at the level of roles. In the other, it is a fourth outcome the
question does not name: a differentiation that regenerates around
interchangeable holders, with no niche for any particular specialist. The
recovery of a periphery unit made rare was not tested.

The question is unchanged and stays Open.

## Note of 2026-11-22: the restricted theorem, and where it stops

[LEAD-049](../leads.d/LEAD-049.md) took up the "natural first target" that "What would answer it"
names. The class is [CLAIM-369](../claims.d/CLAIM-369.md)'s symmetric resource competition with
nonnegative niche vectors u(θ_i). Each operator's trait is confined to a
box, the bounded adaptation, and moves up the rare-mutant selection
gradient. Operators share one niche map, so they are initially equivalent
up to their traits. The whole system is a gradient flow of [CLAIM-369](../claims.d/CLAIM-369.md)'s
objective L.

- **Sufficient conditions for a stable differentiated equilibrium**
  ([CLAIM-885](../claims.d/CLAIM-885.md), Theorem A). Each trait is interior and stationary, or
  held at its bound by a strictly outward gradient. The Hessian of L on the
  free coordinates is positive definite. That Hessian contains the Gram
  matrix, so the specialists' niche vectors must be linearly independent.
  An equilibrium in which two present operators share a trait is never
  asymptotically stable. Exactly identical operators stay identical. In
  [CASE-322](../cases.d/CASE-322.md)'s Gaussian-niche runs, operators started 10⁻³ apart
  differentiate to equilibria meeting these conditions whenever the
  niche space has room for them all (22 of 27 runs). With too many, some
  pair up on near-identical traits.
- **Recovery when rare, residents frozen** (Theorem B). Every specialist
  has λ_i ≥ n*_i d_i² > 0. This is the question's frozen measurement,
  against the −i community, and it holds at every such community, since
  that community is unique at fixed traits.
- **Recovery against re-adapted residents** (Theorem C). It is positive if
  the frozen −i community itself meets Theorem A. Otherwise it can fail.
  [CLAIM-886](../claims.d/CLAIM-886.md) gives a two-resource trade-off in which a stable pair of
  specialists coexists with a stable lone generalist. A specialist
  returning against that generalist has growth −c/5. A lone resident
  leaves its corner for the vacated resource whenever c/B < a'(0)/a'(1),
  and in [CASE-322](../cases.d/CASE-322.md)'s runs it then ends at the generalist. In the
  Gaussian-niche runs the condition never held, since residents always
  moved into the vacancy. Recovery stayed positive, but at a median 0.29
  of the frozen rate.

What the lead's "What would count" asked: a theorem for the class, and a
counterexample. Both are now filed. The counterexample does not show that
differentiation needs more than competition and bounded adaptation, since
the pair is stable. It shows that recovery when rare against residents
that have had time to re-adapt needs more. What it needs, in that
instance, is a trade-off under which the vacated niche is not worth
entering (c/B > a'(0)/a'(1)), or a generalist that leaves room
(a(1/2) < 1/2).

This bears on the question's distinctions. Its frozen and trainable
measurements part: frozen residents give positive recovery, re-adapted
ones negative. Its third outcome appears in an unexpected form, an
alternative stable state of one generalist that removal can tip the
system into. Whether that is "entrenched asymmetry" or a further outcome
is left to the owner ([CLAIM-886](../claims.d/CLAIM-886.md)).

Not attempted: asymmetric interactions, delayed adaptation ([THEORY-548](../theory.d/THEORY-548.md)),
influence-dependent training ([QUESTION-134](QUESTION-134.md)), invasion graphs with
adaptive traits, and a trainable returning specialist.

The question is unchanged and stays Open.

## Note of 2026-11-22: operators with functions, recovery when rare, and refill

[LEAD-016](../leads.d/LEAD-016.md) ran a reduced version of [CASE-117](../cases.d/CASE-117.md) ([CASE-341](../cases.d/CASE-341.md)). It used
linear operators identical but for initialization, with four contexts, one
rare. Every rule tried differentiated them into one specialist per context,
the rare one included.

- **The test from a small positive start.** Each specialist was frozen
  and given share 10⁻³ or 10⁻⁵, with no further intervention. With no
  spare operator, it recovered under a multiplicative contribution rule
  at a rate that does not depend on its starting share. It also recovered
  under ordinary mixture-of-experts gating, but at a rate proportional to
  that share, and not from 10⁻⁵ within the window.
- **A caution for this question's λ_i.** [CLAIM-918](../claims.d/CLAIM-918.md) derives the
  proportionality. Under any softmax router trained by gradient, the
  recovery exponent at rarity tends to a value that does not depend on
  the operator's competence. A balancing loss in the gradient does not
  change that.
- **The second outcome, measured.** A usage bias, an imposed balancer
  outside the gradient, raised an incompetent copy to 0.19 of the rare
  context. The multiplicative rule drove it out.
- **With two spare operators.** A spare refilled a removed specialist's
  niche every time. It also took the niche of a suppressed specialist,
  which then stayed shut out with its competence intact ([CLAIM-919](../claims.d/CLAIM-919.md)).
  The rare specialist's recovery was near zero where a spare had
  co-learned its job (residual direction d² ≈ 0).

[CLAIM-875](../claims.d/CLAIM-875.md)'s two readings return here, now with a functional niche. The
role is regenerated, but its particular holder is not kept. [CLAIM-919](../claims.d/CLAIM-919.md)
files the same two readings for the owner.

The question is unchanged and stays Open.

## Note of 2026-11-22: Chesson read, through his own restatement

The note of 2026-10-29 ends: "The first outcome's name still rests on no
reading of Chesson." His 1990 paper, [LIT-1826](../literature.d/LIT-1826.md), is still Unfetched, and
his 1994 paper, [LIT-1827](../literature.d/LIT-1827.md), still Unavailable; both were sought again on
this date. His 2011 chapter, [LIT-tmp7sngn](../literature.d/LIT-tmp7sngn.md), which restates the 1990
reworking of MacArthur's model, is read in full ([NOTE-tmp6d961](../notes.d/NOTE-tmp6d961.md),
[THEORY-tmpac7iw](../theory.d/THEORY-tmpac7iw.md)). Three things bear here.

- **The first outcome's test is Chesson's.** "[B]y stable coexistence, a
  stable equilibrium is not implied. Instead, the requirement is recovery
  of each species from low density, which is fully compatible with
  fluctuating coexistence" (§2.2, p. 49). That is this question's λ_i > 0
  against the resident regime, not equal weights and not a fixed point.
  The words "stabilizing" and "equalizing" are not in the chapter; they
  are Chesson (2000), [LIT-1219](../literature.d/LIT-1219.md), still Unavailable.
- **In the potential case the test has a closed form for two
  components.** MacArthur's model is [CLAIM-369](../claims.d/CLAIM-369.md)'s class, and a rare
  component's growth against a lone resident is ‖u_i‖(κ_i − ρκ_j), with
  ρ the cosine of the niche vectors and κ_i = r_i/‖u_i‖
  ([CLAIM-tmpv65bg](../claims.d/CLAIM-tmpv65bg.md)). Both recover when rare exactly when
  ρ < κ_i/κ_j < 1/ρ. So overlap alone does not decide the first outcome:
  a component with a distinct niche, ρ small, can still be excluded by a
  large enough fitness gap. That is [CASE-118](../cases.d/CASE-118.md)'s "feature geometry alone
  does not fix coexistence", in Chesson's terms.
- **Neutral is not the first outcome.** With ρ = 1 and equal κ, nothing
  recovers from low density (p. 49). Identical operators sharing one niche
  are in that state, which agrees with [CLAIM-885](../claims.d/CLAIM-885.md)'s finding that exactly
  identical operators stay identical.

The chapter's criterion is pairwise. With more than two operators, the
earlier note's conditions stand: recovery at every −i community, and an
acyclic invasion graph, which [THEORY-1168](../theory.d/THEORY-1168.md) gives in the potential case.

The question is unchanged and stays Open.
