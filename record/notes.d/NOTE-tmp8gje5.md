---
status: Read
paper: 'LIT-tmpd40td'
title: 'Balduzzi et al. — Open-ended learning in symmetric zero-sum games'
version: 1
history:
- version: 1
  date: '2026-10-24'
  note: >-
    Read in full on 2026-10-24 from arXiv:1901.08106v2 (13 May 2019), the
    authors' "ICML 2019, final version", an 18-page PDF under arXiv's
    non-exclusive distribution licence, extracted by pdftotext. Read:
    sections 1–6 (pp. 1–8) and appendices A–H (pp. 10–18), with every
    proof followed. The reference list was skimmed. The inner product of
    Theorem 1 was checked against main.tex in the v2 source, which matches
    the PDF. Page numbers below are the PDF's. Every quotation was checked
    against the extracted text by script, and Example 3's rank formula was
    checked by script for cycles of length 3 to 10.
date: '2026-10-24'
summary: >-
  A framework paper with an algorithm and two small experiments. Symmetric
  zero-sum games between parametrized agents split into transitive and
  cyclic parts relative to a measure on agents. In a cyclic game an
  individual's performance is meaningless, so evaluation moves to
  populations: the value of the game between them, which is invariant to
  redundant members, and the convex hull of their evaluation rows. Training
  each supported agent on what it beats grows that hull.
---
<!-- inactive-ok-file: THEORY-tmpxh6cj — Proposed; filed from this reading, named -->
<!-- inactive-ok-file: CLAIM-tmpuxcp6 CLAIM-tmp0qupq CLAIM-436 CLAIM-440 — Proposed; the accounts this reading bears on, named in prose, nothing here rests on them -->

# NOTE-tmp8gje5: Balduzzi et al. — Open-ended learning in symmetric zero-sum games

## What the paper does

**Setting.** A functional-form game: a set W of agents (say, network
weights) and an antisymmetric φ(v, w), positive when v wins (p. 2). φ can
be P(v ≻ w) − ½ or the log-odds. The agent's parametrization is folded
into φ.

**Decomposition (Theorem 1, p. 3; proof pp. 11–12).** With a probability measure
on W, div φ(v) = ∫φ(v, w)dw is v's mean payoff against agents drawn from
that measure. Then φ = grad(div φ) + ψ with div ψ = 0. The first part is
transitive, φ(v, w) = f(v) − f(w); the second is cyclic, wins against some
agents balanced by losses to others. The decomposition is a direct sum,
since div grad f = f. The paper states it as orthogonal "with respect to
the inner product on games", defined as ⟨φ, ψ⟩ := ∫φ(v, w)ψ(v′, w′)dv dw
dv′ dw′, which is also how v2's TeX source has it. With v, w, v′, w′ independent,
that form is (∫φ)(∫ψ), and it is zero for every pair of antisymmetric
functions. So the orthogonality proved is vacuous. The proof shown never
uses div ψ = 0. With the ordinary product ∫φψ dv dw, the claim is true:
⟨grad f, ψ⟩ = 2∫f·div ψ = 0. The reader re-derived that. The theorem
stands with a corrected inner product.

Two consequences the paper does not stress:
- **The split depends on the measure.** Change which agents count as the
  reference population and f, the transitive strength, changes.
- **Monotonic is not transitive.** A monotonic game, φ = σ(f(v) − f(w)),
  orders the agents completely and has no cycles, but it is not a gradient
  and has a cyclic part. The paper keeps the two apart and builds its
  results for both.

**Transitive and cyclic examples.** Self-play, training against the latest
agent, suits transitive and monotonic games and fails in cyclic ones. The
disc game, φ(v, w) = v₁w₂ − v₂w₁ on a disc, is cyclic and embeds
rock-paper-scissors at every radius (pp. 3–4).

**Gamescapes (pp. 4–5).** The empirical gamescape of a population P is the
convex hull of the rows of its evaluation matrix A_P.
- Proposition 2: adding agents that are behaviourally mixtures of members
  leaves it unchanged, up to an isometric embedding.
- Proposition 3: its dimension is the rank of A_P.
- Example 3: a cycle of n agents has rank n − 2 for even n and n − 1 for
  odd n. The reader checked this for n = 3 to 10.
- "it is always possible that an agent that appears to be dominated is
  actually part of a partially observed cycle" (p. 5). And: "Without
  further assumptions about the structure of φ, it is impossible to draw
  strong conclusions about the nature of the FGS from the EGS computed
  from a finite population" (p. 5).

**Population performance (Definition 3, Proposition 5, p. 5).** v(P, Q) is
the value of the zero-sum game with payoff matrix φ(v, w), v ∈ P, w ∈ Q.
- (i) It does not depend on which Nash pair is used.
- (ii) In a monotonic game it compares the best agents of each.
- (iii) If hull(P) ⊂ hull(Q), then v(P, Q) ≤ 0 and v(P, R) ≤ v(Q, R) for
  every R.
In concentric rock-paper-scissors populations every v is 0, though the
outer ones exploit a rock-only opponent better.

