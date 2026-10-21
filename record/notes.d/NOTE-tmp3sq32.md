---
status: Read
paper: LIT-tmp363mx
title: 'Bergemann and Morris — Information design, a unified perspective'
version: 1
history:
- version: 1
  date: '2026-10-21'
  note: >-
    Read in full from Cowles Foundation Discussion Paper 2075R3 (February
    2017, revised March 2018; the copy dated 20 March 2018 and marked
    "forthcoming in Journal of Economic Literature"; 71 pages), from the
    Cowles Foundation's site, text extracted with pdftotext. It is the
    accepted manuscript, not the typeset JEL article (57(1): 44–95), and
    was not compared with it. Read: §§1–8 and the Appendix (the
    computations for §3.2 and Propositions 5–6 with proofs). The figures
    are not in the extracted text ("Insert Figure …") and were read from
    the prose. The investment examples of §3 were re-derived here and the
    two-firm case solved as a linear program, the volatility bound of §5.2
    checked numerically, and Proposition 1 and the one-player inclusion
    of §4.2 re-derived.
date: '2026-10-21'
summary: >-
  A designer who can commit to how players are informed, but not to what
  they do, can attain exactly the Bayes correlated equilibria: joint
  distributions of states and actions in which no player, told his
  recommended action, wants to deviate. The set is a polytope given by
  linear obedience constraints, so information design is a linear program
  over it. Read literally there is a designer; read metaphorically the set
  bounds what any information structure could produce. More prior
  information shrinks the set. Public signals serve a designer who wants
  correlated actions, private ones the reverse. Its two-firm example with
  strategic substitutes misstates the optimal rule for the parameters it
  assumes.
---
<!-- inactive-ok-file: CLAIM-tmpjo2zr — Proposed; filed from the same exchange, the claim this reading bears on, cited as open -->
<!-- inactive-ok-file: TERM-tmp5lqn0 — Proposed; filed from the same exchange, named as the entry this reading bears on -->
<!-- inactive-ok-file: CLAIM-199 CLAIM-326 — Proposed; the Blackwell line, named for comparison, cited as open -->
<!-- inactive-ok-file: THEORY-156 THEORY-tmpmo8m9 — Proposed; readings of Blackwell's order and of the incentive order, cited as open -->
<!-- inactive-ok-file: LIT-tmp8x4zb LIT-tmpwyfa1 — Unavailable or Deferred; works not read, named for comparison -->

# NOTE-tmp3sq32: Bergemann and Morris — Information design, a unified perspective

## Contribution

A survey that puts Bayesian persuasion (one receiver, an informed sender),
communication in games (many players, an uninformed mediator) and the
authors' robust predictions under one problem: what can be achieved by
choosing players' information alone, in a game with uncertain payoffs.
Its tool is Bayes correlated equilibrium (BCE). Its distinctive emphasis
is the **metaphorical** reading, in which no designer exists and the set
of BCE is used by the analyst to bound what any information structure
could produce. It also places the problem in Forges's (1993) taxonomy of
correlated equilibria with incomplete information and discusses where the
revelation principle fails.

## Key insight

Control over what people know is control over a polytope of outcomes, and
the polytope is computable before anyone asks who controls it. "The
information design problem can be solved in two steps. First, we can
identify the set of outcomes that could be induced by the information
designer. Second, we can identify which of these outcomes would be
preferred." The first step is the same whether the designer is a
government, a platform, or nobody.

## Assumptions

- Finite players, actions and states; a common full-support prior ψ shared
  by the designer and players. A basic game G = ((A_i, u_i), Θ, ψ) and a
  prior information structure S = ((T_i), π).
- **Commitment**: the designer commits to a rule before the state and
  types are realized. This separates it from cheap talk and signalling.
- **Omniscience** in the leading case: the rule may condition on the state
  and on every player's type. §6 drops this (with and without elicitation).
- **The designer picks the equilibrium.** The revelation principle needs
  it. §7 drops it (maxmin design).
- All information structures are feasible, information is free, there is
  one designer, and the setting is static.
- Bayes Nash equilibrium as the solution concept.

## Key results

- **Definition 1, obedience.** For each i, t_i, a_i and a′_i:
  Σ u_i((a_i, a₋ᵢ), θ) σ((a_i, a₋ᵢ) | t, θ) π(t | θ) ψ(θ) ≥ the same with
  a′_i. Linear in σ.
- **Proposition 1 (revelation principle).** An omniscient designer can
  attain σ iff σ is a BCE. The proof is cited from Bergemann and Morris
  (2016a); re-derived in THEORY-tmpetatd.
