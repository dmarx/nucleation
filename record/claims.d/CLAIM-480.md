---
number: 480
status: Active
formerly:
- CLAIM-tmpose3y
title: 'Composing interactions can turn an interior into a constraint, and sometimes into a constraint of a new kind: in the chain E = ½k₁(x₁ − x₂)² + ½k₂(x₂ − x₃)², with x₂ internal and equilibrated, the boundary sees E_eff = ½·k₁k₂/(k₁ + k₂)·(x₁ − x₃)², a coupling between x₁ and x₃ that neither part has; if the interior relaxes slowly, eliminating it leaves a history-dependent constraint, a memory kernel, so interconnection fixes an effective constraint on the boundary''s trajectories and separation of time scales decides only whether that constraint is approximately memoryless; and for cellular sheaves the reduced constraint can relate three boundary values where every relation among the parts is pairwise'
version: 2
history:
- version: 2
  date: '2026-10-27'
  note: >-
    Revised at the owner's review of the pull request. Version 1 ended
    "if the interior relaxes slowly, eliminating it leaves a memory kernel
    instead, so whether a composite presents its boundary with an
    instantaneous constraint or a history-dependent one turns on the
    separation between its interior's time scale and the boundary's",
    and its body said that without separation the composite presents no
    constraint. A history-dependent relation is a constraint on admissible
    trajectories, so the claim now says what separation decides: whether
    the constraint is approximately memoryless, not whether there is one.
    The higher-order reduction of Hansen and Ghrist (THEORY-1090) is
    brought into the title and body. Status and warrant unchanged; the
    added part is demonstrated by the reading.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in either computation. The reading, that the interior has
  become a constraint for whatever interacts only with the boundary, is
  defeated by an interaction confined to x₁ and x₃ that tells apart two
  equilibrated composites with the same k₁k₂/(k₁ + k₂); black-boxing
  says there is none for the static energy, and the claim makes no
  promise about probes faster than the interior relaxes.
tags:
- complex-systems
- compositionality
- mathematics
date: '2026-10-27'
line:
- distributed-agency
- formal-apparatus
corroborates:
- CLAIM-477
complements:
- CLAIM-478
- CLAIM-471
grounds:
- LIT-1644
- LIT-1245
- THEORY-1090
- THEORY-1089
uses:
- TERM-090
- TERM-091
summary: >-
  From A22 §4 and A23 §IV of the exchange of 2026-10-27, which called
  composition "the most important missing mechanism" after the owner's
  U20. Eliminating an equilibrated interior leaves an effective boundary
  relation that no part has; an outside system interacting only with the
  boundary meets it as a constraint, and "The interior has effectively
  become apparatus." Baez and Fong's black-boxing functor is the general
  theorem for passive linear networks. The memory case ties it to
  Mori–Zwanzig and to [CLAIM-478](CLAIM-478.md): interconnection yields an effective
  constraint on the boundary's trajectories in every case, and separation
  of time scales decides only whether it is approximately memoryless. For
  cellular sheaves the reduction can need a richer relational vocabulary
  than the parts used (THEORY-1090; QUESTION-283). It is independent evidence
  for [CLAIM-477](CLAIM-477.md), that constraints are realized by organization.
---
<!-- inactive-ok-file: CLAIM-477 CLAIM-478 — Proposed; the claims this corroborates and sits beside, cited as open -->
<!-- inactive-ok-file: LIT-1660 — Unavailable; cited for what it is standardly cited for -->
<!-- inactive-ok-file: QUESTION-283 CLAIM-419 CLAIM-479 — Open, Proposed or new; the question this result raises and the claims about luria it bears on -->

# CLAIM-480: Composing interactions can turn an interior into a constraint, and sometimes into a constraint of a new kind: in the chain E = ½k₁(x₁ − x₂)² + ½k₂(x₂ − x₃)², with x₂ internal and equilibrated, the boundary sees E_eff = ½·k₁k₂/(k₁ + k₂)·(x₁ − x₃)², a coupling between x₁ and x₃ that neither part has; if the interior relaxes slowly, eliminating it leaves a history-dependent constraint, a memory kernel, so interconnection fixes an effective constraint on the boundary's trajectories and separation of time scales decides only whether that constraint is approximately memoryless; and for cellular sheaves the reduced constraint can relate three boundary values where every relation among the parts is pairwise

