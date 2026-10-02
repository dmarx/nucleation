---
number: 345
status: Read
formerly:
- NOTE-tmp7cyl2
paper: 'LIT-411'
title: 'Chalmers — Could a large language model be conscious?'
version: 1
history:
- version: 1
  date: '2026-10-02'
  note: >-
    Read in full (arXiv:2303.07103 v3, the Boston Review text, 17 pp.;
    text extracted with PyMuPDF). Every section, all 33 footnotes and the
    July 2023 Afterword were read. The v1 draft (4 March 2023, a talk
    transcript with slides) was read for its conclusions and notes only,
    to record what changed. The NeurIPS video and the Boston Review web
    page were not seen. The surveys in fn 30 (Francken et al., which the paper spells
    "Frankel"; Bourget & Chalmers) were not checked against their sources, and their figures
    are reported as the paper gives them.
date: '2026-10-02'
summary: >-
  Asks for a feature X that indicates LLM consciousness or its absence.
  Self-report is fragile and trained in. Conversation and general
  intelligence give some limited reason. Six obstacles stand against it:
  biology, senses and embodiment, world and self models, recurrence, a
  global workspace and unified agency, the last three strongest, all but
  biology temporary. On mainstream assumptions, with at least 1/3 credence
  per requirement, that gives under 10% for current LLMs and 25% or more
  for conscious LLM+ systems within a decade. The numbers are illustrative,
  biology is set aside rather than answered, and the twelve "challenges"
  are offered as roadmap or red flags.
---
<!-- inactive-ok-file: THEORY-023 THEORY-043 — Proposed; this reading says how the paper bears on those accounts, and does not lean on them -->

# NOTE-345: Chalmers — Could a large language model be conscious?

## Contribution

The paper gives the LLM-consciousness question a usable form. Instead of
intuitions about chatbots, it asks for a feature X with two defended
premises: LLMs have or lack X, and having or lacking X makes consciousness
probable or improbable. It then runs the strongest candidates through that
form. Its two original contributions are the classification of objections
as temporary or permanent, and the "theory-balanced" credence calculation.
That calculation became the method of the indicator-property report
([LIT-056](../literature.d/LIT-056.md)). It adds no evidence about any model.

## Key insight

Almost every reason to deny consciousness to current LLMs is a missing
architectural feature that someone is already building: recurrence,
memory, a workspace, a body, a self model, a single agent. So the case
against current LLMs is much stronger than the case against their
successors. Only biology is a permanent objection, and that is the one the
paper sets aside.

## Assumptions

- **Consciousness is subjective experience**, in Nagel's sense, and is real,
  not an illusion (§1). "That's a substantive assumption."
- **Mainstream views in the science and philosophy of consciousness.**
  Chalmers's own views (the hard problem, panpsychism) are said not to play
  a central role. Fn 29: his views "lean somewhat more to consciousness
  being widespread".
- **Substrate.** He has argued that biological requirements are "a sort of
  biological chauvinism" ("silicon is just as apt as carbon"), but sets
  the question aside for the body of the paper and gives it at least 1/3
  credence in the numbers.
- **Independence**, for the arithmetic only, explicitly false: "Of course
  the factors are not independent, which drives the figure somewhat
  higher" (§4).
- **Training versus post-training processing** (§3, world models). A
  system trained to minimise prediction error may use world models in
  processing. The analogy is evolution, which maximises fitness and
  produces eyes and wings.

## Key results

All are informal arguments and illustrative credences. There are no
experiments or proofs.

- **Evidence for, in X-form (§2).**
  - *Self-report*: LaMDA's reports are reversed by a one-word change of
    prompt in GPT-3 (Berkowitz). The model was trained on human talk about
    consciousness, and "the fact that it has learned to imitate those
    claims doesn't carry a whole lot of weight". Schneider and Turner's
    test needs a system not trained on the material.
  - *Seems-conscious*: weak, given ELIZA and the attribution literature.
  - *Conversational ability*: matters only as a sign of general
    intelligence.
  - *General intelligence*: domain-general use of information is "often
    regarded as one of the central signs of consciousness". Overall, no
    strong evidence, but "some limited reason".
