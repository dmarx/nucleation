---
number: 585
status: Active
formerly:
- THEORY-tmpmp87h
title: "In the Döring–Isham scheme for realising collections of systems in topoi, disjoint sums of quantum systems compose exactly; along a tensor product of finite-dimensional systems, the pull-back of a constituent's quantity agrees with the composite's own quantity at a context exactly when every projection in it with proper support on the first factor has the form P⊗1, so it fails for every non-scalar quantity and no operator on the composite realises the pull-back"
version: 2
history:
- version: 2
  date: '2026-10-19'
  note: >-
    Corrected and promoted at the owner's direction, carrying out the
    promotion audit's decision for THEORY-585 (batch 044, ADR-047 v2).
    The failure the source asserts, (4.46) and the non-existence of an
    operator realising the pull-back, is proved for finite dimensions in
    the dated note below. The proof also shows the old title's "only on
    contexts of the form V₁⊗ℂ1" was too strong: agreement is decided by
    the context's projections, and holds, for instance, on a context of
    maximally entangled projections. The title now states the exact
    condition. The former promote_when's refutation route, a variant of
    the rules that repairs composites, moves to QUESTION-tmpucqdf.
tags:
- quantum-foundations
- mathematics
- mereology
date: '2026-10-16'
source:
- LIT-310
- LIT-378
presupposes:
- THEORY-553
summary: >-
  Döring & Isham, paper IV (2007/8), [LIT-310](../literature.d/LIT-310.md) ([NOTE-285](../notes.d/NOTE-285.md)), restated in
  [LIT-378](../literature.d/LIT-378.md) §§11–13 ([NOTE-326](../notes.d/NOTE-326.md)). Classical physics satisfies the translation
  condition (3.18) exactly. For quantum disjoint sums the pull-back of
  δ̆(A₁⊕A₂) is δ̆(A₁) (Lemma 4.2, 4.24; checked). For H₁⊗H₂ the pull-back
  gives δ(Â₁)_{V_W}⊗1̂ at each context W, which equals δ(Â₁⊗1̂)_W on
  contexts V₁⊗ℂ1̂. That it differs elsewhere, and that no operator
  realises it, are asserted. The rules are "partly experimental", and the
  trivial-system rule contradicts the series' own definition of contexts.
---

<!-- inactive-ok-file: THEORY-017 — Proposed; named in Connections as NOTE-285 relates it, not leaned on -->
<!-- inactive-ok-file: LIT-310 — Proposed; read in full in NOTE-285 and cited as the source of the composite construction whose failure this account proves -->

# THEORY-585: In the Döring–Isham scheme for realising collections of systems in topoi, disjoint sums of quantum systems compose exactly; along a tensor product of finite-dimensional systems, the pull-back of a constituent's quantity agrees with the composite's own quantity at a context exactly when every projection in it with proper support on the first factor has the form P⊗1, so it fails for every non-scalar quantity and no operator on the composite realises the pull-back

## Source

Döring & Isham (2007; *J. Math. Phys.* 49, 2008), "A topos foundation for
theories of physics: IV. Categories of systems", [LIT-310](../literature.d/LIT-310.md), read in full in
[NOTE-285](../notes.d/NOTE-285.md). The same construction, restated, is [LIT-378](../literature.d/LIT-378.md) §§11–13, read in full
in [NOTE-326](../notes.d/NOTE-326.md).

## What was actually shown

**The scheme.** Systems form a category Sys whose arrows translate one
system's physical quantities into another's, with composite ⋄ and disjoint
sum ⊔ as monoidal structures. Each arrow j is to be realised by a triple
(τ(j), φ(j), β(j)) that pulls a quantity arrow of S back to one of S₁
(Def 3.2, eq. 3.5). The target is the translation condition (3.18): the
pull-back of A's arrow is the arrow of A's translation. The rules are
"partly 'experimental'".

**Classical physics (§2.4).** Pull-back along the inclusion into a disjoint
union, or the projection from a product, satisfies the condition exactly
(2.33).

**Quantum disjoint sums (§4.2).** The functor V ↦ V ⊕ ℂ1̂_{H₂} induces the
pull-back. Lemma 4.2, δ(Â₁⊕Â₂)_{V₁⊕V₂} = δ(Â₁)_{V₁} ⊕ δ(Â₂)_{V₂}, gives
the pull-back of δ̆(⟨A₁, A₂⟩) as δ̆(A₁) (4.24). [NOTE-285](../notes.d/NOTE-285.md) checked it.

**Quantum composites (§4.3).** The functor W ↦ V_W, the largest V with
V⊗ℂ1̂ ⊆ W, induces the pull-back, into an augmented context category that
re-admits ℂ1̂. At each context W the pulled-back arrow is the Gel'fand
transform of δ(Â₁)_{V_W} ⊗ 1̂ (4.44–4.45). It agrees with δ̆(A₁⋄1) at
every W of the form V₁⊗ℂ1̂ (fn. 27). [NOTE-285](../notes.d/NOTE-285.md) checked the construction.

