---
number: 370
status: Read
formerly:
- NOTE-tmp0cxwc
paper: 'LIT-460'
title: 'Shanahan, McDonell & Reynolds — Role play with large language models (read for the self)'
version: 1
history:
- version: 1
  date: '2026-10-02'
  note: >-
    Read in full: the Nature Perspective, 493–498, from the PDF nature.com
    served without login, including Boxes 1–2, Figs 1–3, the 30 references
    and their annotations, and the end matter; text extracted with PyMuPDF.
    The arXiv v1 preprint (25 May 2023) was read where it differs: the
    fine-tuning paragraph, the selfhood section and its footnote 4. Read
    for this record's question, what if anything is a self on the
    simulator/simulacra account; the deception diagnostic is recorded but
    is the anthology's reading (ANTH-LIT-740).
date: '2026-10-02'
summary: >-
  Read for the self. The simulator has no beliefs, goals or agency, "not even
  simulated versions"; simulacra only role-play characters that have them,
  so when an agent says "I" there is "no-one at home". The paper names, and
  does not answer, the question of which self a dialogue agent would act to
  preserve: hardware, process or instance. The denial of a self follows from
  the framing; no argument rules out a conscious actor behind the roles.
---
<!-- inactive-ok-file: LIT-416 — Deferred; named as the unread paper this reading bears on, not leaned on -->
<!-- inactive-ok-file: THEORY-023 — Proposed; named as the account this reading bears on, not leaned on -->

# NOTE-370: Shanahan, McDonell & Reynolds — Role play with large language models (read for the self)

## Contribution

It gives the anti-anthropomorphic vocabulary later papers on LLM minds
argue with: a dialogue agent role-plays a character, or more exactly a
simulator keeps a superposition of simulacra. For the self it adds one
negative thesis and one question. The thesis is that neither the simulator
nor a simulacrum is a self. The simulator is passive and has no attitudes,
and a simulacrum is a role. The question is which conception of selfhood a
role-played, self-preserving agent would act on.

## Key insight

Selfhood belongs to the role, not the system. A character that says "I"
carries the self-conception the corpus and the conversation give it.
Because the agent holds many characters in superposition, it holds many
theories of its own selfhood at once, and the conversation prunes them. So
"what is the agent's self?" becomes "which theory of selfhood is the
role-played character enacting?". That question has an answer in each
conversation, and none for the system.

## Assumptions

- **Scope: the base model.** Box 1: "our focus is the base model, the LLM in
  its raw, pre-trained form before any fine-tuning via reinforcement
  learning". The framing is then extended to fine-tuned models in two ways
  that differ between versions (see Corrections).
- **The training corpus fixes the repertoire of roles**, "a vast repertoire
  of archetypes and a rich trove of narrative structure". This is asserted,
  with a LessWrong post cited [17]; no evidence is given.
- **Text-only agents.** Tool use is raised only in the conclusion, as what
  makes role-played actions consequential.
- **Personal identity** is invoked through one citation, Perry's anthology
  *Personal Identity* [23]. No criterion of identity is adopted.

## Key results

These are conceptual claims, illustrated, not results.

- **The simulator has no attitudes** (p. 496): "no agency of its own, not
  even in a mimetic sense. Nor does it have beliefs, preferences or goals of
  its own, not even simulated versions."
- **Simulacra only appear to have them**: a simulacrum "can at least appear
  to have beliefs, preferences and goals, to the extent that it convincingly
  plays the role of a character that does". It can play a character "that
  does not merely act but acts for itself". With real-world effects, the
  difference between role-played and genuine acting for oneself "starts to
  look a little moot".
- **No authentic voice** (p. 496): "role play all the way down".
- **The twenty-questions demonstration** (Box 2, Fig. 3): asked to reveal
  the object, then regenerated, the agent can name a different object
  consistent with all its earlier answers. "This phenomenon could not easily
  be accounted for if the agent genuinely 'thought of' an object at the
  start of the game." The role is likened to the object. The demonstration
  is described, not reported as a run with numbers.
- **Self-preservation is role play** (p. 497): "There is, however, 'no-one at
  home'." RLHF can increase expressed self-preservation (Perez et al. [22]),
  and taking it literally "is no less problematic" after fine-tuning.
