---
status: Open
title: 'For finite resource-graded transition systems, when do the distinctions drawn by enriched Yoneda profiles, restricted to declared probes, agree with those drawn by behavioural equivalence and bisimulation pseudometrics, and what does each remember that the other forgets?'
version: 1
tags:
- mathematics
- individuation
- epistemology
date: '2026-11-05'
line:
- formal-apparatus
refines:
- QUESTION-tmptcuch
summary: >-
  A's question, from the owner's paste of 2026-11-05 (fourth), A's "Toward a
  resource-sensitive Yoneda theory of individuation" §10: compare "A
  categorical or enriched-Yoneda approach that characterizes configurations
  through their structured relations to other configurations" with "A
  coalgebraic approach that characterizes states through their possible
  future observable behaviors", asking "whether the same resource-bounded
  distinctions arise from both constructions"; agreement under stated
  conditions would be a theorem, and disagreement would show "what each
  framework remembers and forgets". The record holds bisimulation metrics
  ([THEORY-247](../theory.d/THEORY-247.md), [THEORY-280](../theory.d/THEORY-280.md)) and enriched profiles ([CLAIM-tmpxcbet](../claims.d/CLAIM-tmpxcbet.md),
  [TERM-tmpvb0eg](../terms.d/TERM-tmpvb0eg.md)) and no entry joining them. The filer's smallest example,
  checked with python3 -I, shows the full profiles and bisimulation
  disagreeing and the comparison worth making only for restricted
  profiles. The wording is A's; adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-tmp0d5si CLAIM-tmpe18y0 CLAIM-tmpg7w69 CLAIM-tmpxcbet QUESTION-008 TERM-tmpckwjg TERM-tmpvb0eg — Proposed or Deferred; A's proposals of 2026-11-05 and the entries filed beside them, and the record's deferred question on approximate bisimulation, cited as filed, nothing here resting on their being settled -->

# QUESTION-tmpjcbyk: For finite resource-graded transition systems, when do the distinctions drawn by enriched Yoneda profiles, restricted to declared probes, agree with those drawn by behavioural equivalence and bisimulation pseudometrics, and what does each remember that the other forgets?

## Why it is a question

A (§10): "For computational processes that evolve and respond to inputs,
coalgebraic behavioral equivalence and bisimulation may be more
immediately applicable than ordinary representable presheaves. These
theories classify states according to their observable behavior under
transitions." "The approaches are related but not interchangeable. A
useful research question would be whether the same resource-bounded
distinctions arise from both constructions in selected classes of origami
mechanisms. If they agree under specified conditions, we could identify
those conditions as a theorem. If they disagree, the counterexamples may
reveal what each framework remembers and forgets." And the guard: "A
Yoneda profile is not automatically a behavioral theory of an evolving
system. The transition semantics must be supplied."

**What the record holds on each side.** Behavioural: [THEORY-247](../theory.d/THEORY-247.md), the
discounted bisimulation metric of finite action-free labelled Markov
chains as a bicausal optimal-transport distance, and [THEORY-280](../theory.d/THEORY-280.md), its
estimation from samples; [QUESTION-190](QUESTION-190.md) asks about that estimate's sample
complexity. The resource-aware form is named in [TERM-tmpckwjg](../terms.d/TERM-tmpckwjg.md) and
[CLAIM-tmpe18y0](../claims.d/CLAIM-tmpe18y0.md) as the equivalence for universality, "a resource-aware
bisimulation", and [QUESTION-008](QUESTION-008.md) asks it of communicative systems.
Relational: enriched profiles that keep a threshold ([CLAIM-tmpxcbet](../claims.d/CLAIM-tmpxcbet.md)) and
recover an additive distance ([CASE-tmp0d5si](../cases.d/CASE-tmp0d5si.md)), restricted profiles at a
budget ([CLAIM-tmpg7w69](../claims.d/CLAIM-tmpg7w69.md)), and the incoming, outgoing and observational
profiles of [TERM-tmpvb0eg](../terms.d/TERM-tmpvb0eg.md). No entry compares the two.

**Why the full profiles are the wrong comparison (the filer's).** Take
states S, X, Y and Z with moves S → X costing 1, S → Y costing 5, and
X → Z and Y → Z each costing 1, costs adding. X and Y are bisimilar: each
has one move, of cost 1, to Z. Their incoming profiles over (S, X, Y, Z)
are (1, 0, ∞, ∞) and (5, ∞, 0, ∞), and their outgoing ones (∞, 0, ∞, 1)
and (∞, ∞, 0, 1). Both profiles separate X from Y, as Yoneda says they
must for any two non-isomorphic objects, since each profile includes the
object's own identity. Bisimulation forgets where a state is and how it
was reached; the full profile forgets nothing. Restricted to the probes
{S, Z}, the outgoing profiles agree, (∞, 1) for both, as bisimulation
does, and the incoming ones still differ at S, 1 against 5. So the
question is about restricted profiles: which probe families make the
profile's distinctions those of a behavioural pseudometric, and whether
the incoming direction, the cost of producing a state, has any
behavioural counterpart. Checked with python3 -I by partition refinement
and shortest paths.

## What would answer it

For a stated class of finite resource-graded transition systems, with a
declared transition semantics and probe family: a theorem that the
profile pseudometric restricted to the family equals, or is within a
stated factor of, a stated behavioural pseudometric, under conditions
that are named; or a counterexample in each direction, a pair the
profiles separate and the behaviour identifies, and a pair the behaviour
separates and the profiles identify, with what each keeps. Either would
answer it for that class, as A proposes for "selected classes of origami
mechanisms".

## What would not answer it

- **The example above.** It shows that the full profiles and bisimulation
  differ, which follows from Yoneda; the question concerns restricted
  families and behavioural metrics.
- **A profile with no transition semantics.** A: "The transition semantics
  must be supplied."
- **Agreement under probes chosen to agree.** [CLAIM-322](../claims.d/CLAIM-322.md): such probes show
  only that they can be selected.
