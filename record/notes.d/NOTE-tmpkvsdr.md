---
status: Read
paper: LIT-966
title: 'Handfield et al. — Cooperative Dilemmas in Rational Debate'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from arXiv:2504.06485v1 (39 pages), text extracted with
    pdftotext: the main text (§§1–4) and the whole Supplementary
    Information (A–D: the argument semantics, the strategy enumeration,
    the formal model and Markov-chain payoff computation, the error
    extension, and the supplementary figures). Figure 5, the one the
    non-monotonicity result rests on, was viewed as a rendered page
    image. The other figures were read from captions and the text
    reporting them. The code repository was not opened.
date: '2026-10-14'
summary: >-
  Two debaters move through a Betz-style space of truth assignments,
  each moving minimally when refuted, with payoff u = w·v − d (true
  beliefs against changes of mind). At moderate truth weights the
  truth-optimal equilibrium is asymmetric: one debater argues boldly and
  the other free-rides with a compromise strategy, a snowdrift dilemma.
  At low weights, or with error, both exit. In a narrow borderline region
  of mixed equilibria, raising the weight on truth lowers collective
  accuracy. A two-person model, n = 3 propositions, and every result is
  numerical.
---
<!-- inactive-ok-file: CLAIM-192 THEORY-tmpvtupa — Proposed; the thesis this reading bears on, named and not leaned on, and the account filed from this reading -->

# NOTE-tmpkvsdr: Handfield et al. — Cooperative Dilemmas in Rational Debate

## Contribution

The paper turns Betz's debate dynamics into a two-player game. Debaters
care about ending with true beliefs and also about not changing their
minds. It shows that this mixed motive makes debate a cooperative
dilemma in parts of parameter space: there are profiles that are
socially optimal for accuracy but are not equilibria. It also shows that
stronger truth motivation does not always raise equilibrium accuracy.

## Key insight

In deductive debate, being refuted is costly to the refuted party and
useful to both. So each debater would rather the other did the
belief-disrupting work. Arguing boldly means choosing premises one
accepts for conclusions one rejects, so that every argument eliminates
one's own position. Bold argument is a contribution to a public good,
and free-riding on it is individually rational.

## Assumptions

- **Two debaters** and n logically independent atomic propositions,
  with n = 3 for exact results. Positions are vectors in {0,1}^n, and
  one random position is the truth.
- **Arguments** have two premises and one conclusion. An argument
  eliminates the positions satisfying the premises and the negation of
  the conclusion. Logic is classical and monotonic. In the baseline,
  arguments are valid, meaning they never eliminate the truth.
- **Minimal revision.** A refuted debater moves to the nearest tenable
  position by Hamming distance, with ties broken at random.
- **Strategies** are fixed rules on premises × conclusion, each drawn
  from {S+, S−, O+, O−} (self or other, accept or reject), giving 16
  strategies plus Exit. A debater picks uniformly among feasible
  argument classes and passes if none is feasible. A rule that depends
  only on current positions is a strong restriction: there is no memory
  and no planning.
- **Turns** are random. After each argument the debate continues with
  probability δ. The SI says "ends with probability δ" at one point, but
  Eq. 18 and the main text treat δ as the continuation probability.
- **Payoff** u = w·v − d, where v ∈ [0, n] is the number of true beliefs
  at the end and d is the total Hamming distance moved. Exit gives
  w·n/2 to both.
- **Error extension.** With weight α, invalid arguments (which eliminate
  the truth) are chosen too.
- **Equilibrium selection.** Nash equilibria after iterated removal of
  weakly dominated strategies. Among those left, the one most
  truth-conducive (an "epistemic planner") is chosen. A utilitarian
  criterion is checked in SI D.3.

## Key results

- **Strategy classes and accuracy (Fig 2, n = 3).**
  - Profiles with at least one bold strategy (S+S− or O+O−) maximise
    collective accuracy.
  - Profiles where both are conservative or both refusenik do much
    worse.
  - Profiles with a compromising strategy and none bold vary widely.
- **Error (Fig 3).** At α = 0, (S+S−, S+S−) is truth-maximising for all
  δ. At α > 0, less argumentative profiles do better in long debates,
  because bold argument keeps eliminating until something goes, possibly
  the truth.
