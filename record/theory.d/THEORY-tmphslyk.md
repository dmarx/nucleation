---
status: Active
title: "Diffusion can destabilise a homogeneous steady state of reacting chemicals that is stable without it: a disturbance of one finite wave-length grows while uniform and very short ones decay, so a stationary pattern appears whose spacing is set by the reaction and diffusion constants and only its phase by the disturbance; with two substances this needs them to diffuse at different rates, and the pattern lasts only while free energy is supplied"
version: 1
tags:
- complex-systems
- natural-sciences
date: '2026-10-16'
source:
- LIT-535
- LIT-527
summary: >-
  Turing (1952), [LIT-535](../literature.d/LIT-535.md), read in full in [NOTE-427](../notes.d/NOTE-427.md), with Cross & Hohenberg
  (1993), [LIT-527](../literature.d/LIT-527.md), skimmed in [NOTE-418](../notes.d/NOTE-418.md). The linear analysis on a ring gives
  exact conditions (9.4a, b) for stationary waves of finite wave-length;
  that equal diffusibilities cannot satisfy them is [NOTE-427](../notes.d/NOTE-427.md)'s substitution,
  not stated in the paper. Turing calls the linearity assumption "a
  serious one" and the biological examples "very limited". Stationary
  chemical Turing patterns were first made in 1989–1991, and real
  morphogens implementing the mechanism had not been identified by 1993.
---
<!-- inactive-ok-file: NOTE-418 — Skimmed; cited only for the later chemical realisations and the status of morphogens, which the skim read -->
<!-- inactive-ok-file: THEORY-072 THEORY-088 — Proposed; neighbouring accounts named for context, nothing here rests on their being settled -->

# THEORY-tmphslyk: Diffusion can destabilise a homogeneous steady state of reacting chemicals that is stable without it: a disturbance of one finite wave-length grows while uniform and very short ones decay, so a stationary pattern appears whose spacing is set by the reaction and diffusion constants and only its phase by the disturbance; with two substances this needs them to diffuse at different rates, and the pattern lasts only while free energy is supplied

## Source

Turing (1952), [LIT-535](../literature.d/LIT-535.md), "The Chemical Basis of Morphogenesis", *Phil.
Trans. R. Soc. Lond. B* 237:37–72, read in full in [NOTE-427](../notes.d/NOTE-427.md). Cross &
Hohenberg (1993), [LIT-527](../literature.d/LIT-527.md), skimmed in [NOTE-418](../notes.d/NOTE-418.md), for the later chemical
realisations and the status of morphogens.

## What was actually shown

**The modes (§§6–7).** On a ring of cells, Fourier transforming separates
the linearised equations into pairs, and mode s grows as e^{p_s t} with
(p − a + μ′U)(p − d + ν′U) = bc in the continuum (9.1), a, b, c, d the
marginal reaction rates and U the squared wave-number. After a while the
mode with the largest Re p dominates.

**Six types of onset (§8).** Stationary or oscillatory, at extreme long,
finite or extreme short wave-length. Case (d), stationary waves of finite
wave-length, is "the case which is of greatest interest". Travelling
waves (e) and short-wave oscillation (f) need three or more substances.
Each case is shown with explicit parameters.

**Conditions for case (d) (p. 55).** bc < 0, with
4√(μ′ν′)/(μ′+ν′) < (d−a)/√(−bc) < (μ′+ν′)/√(μ′ν′) (9.4a) and, for
instability, (d/√(−bc))√(μ′/ν′) − (a/√(−bc))√(ν′/μ′) > 2 (9.4b). [NOTE-427](../notes.d/NOTE-427.md)
substitutes μ′ = ν′: (9.4a) then needs (d−a)/√(−bc) < 2 and (9.4b) needs
it > 2, so two substances with equal diffusibility cannot give the
pattern. The §10 example uses diffusion constants of 5×10⁻⁸ and 2.5×10⁻⁸
cm² s⁻¹.

**The spacing.** The pattern's wave-length is the "chemical wave-length",
set by the constants, not by tissue size. Only phase or orientation comes
from the disturbance, "like an upright stick falling over" (p. 66).

**A worked case (§10).** Twenty cells, computed on the Manchester
computer: the linear theory predicts three lobes, with four the closest
competitor, and slow onset gives three reliably. The final states are
"only dynamic equilibria … in order to maintain the wave pattern a
continual supply of free energy is required" (pp. 65–66).

**Later realisation ([LIT-527](../literature.d/LIT-527.md), §X.B.5).** Stationary chemical Turing
structures were found only in 1989–1991, in gels and in the
chlorite–iodide–malonic-acid reaction without macroscopic gradients.

**What could have come out otherwise.** Diffusion, a smoothing process,
could only have stabilised a homogeneous state. It does not always.

## What this does not say

- **That development works this way.** No real reaction is identified; the
  §10 chemistry is chosen to give the required rates. Turing concedes the
  biological examples are "very limited" (p. 72). Cross and Hohenberg
  report that "the chemical identification of the morphogens has proved
  elusive" (p. 1050).
- **What happens far from onset.** Everything outside §10 is linear about
  homogeneity, an assumption Turing calls "a serious one". In two
  dimensions he asserts, without derivation, that the non-linear
  instability is almost always "catastrophic".
- **That activator–inhibitor structure is necessary in general.** It is
  necessary within the linear two-species model; Cross and Hohenberg call
  it "by no means a general necessary condition" for this type of
  instability (§XI.A).
- **That the pattern is an equilibrium.** Turing's "equilibrium" means a
  steady state. The patterns are fed, which places them among dissipative
  structures before the term existed.

## Connections

- **Dissipative structures ([THEORY-tmpyw70u](THEORY-tmpyw70u.md)).** Prigogine names this
  instability of the Brusselator the "Turing bifurcation" and credits this
  paper with first seeing it. Turing's criterion is purely kinetic, which
  fits the lecture's conclusion that far from equilibrium the kinetics
  decides.
- **Spiral defects in cortex ([THEORY-088](THEORY-088.md))** treats slow cortical activity
  as a pattern-forming medium, of the kind this paper founded.
- **Non-reciprocal metabolic cycles ([THEORY-tmpsuuh4](THEORY-tmpsuuh4.md))** uses the same
  linearise-and-read-the-growing-mode method, with conserved catalysts in
  place of reactants.
- **Organisms against flames ([THEORY-072](THEORY-072.md)).** The mechanism is the same in
  an embryo and an unstirred reactor, so it cannot be what marks organisms
  off; [NOTE-427](../notes.d/NOTE-427.md) reads it as a pattern-forming step inside organisms.
