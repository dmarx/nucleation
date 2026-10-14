---
number: 717
status: Read
formerly:
- NOTE-tmp7gxox
paper: LIT-1021
title: 'Kamenica & Gentzkow — Bayesian Persuasion'
version: 1
history:
- version: 1
  date: '2026-10-13'
  note: >-
    Read in full from the published AER PDF (26 pp., pp. 2590–2615) posted
    on Gentzkow's Stanford faculty page
    (web.stanford.edu/~gentzkow/research/BayesianPersuasion.pdf). Text
    extracted with pdftotext. The text layer is clean, but the hats and
    tildes on v̂, ṽ and Ṽ come out displaced, so formulas were read against
    the layout and are restated here, not quoted. Read: the introduction,
    Sections I–VII, all footnotes, and Appendix A (the proofs of
    Propositions 1–5 and Lemmas 1–5). The steps the authors call "simple
    algebra" were not all redone; the judge example's numbers were. Not
    read: the online Appendix, to which the article defers the compact
    metric state space, the equivalence with verifiable concealment, the
    upper bound on gains in other communication games, and the monotone
    case of "worst belief". The NBER working paper (w15540, November 2009,
    nber.org) was consulted only for two passages, its related-work
    paragraph and its Section 7.6 on limited commitment, and is cited as
    such. Every quotation below was checked against the extracted text by
    script, with whitespace and line-end hyphenation normalised.
date: '2026-10-13'
summary: >-
  With a common prior and a sender who commits to a signal the receiver
  sees, any distribution of posteriors whose mean is the prior can be
  induced, so the sender's best value is the concave closure of its
  posterior-value function at the prior (Corollary 2). A fully informed,
  fully rational receiver can be moved; at the optimum she is indifferent
  whenever she acts for the sender. The paper never cites Blackwell, does
  not analyse manipulation, and has the receiver know the design.
---
<!-- inactive-ok-file: CLAIM-050 CLAIM-199 — Proposed; the Blackwell-line claims this reading bears on, open -->
<!-- inactive-ok-file: THEORY-040 — Proposed; the present-structure account QUESTION-071 holds, cited as open -->

# NOTE-717: Kamenica & Gentzkow — Bayesian Persuasion

## Contribution

A general model of a sender who chooses what a receiver will learn, with
an arbitrary finite state space, compact action space, prior and
preferences. It shows that choosing a signal is the same as choosing a
distribution of posteriors whose mean is the prior, and that nothing else
constrains it. From that it gets a necessary and sufficient condition for
the sender to gain (the concave closure of its value lies above its value
at the prior) and properties of the optimal signal. The mathematics is
Aumann and Maschler's concavification, which the authors credit; what is
new is the general persuasion setting and the characterisations.

## Key insight

Bayes's rule constrains only the average of the beliefs a signal produces.
So a sender who controls the experiment, but not its reading, can split
the prior into posteriors arranged to fall where the receiver's action
changes in its favour. The receiver who knows exactly how the experiment
was designed still acts as the sender wants more often than she would
without it: in the judge example, "the judge knows 70 percent of
defendants are innocent, yet she convicts 60 percent of them!"

## Assumptions

- **Common prior** μ₀ in the interior of Δ(Ω); Ω finite (compact metric in
  the online Appendix, unread); A compact, at least two actions, each
  optimal at some belief; u and v continuous.