- **Cooperative dilemmas (§2.4.2, after Peña and Nöldeke).** C and D
  form a cooperate–defect pair iff E(C,C) > E(D,D), E(C,C) ≥ E(C,D) and
  E(D,C) ≥ E(D,D), with at least one inequality strict. A game is a
  cooperative dilemma if C is in a social optimum, D is played in a
  suboptimal equilibrium, and (C, D) is such a pair.
- **Table 1 (δ = 0.8).**
  - Truth weight 2.5: a prisoner's dilemma, S−O− against S+S+.
  - Truth weight 3.5: a stag hunt (S−O− against S+O+) and a snowdrift
    (bold against S+O+).
  - Truth weight 4.5: a snowdrift.
  - Truth weight 9.5: no dilemma.
  - (Exit, Exit) appears as a pure equilibrium in *every* row. That is
    structural: if the other debater exits, no deviation changes your
    payoff.
- **Harmony (Fig 4).** The rank correlation of payoffs is always
  positive, so debate is never zero-sum. Cooperation is easiest in long
  debates and a narrow band of truth weights.
- **Regimes (Fig 5, α = 0).**
  - Low w: refusenik, "almost invariably" (Exit, Exit), an "agreement to
    disagree".
  - High w and short debates: all-bold. S+S− weakly dominates, and
    (S+S−, S+S−) is the unique equilibrium after elimination and
    truth-optimal.
  - Slightly lower w or longer debates: the best reply to S+S− is a
    compromise such as S+O+, giving an asymmetric bold–compromise
    equilibrium, a snowdrift with "a modest loss of collective accuracy".
  - A borderline band: conservative strategies appear.
- **Error and disengagement (§2.6.4).** At α = 0.1 and α = 0.3,
  refusenik strategies, mostly Exit, take over much of the space.
- **Non-monotonicity (§2.6.5, Fig 5 lower panels, Fig 9).** At α = 0 and
  α = 0.1, collective accuracy dips as w rises within the borderline
  band. Here there is no pure equilibrium, and in the mixed equilibrium
  each player randomises to make the other indifferent. So as a player
  cares more about truth, "their opponent must therefore more frequently
  use strategies to frustrate that outcome". The rendered figure shows
  the dip as local and small, most visible for δ = 0.9. Fig 9 reports
  that it survives utilitarian equilibrium selection.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Bold argument is truth-optimal for error-free debaters | moderate | exact Markov computation, n = 3, Figs 2–3 |
| C2 | Mixed truth-and-obstinacy motives make debate a cooperative dilemma (PD, stag hunt or snowdrift) at low and moderate truth weights | moderate | Table 1 at δ = 0.8; Fig 5 across δ |
| C3 | The typical dilemma is snowdrift: one debater argues boldly and the other free-rides with a compromise strategy | moderate | §2.6.3, Fig 5 |
| C4 | Raising the truth weight can lower equilibrium collective accuracy | weak | a narrow mixed-equilibrium band, a small dip, Fig 5 and Fig 9 |
| C5 | Higher error rates drive debaters to exit | moderate | Fig 5, α = 0.1 and 0.3 |
| C6 | Obstinacy is a rational response to deductive refutation, since revision may move one further from the truth | weak | informal argument, §3 |
| C7 | The framework could explain confirmation bias, mistaken expert consensus and polarisation | weak | stated as a possible generalisation, §3, not modelled |

## Method

For n = 3, the debate is a Markov chain on states (T, p′, p″): 2,816
states, and over 4,000 with error. Expected end-states are computed as
(1 − δ)·y(0)(I − δM)^−1, and expected revisions as
d = δ Σ_{i,j} z_i M_ij Q_ij with z = y(0)(I − δM)^−1. For n ≥ 4, the
chain (about 2.5 million states at n = 4) is replaced by simulation, with
200,000 or more debates per profile (Fig 8). Nash equilibria come from
the 17 × 17 payoff table.

## Concepts

- **Tenable position.** A truth assignment not yet eliminated by any
  argument.
- **Bold, conservative, compromising, refusenik.** Bold strategies force
  a move unless the target already holds the truth. Conservative ones
  never force at least one debater to move. Refusenik ones never force
  anyone to move. Compromising ones are the remaining dyadic strategies.