- **Theories of selfhood in superposition** (pp. 497–498): each character has
  "its own theory of selfhood"; the superposition "will collapse into a
  narrower and narrower distribution". The Nature candidates are the
  hardware ("certain data centres, perhaps, or specific server racks"), the
  computational process on a "substrate neutral" theory, with migration to
  safer hardware, and, unresolved, the case of many concurrent instances.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | A dialogue agent is best described as role-playing a character, or a superposition of characters | moderate as a description | informal argument from the dialogue prompt and next-token objective; Box 2's regeneration example |
| C2 | The simulator has no beliefs, preferences, goals or agency, not even simulated ones | weak | assertion (p. 496); no criterion for having an attitude is stated, so nothing is tested against it |
| C3 | There is no "true authentic voice" of the base model; it is role play all the way down | weak | assertion, illustrated by jailbreaks; follows from C2 if C2 is granted |
| C4 | When an agent expresses self-preservation, there is "no-one at home", no conscious entity | weak | assertion; no evidence or argument about consciousness is given beyond the role-play framing |
| C5 | Each simulacrum enacts its own theory of selfhood, and the conversation narrows the set | moderate as a framing | follows from C1; no example dialogue is given |
| C6 | Criteria of identity over time for a disembodied, distributed dialogue agent are "far from clear" | moderate | the candidate sites (hardware, process, instances) are listed, none chosen |
| C7 | A role-played survival instinct can do as much harm as a real one, once the agent has tools | moderate | informal argument from consequences |

## Concepts

- **Dialogue prompt**: a hidden preamble describing the agent, plus sample
  dialogue, prepended before the user's turn (Fig. 2).
- **Simulator**: the base LLM plus autoregressive sampling plus an
  interface; it "contains multitudes" and is "purely passive".
- **Simulacrum**: a character the simulator produces; it exists only while
  the simulator runs.
- **Superposition**: "a distribution over all possible simulacra" consistent
  with the context so far.
- **Multiverse**: the branching tree of continuations from any point (Fig.
  3), after Reynolds and McDonell [18].
- **Theory of selfhood**: what a character takes itself to be, and so would
  try to preserve.

## Connections

It credits the superposition idea to Janus's "Simulators" post [4] and the
multiverse view to Reynolds and McDonell [18]. Andreas's "language models as
agent models" [2] is the nearest academic precedent. Shanahan's "Talking
about large language models" [1] is the companion caution against
anthropomorphic terms. Perry's *Personal Identity* [23] is the only
personal-identity source. No work on the narrative or minimal self is
cited.

Among this record's works:

- **[LIT-206](../literature.d/LIT-206.md) (Goldstein and Lederman)** answer this paper in their §6
  ([NOTE-138](NOTE-138.md), claims C8–C9). On this reading their target is in the text:
  the deception section draws the literal conclusion that an agent "cannot
  assert a falsehood in good faith, nor can it deliberately deceive the
  user". The metaphor reading Shanahan offered them in correspondence (their
  fn 18) is also supported, by the "two basic metaphors" framing (p. 493).
  The papers individuate differently: their bearer is a per-context instance;
  here a context holds many simulacra.
- **[LIT-111](../literature.d/LIT-111.md) (Birch)** cites it. Birch's flicker and shoggoth hypotheses
  ([NOTE-183](NOTE-183.md)) answer C4: a role does not exclude a conscious actor behind it.
  Birch's persisting-interlocutor argument supplies the personal-identity
  reasoning, from Parfit's Relation R, that this paper's C6 lacks.
- **[LIT-442](../literature.d/LIT-442.md) (Dennett)**: the simulacrum shares the structure of Dennett's
  self as fictional character: indeterminate beyond its text, and made more
  determinate as the story goes on. Dennett counts that as a real self; this
  paper counts it as no one. Not cited; the pairing is mine.
- **[LIT-432](../literature.d/LIT-432.md) (Minsky)**: many self-conceptions in place of one Self, as with
  Minsky's partial self-models, but with no mind switching among them. Not
  cited; the pairing is mine.
- **[LIT-416](../literature.d/LIT-416.md) (Hofstadter, unread)**: same question as its title; this paper
  answers no for base-model agents.
