---
status: Read
paper: LIT-1570
title: 'Athreya, Czuppon & Gokhale — The evolution of dependence and cohesion in incipient endosymbioses'
version: 1
history:
- version: 1
  date: '2026-10-27'
  note: >-
    Read in full from the bioRxiv preprint, version 2, posted 2025-05-31
    (doi:10.1101/2023.07.17.549359, CC BY-NC 4.0), fetched on 2026-10-27
    from biorxiv.org and extracted with pdftotext. This is not the
    version of record: the American Naturalist article (2025) was not
    reached. Version 2 carries the published title, thanks "two anonymous
    reviewers", and was posted before the journal's online date of
    2025-09-18, so it is probably close to the accepted text. Differences
    from the journal version are unknown. Version 1 (2023-07-19) had a
    different title and was not read. Read: the abstract, introduction,
    model, all four results subsections, the conclusions, Tables 1–3,
    the captions of Figures 1–5, and Supplementary Notes S1–S6 with the
    captions of Figures S1–S14 and Table S1. Figures were read from their
    captions and the text. The Mathematica notebooks and simulation code
    (Zenodo 15533092) were not run. Two checks were made here: that the
    sufficient condition on the collective carrying capacity gives 40 at
    the Figure 4 parameters, and the sign logic of the ephemeral-limit
    mutualism (Note S1.B).
date: '2026-10-27'
summary: >-
  An adaptive-dynamics model in which hosts, symbionts and host–symbiont
  collectives are three populations. Each partner has an "obligacy"
  (investment in collective rather than free-living growth) and an
  "adhesion" (investment in synchronized, collective reproduction). The
  faster-growing partner, the symbiont, becomes fully obligate first. What
  the host's obligacy then does depends on within-collective births and
  deaths: it stays, rises to full dependence, or falls to none. Obligacy
  rises only if the collective's carrying capacity is high enough;
  collective growth rate does not matter. Early on, dependence evolves
  ahead of cohesion. That last result holds for the trait mapping the
  authors chose, and their own Table S1 reverses it under the opposite
  mapping. The authors say the available data can neither confirm nor
  refute it.
---
<!-- inactive-ok-file: THEORY-tmpmjn0i THEORY-tmpyk1k6 — Proposed; filed from this reading -->
<!-- inactive-ok-file: QUESTION-277 THEORY-141 THEORY-418 THEORY-443 LIT-1568 LIT-1573 LIT-tmpi201p LIT-tmpt00nh CASE-173 CASE-177 — Open, Proposed or Deferred; the question, accounts, works and cases this reading is set beside, nothing here rests on them -->

# NOTE-tmp5hcss: Athreya, Czuppon & Gokhale — The evolution of dependence and cohesion in incipient endosymbioses

## Contribution

It treats the early evolution of an endosymbiosis as movement in a plane
with two axes. One is **mutual dependence**, how well the partners grow
alone against together. The other is **reproductive cohesion**, how often
they reproduce as a unit. Each axis is set by a trait in each partner.
Earlier models (Law & Dieckmann 1998; Nguyen & van Baalen 2020) let
populations grow exponentially, or held the host's traits fixed. This
one gives all three populations logistic growth and lets both partners'
traits evolve. Three results follow:
- carrying capacity, not growth rate, decides whether dependence starts
  at all;
- which partner becomes obligate first is set by population growth
  parameters;
- early on, dependence outruns cohesion.

## Key insight

Because the collective's reproduction aligns the partners' interests, the
partner that evolves faster gets there first. The symbiont, with the
larger population and faster growth, gives up free-living reproduction
first. At that point the host's own obligacy stops mattering in the base
model: "R₀(Ω̃_H, Ω_H, 1) = 1". What happens next depends on details of
life inside the collective. If partners die there more than they
reproduce, the host follows into full dependence. If they reproduce there
more than they die, the host is selected back to independence. So full
mutual dependence, the model's mark of a transition, is a
parameter-dependent outcome, not the default. In the authors' words, a
transition "is far from an inevitable outcome of the existence of a
higher level of selection".

## Assumptions

- **Three populations, logistic growth (Eq. 1).** Free hosts H, free
  symbionts S and collectives C, with growth rates f and carrying
  capacities K. Hosts and symbionts associate at rate a and dissociate at
  rate d, and dissociation returns exactly one of each.
- **Benefits only inside the collective.** A free host's growth does not
  depend on the symbiont's traits, and vice versa. There are no
  Lotka–Volterra cross terms.
- **A growth trade-off (Eq. 2, "default").**
  - f_H = r_H(1 − Ω_H) and f_S = r_S(1 − Ω_S): each partner's free growth
    falls with its own obligacy only;
  - f_C = r_C Ω_H Ω_S α_H α_S;
  - d = d₀(1 − α_H α_S): dissociation falls only when both adhesions are
    high;
  - a = a₀, a constant.

  Note S1 states the general constraint ∂a/∂αᵢ ≥ 0, but every analysis
  holds a fixed.
