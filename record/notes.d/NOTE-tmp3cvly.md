---
status: Read
paper: 'LIT-tmph7en9'
title: 'Semantic Unification'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read in full from the arXiv PDF (1403.3351v1, 12 pages, text layer
    extracted): abstract, §§1–6 and the reference list. Proposition 1 and
    its proof sketch checked; the failure example after it, the four
    anaphora examples of §4.3 and the probability table of §5.1
    recomputed by hand. The published chapter (LNCS 8222, pp. 1–13) was
    not compared with the preprint. Reference [7] (Dagan and Itai, the
    corpus method of §5) and DRT itself [14] were not read.
date: '2026-10-09'
summary: >-
  Puts basic DRT into sheaf form: a DRS is a section of a presheaf of
  consistent literals, an anaphoric resolution is a cover by variable maps,
  and the discourse's meaning is the gluing, unique if it exists
  (Proposition 1). All the interpretive work is in choosing the cover;
  the only obstruction to gluing shown is inconsistency, so the paper
  models context dependence and ambiguity, not contextuality in the
  Abramsky–Brandenburger sense. Its probabilistic section ranks covers by
  summed corpus counts, not by gluing distributions.
---

<!-- inactive-ok-file: THEORY-013 — Proposed; cited for the distinction it draws, not as settled -->

# NOTE-tmp3cvly: Semantic Unification

## Contribution

The paper gives Discourse Representation Theory's merge-and-unify step a
sheaf-theoretic form. Basic DRS become sections of a presheaf F on a
category of (vocabulary, variables) pairs; DRT's identification of
referents becomes a cover; and the semantics of a whole discourse is the
gluing of its sentences' sections along that cover. It then composes F
with a distribution functor to accommodate preferential anaphora, where
several resolutions are possible. It is a programme paper: one proposition,
worked examples, and three directions for future work (the logical
operations of full DRS, complexity of finding a gluing, learned
distributions).

## Key insight

Resolving anaphora is choosing how to identify the referents of separate
sentences, and once that identification (the cover) is fixed there is
nothing left to choose: the global meaning either exists, uniquely, or the
identification is semantically wrong. Interpretation lives in the cover,
and the gluing condition is a correctness check on it.

## Assumptions

- A first-order language with relation symbols only: no constants, no
  function symbols.
- **Basic DRS only**: conditions are finite sets of literals. Negated,
  conditional, disjunctive and quantified conditions are left to future
  work, so accessibility (the donkey sentence's real difficulty) is
  discussed in §3 but never modelled.
- Sections are deductive closures of *consistent* finite sets of literals;
  inconsistency is what takes a candidate out of F.
- No Grothendieck topology is defined. Covers are given concretely as
  jointly surjective families {fᵢ : (Lᵢ, Xᵢ) → (L, X)} with L = ∪ Lᵢ, and
  gluing is defined directly by restriction from the global section. There
  is no separate compatibility-on-overlaps condition, so "compatible family"
  has no independent meaning here.
- In every linguistic example the local vocabularies are disjoint, which by
  the paper's own remark makes consistency the only obstruction.

## Key results

- **Presheaf F** (§4.1). F(L, X) = deductive closures of consistent finite
  sets of literals over X in L; for f : (L, X) → (L′, Y), F(f)(s) ⊢ ±A(x)
  iff s ⊢ ±A(f(x)). Functoriality is asserted ("easily verified").
- **Proposition 1** (§4.2). For a cover {fᵢ} and family {sᵢ}, a gluing, if
  it exists, is unique: it can only be the deductive closure of
  {±A(fᵢ(x)) | ±A(x) ∈ sᵢ}, and it is a gluing if consistent and if it
  restricts to each sᵢ. *Holds when:* any cover; existence is not
  guaranteed.
- **Failure without inconsistency** (§4.2). With L₁ = L₂ = {R, S},
  s₁ = {R(x), S(u)}, s₂ = {S(y), R(v)}, x, y ↦ z and u, v ↦ w, the
  candidate restricts along f₁ to {R(x), S(x), R(u), S(u)} ≠ s₁. With
  shared vocabulary, a gluing fails if the merge adds anything about a
  local referent in its own vocabulary. I checked this; it is right.
- **Examples** (§4.3): "John sleeps. He snores." (one cover, glues);
  "John beats his donkey" (three local sections glued onto {a, b}); "John
  owns a donkey. It is grey." (merging "it" with John is inconsistent via
  Man/¬Man, merging it with the donkey glues); "John put the cup on the
  plate. He broke it." (two covers, both glue).
