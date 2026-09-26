---
number: 168
status: Read
formerly:
- NOTE-tmpt4fcr
paper: LIT-165
title: 'Hartmann & Trpin — Coherence-based explanatory power'
version: 2
history:
- version: 2
  date: '2026-09-26'
  note: >-
    Read in full (full text of the open-access (CC BY) publisher PDF,
    Philosophical Studies 183:1817–1843 (27 pp.), via rd.springer.com — all
    of §§1–7, both figures, Table 1, footnotes, the Appendix proofs of
    Propositions 1–2, and the references. I also recomputed the paper's
    three numerical claims (the chain and collider examples of §5.1 and the
    OLI counterexample in the Appendix); all three reproduce.). Upgraded
    from `Skimmed` to `Read`: the claims table, assumptions and results are
    new, and the skim is corrected where the full text disagreed.
date: '2026-09-26'
summary: >-
  If explanatory power is measured contrastively over sets of explanantia,
  as E_CohOG+(E; H) = (Coh(H∪{E}) − Coh(H∪{¬E})) / (Coh(H∪{E}) +
  Coh(H∪{¬E})) with Olsson–Glass overlap normalised by its independence
  value (CohOG+), then the measure provably satisfies Roche & Sober's Two
  Likelihood Inequalities for single hypotheses (Prop. 2) and violates the
  One Likelihood Inequality (OLI). Two numerical examples show that adding
  a distal cause (for P(H1) < .7) or a negatively interacting cause (for
  P(H1) = P(H2) < .75) can raise explanatory power. Both are existence
  demonstrations, not general theorems.
---

# NOTE-168: Hartmann & Trpin — Coherence-based explanatory power

## Contribution

The paper defines a family of explanatory-power measures (Definition 1) that take a *set* of explanantia and contrast its coherence with E against its coherence with ¬E. It proves that the Shogenji-based member is the Schupbach–Sprenger measure generalised to n hypotheses (Prop. 1), and that the CohOG+-based member satisfies TLI but not OLI for single hypotheses (Prop. 2 and its Appendix remark). It shows by two numerical examples that this member can rank a richer explanans set above a sparser one in exactly the chain and negative-interaction cases where Roche & Sober (2023) proved every two-place TLI measure cannot. Against Lange (2022) it offers a representational reply that applies to probabilistic measures generally: separate core hypotheses from auxiliaries, and the entailment P(E|H)=1 usually disappears.

## Key insight

Roche & Sober's impossibility results are, the authors argue, "representation-relative" (p. 1834). They follow from TLI *together with* the practice of collapsing several explanantia into one conjunctive hypothesis, not from TLI alone. A measure whose argument is a structured set can let the mutual fit of explanantia count, and can then prefer {distal, proximal} over {proximal}, or {H1, H2} over {H1} when the causes interact negatively. It can do this while still behaving like a likelihood measure for single hypotheses.

## Assumptions

- A prior probability P over binary propositional variables H1..Hn, E. Explanans and explanandum sets are disjoint (H ∩ E = ∅). The explanandum is a single binary variable, so its complement is {¬E}; multi-variable explananda are left for future work (fn. 8).
- Explanantia are "distinct" (fn. 11). They are represented as a set rather than a conjunction when each "retain[s] explanatory relevance" (p. 1828); conjunction is appropriate when it individuates a single explanatory variable (the bachelor example).
- In the Bayesian-network examples, probabilistic dependencies are taken to correspond to causal ones (fn. 5).
- The measures rank *candidate* explanations of a fixed explanandum. They do not decide what counts as an explanation (§6).
- The Lange reply assumes that a principled core/auxiliary split exists. The authors concede it is "itself contestable" (p. 1837).

## Key results

