---
status: Read
paper: LIT-tmp31ier
title: 'DeVille and Lerman 2013 — Modular dynamical systems on networks'
version: 1
history:
- version: 1
  date: '2026-11-19'
  note: >-
    URL read: https://arxiv.org/pdf/1303.3907 (HTTP 200, 453 KB PDF, v1 of
    15 Mar 2013, 37 pages), fetched 2026-11-19. Kind of copy (step 5): arXiv
    preprint, the authors' own upload. No obstacle. Text extracted with
    pdftotext -layout to dl/text.txt. Diagrams (xypic) extract poorly; read
    from structure. Read: abstract; §1 in full (overview, background,
    contributions, motivating example, main ideas); §2.1 (graphs, networks,
    maps of networks); §4 in full (fibrations, Lemma 4.1.5, Proposition
    4.2.1, Theorem 4.3.1 with proof, Remark 4.3.3); §5 in full (surjective,
    injective and general fibrations); §6.2 statements (Theorem 6.2.3,
    Corollary 6.2.4). Skipped: §2.2-2.4 (open systems, interconnection,
    dependency) and §3 (symmetry groupoid, groupoid-invariant vector fields)
    beyond what the theorems' statements need; §6.1 and the proofs in §6.
date: '2026-11-19'
---

# NOTE-tmpubt2l: DeVille and Lerman 2013 — Modular dynamical systems on networks

## Contribution

DeVille and Lerman (arXiv 1303.3907, 2013) treat a network as a directed multigraph whose nodes carry phase spaces (manifolds). A dynamical system on it is built from control systems, one per node, that depend only on the node's inputs ("dependency"). Nodes with isomorphic input networks must use the same control system ("modularity", groupoid invariance). Their main theorem is that a graph fibration, in Boldi and Vigna's sense of a unique lift of each incoming edge, induces a map of dynamical systems going the opposite way. A surjective fibration gives an embedding of the quotient's dynamics as an invariant polydiagonal. An injective fibration gives a projection of a large system onto a driving subsystem. The setting is coordinate-free, on manifolds, generalizing one direction of Golubitsky and Stewart's balanced-relation results.

## Key results

- **Definition of fibration** (Definition 4.1.1, p. 22): "A map ϕ : G → G′ of directed graphs is a fibration if for any vertex a of G and any edge e′ of G′ ending at ϕ(a) there is a unique edge e of G ending at a with ϕ(e) = e′ ."
- **Fibrations preserve input trees** (Lemma 4.1.5, p. 22): the induced maps of input trees "are isomorphisms for all nodes a of G."
- **Main theorem** (Theorem 4.3.1, p. 24): for a fibration of networks, for any groupoid-invariant virtual vector field w′ on the target, the phase-space map Pϕ "intertwines the vector fields I ′ (w′ ) and I (ϕ∗ w′ )". The paper calls this "arguably the main result of the paper" (p. 24).
- **Surjective fibrations give synchrony subspaces** (Lemma 5.1.1, p. 26): Pϕ "is an embedding whose image is a “polydiagonal”" ∆ϕ = {x ∈ PG | xa = xb whenever ϕ(a) = ϕ(b)}. Abstract: "surjective graph fibrations lead to synchrony subspaces in networks."
- **Balanced quotients are surjective fibrations** (§1.3 item 3, p. 4): "the quotient maps of graphs by balanced equivalence relations of [61] are special cases of graph fibrations — they are the surjective graph fibrations."
- **Only one direction** (Remark 4.3.3, pp. 25–26): Theorem 4.3.1 generalizes "Theorem 5.2 (direction (b)) of [61] and of Theorem 9.2 of [57]. We do not attempt to establish the converse."
- **Injective fibrations give driven systems** (§5.2, pp. 27–28): "the notion of an injective fibration makes precise the intuitive idea of a subsystem driving a larger network." The map is a surjective submersion (Lemma 5.2.1). The abstract calls such surjections "“abstractions” in the computer science sense of the word."
- **Pull-back of invariant fields is onto** (Theorem 6.2.3 and Corollary 6.2.4, p. 31): ϕ∗ : V(G′, P′) → V(G, P) "is surjective"; and "In particular ϕ∗ is an isomorphism if ϕ is surjective."
- **Motivating example without symmetry** (§1.4, p. 5): a three-node graph with invariant subspaces ∆ and ∆′ where "The graph has no non-trivial symmetries."

