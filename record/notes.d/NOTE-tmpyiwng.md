---
status: Read
paper: 'LIT-tmp6z0ji'
title: 'The Evolution of Cooperation'
version: 1
history:
- version: 1
  date: '2026-10-02'
  note: >-
    Read in full (JSTOR printout of Science 211: 1390–1396 on Axelrod's
    University of Michigan page; text extracted with PyMuPDF). Summary,
    all sections, and notes 1–42 read. The payoff inequalities for ALL D
    and for alternating D/C against TIT FOR TAT lost their right-hand
    sides in extraction; they are reconstructed here from the payoff
    streams the text states, and agree with condition (1), which survived.
    Fig. 1's value for S did not survive extraction.
date: '2026-10-02'
summary: >-
  TIT FOR TAT won Axelrod's two tournaments (14 entries plus random, 200
  moves; 62 entries, expected 200 moves) and went to fixation in an
  ecological replay. Against it, only ALL D or alternation need be
  checked, so no strategy does better iff w ≥ (T−R)/(T−P) and
  w ≥ (T−R)/(R−S). ALL D is stable for all w; kinship or a cluster with
  enough in-cluster interactions lets reciprocity in, and a nice stable
  strategy resists clusters. ALL C ties with TIT FOR TAT, so stability is
  neutral, not strict.
---

# NOTE-tmpyiwng: The Evolution of Cooperation

## Contribution

1. A probabilistic treatment of repeated interaction in biology: after each
   move the same pair meets again with probability w.
2. An account of the whole "chronology" of cooperation: robustness among
   many strategies, stability once established, and initial viability in
   an asocial population.