- **Distribution functor** (§5). D_R over a commutative semiring R: finite
  support functions summing to 1, with image measure as the action. Over
  the Booleans it is the finite powerset functor, over R⁺ finite
  probability distributions. Same pattern as [LIT-016](../literature.d/LIT-016.md)'s D_R ℰ, with F in
  place of the event sheaf ℰ.
- **Ranking covers** (§5.1). For "John gave the bananas to the monkeys.
  They were ripe. They were cheeky.", the four covers c₁–c₄ get
  probability proportional to the *sum* of the corpus counts of their two
  adjective–noun patterns (ripe banana 14, ripe monkey 0, cheeky banana 0,
  cheeky monkey 10): 14/48, 24/48, 0, 10/48. The printed d(t₄) = 0.205 is
  10/48 = 0.208. c₂ (bananas ripe, monkeys cheeky) is chosen.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Basic DRS form a presheaf on (vocabulary, variables) with restriction by pulling literals back along variable maps | moderate | §4.1; functoriality asserted, not shown |
| C2 | Relative to a fixed cover, semantic unification has at most one result | strong (proof) | Proposition 1 (immediate from the definitions) |
| C3 | DRT's merging of referents is the choice of cover, and the gluing condition expresses the semantic correctness of the merge | moderate | §4.3 examples; an interpretation, illustrated, not a theorem |
| C4 | Constraint-based anaphora resolution (agreement via negative literals) is the existence or non-existence of a gluing | moderate | Example 3 of §4.3 |
| C5 | Composing with a distribution functor handles preferential anaphora | weak | §5.1: the distribution is placed on the candidate global sections directly, not obtained by gluing local distributions; maximum entropy is mentioned and not used |
| C6 | The corpus-event probabilities "correspond to the coverings of the sheaf model" | weak | one worked example; the additive scoring gives 14/48 to "the bananas were cheeky" although "cheeky banana" has count 0 |
| C7 | The approach extends to full DRS and "to some extent obviates the need for" its extended conditions | not supported here | stated as belief in §3 and as future work in §6 |

## Concepts

- **section**: an element of F(L, X), a deductively closed consistent set
  of literals; a basic DRS.
- **cover**: a jointly surjective family of maps into (L, X), with the
  vocabularies' union L. Covers can identify variables, so a cover *is* a
  resolution of the anaphors.
- **gluing / semantic unification**: a section over (L, X) restricting to
  every local section along the cover.
- **contextual**: used throughout in the sense of context-dependent
  meaning (Harris and Firth's distributional context, and the discourse
  context of an anaphor), not in the sense of a compatible family with no
  global section.
- **multivalued gluing**: the case where several gluings, or several
  covers' gluings, are possible and must be ranked.

## Connections

The sheaf machinery and the D_R functor are from Abramsky and
Brandenburger ([LIT-016](../literature.d/LIT-016.md)) and Abramsky's work on relational databases; the
linguistic side is DRT (Kamp and Reyle) with DPL and Visser's monoid
semantics named as compositional successors. The donkey sentence comes
from Geach. The probabilities follow Dagan and Itai (COLING 1990). The
paper mentions DisCoCat ([LIT-273](../literature.d/LIT-273.md)) only in the introduction, as another way
language is "contextual"; there is no construction linking the two, and no
use of vector-space meanings.

## Bearing on the record

