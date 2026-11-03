---
status: Active
title: 'A construction of self-formation: an agent''s own frustration at two demands one shared output cannot meet drives production of a sensor and a differentiating channel that then maintain each other; past a threshold of discrepancy (D ≈ 0.645 at unit drive) the capacity forms, outlasts the conflict, meets later conflicts of the same class up to D ≈ 1.047 with no frustration, and is lost at damage 0.5; a capacity upheld from outside is told apart by knockouts afterwards, but one installed by an outside pulse and then self-maintained is told apart only by a knockout during formation'
version: 1
standing: fictional
kind: construction
tags:
- agency
- complex-systems
date: '2026-11-03'
line:
- will-organization
variant_of:
- CASE-189
- CASE-115
illustrates:
- CLAIM-tmpbeh2e
- CLAIM-516
- CLAIM-522
summary: >-
  Built at the owner's request ("build the [CASE-189](CASE-189.md) extension") to test
  [CLAIM-tmpbeh2e](../claims.d/CLAIM-tmpbeh2e.md), the positive account of self-formation filed from U33 of
  the exchange "Assess SDT Coverage". scratch/formal/self_formation.py.
  Fictional and stipulated: the sensor and channel are capacity variables
  present from the start, raised from zero, as [CASE-189](CASE-189.md)'s are. It bears out
  the claim's first test (transfer within a class) and qualifies its
  second: a knockout of the producing process separates own formation from
  outside installation only if it is made during formation. After the
  fact the two are the same organization.
---
<!-- inactive-ok-file: THEORY-040 THEORY-1118 THEORY-328 THEORY-047 THEORY-054 QUESTION-011 QUESTION-071 QUESTION-118 QUESTION-364 CLAIM-404 TERM-066 CLAIM-329 CLAIM-tmpxpdqi — Proposed, Open or Deferred; the entries on which provenance matters, cited as open -->
<!-- inactive-ok-file: CLAIM-tmpbeh2e — Proposed; the claim this construction tests -->

# CASE-tmph9iwi: A construction of self-formation: an agent's own frustration at two demands one shared output cannot meet drives production of a sensor and a differentiating channel that then maintain each other; past a threshold of discrepancy (D ≈ 0.645 at unit drive) the capacity forms, outlasts the conflict, meets later conflicts of the same class up to D ≈ 1.047 with no frustration, and is lost at damage 0.5; a capacity upheld from outside is told apart by knockouts afterwards, but one installed by an outside pulse and then self-maintained is told apart only by a knockout during formation

## The construction

An agent acts in two contexts, A and B, with targets a and b, D = |a − b|. As
in [CASE-115](CASE-115.md), one shared output cannot meet both. Its output is
y_k = x + s_k·u·z with s_A = +1, s_B = −1, a shared level x and a
differentiating command z ∈ [−1, 1]. How far it can differentiate is
u = σ(S)σ(G), σ(c) = c/(1 + c), where S is its capacity to tell A from B, a
sensor, and G its capacity to act differently on them, a channel. With x and z
adapting fast, its residual frustration is F(u, D) = max(0, D/2 − u)².

The capacities are slow:

- Ṡ = αF + βP(G) + e_S(t) − (1 + d)S
- Ġ = αF + βP(S) + e_G(t) − (1 + d)G
- P(c) = 3c²/(1 + c²)

αF is production driven by the agent's own frustration, the "own activity on a
discrepancy" of [CLAIM-tmpbeh2e](../claims.d/CLAIM-tmpbeh2e.md). βP is the mutual production by which sensor
and channel maintain each other, [CASE-189](CASE-189.md)'s Construction 1. e(t) is any outside
supply, and d damage on turnover.

## Results

