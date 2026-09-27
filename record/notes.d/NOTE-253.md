---
number: 253
status: Read
formerly:
- NOTE-tmp9hu3e
paper: LIT-280
title: 'Towards a complete cohomology invariant for non-locality and contextuality'
version: 1
history:
- version: 1
  date: '2026-09-27'
  note: >-
    Read in full (The full text of arXiv 1807.04203 v1, from the arXiv PDF,
    46 pp.: abstract, §§1–9 (Background; False positives; Joint scenarios
    and joint models; Contextuality of joint models; Cyclic models, paths
    and cycles; Cohomology of cyclic models with the §7.2.1 examples;
    Extension to general models with the §8.1 examples, including the full
    91-equation system for the Kochen–Specker cover; Conclusions and
    Conjecture 9.1), acknowledgements and all 20 references. The paper has
    no appendices. Nothing was skipped. The arXiv abstract page lists one
    version only, v1 (11 Jul 2018, 733 KB; comment "46 pages, 25 figures";
    quant-ph only), with no journal reference and no DOI other than the
    arXiv DataCite one. The PDF's own title is "Towards a complete
    cohomological invariant…" (the arXiv listing says "cohomology").
    `pdftotext` was not available, so I extracted the text with PyMuPDF. The
    bundle diagrams (Figs 1–25) do not survive extraction. I read the tables
    and the linear systems from the text. I did not use the figures for any
    claim I checked; I recomputed those instead. I then implemented the
    paper's joint-model construction and its ℤ/2 obstruction myself, as
    exact linear algebra over GF(2), with GF(1000003) as a stand-in for ℚ. I
    checked every worked example and ran a randomised test of the main
    theorem (details under Key results).). The first NOTE on this paper,
    which was seeded from its abstract alone.
date: '2026-09-27'
summary: >-
  For cyclic scenarios, where the contexts' intersection graph is a single
  chordless N-cycle, Carù proves that ℤ/2 Čech cohomology of the (N−1)-th
  iterated "joint model" is a complete invariant for logical and strong
  contextuality (Thm 7.7). I confirmed this on the Hardy model, on his own
  2017 counterexample (detected on all 22 sections at level 3) and on 659
  random contextual cycle models. The extension beyond cycles does not
  hold as stated. Prop 8.2 is false on the paper's own Table 5 model.
  Worse, the one non-cyclic case the paper claims to repair, the §8
  Kochen–Specker cover of Abramsky–Mansfield–Barbosa, is never detected at
  any level under the paper's definitions (my proof and computation). That
  refutes the paper's closing Conjecture 9.1.
---

# NOTE-253: Towards a complete cohomology invariant for non-locality and contextuality

## Contribution

AMB 2011 ([LIT-277](../literature.d/LIT-277.md)) introduced the Čech obstruction γ as a sufficient witness of contextuality. Carù 2017 ([LIT-279](../literature.d/LIT-279.md), [NOTE-252](NOTE-252.md)) showed that γ can miss strong contextuality on every section of a model on the Bell cover. This paper changes the model, not the cohomology.

- *The construction.* It replaces a model S by its "joint model" S^(1). The measurements of S^(1) are the old contexts, its contexts are pairs of overlapping old contexts, and its sections are compatible pairs of old sections. Iterating gives S^(k), and the paper computes the ordinary ℤ/2 obstruction there.
- *What is proved.* On cyclic scenarios, where the contexts form one chordless cycle of length N, the obstruction on S^(N−1) detects exactly the logically contextual sections, and it is non-zero everywhere exactly when S is strongly contextual (Thm 7.7). That covers the Bell (2,2,d) cover, the N-cycle (KCBS-type) scenarios, and hence both the Hardy model and Carù's own 2017 counterexample.
- *What is not.* An extension to non-cyclic scenarios is offered through a "cyclic contextuality property" (Thm 8.4). Completeness in general is left as Conjecture 9.1.

## Key insight

The false negatives of γ come from "Z-shaped" signed combinations over one context: s₁t₁ + s₂t₁ + s₂t₂ has the same marginals as the single section s₁t₂. That shape is only a false witness when s₁t₂ is *not* in the support.