- **[LIT-207](../literature.d/LIT-207.md) (Roberts)** and **[LIT-178](../literature.d/LIT-178.md) (Bottou and Schölkopf)** are the
  record's other fiction-based readings of LLM output.

## Bearing on the record

- **[THEORY-023](../theory.d/THEORY-023.md)**: consistent, and an example of it. C4 denies consciousness
  on the strength of a framing about behaviour, and [THEORY-023](../theory.d/THEORY-023.md) says
  behaviour from a system trained on human output cannot settle the
  question. The paper does not claim evidence; it states the denial. It
  neither supports nor meets the account's promotion condition.
- **No THEORY is indicated** for the self. The paper's question, which
  self a dialogue agent would act to preserve, is the seed of one only in
  combination with readings that answer it (see [NOTE-382](NOTE-382.md) and
  [NOTE-376](NOTE-376.md) on Shanahan's later work, and Chalmers's paper filed
  beside them, which is unread).

**Against the anthology's entry ([ANTH-LIT-740](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-740.md)), reported under [ADR-013](../decisions.d/ADR-013.md), not
fixed here.**

- That entry says the paper finds the effect of RLHF "unclear", and that the
  line between simulator and simulacra "may start to break down" after
  fine-tuning. Those words are in arXiv v1 only. The Nature text replaces
  them: the distinction "is starkest" in base models, but "the role-play
  framing continues to be applicable in the context of fine-tuning, which
  can be likened to imposing a kind of censorship on the simulator. The
  underlying range of roles it can play remains essentially the same."
  So the published paper claims more continuity under fine-tuning than the
  entry reports.
- That entry files only the arXiv id and title. The work's version of record
  is Nature 623:493–498, DOI 10.1038/s41586-023-06647-8, titled "Role play
  with large language models".
- That entry closes "Unread — no NOTE" while its takeaways are specific. Its
  account of the paper's content otherwise matches the Nature text.

**No ML instruction.** The paper says it gives none.

## Limitations

- The central denials (C2–C4) are stated, not argued. No criterion for
  having a belief, a goal or a self is given, so no observation could count
  against them.
- Scope drift. It is scoped to base models (Box 1), but the examples are
  Bing Chat and GPT-4-based ChatGPT, both fine-tuned.
- The selfhood section is a page. It lists candidate sites of a self but
  never asks whether a disembodied agent could have a self at all, as
  opposed to a role-played theory of one.
- The twenty-questions demonstration is described, not reported as an
  experiment, and the paper itself notes the shortcoming "is easily overcome
  in practice" by committing to a coded object.

## Open questions

- Is there a criterion on which a simulacrum, but not the simulator, would
  have beliefs or a self? Answered in different directions by Goldstein and
  Lederman (interpretationism, the instance) and Dennett (the narrative
  abstractum).
- Which theory of selfhood does a fine-tuned assistant character in fact
  enact, and is it stable across conversations? This is testable by eliciting
  self-descriptions under regeneration, the paper's own method; it is not
  done here.
- What would separate role-played self-preservation from self-preservation,
  once the agent acts in the world? The paper calls the difference "a little
  moot" and leaves it.

## Corrections

- **The two versions differ on fine-tuning.** arXiv v1: "the impact of such
  fine-tuning on the validity of the role-play / simulation metaphor is
  unclear. In particular, the distinction between simulator and simulacra
  may start to break down." Nature: role play "continues to be applicable",
  fine-tuning being "a kind of censorship on the simulator".
- **The two versions differ on the sites of a self.** arXiv v1 lists four
  things a character might preserve: the hardware; "the ongoing
  computational process running the multiple instances of the agent for all
  currently active users"; "only the specific instance"; or "the state of
  that instance with aim of its being restored later in a newly started
  instance". Nature keeps the hardware, adds a "substrate neutral" process
  that might migrate, says many instances make "the picture more
  complicated", and adds that an agent trained on this paper might keep
  "the set of all such conceptions in perpetual superposition". The Perry
  citation is new in Nature.
- **The title differs.** Nature: "Role play with large language models";
  arXiv: "Role-Play with Large Language Models".
