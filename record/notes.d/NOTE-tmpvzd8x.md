---
status: Read
paper: 'LIT-tmpdbgz6'
title: 'Language Evolution by Iterated Learning With Bayesian Agents'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read from the authors' posted copy of the published article
    (cocosci.princeton.edu/tom/papers/iteratedcogsci.pdf: the Cognitive
    Science 31 (2007) 441–480 typeset pages, 40 pages, text layer). All
    eight sections, the notes and the figure captions read in full; the
    reference list checked for what it cites. The symbol ε (production
    noise) and some summation signs did not survive text extraction;
    equations involving them are reconstructed from the surrounding
    prose and checked against each other (Table 1's θ1 and λ2 follow from
    Eqs. 14 and 15 with its q12 and q21). Figures are plots without
    numbers in the text; no value is read off them.
date: '2026-10-09'
summary: >-
  Iterated learning is a Markov chain on hypotheses. If every learner
  shares a prior and samples from its posterior, the chain is a Gibbs
  sampler on P(d|h)P(h), so the probability a learner holds language h
  converges to the prior P(h), whatever the amount of data passed on. If
  learners take the MAP hypothesis, it is stochastic EM with no
  observations: the outcome centres on the prior's mode, depends on data
  amount and noise, and in a two-language case is the same for every
  prior strength below a threshold. An unbounded population with equal
  fitness has the same equilibrium.
---

<!-- inactive-ok-file: LIT-tmp9f0fn — Deferred, no lawful full text; named as the ancestor of the method, not leaned on -->
<!-- inactive-ok-file: THEORY-tmp0w0cu — Proposed; the account this reading produced or bears on -->

# NOTE-tmpvzd8x: Language Evolution by Iterated Learning With Bayesian Agents

## Contribution

Before this paper, iterated learning (Kirby's model of each learner
learning from the output of a previous learner) was studied by simulating
particular learning algorithms, and the argument that a "bottleneck" on
transmitted data drives languages toward structure rested on those
simulations. After it, there is a general analytic result for Bayesian
learners: when learners sample from the posterior, the stationary
distribution over languages is exactly the learners' prior, independent of
the data, the bottleneck and the hypotheses' structure. It also identifies
the two learning rules with two statistical algorithms, the Gibbs sampler
and stochastic EM, so their convergence theory transfers.

## Key insight

A chain of learners who each infer a hypothesis from data and then
generate data from it is alternately sampling h given d and d given h.
That is a Gibbs sampler for the joint P(d|h)P(h). Its stationary
distribution has the prior as its marginal on h. The first learner's data
is "only a single piece of information, while the prior asserts its effect
on each iteration" (§4.1). What survives transmission is therefore what
the learners already expected, and the population's languages come to
mirror the learners' inductive biases.

## Assumptions

- **Assumption 1**: every learner uses the same learning algorithm and
  production algorithm. For Bayesian learners this means the same
  hypothesis space H and the same prior P(h).
- **Assumption 2**: discrete generations with one learner each, learning
  from the previous learner's data. Or, Assumption 2′ (§7): an unbounded
  population in continuous time, each learner learning from a random
  member of the population at the previous instant.
- **Assumption 3**: learners know the production distribution P_PA(d|h),
  so learning and production are consistent (the likelihood is the true
  production distribution).
- **Ergodicity** of the Markov chain (irreducible and aperiodic), which
  fails when some language is a sink. In the two-language example it
  fails only when the languages never agree (s = 0) and production is
  noiseless (ε = 0).
- H and D finite (note 1), "not a necessary assumption".
- **No selection**: the population result needs equal fitness f_j = 1.
  The authors warn that selection "could easily disrupt" the
  correspondence with statistical inference (§8.2).
- The prior is not read as innate language-specific constraint: it
  "collects together all of the factors affecting how easily a learner will
  come to entertain a particular hypothesis" (§3.1). The analysis is at
  Marr's computational level, not a claim about mechanism.

## Key results

- **Markov chains (Eqs. 9–11).** Summing out data gives a chain on
  hypotheses with q_ij = Σ_d P_LA(h_n = i | d) P_PA(d | h_{n−1} = j);
  summing out hypotheses gives a chain on data; grouping gives a chain on
  (h, d) pairs.