- **[LIT-016](../literature.d/LIT-016.md) / [NOTE-016](NOTE-016.md), [THEORY-012](../theory.d/THEORY-012.md).** The paper borrows the presheaf,
  gluing and distribution-functor shape of [LIT-016](../literature.d/LIT-016.md), but not its notion of
  contextuality. In [LIT-016](../literature.d/LIT-016.md) and [THEORY-012](../theory.d/THEORY-012.md), contextuality is a family that
  agrees on overlaps and still has no global section. Here no
  overlap-compatibility is defined, and the obstructions shown are
  inconsistency (Example 3) and over-determination of a local section (the
  R, S example). Neither is that phenomenon. The paper is the source of the
  "sheaves for language" idea; the record should not cite it as showing
  that language is contextual in [THEORY-012](../theory.d/THEORY-012.md)'s sense.
- **[LIT-277](../literature.d/LIT-277.md), [LIT-265](../literature.d/LIT-265.md).** Nothing here computes a cohomological obstruction
  or a contextual fraction, and neither could apply as things stand: both
  measure the failure of a compatible family to glue, and this paper's
  families have no overlap condition to be compatible under.
- **[THEORY-013](../theory.d/THEORY-013.md).** That document separates context-dependent marginals from
  contextuality in language data. This paper is an early instance of the
  conflation it warns about: its abstract says language is contextual and
  sheaves model contextuality, but what it models is context dependence and
  ambiguity. The paper has no data, so it neither supports nor
  contradicts [THEORY-013](../theory.d/THEORY-013.md)'s empirical claim.
- **[LIT-273](../literature.d/LIT-273.md) / [NOTE-245](NOTE-245.md), [LIT-272](../literature.d/LIT-272.md) / [NOTE-246](NOTE-246.md).** These are the same co-author's
  compositional distributional programme. The two approaches are presented
  side by side and not joined. [NOTE-245](NOTE-245.md) finds that DisCoCat's posetal
  framing cannot distinguish parse ambiguities. Here anaphoric ambiguity is
  represented by a set of covers, so the two programmes place ambiguity in
  different structures, and neither paper relates them.
- **[LIT-838](../literature.d/LIT-838.md) / [NOTE-608](NOTE-608.md), [THEORY-162](../theory.d/THEORY-162.md).** Heim's file change semantics is DRT's
  sister account of indefinites and donkey anaphora. This paper's cover
  does the work Heim gives to a pronoun finding a familiar card. It handles only the
  basic, unembedded case, so the accessibility facts that motivate both DRT
  and Heim lie outside it.
- **No THEORY filed.** The reading's one structural point is that
  ambiguity sits in the choice of cover and a fixed cover glues at most
  once. That is a fact about this construction, stated as Proposition 1,
  not a finding about language that the record lacks.
- No instruction for machine-learning practice; nothing for the anthology.

## Limitations

- Only basic DRS; no negation, implication, disjunction or quantifier
  conditions, so none of the accessibility constraints that DRT exists to
  handle. The authors say so ("rather short and preliminary").
- No Grothendieck topology, so F is not shown to be a sheaf, and the cover
  notion is ad hoc.
- How covers are generated (which identifications are candidates) is
  outside the model; the paper calls it the "intelligence" of the
  operation and leaves it to accessibility constraints and corpus counts.
- The probabilistic section does not glue local distributions. It places a
  distribution on candidate global sections by an additive score, without
  normalising per anaphor or assuming independence. A product of counts
  would give c₂ probability 1, and the additive score gives weight to
  readings with a zero-count pattern.
- One worked corpus example; no evaluation. Small errors: Example 2 is
  labelled "intersentential" although anaphor and antecedent are in one
  sentence, and 10/48 is printed as 0.205.

## Open questions

- Whether a genuinely contextual discourse exists in this framework: a
  family of local DRS sections that agree on every overlap of a fixed cover
  and have no gluing. That would need shared vocabulary and an overlap
  condition the paper does not define.
- Whether the cover-choice step can be internalised, for example as a
  presheaf over covers or a sheaf on a site whose objects include
  identifications, so that ranking resolutions becomes gluing rather than
  an external score.
- The extension to full DRS that §6 promises. Later work by Sadrzadeh and
  collaborators on contextuality in ambiguous phrases may take this up; it
  was not checked for this note.