All from scratch/formal/self_formation.py (scipy's solve_ivp, rtol 10⁻⁹).

**The maintained state.** With no frustration, S = G = (3 + √5)/2 ≈ 2.618 is
stable, with a saddle at (3 − √5)/2 ≈ 0.382 and extinction at 0. There
u ≈ 0.5236, so the formed capacity resolves any D ≤ 1.0472.

**Formation, persistence and transfer.** Discrepancy D = 1 on t < 20, none on
20–60, a new discrepancy of the same class, D = 0.8, on 60–80.

| system | S(20) | S(59) | ∫F on [0, 20] | ∫F on [60, 80] |
|---|---|---|---|---|
| self-forming (α = 1, β = 1) | 2.618 | 2.618 | 0.794 | 0.000 |
| no maintenance cycle (β = 0) | 0.219 | 0.000 | 4.406 | 2.955 |
| same agent, never exposed | 0 | 0 | 0 | 0.876 |

The self-forming agent meets the later conflict with no frustration. An agent
of the same kind that was never exposed must form the capacity first, at a cost
of 0.876. Without the maintenance cycle the capacity only tracks the
frustration that drives it, never resolves the conflict, and is gone once the
conflict ends.

**Thresholds.** At D = 1, formation needs α > 0.390. At α = 1 it needs
D > 0.645: smaller discrepancies are tolerated, at a standing frustration, and
form nothing.

**The class is bounded.** A later D = 1.6 exceeds what was formed. The capacity
stretches, S from 2.618 to 2.712, but frustration stays at 0.071, and S
returns to 2.618 when the conflict ends.

**Provenance.** Three agents reach the same maintained state, S = 2.618 at
t = 29:
- *own*, formed by its frustration;
- *pulse*, with no frustration-driven production (α = 0) and an outside supply
  of 3 on t < 2, then its own maintenance;
- *upheld*, with no internal maintenance (β = 0) and an outside controller
  supplying P(G) and P(S) as feedback; its trajectory equals own's to
  machine precision ([CLAIM-522](../claims.d/CLAIM-522.md)).

| knockout | own | pulse | upheld |
|---|---|---|---|
| internal maintenance, from t = 30 | 0 | 0 | 2.618 |
| outside supply, from t = 30 | 2.618 | 2.618 | 0 |
| frustration-driven production, from t = 0 | 0 | 2.618 | 0 |

Upheld is told apart afterwards. Own and pulse are not: after formation they
are the same organization, and only a knockout made during formation
separates them.

**Damage.** With constant damage on turnover after formation, the capacity
settles at 1.730 for d = 0.3 and 1.299 for d = 0.45. At d = 0.5 it approaches
the fold at 1 (critical slowing, 1.003 at t + 400), and at d = 0.55 it is lost,
as in [CASE-189](CASE-189.md)'s Construction 1.

## What it shows and does not

It shows [CLAIM-tmpbeh2e](../claims.d/CLAIM-tmpbeh2e.md)'s account working in a model. A discrepancy the agent
cannot meet drives production of a distinction and a channel. The capacity
outlasts the discrepancy because sensor and channel maintain each other
([CLAIM-516](../claims.d/CLAIM-516.md)'s productive cycle), and it serves later discrepancies of the same
class, which the claim's first test detects.

It qualifies the claim's second test. Interventions on the processes that
produce and maintain a capacity tell an agent that formed it from one in which
it is upheld from outside. But they tell it from one in which it was installed
from outside and then self-maintained only if made during formation. After the
fact the history leaves no trace, which is [QUESTION-071](../questions.d/QUESTION-071.md)'s point for
self-formation.

## Why the provenance result matters

That a self-maintained capacity's origin leaves no trace in its present
organization would be idle if nothing turned on origin. The record holds
several entries on which something does.

- **Responsibility and freedom.** On structural accounts of free agency, a
  condition stated only in present psychological structure is met by an agent
  whose structure a manipulator installed ([THEORY-040](../theory.d/THEORY-040.md); McKenna and Coates,
  [THEORY-1118](../theory.d/THEORY-1118.md)). The "pulse" agent here is that agent in miniature: installed
  once, then self-maintaining, indistinguishable afterwards. So the
  construction is a case for the historical condition those entries say such
  accounts need. Fischer and Ravizza's ownership is historical, by taking
  responsibility ([THEORY-121](../theory.d/THEORY-121.md)). Kane's ultimate responsibility is the strongest
  such condition ([CLAIM-022](../claims.d/CLAIM-022.md)'s note of 2026-11-02). And Pereboom's four-case
  argument ([THEORY-328](../theory.d/THEORY-328.md)) is the warning that a historical condition may not
  separate the installed agent from an ordinarily caused one either.
- **Whose the will is.** Explaining efficacy does not settle whose the will is
  ([CLAIM-022](../claims.d/CLAIM-022.md)), and what makes a will-organization the agent's own is
  [QUESTION-011](../questions.d/QUESTION-011.md). Both hold only with a historical condition, and this
  construction shows the present cannot supply one.
- **Reflexive control.** An outside pulse that leaves the agent maintaining
  what was installed is [CLAIM-404](../claims.d/CLAIM-404.md)'s informational route and [CASE-123](CASE-123.md)'s
  one-time-perturbation variant, interpretive capture ([TERM-066](../terms.d/TERM-066.md)) that needs no
  continued control. This is the dynamics that makes it undetectable after the
  fact. [CLAIM-tmpxpdqi](../claims.d/CLAIM-tmpxpdqi.md)'s domination clause, another's capacity to govern one's
  governing relations whether used or not, is the standing form of the same
  vulnerability.
- **Autonomy as psychology measures it.** Self-determination theory holds that
  how a regulation was taken in, under controlling or supportive conditions,
  shapes how autonomous acting on it is ([THEORY-047](../theory.d/THEORY-047.md)). If that is right, an
  outside-installed and a self-formed capacity must differ somewhere this model
  lacks, for instance in how the capacity is integrated with the agent's other
  demands ([THEORY-054](../theory.d/THEORY-054.md)). The construction locates where to look: not in the
  capacity, which is identical, but in its relations to the rest.
- **Endorsement in advance.** The voluntary delegation of [CASE-128](CASE-128.md) differs from
  an imposed restriction only in how it came about. The record already counts
  that difference as one of self-governance.
- **The counterweight.** An objective that originates outside a learning system
  can still become its goal ([CLAIM-356](../claims.d/CLAIM-356.md)). Exogenous origin does not by itself
  disqualify; the entries above say what more, on each view, would.
- **Persistence.** For collectives the record already holds that what persists
  is what is causally transmitted, not what resembles ([CLAIM-329](../claims.d/CLAIM-329.md),
  [QUESTION-118](../questions.d/QUESTION-118.md)). Whether a self-formed capacity continues the agent's will is
  the same question asked of a capacity ([QUESTION-364](../questions.d/QUESTION-364.md)).

**The view it qualifies.** Juarrero ([LIT-tmpw5nxr](../literature.d/LIT-tmpw5nxr.md), [NOTE-tmpv0g6b](../notes.d/NOTE-tmpv0g6b.md)) holds that
coherent dynamics "carry their history on their backs" (p. 75) and "make
manifest the context and the moment in which they were created" (p. 76). Her
examples, graphite and diamond, are different attractors reached by different
routes. Here one attractor is reached by two routes and keeps no trace of which,
so the construction limits her general claim without contradicting her
examples. Her self-determination is closure, a present, maintenance-provenance
notion with no formation condition (pp. 93–94).

It does not show a new variable coming to be. S and G are in the model from the
start, and formation raises them from zero, so this is a bistable system pushed
across a separatrix, as [CASE-189](CASE-189.md) says of itself. The "class" is fixed by the
stipulated cue: the sensor tells A from B and nothing else. The production terms
are not paid for thermodynamically ([CASE-189](CASE-189.md)'s notes of 2026-10-31).