- **Two languages (Eqs. 14–15).** θ1 = q12 / (q12 + q21); second
  eigenvalue λ2 = 1 − q12 − q21, which sets the rate of convergence.
- **Sampling converges to the prior (Eqs. 25–30).** With P(h|d) as the
  learning rule, θ_i = P(h = i) satisfies θ = Qθ; the chain on data has the
  prior predictive P_PA(d) = Σ_h P_PA(d|h)P(h) as its stationary
  distribution (Eqs. 31–36). Holds for any production algorithm and any
  amount of data; the same holds if learners average over hypotheses
  rather than sample one.
- **Gibbs sampler (§4.2).** Iterated learning by sampling is a
  systematic-scan Gibbs sampler for P_PA(d|h)P(h), so convergence is
  geometric in n under standard results. The authors call this, to their
  knowledge, the first connection between MCMC and human cognition.
- **MAP as stochastic EM (§5.1).** Iterated learning with MAP learners is
  stochastic EM (one sample of the latent variable per iteration) in a
  model where the transmitted data are the latent variable and there are
  no observations. The stationary distribution should be approximately
  centred on the prior's maximum, with variance growing with the rate of
  change between generations. No explicit asymptotic result exists for
  discrete hypothesis spaces.
- **MAP with two languages (Table 1).** With prior α > 0.5 on L1,
  agreement s and noise ε: if ε < 1 − α, θ1 = (s + (1 − s)ε) / (s + 2(1 −
  s)ε) and λ2 = (1 − s)(1 − 2ε), independent of α. If ε > 1 − α, θ1 = 1
  and λ2 = 0. So a weak bias (α just above 0.5) and a strong one (α just
  below 1 − ε) give the same outcome: MAP learning can amplify weak
  biases.
- **Compositionality simulation (§6).** Four meanings and four utterances
  ({00, 01, 10, 11}); 4 compositional and 256 holistic languages (260
  hypotheses), prior α/4 on each compositional and (1 − α)/256 on each
  holistic; α ∈ {0.01, 0.5}, ε ∈ {0.01, 0.05}, m = 1 … 10 utterances per
  generation (Monte Carlo transition matrices for m > 4). Sampling: the
  long-run frequencies match the prior at every m; larger m only slows
  mixing (λ2 rises). MAP: with α = 0.01 compositional languages are never
  chosen (each is matched by a holistic language with the same mapping and
  higher prior mass); with α = 0.5 and m = 1 or 2 only compositional
  languages appear; holistic ones appear from m = 3, more at m = 10.
- **Populations (§7).** Under equal fitness, dp_i/dt = Σ_j q_ij p_j − p_i
  has the unique stable equilibrium p = θ, so the single-chain stationary
  distribution is also the long-run population share.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Iterated learning by posterior sampling has the shared prior as its stationary distribution over hypotheses, and the prior predictive over data | strong (proof), under Assumptions 1–3 and ergodicity | Eqs. 25–36 |
| C2 | Iterated learning by sampling is a Gibbs sampler on P(d\|h)P(h) | strong (identification) | §4.2 |
| C3 | Iterated learning by MAP is stochastic EM with no observations, so its stationary distribution concentrates near the prior's mode | moderate: the identification is exact, the "approximately centred" behaviour is borrowed from stochastic-EM results for other settings | §5.1 |
| C4 | Under MAP, the outcome depends on data amount and noise and can be the same for a range of prior strengths, amplifying weak biases | strong for the two-language case (closed form); illustrated, not proved, in general | Table 1, §6.2 |
| C5 | With sampling learners, a bottleneck is not needed for structured languages to emerge, but they emerge only if the prior favours them | strong under the model | §4.4, §6.1 |
| C6 | The single-learner chain's stationary distribution is the equilibrium of an unbounded equal-fitness population | strong (linear dynamics) | §7, note 6 |
| C7 | Anything transmitted by iterated learning, including "legends, religious concepts, and social norms", will come to match learners' inductive biases | weak: an extrapolation in the conclusion, not analysed | §8.5 |

## Method

