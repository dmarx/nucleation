---
status: Read
paper: 'LIT-tmp6d9wu'
title: 'Börgers & Sarin — Learning through reinforcement and replicator dynamics'
version: 1
history:
- version: 1
  date: '2026-10-24'
  note: >-
    Read in full on 2026-10-24 from the authors' working paper ("This
    Version: October 1995", 31 pp.), fetched from Levine's Working Paper
    Archive (www.dklevine.com/archive/refs4380.pdf) and extracted by
    pdftotext. Read: abstract, sections 1–7, all footnotes, and the four
    examples. Figures 1 and 2 are scanned and were read from captions and
    the surrounding text; the equations of Example 3 did not extract
    legibly. The reference list was skimmed. The journal version
    (JET 77:1–14) was not read. Page numbers below are the working
    paper's. Every quotation was checked against the extracted text by
    script.
date: '2026-10-24'
summary: >-
  A short theoretical paper. One Bush–Mosteller learner with payoffs in
  (0, 1), Cross's model, moves in expectation as a population under the
  discrete replicator step, and in the continuous-time limit follows the
  Taylor replicator dynamic at any finite time. For every learning speed,
  though, the discrete process is absorbed in a pure strategy profile with
  probability one. With negative payoffs a probability-matching force
  enters beside a replicator force. Proofs are by Euler's method and
  Norman's theorems on slow learning; the negative-payoff limit is stated
  with its proof omitted.
---
<!-- inactive-ok-file: THEORY-tmphhvqf THEORY-tmpbq2nj — Proposed; filed from this reading, named -->
<!-- inactive-ok-file: THEORY-tmp3oyxw THEORY-tmp9g2s5 CLAIM-tmp1xoac CLAIM-tmp0qupq CLAIM-tmp8z857 CLAIM-tmp28sti CLAIM-tmpuxcp6 NOTE-tmp43vkx CLAIM-436 CLAIM-440 — Proposed or new; the accounts this reading bears on, named in prose, nothing here rests on them -->

# NOTE-tmpcqwez: Börgers & Sarin — Learning through reinforcement and replicator dynamics

## What the paper does

**The question.** Whether the analogy between learning and biological
evolution holds at the level of the individual. The authors set aside
imitation in populations (Binmore and Samuelson, Schlag), which they call
complementary, and ask whether one learner's mind can be a population of
ideas (pp. 1, 6).

**The biological model** (Section 2). Two continuum populations, one per
player role. Each period a fraction α of each is drawn and matched; each
individual has offspring equal to its payoff, and deaths fall only on the
old so that sizes stay fixed. This gives Proposition 1: Δp_j = α p_j
(e_j U q − p U q). The altered death rule removes the denominator of
Binmore's discrete replicator equation, and is chosen to make the
comparison with learning exact. With time step θ and active fraction θα,
θ → 0 gives the continuous Taylor dynamic at every finite t
(Proposition 2, Euler's method).

**Cross's learning model** (Section 3). Two players, each observing only
its own action and payoff, with payoffs Ũ ∈ (0, 1) read as "strengths of
reinforcement", not von Neumann–Morgenstern utilities. Having played j
and received Ũ, a player sets P_j ← Ũ + (1 − Ũ)P_j and P_j′ ← (1 − Ũ)P_j′.
Proposition 3: the conditional expected change is p_j(e_j Ũ q − p Ũ q),
the biological model's actual change. I re-derived it: playing j (prob.
p_j) raises P_j by Ũ(1 − p_j) and playing j′ ≠ j lowers it by Ũ p_j, and
the sum is p_j[(Ũq)_j − pŨq]. Proposition 4: with steps scaled by θ, the
process converges in probability, as θ → 0 and nθ → t, to the continuous
replicator solution at t. The proof checks the conditions of Norman's
Theorem 8.1.1, all of them polynomial on a compact domain.

**Stimulus sampling** (Section 4). The learner as a continuum of stimuli,
each suggesting one action; one is sampled, and a mass of stimuli equal to
the payoff is re-programmed to the action taken. That is Cross's model
exactly, and a "pseudo-biological" model in which one representative
individual per population plays and has offspring of positive measure. The
learning process is the stochastic version of the biological one: equal
in expectation, and the same in the limit.

