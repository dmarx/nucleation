---
status: Read
paper: 'LIT-1137'
title: 'Krakauer et al. — The information theory of individuality'
version: 1
history:
- version: 1
  date: '2026-10-29'
  note: >-
    Read in full on 2026-10-29 in both versions. The version of record
    (Theory in Biosciences 139:209–223, 2020, CC BY) from Europe PMC's
    full text of PMC7244620
    (https://www.ebi.ac.uk/europepmc/webservices/rest/PMC7244620/fullTextXML),
    converted to text; the Springer PDF returned a bot page. The preprint
    from arXiv's own copy, v1 of 8 December 2014
    (https://arxiv.org/pdf/1412.2447, 17 pages). Read in each: all
    sections, the appendix on closure and sufficiency, the footnotes and
    the references; the 2020 figures from their captions only. Checked:
    the identities A* + nC = A + I(S_{n+1}; E_n) and A* − A = SI − CI, the
    expansions of A′* and A′ for an enlarged system, from which both
    measures are non-decreasing (THEORY-tmpx3lyj), and the closure ⇒
    sufficiency argument. The 2020 example (two logistic binary units)
    was computed by record script at four parameter settings
    (2026-10-29). The versions differ (see Connections).
date: '2026-10-29'
summary: >-
  Splits I(S_n, E_n; S_{n+1}) two ways, into A* = I(S_{n+1}; S_n) plus
  nC = I(S_{n+1}; E_n | S_n), or I(S_{n+1}; E_n) plus A = I(S_{n+1}; S_n | E_n),
  and in the 2020 version names A* organismal, A colonial and nC
  environmentally determined individuality, read through a partial
  information decomposition left unspecified. Both A* and A can only grow
  as variables move from environment to system, so they cannot by
  themselves find a boundary; the 2020 version says a size cost is
  needed and does not supply one. Illustrated on one two-unit system; no
  algorithm and no data.
---
<!-- inactive-ok-file: LIT-005 — Proposed; the critique this reading is compared with, cited as open -->
<!-- inactive-ok-file: LIT-1122 — Deferred; named as the slow-variable work both versions cite, nothing here rests on it -->

# NOTE-tmpypk9d: Krakauer et al. — The information theory of individuality

## Contribution

It proposes that individuals be found rather than assumed: an
individual is an aggregate that "propagates information from its past
into its future". For a system S and its environment E it decomposes the
one-step predictive information about the system and reads the terms as
kinds of individuality. The 2020 version adds a partial-information
decomposition of those terms, a worked two-unit example and the
admission that the measures cannot locate boundaries without a size
penalty.

## Key insight

The predictability of a system's next state can be credited to the
system first and the environment second, or the other way round. Credit
the system first and the system's own term is A*; credit the environment
first and it is A. The two orders differ by the shared minus the
synergistic information, so a system can score high on one and low on
the other, and the difference separates a self-maintaining organism from
a colony that persists only through interaction with its surroundings.

## Assumptions

- **A joint Markov process** (S_n, E_n) with kernels φ(e, s; s′) and
  ψ(s, e; e′), finite state sets (2020, §"The origin of information").
- **A partition given in advance.** The measures score a chosen
  system–environment split; finding the split is the open part.
- **Consistent measurements** over a time scale at which regularities
  show; the authors say the right scale "can [not] be known in advance".
- **A partial information decomposition** whose concrete measure is left
  open (2020, footnote 1): "we will use the decomposition as a
  conceptual framework".

## Key results

- **Two decompositions.** I(S_n, E_n; S_{n+1}) = A* + nC =
  I(S_{n+1}; E_n) + A, hence A* + nC = A + I(S_{n+1}; E_n) and
  A* − A = I(S_{n+1}; E_n) − nC, called non-trivial informational closure
  (2014) and environmental coding (2020).
- **PID form (2020, eqs. 2–5).** A* = SI + UI_S, A = CI + UI_S,
  nC = CI + UI_E, NTIC = SI − CI.
- **Closure implies sufficiency.** Under the Markov structure,
  nC = I(S_{n+1}; S_{n−1} | S_n) + I(S_{n+1}; E_n | S_{n−1}, S_n), so nC = 0
  forces I(S_{n+1}; S_{n−1} | S_n) = 0; closure is the stronger notion
  (appendix; Pfante et al. 2014 for the general case).
- **Enlarging the system.** Moving ΔS from E into S gives
  A′* = A* + I(ΔS_{n+1}; S_n | S_{n+1}) + I(S_{n+1}ΔS_{n+1}; ΔS_n | S_n) and
  A′ = A + I(S_{n+1}ΔS_{n+1}; ΔS_n | E′_n) + I(ΔS_{n+1}; S_n | E′_n ΔS_n S_{n+1}),
  so "both individuality measures can only grow or stay constant with
  increasing system size … Thus, they are not sufficient to detect the
  precise boundaries between individuals. In order to obtain precise
  boundaries we would need to impose a cost function—or regularizer—on
  system size" (2020). nC′ can move either way.
- **Example (2020, Figs. 2–3).** Two ±1 units with logistic updates in
  self-coupling α, cross-coupling β and interaction γ. The text says A
  and A* coincide at γ = 0 and high α, β, diverge as γ grows (A* falls,
  A rises), and that a correlated environment moves information from nC
  into A*.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | A* + nC = A + I(S_{n+1}; E_n) | strong | chain rule, checked |
| C2 | Informational closure implies sufficiency of the present state | strong | appendix, checked |
| C3 | A* and A are non-decreasing in the system's extent | strong | expansions, checked ([THEORY-tmpx3lyj](../theory.d/THEORY-tmpx3lyj.md)) |
| C4 | Boundaries need a size cost the measures do not contain | strong | follows from C3; stated in 2020 |
| C5 | A*, A and nC are three distinct forms of individuality | weak | interpretation; one two-unit example |
| C6 | Maximizing A* identifies "complex organisms in their environments" | weak | asserted; at odds with C3 unless the candidates have fixed size |

## Method

None implemented. The 2014 version proposes adding variables to the
system while A* or A rises and nC falls, stopping at the largest set
"no better at predicting its future than the previous largest set"; the
2020 version keeps the incremental expansion but says a regularizer is
needed and that finding the optimal partition is not its objective.

## Concepts

- **Organismal individuality A*** = I(S_{n+1}; S_n); in Krakauer and
  Zanotto 2006, "autonomy".
- **Colonial individuality A** = I(S_{n+1}; S_n | E_n); Bertschinger et
  al.'s autonomy.
- **Environmental determination nC** = I(S_{n+1}; E_n | S_n), the
  non-closure.
- **NTIC / environmental coding** = A* − A.
- **Informational closure**: nC = 0; the system predicts every influence
  of the environment on it.

## Connections

The two versions are different papers in places. The 2014 arXiv v1 has
the decompositions, the closure and expansion algebra and a stopping rule;
it calls the two readings "genomic" and "environmental determination" and
lists authors Krakauer, Bertschinger, Olbrich, Ay, Flack. The 2020 article
reorders authors (Flack before Ay), renames the readings, adds the PID
terms, the two-unit example, the size-cost sentence, and links to the
free-energy principle and to Biehl et al.'s agent detection. Both cite
Flack's slow-variable work ([LIT-1122](../literature.d/LIT-1122.md)) for coarse-graining as the route to
new levels. Bourrat's critique ([LIT-005](../literature.d/LIT-005.md), [NOTE-027](NOTE-027.md)) is of the 2020 measures.
Kolchinsky and Wolpert ([LIT-1149](../literature.d/LIT-1149.md)) cite the 2014 preprint.

## Bearing on the record

- **[QUESTION-115](../questions.d/QUESTION-115.md).** The LIT asked a reading to check A11's claim that A*
  and A do not decrease as the candidate is enlarged, and the size cost
  the paper says is needed. Both are confirmed, in the 2020 version only:
  the 2014 preprint makes the monotonicity claim but offers a stopping
  rule instead of a size cost. The check is filed as [THEORY-tmpx3lyj](../theory.d/THEORY-tmpx3lyj.md).
  The question's summary, which reports A11's reading, can be marked as
  read and confirmed. Proposed dated note below.
- **[CASE-101](../cases.d/CASE-101.md).** The case's arm A (common input) is where A* fails, as
  Bourrat argued and [THEORY-424](../theory.d/THEORY-424.md) holds. The reading adds that A, which
  conditions on the environment, scores the common-input arm near zero
  only if the common input is in E; the case should state which variables
  it puts in E for each arm, since all three measures are relative to
  that split.
- **[LIT-005](../literature.d/LIT-005.md), [NOTE-027](NOTE-027.md).** Bourrat's A* and A are the 2020 article's. His
  objection to nC as a measure of individuality is the article's own
  gloss: nC "quantifies the degree of environmental determinism", and the
  article does not offer it as individuality except by its heading.
- **[THEORY-424](../theory.d/THEORY-424.md).** Consistent: the measures are observational mutual
  informations, and the article nowhere intervenes.

No instruction for machine-learning practice; nothing for the anthology.

## Limitations

- **No algorithm, no data.** Both versions leave identification to future
  work.
- **PID unspecified**, so SI, UI and CI have no values; only the
  classical sums are computable.
- **The example's text over-reads the figures.** A record computation of
  the 2020 two-unit system with a random environment and γ = 0 gives
  A* = A = 0.998 bits at α = 5, β = 1, but A* = 0.189 and A = 0.311 at
  α = β = 5 (and at α = β = 3). A and A* coincide at γ = 0 when the
  self-coupling dominates, not "at high values of α_S and β_S" in
  general; with an independent environment, conditioning on it can only
  raise the system's own term.
- **Slips.** Both versions write the joint entropy as H(S; R) and say
  H(S|R) where they mean H(R|S); "Sn+" stands for S_{n+1} in the appendix;
  the 2020 caption of Fig. 3 reads "αE = 2βE = γE = 0" for what the text
  calls an environment with memory; Krakauer and Flack 2010 is listed
  twice.

## Open questions

- With a size cost, what boundary do A*, A and nC pick in [CASE-101](../cases.d/CASE-101.md)'s three
  arms, and do they disagree as A12 expected?
- Which PID makes the 2020 decomposition non-negative and well defined
  for these processes, and do the conclusions depend on it?
