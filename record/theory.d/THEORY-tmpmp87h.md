---
status: Proposed
promote_when: >-
  A proof that δ(Â₁⊗1̂)_W ≠ δ(Â₁)_{V_W}⊗1̂ for some context W of the composite,
  with a proof that no operator B̂ has the pulled-back arrow as its
  representation, would promote it. A variant of the rules, or of the
  context category, under which tensor-product composites satisfy the
  translation condition would refute the claim that the scheme fails for
  them. The authors' "relatively easy to show" and "there appears to be no"
  cannot settle it, and neither can a further check on disjoint sums.
title: "In the Döring–Isham scheme for realising collections of systems in topoi, disjoint sums of quantum systems compose exactly, but along tensor products the best pull-back of a constituent's quantity agrees with the composite's own quantity only on contexts of the form V₁⊗ℂ1, since the composite's context poset holds contexts that mix the factors; the failure elsewhere is asserted, not proved"
version: 1
tags:
- quantum-foundations
- mathematics
- mereology
date: '2026-10-16'
source:
- LIT-310
- LIT-378
presupposes:
- THEORY-tmpirvdi
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
<!-- inactive-ok-file: LIT-310 — Proposed; read in full in NOTE-285 and cited as the source of the composite construction whose failure this account states as unproved -->

# THEORY-tmpmp87h: In the Döring–Isham scheme for realising collections of systems in topoi, disjoint sums of quantum systems compose exactly, but along tensor products the best pull-back of a constituent's quantity agrees with the composite's own quantity only on contexts of the form V₁⊗ℂ1, since the composite's context poset holds contexts that mix the factors; the failure elsewhere is asserted, not proved

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

- **That the failure is a theorem.** Neither (4.46) nor the non-existence
  of B̂ is proved, and fn. 25 leaves open an easier case, W = V₁⊗V₂ with V₂
  non-trivial. Hence Proposed.
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

- **Presupposes** [THEORY-tmpirvdi](THEORY-tmpirvdi.md): the arrows being translated are the
  quantity representations into ℝ^⪰ of paper III.
- [NOTE-285](../notes.d/NOTE-285.md) relates the result to [THEORY-017](THEORY-017.md): constituent quantities
  translate faithfully only on the sub-poset of contexts a given tensor
  factorisation picks out.
- Mereology in the record does not engage physical composition in these
  terms; the tag is for the subject, what counts as a system and its parts.
