---
number: 16
status: Skimmed
formerly:
- NOTE-tmpgv359
paper: LIT-016
title: 'The sheaf-theoretic structure of non-locality and contextuality'
version: 1
date: '2026-09-25'
summary: >-
  Contextuality, with non-locality as a special case, is exactly the non-existence of a global section of a presheaf of distributions over a measurement cover, which gives a Hilbert-space-free, linear-algebraic and hierarchical treatment of Bell, Hardy and GHZ-type arguments.
---

<!-- inactive-ok-file: LIT-016 — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-25 -->

# NOTE-016: The sheaf-theoretic structure of non-locality and contextuality

## Contribution

The paper uses sheaf theory to treat non-locality and contextuality in one framework that generalizes Bell-type probability tables to arbitrary measurement covers, including Kochen-Specker configurations. Contextuality corresponds exactly to obstructions to global sections, and a linear-algebraic method computes these obstructions. It establishes a strict hierarchy of no-go strength with Bell < Hardy < GHZ, and shows that local hidden-variable models with negative probabilities exist exactly for no-signalling models. It characterizes maximal/strong contextuality qualitatively, as no global section in the support, gives a combinatorial generalization of Kochen-Specker parity proofs, and strengthens no-signalling to arbitrary families of commuting observables in quantum mechanics.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- The setting (measurements, events, distributions, measurement covers, empirical models) is independent of Hilbert space, so results hold for any theory with the structural properties (§1, §2).
- Global sections ↔ solutions of a linear system defined by an incidence matrix; solving over the reals (allowing negative weights) is how the negative-probability/no-signalling correspondence arises (§4, §5).
- Strong contextuality is defined via supports, identified with maximal non-locality; Kochen-Specker graphs give generic, model-independent strong contextuality (§6-7).
- Bell-type scenarios admit no Kochen-Specker-type (generic) theorem, since their covers are not combinatorially rich enough (§9.3).
- The Postlude presents sheaves and presheaves over contexts as a general "logic of contextuality" connected to semantics of computation, and points to later Čech-cohomology obstructions (Abramsky, Mansfield, Soares Barbosa) (§10).

## Open questions

- Foundational for the "contextuality as local consistency without global consistency" view that later work (cohomology of contextuality, the contextual fraction) builds on. Check the precise statement of the negative-probability ↔ no-signalling theorem (§5.4) and the hierarchy proofs.
- Note that its notion of contextuality (Kochen-Specker / sheaf) is different from Spekkens' generalized noncontextuality in items 14, 17 and 71. A deeper read should keep the two apart.
- ML link (real but indirect): item 69 cites this paper, and sheaf-theoretic "local-to-global" consistency underlies sheaf neural networks and related data-fusion work. The link is conceptual; this paper contains no ML.