- *Why the joint model removes it.* A context of the joint model is a pullback: a union of full rectangles A_u × B_u, one per value u on the overlap. So a Z over a joint context always closes (Lemma 7.4, the "no-Z lemma").
- *Why iteration matters.* Iterating the construction turns a path of n contexts into a single context n levels up. That lets an induction on n replace any signed "partial family" along a path by a genuine one (Thm 7.6).
- *Why N − 1 levels suffice on a cycle.* On an N-cycle, one context of level N − 1 already spans the whole cycle minus its closing edge. Cohomology there is asking whether a genuine path around the cycle closes up.

## Assumptions

- **Scenario and model (§2.1), as in [LIT-278](../literature.d/LIT-278.md) and [LIT-279](../literature.d/LIT-279.md).**
  - *The scenario.* ⟨X, M, (O_m)⟩, with X finite and M an antichain cover.
  - *Possibilistic models only.* S ⊆ ℰ satisfying:
    - (1) S(C) ≠ ∅;
    - (2) flasque beneath the cover (possibilistic no-signalling);
    - (3) compatible families glue.
  - *LC and SC.* LC(S, s): s lies in no compatible family. SC: LC at every s.
- **The obstruction (§2.2).** The ordinary relative γ_{C₀} of AMB/ABKLM, via the snake lemma.
  - *Prop 2.1.* γ(r₀) = 0 iff r₀ lies in a compatible family of F.
  - *Theorem 2.2.* CLC ⇒ LC and CSC ⇒ SC.
- **Coefficients.** F^(k) := F_{ℤ₂} S^(k) (eq. 3, §7.1).
  - *Where ℤ/2 is used.* The no-Z lemma uses 2 = 0.
  - *Not essential (my observation).* Lemma 7.5 holds over any ring by a one-line argument: a 1-partial family's two marginals are single sections s₁, t_l with s₁|∩ = t_l|∩, so (s₁, t_l) is in the pullback. I also confirmed Thm 7.7 numerically over GF(1000003).
- **Connectedness.** Covers are connected (footnote 7), and |M^(k)| ≥ 2 for all k (Remark 4.4). The scenarios excluded by the second condition are acyclic in Barbosa's sense, and by Vorob'ev's theorem they carry no contextuality.
- **Cyclic scenario (Def 6.6).** M^(1), the intersection graph of the contexts, is a chordless cycle. Then every M^(k) is a chordless |M|-cycle (Prop 6.7).
- **Cycles in Def 6.2 may have chords.** An n-cycle for M^(k) is any closed simple path in the intersection graph. Chordless cycles are singled out separately. This matters for §8 (Limitations).
- **Cyclic contextuality property, CCP (Def 8.1).** Every LC section s is LC on the restriction S|_{D•} to some "cycle" D• ⊆ M.
- **No-signalling built in.** There is no probabilistic content. The "strong" in the title is SC in the Abramsky–Brandenburger sense.

## Key results

- **Defs 4.1, 4.3 (joint scenarios).**
  - *First joint scenario.* X^(1) := M. M^(1) := {{C, C′} : C ≠ C′, C ∩ C′ ≠ ∅}. O^(1)_C := ℰ(C).
  - *Iteration.* The k-th joint scenario is the first joint scenario of the (k−1)-th.
  - *Well defined (Prop 4.2).* Every joint cover is a graph: its contexts have size 2.
- **Def 4.5, Prop 4.6 (joint models).** S^(1)(U) := compatible tuples (s_C)_{C∈U} with s_C ∈ S(C). On a context {C, C′} this is the pullback S(C) ×_{S(C∩C′)} S(C′). S^(1) is again an empirical model (conditions 1–3 proved), and S^(k) is iterated likewise (Def 4.7).
- **Prop 5.1 (proved).** LC(S, s) ⇔ ∃C′ overlapping C such that every t ∈ S(C′) matching s gives LC(S^(1), (s, t)) ⇔ the same for every C′.
  - *Cor 5.2.* SC(S) ⇔ SC(S^(1)).
  - *Cors 5.4, 5.5.* LC(S, s) ⇔ LC^(k)(S, s) for some or all k. SC(S) ⇔ SC(S^(k)).
  - *Def 5.3.* LC^(k)(S, s) means LC(S^(k), t) for *all* t with s ∈ flatten(t).