**The asserted failure.** "It is relatively easy to show" that
δ(Â₁⊗1̂)_W ≠ δ(Â₁)_{V_W}⊗1̂ in general (4.46), so (3.18) fails (4.47), and
"there appears to be no operator B̂" whose arrow equals the pull-back. The
authors attribute this to "operator entanglement": contexts of
V(H₁⊗H₂) not of the form V₁⊗V₂. Their summary is that quantum physics
"almost" satisfies the scheme (§5).

**What could have come out otherwise.** The pull-back could have agreed
with the composite's quantity on every context, as it does for disjoint
sums. On the contexts the factorisation picks out it does; elsewhere the
authors say it does not, without proof.

## What this does not say

- **That the source proves the failure.** Neither (4.46) nor the
  non-existence of B̂ is proved in the paper, and fn. 25 leaves open the
  case W = V₁⊗V₂ with V₂ non-trivial. Both are proved in the dated note
  below, for finite dimensions, and that case fails.
- **That the failure follows the factorisation.** It does not: a context
  whose projections all have full support on H₁, such as one spanned by
  maximally entangled projections, agrees for every quantity, while
  V₁⊗V₂ with both factors non-trivial does not.
- **That it concerns entanglement of states, Bell non-locality or
  contextuality.** The "entanglement" is in the context poset of H₁⊗H₂. The
  paper treats no states on composites and nothing like a partial trace.
- **That the rules are settled.** Several are conjectures (Rule 6), and the
  rule that the trivial system's topos is Sets contradicts the series'
  exclusion of ℂ1̂ from the contexts, under which the trivial system's topos
  is degenerate ([NOTE-285](../notes.d/NOTE-285.md)'s observation, repeated in [NOTE-326](../notes.d/NOTE-326.md)).
- **That there is a single topos for all systems.** The "gros topos" is
  posed in §5, not built.

## Connections

- **Presupposes** [THEORY-553](THEORY-553.md): the arrows being translated are the
  quantity representations into ℝ^⪰ of paper III.
- [NOTE-285](../notes.d/NOTE-285.md) relates the result to [THEORY-017](THEORY-017.md): constituent quantities
  translate faithfully only on the sub-poset of contexts a given tensor
  factorisation picks out.
- Mereology in the record does not engage physical composition in these
  terms; the tag is for the subject, what counts as a system and its parts.

## Note of 2026-10-19: the composite's failure, proved

The promotion audit (batch 044) proved what the source asserts, for
finite-dimensional H₁ and H₂ with dim H₂ ≥ 2. δ(Â)_V is outer
daseinisation, ∫λ d(δ^i(Ê_λ)_V), where δ^i(P)_V is the largest projection
of V below P. The pulled-back arrow at a context W is δ(Â₁)_{V_W}⊗1̂, with
V_W = W ∩ (B(H₁)⊗1̂), which may be ℂ1̂ in the augmented category. Two
arrows into ℝ^⪰ agree at W exactly when their operators agree at every
sub-context of W, since restriction of states is onto and the Gel'fand
transform is injective. Call the support of a projection R on H₁ the
range of its partial trace, and call W good if every projection of W with
proper support has the form e⊗1̂.

- **Agreement exactly on good contexts.** If W is good, so is every
  sub-context V′. For λ below the top of Â₁'s spectrum, a projection of V′
  under Ê_λ⊗1̂ has support under Ê_λ, so it is e⊗1̂ with e ∈ V_{V′}. Hence
  δ^i(Ê_λ⊗1̂)_{V′} = δ^i(Ê_λ)_{V_{V′}}⊗1̂ for every λ, and the operators
  agree. If W is not good, take an offending R with support P and
  V′ = {0, R, 1̂ − R, 1̂}. Then V_{V′} = ℂ1̂, so for Â₁ = 1̂ − P the pull-back
  is 1̂, while δ((1̂ − P)⊗1̂)_{V′} has eigenvalue 0 on R ≤ P⊗1̂.
- **Every non-scalar quantity fails.** With u an eigenvector for Â₁'s
  least eigenvalue and q any unit vector of H₂, R = |u⟩⟨u|⊗|q⟩⟨q| has proper
  support and is not e⊗1̂. At V′ as above the pull-back is λ_max·1̂, while
  δ(Â₁⊗1̂)_{V′} takes the value λ_min on R. This is (4.46).
- **No operator realises the pull-back.** If δ(B̂)_W = δ(Â₁)_{V_W}⊗1̂ for
  every W, then at a maximal W containing B̂, B̂ = δ(B̂)_W = b⊗1̂. At
  W = V⊗V₂ with V maximal containing b, V_W = V gives b = δ(Â₁)_V, so b
  dominates Â₁ in spectral order. At W = V⊗V₂ with V maximal containing
  Â₁, Â₁⊗1̂ = δ(b⊗1̂)_W dominates b⊗1̂. So b = Â₁, and B̂ = Â₁⊗1̂, which
  the previous point rules out.
- **Disjoint sums.** Projections of V₁⊕V₂ are e₁⊕e₂, so the largest one
  under E₁⊕E₂ is the pair of largest ones: Lemma 4.2, and the exact
  composition for disjoint sums.

V₁⊗V₂ with both factors non-trivial is not good, since p⊗q has proper
support; ℂ1̂⊗V₂ and a context of maximally entangled projections are.
Infinite dimensions are not treated.