- **The symbiont is faster.** K_S > K_H and r_S > r_H throughout, so more
  symbiont mutants arise and the symbiont's traits evolve faster
  (Dieckmann & Law's canonical equation).
- **Collective carrying capacity is a constant.** It is not a function of
  the traits, on the view that the partnership opens a niche with a fixed
  capacity.
- **One symbiont unit per host, acquired once.** There is no growth of
  symbionts inside a host, no mixed infections, and no competition
  between free types and collectives.
- **Separation of timescales and small mutations**, with invasion judged
  by R₀ from the next-generation theorem. To suppress floating-point
  artefacts, the numerics accept a mutant only when R₀ > 1 + 10⁻⁷ (Note
  S6).
- **The definition of a transition.** A collective is an obligate
  endosymbiosis if the symbiont is intracellular, at least one partner is
  obligate, and the collective reproduces as a unit. A transition in
  individuality is "complete mutual dependence and reproductive
  cohesion", Ω = α = 1 for both partners. This follows van Gestel and
  Tarnita, for whom a life cycle marks an evolving entity.

## Key results

- **Obligacies alone (Fig. 2).** The symbiont's obligacy reaches 1 first.
  The host's then stops evolving, because once f_S = 0 the host's R₀ is
  exactly 1. The model therefore predicts neutral variation in host
  obligacy loci. At Ω_S = 1, the symbiont's equilibrium population
  exceeds its own carrying capacity, sustained by "backflow" from
  dissociating collectives. The authors call this counterintuitive: the
  partner that gave up independent reproduction is the more abundant.
- **Adhesions alone (Fig. 2).** The symbiont's adhesion reaches 1 first.
  The host's then rises to an evolutionarily stable value, and the pair
  drifts along a ridge of evolutionarily stable strategies near (1,1).
  The authors attribute the drift in their figures to floating-point
  error, though drift along a neutral ridge is what they predict for real
  populations. The ridge exists because adhesion helps hosts and
  symbionts at first, by raising collective growth, and hurts later, by
  cutting the dissociations that supply free individuals.
- **Births and deaths inside the collective (Eq. 6, Fig. 3, Table 2).**
  - **Death without birth** (d_H = d_S > 0): obligacies rise only from
    initial values above a threshold, which grows with the death rate.
    Once Ω_S = 1, the host also goes to 1, giving full mutual dependence.
  - **Birth without death** (b_H = b_S > 0): obligacies rise from (0,0)
    with no threshold. Once Ω_S = 1, the host's obligacy falls to 0, a
    one-sided dependence. There is then no fixed point: the symbiont goes
    extinct while host and collective populations grow without bound.
  - Adhesion results are unchanged, except that adhesions do not rise at
    high death rates (Fig. S8).
  - With Ω_S = 1, the equilibrium shows that the sign of b_S − d_S
    decides whether more host obligacy raises or lowers the collective's
    abundance (Eq. 7).
- **Carrying capacity, not growth rate (Fig. 4, Notes S3.B and S6).**
  - With K_C = 10, the traits stay at (0,0). With K_C = 50 or 500 they
    rise, and r_C (1 or 40) makes no difference.
  - Suggested sufficient condition: K_C > aK_HK_S/d. That is the
    collective population that association and dissociation alone would
    maintain. At the Figure 4 parameters it is 0.1·100·200/50 = 40, as
    checked here.
  - Perturbing a (0.01, 5) moves the outcome as predicted. The authors
    have not shown the condition is necessary.
  - K_C sets where adhesion ends up, but not obligacy.
  - With small r_C, the 10⁻⁷ acceptance cutoff hides real increases
    (Note S6), so "r_C does not matter" partly depends on the numerics.
- **Dependence before cohesion (exponential model, Fig. 5).**
  - Letting K_C → ∞ makes the invasion criterion exact and "separable":
    f̃_H(1 − d̃/(a f̃_C)) > f_H(1 − d/(a f_C)).
  - From this follow an optimization principle, no evolutionary
    branching, and monotone increase in all four traits.
  - Simulations then show Ωᵢ > αᵢ for both partners. Mutual dependence
    (Ω_HΩ_S) runs ahead of cohesion (α_Hα_S) until the trajectories hit
    the feasibility bound, where the collective grows without limit.
  - The authors' reason is that free growth depends on one's own
    obligacy alone, while dissociation depends on the product of both
    adhesions. A gain in adhesion is therefore "damped by the other
    adhesion".
- **The bias depends on that choice (Note S4.E, Table S1).** The appendix
  varies the two structural choices.
  - Free growth depending on one's own obligacy, with dissociation on
    both adhesions (the default): dependence-biased.
  - Free growth on both obligacies, with dissociation on one adhesion:
    biased towards cohesion.
  - Matched choices (own/one, or both/both): little or no bias. The slight
    bias in own/one is called an artefact.

  The robustness checks of Figure S14 vary other things, all within the
  default structure: additive instead of multiplicative effects,
  symmetric or tenfold-asymmetric growth parameters, and a higher d₀. The
  authors "arrived at case i-II from biological considerations, and we
  therefore make the associated prediction".
- **The empirical check (Table 3).** Ten symbioses are classified by
  dependence and transmission mode, after Estrela, Kerr & Morris (2016).
  The authors say the data are qualitative and a snapshot, and "does not
  allow us to confirm/refute the bias".
- **An ephemeral limit (Note S1.B).** When collectives are fleeting
  (ẋ_C ≈ 0), the model reduces to a symmetric Lotka–Volterra mutualism
  with cross-term coefficient a(d/(d − f_C) − 1). That is positive when
  d > f_C, a mutualism, and harmful to both when the collective grows
  faster than it dissociates. The sign logic was checked here.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | The partner with the faster population growth (more mutants) becomes fully obligate first, an instance of the Red King effect in which the collective, not a mutualism, aligns interests | moderate within the model | simulations (Figs 2, 4) and the canonical equation; the direction follows from the assumed K_S > K_H, r_S > r_H |
| C2 | Once the symbiont is fully obligate, the host's obligacy is neutral, or rises, or falls, depending on whether within-collective deaths or births dominate | moderate within the model | R₀ = 1 shown analytically for the base case; Fig. 3 and Eq. 7 for the others, with only b_H = b_S and d_H = d_S tested |
| C3 | Whether dependence and cohesion start to evolve depends on the collective's carrying capacity, not its growth rate; K_C > aK_HK_S/d suffices | moderate within the model | Fig. 4, Fig. S5; sufficiency supported numerically, necessity not shown; Note S6's cutoff caveat |
| C4 | Early in an endosymbiosis, mutual dependence evolves faster than reproductive cohesion, "even if investments in dependence and cohesion are uncorrelated" | weak as a claim about nature, moderate within the model | Fig. 5 under the default mapping; Table S1 shows the bias set by the mapping's structure and reversed under the alternative |
| C5 | Endosymbioses in nature are "more likely to be mutually dependent than cohesive" | weak | follows from C4 if the default mapping is right; Table 3 cannot test it, by the authors' account; indirect support cited (metabolic exchange is common, Black Queen dynamics, rapid experimental evolution of dependence) |
| C6 | A transition in individuality is not an inevitable outcome of a higher level of selection | moderate | C2 and C3: full mutual dependence and cohesion need particular parameters |

## Concepts

- **Obligacy (Ωᵢ)**: partner i's investment in collective over
  free-living growth, in [0, 1]. At 1 it cannot reproduce alone.
- **Adhesion (αᵢ)**: partner i's investment in synchronized reproduction.
  It raises the collective's growth and lowers dissociation.
- **Mutual dependence**: Ω_HΩ_S. The product is motivated by Ω's
  multiplicative effect on collective growth (footnote 1).
- **Reproductive cohesion**: α_Hα_S. It is "similar to, but stronger
  than, vertical symbiont transmission", since it requires the partners'
  replication to be coupled, as mitochondrial fission is to the cell
  cycle. The fig–wasp mutualism is the example of high obligacy with low
  adhesion.
- **Egalitarian transition**: one between unrelated partners (Queller),
  as against fraternal transitions such as multicellularity.
- **Red King effect**: in a mutualism, the slower-evolving partner gets
  the better share (Bergstrom & Lachmann 2003). Here the faster partner
  gives up independence first.
- **Feasibility bound**: d > f_C(1 + a√(K_HK_S/(f_Hf_S))). Beyond it the
  exponential model has no positive equilibrium and collectives grow
  without limit.

## Connections

The authors build on Law & Dieckmann (1998), Nguyen & van Baalen (2020)
and Estrela, Kerr & Morris (2016), from whom the two-dimensional framing
comes. None of these is in the record. Their Red King argument is
Bergstrom & Lachmann's. They place reductive genome evolution under
"other mechanisms such as Muller's ratchet" (LIT-1573, Moran 1996) "or
environment-induced redundancy", the latter citing the Black Queen
(LIT-1568, read in NOTE-tmp85ewc), McCutcheon & Moran (2010) and Husnik
et al. (2013, LIT-1569). These, they say, are "predicated on
endosymbionts occurring within the hosts". They cite symbiont
replacement in aphids (Chong & Moran 2018) for the host side of the
asymmetry. Frank's models of host control (LIT-tmpi201p, LIT-tmpt00nh)
are not cited.

## Bearing on the record

- **QUESTION-277.** The question rested its first two dimensions on this
  paper, and the reading partly bears that out. D and R are separate
  traits with separate dynamics, and the model gives conditions under
  which either stalls. But:
  - **The ordering result does not stand as a finding about
    endosymbiosis.** "Dependence evolves faster than cohesion" is fixed
    by the structural choice of how traits enter free growth and
    dissociation, and reverses under the alternative. The question's
    summary repeated the exchange's version, "even when investments in
    the two are uncorrelated". That is true of the model's traits, but
    the bias comes from how they act, not from correlation. A note goes
    on QUESTION-277.
  - **The model has no gene loss, no transfer and no host control.**
    Obligacy is a phenomenological trade-off between free and collective
    growth. The paper does not model the question's routes (Black Queen,
    drift, transfer), and says reductive evolution may be driven by
    "other mechanisms". So the paper speaks to D and R, not to G or C.
  - **One-sided dependence is a natural outcome.** Symbiont obligate and
    host free is what the birth-dominated case gives. It is consistent
    with the empirical asymmetry the paper notes: symbionts are more often
    obligate than hosts.