- **Def 7.1.** CLC^(k)(S, s) means CLC(S^(k), t) for **every** section t of S^(k) with s ∈ flatten(t).
- **Thm 7.2 (proved).** CLC^(k)(S, s) ⇒ LC(S, s), and CSC(S^(k)) ⇒ SC(S). So soundness is inherited at every level.
- **Def 7.3.** An n-partial family is a compatible F^(k)-family over an n-path of M^(k) whose two end-restrictions are genuine sections. It is "standard" if some genuine S^(k)-family on the path has the same ends.
- **Lemma 7.4 (no-Z) and Lemma 7.5 (proved).** Every 1-partial family is standard. The proof of 7.5 is an algorithm that repeatedly contracts a Z. It terminates because each step removes 2 or 4 summands, a point the paper leaves implicit. A shorter proof is noted under Assumptions.
- **Thm 7.6 (proved; the key technical result).** On a cyclic scenario, for k ≥ 1 and n ≤ k with n < |M|, every n-partial family for F^(k) is standard.
  - *Proof.* Induction on k, restricting each component to the shared vertex (Remark 4.8, Prop 6.9).
  - *My check.* I checked the compatibility chain in Claim 1 and the gluing in Claim 2. They go through because both composites F^(k)(C) → F^(k−1)(K_i ∩ K_{i+1}) agree on basis elements.
  - *A typo.* In eq. (15), "S^(k−1)(C¹₁)" should read S^(k−1)(C²_n).
- **Thm 7.7 (main theorem; proved).** On a cyclic scenario with n := |M| − 1:
  - LC(S, s) ⇔ CLC^(n)(S, s) for every section s;
  - SC(S) ⇔ CSC(S^(n)).

  **My verification.** It holds on every case I tried, under the paper's Def 7.1 with ℤ/2.
  - *Carù 2017 (2,2,4) model ([LIT-279](../literature.d/LIT-279.md)).* All 22 sections are strongly contextual.
    - Levels 0, 1 and 2: detected on 0/22.
    - Level 3: detected on 22/22, and CSC(S^(3)) holds. S^(3) has 48 sections.
    - This confirms the paper's §7.2.1 claims (Figs 18–21).
  - *Hardy.* Detected on 0/13 at levels 0–2, and on 1/13 at level 3: exactly the one LC section (a1,b1) ↦ 00. Level N − 1 is needed, so the bound is tight here, as the paper says.
  - *Table 2 model (5 LC sections).* Detected on 2, 2, 2, 5 at levels 0–3.
  - *PR box.* Detected everywhere from level 0, and the detection persists.
  - *Random test.* 659 random contextual models with random flasque supports on N-cycles with N = 3, 4, 5, 6 and 2–3 outcomes:
    - 0 violations of LC ⇔ CLC^(N−1), and 0 of SC ⇔ CSC(S^(N−1)) on the 3 SC instances;
    - 0 violations of monotonicity in k;
    - level N − 2 was insufficient in 617 of 659 models.
  - *Over a large prime field (standing in for ℚ).* Same results on the named models.
- **§7.2.1 examples.** The Hardy and Carù-2017 claims are confirmed (above). The Table 2 claim that level 1 suffices is false under Def 7.1 and true only under the existential reading (corrections).
- **Def 8.1 (CCP), Prop 8.2, Prop 8.3, Thm 8.4.**
  - *Prop 8.2.* If S has CCP, then LC(S, s) ⇔ CLC^(n−1)(S, s), with n the size of s's contextual cycle.
  - *Prop 8.3 (proved; consistent with all my runs).* CLC^(k) ⇒ CLC^(l) for l ≥ k, and likewise for CSC.
  - *Thm 8.4.* With CCP, and N the largest cycle in M^(1): LC ⇔ CLC^(N−1) and SC ⇔ CSC(S^(N−1)).

  **Two defects (mine).**
  - (i) *Prop 8.2 needs the contextual cycle to be chordless.* Its proof applies Thm 7.7 to S|_{D•}, which needs D• to be cyclic, i.e. chordless. But Def 8.1 uses Def 6.2's cycles, which may have chords.
  - (ii) *The step "CLC^(n−1)(S|_{D•}, s) readily implies CLC^(n−1)(S, s)" is not argued, and it is false.* Def 7.1 quantifies over sections t at contexts of M^(n−1) that leave the cycle, and a vanishing obstruction there is not excluded.

  **Counterexample: the paper's own Table 5 model, section s₁₀ = (b,d) ↦ (1,1).**
  - *The setting.* Its contextual cycle is the triangle {bc, bd, cd}, so n = 3. On that sub-cover, CLC^(2) holds (my computation, as Thm 7.7 says).
  - *The failure.* In the whole model, the level-2 section t built over ab–bd–cd, which contains s₁₀, lies in a compatible ℤ/2 family. I exhibited it and checked it on every overlap. So CLC^(2)(S, s₁₀) fails, and Prop 8.2 is false.
  - *Thm 8.4's conclusion survives for this model.* All 7 LC sections are detected at level 3, hence at level 4 by Prop 8.3. But its proof goes through Prop 8.2.
