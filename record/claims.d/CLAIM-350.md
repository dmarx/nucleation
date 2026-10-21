---
number: 350
status: Active
formerly:
- CLAIM-tmpa1kmr
title: 'A coarse-graining preserves a deterministic judgment exactly when the judgment is constant on its fibres: the judgment then factors through the coarse description, uniquely on its image, and otherwise two states the judgment tells apart have been merged'
version: 2
history:
- version: 2
  date: '2026-10-21'
  note: >-
    Note of 2026-10-21 added, from the exchange of 2026-10-20 on effective
    description, agency and legibility: A12 and A13 proposed TERMs for
    identifiability relative to an observational regime and for
    target-preserving coarse-graining; both are this claim's condition, so
    no TERM is filed. Extended the same day: the causal-abstraction readings give the distributional criterion beside this claim's fibre-wise one. The claim is unchanged.
role: granted
warrant: demonstrated
tags:
- mathematics
- mathematical-statistics
date: '2026-10-18'
line:
- pragmatic-transport
- formal-apparatus
complements:
- CLAIM-152
summary: >-
  A21 §3 and §18 (Candidate 1) of the exchange of 2026-10-17, and A22's
  Construction A: for a judgment J and a coarse-graining C on the same
  states, J = j∘C for some j exactly when C(x₁) = C(x₂) implies J(x₁) =
  J(x₂). Granted, because it is elementary (the universal property of a
  quotient) and Ak's; the proof is in the body. It is [CLAIM-152](CLAIM-152.md)'s
  judgment-valued special case with the converse added: [CLAIM-152](CLAIM-152.md) says a
  partition sufficient for one target need not be for another, and this
  says which partitions serve a deterministic judgment, those whose
  fibres lie inside its level sets, so the coarsest is the judgment's own
  partition. The sharp edge: it says when a description keeps a
  judgment, never whether the judgment is right. A21's probabilistic and
  causal versions are recorded in the body, not claimed.
supports:
- CLAIM-348
- CLAIM-tmppi0xf
---
<!-- inactive-ok-file: CLAIM-127 — Proposed; cited in the note of 2026-10-21, nothing here rests on it -->

# CLAIM-350: A coarse-graining preserves a deterministic judgment exactly when the judgment is constant on its fibres: the judgment then factors through the coarse description, uniquely on its image, and otherwise two states the judgment tells apart have been merged

## The claim

A21 §3, under the owner's U21 ("flesh this out further, and look for more
connections on the nucleation record"): "For a deterministic judgment
\(Y=J(X)\) and deterministic coarse-graining \(Z=C(X)\), the following are
equivalent: 1. There exists a function \(j\) such that \(Y=j(Z)\). 2.
Whenever \(C(x_1)=C(x_2)\), we have \(J(x_1)=J(x_2)\)." Its gloss: "**A coarse
description is adequate for a normative judgment exactly when it does not
merge states that the judgment must distinguish.**" A20 had stated the
condition one turn earlier as a one-way test. A22 made it the manuscript's
Construction A, "Elementary demonstrable result".

## Proof

Let C: X → Z and J: X → Y be any functions on one set of states X.

- **If J = j∘C, J is constant on C's fibres.** If C(x₁) = C(x₂), then J(x₁) =
  j(C(x₁)) = j(C(x₂)) = J(x₂).
- **If J is constant on C's fibres, J = j∘C.** For z in the image C(X),
  choose any x with C(x) = z and set j(z) = J(x). Another choice x′ has
  C(x′) = z = C(x), so J(x′) = J(x), and j is well defined. Then J(x) =
  j(C(x)) for every x.
- **j is unique on the image, and free off it.** Two such maps agree at
  every z = C(x), since both equal J(x) there. Values at points of Z that no
  state reaches are unconstrained.

Equivalently, C preserves J exactly when the partition of X into C's fibres
refines the partition into J's level sets. The coarsest coarse-graining that
preserves J is therefore J's own partition, x ↦ J(x). A different judgment
has different level sets and so a different coarsest description, which is
[CLAIM-152](CLAIM-152.md)'s target-relativity stated for judgments.

## How it stands to [CLAIM-152](CLAIM-152.md)

