---
status: Active
title: 'A translation between two logics presented as institutions is correct, in the Satisfaction Condition''s sense, when a translated sentence holds in a model exactly when the original holds in the model''s translation; given the model translation this fixes the sentence translation up to semantic equivalence, and when every model of the target is reached it preserves and reflects entailment, so one logic''s prover can decide the other''s; but the condition alone admits collapsing translations and is relative to a model translation it does not supply'
version: 1
tags:
- logic
- mathematics
- translation
date: '2026-10-29'
source:
- LIT-1661
summary: >-
  Goguen and Burstall (1992), [LIT-1661](../literature.d/LIT-1661.md), read in [NOTE-tmpyi64y](../notes.d/NOTE-tmpyi64y.md) from the
  published JACM article: Definition 32 (p. 125), Proposition 33 and
  Proposition 35 (p. 126), Theorem 39 (pp. 127–129). Active: proved, and
  checked on toy morphisms between propositional institutions. The
  collapsing morphism and the atom-negating morphism are my constructions,
  not the paper's. It is a criterion relative to a chosen model
  translation, and says nothing about translation beyond truth
  conditions.
---
<!-- inactive-ok-file: CLAIM-469 — Open or Proposed; the entries this result bears on, cited as open -->

# THEORY-tmpkmtoo: A translation between two logics presented as institutions is correct, in the Satisfaction Condition's sense, when a translated sentence holds in a model exactly when the original holds in the model's translation; given the model translation this fixes the sentence translation up to semantic equivalence, and when every model of the target is reached it preserves and reflects entailment, so one logic's prover can decide the other's; but the condition alone admits collapsing translations and is relative to a model translation it does not supply

## Source

Goguen and Burstall (1992), [LIT-1661](../literature.d/LIT-1661.md), §4.1, pp. 124–129 of the Journal of
the ACM 39(1); read in [NOTE-tmpyi64y](../notes.d/NOTE-tmpyi64y.md).

## What was actually shown

**The definition.** An institution morphism Φ: 𝒥 → 𝒥′ is a functor
Φ: **Sign** → **Sign**′, a natural α: Φ; Sen′ ⇒ Sen and a natural
β: Mod ⇒ Φ^op Mod′, "such that the following Satisfaction Condition holds
m ⊨_Σ α_Σ(e′) iff β_Σ(m) ⊨′_Φ(Σ) e′" for every Σ-model m and every
Φ(Σ)-sentence e′ (Definition 32, p. 125). Sentences go from 𝒥′ to 𝒥,
models from 𝒥 to 𝒥′. The worked example forgets predicates to go from
first-order logic with equality to equational logic (pp. 124–125).

**The sentence translation is fixed by the model translation.**
Proposition 33 (p. 126): (β_Σ M)* = α_Σ⁻¹(M*) and
(α_Σ E′)* = β_Σ⁻¹(E′*). With E′ = {e′}, the models of α_Σ(e′) are
exactly the models β sends into the models of e′. So once β is given,
α_Σ(e′) is determined up to semantic equivalence; only whether some
sentence has that model class is left open.

**Soundness gives entailment.** Φ is sound iff each β_Σ is surjective on
objects (Definition 34). Then for Φ(Σ) = Σ′, e′ ∈ E′• iff
α_Σ(e′) ∈ α_Σ(E′)• (Proposition 35, p. 126): entailment is preserved and
reflected, and "a theorem prover for first-order logic with equality can
be used for equational theories" (p. 126).

**Structure is carried over.** If Φ has a [finitely] cocontinuous left
inverse Ψ on signatures (cordial, Definition 38), the induced functor on
theories is [finitely] cocontinuous, so a target theory built as a
colimit of small theories translates to a colimit of their translations
(Theorem 39, pp. 127–129).

**Checks, on propositional logic with Φ the identity on signatures.**
(1) α renaming nothing and β the identity: the condition holds. (2) α
sending each atom p to ¬p and β the identity: it fails. (3) The same α
with β complementing valuations: it holds, β is surjective, and in the
tests run no entailment was gained or lost. (4) β sending every model to
one valuation v₀, and α sending e′ to "true" or "false" according as
v₀ ⊨ e′: the condition holds, β is not surjective, and entailment
differed from the source in 232 of 840 tests. (2)–(4) are my
constructions.

**What could have failed.** Proposition 35 could have needed more than
surjectivity, for example injectivity of α or a completeness property;
the proof (p. 126) uses only surjectivity of β and the Satisfaction
Condition, in both directions.

## What this does not say

- **That correctness is structural resemblance.** Checks (1)–(3) show
  that a shape-preserving translation can fail the condition and a
  shape-changing one can satisfy it. Correctness is fixed by the models.
- **That the Satisfaction Condition alone ensures fidelity.** Check (4)
  satisfies it and loses entailment. Fidelity in Proposition 35's sense
  needs soundness. Equality of two composite morphisms along different
  routes is a further, separate property, which the collapsing morphism
  can have.
- **Where β comes from.** The criterion is relative to a model
  translation that is given. For natural languages no category of models
  or functor between them is given; the paper names natural-language
  semantics as an application (p. 95) and develops nothing.
- **Anything beyond truth conditions.** Satisfaction is two-valued and
  the condition is exact for every model and sentence. Force, register,
  implicature and degrees of loss count only if written into the
  sentences and models.
- **That every change of vocabulary or logic is a morphism.** A
  migration that splits one type into two is not a signature morphism
  from the old signature to the new; the paper's morphisms also run
  against the direction of sentence translation, a choice the authors
  call arbitrary and perhaps wrong (p. 110).
