---
number: 810
status: Read
formerly:
- NOTE-tmpttt5h
paper: LIT-939
title: 'Vilone and Polizzi — Opinion misperception and the emergence of silence'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from the publisher's open-access PDF (PLOS ONE,
    CC BY, journals.plos.org "printable" file, 17 pages), text extracted
    with pdftotext: abstract, introduction, both models with their
    results, discussion and the reference list. Equation 3, which the
    PDF extraction garbles, was read from the article's JATS XML on the
    same site. The figures were read from their captions and the text
    that reports them; no supplementary file (the simulation code) was
    opened.
date: '2026-10-14'
summary: >-
  In two agent-based models on scale-free networks, agents' private
  beliefs are fixed and only what they say changes. A small hard-core
  minority placed on nodes of a chosen degree makes the expressed and
  locally perceived opinion far more minority-leaning than the beliefs,
  mainly by driving 55–60% of agents, almost all of the majority, into
  silence. The network's direct effect on perception is small and not
  even of constant sign. Simulation only, with no empirical validation.
---
<!-- inactive-ok-file: CLAIM-192 — Proposed; the thesis this reading bears on, named and not leaned on, and the account filed from this reading -->

# NOTE-810: Vilone and Polizzi — Opinion misperception and the emergence of silence

## Contribution

The paper separates two sources of opinion misperception in a network:
the "exogenous" one, where heavily connected nodes are over-represented
among everyone's neighbours (the friendship paradox), and the
"endogenous" one, where agents change what they express. With beliefs
held fixed, it finds the first small and the second large. In the
second model the large effect comes almost entirely from the majority
falling silent, not from anyone switching sides.

## Key insight

A community's public face can come apart from what its members believe
without any member changing a belief. If agents may stay silent, and do
so whenever their weighted surroundings do not clearly agree with them,
silence cascades. The few who never go quiet then make up a far larger
share of what anyone hears.

## Assumptions

- **Fixed beliefs.** Each agent's private belief b_i = ±1 never changes.
  The authors say this models expression and "not … changes in beliefs",
  and may "lead to observe more extreme dynamics" than when beliefs
  can move.
- **Binary opinions,** with a third expressed state ω_i = 0 (silence).
- **Topology.** Scale-free networks, N = 5000, P(k) ∝ k^−λ with λ = 2.2
  ("Twitter-like"), plus a check at λ = 1.5. Molloy–Reed generation,
  minimum degree 2, maximum ⌊√N⌋.
- **The hard-core minority.** Agents with b = −1 and σ = 1 are placed on
  every node of degree K_c, and only there. The rest have b = +1 and σ
  drawn uniformly from [0, 1]. So the minority's size and connectedness
  are not varied separately: high K_c means few, well-connected
  minority agents.
- **"Charisma" is degree.** The influence of j on i is
  A_i^j = deg(j)/deg(i), by stipulation.
- **Bounded rationality.** Agents see only their neighbours' expressed
  opinions and take the majority among them as the opinion climate.

## Key results

- **Model 1 (pp. 3–7).** With probability σ_i an agent expresses its
  belief, and otherwise ω_i = sign(Σ_{j∈Γ_i} ω_j). Silence occurs only
  before any neighbour has spoken.
  - The average expressed opinion ⟨ω⟩ is below the average belief ⟨b⟩
    for every K_c.
  - The local climate r = ⟨Δ_i⟩, the mean of each agent's neighbours'
    average expressed opinion, is below ⟨ω⟩. This topological distortion
    is "rather small (at most around 15% for K_c = 10)".
  - At K_c = 3 (hard-core share ≈ 18%) agents observe an average opinion
    "slightly less than 0.2" against an average belief "around 0.67".
  - "Topology itself contributes only partially to opinion
    misperception … most of the phenomenon is due to the mismatch
    between agents' expressed and private opinions."
  - As K_c grows all curves tend to 1, because the minority vanishes.
- **Model 2 (pp. 7–11).** Each agent picks ω_i ∈ {−1, 0, +1} to maximise
  G(ω_i) = −| (σ_i b_i + Σ_{j∈Γ_i} A_i^j ω_j) / (|Γ_i| + 1) − ω_i |,
  where |Γ_i| ≡ Σ_{j∈Γ_i} |ω_j| counts the neighbours who are not silent.
  It picks the expressed value nearest a weighted mean of its own
  belief and its neighbours' expressions, so silence wins whenever that
  mean lies between −1/2 and +1/2.
  - Expressed and locally perceived opinion stay below the belief level
    and reach a plateau as K_c grows. Model 1 had approached the belief
    level instead. "Even when being of a negligible number,
    well-connected minorities are able to sway the global opinion
    towards their side."
  - The shift "is not due to majoritarian agents publicly aligning to
    the opinion of the minority, but to majority's choice of staying
    silent." About 55–60% of agents, almost all with positive beliefs,
    end silent, "regardless of K_c" (Fig 3).
  - Silenced agents per hard-core agent rise superlinearly with K_c,
    fitted as ∝ K_c^ν with ν ≈ 2.1 (Fig 4). At K_c = 2 the minority is
    about 35% and each member silences fewer than 2 agents. At K_c = 20
    it is under 0.1% and each silences about 150, "much more than their
    neighbors". The exponent is close to λ because the silent fraction
    is roughly constant while the minority's size falls as K_c^−λ.
  - Here the locally perceived opinion is closer to the true beliefs
    than the global average expressed opinion. The direct topological
    effect is "besides small, also non-universal".
  - λ = 1.5 gives qualitatively the same picture (Fig 5).