[CLAIM-152](CLAIM-152.md) holds that a sufficient statistic is sufficient for a target, so
the partition that wins depends on the target ("fix the outcomes differently
and a different partition wins"). For a target that is a deterministic
function J of the state, "C is sufficient for J(X)" and "J is constant on
C's fibres" coincide (up to null sets, when X carries a distribution). So
this claim is [CLAIM-152](CLAIM-152.md)'s judgment-valued special case. What it adds is the
converse: [CLAIM-152](CLAIM-152.md) says which partitions can fail, and this says exactly
which succeed.

## A21's further statements, recorded, not claimed

A21 §18: "probabilistic and decision-theoretic versions require preservation
of the corresponding conditional distributions or achievable risks." Each
needs its own statement:

- **Probabilistic.** For finite X with every state of positive probability,
  C is sufficient for a random judgment Y (P(Y | X) = P(Y | C(X))) exactly
  when the map x ↦ P(Y | X = x) is constant on C's fibres. That is the
  proof above applied to that map: if P(Y | X = x) = g(C(x)), averaging over
  the fibre gives P(Y | C = z) = g(z); conversely, if P(Y | X = x) =
  P(Y | C = C(x)), it is a function of C(x). Checked here for the finite
  case only.
- **Decision-theoretic.** Preservation of achievable risk over a declared
  family of decisions is Blackwell's order ([THEORY-156](../theory.d/THEORY-156.md)), not this lemma.
  A bounded decision-loss criterion (A21 §12, D(C) = E[L(J(X), Ĵ(C(X)))])
  is a definition, and choosing its loss L is, as A21 says of one such
  choice, "itself normative".
- **Causal.** A21 §6's condition C_*(P_ℓ^{do(a)}) = P_L^{do(ā)}, for a
  declared family of interventions, defines intervention-consistent
  coarse-graining. It is a definition, not a theorem, and it holds only
  relative to the macro-interventions ā, whose meaning [QUESTION-115](../questions.d/QUESTION-115.md) asks
  about.

## What it does not say

- **That the judgment is correct.** A22: it "establishes the adequacy of an
  abstraction for a specified judgment, not the correctness of the
  judgment's underlying standard."
- **That a description adequate for one judgment is adequate for another.**
  That is the point of [CLAIM-348](CLAIM-348.md) and its construction [CASE-110](../cases.d/CASE-110.md).
- **That observational adequacy is causal adequacy.** A state space with a
  distribution can satisfy the probabilistic version while interventions
  tell its merged states apart (A22's Construction B; [CLAIM-127](CLAIM-127.md)).
- **Anything about bounded judges.** A receiver that cannot compute j can do
  better with a different description ([CLAIM-199](CLAIM-199.md)).

## Note of 2026-10-21: two proposed TERMs that are this claim's condition

A12 of the exchange of 2026-10-20 proposed a TERM for "identifiability
relative to an observational regime" with the criterion
π(s₁) = π(s₂) ⟹ V(s₁) = V(s₂). A13 proposed another for
"target-preserving coarse-graining", J = j∘T iff T(x) = T(x′) ⇒
J(x) = J(x′). Both are this claim's condition, with the coarse-graining
read as an observation map in the first. No TERM is filed. This claim's
title is the definition, and its "Equivalently ... refines the partition
into J's level sets" gives the partition form.

The same exchange gave this claim's "What it does not say" (Construction
B, [CLAIM-127](CLAIM-127.md)) its first parameterized form: a closed coarse-graining that
loses an intervention response, filed as [CLAIM-tmppi0xf](CLAIM-tmppi0xf.md) with
[CASE-tmpdc0tl](../cases.d/CASE-tmpdc0tl.md). The note of 2026-10-21 on [CLAIM-397](CLAIM-397.md) uses this claim's
condition to widen a non-identifiability result to every functional of a
law.

The causal-abstraction papers were read the same day. This claim's causal
bullet defines intervention-consistent coarse-graining "for a declared
family of interventions"; Rubenstein et al.'s exact transformation is that
notion as a theorem-bearing definition, and its column condition for
averaging linear variables is [THEORY-755](../theory.d/THEORY-755.md)'s column-equitability
([THEORY-tmpj5zq1](../theory.d/THEORY-tmpj5zq1.md)). It is distributional, a match of push-forward laws, not
the fibre-wise factorization this claim proves, and the hidden governance
bit separates them ([THEORY-tmpjfhcb](../theory.d/THEORY-tmpjfhcb.md), [CLAIM-tmp4r4mi](CLAIM-tmp4r4mi.md)). Beckers and
Halpern's compatibility condition is this claim's shape one level up, on
contexts ([THEORY-tmpjtnjd](../theory.d/THEORY-tmpjtnjd.md)).