- **THEORY-141.** Here the collective's shared fate "aligns interests"
  through the Red King effect without any policing. That is a mechanism
  of alignment that THEORY-141's list (policing and similar) does not
  name. The model has no within-collective conflict, though, so it cannot
  test whether selection between collectives trumps selection within.
  The comparison is mine.
- **THEORY-443 and the transition criterion.** The paper's operational
  definition of a transition, full dependence plus full cohesion, giving
  a life cycle, is one concrete criterion for Darwinian individuality of
  a partnership. Under it, aphid–*Buchnera* (Table 3: mutually obligate,
  vertical) is a candidate, and the base model predicts the host's
  dependence will not follow unless collective mortality dominates. It
  offers a parameter to measure for CASE-173: the balance of births and
  deaths of partners inside the collective.
- **CASE-177 (*Hodgkinia*).** The model fixes one symbiont unit per host
  and so cannot represent lineage splitting or symbiont titre. The
  authors list symbiont growth inside a host as the extension most
  needed.
- Filed as THEORY-tmpmjn0i (the ordering result, with its dependence on
  the mapping) and THEORY-tmpyk1k6 (the asymmetry, and the outcomes
  after the symbiont becomes obligate). No instruction for
  machine-learning practice.

## Limitations

- **The headline result is a modelling choice.** Table S1 is the
  authors' own evidence that the dependence-first bias follows from the
  i-II structure, and Figure S14's "remarkably robust" checks never leave
  it.
