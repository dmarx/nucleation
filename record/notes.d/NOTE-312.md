---
number: 312
status: Read
formerly:
- NOTE-tmpznozh
paper: LIT-357
title: 'Studies on the Foundation of Quantum Mechanics. I'
version: 1
history:
- version: 1
  date: '2026-09-29'
  note: >-
    Read in full (The full paper, *Proceedings of the Physico-Mathematical
    Society of Japan*, 3rd series, 19 (1937), pp. 766–789 (24 pp.), from the
    free PDF on J-STAGE (DOI 10.11429/ppmsj1919.19.0_766; the landing page
    marks the full text world-readable). The PDF is a scan. Its OCR layer is
    unusable, so I read every page from rendered page images, re-rendering
    p. 780 at higher resolution to check the formulas. I read §1
    Introduction; Part I "Logic, system of quantum mechanical propositions":
    §2 (statistical propositions), §3 (specification of states), §4 (meet
    and join), §5 (the modular identity, or the parallelogram law), a second
    "§5" (algebra of quantities; the numbering is the paper's), §6
    (conclusions to Part I); the closing Note; and Figs. 1–2. Nothing was
    skipped. The "note at the end" promised in the p. 774 footnote is the
    short Landau–Peierls note on p. 789. J-STAGE gives only the year, so
    `published:` uses 1 January 1937. The paper was read at a meeting in
    Osaka on 13 March 1937 and received on 31 May 1937. Part II was not
    looked for. No anthology entry exists for this paper.). The first NOTE
    on this paper, which was seeded from its abstract alone.
date: '2026-09-29'
summary: >-
  Husimi derives Birkhoff and von Neumann's lattice axioms from
  statistical premises. Implication is P̄ ≤ Q̄ in every state (and
  requires compatibility), negation is Q̄ = 1 − P̄, and compatible
  propositions obey classical logic. Meet is obtained from "Ehrenfest's
  principle" (additivity of mean values) via the top eigenvalue of aP + bQ
  (pp. 778–779), and the modular law, equivalently the parallelogram law
  |P| + |Q| − |P∩Q| = |P∪Q|, is proved under a finite-chain assumption.
  The orthomodular identity is used but never named or stated as an axiom.
  It appears as the step "since we admit traditional logic to any
  classical part … S + P∩Q = R" for R ⊃ P∩Q (p. 784), and as the case "(Q
  − P) + P = Q provided Q ⊃ P" of a classical identity (p. 780).
---

# NOTE-312: Studies on the Foundation of Quantum Mechanics. I

## Contribution

Birkhoff and von Neumann ([LIT-306](../literature.d/LIT-306.md)) ended their paper with two open questions, which Husimi quotes (p. 767): the experimental meaning of meet and join, and a physical motivation for the modular law L5. This paper answers both inside a stated set of phenomenological axioms. Propositions are statistical predicates of states. Their order and negation are defined from mean values. Meet exists because mean values of quantities add ("Ehrenfest's principle"). Modularity follows from the dimension function (the parallelogram law), which is itself argued from a "super-statistics" counting argument plus the covering property of points. The paper also argues that the multiplication of observables can be dispensed with once spectral decomposition is admitted. It criticises Jordan's quasi-multiplication and Temple's "selective operators".

## Key insight

The logic of quantum propositions can stay two-valued if a proposition is read as a predicate whose argument is a state, and "P implies Q" means P̄ ≤ Q̄ in every state. Non-classicality then lives entirely in *which* combinations of propositions exist. Compatible sets are Boolean. Meet and join of incompatible propositions are not given logically; they are forced by the additivity of expectations. For monomials A = aP and B = bQ, the proposition "A + B takes its greatest possible value a + b" is P ∩ Q (pp. 778–779).

## Assumptions

Axioms are named as in the paper.

- **Ehrenfest's principle** (pp. 767–768): every linear relation between mean values in classical theory survives quantisation. The example is A: mean(A + B) = mean(A) + mean(B).
- **SD** (p. 769): spectral decomposition, A = ∫ λ dλ(Pλ), as the motivation for treating propositions first.
- **St** (p. 770): every proposition P has a probability P̄ in each state.
- **Ip** (p. 771): if P̄ ≤ Q̄ in every state then P ⊂ Q, "at the same time demanding the compatibility P and Q".
- **Ng** (p. 771): if Q̄ = 1 − P̄ in every state, Q is the negation P′.
- **Cl** (p. 771): logical combinations of mutually compatible propositions exist.
- **Assumption F** (p. 773): chains have finite length, with a uniform finite bound. It is explicitly counterfactual for "the more important cases".
- **CS** (Compton–Simon; pp. 774–775): immediate repetition of an observation reproduces the result. **PS** (p. 775): a maximum observation prepares a definite (pure) state.
- **AP** (p. 776): the dimension |P| (the number of points in a spectral decomposition of P) is independent of the decomposition. It is motivated by the "virgin" (uniform) state and by symmetry of transition probability, Σ_Q (P, Q) = Σ_Q (Q, P) = 1.
- **M** (p. 777): meets exist. This is justified via Ehrenfest's principle (pp. 778–779), and joins follow by duality, P ∪ Q = (P′ ∩ Q′)′ (p. 779).
- **Pl\*** (p. 783), from super-statistics: |P| + |Q| ≥ |P ∪ Q|. It is used only in the restricted form "the join of two distinct points is a line" (p. 784).
- **Sb** (p. 783): a set closed under meet, join and *relative* negation U − V (U ⊃ V) is itself a quantum propositional system obeying the chain law. It is proposed, but Husimi "ha[s] not been successful in proceeding this way", and he uses Pl\* instead.

## Key results

- **Order and Boolean blocks (§2, pp. 771–774).** Implication is a partial order with O and I as bottom and top. Negation is an order-reversing involution. A "maximum set" of compatible propositions ("observation-space", following BvN) is Boolean. Under Assumption F, each maximum set is the power set of n mutually exclusive points, with n the length of any complete chain (p. 773). Quantities are written A = Σ aᵢPᵢ, and are "maximum" when the eigenvalues are distinct and "monomial" when A = a·P.
- **States (§3, pp. 774–777).** Mixtures come from incomplete observation. Dimension (AP) and the chain law |P … Q| = |Q| − |P| (p. 777) are established. The statement P̄ > 0 is classical and has "statistical weight" |P| (super-statistics).
- **Meet from additivity (§4, pp. 777–779).** For positive monomials aP and bQ, every R ⊂ P, Q lies under the proposition (A + B = a + b), which is therefore P ∩ Q. The join is obtained by negation (MJ). The derived identities include the lattice laws, P ∩ P′ = O, P ∪ P′ = I, and the modular *inequality*: P ⊂ R ⇒ P ∪ (Q ∩ R) ⊃ (P ∪ Q) ∩ R (p. 779).
- **Why distributivity fails (§4, pp. 779–781).** The classical decomposition of A + B needs Pl′: P − P∩Q = P∪Q − Q. Husimi shows Pl′ is equivalent to the distributive law D. It would make all propositions in a maximum set containing P ∩ Q, P and P ∪ Q compatible with Q, so it "cannot hold in the quantum theory" (p. 780). He prefers Pl′ to D as the characteristic classical condition because it reads as the addition law of probability, W: mean(P∪Q) = P̄ + Q̄ − mean(P∩Q) (p. 781).
- **Modularity (§5 "The modular identity, or the parallelogram law", pp. 781–784).** Md (if P ⊂ Q then P ∪ (Q ∩ R) = Q ∩ (P ∪ R)) is equivalent to Pl (|P| + |Q| − |P∩Q| = |P∪Q|), after Dedekind (p. 782). Pl is "a partial conservation of the addition law of probability", and is the addition law itself in the virgin state (p. 782). Dedekind's theorem that a lattice all of whose sublattices satisfy the chain law is modular is reproduced (Fig. 1). The route through Sb is abandoned, and Fig. 2 shows that a stronger form of Sb with full negation is false (the 16-element free complemented lattice on P ⊂ Q). From Pl\* for points plus the orthomodular step "S + P∩Q = R", Husimi proves: if P and Q cover P ∩ Q, then P ∪ Q covers P and Q. By induction on quadrilaterals this gives the full parallelogram law (p. 784), citing G. Birkhoff (Proc. Camb. Phil. Soc. 29, 441, 1933).
- **Algebra of quantities (second "§5", pp. 784–788).** Meet and join are "analogously constructed" to classical conjunction and disjunction but "not isomorphic" with them, which is why W fails (pp. 784–785). Meet and join cannot be introduced on quantities from the ordering alone, because by Freudenthal's result that would make the algebra classical (p. 785). Multiplication can be replaced by admitting spectral decomposition for each element, so the algebra ℜ of quantities is the linear hull of the propositions 𝔓 (pp. 786–787). The meet and join postulates are necessary for decomposing a sum; sufficiency is left open (p. 787). Temple's selection theory is criticised because addition as mixing makes the mixing ratio "meaningless" apart from the initial state (pp. 787–788).
- **Conclusions (§6, pp. 788–789).** "we have derived the axioms of Birkhoff and v. Neumann on the phenomenological basis". The "only defect" is the super-statistics step. The link between transition probability and the inner product of the resulting projective geometry is deferred "to a following communication".

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Propositions with implication P̄ ≤ Q̄ and negation 1 − P̄ form a bounded, involutively complemented poset whose compatible blocks are Boolean | moderate | Axioms St, Ip, Ng, Cl and direct argument (pp. 770–772); Boolean blocks follow from Cl, which is itself postulated |
| C2 | Under Assumption F each Boolean block is the power set of n points, n the length of any complete chain | moderate | argument p. 773 by successive disjunction and conjunction with chain elements |
| C3 | Additivity of mean values forces the meet: for aP, bQ positive, P ∩ Q = (A + B = a + b) | moderate | informal eigenvalue argument (pp. 778–779); it assumes the spectral decomposition of A + B exists |
| C4 | Pl′ (P − P∩Q = P∪Q − Q) is equivalent to the distributive law and therefore fails in quantum theory | strong | lemma-by-lemma derivation, pp. 780–781 |
| C5 | Md ⇔ Pl, and Pl is the addition law of probability in the virgin state | strong / moderate | Md ⇔ Pl proved following Dedekind (p. 782); the probabilistic reading is interpretive |
| C6 | "The join of two distinct points is a line", plus classical logic on compatible parts, yields the parallelogram law for all quadrilaterals | moderate | covering-property induction, p. 784. The step S + P∩Q = R is the orthomodular identity, justified only by "we admit traditional logic to any classical part" |
| C7 | Sb (closure under meet, join and relative negation, with the chain law) implies Md | weak | "extremely probable" but unproved (p. 783) |
| C8 | Multiplication of quantities is dispensable given spectral decomposition | weak | informal argument, pp. 786–787 |
| C9 | The axioms of Birkhoff and von Neumann are thereby "derived … on the phenomenological basis" | moderate | §6. It holds only under Assumption F and the super-statistics premise (Pl\*), both of which Husimi flags as weak points |

## Method

The paper is axiomatic and argumentative. Physical principles (Ehrenfest additivity, complementarity, Compton–Simon repeatability, uniform a priori probability) are each turned into a named axiom. Lattice-theoretic consequences are then derived, some with short lemma chains (pp. 780–781, 784) and some by informal eigenvalue reasoning (pp. 778–779). Two figures give Hasse diagrams: Dedekind's nine-element sublattice, and the free complemented lattice on P ⊂ Q together with its chain-law and modular quotients.

## Concepts

- **proposition** — a predicate whose argument is a state, with a probability P̄ in each state (St). It is not a truth-valued sentence (p. 770).
- **compatible** — simultaneously decidable in a suitable experiment (p. 771). Implication presupposes it (Ip).
- **maximum set / observation-space** — a maximal set of pairwise compatible propositions. It is Boolean.
- **point, line** — a proposition of dimension 1, respectively 2 (pp. 773, 784).
- **dimension |P| / a priori statistical weight** — the number of points in a spectral decomposition of P (AP, p. 776).
- **virgin state** — the uniform mixture of the pure states of a maximum set (p. 776).
- **super-statistics** — treating the classical statement P̄ > 0 as a disjunction of |P| equiprobable exclusive statements (p. 777).
- **relative negation U − V** — U ∩ V′ for U ⊃ V (p. 780; Axiom Sb, p. 783). It is the operation in which the orthomodular identity V + (U − V) = U is implicit.
- **Ehrenfest's principle** — conservation of classical linear relations between mean values (p. 767). The name is Husimi's.

## Connections

The paper is a direct response to Birkhoff and von Neumann ([LIT-306](../literature.d/LIT-306.md)). It takes their lattice L1–L73 and the modular law L5 as the target, and it shares their finite-dimension assumption, which Husimi calls "Assumption F" and says they also needed (p. 773). [NOTE-275](NOTE-275.md) had credited the orthomodular law to this paper with "unverified here"; the text shows the law is used, not isolated. Husimi reads propositions as predicates on states and insists that quantum logic "can be embedded … in the scheme of traditional logic" (p. 770). That is a different move from the topos programme's multivalued, sieve-valued truth ([LIT-325](../literature.d/LIT-325.md)), which the record holds as the modern answer to the same question. Husimi explicitly rejects many-valued logics (Łukasiewicz, Reichenbach, Février) as unnecessary (p. 770).

## Bearing on the record

- **Map row 1 ("use the orthomodular subspace lattice"; [LIT-306](../literature.d/LIT-306.md) misattributed).** Husimi is only a partial repair. He can be cited for the physical derivation of the BvN lattice, and for the orthomodular identity *as a consequence of* "implication requires compatibility" plus "classical logic within compatible sets". He should not be cited as stating an orthomodular axiom. Since the owner works in finite-dimensional embedding spaces, where subspace lattices are modular and hence orthomodular, the honest citation is BvN ([LIT-306](../literature.d/LIT-306.md)) for the lattice, plus a textbook or survey that states orthomodularity as the infinite-dimensional survivor. Husimi can be added as the historical source of the idea.
- **Map row 5 (non-sequitur as truth-value gap).** Husimi's §2 is relevant and uncited. Complementarity means "we can eventually neither affirm nor deny a given proposition; the decision may be *meaningless*" (p. 769, citing von Neumann's *Grundlagen* p. 134). O and I are "not … proper proposition[s] … which can be either true or false" (p. 775). But he resolves the gap by staying two-valued over states, not by a third truth value. A reader of the owner's truth-value-gap claim should be told that this early source considers the gap reading and declines it.
- **Machine-learning practice.** None. No anthology entry is warranted.

