---
number: 237
status: Skimmed
formerly:
- NOTE-tmpkjjf0
paper: LIT-263
title: 'Budroni et al., Kochen–Specker contextuality (RMP review)'
version: 1
date: '2026-09-27'
summary: >-
  A review that fixes a minimal definition of Kochen–Specker contextuality as the impossibility of a global joint distribution whose marginals are the context distributions (Fine's theorem; the sheaf-theoretic framework is one of several equivalent formulations), and that treats Spekkens's generalized contextuality as a different notion, covered only to mark the difference.
---
<!-- inactive-ok-file: LIT-263 — Deferred: filed and skimmed on 2026-09-27 while bringing the contextuality threads together; the theories citing it are Proposed until it is read closely -->

# NOTE-237: Budroni et al., Kochen–Specker contextuality (RMP review)

## Contribution

The Kochen–Specker theorem says quantum mechanics conflicts with classical models in which a measurement's result does not depend on which compatible measurements are performed with it. The review introduces this "quantum contextuality" and its current state: proofs of the theorem, different notions of contextuality, how to test them experimentally and what loopholes arise, links to nonlocality and graph theory, and applications in quantum information processing.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- §I (p. 2): the review focuses on Kochen–Specker contextuality; "a different notion of nonclassicality proposed in Spekkens (2005) is only briefly covered to highlight the differences".
- §IV.A.1 (Eqs. 14–16): NCHV models defined by the marginal problem; local consistency of the marginals "is sometimes called the sheaf condition (Abramsky and Brandenburger, 2011)", equal to no-signalling in Bell scenarios and "nondisturbance" in general; existence of an NCHV model ⇔ a global distribution (Fine's theorem), several formulations (marginal problem, polytope, sheaf, graph, hypergraph) said to be substantially equivalent.
- §IV.A.4: logical (possibilistic) and strong contextuality and the noncontextual fraction are attributed to Abramsky & Brandenburger 2011 ([LIT-016](../literature.d/LIT-016.md)), with "strongly contextual ⇔ maximally contextual".
- §IV.C.5 (Eqs. 54–55): Kujala, Dzhafarov & Larsson 2015's maximally noncontextual models for n-cycle scenarios allow context-dependent marginals; the KCBS data of Lapkiewicz et al. still violate the modified inequality.
- §IV.E.1–4: Spekkens's definitions for prepare-and-measure scenarios (Eqs. 64–66), the qubit preparation-contextuality proof (Eqs. 67–70), the Mazurek et al. 2016 inequality (Eq. 73, bound 5/6, observed 0.99709 ± 0.00007); §IV.E.4 notes that Bell's and Kochen–Specker's own qubit hidden-variable models are preparation contextual (citing Leifer & Maroney 2013), and that the definition rests on a methodological Leibniz principle.
- §V.B.2: Vorob'ev's theorem — a marginal scenario with an acyclic hypergraph always admits a joint distribution, so contextuality needs a cycle of length > 3 in the compatibility graph.

## Open questions

- It places the sheaf-theoretic formulation ([LIT-016](../literature.d/LIT-016.md)) inside the standard KS literature and names the relation to Spekkens contextuality without deriving it; for the derivation the primary source is Spekkens 2005 (cx1).
- §IV.C (imperfect compatibility) is where KS contextuality meets data with context-dependent marginals; it is the physics-side counterpart of contextuality-by-default (cx4).
- A deeper reading should check §V.C (KS vs Bell) and §VI.A (contextuality and magic states), which bear on [LIT-007](../literature.d/LIT-007.md)'s stabilizer results.