- **§8.1, the AMB §8 Kochen–Specker cover {A,B,C},{B,D,E},{C,D,E},{A,D,F},{A,E,G}.** This is the only non-cyclic known false negative, and the test case for (b).
  - *Level 0.* The paper's ℤ/2 system has a wrong equation (corrections). Correctly, γ vanishes over ℤ/2 on 9 of 15 sections, matching [NOTE-250](NOTE-250.md).
  - *Level 1.* The paper claims S^(1) removes every false positive. Under Def 7.1 my count is still 6/15 detected (unchanged). Even under the existential reading, 12/15: the three sections with A ↦ 1 remain undetected, including s_{ABC,A}. The paper's contradiction "0 = u = a ⊕ b ⊕ t" is refuted by an explicit family through (s_{ABC,A}, s_{AEG,A}). I found it by solver and checked it independently on all overlaps.
  - *Every level (my lemma and proof).*
    - *Lifting.* Any compatible R-family on S^(k) lifts to a compatible family on S^(k+1), over any ring R. Each joint context is a union of full rectangles, and flasqueness makes every fibre two-sided. A component that is a single genuine section on both ends can be lifted as that single pair.
    - *The family.* ABC ↦ s_A, BDE ↦ s_D, CDE ↦ s_D, ADF ↦ s_A + s_D + s_F (ℤ/2; over ℤ, s_A + s_D − s_F), AEG ↦ s_A. It is compatible, and genuine on the four contexts other than ADF, whose intersection graph is K₄.
    - *The consequence.* For every k, some t ∈ S^(k) containing s_{ABC,A} has γ(t) = 0. I built the lifted family explicitly up to level 4, the level Thm 8.4 would prescribe since the largest cycle in K₅ is 5, and checked it compatible. At level 4 it has a single genuine section containing s_{ABC,A} at 177 of the 1350 contexts.
    - *The same holds for all 9 sections with vanishing level-0 γ.* Each lies in a ℤ/2 family that is genuine on four contexts forming K₄ (by hand, from the 3-dimensional solution space).
    - *Measured counts.* Def-7.1 counts stay at 6/15 for levels 0–3. CSC(S^(k)) is false at every level.
  - *Consequences.*
    - (1) The §8.1 claim and the Conclusions' "gets rid of all the known false positives" are false for this model.
    - (2) **Conjecture 9.1** ("∃k: LC(S, s) ⇔ CLC^(k)(S, s) for all s") is **false**: s_{ABC,A} is LC, but CLC^(k) fails for every k. That holds with ℤ/2 as the paper fixes it, and with ℤ.
    - (3) Under the chordal reading of CCP, the model has CCP (the whole 5-cycle) and Thm 8.4 is false for it. Under the chordless reading, it lacks CCP: of its 15 sections, 11 are LC on no chordless cycle (the only chordless cycles of K₅ are triangles). So the paper's "all the models that have appeared in the literature … share this property" is false for its own example.
  - *A repair I computed, not in the paper.* Read CLC existentially: some context K of level k at which *every* t ∋ s has γ(t) ≠ 0. That reading is sound, by the same argument as Prop 5.1, and it detects all 15 sections of this model at level 2. Whether it is complete in general is open.