## Assumptions

- Continuous-time vector fields on finite-dimensional manifolds. Graphs are finite directed multigraphs with loops allowed.
- Modularity: nodes with isomorphic input networks (height-one input trees with their phase spaces) share one control system. This is the paper's groupoid invariance (§3), which plays the role of Golubitsky and Stewart's admissibility.
- Maps of networks must preserve phase spaces (P′ ∘ ϕ = P).

## Concepts

- **Graph fibration** (Boldi–Vigna): unique lifting of incoming edges; equivalently, an input-tree isomorphism at every node (Lemma 4.1.5).
- **Surjective fibration ↔ quotient**: the quotient of a graph by a balanced relation. Its dynamics embed as a polydiagonal.
- **Injective fibration ↔ driving subsystem**: no edges from outside the image into it. Its dynamics are a projection of the whole.
- **Maps of dynamical systems**: maps h with dh ∘ X = Y ∘ h. They need not be invertible (semiconjugacies, embeddings).
- **Virtual vector field / control system**: a node's vector field as a function of its inputs, before interconnection.

## Bearing on the record

- **THEORY-1065** — supports, for one direction, and generalizes it. Balanced relations give surjective graph fibrations, and these give invariant polydiagonals for every modular (groupoid-invariant) vector field, on manifolds rather than Euclidean spaces. The paper does not prove the converse (unbalanced implies not invariant), which is the half of THEORY-1065 that needs Stewart, Golubitsky and Pivato's construction. It confirms the record's note that "graph fibration" is this theorem's structure under Boldi and Vigna's name.
- **THEORY-1059** — supports, with a contrast the record should note. The quotient's dynamics embed in the original's (Lemma 5.1.1, Theorem 4.3.1). The maps go from quotient to original ("Rather than restricting from polydiagonals we extend from polydiagonals", p. 4). Corollary 6.2.4 states that for a surjective fibration the pull-back of invariant fields is an isomorphism: in this class every modular field on the quotient comes from one on the original, and conversely. THEORY-1059, from Stewart, Golubitsky and Pivato, says instead that the quotient admits more dynamics than restriction produces (Remark 7.5). The two classes differ: this paper's modularity ties a node's equation to its input network, while the 2003 paper's admissibility uses arrow types. The paper does not compare them on this point, so the difference is left open (reader's observation).
- **QUESTION-tmpex36a** — leaves open. The paper supplies the commuting-map form A21 used for the bridge (h ∘ ϕt = ψt ∘ h, eqs. 1.1.1–1.1.2). Its injective-fibration "abstraction" is a precise sense in which a subsystem drives, and can stand for, a larger network. It says nothing about learning or inputs.
- **CLAIM-tmpj540o** — supports its step 2 in spirit. Robust synchrony comes from fibrations, of which symmetry orbits are a special case, without needing a permutation action. The example of §1.4 has no nontrivial symmetry.

## Limitations

- Existence only, no stability. Like the 2003 paper, nothing here says the polydiagonal attracts.
- One direction only: fibrations give maps of dynamical systems, and no converse is attempted (Remark 4.3.3).
- Continuous-time smooth systems on manifolds. Discrete-time and stochastic versions are announced as future work (p. 3), so feed-forward neural networks are not directly covered.
- Unweighted multigraphs. Weights would have to be encoded as edge types or phase-space labels, which the paper does not do.