- **Definition 1** (p. 1829): E_Coh(E; H) := [Coh(S_E) − Coh(S_¬E)] / [Coh(S_E) + Coh(S_¬E)], with S_E = H ∪ E and S_¬E = H ∪ E^C.
- **Eq. 1** CohSh(S) = P(H1..Hn, E) / (P(H1)···P(Hn)P(E)). **Eq. 2** CohOG(S) = P(H1..Hn, E) / P(H1 ∨ … ∨ Hn ∨ E). **Eq. 3** CohOG+(S) = CohOG under P divided by CohOG under P̃, the independence distribution with the same marginals, = CohSh(S) · [1 − P(¬H1)···P(¬Hn)P(¬E)] / [1 − P(¬H1, …, ¬Hn, ¬E)].
- **Proposition 1**: with CohSh, E_Coh(E; H) = E_ScSp(E; H1..Hn) = [P(H1..Hn|E) − P(H1..Hn|¬E)] / [sum]. This generalises Prop. 3 of Hartmann (2023). *Proof:* algebra in the Appendix. The printed penultimate line has "−" where the denominator should read "+", a typo.
- **Proposition 2**: if P(E|H1) > P(E|H2) and P(E|¬H1) < P(E|¬H2), then E_CohOG+({E};{H1}) > E_CohOG+({E};{H2}). *Proof:* with e = P(E) fixed and h eliminated as (e−q)/(p−q), the measure increases in p = P(E|H) and decreases in q = P(E|¬H), by sign analysis of the partial derivatives. It does **not** satisfy OLI (counterexample above).
- **Chain H1→H2→E** with P(H2|H1)=.9, P(H2|¬H1)=.1, P(E|H2)=.5, P(E|¬H2)=.1: E_CohOG+({E};{H1,H2}) > E_CohOG+({E};{H2}) for P(H1) < .7 (Fig. 1). The inequality reverses at high P(H1), e.g. 90%. The distal cause alone never beats the proximal one (fn. 13). Verified numerically: at P(H1)=.05 the values are .768 vs .748; at .9 they are .179 vs .207; H1 alone gives .671.
- **Collider H1→E←H2** with P(H1)=P(H2), P(E|H1,H2)=.7, P(E|H1,¬H2)=P(E|¬H1,H2)=.71, P(E|¬H1,¬H2)=.01: E_CohOG+({E};{H1,H2}) > E_CohOG+({E};{H1}) for P(H1) < .75 (Fig. 2). Verified: at .4 the values are .611 vs .585.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | The Shogenji-based coherence measure of explanatory power equals Schupbach–Sprenger, generalised to n explanantia | strong | Prop. 1, proof in Appendix |
| C2 | E_CohOG+ satisfies TLI for single-hypothesis explanans sets | strong | Prop. 2, derivative proof in Appendix (fixing P(E), which is legitimate since both hypotheses share one distribution) |
| C3 | E_CohOG+ violates OLI | strong | explicit counterexample in the Appendix, reproduced |
| C4 | E_CohOG+ can rank {distal, proximal} above {proximal} in a causal chain | moderate | one parameterised numerical example (Fig. 1), reproduced; an existence result only |
| C5 | E_CohOG+ can rank two negatively interacting causes above one | moderate | one numerical example (Fig. 2), reproduced; conditions for this "not clear" (p. 1836) |
| C6 | Roche & Sober's pathologies come from collapsing explanantia into conjunctions, not from TLI | weak–moderate | informal argument, plus C4–C5 as possibility proofs; not a theorem characterising which set-based measures escape |
| C7 | Lange's entailment problem arises only if auxiliaries are counted in the explanans | weak | informal argument and one stipulated reconstruction (Poisson vs Newton, where P(E|H_N) > P(E|H_P) is assumed, not derived); authors concede it is not fully resolved |
| C8 | E_CohOG+ "provides the expected results in test cases" and is "conceptually justified" (p. 1836) | weak | two worked cases; the justification of CohOG+ is outsourced to Hartmann & Trpin (forthcoming, J. Phil.) |
| C9 | Other coherence measures (Douven–Meijs ratio, Fitelson+1) also satisfy TLI and avoid both problems | weak | "preliminary computational evidence", not shown |
| C10 | Coherentism is a more adequate elaboration of probabilism, not a rejection of it (§7) | assertion | concluding framing |

The headline in the abstract and §7, that the measure "accommodates key scientific judgments" and overcomes the challenges, claims more than the body shows. The body gives one theorem about single hypotheses and two examples about sets.

## Method

Define the set-valued contrastive measure (Def. 1) and choose a base coherence measure. Check the base measure against adequacy conditions: TLI and OLI analytically for singleton explanans sets. Then evaluate it on parameterised Bayesian networks (chain, collider) by plotting the measure against prior probability and reading off the parameter region where the richer set wins.

## Concepts

- **Explanatory power** — how well a candidate explanans fits a fixed explanandum, contrastively against ¬E. It is not whether the candidate is an explanation (§6).
- **Reverse confirmation** — the likelihood-based family (Table 1: Eells–Jeffrey, Popper, McGrew, Good, Christensen, Schupbach–Sprenger, Crupi–Tentori), classed as affirmative, comprehensive or hybrid after Cohen (2016).
- **TLI / OLI** — the Two / One Likelihood Inequalities of Roche & Sober (2023), stated on p. 1824.
- **Temporal shallowness; negative causal interaction** — the two Roche–Sober problems addressed (p. 1825).
- **Explanans set vs conjunctive explanans** — the paper's representational principle: conjoin when the conjunction defines the explanans, keep a set when conjoining "flattens explanans structure" (p. 1828).
- **CohOG+** — relative overlap normalised by the relative overlap under an independence counterpart with equal marginals (Eq. 3).
- **Structurally proper coherence measures** — the uncharacterised subset of coherence measures that register both mutual support among explanantia and contrast with the explanandum (p. 1836).

## Connections