- **Evidence against (§3).**
  - *Biology*: contentious, set aside.
  - *Senses and embodiment*: Chalmers doubts they are required (a "pure
    thinker" could have cognitive consciousness). Text training may give
    some grounding (Pavlick and colleagues). Multimodal and virtually
    embodied LLM+ systems answer the objection anyway.
  - *World and self models*: whether LLMs have them is empirical. Othello
    probing (Li et al.) gives "some evidence". Self models are "especially
    limited".
  - *Recurrent processing*: transformers are "almost entirely
    feedforward". The replies are limited recurrence via recirculated
    outputs, the possibility of feedforward consciousness, and recurrent
    LLMs (LSTMs, external memory).
  - *Global workspace*: a high-capacity system may not need a
    limited-capacity workspace. Multimodal LLM+ systems with a
    low-dimensional interface between modules "look a lot like" one
    (Perceiver IO, after Juliani, Kanai and Sasai; Goyal and Bengio).
  - *Unified agency*: "maybe the deepest". LLMs are "chameleons" without
    stable goals. The replies are that disunity is compatible with
    consciousness (dissociative identity), that one LLM may host "an
    ecosystem of multiple agents", and that agent models trained on one
    individual could be unified.
  - *Assessment*: biology and grounding rest on contentious premises, world
    models on unobvious ones. Recurrence, workspace and agency are the
    strongest. "For all of these objections except perhaps biology … the
    objection is temporary rather than permanent."
- **Credences (§4, v3).** At least 1/3 credence each that biology, sensory
  grounding, self models, recurrence, workspace and unified agency are
  required. If independent, a system lacking all six has under 1/10
  chance of being conscious, since (2/3)⁶ ≈ 0.088. Dependence pushes the
  figure up and unknown X's push it down: "somewhere under 10 percent".
  For LLM+ systems: over 50% that sophisticated ones with all these
  properties exist within a decade, and at least 50% that they would be
  conscious, so "25 percent or more".
- **Theory-balanced approach (fn 30).** A survey of consciousness
  scientists has just over 50% accepting or finding promising global
  workspace theory, just under 50% local recurrence, and just over 50%
  higher-order and predictive-processing theories. A 2020 PhilPapers
  survey has 3% accepting or leaning toward current-AI consciousness and
  39% toward future-AI consciousness. Chalmers reads these as supporting a
  collective credence above 1/3 for each of workspace, recurrence and self
  models, and at least 1/3 for biology.
- **Twelve challenges (§4).** 1 benchmarks; 2 theory; 3 interpretability;
  4 ethics; 5 perception-language-action models in virtual worlds; 6 world
  and self models; 7 memory and recurrence; 8 global workspace; 9 unified
  agent models; 10 describing untrained features of consciousness; 11
  mouse-level capacities; 12 "If that's not enough for conscious AI:
  What's missing?".
- **Afterword (July 2023).** GPT-4 is "a significant advance along some of
  the dimensions", which does not change the analysis "in any fundamental
  way" but may shorten timelines.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | LLM self-reports are weak evidence of consciousness, because they are fragile and trained on human reports | moderate | prompt-reversal example (Berkowitz); training-corpus argument §2 |
| C2 | General intelligence gives some limited reason to take LLM consciousness seriously | weak | appeal to what consciousness researchers "often" regard as a sign; no theory applied |
| C3 | Recurrence, a global workspace and unified agency are the strongest current obstacles | moderate | §3 survey of theories; plausibility judgements |
| C4 | All obstacles except perhaps biology are temporary | moderate as a claim about research programmes; asserted for timelines | existence of simple systems with each X (LSTMs, Perceiver IO, agent models) |
| C5 | It is reasonable to give under 10% credence to current LLM consciousness on mainstream assumptions | weak (illustrative) | 1/3 per factor, independence assumed and disclaimed; "specious precision" |
| C6 | It is reasonable to give 25% or more credence to conscious LLM+ systems within a decade | weak (illustrative) | product of two stipulated 50% credences |
| C7 | Biological requirements are a sort of chauvinism | assertion here | cites his earlier work; not argued in this paper |
| C8 | A theory-balanced approach, weighing theories by expert acceptance, can give collective credences for AI consciousness | proposal | fn 30; the conversion from "accept or find promising" to credence is left as "further work" |
| C9 | Training to minimise prediction error can produce world models in processing | moderate as a possibility; empirical status open | evolution analogy; Othello probing as "some evidence" |

## Concepts

- **Consciousness / sentience** — subjective experience, "something it's
  like" (Nagel). Used as rough equivalents; "sentience" is set aside as
  more ambiguous (§1).
- **Dimensions of consciousness** — sensory, affective, cognitive and
  agentive experience, and self-consciousness (§1).
- **LLM+ / extended large language model** — an LLM with added modalities,
  actions or tools. Not the extended mind.
- **Feature X** — the regimented form of an argument for or against (§§2–3).
- **Temporary versus permanent objection** — whether a research programme
  could supply the missing X (§3).
- **Theory-balanced approach** — credences over several theories'
  predictions, weighted by the evidence for or acceptance of each (fn 30).
- **Agent model** — an LLM trained or prompted to model a single agent
  (§3).

## Connections

Birch's theory-heavy, theory-neutral and theory-light approaches ("The
Search for Invertebrate Consciousness", 2021) are the frame fn 30 extends.
Birch's later manifesto ([LIT-111](../literature.d/LIT-111.md), [NOTE-183](NOTE-183.md)) turns the self-report worry into
the gaming problem. Butlin, Long et al. ([LIT-056](../literature.d/LIT-056.md), [NOTE-052](NOTE-052.md)) is cited in fn
21 as forthcoming work; [NOTE-052](NOTE-052.md) records that it builds on this paper.
Schwitzgebel ([LIT-191](../literature.d/LIT-191.md), [NOTE-104](NOTE-104.md)) cites the 25% figure. His Mimicry Argument
formalises §2's training worry, and his minimal-instantiation problem
bites the workspace and recurrence criteria of §3. Seth ([LIT-135](../literature.d/LIT-135.md), [NOTE-169](NOTE-169.md))
is the biological naturalist Chalmers sets aside. [NOTE-169](NOTE-169.md) records that
Seth attributes the phrase "computational biological naturalism" to
Chalmers. Nagel ([LIT-096](../literature.d/LIT-096.md))
supplies the definition. Schwitzgebel's US paper ([LIT-159](../literature.d/LIT-159.md), [NOTE-131](NOTE-131.md)) is
the same liberality worry run on groups. This paper's workspace, "a
central clearing-house … from numerous non-conscious modules", is the
subsystem-driven model Schwitzgebel used against Chalmers's
correspondence objection, and here Chalmers does not raise that
objection against it. The extended-mind paper ([LIT-097](../literature.d/LIT-097.md)) is unrelated
despite the word "extended". The hard problem is named only as challenge
2. Chalmers's core consciousness work, filed alongside this reading, is
where his own view lies, and fn 29 is the only place it enters the
numbers.

## Bearing on the record

- **[THEORY-023](../theory.d/THEORY-023.md): consistent, and a candidate source.**
  - *Behaviour half.* §2 makes the undercutting argument in 2022: trained
    self-report is weak evidence. It adds a fifth independent voice to the
    four [THEORY-023](../theory.d/THEORY-023.md) cites. Challenge 10, untrained descriptions of
    consciousness, is a proposal for the training-immune marker that
    [THEORY-023](../theory.d/THEORY-023.md) names as a refuter, not an instance of one.
  - *Architecture half.* The obstacles that do the work are theory-derived,
    and building them is treated as progress. That is the functionalist
    face of the Janus problem. Biology, the naturalist's face, is set aside
    with a reference to earlier work (C7). The credence calculation folds
    biology in at 1/3, so it is not conditional on functionalism outright.
    But it is a credence under assumed theories, which [THEORY-023](../theory.d/THEORY-023.md)'s
    `promote_when` says cannot settle the question. It does not move a
    party by evidence both sides accepted in advance.
  - *Prior.* It is a fifth position, alongside Seth, Birch, Butlin et al.
    and Schwitzgebel in "What this does not say": low for current LLMs,
    significant for LLM+ systems within a decade, higher on Chalmers's own
    views (fn 29). [THEORY-023](../theory.d/THEORY-023.md) could cite it as a source for the behaviour
    half and as an example of the architecture half. That is for whoever
    next revises [THEORY-023](../theory.d/THEORY-023.md).
- **[THEORY-043](../theory.d/THEORY-043.md).** Only the workspace remark and the "ecosystem of
  multiple agents" remark touch it (see Connections). Neither is argued.
- **[NOTE-131](NOTE-131.md)'s correspondence principle is not stated here.**
- **Anthology.** Not held there. The engineering challenges are framed as a
  roadmap or red flags, not as advice, and no anthology topic holds AI
  consciousness. No [ADR-013](../decisions.d/ADR-013.md) entry.

## Limitations

- **The numbers are illustrative**, by the author's own repeated warning.
  The independence assumption is disclaimed in the same breath, and the
  50% figures in the LLM+ estimate are stipulated.
- **"Mainstream assumptions" is doing the work.** The survey figures in fn
  30 measure acceptance or finding a theory promising, not credence, and
  Chalmers says converting them "requires further work".
- **Biology is not engaged.** The one objection classed as possibly
  permanent is set aside by reference to earlier work.
- **Empirical claims are dated.** Transformers are "almost entirely
  feedforward", self models are poor, Perceiver IO is the workspace
  example. The Afterword already shortens timelines.
- **General intelligence as evidence** (C2) is asserted from what
  researchers "often" regard as a sign, with no theory applied.

## Open questions

- Is there a description of a feature of consciousness that a model could
  produce without its training material containing it, and how would one
  certify the absence (challenge 10)?
- Does the theory-balanced credence change if theories are weighted by
  evidence rather than by expert acceptance (fn 30)?
- Does a single LLM hosting "an ecosystem of multiple agents" count as one
  candidate subject or many, and which one would a credence be about?

## Corrections

- No seeded skim to correct. The brief's citation is right.
- **The numbers changed between versions.** v1 (March 2023) gave at least
  25% to biology, grounding and self models and 50% to recurrence,
  workspace and agency. That made the product "at most a 5% or so chance"
  (0.75³ × 0.5³ ≈ 0.053), before adjustments to "somewhere under 10%". v3
  gives at least 1/3 to all six, with a product under 1/10. Both end
  "under 10 percent". v1's summary slide labels biology "highly
  contentious, permanent".
- **Challenge numbering in v3 is inconsistent.** The body calls the
  untrained-features challenge the "third", virtual worlds the "fourth",
  world and self models the "fifth", recurrence the "sixth", the workspace
  the "seventh" and mouse-level capacities the "ninth". It leaves unified
  agency unnumbered. The closing list numbers them 10, 5, 6, 7, 8, 11 and
  9.
- **Fn 21** cites "Robert Long, Patrick Butlin, et al."; arXiv:2308.08708
  ([LIT-056](../literature.d/LIT-056.md)) lists Butlin first. §4 has an orphaned footnote mark ("unified
  agency.1").
- **For [NOTE-104](NOTE-104.md).** Its gloss "Chalmers (2023) gives ~25% credence to AI
  consciousness within a decade" is fair. The text's figure is "25 percent
  or more" that conscious LLM+ systems will exist within a decade, on
  mainstream assumptions.