- **Conjecture 9.1.** Stated with a four-condition heuristic (contextual, non-cyclic, no CCP, false positive at every level). Refuted as stated (above).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | S^(1), and hence every S^(k), is a well-defined empirical model; SC(S) ⇔ SC(S^(k)); LC(S, s) ⇔ LC^(k)(S, s) | strong (proof) | Props 4.2, 4.6, 5.1; Cors 5.2, 5.4, 5.5 |
| C2 | Non-vanishing joint-model obstruction is sound: CLC^(k) ⇒ LC, CSC(S^(k)) ⇒ SC | strong (proof) | Thm 7.2 |
| C3 | On joint contexts, every 1-partial family is standard (no Z-shaped false witness survives) | strong (proof; a one-line proof over any ring also works) | Lemmas 7.4, 7.5 |
| C4 | On cyclic scenarios, n-partial families with n ≤ k, n < \|M\| are standard | strong (proof) | Thm 7.6 |
| C5 | On cyclic scenarios, LC ⇔ CLC^(\|M\|−1) and SC ⇔ CSC(S^(\|M\|−1)) | strong (proof; confirmed on Hardy, Carù 2017, Table 2, PR and 659 random cycle models) | Thm 7.7; my computation |
| C6 | Carù 2017's strongly contextual model is detected at level 3 on every section, not at levels 1–2 | strong after my check (the paper argues from Figs 18–21) | §7.2.1; my computation, 0/22, 0/22, 22/22 |
| C7 | The bound \|M\| − 1 is tight (Hardy needs level 3) | strong (example, confirmed) | §7.2.1 |
| C8 | The Table 2 model is already detected at level 1 | false under Def 7.1 (level 3 needed); true only under an existential reading the paper does not state | §7.2.1; my computation |
| C9 | With CCP, LC ⇔ CLC^(n−1) for n the contextual cycle's size | false as stated (the paper's Table 5 model, s₁₀, n = 3, fails at level 2); the proof step "readily implies" is unargued, and "cycle" must be chordless for Thm 7.7 to apply | Prop 8.2; my counterexample, explicit family checked |
| C10 | CLC^(k) is monotone in k | strong (proof; consistent with all runs) | Prop 8.3 |
| C11 | With CCP, SC ⇔ CSC(S^(N−1)), N the largest cycle in M^(1) | unproven (rests on C9); false for the AMB §8 model under the chordal reading of CCP | Thm 8.4; my lemma and computation |
| C12 | "Most" models, and all models in the literature, have CCP | weak (assertion); false for AMB §8 under the chordless reading its proof needs | §8, p. 36 |
| C13 | The first joint model removes all false positives of the AMB §8 Kochen–Specker model | false (explicit ℤ/2 family through (s_{ABC,A}, s_{AEG,A}); the paper's level-0 system has a wrong equation) | §8.1; my computation |
| C14 | Conjecture 9.1: some level k makes CLC^(k) a complete invariant for every model | refuted as stated (AMB §8 model, s_{ABC,A}, every k, over ℤ/2 and ℤ) | §9; my lifting lemma |
| C15 | The invariant is obtained "without compromising the practical computability" | weak (assertion; no complexity analysis). It is linear algebra, but on objects that grow exponentially (AMB §8: 5, 10, 30, 150, 1350 contexts at levels 0–4) | §1; my measurements |

## Method

- **Transform the model, keep the cohomology.**
  - *Iterate the pullback.* Iterate the joint-model construction (a pullback of adjacent contexts).
  - *Compute the obstruction.* Compute the usual relative Čech obstruction with ℤ/2 coefficients on S^(k), and collect it over all t with s ∈ flatten(t) (Def 7.1).
- **Proof technique.**
  - *Graph combinatorics.* Paths and chordless cycles in the iterated intersection (line) graphs (§6).
  - *The no-Z lemma.* It handles single contexts.
  - *Induction.* An induction that trades path length for level (Thm 7.6).
- **Examples.** Bundle diagrams with hand-solved ℤ/2 systems (Table 2), pictures (Hardy, Carù 2017), and a machine-solved 91-equation ℤ/2 system (§8.1).
- **My re-check.** I built S^(k) literally from Defs 4.1 and 4.5. For each context I tested whether the unit vector of each section lies in the projection of the kernel of the compatibility system, over GF(2) and GF(1000003). I evaluated Def 7.1 and an existential variant, and verified every witness family independently on all overlaps.

## Concepts

- **Joint scenario / joint model, S^(k)** — measurements are the previous contexts, contexts are overlapping pairs, sections are compatible pairs. A section of S^(k) is a compatible family over a "walk" of k + 1 base contexts.
- **flatten(t)** — the base sections occurring in a section t of S^(k) (Remark 4.9). The text says "sections of S^(k)"; it means sections of S.
- **LC^(k), CLC^(k)** — LC or CLC at every level-k section containing s (Defs 5.3, 7.1).
- **n-path, n-cycle, chordal; proper and improper 3-cycles** — Def 6.2, §6.1.1, in the graph M^(k).
- **Cyclic scenario** — M^(1) is a chordless cycle (Def 6.6).
- **n-partial family; standard form** — Def 7.3.
- **Z-shape / cohomology loop / non-standard loop** — a signed path s₁t₁ ± s₂t₁ ± s₂t₂ inside one context, the mechanism of false witnesses (§3, footnote 5).
- **Cyclic contextuality property (CCP)** — Def 8.1.
- **False positive** — as in [LIT-277](../literature.d/LIT-277.md) and [LIT-279](../literature.d/LIT-279.md): a false *negative* of the witness.

## Connections

- **[LIT-277](../literature.d/LIT-277.md) (AMB 2011, [NOTE-250](NOTE-250.md)).** This paper uses its obstruction unchanged, on transformed models.
  - *Hardy.* Hardy's possibilistic contextuality, invisible to [LIT-277](../literature.d/LIT-277.md)'s γ over ℤ and ℤ/2 on all 13 sections, is detected at level 3.
  - *The §8 cover.* The paper claims to fix it and does not. Its ℤ/2 recount of the §8 cover contradicts [NOTE-250](NOTE-250.md)'s 9/15, and [NOTE-250](NOTE-250.md) is right.
- **[LIT-279](../literature.d/LIT-279.md) (Carù 2017, [NOTE-252](NOTE-252.md)).** The direct sequel. The 2017 conclusion's hope of obstruction theory and Postnikov towers is dropped; the 2018 paper instead changes the model.
  - *The 2017 counterexample.* It is on a cyclic scenario, so Thm 7.7 covers it. Detection at level 3 is confirmed.
  - *What remains of the 2017 analysis.* Level 3 detection does not rescue ordinary γ. [NOTE-252](NOTE-252.md)'s statement that γ misses it at every section stands.
- **[LIT-278](../literature.d/LIT-278.md) (ABKLM 2015, [NOTE-251](NOTE-251.md)).** It supplies the connecting-homomorphism definition (Prop 2.1, Thm 2.2).
  - *Beyond AvN.* The new invariant detects models outside the All-vs-Nothing class. Hardy is not SC. The 2017 model and the §8 cover are SC without AvN, per [NOTE-251](NOTE-251.md) and [NOTE-252](NOTE-252.md).
  - *Whether this contradicts Thm 21.* It does not: Thm 21 concerns γ on S itself.
- **[LIT-016](../literature.d/LIT-016.md) (Abramsky & Brandenburger).** Supplies the framework, with no-signalling as flasqueness.
- **Barbosa's thesis [Bar15] and Vorob'ev [Vor62].** They are cited for "acyclic ⇒ non-contextual", which motivates restricting to cycles. The paper also asserts, without proof, that every cyclic cover in Barbosa's sense contains a cyclic subcover in this paper's sense. Not in the record; unverified.
- **[ABCP17] (Abramsky, Barbosa, Carù, Perdrix; Crossref DOI 10.1098/rsta.2016.0385).** It is cited for stabiliser strong contextuality being witnessed on a 4-cycle; unverified here. Not in the record.
- **The complexity context (my remark, unverified citation).** On a cycle, logical contextuality is decidable directly by composing the support relations around the cycle, in polynomial time. Here the invariant enumerates every compatible path. I recall that deciding possibilistic non-locality is NP-complete in general (Abramsky, Gottlob & Kolaitis, IJCAI 2013). If so, no complete invariant of this kind can be polynomial-size in general, unless P = NP. That citation was not checked in this session.
- **Anthology.** No ANTH- citation is warranted. Earlier readings found nothing on cohomology or contextuality in the Anthology of the SOTA.

## Bearing on the record

- **[THEORY-012](../theory.d/THEORY-012.md) (Active).** Its cohomology bullet says the obstruction is "a computable relaxation" of the exact criterion, complete on All-vs-Nothing models, with three documented failures. This paper supports and refines that without contradicting it.
  - *What it adds.*
    - (a) On cyclic covers (the Bell (2,2,d) and N-cycle scenarios), γ computed on the (N−1)-th iterated joint model is exactly complete for logical and strong contextuality. That covers Hardy and [LIT-279](../literature.d/LIT-279.md)'s counterexample, so two of the three documented failures are removable by changing the model rather than the coefficients.
    - (b) Beyond cycles, nothing general is established. The §8 cover stays undetected at every level under the paper's definitions (my lemma), and the paper's completeness conjecture is false as stated.
    - (c) The price of completeness is size. The joint models grow exponentially, so "computable relaxation" should not be read as "polynomial".
  - *Proposed wording.* See the report line. The bullet's "Still open" line survives.
- **[THEORY-014](../theory.d/THEORY-014.md) (Proposed).** It refines, but does not change, the reading [NOTE-251](NOTE-251.md) and [NOTE-252](NOTE-252.md) gave. The ℤ-relaxation fails through signed "Z" combinations inside one context. Pulling back to joint contexts, which are unions of full rectangles, is exactly what makes such combinations harmless. The inference is mine; no status change.
- **[LIT-265](../literature.d/LIT-265.md) (contextual fraction; Deferred).** No bearing beyond [NOTE-252](NOTE-252.md)'s remark.
- **[THEORY-013](../theory.d/THEORY-013.md), [THEORY-015](../theory.d/THEORY-015.md), [THEORY-016](../theory.d/THEORY-016.md).** No bearing.
- **ML practice.** It carries nothing. This is algebraic topology for quantum foundations. A DeepMind-funded scholarship is not a connection.
- **For filing.**
  - *Tags.* `contextuality`, `quantum-foundations`, `mathematics`, mirroring [LIT-277](../literature.d/LIT-277.md), [LIT-279](../literature.d/LIT-279.md) and [THEORY-012](../theory.d/THEORY-012.md).
  - *Lineage.* It extends [LIT-279](../literature.d/LIT-279.md) (resolves its counterexample) and [LIT-277](../literature.d/LIT-277.md) (answers the Hardy gap on cyclic covers). It corrects nothing in either. Its own recount of [LIT-277](../literature.d/LIT-277.md)'s §8 case is itself wrong.

## Limitations

- **Completeness is proved for cyclic scenarios only.** That excludes (2,3,2) and larger Bell covers, GHZ-type tripartite covers and most Kochen–Specker covers. The "Towards" of the title is accurate. The abstract's "vast majority of empirical models" is not established.
- **§8 does not hold as written.**
  - *Prop 8.2 is false.* It fails on the paper's own Table 5 model.
  - *Thm 8.4 is unproved.* It is false on AMB §8 if CCP allows chordal cycles, and vacuous there if not.
  - *The CCP prevalence claim is unsupported.*
- **The one non-cyclic example is mishandled.** There is a wrong equation at level 0, and a false "no family exists" at level 1. Under Def 7.1 the invariant never detects the model, which refutes Conjecture 9.1.
- **The definitions and the examples diverge.** The theorems use the universal Def 7.1. The examples silently use an existential, context-wise reading. The existential reading is sound and stronger in practice (it detects AMB §8 at level 2, my computation), but it is neither defined nor proved complete.
- **Computational cost is never analysed.** On an N-cycle, S^(N−1) has one section per compatible open path around the cycle, which is exponential in N in general, and a direct check is already polynomial there. Off cycles, the number of contexts grows like iterated line graphs: 5, 10, 30, 150, 1350 for the §8 cover.
- **Possibilistic only.** Nothing is said about probabilistic contextuality or its degree. The coefficients are fixed to ℤ/2, although the proofs do not need them.
- **Arguments from pictures.** The Hardy and Carù-2017 detections at level 3 are argued from Figs 17 and 21 ("The reader can verify"). They are true (my check) but not shown in the text.
- **Slips.**
  - "Theorem 2.2" for Theorem 7.7 (pp. 15, 33);
  - "[Car15]" for [Car17] (Fig 19);
  - the Table 7 header "(1,0,0), (0,1,0), (1,0,0)" (the third should be (0,0,1));
  - "b1" for a variable in the §8.1 system;
  - eq. (15)'s S^(k−1)(C¹₁);
  - "Theferefore", "ciclicity", "litterature", "Becuase", "emirical";
  - the title's "cohomological" (PDF) against "cohomology" (arXiv).

## Open questions

- **Is the existential variant complete?** Is "some context at which every containing section is detected" complete for all finite models at some level? It detects AMB §8 at level 2 and every cyclic model by Thm 7.7. A proof, or a counterexample, would settle what this paper set out to do.
- **A correct CCP statement.** Is Thm 8.4 true when the contextual cycle is required to be chordless, and when CLC is read existentially? The Table 5 counterexample to Prop 8.2 does not refute it.
- **Is there a more compact certificate?** Is there a polynomial-size cohomological certificate on cycles, better than enumerating all N-paths? Given the (unverified) NP-hardness in general, which classes admit one?
- **Carù's 2019 thesis.** Does "Logical and Topological Contextuality in Quantum Mechanics and Beyond" repair §8 or Conjecture 9.1? Unverified; not obtained.

## Corrections to the seeded skim

- none (there was no seed or dossier)
- **What the abstract claims, against what the body shows.** The abstract says "we introduce a cohomology invariant for possibilistic and strong contextuality which is applicable to the vast majority of empirical models". The introduction adds "without compromising the practical computability", and the Conclusions say the invariant "gets rid of all the known false positives from the literature, and proved its efficacy in general models". What the body proves:
  - *Proved.* Completeness on cyclic scenarios only (Thm 7.7).
  - *Proved on a false step.* The extension to models with the "cyclic contextuality property" (Prop 8.2, Thm 8.4) rests on an unargued step ("readily implies"), and Prop 8.2 is false as stated (my Table 5 counterexample below).
  - *Asserted.* "Vast majority" and "all the models that have appeared in the literature … share this property" have no support. The paper's own §8.1 Kochen–Specker model lacks the property on the reading its proof needs.
  - *Not shown.* Computability is never analysed. The size of the object grows exponentially (below).
- **The §8.1 Kochen–Specker analysis is wrong at both levels.**
  - *Level 0.* The ℤ/2 system contains a wrong equation: "a ⊕ c = d ⊕ f" for the overlap {A,B,C}∩{B,D,E} at B ↦ 0 should read a ⊕ c = e ⊕ f. With that error the solution space collapses to 2 dimensions, and the paper concludes that the obstruction vanishes on only 4 of 15 sections. The corrected system has a 3-dimensional solution space, and the obstruction vanishes on 9 of 15 sections, as [NOTE-250](NOTE-250.md) found.
  - *Level 1.* The paper claims the first joint model removes all false positives. It does not. I exhibit an explicit compatible ℤ/2 family through the very section the paper says cannot be extended, (s_{ABC,A}, s_{AEG,A}), and checked it on every overlap. Under the paper's Definition 7.1 the invariant never detects this model at any level (Key results).
- **The worked examples use a weaker definition than the one the theorems use.**
  - *Definition 7.1.* CLC^(k)(S, s) requires a non-zero obstruction at *every* section t of S^(k) with s ∈ flatten(t).
  - *The examples.* The Table 2, Hardy, Table 5 and Kochen–Specker examples check only "the only section containing s" at *one* chosen context.
  - *Where they disagree.* On Table 2 the paper says level 1 detects s₂ "although |M| = 4". Under Def 7.1 it does not: t = ((a1,b1) ↦ 11, (a2,b1) ↦ 11) has vanishing obstruction, and Def 7.1 needs level 3. On Table 5 the paper says level 1 detects s₁₀. Under Def 7.1 level 3 is needed.
  - *The existential reading is sound.* It is what the examples compute, but the paper never states it.
- **"The size of the largest cycle in this scenario is 4" (Table 5, p. 38) is wrong.** The intersection graph has the Hamiltonian 5-cycle ab–ad–cd–bc–bd. So Thm 8.4's level is 4, not 3.
- **Identification note for filing.**
  - *No published version.* Crossref has no published version: a title search, and an author search on Carù, return only the 2017 EPTCS paper and unrelated works (no contact address was sent). So no `doi:` is given.
  - *The author's own listing.* His Oxford publications page lists it as "Towards a cohomology invariant for non-locality and contextuality" (2018), with no venue.
  - *The thesis.* The same page lists his DPhil thesis, "Logical and Topological Contextuality in Quantum Mechanics and Beyond" (Oxford, 2019). Whether the thesis contains or corrects this material is unverified; I did not obtain it.
  - *A talk.* A slide deck "Towards a complete cohomology invariant for contextuality" exists from the QCQMB 2018 Prague workshop (not read).
  - *Affiliation.* Department of Computer Science, University of Oxford.
  - *Funding.* The Oxford-Google DeepMind Graduate Scholarship and the EPSRC DTP.