The paper replies to Roche & Sober (2023, Phil. Sci. 90:129–149) and Lange (2022, Phil. Sci. 89:252–267). It extends Hartmann & Trpin (2023, "Conjunctive explanations: a coherentist appraisal") and depends on Hartmann & Trpin (forthcoming, "Why coherence matters", J. Phil.) for CohOG+. It generalises Hartmann (2023)'s Prop. 3. It sits in the Bayesian coherentism of Bovens & Hartmann (2003), Shogenji (1999) and Olsson (2002), and cites BonJour and Thagard for the tie between explanation and coherence. None of these works is held in the record. The record holds nothing else on explanatory power or coherence measures; [LIT-156](../literature.d/LIT-156.md) (reciprocal causation) is the nearest philosophy-of-science neighbour and is not engaged.

**Epistemology tag.** The work relies on formal, Bayesian epistemology. Explanatory power is modelled on the agent's prior credences, and the measure is meant to serve inference to the best explanation (p. 1838). Coherence is the notion from coherentist theories of justification (BonJour 1985), treated probabilistically. The position is that coherence is a legitimate epistemic dimension that refines probabilism rather than replacing it. The paper does not take a stance on justification or knowledge as such. The tag is justified, as a secondary tag: the paper's subject is scientific explanation, and its apparatus is credal and evidential.

## Bearing on the record

This is formal philosophy of science. It carries no instruction for ML practice. The seeded LIT's suggestion that a set-valued explanatory-power measure is relevant to the anthology's weighing of competing explanations is speculative. The measure needs a joint prior over the explanantia, which such comparisons do not have, so nothing here should go to the Anthology of the SOTA. It could matter to a THEORY-style comparison only as a formal metaphor. No THEORY document is supported or contradicted. The current primary topic, `philosophy-of-science`, is right.

## Limitations

- Only single-hypothesis TLI is proven. The set-level advantages are shown by two hand-picked parameterisations, with no characterisation of when the richer set wins, and the authors say so (p. 1836).
- The escape from Roche & Sober changes the argument type from a conjunction to a set. A critic can reply that this changes the question: the two-place theorems still hold for conjunctions, which the authors grant (p. 1834). Whether to use a set or a conjunction is a modelling choice the paper leaves to judgment.
- The result depends on the choice of CohOG+, whose defence is in a separate paper. There is no axiomatisation or representation theorem (§7).
- Two of Roche & Sober's four problems are excluded by fiat (fn. 4). Only a binary explanandum is treated.
- The Lange reply is generic and partial. Its example stipulates P(E|H_N) > P(E|H_P).
- Production defects: fn. 4 is garbled, and the proof of Prop. 1 has a sign typo.

## Open questions

- Characterise the "structurally proper" coherence measures: which base measures make Definition 1 satisfy TLI and avoid both Roche–Sober problems? A representation theorem would settle this.
- Give general conditions, not examples, under which adding a distal or negatively interacting cause raises E_CohOG+.
- Is the non-monotonicity in P(H1) intuitive? The richer explanation loses once the distal cause is common (P(H1) > .7).
- How should multi-variable explananda and non-atomic explanantia be handled (fn. 8, p. 1832)?
- Can a principled core/auxiliary criterion be given, so that the Lange reply does more than relocate the problem?

## Corrections to the seeded skim

- The skim says fn. 7 restates "the Good, Schupbach–Sprenger and Crupi–Tentori measures" with Shogenji coherence. Fn. 7 (p. 1827) restates McGrew's E_MG = P(E|H)/P(E) (following Brössel 2015), Schupbach–Sprenger and Crupi–Tentori. Good's measure is the log of E_MG (Table 1), but the paper does not name it there. Fn. 7 sits in §4, not §3. Proposition 1 is in §5, not §3.
- The skim says the measure "satisfies TLI without the shallowness and negative-interaction failures". The full text is narrower. Prop. 2 proves TLI only for single-element explanans sets ({H1} vs {H2}). The paper itself says E_CohOG+ is "a TLI measure in the technical sense, but not in the structurally constrained sense that underwrites Roche and Sober's theorems" (p. 1832). The failures are avoided because the sets {H1,H2} and the conjunction H1∧H2 are scored differently. That shows possibility in two parameterised examples, not a general theorem, and the authors add that "It is not clear under which conditions" including interacting causes wins (p. 1836).
- The skim does not mention that E_CohOG+ fails OLI (Appendix counterexample: h=.5, p=.603, q=.103 gives .59; h=.01, p=.65, q=.35 gives .55, with P(E)=.353 in both — verified).
- The skim does not mention the scope restriction. Only two of Roche & Sober's four problems are addressed; "non-explanations" and "explanatory irrelevance" are set aside as not genuine challenges (fn. 4, whose printed text is garbled: a sentence fragment is misplaced into the body of p. 1825).
- The skim does not mention that the Lange reply (§2) is explicitly not specific to coherence measures and that the authors "do not claim that this resolves Lange's challenge completely" (p. 1821).
- The "structurally proper coherence measures" subset (p. 1836) and the "preliminary computational evidence" that Douven–Meijs-ratio and Fitelson(+1) coherence also work are not in the skim; that evidence is not shown in the paper.