- **Discussion (pp. 12–13).** The silencing "emerges regardless of the
  network position or size of minoritarian agents": numbers compensate
  for low centrality and centrality for small numbers. The majority and
  minority swap places in expressed opinion only when the minority
  exceeds about 30%. The authors note that this is close to Centola and
  Baronchelli's tipping point. Ross et al.'s bot model also reports
  50–60% silenced.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | With beliefs fixed, the expressed and perceived opinion of a group can be far more minority-leaning than its beliefs | moderate | both models, Figs 1–3; simulation only |
| C2 | The main driver in model 2 is the majority's silence, not conversion of expression | moderate | Fig 3 |
| C3 | The network's direct, friendship-paradox distortion of local perception is small and of no fixed sign | moderate | r − ⟨ω⟩ in both models, Figs 1, 2 and 5 |
| C4 | The silenced fraction (55–60%) is roughly independent of the minority's degree and size | moderate | Fig 3; a single network family, one weighting rule |
| C5 | A small vocal minority weakens a majority's public expression but overturns it only above roughly 30% | weak | one sentence in the Discussion, no figure isolates it |
| C6 | Social media's degree heterogeneity "can promote" silencing in real online systems | weak | the authors' extrapolation; no empirical test |

## Method

Asynchronous random-sequential updates, with N updates making one time
unit. Model 1 results are averaged over 10,000 realisations and model 2
over 5,000. The state variables are ⟨b⟩, ⟨ω⟩ and r. Misperception is
⟨b⟩ − r, the topological contribution is r − ⟨ω⟩, and the private–public
mismatch is ⟨b⟩ − ⟨ω⟩ (Table 1).

## Concepts

- **Opinion misperception.** "The wrong evaluation by community's
  members of the real distribution of opinions or beliefs about a given
  topic."
- **Hard-core (HC) agents.** After Noelle-Neumann, people who "stick to
  their opinion regardless of the prevailing opinion climate". Here,
  b = −1 and σ = 1.
- **Exogenous vs endogenous misperception.** Exogenous means from
  network position alone ("illusion of majority"). Endogenous means from
  agents' decisions about what to express.
- **Spiral of silence.** The cascade in model 2, in which agents whose
  surroundings are silent or opposed fall silent and so silence others.

## Connections

The paper adapts Merdes's model of unpopular norms (agents minimise the
gap between perceived surroundings and private belief) and sets itself
against Lerman et al.'s "majority illusion", whose topological effect it
finds small once agents interact. Noelle-Neumann's spiral of silence and
Miller and Prentice's pluralistic ignorance are the theories it
formalises. It cites Ross et al. on social bots for an independent
55–60% silenced figure.

## Bearing on the record

- **[QUESTION-047](../questions.d/QUESTION-047.md).** The paper bears on the question, but not in the form
  the question asks. Nothing in the model is a belief the community
  settles on: beliefs are fixed by construction, and what changes is
  expression. What it supplies is a community-level mechanism by which
  the community's *apparent* opinion, which is all any member can
  observe, comes apart from every member's belief. The structural
  variable is the option of silence together with degree-weighted
  influence. That is relevant to [QUESTION-047](../questions.d/QUESTION-047.md)'s "which community-level
  mechanisms", and it is filed as [THEORY-242](../theory.d/THEORY-242.md). It does not show
  sound inquirers *settling on* a belief, and the agents are not
  inquirers: they do not reason about evidence at all.
- **The LIT's seeded claim, checked.** [LIT-939](../literature.d/LIT-939.md)'s body says "the
  community comes to appear to hold a belief that its members do not …
  The outcome is set by structure, not by any member's reasoning." The
  first half holds, with the qualifier that the minority opinion becomes
  more prominent and does not become the majority unless the minority
  exceeds about 30%. The second half needs correcting. The paper's own
  finding is that the *direct* structural (topological) effect is small,
  and that the bias is mainly "endogenous", due to the agents'
  decision rule. Structure matters through who influences whom (A_i^j)
  and through the cascade, not through network geometry alone.
- **The LIT summary's "few, well-connected, charismatic agents".** This
  repeats the abstract, but the body finds the silencing "regardless of
  the network position or size" of the minority. At low K_c a large,
  poorly connected minority produces the same silent fraction.
- **[CLAIM-192](../claims.d/CLAIM-192.md)** (a multi-session argument's thesis moving with no
  participant arguing for it). This is an analogue only, and a weak one:
  what moves here is what is said, not a thesis anyone holds.
- No instruction for machine-learning practice; nothing for the
  anthology.

## Limitations

- Simulation only. The authors say the model "should also be validated
  with empirical data".
- Beliefs cannot change, so the result says nothing about whether
  silence would in time shift beliefs.
- A single decision rule. "Implementing different rules may lead to
  different macroscopic outcomes."
- The minority's number and degree are varied together, never apart.
- "Charisma" is identified with degree by stipulation.
- How hard-core agents are kept from falling silent in model 2 is not
  said. With σ = 1 they are still subject to G, and a hard-core agent
  surrounded by speaking majority neighbours would minimise G at 0 or
  +1. The text describes them as always expressing −1.

## Open questions

- Do surveys of private against expressed opinion on a real platform
  show a silent majority of the size the model predicts? The authors
  name this test.
- Does the silent fraction stay near 55–60% under other influence rules,
  multi-level opinions, or beliefs that move?
- Does revealing the true distribution of beliefs stop the cascade? The
  authors propose testing this intervention.