## Limitations

- Everything is proved under Assumption F (finite chains), which the author says fails "in the more important cases of actual quantum mechanics" (p. 773).
- The existence of meet (Axiom M) rests on an informal eigenvalue argument that presupposes spectral decomposition of A + B, which the paper elsewhere treats as something to be derived (p. 787). The argument is circular to that extent.
- The key sharpening from Pl\* to Pl uses the orthomodular step only as "traditional logic in any classical part" (p. 784), without showing that P ∩ Q and R ⊃ P ∩ Q lie in a common maximum set. That follows from Ip, but the paper does not say so.
- Husimi himself names the "super-statistics" premise as "the only defect" (§6).
- Sb ⇒ Md is conjectured, not proved (p. 783).
- Part I stops short of the inner product and the connection between transition probability and Hermitian form (§6, p. 789), which is deferred to Part II.

## Open questions

- Husimi's own: whether Axiom Sb (closure under meet, join and relative negation, with the chain law) implies modularity (p. 783); and whether the meet/join postulates are sufficient, not only necessary, for decomposing a sum of quantities (p. 787).
- For the map: which source to cite for orthomodularity as an axiom (Kalmbach 1983 or Piron, both unread here). And whether the owner's lattice is finite-dimensional, in which case modularity, and so BvN, already suffices.