**Effective diversity (Definition 4, p. 6).** d(P) = pᵀ⌊A_P⌋₊p, how much the
Nash-supported agents beat one another. It is zero when one agent
dominates.

**Algorithms (pp. 6–7).**
- PSRO_N trains a new agent against the Nash mixture. Proposition 6: if
  it beats the Nash, the gamescape strictly grows. It stalls once the
  game's own Nash, the origin in the disc game, is inside the gamescape.
- PSRO_rN trains each Nash-supported agent against the Nash-weighted
  mixture of the agents it beats or ties: "amplify their strengths and
  ignore their weaknesses". Proposition 7 calls its objective effective
  diversity. Training agents on what they lose to instead shrinks the
  gamescape: "Perhaps counter-intuitively, building objectives using the
  weak points of agents does not encourage diverse niches" (p. 7).

**Experiments (pp. 7–8).**
- Colonel Blotto (3 areas, 10 coins, MPO oracle) and differentiable Lotto
  (9 customers, gradient oracle), compared by relative population
  performance at fixed oracle budget.
- PSRO_rN is positive against PSRO_N, PSRO_U and self-play in both.
  PSRO_U and PSRO_N are comparable.
- Self-play tracked as a population still does worst in Lotto, but in
  Blotto it slightly beats PSRO_N and PSRO_U.
- Only PSRO_rN grows the hull's area at every iteration.
- Two games, no error bars reported in the text.

**Behaviourism** (appendix A). "The paper adopts a strict form of
behaviorism: an agent is what it does" (p. 10), or more exactly all that
it can do against every other agent.

## What it establishes and what it does not

**Proved and re-derived.** Theorem 1 as a direct sum, and with the L²
product as orthogonal. Propositions 2–7. 5(i) is the uniqueness of a game's
value. 5(iii) needs hull read behaviourally: each agent of P is, in its
results against everyone, a mixture of agents of Q. Then Q can mirror any
mixture of P, and antisymmetry gives v ≤ 0. Two defects:
- **Proposition 5(ii).** Printed as max f − max f "If φ is monotonic"; for
  φ = σ(f(v) − f(w)) the value is σ(max f − max f). The proof says only
  that both players concentrate on their best agent, which gives the σ
  form.
- **Definition 4.** Takes "a Nash equilibrium". The text then speaks of
  the maximum-entropy one. Unlike v, diversity depends on the choice.

**Not established.** That PSRO_rN outperforms in general. Two
resource-allocation games, and the paper itself names the failure mode in
which every agent has a private exploit and the population fills with
specialists. Nor anything about the gap between what a finite population
shows and the game, which the authors say cannot be bounded without
assumptions on φ.

## How it bears on the record

- **CASE-124 and CASE-tmpw4r7u: capture of the scoring layer.** Population
  performance is the strongest invariant in this group. It is a game value,
  so no equilibrium selection is involved, and redundancy in the strong
  sense, any member that is a behavioural mixture of others, leaves it
  unchanged. It avoids the uniqueness condition that Nash averaging needs
  (THEORY-tmpzogk3). The price is that it scores populations, not
  members. For the governance line, a coalition's standing so measured
  cannot be raised by adding processes that only reproduce what its
  members already do. **Narrows the capture routes, at the level of
  coalitions.**
- **TERM-077, CLAIM-434 and THEORY-894.** The monotonic/transitive
  distinction is the record's own. A monotonic game has an ordinal
  potential (the order by f) and a nonzero Hodge cyclic part, the gap
  CLAIM-434 records between acyclic wins and zero curl. The paper also shows
  that the Hodge transitive part is relative to a measure over
  opponents, which THEORY-894's weighted form implies and does not say in
  words. **Supports CLAIM-434's separation.**
- **CLAIM-tmpuxcp6.** Two things. First, "the performance of individual
  agents is meaningless" in a fully cyclic game is the strong form of the
  claim's nonintegrability. No transitive ordering of individual options
  exists, and the paper's answer is to stop ranking options and hold a
  portfolio, a Nash mixture over a population. That is close to the claim's
  third relief, cheap periodic coordination: a mixed or alternating
  allocation that keeps the cycle and stops paying for it. Second,
  lifting to populations only orders populations nested by hull
  (Proposition 5(iii)). Values between non-nested populations can cycle
  again, as singletons in rock-paper-scissors show. So moving from options
  to portfolios does not by itself make a record integrable.
  **Complicates: relief by mixing is formal here, and partial.**
- **CLAIM-tmp0qupq.** The contrast between self-play, which responds to
  the latest agent and cycles in cyclic games, and response to the
  population's Nash mixture, which accumulates, has a governance reading.
  A learned prior over authority updated only against the latest
  incumbent can cycle among regimes. One updated against a remembered
  population of regimes cannot cycle the same way. This is interpretive;
  the paper is about training agents. **Bears, by analogy only.**
- **CLAIM-436 and CLAIM-440.** A cyclic game admits no ordering of
  individuals, so no currency over them, but a value between populations
  exists always. That is a currency for portfolios, not for options, and
  it is cardinal. **Irrelevant to the options-level claims, and a possible
  extension.**
