---
status: Read
paper: 'LIT-1149'
title: 'Kolchinsky and Wolpert — Semantic information and autonomous agency'
version: 1
history:
- version: 1
  date: '2026-10-29'
  note: >-
    Read in full on 2026-10-29 from arXiv's own copy, v3 of 7 November
    2018 (https://arxiv.org/pdf/1806.08053, 21 pages), text extracted with
    pdftotext. Read: the abstract, §§I–VII, Appendices A and B, the
    captions of Figures 1, 2, B.3 and B.4 and the 146 references. Figures
    were read from captions and text only. Checked: the food-seeking
    example's stored semantic information (the coarse-graining
    {1}, {2,3,4}, {5} carries 1.371 bits of the 2.322), its efficiency
    (0.59) and thermodynamic multipliers (22.1/2.32 = 9.5;
    −13.7/2.32 = −5.9); the derivation of Appendix A's bound, which is
    approximate as stated. The authors' Python code was not run. The
    journal version (Interface Focus 8, 20180041), free at PubMed Central
    (PMC6227811), was not fetched: Europe PMC's full-text service
    returned a server error on 2026-10-29.
date: '2026-10-29'
summary: >-
  Defines a system's semantic information about its environment as the
  least syntactic information (initial mutual information, or transfer
  entropy over [0, τ]) that an intervention by coarse-graining the
  environment can leave while keeping the system's viability at τ
  unchanged, viability being the negative Shannon entropy of the system's
  state. Viability function, system–environment split, τ and initial
  distribution are the analyst's choices, which the paper concedes and
  proposes to fix by maximizing the measures. One five-location
  food-seeking toy; no theorem beyond 0 ≤ semantic ≤ syntactic.
---

# NOTE-tmpcwd0c: Kolchinsky and Wolpert — Semantic information and autonomous agency

## Contribution

It gives a formal, intrinsic-looking definition of "meaningful"
information for any physical system: the part of its correlation with
the environment that causally matters for the system's continued
existence. It defines two kinds (stored, from initial mutual information;
observed, from transfer entropy), an information/viability curve, a
semantic efficiency, semantic content of a state, and for stored
information a thermodynamic multiplier comparing the viability benefit
with the Landauer cost of acquiring the information.

## Key insight

Scramble the system–environment correlation and watch viability.
Scrambling by coarse-graining the environment as the system sees it
lets one strip correlations away gradually; the smallest amount of
correlation that still yields the actual viability is the meaningful
part, and what it correlates with is the content.

## Assumptions

- **A world split into system X and environment Y**, fixed over [0, τ],
  discrete finite state spaces, an initial joint distribution p(x₀, y₀).
- **Viability V = −S(p_{X_τ})**, plus internal entropies when states are
  macrostates (App. B). The authors call it exogenous: "the viability
  function is exogenously determined by the scientist analyzing the
  system".
- **Interventions by pre-garbling.** p̂^φ(x₀ | y₀) = p(x₀ | φ(y₀)) for a
  coarse-graining φ of Y; for observed information the system's update
  rule is coarse-grained the same way at each step, the environment's
  left alone.
- **First-order Markov, discrete-time dynamics** for observed
  information; time-inhomogeneous allowed.
- **Energetics ignored** in interventions and in the multiplier
  (§V A 3), which the authors flag.

## Key results

- **Stored semantic information (§V A).** S_stored = I_{p̂^opt}(X₀; Y₀),
  where p̂^opt minimizes I over φ subject to V(p̂^φ_{X_τ}) = V(p_{X_τ}).
  0 ≤ S_stored ≤ I_p(X₀; Y₀); η_stored = S/I ∈ [0, 1]. The optimal
  intervention need not be unique (redundant sources).
- **Thermodynamic multiplier.** κ = ΔV_tot/I_p(X₀; Y₀), with
  W_min = k_B T ln 2 · I as the cost of measurement; κ = η · ΔV/S.
- **Observed semantic information (§V B).** The same construction with
  Σ_t T(Y_t → X_{t+1}) in place of I(X₀; Y₀).
- **Example (§V A 4, App. B).** Five locations, agent at the centre with
  exact knowledge of the food's location, death macrostate of 100 bits'
  internal entropy, τ = 5: I = log₂ 5 = 2.32 bits, S_stored ≈ 1.37,
  η ≈ 0.6, ΔV ≈ 22.1 bits, κ ≈ 9.5; for an agent that flees the food,
  the same S and ΔV ≈ −13.7, κ ≈ −5.9.
