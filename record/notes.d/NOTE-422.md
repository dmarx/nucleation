---
number: 422
status: Read
formerly:
- NOTE-tmporp14
paper: 'LIT-525'
title: 'Comments on a derivation and application of the ‘maximum entropy production’ principle'
version: 1
history:
- version: 1
  date: '2026-10-02'
  note: >-
    Read in full (the authors' manuscript as submitted on 15 April 2007, 5
    pp., Zenodo record 889780, CC BY-SA; text extracted with PyMuPDF; the
    displayed equations survived extraction). I re-derived the spin-chain
    results and Eq. 3, and checked §2 against Dewar 2003 (LIT-521,
    read the same day). Dewar 2005, the target of §1, could not be read, so
    §1's description of that letter's equations (13)–(19) is taken as
    given. The published Comment was not seen.
date: '2026-10-02'
summary: >-
  Two corrections to Dewar. First, Dewar 2005 derives MaxEP far from
  equilibrium from a fluctuation theorem plus a quadratic approximation to
  the flux distribution, used as if valid for all f. Both can hold together
  only for small F, where A(F) = ∂λ/∂F is constant: the linear regime. So
  the orthogonality condition ∂D/∂F = 4λ, which yields both maximum and
  minimum dissipation, fails for nonlinear constitutive relations, as an
  exactly solvable spin chain shows. Second, Dewar 2003's SOC divergence
  disappears once the quartic term is kept.
---
# NOTE-422: Comments on a derivation and application of the ‘maximum entropy production’ principle

## Contribution

The Comment locates the error in Dewar's 2005 claim to have derived MaxEP
for systems far from equilibrium, and shows that his 2003 claim that MaxEP
implies self-organized criticality (SOC) is unjustified. After it, the
information-theoretic route to a far-from-equilibrium extremum principle is
open again: "the question of the existence of possible extremal principles
… that might apply to far-from-equilibrium regimes … has not been settled"
(p. 3).

## Key insight

A fluctuation theorem compares the probability of a flux f with that of
−f. A Gaussian approximation around the mean F describes p(f) only near F.
Both can apply at once only when f and −f are both near F, which means F
near zero. That is the linear, near-equilibrium regime. Any derivation that
uses both at large F has quietly assumed linearity.

## Assumptions

- **Dewar's own setup** for §1: MaxEnt with constraints ⟨f_i⟩ = F_i and
  multipliers λ_i. Paths pair as (i+, i−) with f antisymmetric, and the
  fluctuation theorem is p(f)/p(−f) = exp(2Σλ_k f_k) (Dewar 2005, Eq. 13,
  which the authors "have verified").
- **The spin chain** (§1.1) is a one-chain simplification of Bruers's
  two-chain model. Paths are sequences of τ spins σ_t = ±c with c = 1/τ,
  and f = Σσ_t, read as net flux per macroscopic time. The large-τ limit is
  taken with Stirling's approximation.
- **§2** uses Dewar 2003's sandpile setup unchanged: p(F|F_ext) ∝
  exp H(F|F_ext), with H = rF² + gF⁴, r > 0 and g < 0.

## Key results

- **The faulty step** (§1). Dewar's Eq. 15, λ_k = Σ_j A_jk(F) F_j,
  requires his quadratic Eq. 14 to hold for all f. Differentiating it gives
  ∂A_jk/∂F_n = 0 (Eq. 2 here), so A is independent of F: linear
  constitutive relations, "contrary to Dewar's claim".
- **The correct gradient** (Eq. 3). With D = ⟨2Σλ_k f_k⟩,
  ∂D/∂F_n = 2λ_n + 2Σ_k A_nk(F) F_k. Dewar's orthogonality condition
  ∂D/∂F_n = 4λ_n holds only when Σ_k A_nk F_k = λ_n, in particular when A
  is constant. I re-derived Eq. 3 from D = 2Σλ_k F_k and A_nk = ∂λ_k/∂F_n.
- **Consequence.** The orthogonality condition is what Dewar uses to derive
  both "maximum dissipation" (hence MaxEP) and "minimum dissipation"
  (hence minimum entropy production). Both derivations therefore need
  linear constitutive relations (p. 3).