- **Commitment.** Receiver observes the chosen signal π and its realization,
  and the realization is reported truthfully. "This makes our environment
  effectively nonstrategic." Sender's "choice of a signal establishes the
  meaning of messages". The authors defend it by legal mandate (Brady v.
  Maryland), committed disclosure rules (grading, hospital ratings),
  organizational procedure ("Firms commit to the information they will seek
  out for performance reviews"), publicly registered studies, and direct
  observation (taste tests, trial software).
- **No transfers**, and Sender cannot affect Receiver's payoffs.
- **Sender-preferred tie-breaking:** "If Receiver is indifferent between some
  actions at a given belief, we assume she takes an action that maximizes
  Sender's expected utility." This is what lets the optimum put Receiver
  exactly at indifference.
- **Single receiver.** Multiple receivers who care about each other's actions
  and receive private signals are explicitly outside the method.
- **Arbitrarily informative signals** are made innocuous by redefining the
  state: see the garbling passage under Connections.

## Key results

- **Proposition 1.** For a value v*, these are equivalent: some signal has
  value v*; some *straightforward* signal (realizations are recommended
  actions, and Receiver follows them) has value v*; some Bayes-plausible
  distribution of posteriors τ has E_τ v̂(μ) = v*. Construction: π(s | ω) =
  μ_s(ω) τ(μ_s) / μ₀(ω). Bayes plausibility is "the only restriction on the
  equilibrium distribution of posteriors". The first equivalence is likened
  to the revelation principle.
- **Corollary 2.** With V the concave closure of v̂, the value of an optimal
  signal is V(μ₀), and Sender benefits from persuasion iff V(μ₀) > v̂(μ₀).
  An optimal signal exists because Sender-preferred tie-breaking makes v̂
  upper semicontinuous.
- **Judge example.** Prior Pr(guilty) = 0.3; Receiver convicts iff the
  posterior is at least 0.5. The unique optimum is π(i | innocent) = 4/7,
  π(g | innocent) = 3/7, π(g | guilty) = 1, giving posteriors 0 (weight
  0.4) and 0.5 (weight 0.6), and conviction with probability 0.6 against
  0 with no information and 0.3 with full information.
- **Remark 1.** v̂ concave: no gain at any prior, and no disclosure is
  optimal. v̂ convex and not concave: gain at every prior, and full
  disclosure is optimal.
- **Proposition 2.** No "information Sender would share" (no μ with v̂(μ) >
  E_μ v(â(μ₀), ω)) implies no gain. Such information plus a discrete
  preference at the prior implies a gain. With A finite, discreteness holds
  at the prior generically (except on a Lebesgue-null set). The sufficient
  condition is useless for connected A.
- **Proposition 3 (and 6 in the appendix).** If v̂(μ) = ṽ(Tμ) for a linear T,
  Sender benefits iff ṽ lies below its concave closure at Tμ₀. For the
  expected-state case Ṽ is only an upper bound on the optimal value, with a
  counterexample (A = [0,1], Ω = {−1, 0, 1}, v = a²).
- **Proposition 4.** If an optimal signal induces a belief that leads to a
  worst action, Receiver is certain of her action there.
- **Proposition 5.** Under Assumption 1 (no weakly-but-not-strictly induced
  dominant action) and a strict gain, at any induced belief that is interior
  or leads to a best-attainable action, Receiver's preference is not
  discrete: with finite A, she is indifferent between two actions.
- **Alignment (Section IV).** More aligned preferences weakly raise Sender's
  optimal value, but can lower the gain, and "making preferences more
  aligned can reduce the extent of communication in equilibrium."
- **Lobbying.** Quadratic losses; full disclosure is uniquely optimal when
  α > 1/2, no disclosure when α < 1/2, and the bias ω* does not matter.
  Observed industry-biased studies therefore suggest that "the intended
  constituency is not fully rational, the lobbyists cannot commit not to
  distort study results ex post, or the payoff functions differ".
- **Product information.** A trial separates consumers into those sure the
  product is not for them and those just willing to buy; "Such optimal
  information provision allows the firm to extract all the consumer
  surplus."
- **Extensions.** Receiver's private information and her own later
  information gathering are absorbed into v̂, keeping Proposition 1 and the
  corollaries but losing the discreteness results.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Any Bayes-plausible distribution of posteriors is induced by some signal, so Bayes plausibility is the only constraint | strong | Proposition 1, proof in Appendix A (Carathéodory for finite support) |
| C2 | Sender's optimal value is V(μ₀); Sender gains iff V(μ₀) > v̂(μ₀) | strong | Corollary 2 |
| C3 | With finitely many actions, information Sender would share suffices for a gain at a generic prior | strong | Proposition 2 and Lemma 1 |
| C4 | At an optimum the receiver taking the worst action is certain, and the receiver at an interior belief is indifferent | strong under Assumption 1 | Propositions 4 and 5 |
| C5 | Greater preference alignment can make the optimal signal less informative | strong as an existence claim | Section IV argument; the lobbying example for ω* |
| C6 | Commitment results bound Sender's gain from communication in any other communication game | asserted here | proof in the online Appendix, unread |
| C7 | Systematic harm to receivers from persuasion indicates limited rationality | informal | the Conclusion's one sentence; no theorem in the article |

## Concepts

- **Signal π.** A finite realization space S and distributions π(· | ω).
  An experiment in Blackwell's sense, though the paper does not say so.
- **Distribution of posteriors τ; Bayes plausible.** τ over Δ(Ω) with
  Σ μ τ(μ) = μ₀.
- **Straightforward signal.** S ⊆ A, and Receiver takes the recommended
  action.
- **v̂(μ).** Sender's expected utility when both hold belief μ and Receiver
  plays â(μ).
- **Concave closure V.** The smallest concave function weakly above v̂
  (Aumann and Maschler's concavification).
- **Default action.** â(μ₀), Receiver's action with no information.
- **Persuasion and incentives.** "There are two ways to induce a person to
  do something. One is to provide incentives, by which we mean anything
  which changes marginal utility—explicit payments, coercion, or supply of
  complementary goods. The other is to persuade, by which we mean anything
  which changes beliefs."
- **Discrete preference; worst action; best-attainable action; more
  aligned.** As defined in Sections II–IV.

## Connections

- **Aumann and Maschler (1995)** supply the formal method; the authors call
  their problem "mathematically analogous". Brocas and Carrillo (2007) is
  the binary special case. Crawford and Sobel, Grossman, Milgrom, Kartik
  and Spence are the strategic-communication models from which commitment
  sets this one apart.
- **Blackwell is not cited.** The word does not occur in the published
  article or the NBER working paper. The garbling relation is there,
  unnamed: "We can define ω to be the realization of the most informative
  signal Sender can generate. Then, his choice of π is equivalent to a
  choice of how much to garble information that is potentially available."
  Footnote 5 points to Ganuza and Penalva's orders on signals by the
  dispersion of posteriors, and footnote 15 notes that comparing "the
  informativeness of sets of signals" is a complication left aside.
- **Deception and bounded receivers** are set aside. The NBER version names
  work "where Receivers are not perfect Bayesians (Mullainathan, Schwartzstein,
  and Shleifer 2008, Ettinger and Jehiel forthcoming)" and keeps it apart.
  It also says that if Sender chose his signal covertly, "the only
  equilibrium would be for Sender to choose the fully informative signal and
  the set of equilibria would be isomorphic to those of Crawford and Sobel
  (1982)."

## Bearing on the record

The LIT's standing named three checks. Each is answered here.

**Does the paper relate persuasion to Blackwell's order ([CLAIM-050](../claims.d/CLAIM-050.md))?** Not
by name. It has the garbling relation, in the passage quoted above, and it
uses it only to defend the assumption that Sender can generate any signal.
It does not order signals by informativeness, compare the optimum with
full disclosure in Blackwell's sense, or prove anything about the order.
The LIT's phrase "preferring a garbling of full information" is therefore
the record's gloss, and as stated it is empty: under the paper's
redefinition of ω every signal is a garbling of full information, the
optimum included. What the paper does show, and what bears on [CLAIM-050](../claims.d/CLAIM-050.md),
is that the party who chooses the experiment can strictly prefer a less
informative one, and that how much it reveals is not monotone in how
aligned it is with the receiver (C5). That does not conflict with
Blackwell's theorem, which ranks experiments for the person deciding;
Sender's objective is not a decision problem of Receiver's. The bearing
is the record's: [CLAIM-050](../claims.d/CLAIM-050.md) says what fidelity is for a receiver, and this
paper is a reason not to assume that whoever chooses the rendering
procedure wants the procedure that ranks highest. It also touches
[CLAIM-230](../claims.d/CLAIM-230.md): the paper fixes the state by fiat as "the realization of the
most informative signal Sender can generate", so here too the decision
measure is fixed by whoever labels the state. Nothing in the paper bears on
the bounded-receiver claims ([CLAIM-199](../claims.d/CLAIM-199.md), [CLAIM-225](../claims.d/CLAIM-225.md)); its receiver is ideal.

**Is it manipulation ([QUESTION-070](../questions.d/QUESTION-070.md))?** The paper does not say, and does not
ask. It uses the word once, in the introduction, as a gloss on Sender's
aim: "If Receiver understands that Sender chose what information to convey
with the intent of manipulating her action for his own benefit, can Sender
still gain from persuasion?" Its own taxonomy has two kinds of influence,
incentives and persuasion, with coercion among the incentives and
"anything which changes beliefs" counting as persuasion. Manipulation is
not a third kind. The nearest normative remark is the Conclusion's, that
systematic harm to receivers "suggests that limited rationality may be at
play" (C7). Two things in the paper matter for where [QUESTION-070](../questions.d/QUESTION-070.md) would
draw the line, and both readings of them are the record's:

- *Harm depends on the baseline.* In the judge example, the record's
  arithmetic gives the judge a just verdict with probability 0.7 under the
  optimal signal (0.4 sure acquittals plus 0.6 × 0.5 convictions), exactly
  what she gets with no information and below the 1.0 of full information.
  In the product example the consumer, indifferent when she buys, gets her
  outside option either way, and the firm takes "all the consumer
  surplus". So the receiver is not harmed against no information, and
  loses all the value the information could have had for her. An account
  that defines manipulation by harm has to say which baseline it uses.
- *The definitions on file need intent and covertness.* Susser, Roessler
  and Nissenbaum ([LIT-1002](../literature.d/LIT-1002.md), unread) are summarised in [QUESTION-070](../questions.d/QUESTION-070.md) as
  requiring that influence be intentional and covert. Here the design is
  overt, and the paper's aim is to show it works when overt. If those
  definitions are right, Bayesian persuasion is not manipulation, whatever
  the sender intends. The LIT's statement that this is "often argued" was
  not checked against any work and still is not.

On the organized-whole part, the paper's Sender is any optimiser of v; no
intention enters the analysis beyond the maximisation. Several of its own
examples are institutional procedures: grading policies, rating
procedures, performance reviews, tenure rules. That a procedure adopted
for any reason, or selected, would have the same effect is the record's
inference, not the paper's.

**Is the steering invisible in present structure ([QUESTION-071](../questions.d/QUESTION-071.md))?** In this
model, no, and the LIT's standing needs correcting. The receiver is not
ignorant of who chose the information structure or why: she observes the
signal, and the paper stresses that she is "fully aware that the
investigation was designed to maximize the probability of conviction."
The history the LIT says would reveal the steering is common knowledge, and
knowing it does not undo it. Moreover the optimum leaves a trace in present
belief: by Propositions 4 and 5 the receiver is certain when she takes the
sender's worst action and indifferent when she takes another. A posterior
that sits exactly on a decision boundary is the signature of sender-optimal
design. So the case does not instantiate [QUESTION-071](../questions.d/QUESTION-071.md)'s first part
(invisibility). It is a different case the question does not yet name:
influence that is fully visible and still effective, because each step of
the receiver's inference is correct. Whether that helps [THEORY-040](../theory.d/THEORY-040.md) is open;
the paper is about beliefs and actions, not about will or psychological
structure.

The paper carries no instruction for machine-learning practice.

## Limitations

- **The receiver is an ideal Bayesian with a common prior.** Every result
  depends on it; the paper treats departures as outside its scope and as
  evidence of limited rationality.
- **Commitment is strong.** The paper defends it with real settings and,
  in the online Appendix (unread), with an equivalence to verifiable
  concealment and an upper-bound result.
- **One receiver.** The method fails when receivers' actions depend on
  others' signals.
- **No welfare or normative analysis.** Receiver's welfare is not computed
  anywhere in the article; the remarks on it above are the record's.
- **Not Blackwell.** Informativeness is used informally, and comparing sets
  of optimal signals is left aside (footnote 15).

## Open questions

- Whether the receiver's indifference at the optimum is a general signature
  a third party could test for, not only in the finite-action case.
- Whether a definition of manipulation by function or selection history
  ([QUESTION-070](../questions.d/QUESTION-070.md)'s "what would answer it") counts overt, committed
  information design, and what baseline its notion of harm uses.
- What the order on signals that persuasion induces looks like against
  Blackwell's: Ganuza and Penalva's dispersion orders, cited in footnote 5,
  would be the place to look.