**Asymptotics** (Section 5). The limits hold at every finite time and say
nothing about t → ∞. Proposition 5: for every θ > 0 and every
initial state, the discrete learning process converges with probability one
to a pure strategy pair, by Norman's theorem on absorbing processes. The
absorbing states are J × K, and footnote 20 adds that from any interior start
every pure pair has positive probability of being the limit. In a matching
pennies game with payoffs 0.2 and 0.8, the continuous replicator dynamic
cycles on the level curves of p(1 − p)q(1 − q), the discrete replicator
process spirals out towards the boundary without converging, and the
learning process is absorbed in a corner. "Mathematically speaking, the
learning process converges pointwise, but not uniformly on the complete real
line, to continuous time replicator dynamics" (p. 17).

**Negative payoffs** (Section 6). Probability taken from a punished
strategy is redistributed, proportionally or to one randomly chosen
alternative; the two rules have the same expected motion. Norman's
regularity fails on the boundary, and the authors say they "believe" the
limit result extends, omitting the proof (p. 20). The limit is

dp_j/dt = p_j(Ū_j* − p|Ũ|q) + Ū_j*(σ_j* − p_j),

a replicator term in benefits and a term that drives the probability of
choosing j towards the probability σ_j* that j is reinforced. With all
payoffs of one absolute size the replicator term vanishes. In a
one-player problem the choice probability goes to the state probability μ
(Example 2), and in a ±0.5 matching pennies the mixed equilibrium is
globally stable, which they call accidental: "In general, probability
matching is irrational, and therefore the limit points of our learning
process will not be Nash equilibria" (p. 25).

**Further research** (Section 7). A moving aspiration level, studied in a
companion paper, makes some payoffs negative and so makes probability
matching unavoidable: "The endogeneity of the aspiration level then makes it
in most cases unavoidable that there is an element of probability matching
in the continuous time limit" (p. 26).

## What it establishes and what it does not

It establishes, as theorems, that one Cross learner's expected motion is the
discrete replicator step of a two-population model, and that on any finite
horizon the slow-learning limit is the deterministic Taylor replicator
dynamic. It also establishes that the identification fails at infinity in
the strongest way: the expected dynamic can cycle, while every sample path
is absorbed at a vertex. The negative-payoff limit is stated and computed
in examples, with the proof omitted. The paper does not show that people
learn this way. It cites the experiments as "some support" (p. 4) and
names habitual choice as the domain where the model is most plausible. It
treats two players, not multi-agent systems in general. Its asymptotic
result is for this rule: payoffs as fractions of the distance to a vertex,
with no exploration.

## How it bears on the record

- **The replicator reading of authority (CASE-tmpw4r7u,
  CLAIM-tmp1xoac).** These inherit "Cross learning is the Taylor replicator
  dynamic" through Soma et al. (THEORY-tmp3oyxw). The source supports
  it and narrows it: the identity is of expected motion, and of actual
  motion only on finite horizons in the slow-learning limit. Results about
  long-run behaviour, such as rest points, cycles and basins, transfer from
  the replicator dynamic to the learner only with that caveat. Stochastic
  stability, which CLAIM-tmp1xoac brings in for finite populations, is the
  right tool for exactly this reason.
- **Lock-in (CLAIM-tmp0qupq, CLAIM-tmp8z857, CLAIM-tmp28sti).** Proposition 5 is
  absorption without any self-confirming loop. A single learner whose
  updates are payoff-weighted moves towards what it just did, and with no
  exploration it ends at a pure profile with probability one, which
  profile depending on chance. That supports the record's worry that
  persistence need not mean fitness, and narrows its mechanism: the claims
  locate entrenchment in evidence or authority feedback, and here
  entrenchment needs neither, only reinforcement of the chosen with no
  return path. It is the single-learner counterpart of Soma et al.'s
  finite-population loss of types (THEORY-tmp9g2s5). Read for
  CLAIM-tmp8z857, relief as reinforcement of the defensive choice is this
  update rule, and absorption is the limiting case of a defense chosen so
  often that the alternative is never sampled.
- **Cycles (CLAIM-tmpuxcp6).** Matching pennies shows that a cycle in the
  mean dynamic need not be a cycle in any realized learner. A cyclic regime
  observed in an organization's record is evidence of something beyond
  Cross-style reinforcement, such as exploration or noise, which keeps it
  off the boundary. The Q-learning dynamics read beside this one
  (NOTE-tmp43vkx) supply such a term.
- **Probability matching.** A learner that matches choice to success
  frequency, as the moving-aspiration case makes unavoidable, ends where
  no ordering of the options is followed exactly. It bears on the record's
  common-currency line as a known mechanism by which reinforcement learning
  departs from maximizing, not as a failure of ordering. CLAIM-436 and
  CLAIM-440 are not otherwise touched.