## The computation

Three nodes, x₁ and x₃ at the boundary and x₂ inside (A22 §4):

E(x₁, x₂, x₃) = ½k₁(x₁ − x₂)² + ½k₂(x₂ − x₃)².

Holding the boundary fixed, ∂E/∂x₂ = 0 gives x₂* = (k₁x₁ + k₂x₃)/(k₁ + k₂).
Then x₁ − x₂* = k₂(x₁ − x₃)/(k₁ + k₂) and x₂* − x₃ = k₁(x₁ − x₃)/(k₁ + k₂), so

E_eff(x₁, x₃) = ½ · k₁k₂/(k₁ + k₂) · (x₁ − x₃)².

The composite acts on its boundary as one spring of stiffness k₁k₂/(k₁ + k₂)
joining x₁ and x₃, which are not joined directly in the network. The
elimination is a Schur complement, or Kron reduction, the operation behind
effective resistance.

**With memory.** If the interior is not fast, it cannot be replaced by its
equilibrium. For a linear system ẋ = Ax + By, ẏ = Cx + Dy, solving for y and
substituting gives

ẋ(t) = Ax(t) + Be^{Dt}y(0) + ∫₀ᵗ Be^{D(t−s)}Cx(s) ds.

The boundary now depends on its own past through a kernel set by the
interior's dynamics D (A23 §IV). When D is fast and stable the kernel
concentrates near s = t, and the integral tends to −BD⁻¹Cx(t), which is the
static elimination. So the composite presents its boundary with one of
three things (A23 §IV):

- an approximately instantaneous constraint, when the interior relaxes fast;
- a history-dependent constraint, when its memory is significant;
- further active modes, when the interior cannot be eliminated at all.

All three are constraints on the boundary's admissible trajectories. A memory
kernel restricts which boundary histories can occur just as an instantaneous
coupling restricts which boundary states can. What separation of time scales
provides is the condition under which the instantaneous approximation is
adequate:

| what | gives |
|---|---|
| interconnection | an effective behavioural constraint at the boundary |
| sufficient separation of interior and boundary time scales | an approximately memoryless form of that constraint |

So the claim does not privilege memoryless structure over structure sustained
through history. Baez and Fong's black box shows the same thing exactly. With
inductors and capacitors it is a frequency-dependent relation at the terminals,
exact at every frequency, and needs no separation ([NOTE-1223](../notes.d/NOTE-1223.md)).

The record holds this family of reductions as Mori–Zwanzig ([LIT-1245](../literature.d/LIT-1245.md), read,
and its neighbours).

## The reading

A22: "To a system interacting only with the boundary, the entire three-node
organization behaves like a direct coupling between nodes 1 and 3. … **The
interior has effectively become apparatus.** … An internal organization of
interactions becomes a condition governing what external interactions are
possible." A23: "This is not simply a useful linguistic redescription. The
composite has an externally measurable boundary relationship derived from its
internal organization."

Baez and Fong ([LIT-1644](../literature.d/LIT-1644.md), read in [NOTE-1223](../notes.d/NOTE-1223.md)) give the general result for passive linear
networks. Black-boxing a circuit to the relation it imposes at its terminals is
a functor, so the external behavior of a composite is the composite of external
behaviors. Willems's behavioural form ([LIT-1660](../literature.d/LIT-1660.md)) states the same projection
for any interconnection. The external behaviour is the projection of the joint
behaviour onto the variables an observer can reach.

## When the reduced constraint is of a new kind

The chain above reduces to another pairwise coupling, and for scalar networks
that is always so: the Schur complement of a graph Laplacian is a graph
Laplacian on the boundary (Hansen and Ghrist, Thm 4.2). For cellular sheaves
it is not. Hansen and Ghrist's example ([THEORY-1090](../theory.d/THEORY-1090.md); Fig. 4.1, p. 20) is
a star with stalk ℝ² at the centre and ℝ at three leaves. The centre's maps
are the first coordinate, the second, and their sum. Every consistent
assignment is fixed by the centre's value (p, q), so the boundary values are
(p + q, q, p), and the reduced constraint is

v₁ = v₂ + v₃,