Reduce iterated learning to a homogeneous finite Markov chain by summing
out data (or hypotheses), find the stationary distribution as the
eigenvector of the transition matrix with eigenvalue 1, and use the second
eigenvalue for the rate. For Bayesian learners, verify by substitution
that the prior (and the prior predictive) is stationary. Worked examples:
a two-language "Gavagai" case with closed forms, and a 260-hypothesis
compositionality case with numerically computed transition matrices.

## Concepts

- **iterated learning**: each learner forms a hypothesis from data
  produced by a learner who learned the same way, then produces data for
  the next.
- **learning algorithm P_LA(h|d) / production algorithm P_PA(d|h)**: the
  two conditional distributions that define one generation.
- **prior**: everything that makes a hypothesis easier or harder to adopt,
  read as "the amount of evidence that a learner would need to see in
  order to adopt a particular language" (§3.1).
- **bottleneck**: the finite amount of data passed between generations.
- **stability ratio**: mean q_ii for compositional languages over mean q_ii
  for holistic ones (§6.1).

## Connections

- **Kirby (2001), Brighton (2002), Smith, Kirby & Brighton (2003)**: the
  iterated learning model and its simulations of the emergence of
  compositionality, which the paper re-reads as MAP-like learners
  (minimum description length is MAP under a coding prior).
- **Nowak, Komarova et al. (2001–2003)**: the language dynamical equation;
  the paper's population result is its equal-fitness case.
- **Kirby, Smith & Brighton (2004)**: an earlier Bayesian framing (note 2).
- **Geman & Geman (1984); Celeux & Diebolt (1985)**: Gibbs sampling and
  stochastic EM.
- **[LIT-tmpe93h7](../literature.d/LIT-tmpe93h7.md)** (Kirby, Cornish & Smith 2008, read in [NOTE-tmppvy0t](NOTE-tmppvy0t.md)) is
  the laboratory version of the process. It cites this paper only within a
  block of model references and does not discuss priors. Its human chains
  show increasing structure and learnability, which is what this paper
  says either learning rule produces when the prior favours structure.
- **[LIT-tmp9f0fn](../literature.d/LIT-tmp9f0fn.md)** (Bartlett 1932): the paper does not cite Bartlett, but
  its closing extrapolation to legends is the claim Bartlett's serial
  reproduction of a folk tale was about: material drifts toward what the
  rememberer's culture makes expectable. This paper gives that a
  formal form for one class of learner. The connection is mine.

## Bearing on the record

- No existing THEORY covers iterated learning, cultural transmission or
  convergence to a prior (grep of theory.d on 2026-10-09). This reading
  produces [THEORY-tmp0w0cu](../theory.d/THEORY-tmp0w0cu.md): under posterior sampling, iterated learning
  converges to the shared prior, and the MAP case is where data amount
  matters. Its "what this does not say" carries the limits below.
- No instruction for machine-learning practice; not an anthology
  candidate.

## Limitations

- **Homogeneous learners.** Everything rests on all learners sharing one
  prior and one likelihood that matches production. Heterogeneous priors,
  or learners who learn from several teachers, are outside the analysis
  (§8.2 names multi-generation input as future work via stochastic EM
  variants).
- **No selection.** With fitness differences the population result and
  the statistical-algorithm correspondence may fail; the authors say so.
- **Which rule humans use is open.** The authors argue for sampling from
  probability matching but say the question "has not been explored in
  depth" for language (§8.4). The two rules give opposite answers on
  whether the bottleneck matters.
- **MAP results are rough.** Beyond two languages, the MAP case rests on
  stochastic-EM behaviour established for other settings and on one
  simulation.
- **The paper does not decide between innate and general-purpose
  explanations of universals**; it states both can use its results.
- **The compositionality example is shaped by H.** Note 5: the stability
  ratio's decline with m comes partly from holistic languages that
  duplicate compositional mappings, "rather than being a general trend".

## Open questions

- Do human transmission chains converge to an independently measured
  prior? A chain experiment in which each participant's prior is
  measured or manipulated would test C1 directly.
- How does the MAP stationary distribution depend on bottleneck size in
  general (the authors point to Dowman, Kirby & Griffiths 2006)?
- What happens between sampling and MAP (posterior raised to a power), and
  with heterogeneous priors in a population?