- **Spin chain, exact** (§1.1). Z(λ) = [2cosh(λ/τ)]^τ, F = tanh(λ/τ),
  λ(F) = τ artanh F, A(F) = τ/(1 − F²). The fluctuation theorem holds
  exactly. The large-deviation form of p(f) (Eq. 4) has quadratic expansion
  −τ(f − F)²/(2(1 − F²)), matching Dewar's Eq. 14 near F. But Dewar's Eq. 15
  would need τ artanh F = τF/(1 − F²), which holds only as F → 0. I checked
  each of these.
- **SOC** (§2). The divergence of ⟨F²⟩ as F_ext → 0 in Dewar 2003 comes
  from expanding H to quadratic order about ⟨F⟩ and using that form for all
  F. The quadratic coefficient vanishes like |g|F_ext². Keeping the quartic
  term and scaling y = F|g|^{1/4} gives ⟨F²⟩ ∝ 1/√|g|, finite at
  F_ext = 0. And since the model does not specify H at large F, "no
  conclusion about the large-F behaviour … can be drawn" (p. 5).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Dewar's 2005 derivation of MaxEP holds only for linear constitutive relations | strong as an argument about the stated equations; not checked here against Dewar 2005 itself | Eqs. 1–3; the authors verified Dewar's Eqs. up to 13 |
| C2 | The same failure applies to the derivation of minimum entropy production by the same route | strong, conditional on C1 | p. 3: both rest on the orthogonality condition |
| C3 | An exactly solvable spin chain shows the failure explicitly | strong | §1.1, Eq. 4; re-derived |
| C4 | Dewar 2003's SOC result is an artefact of a mean-field quadratic expansion | strong | §2; checked against Dewar 2003 Eqs. 26–28 |
| C5 | Whether a MaxEP model shows SOC is fixed by the assumed large-F tail of p(F), not derived | strong (logical) | §2, p. 5 |
| C6 | MaxEP or something like it may still underlie SOC | conjecture, flagged as such | "remains an intuitively appealing notion" (p. 5) |

## Concepts

- **Constitutive relation**: here, the map F ↦ λ(F) from mean fluxes to
  their conjugate Lagrange multipliers (forces). It is linear when
  A = ∂λ/∂F is constant.
- **Orthogonality condition**: Dewar's claim that λ(F) points along the
  steepest ascent of the mean dissipation D(F).

## Connections

It criticises Dewar 2003 ([LIT-521](../literature.d/LIT-521.md)) and Dewar 2005 (not filed;
unreadable). It credits Bruers's 2006 preprint for the model and for
noting that the orthogonality condition is valid only for linear systems.
It adds that Bruers does not identify the error, and repeats an incorrect
identity for D. Kleidon's review ([LIT-519](../literature.d/LIT-519.md)) cites this Comment and
Bruers (2007) as the criticisms of Dewar's foundation.

## Bearing on the record

- **MEP is contested, and this is why.** The record's MEP entries are Dewar
  2003, this Comment and Kleidon's review. Read together, they say the
  empirical MEP literature, mostly climate box models, rests on a
  foundation that has been derived only near equilibrium. The far-from-
  equilibrium regime is where MEP is applied and where it would differ from
  Onsager–Prigogine linear theory.
- **Prigogine.** The Comment does not discuss Prigogine directly. But its
  point that minimum entropy production, derived through the orthogonality
  condition, also needs linear constitutive relations is consistent with
  treating the minimum principle as a near-equilibrium result. Its scope is
  limited to the derivation it examines.
- **No ML instruction**, and nothing for the anthology.

## Limitations

- **Read from the submitted manuscript.** It is marked "Confidential: not
  for distribution", but is deposited under CC BY-SA. The published Comment
  may differ.
- **The 2005 letter was not checked.** The account of Dewar 2005's
  equations is the authors'.
- **One model.** The spin chain is a single, scalar (m = 1) example.
- **Not a disproof of MaxEP.** It removes one derivation and one
  application. It offers no counterexample to MEP as an empirical
  principle.

## Open questions

- Is there any derivation of an extremum principle for steady states that
  holds with nonlinear constitutive relations?
- What large-F behaviour of p(F|F_ext) would a MaxEP model actually
  predict, so that the SOC question could be decided rather than assumed?

## Corrections

- none to a seeded skim (there was no seed)
- **The title's quotation marks** are typographic single quotes in the
  published title (Crossref). The submitted manuscript uses double quotes.
  The LIT keeps Crossref's.