a relation among three boundary values. No sheaf on the boundary vertices,
whose conditions are all pairwise, has exactly that space of consistent
assignments; any that admits it admits more. "The problem is that the internal
node allows for constraints between boundary nodes that cannot be expressed by
purely pairwise interactions" (p. 20).

So composition followed by reduction can force a change in the type of
relational structure an adequate description needs, not only in its
parameters. The parts' relations were all pairwise. The composite's effective
relation is not, and a vocabulary of pairwise relations cannot state it. This
is the strongest result the claim holds. It has a direct counterpart in luria,
where a record's relation scheme meets what a composed organization requires
and cannot express it ([CLAIM-419](CLAIM-419.md), [CLAIM-479](CLAIM-479.md)).

Its limit: it concerns what a class of mathematical descriptions can express.
It does not show that a new fundamental interaction has arisen, or that the
three-way relation is anything but the effective trace of pairwise relations
through a hidden interior. Whether composition generally creates effective
structure that needs a richer relational vocabulary than its parts is
[QUESTION-283](../questions.d/QUESTION-283.md).

## Why it bears on the record

- **[CLAIM-477](CLAIM-477.md)** holds that the constraints are realized too, and that
  relata are realizations of them. This is a case with nothing interpretive
  in it. The constraint between x₁ and x₃ is realized by the interior and
  changes when the interior's springs do. It is not detached from the world,
  and it is not fixed.
- **[CLAIM-478](CLAIM-478.md)** says separation makes constraints. The memory case shows
  what separation does: it makes the composite's constraint approximately
  instantaneous. Without it the composite still constrains its boundary, by
  a relation over histories.
- **[CLAIM-471](CLAIM-471.md)** is about gluing local descriptions. This is the other
  half A22 found missing: "Sheaf theory tells us how locally defined
  information can be made compatible. But what happens when we **physically
  connect** two systems and then observe them as one system?"

## What it does not claim

That the composite is an individual. Effective boundary behaviour is one of the
properties A23 §VI listed. The others (persistence, autonomy, boundary
robustness, constraint maintenance and self-modification) need their own
evidence. Nor does the effective coupling add a new fundamental law. It is an
effective restriction, and is no more fundamental than the parts it is
realized by (A23 §XII).

## Note of 2026-10-27 (evening): the readings of the U15–U23 works

- **The computation is in the literature.** Baez and Fong's Example 2.9
  ([NOTE-1223](../notes.d/NOTE-1223.md), pp. 14–15) is two resistors in series. With k = 1/r, its
  interior potential and boundary power are this claim's x₂* and E_eff.
  General elimination is their Thm 3.3(vi) with Lemma 3.4: eliminating a
  node s adds c_is·c_js/Σ_k c_ks to each coupling ([THEORY-1089](../theory.d/THEORY-1089.md)). The
  paper's form is dissipated power, not spring energy. The algebra is the
  same.
- **The memory case needs a qualification.** With inductors and capacitors
  the black box is exact at every frequency, as an impedance over ℝ(s),
  under zero initial conditions. A composite therefore always presents its
  boundary with an exact relation, and no separation of time scales is
  needed for that. What separation decides is whether the relation is
  approximately instantaneous, which is how the title puts it. The term in
  y(0) is outside Baez and Fong's assumptions.
- **Black-boxing is a functor** ([THEORY-1063](../theory.d/THEORY-1063.md), Thm 1.1): circuits with the
  same behaviour are interchangeable in every composite. That supports the
  defeater's "there is none" for passive linear networks.
- **The constraint can be of higher order than any interaction that
  realizes it.** Hansen and Ghrist ([NOTE-1233](../notes.d/NOTE-1233.md), §4.2, Fig. 4.1, Thm 4.3;
  [THEORY-1090](../theory.d/THEORY-1090.md)) show that eliminating an interior vertex of a cellular
  sheaf can leave the boundary a constraint that no pairwise sheaf
  expresses, where for scalar networks the result stays pairwise (Thm 4.2).
  So composition can make a constraint not only new but of a new kind.
- **Spivak** ([NOTE-1225](../notes.d/NOTE-1225.md)) composes by summing pulled-back potentials and
  never eliminates an interior. Rigid constraints appear in his paper only
  as limits of stiff potentials (p. 9).