- **Collective accuracy.** The mean of the two debaters' fractions of
  true beliefs, which is what "a hypothetical impartial observer" cares
  about.
- **Consensus.** The share of propositions on which the two agree. It is
  tracked separately, since consensus need not be on the truth (SI D.1).
- **Obstinacy.** The aversion to revision, priced at one unit per
  proposition flipped.

## Connections

The model builds on Betz's *Debate Dynamics* (2013). It differs in
having random turn order, a continuous end probability and no fallback
to random arguments (SI B.1). It takes its definition of cooperation from
Peña and Nöldeke (2023). It places itself beside Mayo-Wilson, Zollman and
Danks's independence thesis, List and Pettit's and Dunn's epistemic
free-riding, and Zollman's network models ([LIT-735](../literature.d/LIT-735.md), which the record
holds), and it cites Zollman's transient diversity for "why expert
communities sometimes maintain mistaken consensus".

## Bearing on the record

- **[QUESTION-047](../questions.d/QUESTION-047.md).** The paper supplies a named mechanism by which
  individually rational inquirers produce a collectively worse epistemic
  state: free-riding on the cost of being refuted. That part is filed as
  [THEORY-tmpvtupa](../theory.d/THEORY-tmpvtupa.md). Three cautions about using it for the question:
  - **Two people, not a community.** No structural variable of the kind
    [QUESTION-047](../questions.d/QUESTION-047.md) lists (communication density, influence weighting) is
    present. The variables are debate length, truth weight and error
    rate.
  - **No settled group belief.** The outcome measured is *collective
    accuracy*, the mean of two individual accuracies. The paper does not
    show the pair settling on a shared belief that neither reasoned to.
    Each debater ends where minimal revision under the other's
    arguments put it, which is in a sense where neither reasoned to
    independently, but the paper does not frame or measure it that way.
  - **"Sound" needs a qualifier.** The debaters are logically flawless at
    α = 0, but they are not pure truth-seekers: obstinacy is in their
    utility. [QUESTION-047](../questions.d/QUESTION-047.md)'s "individually sound inquirers" fits only if
    a preference against revising beliefs counts as soundness. The paper
    argues it can (§3), informally.
- **The LIT's seeded claim, checked.** [LIT-966](../literature.d/LIT-966.md)'s body says this "is a
  named mechanism by which a group settles on what no member reasoned
  to". The first half is fair. The second is the record's reading, not
  the paper's: the paper shows equilibrium strategy profiles with lower
  collective accuracy than the social optimum, not a group settling on a
  belief. It also says "strategies that are optimal for each debater
  give a collectively worse belief outcome", which holds only in the
  dilemma regions. At high truth weight with short debates the
  equilibrium is the truth-optimal one (Table 1, "No dilemmas"; §2.6.2).
- **The LIT summary's "raising the debaters' motivation to seek truth can
  sometimes give equilibria with worse collective outcomes".** Accurate,
  and "sometimes" is apt: the effect is confined to a narrow band of
  mixed equilibria and is small.
- **[CLAIM-192](../claims.d/CLAIM-192.md).** The debaters' strategies are fixed rules over current
  positions, so the model is no direct test of a multi-session argument.
  It does suggest one design for one: whether participants who bear the
  cost of revision argue less boldly.
- No instruction for machine-learning practice; nothing for the
  anthology.

## Limitations

- n = 3 for the exact results. Larger n is shown only for equilibrium
  types (Fig 8), from simulation.
- The strategy space is coarse and memoryless. The "ideal cooperative
  debater" of §2.4.1 lies outside it, as the authors say.
- Propositions are atomic and independent, and logic is classical,
  which the authors acknowledge.
- Equilibrium selection by a truth-favouring planner is an idealisation.
  (Exit, Exit) is always an equilibrium, so which equilibrium the
  results describe depends on selection.
- The broader explanatory claims of the Discussion are not modelled.

## Open questions

- Does the snowdrift structure survive in groups larger than two, where
  free-riding on others' refutations becomes a many-player public-goods
  problem?
- Would strategies with memory or adaptive targeting, nearer the ideal
  cooperative debater, remove the dilemma?
- Is the non-monotonicity robust beyond n = 3 and the borderline band?
