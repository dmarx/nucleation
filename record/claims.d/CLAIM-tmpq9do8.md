---
status: Proposed
title: 'The loop that keeps a lucid agent''s model in touch with what it models runs between judgement and observation: each judgement reshapes the observer whose later observations it then judges, and action on the world is not part of that loop, so active inference''s action–perception cycle misplaces where the agent is active'
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  Either of two results. (a) Perceptual or retrieval learning that changes
  what an agent individuates or can retrieve shown to need contingency
  between action and outcome: with action and its outcomes held fixed,
  the agent's own judgements, made without feedback, leave the observer
  unchanged. (b) Lucid judgement shown to fail when every contingency
  between intention and outcome is removed while consciousness is
  otherwise preserved, by evidence that does not itself restore such a
  contingency (CASE-tmpxgcq2). Not defeated by a redescription of the loop
  as mental action and structure learning inside one generative model
  (CLAIM-tmp9cjyo), which concedes that action on the world is not part
  of it and contests only where the boundary is drawn. Not defeated by a
  showing that action matters for building the model, or that agents
  usually act.
tags:
- cognition
- agency
- probabilistic-modeling
date: '2026-10-16'
line:
- distributed-agency
- pragmatic-transport
- will-organization
rests_on:
- CLAIM-297
- CLAIM-275
grounds:
- LIT-tmp670rc
- THEORY-tmpns74h
- THEORY-tmp6rcgc
- THEORY-tmp2k3a9
- LIT-tmpuamcv
complements:
- CLAIM-tmp84z6h
- CLAIM-tmpt568z
uses:
- TERM-026
- TERM-039
summary: >-
  The owner's, U1 of the exchange of 2026-10-16: Friston's free-energy
  approach is "generally correct, but the cybernetic model is wrong";
  action can be cut out of the loop, which decomposes into "Judgement (qua
  measurement that generates interpretations) <--> Observation". At U2 the
  owner held that the pragmatic-transport and will-organization models are
  "both manifestations of the same underlying model". The claim is stated
  in that model's terms, as [CLAIM-297](CLAIM-297.md)'s circuit, and in the diachronic
  form A4 proposed and the owner asked to be filed at U5 ("make the
  revisions"): a judgement need not produce the observation it judges,
  but it reshapes the observer that produces the next one. The sharp edge: the synchronic form, in which each judgement
  produces its own outcome, is not claimed. That is the open route of
  [TERM-039](../terms.d/TERM-039.md) and [CLAIM-127](CLAIM-127.md), and the record demoted it once before
  ([CLAIM-109](CLAIM-109.md)).
---

# CLAIM-tmpq9do8: The loop that keeps a lucid agent's model in touch with what it models runs between judgement and observation: each judgement reshapes the observer whose later observations it then judges, and action on the world is not part of that loop, so active inference's action–perception cycle misplaces where the agent is active

## The claim

The owner, at U1: "Friston's 'Free Energy' approach is generally correct,
but the cybernetic model is wrong. Rather than cycling between `Action <-->
Perception`, we can cut 'Action' out of the loop completely and constrain
attention to the internal feedback loop, which decomposes nicely into
`Judgement (qua measurement that generates interpretations) <-->
Observation`, which connects us back to our model and also makes our
complaint with Friston's formulation precise."

The record's model already has this loop. [CLAIM-297](CLAIM-297.md) writes the operator
model as a circuit, "frame → retrieval → interpretation → endorsement →
future retrieval policy". It is two coupled processes over a meaning state
x, operator weights w and queries q:

- meaning: x_{t+1} = Σᵢ w_{i,t} P_i(q_t)ᵀ x_t;
- influence: w_{t+1} = G(w_t, x_t, o_t, E_t);
- queries: q_{t+1} = Q(x_{t+1}, w_{t+1}, g).

Read with the owner's terms, the query is the judgement's measurement
context, the operators applied under it are the judgement, and x is the
interpretation it yields. The interpretation, through endorsement and the
next query, fixes what will be retrieved and so what the next judgement
observes. Nothing in the circuit acts on the world. The world enters only
as evidence o_t in the update of influence. [CLAIM-275](CLAIM-275.md) holds the half that
concerns order: an operator can intervene on the meaning canvas before it
has the interpretation its intervention makes available.

"Generates" is read diachronically. A judgement need not produce the
observation it judges. It changes the observer, which produces the later
observations. The record holds this for perception: perceptual learning
can install frames that change which objects a perceiver individuates from
the same input, so "cognition can shape the perceptual system over time
while leaving open whether any single percept is cognitively penetrated"
([THEORY-tmpns74h](../theory.d/THEORY-tmpns74h.md)). And for cognition: percepts are used only inside a
"cognitive envelope", where working memory holds "recoded, task-dependent
abstractions rather than the percepts themselves" ([THEORY-tmp6rcgc](../theory.d/THEORY-tmp6rcgc.md)). The
observation the loop runs on is already a product of earlier judgement.

The complaint against active inference is then precise in Pearl's terms
([THEORY-tmp2k3a9](../theory.d/THEORY-tmp2k3a9.md)). Active inference treats perception as conditioning on
observations that arrive at the blanket's sensory states, and places all
of the agent's influence on what it observes in action, which samples the
data ([LIT-tmp670rc](../literature.d/LIT-tmp670rc.md)). The claim holds that the agent's main influence on
what it observes is an intervention on itself, the observer, made by
judging. Action on the world is one further influence. It is not part of
the loop.

## Judgement is not action

The objection that a judgement is itself behaviour ([THEORY-tmpltl13](../theory.d/THEORY-tmpltl13.md)), and
so action relabelled ([CLAIM-tmp9cjyo](CLAIM-tmp9cjyo.md)), is answered by where the judgement
acts. Action, in the active-inference sense, changes external states, which
then change sensory states. A judgement changes the judge's own state, the
canvas and the retrieval policy ([TERM-026](../terms.d/TERM-026.md), [CLAIM-275](CLAIM-275.md)). Both are operations.
What separates them is their target, and the claim is that the loop that
keeps a model in touch closes through the second.

QBism is the sharpest contrast ([LIT-tmp7kgwz](../literature.d/LIT-tmp7kgwz.md), read in [NOTE-tmpfpjq8](../notes.d/NOTE-tmpfpjq8.md)). It
agrees that a measurement creates its outcome rather than revealing it: "A
measurement does not, as the term unfortunately suggests, reveal a
pre-existing state of affairs. It is an action on the world by an agent
that results in the creation of an outcome — a new experience for that
agent." But QBism keeps judgement and measurement apart. A judgement is the
agent's state assignment ("a quantum state assignment is also a personal
judgment"). A measurement is "any action an agent takes to elicit a set of
possible experiences", and the agent's "own direct internal awareness of
her own private experience" is the one thing it does not model. Its loop is
judgement, action, experience, update: the action–perception shape this
claim rejects, with the self left out of the measurement. This claim makes
the judgement itself the measurement, and the judge the thing it changes.

## Evidence that judging changes the judge

The record had none from outside its own exchanges until it registered
three works. Two have been read.

- **Feldman and Lynch** ([LIT-tmpuamcv](../literature.d/LIT-tmpuamcv.md), read in [NOTE-tmpj9jxh](../notes.d/NOTE-tmpj9jxh.md)). Measurement
  creates state, not only a response: "If the researcher asks a question
  about attitude (or belief, intention, etc.), and no such cognition
  already exists, the measure creates one". And the diachronic form is
  explicit: "Once the answer has been computed, it can be retrieved to
  answer subsequent questions". This is the route [TERM-039](../terms.d/TERM-039.md) and [CLAIM-127](CLAIM-127.md)
  leave open, an arrow from the context into the interpreter's state,
  argued in classical terms. Three limits:
  - the paper has no data of its own and calls its account speculative;
  - it values the created state mainly for its effect on behaviour;
  - it gives judgement no special place: "all real-world experiences with
    an object have the potential to shape subsequent responses to it".
- **Slovic** ([LIT-tmpetez2](../literature.d/LIT-tmpetez2.md), read in [NOTE-tmp38ooy](../notes.d/NOTE-tmp38ooy.md)): preferences are
  "constructed—not merely revealed—in the elicitation process". Every
  result compares elicitation procedures. That shows the measurement
  context entering the response, which is the route A129's graph already
  has. It never follows a constructed preference into a later judgement,
  so it supports the synchronic reading this claim sets aside, not the
  diachronic one it holds. Construction is claimed only for "important,
  complex, and perhaps unfamiliar" options.
- **Morwitz, Johnson and Schmittlein** ([LIT-tmpj2lkz](../literature.d/LIT-tmpj2lkz.md), Unavailable): merely
  asking purchase intent changes later purchasing. Known from the abstract
  only.

All three are classical in mechanism (retrieval, accessibility,
construction) and do not bear on contextuality. Feldman and Lynch is the
one that supports the claim as held.

## What keeps the loop honest

[CLAIM-tmpki5gp](CLAIM-tmpki5gp.md) objects that, without action, the loop confirms itself.
[CLAIM-tmpt568z](CLAIM-tmpt568z.md) answers from the model: what anchors the loop is evidence
whose arrival or scoring does not pass through the interpretation it
tests ([CLAIM-330](CLAIM-330.md), [CLAIM-141](CLAIM-141.md)). Action is one source of such evidence, not a
necessary one.

## The synchronic form, not claimed

The stronger reading of U1, in which each judgement produces its own
outcome, is not part of this claim:

- **It is open.** Whether eliciting a judgement changes the interpreter,
  and not only the response, is the route [TERM-039](../terms.d/TERM-039.md) and [CLAIM-127](CLAIM-127.md) leave
  open, to be settled by sequential designs.
- **The record demoted it once before.** [CLAIM-109](CLAIM-109.md) said a frame
  "participates in determining which meaning becomes actual", and it was
  demoted to [CLAIM-009](CLAIM-009.md) when its argument ([ARG-002](../arguments.d/ARG-002.md)) was undercut by
  [CLAIM-041](CLAIM-041.md).
- **Contextuality may not help.** If the synchronic form is to differ from
  classical state change, it needs contextuality. The weak sense is the
  starting point of Contextuality-by-Default, not a finding
  ([THEORY-tmpjwpuk](../theory.d/THEORY-tmpjwpuk.md)). The sheaf sense cannot arise for one system judged
  context after context ([THEORY-010](../theory.d/THEORY-010.md)). Spekkens's sense can ([QUESTION-067](../questions.d/QUESTION-067.md)).
  The record holds no behavioural evidence of contextuality proper
  ([CLAIM-325](CLAIM-325.md), [THEORY-tmpr96be](../theory.d/THEORY-tmpr96be.md)).

## What it does not say

- It does not say action is idle. Every lucid locked-in patient built their
  model while acting ([CASE-tmpxgcq2](../cases.d/CASE-tmpxgcq2.md)), and the claim is about the loop that
  keeps a built model in touch, not the one that built it.
- It does not reject free-energy minimization. The owner's complaint is
  with the cybernetic diagram, not with the bound. Three readings already
  make the complaint that active-inference models assume perception and
  action rather than deriving them ([NOTE-450](../notes.d/NOTE-450.md), [LIT-598](../literature.d/LIT-598.md), [LIT-615](../literature.d/LIT-615.md)).
- It does not say judgements are quantum measurements ([ARG-002](../arguments.d/ARG-002.md), [CLAIM-041](CLAIM-041.md)).
- It does not deny that active inference can redescribe the loop, as
  mental action on precision together with structure learning, and no
  action on the world ([CLAIM-tmp9cjyo](CLAIM-tmp9cjyo.md)). That redescription concedes the
  point about action and keeps the disagreement about the diagram.
- It does not file the owner's U2 statement that the two lines are one
  model. It follows that statement in choosing [CLAIM-297](CLAIM-297.md) as the model's
  statement of the loop.

## Rivals

- **Observation and control as one loop through the environment.** [NOTE-121](../notes.d/NOTE-121.md)
  defines an observer by feedback closure, "the observer's outputs must
  alter the environment, which then alters later inputs". The claim denies
  that condition.
- **Meaning from action.** Barrett: "meaning does not trigger action, but
  results from it" ([NOTE-434](../notes.d/NOTE-434.md)). [CLAIM-275](CLAIM-275.md) refuses to fix either order. This
  claim holds that the order through the world is not the one that keeps
  the model in touch.
- **Sense-making from regulation.** Di Paolo: a norm the system itself has
  needs adaptivity, which detects tendencies toward the viability boundary
  "and acts so as to reverse them" ([THEORY-tmprt7jm](../theory.d/THEORY-tmprt7jm.md)).
- **Agency defined by action.** Agents are "the systems that would adapt
  their policy were their actions to affect the world differently"
  ([THEORY-tmpgjsxj](../theory.d/THEORY-tmpgjsxj.md)). On that definition a judge that cannot act is not an
  agent. The claim is about a lucid judge, not about agency.
- **Perceptual control.** Powers: "behavior is the control of input, not
  output", and above the lowest level a system's output "is not a muscle
  force, but a reference level" for the level below ([LIT-tmp626gh](../literature.d/LIT-tmp626gh.md), read in
  [NOTE-tmpxdsyb](../notes.d/NOTE-tmpxdsyb.md)). In that paper every loop closes through the environment,
  down to the spinal systems that control muscle effort. But the theory's
  first statement has a loop with no action: an "imagination connection"
  by which a reference signal returns as the system's own perception, so
  that the system can "plan an action 'mentally' without actually
  performing it" ([LIT-tmpgo33i](../literature.d/LIT-tmpgo33i.md)). That loop is self-satisfying, since the
  "match" is "automatically ensured". It is the synchronic form this claim
  does not claim. Powers adds the anchor problem in the same passage: the
  hierarchy "could not perform very reliably" if its actions were
  "completely 'short-circuited'" by it, and Part II lists switching a
  system "entirely to the imagination-connection" as one of the ego's
  defences (LIT-tmpuh84t). Unlike the 1973 paper, 1960 does reshape the
  observer. The reorganizing system's first act is to build new perceptual
  input functions, "tentative definitions of new variables", driven by
  error in bodily intrinsic signals, "measures of a set of physiological
  states" (NOTE-tmpf65in). And Part II tests a change to the observer by
  imagining: a golfer drops a new idea because "a moment spent imagining
  doing so would reveal" the conflicts it makes (NOTE-tmplcbcz). So
  perceptual control theory has both of the claim's ingredients. The
  imagination loop changes nothing in the perceiver. Reorganization
  changes the perceiver, but is driven by bodily error, not by judgement.
  The claim's loop, judgement reshaping the observer, falls between them.
  The reorganizing system's inputs may include "mean error signal in the
  hierarchy", a scoring signal the learned hierarchy does not set, which
  is QUESTION-tmpr5tck's candidates 2 and 4.
- **The epistemic cut.** Pattee ([LIT-tmpo5atc](../literature.d/LIT-tmpo5atc.md), read in [NOTE-tmp7d44m](../notes.d/NOTE-tmp7d44m.md)) does
  not put measurement first. Measurement and control are converses:
  "measurement transforms physical states to symbols in memory, while
  memory-stored controls transform symbols to physical states", and "control
  of construction came first". So he belongs with the rivals that keep
  action, here control, in the loop. Two of his points still bear. Semantic
  closure, in which the reader of the symbols is built from them, has the
  shape of this claim's diachronic loop. And his condition for objectivity,
  that measurement must not influence the laws it measures, is close to
  [CLAIM-tmpt568z](CLAIM-tmpt568z.md)'s anchor.