- **§3.1, one uninformed receiver** (Kamenica and Gentzkow's example).
  Invest pays −1 in B and x ∈ (0, 1) in G, equal prior; the designer
  maximizes investment. Obedience is p_G ≥ p_B/x, so the optimum is
  p_G = 1, p_B = x: "obfuscate the states of the world in order to
  maximize investment". Re-derived.
- **§3.2, an informed receiver** with a signal correct with probability q:
  p_G ≥ q − (1 − q)/x, binding once q ≥ 1/(1 + x). Prior information
  shrinks the BCE set, and leaves it unchanged while the signal alone
  would not change the decision (at x = 0.55, q = 0.6 < 1/(1 + x) ≈ 0.645).
  Re-derived from the Appendix's (29)–(30).
- **§3.3, two firms** with extra payoff ε if both invest. For ε > 0, a
  public signal: p_B = r_B = (x + ε)/(1 − ε). Confirmed by linear
  programming. For ε < 0 the paper assumes x > ½ and |ε| ≤ x − ½ and
  states p_B = x + ε with r_B = 0, private signals. **That rule is
  infeasible under those assumptions**: p_B = x + ε ≥ ½ forces
  r_B ≥ 2p_B − 1 > 0, and the table's "not invest, not invest" entry
  1 − 2x − 2ε is negative. The linear program gives p_B = x/(1 − 2ε) with
  r_B = 2p_B − 1 (at x = 0.55, ε = −0.03: 0.5189, not 0.52). The paper's
  rule is right when x + ε ≤ ½. The qualitative point stands: the designer
  minimizes correlation under substitutes.
- **§4.1.** Public signals when the designer wants correlated actions,
  private when not, for intrinsic or instrumental reasons. Under
  complements, correlating play relaxes obedience. A benevolent designer
  may obfuscate, since players need not act in their joint interest. The
  "at least one invests" rule, each firm told to invest with probability ½
  in B and both in G, is obedient for x > ½ (conditional payoff
  (2/3)x − 1/3 > 0, re-derived; the extracted text renders the expression
  as "23 x − 12").
- **§4.2.** For one player, three orders coincide: Blackwell's "more
  informative", his sufficiency (garbling) order, and an incentive order,
  one experiment being more incentive-constrained if its BCE set is
  smaller in every decision problem. For many players, Bergemann and
  Morris (2016a)'s **individual sufficiency** is equivalent to the
  incentive order, and it neither implies nor is implied by sufficiency
  of the joint information. Cited, not proved here (THEORY-tmpmo8m9).
- **§4.3.** BCE and linear programming, against concavification
  (Aumann–Maschler; Kamenica–Gentzkow; Mathevet, Perego and Taneva for many
  players), with the limits of each.
- **§5.1, price discrimination** (Bergemann, Brooks and Morris 2015):
  every pair of consumer and producer surplus with consumer surplus ≥ 0,
  producer surplus ≥ uniform monopoly profit and total ≤ efficient
  surplus is attained by some segmentation. A three-value example
  attains three corners with one segmentation.
- **§5.2, volatility** (Bergemann, Heumann and Morris 2015): with signal
  s_i = λε_i + (1 − λ)θ and no strategic interaction, maximal aggregate
  volatility is (σ_θ + √(σ_θ² + σ_ε²))²/4 at λ* = σ_θ/(2σ_θ +
  √(σ_θ² + σ_ε²)) < ½, which stays σ_ε²/4 as aggregate shocks vanish.
  Checked numerically at four parameter pairs.
- **§6.** Without access to players' types the designer is held to
  incentive compatibility with elicitation (Definition 2, Proposition 2)
  or publicly feasible obedience without it (Definitions 3–4,
  Proposition 3). Proposition 5: without elicitation is a subset of with.
  Proposition 6: for one player with two actions and two states they are
  equal. A third action, "invest small", makes the sets strictly nested.
  These map onto Forges's five correlated equilibria.
- **§7.** If the worst equilibrium is played the revelation principle
  fails. Maxmin design recovers Kajii and Morris's robustness: in their
  example the designer can make both players invest with probability up
  to ε/(1 − x).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | The outcomes an omniscient designer can attain are exactly the BCE, a set given by linear obedience constraints | strong | Proposition 1, proved in the authors' 2016 paper; re-derived in THEORY-tmpetatd |
| C2 | Information design unifies Bayesian persuasion, communication in games and robust prediction | strong as a classification | the definitions; Forges's taxonomy mapped in §6.4 |
| C3 | More prior information shrinks the BCE set; for one player the incentive order is Blackwell's, for many it is individual sufficiency | strong for one player, cited for many | §4.2, from Bergemann and Morris (2016a); THEORY-tmpmo8m9 |
| C4 | Public signals are optimal when the designer wants correlated actions, private ones when it wants them uncorrelated | moderate | the two-firm example; cited general results (Arieli and Babichenko; Meyer); the substitutes case misstated |
| C5 | A benevolent designer may obfuscate when there are many players | moderate | the spillover example in §4.1 |
| C6 | Read metaphorically, BCE give predictions robust to the information structure: price discrimination's surplus triangle, aggregate volatility's bound | strong for the cited results | §5, summarizing the authors' papers; the volatility bound checked |
| C7 | Without access to types the attainable set shrinks, and elicitation helps exactly beyond binary one-player problems | strong | Propositions 2, 3, 5 and 6, with proofs of 5 and 6 |

## Concepts

- **Information designer**: commits to a rule mapping states and types to
  messages, cannot choose actions.
- **Decision rule** σ: T × Θ → Δ(A), action recommendations.
- **Obedience; Bayes correlated equilibrium**: Definition 1; a BCE is an
  obedient decision rule.
- **Literal and metaphorical information design**: a real designer
  against an analyst's device for bounding outcomes across information
  structures.
- **Omniscient; with and without elicitation**: whether the designer can
  condition on players' types directly, after asking, or not at all.
- **Individual sufficiency**: one structure is individually sufficient for
  another if some combination makes each player's signal in the first a
  sufficient statistic for his beliefs about the state and the others'
  signals in the second.
- **Maxmin information design**: the designer optimizes against the worst
  equilibrium.

## Connections

It generalizes Kamenica and Gentzkow (2011), held as LIT-1021 and
THEORY-404, which is its one-player case without prior information. It
extends Aumann's correlated equilibrium (1974, 1987) and Myerson's
communication in games (1982, 1991) to a designer with information of
her own, and Forges (1993). It surveys Taneva (2015), Mathevet, Perego and
Taneva (2017) and Kolotilin et al. (2017), and the authors' own BCE
papers. Blackwell (1951, 1953) is the one-player case of its ordering of
information structures.

## Bearing on the record

- **CLAIM-tmpjo2zr.** Its first route, governing an organization "through
  the evidence its own procedures receive", is information design in the
  literal reading, and Proposition 1 gives the exact reach of that route
  when the organization's procedures are Bayesian: any obedient joint
  distribution of states and decisions, and no other. The claim's
  independence of the two routes holds in this frame. Information design
  fixes the payoffs, so it cannot reach the claim's second route, the
  criteria by which evidence is weighed. A designer who could change u_i
  would be a mechanism designer (§6.3). The record's join.
- **The metaphorical reading** is the tool the record lacks for "what
  could any arrangement of information have produced here?". The set of
  BCE bounds the outcomes of every information structure, so if an
  observed pattern lies outside it, no story about who knew what explains
  it.
- **THEORY-404 and LIT-1021** are the one-player, no-prior-information
  case. This survey adds many receivers and prior information, and says
  prior information is what limits a persuader.
- **CLAIM-199, CLAIM-326 and THEORY-156.** §4.2's incentive order is a
  third face of Blackwell's order, beside "more informative" and
  garbling: a better-informed receiver is harder to steer, in every
  decision problem. For the record's ceiling, a garbling shrinks what the
  receiver can do and enlarges what a designer can make it do.
- **Reflexive control** (A25, LIT-tmpwyfa1, unread) and **Mostagir et
  al.** (LIT-tmp8x4zb, Unavailable): A25's link is the right one in kind.
  Reflexive control is designing an adversary's information to induce a
  chosen decision, and §7's maxmin design and the many-player BCE are the
  formal versions. The paper assumes Bayesian players with a common prior,
  which reflexive control does not.
- **TERM-tmp5lqn0.** What a designer chooses is what becomes legible to
  the players. The paper studies Bayesian, unbounded players, so its
  legibility is Blackwell informativeness, not usable information.

No instruction for machine-learning practice; nothing for the anthology.

## Limitations

- **A survey.** Its central results, Proposition 1, the §4.2 orderings and
  the §5 applications, are proved in the authors' other papers.
- **The two-firm substitutes example is misstated** in the copy read (see
  Key results). Whether the JEL version corrects it was not checked.
- **Bayesian, common-prior players** throughout. Bounded or mistaken
  receivers are outside it, so are self-confirming loops of the record's
  kind.
- **Commitment.** "the commitment assumption may be problematic in many
  settings". Without it this is cheap talk, which is not covered.
- **Equilibrium selection.** The revelation principle needs the designer
  to pick the equilibrium. §7 shows what changes when it cannot.
- **Static, one designer, free information.** Dynamic, competing and
  costly design are cited only.

## Open questions

- The authors': a many-player concavification as useful as the
  one-player one; a local approach to valuable information; dynamic
  design for platforms and recommender systems.
- For the record: what is the attainable set when receivers are bounded,
  so that a garbling can raise a receiver's usable information
  (THEORY-tmpgz4cf)? Then a designer could steer by making some
  distinctions easier to use, not only by withholding them.