## Corrections to the seeded skim

- none (there was no seed or dossier)
- The printed title is "Studies on the Foundation of Quantum Mechanics. I." ("Foundation", singular), not "Foundations" as in the batch brief. The volume and pages (19:766–789) are confirmed from J-STAGE metadata and the page heads. The author prints his name as "Kôdi Husimi" (Kōji Fushimi in modern romanisation).
- The brief says Husimi is "usually credited with the orthomodular law". The text does not isolate, name or axiomatise such a law. What it does:
  - **Axiom Ip** (p. 771) builds compatibility into implication: P ⊂ Q is read "as at the same time demanding the compatibility P and Q". **Axiom Cl** (p. 771) makes every maximal compatible set a Boolean algebra ("isomorphic with the field of subsets of a set space", p. 772).
  - Together these entail the orthomodular identity (P ⊂ Q ⇒ Q = P ∪ (P′ ∩ Q)). That inference is mine, not the paper's.
  - The identity is then used as a proof step on p. 784, and written once on p. 780 as a consequence of the classical condition Pl′ that the paper is in the middle of rejecting for quantum theory.
  So "Husimi 1937 introduced the orthomodular law" is at most a reading of Axioms Ip + Cl, not a statement in the paper.
- [NOTE-275](NOTE-275.md) (reading of [LIT-306](../literature.d/LIT-306.md)) says the orthomodular law "was isolated later (Husimi 1937; unverified here)". The text shows that Husimi uses the law but does not isolate it. His stated aim is to supply the "physical motivation … for condition L5 (modular identity)", one of Birkhoff–von Neumann's two open questions, which he quotes (p. 767).
- The derivation is finite-dimensional. **Assumption F** (p. 773) requires every chain of propositions to have finite length with a uniform bound, "introduced for convenience of deductions". Husimi concedes it "does not hold in the more important cases of actual quantum mechanics". In finite dimensions the subspace lattice is modular, and every modular ortholattice is orthomodular (a standard fact, not stated in the paper), so the paper adds nothing there beyond BvN on this point.
