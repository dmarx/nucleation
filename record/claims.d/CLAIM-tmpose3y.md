---
status: Active
title: 'Composing interactions can turn an interior into a constraint: in the chain E = ½k₁(x₁ − x₂)² + ½k₂(x₂ − x₃)², with x₂ internal and equilibrated, the boundary sees E_eff = ½·k₁k₂/(k₁ + k₂)·(x₁ − x₃)², a coupling between x₁ and x₃ that neither part has; if the interior relaxes slowly, eliminating it leaves a memory kernel instead, so whether a composite presents its boundary with an instantaneous constraint or a history-dependent one turns on the separation between its interior''s time scale and the boundary''s'
version: 1
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
- CLAIM-tmpmand1
complements:
- CLAIM-tmpmx2ql
- CLAIM-tmpdjt64
grounds:
- LIT-tmpdkjum
- LIT-1245
summary: >-
  From A22 §4 and A23 §IV of the exchange of 2026-10-27, which called
  composition "the most important missing mechanism" after the owner's
  U20. Eliminating an equilibrated interior leaves an effective boundary
  relation that no part has; an outside system interacting only with the
  boundary meets it as a constraint, and "The interior has effectively
  become apparatus." Baez and Fong's black-boxing functor is the general
  theorem for passive linear networks. The memory case ties it to
  Mori–Zwanzig and to [CLAIM-tmpmx2ql](CLAIM-tmpmx2ql.md): the constraint is instantaneous
  only across a separation of time scales. It is independent evidence
  for [CLAIM-tmpmand1](CLAIM-tmpmand1.md), that constraints are realized by organization.
---
<!-- inactive-ok-file: CLAIM-tmpmand1 CLAIM-tmpmx2ql CLAIM-tmpdjt64 — Proposed; the claims this corroborates and sits beside, cited as open -->
<!-- inactive-ok-file: LIT-tmpdkjum LIT-tmpnyd4r — Deferred; registered from the exchange, unread, cited for what they are standardly cited for -->

# CLAIM-tmpose3y: Composing interactions can turn an interior into a constraint: in the chain E = ½k₁(x₁ − x₂)² + ½k₂(x₂ − x₃)², with x₂ internal and equilibrated, the boundary sees E_eff = ½·k₁k₂/(k₁ + k₂)·(x₁ − x₃)², a coupling between x₁ and x₃ that neither part has; if the interior relaxes slowly, eliminating it leaves a memory kernel instead, so whether a composite presents its boundary with an instantaneous constraint or a history-dependent one turns on the separation between its interior's time scale and the boundary's

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

Baez and Fong ([LIT-tmpdkjum](../literature.d/LIT-tmpdkjum.md), unread) give the general result for passive linear
networks. Black-boxing a circuit to the relation it imposes at its terminals is
a functor, so the external behavior of a composite is the composite of external
behaviors. Willems's behavioural form ([LIT-tmpnyd4r](../literature.d/LIT-tmpnyd4r.md)) states the same projection
for any interconnection. The external behaviour is the projection of the joint
behaviour onto the variables an observer can reach.

## Why it bears on the record

- **[CLAIM-tmpmand1](CLAIM-tmpmand1.md)** holds that the constraints are realized too, and that
  relata are realizations of them. This is a case with nothing interpretive
  in it. The constraint between x₁ and x₃ is realized by the interior and
  changes when the interior's springs do. It is not detached from the world,
  and it is not fixed.
- **[CLAIM-tmpmx2ql](CLAIM-tmpmx2ql.md)** says separation makes constraints. The memory case shows
  the converse failure: without separation the composite does not present a
  constraint, only a history-dependent relation.
- **[CLAIM-tmpdjt64](CLAIM-tmpdjt64.md)** is about gluing local descriptions. This is the other
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
  ([NOTE-tmpigjto](../notes.d/NOTE-tmpigjto.md), pp. 14–15) is two resistors in series. With k = 1/r, its
  interior potential and boundary power are this claim's x₂* and E_eff.
  General elimination is their Thm 3.3(vi) with Lemma 3.4: eliminating a
  node s adds c_is·c_js/Σ_k c_ks to each coupling ([THEORY-tmpugh7c](../theory.d/THEORY-tmpugh7c.md)). The
  paper's form is dissipated power, not spring energy. The algebra is the
  same.
- **The memory case needs a qualification.** With inductors and capacitors
  the black box is exact at every frequency, as an impedance over ℝ(s),
  under zero initial conditions. A composite therefore always presents its
  boundary with an exact relation, and no separation of time scales is
  needed for that. What separation decides is whether the relation is
  approximately instantaneous, which is how the title puts it. The term in
  y(0) is outside Baez and Fong's assumptions.
- **Black-boxing is a functor** ([THEORY-tmp99qi9](../theory.d/THEORY-tmp99qi9.md), Thm 1.1): circuits with the
  same behaviour are interchangeable in every composite. That supports the
  defeater's "there is none" for passive linear networks.
- **The constraint can be of higher order than any interaction that
  realizes it.** Hansen and Ghrist ([NOTE-tmpzqos6](../notes.d/NOTE-tmpzqos6.md), §4.2, Fig. 4.1, Thm 4.3;
  [THEORY-tmpvecoh](../theory.d/THEORY-tmpvecoh.md)) show that eliminating an interior vertex of a cellular
  sheaf can leave the boundary a constraint that no pairwise sheaf
  expresses, where for scalar networks the result stays pairwise (Thm 4.2).
  So composition can make a constraint not only new but of a new kind.
- **Spivak** ([NOTE-tmplvblh](../notes.d/NOTE-tmplvblh.md)) composes by summing pulled-back potentials and
  never eliminates an interior. Rigid constraints appear in his paper only
  as limits of stiff potentials (p. 9).
