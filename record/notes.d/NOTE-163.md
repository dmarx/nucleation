---
number: 163
status: Read
formerly:
- NOTE-tmprstgd
paper: LIT-124
title: 'SEP — Mereology'
version: 2
history:
- version: 2
  date: '2026-09-26'
  note: >-
    Read in full (the full current revision of the SEP entry, fetched as
    HTML on 2026-09-26 (rawM/mereology.html, rawM/mereology-notes.html) and
    converted to text. The header reads "First published Tue May 13, 2003;
    substantive revision Sat Jun 27, 2026", and the notes page is "Copyright
    © 2026 by Achille Varzi". I read all of it: the preamble, §1, §2.1–2.2,
    §3.1–3.4, §4.1–4.5, §5, all 48 notes on the separate notes page, and the
    Related Entries list. Not read: Figures 1–9 are images, so I read them
    only through their captions and the text that describes them. The
    bibliography (about 2,800 lines of "Cited Works" and "Monographs and
    Collections") was scanned but not checked item by item. I did not open
    "Other Internet Resources" or "Academic Tools".). Upgraded from
    `Skimmed` to `Read`: the claims table, assumptions and results are new,
    and the skim is corrected where the full text disagreed.
date: '2026-09-26'
summary: >-
  The entry argues that no mereological principle, not even the
  partial-order core M (Reflexivity, Transitivity, Antisymmetry), is
  merely a fixing of the meaning of "part". It lays out the ladder M ⊂ MM
  (+Supplementation) ⊂ EM (+Strong Supplementation) ⊂ GEM (+Unrestricted
  Sum). GEM is "virtually" a complete Boolean algebra with zero removed,
  and it is reached from M by exactly three adequate pairings:
  Supplementation + Unrestricted Sum2, Strong Supplementation +
  Unrestricted Sum3, and Complementation + Unrestricted Sum1. The
  influential Simons (1987) pairing, Supplementation + Unrestricted Sum3,
  which the entry's own 2003 edition also used, does not yield GEM.
---
<!-- inactive-ok-file: LIT-173 — Deferred: a related seed named by a 2026-09-26 close reading on the mereology tag; lapses when the cited work is read -->
<!-- inactive-ok-file: LIT-159 — Deferred: a related seed named by a 2026-09-26 close reading on the mereology tag; lapses when the cited work is read -->
<!-- inactive-ok-file: LIT-113 — Deferred: a related seed named by a 2026-09-26 close reading on the mereology tag; lapses when the cited work is read -->
<!-- inactive-ok-file: LIT-188 — Deferred: a related seed named by a 2026-09-26 close reading on the mereology tag; lapses when the cited work is read -->
<!-- inactive-ok-file: LIT-167 — Deferred: a related seed named by a 2026-09-26 close reading on the mereology tag; lapses when the cited work is read -->
<!-- inactive-ok-file: LIT-157 — Deferred: a related seed named by a 2026-09-26 close reading on the mereology tag; lapses when the cited work is read -->
<!-- inactive-ok-file: LIT-097 — Deferred: a related seed named by a 2026-09-26 close reading on the mereology tag; lapses when the cited work is read -->
<!-- inactive-ok-file: LIT-168 — Deferred: a related seed named by a 2026-09-26 close reading on the mereology tag; lapses when the cited work is read -->
<!-- inactive-ok-file: LIT-005 — Proposed: read in full and unproven as a formal criterion; cited as a related account, not as an established result -->
<!-- inactive-ok-file: LIT-049 — Proposed: read in full and unproven as a formal criterion; cited as a related account, not as an established result -->

# NOTE-163: SEP — Mereology

## Contribution

The entry is a critical survey of formal mereology in the Leśniewski / Leonard–Goodman tradition. It regiments the principles as first-order axioms over a primitive P, arranges them into a lattice of theories (M, MM, EM, GEM, and their atomistic "A" and atomless "Ā" variants), and for each principle states both what it entails and the philosophical cases against it. The current revision adds material the 2003 edition lacked or got wrong: the correction that Supplementation + Unrestricted Sum3 is not GEM (fixed in 2009, note 29), the weakenings of Supplementation built for non-antisymmetric theories ((P.4c), (P.4d), with Gilmore 2025 and Loss 2021b/2022a), Tsai's (2018) finite first-order axiomatization of GEM, decidability results, the "genuine parthood" treatment of a null item, superatomism, hypergunk, and fuzzy-parthood axioms.

## Key insight

"Part" does not come with its axioms attached. The entry asks where the line falls between principles that fix the meaning of "part" and principles that are substantive metaphysics, and its answer is that no principle is safely on the meaning side: Reflexivity, Transitivity and Antisymmetry each have serious dissenters, and every addition beyond them is contested. The additions interact in ways that are easy to miss. Supplementation plus Reflexivity and Transitivity already entails Antisymmetry. Supplementation plus the harmless-looking existence of products for overlappers already entails Strong Supplementation and so extensionality. How a "sum" is defined changes which theory an unrestricted-composition axiom produces. Classical mereology (GEM) is a tight, robust and decidable theory, but it is one position among several, not a neutral default.

## Assumptions

The entry is a survey, so these are the conventions its formal results are stated under, taken from §2.2 and notes 8–10.

- **Language and logic.** Standard first-order language with identity, a single primitive binary predicate P ("is part of"), and classical predicate calculus. Definite descriptions are treated à la Russell 1905. Note 9 concedes that free logic or plural quantification would arguably suit sums better. Both P and = are kept as primitives because the definability of = via EQ depends on the contested Antisymmetry.
- **Formulas are universally closed.** Initial universal quantifiers are dropped throughout.
- **Proper parthood** is officially (20) PPxy =df Pxy ∧ ¬x=y. It is not the "strict" (20′) Pxy ∧ ¬Pyx used in earlier editions (up to Winter 2012, note 13). The two are equivalent in M and diverge without (P.3).
- **Schemas stand in for sets.** Infinitary principles are axiom schemas over open formulas φ (after Goodman 1951), so they cover only denumerably many specifiable sets. The entry calls this limitation "negligible" for most purposes (§4.3).
- **Scope of "part".** The general relation illustrated by examples (1)–(8): attached or detached, salient or arbitrary, connected or scattered, material or immaterial, spatial or temporal parts. Constitution (9), mixture (10) and group membership (11) are explicitly left out as of "controversial" mereological status. Time- and world-relativized parthood is set aside except in §3.2.
- **Excluded senses (note 1).** The General Systems Theory sense of "mereology" (system decomposition, Mesarović et al. 1970) and the ecological sense (Hutchinson 1978) "are not covered in this entry". Quantum part–whole formalisms are also not covered (note 18).

## Key results

These are the principles and theories the entry lays out, with the axiom forms as the entry states them. P = part, PP = proper part, O = overlap, D = disjoint, A = atom.

- **Definitions (§2.2).** (19) EQxy =df Pxy ∧ Pyx; (20) PPxy =df Pxy ∧ ¬x=y; (21) PExy =df Pyx ∧ ¬x=y; (22) Oxy =df ∃z(Pzx ∧ Pzy); (23) Uxy =df ∃z(Pxz ∧ Pyz); (25) Dxy =df ¬Oxy; (32) Ax =df ¬∃yPPyx.
- **R1: Core (Ground) Mereology M (§2.2).** (P.1) Pxx; (P.2) (Pxy ∧ Pyz) → Pxz; (P.3) (Pxy ∧ Pyx) → x=y. The entry names it "Core Mereology", not "Ground". In M, EQ is an equivalence relation, PP and PE are strict partial orders, and (24) Pxy ↔ (PPxy ∨ x=y), so PP or PE could serve as the primitive instead (Leśniewski used PP, Whitehead PE). O and D cannot define P in M. They can once (P.5) is added, via (31). (26) x=y ↔ EQxy, so (P.3) can be replaced by (P.3′) EQxy → (φx ↔ φy).
- **R2: Supplementation and Minimal Mereology MM (§3.1).** The candidate principles are (P.4a) Company PPxy → ∃z(PPzy ∧ ¬z=x); (P.4b) Strong Company PPxy → ∃z(PPzy ∧ ¬Pzx); and (P.4) Supplementation PPxy → ∃z(Pzy ∧ ¬Ozx). (P.4) implies both (P.4a) and (P.4b), and only (P.4) rules out all three unsupplemented patterns in Fig. 2. MM = M + (P.4). Given (P.1) and (P.2), (P.4) entails (P.3), so (P.3) is redundant in MM. Weaker variants meant for theories without (P.3) are (P.4c) Strict Supplementation (Pxy ∧ ¬Pyx) → ∃z(Pzy ∧ ¬Ozx) and (P.4d) Quasi-supplementation PPxy → ∃z∃w(Pzy ∧ Pwy ∧ ¬Ozw); the two are incomparable (Fig. 3). (P.4′) Proper Supplementation, PPxy → ∃z(PPzy ∧ ¬Ozx), is stronger than (P.4) but collapses to it under Reflexivity. Note 16 adds Super-Strong Company (Full Company), Loss's "Minimal Supplementation", and "Mild Supplementation" (stronger than (P.4), weaker than (P.5)).
- **R3: Strong Supplementation and Extensional Mereology EM (§3.2).** (P.5) ¬Pyx → ∃z(Pzy ∧ ¬Ozx). In M, (P.5) entails (P.4) but not conversely (Fig. 4). EM = M + (P.5), where (P.1) becomes derivable from (P.5) and (P.2) while (P.3) is still needed. Theorem (27): (∃zPPzx ∨ ∃zPPzy) → (x=y ↔ ∀z(PPzx ↔ PPzy)). Its halves are (28) necessity and (29) sufficiency. Given Reflexivity, (P.5) entails (30) ∀z(Ozy → Ozx) → Pyx, and with Transitivity (31) Pyx ↔ ∀z(Ozy → Ozx). Given only (P.1), (31) entails (P.5), so in reflexive, transitive mereologies (P.5) is necessary and sufficient for defining P from O or D. Note 19: the name "strong" misleads, because (P.5) does not entail (P.4) without (P.3).
- **R4: Complementation (§3.3).** (P.6) ¬Pyx → ∃z∀w(Pwz ↔ (Pwy ∧ ¬Owx)). It posits a maximal remainder, a relative complement. (P.6) implies (P.5) but not conversely: Fig. 5 is an EM model where (P.6) fails. The entry says (P.6) "is not ... a principle that can be added to M as a mere strengthening of (P.5)", because its extra strength is compositional (scattered aggregates such as the base and bowl of a wine glass).
- **R5: Atomism and gunk (§3.4).** (P.7) Atomicity ∃y(Ay ∧ Pyx); (P.8) Atomlessness ∃yPPyx. The two are mutually incompatible, and each is consistent with every standard theory X, giving AX and ĀX. Every finite model of M is atomistic, so ĀX has only infinite models (the regular open sets of Euclidean space, Tarski 1935). Hodges and Lewis (1968): even in GEM, no purely mereological formula is true in every finite model of AX and in no infinite one. (P.7) permits infinitely descending atomistic models (Fig. 6; the power set of ℕ, Eberle 1970). "Superatomicity", the requirement that every chain bottom out, is not first-order expressible, and in GEM it with infinitely many atoms entails finitism (Uzquiano 2017, Dixon 2020). Atomistic simplifications: (P.5′) ¬Pxy → ∃z(Az ∧ Pzx ∧ ¬Pzy) replaces (P.5)+(P.7) in AEM and yields hyperextensionality (27′) x=y ↔ ∀z(Az → (Pzx ↔ Pzy)). Relativized bases: (P.5φ/ψ) and (P.7φ/ψ). Proper Atomlessness: (P.8′) ∃y(Pyx ∧ ¬Pxy). Atomless Supplementation: (P.4′′) Pxy → ∃z(PPzy ∧ (Ozx → x=y)), which simplifies ĀMM. Hypergunk (Nolan 2004) is of unknown consistency. Mixed views: (P.7φ) φx → ∀y(Pyx → ∃z(Az ∧ Pzy)) and (P.8φ) φx → ∀y(Pyx → ∃zPPzy). Density: (P.9) PPxy → ∃z(PPxz ∧ PPzy).
- **R6: Bottom collapses (§3.4).** (P.10) ∃x∀yPxy. Added to any mereology containing (P.4), or even (P.4d), it yields (36) ∃x∀y x=y, a one-element world. The escape is "genuine" parthood and overlap: (37) GPxy =df Pxy ∧ ¬∀zPxz, (38) GOxy =df ∃z(GPzx ∧ GPzy), and (P.4G) PPxy → ∃z(GPzy ∧ ¬GOzx).
- **R7: Bounds (§4.1).** (P.11ξ) ξxy → ∃z(Pxz ∧ Pyz). Construing ξ is "a version of" van Inwagen's Special Composition Question. With ξ = O the principle is "rather uncontroversial".
- **R8: Three sums (§4.2).** (39₁) S1zxy =df Pxz ∧ Pyz ∧ ∀w((Pxw ∧ Pyw) → Pzw), a minimal upper bound; (39₂) S2zxy =df Pxz ∧ Pyz ∧ ∀w(Pwz → (Owx ∨ Owy)), after Leśniewski, Tarski and Lewis; (39₃) S3zxy =df ∀w(Ozw ↔ (Owx ∨ Owy)), after Leonard–Goodman, Simons and Casati–Varzi. Principle (P.12ξ,i) is ξxy → ∃zSizxy. Among finite models (P.12ξ,1) is equivalent to (P.11ξ). Given Transitivity, S2 → S3, and S3 → S2 needs (P.5). In EM each +i is idempotent, commutative and associative, (41)–(47), with (47) Pxy ↔ x +i y = y.
- **R9: Products force extensionality (§4.2).** (48) Rzxy =df ∀w(Pwz ↔ (Pwx ∧ Pwy)); (P.13ξ) ξxy → ∃zRzxy. If ξ is merely O, then MM + (P.13ξ) derives (P.5) from (P.4) using only Reflexivity and Transitivity (Simons 1987: 30f), so MM + products ⊇ EM. Infinitary versions (§4.3) are (P.14ψ), (P.15ψ,i) with general sums (52₁–₃), and (P.16ψ) with (53). (P.16ψ) follows from (P.15ψ,1) but not from (P.15ψ,2) or (P.15ψ,3) without stronger assumptions (Pontow 2004). The Fig. 4 MM-model is the counterexample.
- **R10: Classical mereology GEM and the three routes to it (§4.4).** Unrestricted Sumi (P.15i): ∃wφw → ∃zSizφw. GEM = EM + every instance of (P.15₃), which is the systems of Leśniewski and Leonard–Goodman, "also known as Classical Mereology". The same theory is MM + (P.15₂), since (P.5) is then derivable. EM or MM + (P.15₁) is strictly weaker (Fig. 8). Hovda (2009) recovers GEM as (P.2)+(P.4)+(P.15₁)+Filtration (P.17), and note 28 says Filtration must be restricted to ∃wφw. Starting from M, the only adequate pairings are Supplementation + Sum2, Strong Supplementation + Sum3, and Complementation + Sum1 (Hovda 2009; Cotnoir and Varzi 2019). **Supplementation + Sum3 is not GEM**: the Fig. 4 model satisfies both (Pietruszczak 2000a; Pontow 2004). That contradicts Simons (1987: 37), Casati and Varzi (1999) and this entry's 2003 edition, corrected in Spring 2009 (note 29). The entry also gives alternative axiomatizations: Tarski's (P.2) + (P.18), unique unrestricted Sum2; (P.15₂) + (P.19) Singular Sum2; Goodman/Eberle's (31) + (P.3) + (P.15₃); and D, +, or × as primitive via (54), (47) and (55).
- **R11: Finite axiomatization and decidability (§4.4).** GEM is finitely axiomatizable in plain first-order logic (Tsai 2018): EM + (P.20) Top ∃x∀yPyx + (P.21) Strong Complementation ¬∀yPyx → ∃z∀w(Pwz ↔ ¬Owx) + (P.22) ∃zS3zxy + (P.23) ∃xAx → ∃zS3zAz. GEM is decidable (Tsai 2013a), whereas M, MM, EM and "several extensions thereof" are undecidable.
- **R12: The algebra of GEM (§4.4).** It has operators (56) σ (general sum), (58) +, (59) ×, (60) −, (61) ~, (62) U =df σzPzz, and (63) π. GEM's parthood is "virtually isomorphic" to inclusion on the non-empty subsets of a set, which is a complete Boolean algebra with zero removed (Tarski 1935, Grzegorczyk 1955). Note 34 gives the precise first-order statement: every model is isomorphic to a Boolean subalgebra, not necessarily complete, of a complete Boolean algebra minus zero (Pontow and Schubert 2006, Thm 34). Adding Bottom with "genuine" operators, (P.5G) and (P.15₃G), yields a full Boolean algebra.
- **R13: Cardinality and junk (§4.4).** AGEM with κ atoms has 2^κ − 1 elements. So there are models of size 1, 3, 7, 15 and 2^ℵ₀, but none of size 2, 4, 6 or ℵ₀, and none of strongly inaccessible size (Simons 1987; Uzquiano 2006, "the price of universality"). Strong Atomicity: (P.7′) x = σy(Ay ∧ Pyx). Every GEM model has a top element U, so GEM is incompatible with Ascent (P.24) ∃yPPxy, i.e. with junk. The retreats are finitary unrestricted sums only, (P.22), or infinitary sums only for bounded collections, (P.15ψ,i) with ψ = shared underlap.
- **R14: Composition, existence and identity (§4.5).** Restricted principles give only sufficient conditions. Made biconditional, they face the sorites (64) over cell separations, i.e. the Special Composition Question. The candidate answers are: brute or contingent composition (Markosian, Nolan, Cameron), a factually empty or verbal question (Balaguer, Hirsch), van Inwagen's organicism, where the φers compose iff their activity constitutes a life (1990: ch. 9), and further criteria (functional unity, physical bonding, causal dispositions, teleology, patterning, physics-informed conditions). Universalism, (P.15i), is defended by Lewis's argument from vagueness (1986b: 213): no restriction can be vague, a precise one cannot fit intuition, so any restriction is arbitrary. Against ontological exuberance, the entry gives Composition as Identity, where a sum is the parts "counted loosely" (the six-pack at the checkout), and the "wrong level" reply. Nihilism: (P.25) Ax, with corollary (65) Pxy ↔ x=y. Manyism is a variant (Thunder 2023).
- **R15: Indeterminacy (§5).** The entry separates de dicto (66a) from de re (66b) indeterminacy. On the de dicto reading, the vagueness lies in "Tibbles" (Lewis, Varzi and others) or in "part" (Donnelly 2014), and the axioms hold unchanged. On the de re reading, option (i) uses truth-value gaps (Kleene, Łukasiewicz, supervaluation over "precisifications of reality"), and option (ii) uses degrees, with π: pairs → [0, 1]. The fuzzified core is (P.1π) π(x,x) = 1, (P.2π) π(x,z) ≥ min(π(x,y), π(y,z)), (P.3π) if π(x,y) = 1 and π(y,x) = 1 then x = y. Variants are (P.2π′) (Polkowski–Skowron), (P.2π′′) (Sadegh-Zadeh) and (P.3π′) (N. Smith). (P.4) has 16 inequivalent fuzzy renderings, of which (P.4π) is one.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | None of Reflexivity, Transitivity or Antisymmetry is safely a mere meaning-postulate for "part". Antisymmetry "can hardly be regarded as constitutive". | informal argument | §2.1: survey of counterexample families (Kearns; Frege's Etna; Thomson; Net of Indra; perichoresis; time travel; structured propositions) with citations; the author's verdict |
| C2 | Most objections to Reflexivity and Transitivity based on ordinary language equivocate between "part" and a restricted "φ-part", and the genuine threats are metaphysical (time travel, multilocation, structured propositions). | informal argument | §2.1, Simons 1987: 107f; predicate-modifier treatment (Varzi 2006a) |
| C3 | Supplementation (P.4) is "a minimal but substantive addition" to M, not part of the meaning of "part". | informal argument | §3.1: Brentano's accidents, Fine's singletons, Whitehead's boundary-free regions, Aquinas's disembodied soul, cases of coincidence by diminution (Tibbles/Tib, Dion/Theon) |
| C4 | Given (P.1) and (P.2), (P.4) entails (P.3). (P.5) entails (P.4) only given (P.3). | proof (sketched in the entry) | §3.1 one-line argument; §3.2; note 19 |
| C5 | Extensionality (27) is a theorem of EM and needs (P.3) as well as (P.5). A non-antisymmetric theory can keep (P.5) without extensionality. | proof (sketched) plus cited model | §3.2; Cotnoir and Bacon 2012 |
| C6 | Objections to the necessity half (28), survival through change, are not specific to mereology: they are the general problem of diachronic identity and are handled by 4D or time-relativized parthood (28′). | informal argument | §3.2, Leibniz schema (ID)/(ID′); Thomson 1983; Sider 2001 |
| C7 | Coincidence counterexamples to the sufficiency half (29) misfire in cases (a) and (b) and are doubtful in case (c). The structured-whole cases remain "more challenging". | informal argument | §3.2 three-case analysis; the entry lists responses but does not settle it |
| C8 | Complementation (P.6) is strictly stronger than (P.5), and its extra strength is compositional. | cited model plus argument | Fig. 5; wine-glass example (§3.3) |
| C9 | No first-order formula separates finitely from infinitely many atoms, even in GEM. | cited theorem | Hodges and Lewis 1968 (§3.4) |
| C10 | Bottom (P.10) plus (P.4), or even (P.4d), collapses the domain to one element. | proof (sketched) | §3.4 derivation to (36) |
| C11 | MM plus products for overlappers (P.13, ξ = O) already contains EM. | cited proof | Simons 1987: 30f (§4.2) |
| C12 | Supplementation + Unrestricted Sum3 does not yield GEM, contrary to Simons 1987 and the entry's own first edition. | cited countermodel | Fig. 4; Pietruszczak 2000a §7.3, Pontow 2004 §5.2; Hovda 2009 on exhaustiveness (§4.4, note 29) |
| C13 | GEM is finitely axiomatizable in first-order logic and decidable. M, MM and EM are undecidable. | cited theorems | Tsai 2018, 2013a; Tsai 2009–2013b (§4.4) |
| C14 | GEM's models are (sub)algebras of complete Boolean algebras minus zero. AGEM models have 2^κ − 1 elements. | cited theorems | Tarski 1935, Grzegorczyk 1955, Pontow and Schubert 2006 Thm 34 (note 34); Simons 1987: 17 |
| C15 | "All composition principles turn out to be controversial": restricted ones do too little, unrestricted ones too much. | informal argument | §4.5 opening. The entry had earlier called (P.11ξ) with ξ = O "rather uncontroversial" (§4.1), so the headline is slightly stronger than its own treatment of bounds |
| C16 | The Special Composition Question has no agreed answer, and whether the answer may differ across kinds "remains a matter of debate". | survey assertion | §4.5 literature map |
| C17 | Composition as Identity would defuse the exuberance charge but is contested: it entails mereological essentialism given the necessity of identity, its coherence is questioned, and it may preclude strong emergence. | survey assertion with citations | §4.5; Merricks 1999; van Inwagen 1994; McDaniel 2008 (note 43) |
| C18 | On de dicto accounts of vague parthood the mereological axioms need no revision. On degree accounts, fuzzifying M is easy and everything beyond M is hard. The standard objection is spurious precision. | informal argument plus cited formal work | §5; Polkowski–Skowron 1994; N. Smith 2005; Sanford 1976, Tye 1994 |

## Concepts

- **Core Mereology (M)**: (P.1)–(P.3). The prompt's "Ground Mereology" is the older name; this entry uses "Core". MM = Minimal (M + P.4), EM = Extensional (M + P.5), GEM = General Extensional = Classical. A and Ā prefixes mark atomistic and atomless versions.
- **Supplementation vs. Strong Supplementation**: a proper part leaves a disjoint remainder (P.4); anything that is not a part leaves one (P.5). Note 14 says (P.4) is often called "Weak Supplementation".
- **Complementation / Remainder (P.6)**: the existence of a maximal remainder.
- **Sum / fusion**: three non-equivalent definitions (S1 minimal upper bound; S2 Leśniewskian; S3 Leonard–Goodman overlap-based) that coincide in GEM. Note 23: some authors reserve "sum" for S2 and "fusion" for S3.
- **Gunk / hypergunk / junk**: atomless everything (P.8); gunk with no cardinality bound (Nolan); endless upward composition (P.24). Junk is also called "knug" and "coatomlessness" (notes 37–38).
- **Special Composition Question**: under what conditions do some things compose something (van Inwagen 1987, 1990). It contrasts with the General Composition Question, "what is composition?" (note 39).
- **Universalism / nihilism / organicism**: every plurality composes (P.15i) / nothing composes (P.25) / things compose iff their activity constitutes a life.
- **Composition as Identity**: a sum is its parts "counted loosely", "the same portion of Reality" (Lewis 1991: 81).
- **φ-part**: a restricted parthood (functional, direct, component) that need not be transitive even when P is.
- **De dicto / de re indeterminacy**: vagueness in our terms versus vagueness in the objects.

## Connections

The entry builds on Leśniewski (1916, 1927–31), Leonard and Goodman (1940), Goodman (1951), Tarski (1929, 1935, 1937), Simons, *Parts* (1987), and Casati and Varzi (1999). Its systematic backbone is Cotnoir and Varzi, *Mereology* (OUP 2021), which is cited throughout for proofs and history. The formal corrections come from Pietruszczak (2000a), Pontow (2004), Hovda (2009) and Tsai (2013a, 2018).

Within this record:

- The entry's §2.1 case for non-wellfounded mereology, where Antisymmetry fails through mutual parthood, parallels the symmetric ontological dependence defended in [LIT-173](../literature.d/LIT-173.md) (Morganti's metaphysical coherentism). [LIT-173](../literature.d/LIT-173.md) is about dependence, not parthood, and is not tagged `mereology`, so this is a family resemblance, not an application.
- [LIT-113](../literature.d/LIT-113.md) (duality and ontology) says dual theories disagree about "mereology". The entry supplies the vocabulary for stating such a disagreement: atomism vs. gunk, extensional vs. not, universalism vs. nihilism.

## Bearing on the record

Carries nothing for ML practice. Nothing here belongs in the Anthology of the SOTA, and no ANTH- document is affected. No THEORY document in nucleation cites mereology (grep of `record/theory.d` for "mereolog" found nothing), so the entry neither supports nor contradicts one yet.

It is the reference text for the `mereology` topic. That topic's blurb is "parts and wholes — composition, individuation of systems and collectives", which is broader than the entry's scope in one important way: the entry explicitly excludes the systems-theory sense of "mereology" (note 1) and quantum part–whole formalisms (note 18). How it bears on each held work tagged `mereology`:

- **[LIT-142](../literature.d/LIT-142.md) (Meincke, pregnancy).** This is the most direct use. Kingma's Parthood View (the foetus is part of the gestating organism) is a straight claim about P, and Meincke's "neither one nor two" connects to §4.5 (counting, and Composition as Identity's "counted loosely") and §5 (Evans on whether indeterminate parthood makes identity indeterminate). The entry flags that its own formal treatment assumes determinate, tenseless parthood. Meincke's process ontology challenges exactly that, so the entry is background, not an arbiter.
- **[LIT-138](../literature.d/LIT-138.md) (Register, *The Depth of the Body*).** Relevant through §1 (parts may be abstract; ordinary "part" is ambiguous) and §2.1 (Frege's Etna argument and φ-part non-transitivity). The claim that BCI software can be a body part while the server implementing it is not has the form of a transitivity or cross-level question. It also touches §4.5's "cross-categorial sums" (Simons's "ontological chimeras").
- **[LIT-005](../literature.d/LIT-005.md) and [LIT-049](../literature.d/LIT-049.md) (Bourrat on individuality).** These answer a biological, restricted cousin of the Special Composition Question: which partitions of particles into collectives are individuals. The entry lists the organicist and "more stringent biological criteria" answers (van Inwagen; Merricks; Olson; functional unity) as SCQ answers about existence. Bourrat's criteria are about which collectives count as individuals of a kind, which in the entry's terms is a restricted φ-part / components notion, not P. Citing the entry for Bourrat should keep that distinction.
- **[LIT-157](../literature.d/LIT-157.md) (Bourrat, reproducees) and [LIT-188](../literature.d/LIT-188.md) (Griesemer et al., collections / conexuses / communities).** Same bearing as Bourrat: SCQ-style criteria for biological wholes. [LIT-157](../literature.d/LIT-157.md)'s "material overlap" is the entry's O.
- **[LIT-168](../literature.d/LIT-168.md) (Wilson and Barker, Biological Individuals) and [LIT-167](../literature.d/LIT-167.md) (Baedke, The Organism).** Background for the parts-of-organisms and groups-of-organisms questions. The entry's §1 notes that whether groups are mereological wholes is contested (example (11)). Its §2.1 cites Rescher's (1955) biological objection to Reflexivity, "no organism is a functional subunit of itself".
- **[LIT-159](../literature.d/LIT-159.md) (Schwitzgebel, the United States is conscious).** It rests on a group entity being a genuine whole. The entry's §1 treats group membership as of disputed mereological status, and its §4.5 bears on whether the scattered sum exists at all: universalism yes, restricted composition maybe not.
- **[LIT-097](../literature.d/LIT-097.md) (Clark and Chalmers, Extended Mind).** This uses "part of the cognitive process", a functional φ-part in the entry's sense. The entry bears only on keeping that distinct from P.
- **[LIT-123](../literature.d/LIT-123.md) (Carroll).** "Quantum mereology", the factorization of Hilbert space into subsystems, is outside the entry by its own note 18. The entry supplies the classical background (extensionality vs. Maudlin; Albert's lonely atom), not the framework. The skim's "natural companion" overstated this.
- **[LIT-025](../literature.d/LIT-025.md) and [LIT-027](../literature.d/LIT-027.md) (ΦID causal emergence).** Tagged `mereology` in the systems sense, which is the sense note 1 excludes. The entry's only point of contact is §3.2 on structured wholes ("more than the sum of its parts") and note 43 on Composition as Identity versus strong emergence (McDaniel 2008). Those tags are justified by the topic blurb, not by this entry.

Recommended correction for [LIT-124](../literature.d/LIT-124.md) and its note summary: drop "uncontroversial core"; see the first item under corrections.

## Limitations

- By design it covers formal mereology in one tradition, "mostly" Leśniewski / Leonard–Goodman descendants. Mereotopology, location, medieval mereology and non-wellfounded theories are pointed to or handled briefly. Time- and modality-relative parthood are "barred for the moment" apart from §3.2.
- It is a survey. Almost every formal result is stated with a citation and at most a one-line derivation. Correctness rests on the cited sources (Cotnoir and Varzi 2021; Pontow 2004; Hovda 2009; Tsai 2013a/2018), which I did not check.
- It is not neutral in every respect. Varzi is a known extensionalist and universalism-sympathetic author (Varzi 2000, 2006b, 2008, 2009 are cited as the replies). The sections on extensionality (§3.2) and ontological innocence (§4.5) give the extensionalist responses the last word, though the objections are reported fairly.
- The standing claim C15 ("all composition principles turn out to be controversial") is stronger than its own §4.1 verdict on overlap-bounded (P.11ξ).
- Figures 1–9 were read only through captions and surrounding text.
- There are small textual slips. §5 says "claims of the form (64)" where (66) is meant. There are typos: "Nolan 2005 2005", "too week", "concide", "Inwagen 2002a".

## Open questions

These are stated as open by the entry.

- Whether any weakening of Supplementation both blocks Fig. 2's unsupplemented models and suits theories that drop an M axiom (Gilmore 2025). The entry says this is "gaining increasing attention".
- Whether atomless analogues of hyperextensionality (27′) exist: a general "base" predicate for arbitrary domains.
- Mixed atomic and gunky worlds, (P.7φ)/(P.8φ): "no thorough formal investigation has been pursued".
- Whether hypergunk is consistent (Nolan's conjecture, inaccessible cardinals), and whether it is metaphysically possible.
- Whether junk is possible, and so whether GEM's Top is a defect.
- Whether Supplementation + Unrestricted Sum3 is a stable home for the anti-extensionalist (Varzi 2009 and the replies to it).
- The Special Composition Question, and whether its answer varies by kind.
- The coherence of Composition as Identity.
- Whether fuzzy mereology captures indeterminacy at all, given the objection of "the most refined and incredible precision".

For the record, the useful open question is whether the held biology-of-individuality works ([LIT-005](../literature.d/LIT-005.md), [LIT-049](../literature.d/LIT-049.md), [LIT-157](../literature.d/LIT-157.md), [LIT-188](../literature.d/LIT-188.md), [LIT-142](../literature.d/LIT-142.md)) are answering the SCQ about P or a restricted φ-part question. A THEORY document on biological individuation would need to decide that.

## Corrections to the seeded skim

- The skim's headline, carried into [LIT-124](../literature.d/LIT-124.md)'s summary and NOTE-163's front matter, says the core "that parthood is a partial order" is "uncontroversial" and that only the further principles are contested. The entry says the opposite. §2.1 gives objections to each of (16)–(18): Kearns's time-travel and fractal cases against Reflexivity; functional or "φ-part" readings, multilocation, and Frege's Etna argument against Transitivity; and Thomson's statue/clay, the Net of Indra, perichoresis, time-travel walls and structured propositions against Antisymmetry. It concludes that Antisymmetry "can hardly be regarded as constitutive of the basic meaning of 'part'". It ends §2.1 with Donnelly's (2011: 246) doubt that "any useful core mereology" is common to all plausible theories. The entry calls M "the common starting point of all standard theories" (§2.2), which is a claim about what is standard, not that M is uncontroversial. The summary should read "even the partial-order core is contested; everything beyond it more so".
- The skim puts "junk" in §3.4 ("atomism vs gunk (no atoms) vs junk"). §3.4 covers atomism, gunk, hypergunk, mixed views, Density and Bottom. Junk, meaning endless upward composition expressed by Ascent (P.24) ∃yPPxy, is in §4.4, as the upward dual of gunk and as a limitation of GEM, since the existence of the universe U is a GEM theorem.
- The skim says strong supplementation "yields extensionality, contested by cases like statue/clay". Two points are missing. First, the extensionality theorem (27) follows from (P.5) only together with Antisymmetry (P.3), so the non-wellfounded mereology of Cotnoir and Bacon (2012) has (P.5) and is not extensional. Second, the entry argues that coincidence counterexamples to the sufficiency half (29) mostly misfire: if statue and clay are mutual parts, (P.3) fails; if one is part of the other, PP-irreflexivity fails; and if neither is, their proper parts plausibly differ too (the statue's nose versus its matter). §3.2 leaves the structured-whole cases (bouquet, watch, molecule, cat) "more challenging" and open.
- The skim introduces the Special Composition Question in §4.1. The question is only named there, as a version of how to construe ξ in (P.11ξ). Its substance is in §4.5: the soritical schema (64), the brute-composition, contingency and verbal-dispute answers, the organicist and other restricted answers, Lewis's argument from vagueness for universalism, and nihilism (P.25).
- NOTE-163's open questions call the entry "a natural companion to quantum mereology (Carroll, [LIT-123](../literature.d/LIT-123.md))". Note 18 says the entry does not cover quantum part–whole formalisms ("We do not cover these developments here"). Its only quantum material is the Maudlin (1998) versus Calosi et al. (2011) exchange on extensionality, and Albert's (1996) "lonely atom" in configuration space. It is background for [LIT-123](../literature.d/LIT-123.md), not a companion to it.
- The skim treats "several non-equivalent definitions of 'sum'" as a curiosity. They are the entry's main technical correction to the literature: which definition you pick decides which decomposition axiom you need to reach GEM (see Key results R10).