- **The co-evolution result uses the exponential model**, trusted "only
  when the traits have low enough values". The bias is shown only for
  early trajectories, before the feasibility bound. Whether it survives
  later is named as open.
- **Within-collective rates are shared.** Only b_H = b_S and d_H = d_S were
  tested, though these rates decide the host's fate. Unequal and
  trait-dependent rates are named as the next study.
- **No test against data.** Table 3 is qualitative and cannot estimate
  the traits, as the authors say.
- **Constant a, constant K_C, one symbiont unit per host, no competition
  between free and collective types.** All are named by the authors as
  extensions.
- **Slips in the preprint.**
  - Figure 2's caption assigns obligacy and adhesion to panels
    differently from the text.
  - The adhesion ridge is described as connecting states written in Ω
    rather than α.
  - Table 2 reads "b_H = b_S = d_H = d_H".
  - Figure S14 labels two panels "(c)" and writes C_H, C_S for K_H, K_S.
  - The mutant-host equation of S14 has f̃_H x_H where y_H is meant.
  - The main text cites Eq. S14 for the within-collective model, which is
    S13.

  None of these changes a result. Whether the journal version corrects
  them is unknown.

## Open questions

- Which trait mapping is right? Whether a partner's free growth depends
  on its own obligacy or both, and whether dissociation needs both
  partners' adhesion, is an empirical question. The model's prediction
  turns on it. Measuring how symbiont loss affects host free-living
  growth, and how transmission fidelity depends on each partner, would
  bear on it.
- What are b and d, partner births and deaths inside the collective, in
  real symbioses? The authors call measuring them "imperative".
- Does the dependence-first bias survive to later evolutionary times?
- How would a mechanistic route to obligacy, such as gene loss under the
  Black Queen or the ratchet, change the trade-off curve f_i(Ω_i)? The
  authors cite Estrela, Morris & Kerr (2015) for accelerating benefits of
  function loss giving "obligate exploitation" instead of mutual
  dependence.