- **Agency (§VI).** "A physical system is an autonomous agent to the
  extent that it has a large measure of semantic information", with
  decompositions, timescales and initial distributions to be chosen by
  maximizing such measures.
- **Appendix A.** p(X ∈ A) ≲ (log|X| − S)/(log|X| − log|A|) for a small
  viability set A.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Semantic information is bounded by the syntactic information it is drawn from | strong | the actual distribution is in the feasible set |
| C2 | The definition applies to any physical system | moderate | it is well defined for any discrete X, Y and τ once V is fixed |
| C3 | The definition is intrinsic to the system | weak | V, the split, τ and p are chosen by the analyst (§I B, §IV) |
| C4 | Negative entropy is a reasonable viability function | weak | Appendix A's approximate bound; the authors list its failures |
| C5 | Agency can be identified by maximizing semantic information | weak | proposed, not tried |
| C6 | Semantic information can misrepresent (negative value) and is asymmetric | moderate | the fleeing-agent example; the definition |

## Method

For stored information: enumerate coarse-grainings φ of Y, form
p̂^φ(x₀, y₀), run the dynamics to τ, record V and I, take the
information/viability curve and its optimum. Values are rounded to five
decimals to smooth the curve.

## Concepts

- **Syntactic information**: mutual information or transfer entropy.
- **Viability (value of information) ΔV_tot**: V(actual) − V(fully
  scrambled).
- **Viability-optimal intervention**: the most scrambled distribution
  with unchanged viability.
- **Semantic content of x₀**: p̂^opt(y₀ | x₀).
- **Semantic efficiency η**, **thermodynamic multiplier κ**.

## Connections

It formalizes the autonomous-agents tradition (Ruiz-Mirazo and Moreno,
Bickhard, Barandiaran et al., autopoiesis) and contrasts itself with
teleosemantics (Millikan, Godfrey-Smith) and utility-based value of
information. Its interventions are Blackwell-style garblings (Rauh et al.
2017). It cites Krakauer et al.'s individuality ([LIT-1137](../literature.d/LIT-1137.md)) as related
fitness-relevant information, and Touchette and Lloyd for entropy as a
control objective.

## Bearing on the record

- **[CLAIM-152](../claims.d/CLAIM-152.md).** The LIT records A10's caution that "the system's
  continued existence must be defined first, or the test is circular".
  The paper agrees with the first half and does not escape the second.
  Viability is a function the analyst picks, and the boundary of the
  system is an input; §VI then proposes to choose the boundary, the
  timescale and the initial distribution by maximizing semantic
  information, which is measured against that viability. A boundary
  found that way is relative to the chosen viability function, an
  instance of [CLAIM-152](../claims.d/CLAIM-152.md) with viability as the target. The paper also
  concedes that negative entropy does not track identity ("both a
  rhinoceros and a human have low entropy"), so "keeping existing" here
  means staying concentrated, not staying the same system. Proposed dated
  note below.
- **[LIT-1149](../literature.d/LIT-1149.md)'s own label.** The LIT says it is the likeliest source of
  the owner's half-remembered "useful information". The reading neither
  confirms nor rules that out: the paper's name for what it measures is
  "semantic information", and it lists "meaningful", "relevant",
  "functional" and "pragmatic information" as names others have used
  (footnote 1); "useful" is not among them. The idea, information that
  matters for staying in existence, fits the description.

No instruction for machine-learning practice; nothing for the anthology.

## Limitations

- **One toy example**, five locations, deterministic agent, two variants.
- **Choices carry the result.** Viability function, split, τ, initial
  distribution and the class of interventions are all the analyst's.
- **Errors and slips.** Appendix B writes the viability as
  V = S(p_{X_τ}) + Σ p(x_τ) S_int(x_τ), the total entropy without the
  minus sign that the definition (2) requires. It twice calls the
  semantic efficiency κ_stored (≈ 0.6) though κ is the multiplier. The
  main text starts the agent "in location 3 (the middle of the world)";
  Appendix B puts it at ⌊n/2⌋ = 2 for n = 5. Appendix A's bound is
  approximate: the derivation drops a term to reach the displayed form,
  which the text marks only by "≈". Eq. (10)'s text says S_stored "must be
  less than" the mutual information where it can equal it.

## Open questions

- Is there a viability function derivable from the dynamics alone (the
  attractor landscape the authors mention), which would remove the
  circularity?
- Does maximizing semantic information over splits pick out an agent in
  any system where the answer is known, rather than the whole world?