3. Applications at the microbial level, including speculative ones on
   disease and chromosomal nondisjunction (the authors' own list, p. 1391).

## Key insight

Defection is the only solution of the one-shot game and of a game of
known length, but when the end is uncertain a strategy that cooperates
first and then copies its partner cannot be beaten once established,
provided the future matters enough. Getting there from universal
defection needs a foothold: relatives, whose payoffs are partly shared, or
a cluster of reciprocators who mostly meet each other.

## Assumptions

- **Game.** Two-player Prisoner's Dilemma with T > R > P > S and R > (S + T)/2, payoffs in fitness; numerical values R = 3, T = 5, P = 1 in the tournaments (Fig. 1).
- **Continuation.** A fixed probability w that the pair meets again; payoffs discounted by w^(n−1). Choices simultaneous and discrete, said to be equivalent for most purposes to continuous or sequential interaction (note 21).
- **Recognition.** Players can recognize a previous partner and remember at least the last move.
- **No commensurability** of the two sides' payoffs is needed, so host–symbiont pairs qualify.
- **Clustering.** A fraction p of a cluster member's interactions are with other members; the cluster is a negligible share of the residents' interactions.

## Key results

- **Robustness.** First tournament: 14 entries and a random strategy, round robin, 200 moves; TIT FOR TAT (Rapoport) scored highest. Second: 62 entries from six countries, expected length 200 (w = .99654); TIT FOR TAT won again. Its success is attributed to being nice, provocable and forgiving. In an ecological replay it displaced all others and went to fixation.
- **Stability.** Against TIT FOR TAT the best reply is either ALL D or alternation of D and C. TIT FOR TAT v. itself earns R/(1 − w); ALL D earns T + wP/(1 − w); alternation earns (T + wS)/(1 − w²). Hence no strategy does better than TIT FOR TAT iff w ≥ (T − R)/(T − P) and w ≥ (T − R)/(R − S) (condition 1).
- **ALL D** is evolutionarily stable for every w.
- **Initial viability.** Kinship: reckoning payoffs in inclusive fitness can remove T > R and P > S, so cooperation can begin between relatives and spread as conditionality is acquired. Clustering: a cluster of TIT FOR TAT earns p[R/(1 − w)] + (1 − p)[S + wP/(1 − w)], which beats ALL D's P/(1 − w) for large enough p and w.
- **Ratchet.** A nice strategy that is evolutionarily stable cannot be invaded by a cluster of any other strategy.
- **Applications.** Fig wasps and figs (trees abort figs whose wasps under-pollinate), cleaner mutualisms tied to fixed sites, territorial birds that tolerate neighbours' song more than strangers', face recognition and prosopagnosia, symbionts turning parasitic when a host sickens or ages, and two labelled speculations (cancer onset, maternal-age nondisjunction).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | TIT FOR TAT is robust in a variegated environment | moderate | two tournaments with submitted strategies and an ecological replay; the environment is whatever was submitted |
| C2 | TIT FOR TAT is evolutionarily stable iff condition (1) holds | moderate as "no strategy does better"; weak as strict ESS | the reduction to ALL D and alternation is sound; ALL C ties, so stability is neutral |
| C3 | ALL D is evolutionarily stable for all w | strong | one-line argument |
| C4 | Kinship or clustering can establish reciprocity from ALL D | strong for clustering (explicit payoff), moderate for kinship (verbal) | Initial Viability section; formal proofs referred to Axelrod's forthcoming APSR paper (note 19) |
| C5 | A nice ESS resists invasion by clusters | strong | weighted-average argument |
| C6 | Symbionts should turn parasitic as w falls; nondisjunction may be chromosomal defection | speculation, labelled so | Applications |

## Concepts

- **Nice strategy** — never the first to defect.
- **Robustness / stability / initial viability** — the three questions the paper separates.
- **Evolutionarily stable** — here, "cannot be invaded by a rare mutant adopting a different strategy", applied as "no mutant does better".

## Connections

- **Trivers 1971** ([LIT-tmppstp9](../literature.d/LIT-tmppstp9.md)) is the "pioneer account" of reciprocation; Hamilton had given Trivers the Prisoner's Dilemma framing.
- **Hamilton 1964** ([LIT-tmp17vtr](../literature.d/LIT-tmp17vtr.md)) supplies the kinship route to initial viability; note 3 cites Part I.
- **Maynard Smith & Price 1973** ([LIT-tmpex4cg](../literature.d/LIT-tmpex4cg.md)) supply the ESS concept (note 11), and note 16 points to their contest model as another game with gains for cooperation.
- **Alexander** is cited (note 27) for uncertain paternity, not for moral systems.
- **Nowak 2006** ([LIT-tmpbmh7b](../literature.d/LIT-tmpbmh7b.md)) restates direct reciprocity as w > c/b for a donation game and reports TIT FOR TAT's weakness under error.

## Bearing on the record

- **Exchange domain.** Grounded: reciprocity is stable only with retaliation, recognition, and a sufficient chance of meeting again.
- **Kin domain.** Used, not added to: kinship is the starter.
- **Group domain.** Clustering is a population-structure mechanism, not coordination for mutual benefit; it does not ground MAC's group domain.
- **Other MAC domains.** Not grounded. The paper is not about morality.
- **[LIT-101](../literature.d/LIT-101.md).** The w of condition (1) is the formal content of the "shadow of the future" behind the delay-of-gratification premise in moral disciplining ([NOTE-132](NOTE-132.md), A1).
- **No THEORY is indicated.** No instruction for ML practice.

## Limitations

- Strategies are deterministic and error-free; noise is not considered.
- The tournament environment is the set of strategies people submitted.
- Stability is shown against single mutants and clusters, not against neutral drift followed by invasion.
- Formal proofs are deferred to another paper.

## Open questions

- Is TIT FOR TAT, or any pure strategy, stable once neutral mutants such as ALL C can drift in? (Answered in the negative by Boyd & Lorberbaum 1987, not in the record.)
- Does w measurably fall with a partner's illness or age, and does cooperation fall with it, as the Applications predict?

## Corrections

- none to a seeded skim (there was no seed)
- **"Evolutionarily stable" is neutral stability here.** The proof establishes that no strategy does better than TIT FOR TAT against TIT FOR TAT. A strategy that always cooperates does exactly as well, so by Maynard Smith and Price's two-part definition ([LIT-tmpex4cg](../literature.d/LIT-tmpex4cg.md)) TIT FOR TAT is not strictly an ESS. Boyd & Lorberbaum (1987, DOI-10.1038/327058a0) proved that no pure strategy is evolutionarily stable in the repeated Prisoner's Dilemma; checked on Crossref, not read.
