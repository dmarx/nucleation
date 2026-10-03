---
status: Proposed
promote_when: >-
  Two results, one for each half. For the arbitration rule: a
  manipulation of one controller's reliability alone, with the outcome
  values and the effort required held fixed, that moves behaviour between
  devaluation-sensitive and devaluation-insensitive control as Daw et
  al. predict (an unexpected change of contingency favouring the model,
  a fan-out task structure favouring the cache), shown first-hand and in
  more than the stylised tasks the 2005 paper simulates. Their sharpest
  prediction would count most: that incentive learning becomes
  unnecessary in animals whose caching system is lesioned. For the
  Pavlovian half: a model-based Pavlovian revaluation, like the salt
  result, that is shifted toward or away from control by a manipulation
  of its reliability, and an algorithm for it. The account is refuted if
  control share follows a cost of computation or of effort when
  reliability is held constant, which is the expected-value-of-control
  account's prediction and not this one's; or if a dedicated arbitrating
  structure is found to weigh something other than the two predictions'
  reliability. What cannot settle it: more demonstrations that habits
  form with over-training, which every account predicts.
title: 'Model-based and model-free predictions both operate in instrumental and in Pavlovian learning, and which one controls behaviour follows their relative reliability, not the preference of a supervising system'
version: 1
tags:
- behavioral-integration
- learning-and-conditioning
- neuroscience
date: '2026-10-03'
source:
- LIT-tmpk0t5p
- LIT-tmpmlzuo
summary: >-
  Daw, Niv & Dayan ([LIT-tmpk0t5p](../literature.d/LIT-tmpk0t5p.md)) cast habitual and goal-directed
  instrumental control as model-free caching and model-based search, and
  let behaviour follow whichever estimate is less uncertain; simulations
  reproduce the effects of over-training, task complexity and reward
  proximity on devaluation. Dayan & Berridge ([LIT-tmpmlzuo](../literature.d/LIT-tmpmlzuo.md)) show from
  instant revaluation of a salt cue that Pavlovian prediction also has a
  model-based form, and suggest the same reliability arbitration there.
  Both controllers pursue the same ends; neither is the irrational one.
  The instrumental half is qualitative simulation; the Pavlovian half of
  the arbitration is a suggestion. Proposed.
---
<!-- inactive-ok-file: THEORY-056 THEORY-045 — Proposed; accounts this one bears on, with the bearing stated and nothing resting on them -->
<!-- inactive-ok-file: THEORY-tmpkujus THEORY-tmpgx68d — new in this batch; accounts this one is set beside -->

# THEORY-tmp2wlfb: Model-based and model-free predictions both operate in instrumental and in Pavlovian learning, and which one controls behaviour follows their relative reliability, not the preference of a supervising system

## Source

- Daw, Niv & Dayan (2005), [LIT-tmpk0t5p](../literature.d/LIT-tmpk0t5p.md), read in [NOTE-tmpishc1](../notes.d/NOTE-tmpishc1.md): the model,
  Figures 5–6, and the Discussion.
- Dayan & Berridge (2014), [LIT-tmpmlzuo](../literature.d/LIT-tmpmlzuo.md), read in [NOTE-tmpruoh7](../notes.d/NOTE-tmpruoh7.md): §§1–4 and
  the Appendix.

## What was actually shown

**Two instrumental controllers, arbitrated by uncertainty.** Daw et al.
([LIT-tmpk0t5p](../literature.d/LIT-tmpk0t5p.md)) identify habitual control, insensitive to devaluing the
outcome, with a model-free cache of long-run values, and goal-directed
control, sensitive to it, with model-based search through a learned model.
Each is an approximation to the intractable optimal controller, and they
fail in opposite circumstances. The cache needs much experience, since it
bootstraps from its own estimates. The tree learns fast, but each step of
search adds noise. If each tracks its own posterior uncertainty and
behaviour takes the less uncertain estimate, simulation gives the observed
pattern: model-based control early in training; cached control of a distal
lever press after over-training; model-based control kept for the action
next to the reward, and kept for the distal action too when there are more
actions and outcomes to spread experience over (Figs. 5–6). The lesion
literature is read the same way: each lesion leaves one controller alone.
The paper says the controllers serve the same ends, and rejects the picture
of an irrational limbic system fighting a rational prefrontal one.

**Pavlovian prediction is not only model-free.** Dayan and Berridge
([LIT-tmpmlzuo](../literature.d/LIT-tmpmlzuo.md)) report rats whose lever cue had predicted disgusting Dead Sea
salt. Put for the first time into a salt appetite and tested in extinction,
they engaged that lever more than tenfold, nearly as much as a sucrose cue,
before tasting the salt again. A cache stores value without the outcome's
identity and gives "no hint" how to revalue for a state never experienced
(C2 in [NOTE-tmpruoh7](../notes.d/NOTE-tmpruoh7.md)). So the revaluation needed a prediction of which
outcome the cue signals, evaluated against the current bodily state: a
model. They extend Daw et al.'s arbitration to this case, suggesting that
Pavlovian model-based predictions "might be less uncertain" than
instrumental ones because they need not assess the contingency of an
action, and so "may more easily best their model-free counterparts".

**Where the evidence stands.** The instrumental half is qualitative fits to
stylised tasks, as Daw et al. say. The Pavlovian half rests mainly on one
experiment, which the record holds as Dayan and Berridge report it, and the
arbitration there is a suggestion. No algorithm for model-based Pavlovian
revaluation exists by their own account.

## What this does not say

- **Not that no structure arbitrates.** Daw et al. name infralimbic cortex
  or anterior cingulate as candidates, on "limited evidence". The claim is
  about what the arbitration weighs. A structure that compares the two
  estimates' reliability, and has no ends of its own, is not a supervisor
  in the sense denied here. One that chose by its own goals would be.
- **Not hard arbitration.** Taking the lower-variance estimate is a
  simplification, and the paper allows a reliability-weighted average.
- **Not that over-training always makes habit.** Dayan and Berridge propose
  that some persistence after devaluation is a "defocused" model-based
  prediction, which would make the two harder to tell apart. They concede
  this.
- **The over-training result depends on a modelling choice**, the size of
  the per-step search noise, which the main text does not justify.

## Connections

- **The unity it is about.** `behavioral-integration`: two controllers
  with the same ends, and the rule by which one of them acts. Nothing here
  concerns self or person ([ADR-024](../decisions.d/ADR-024.md)).
- **[THEORY-056](THEORY-056.md)** (regulation as one motive state checking another, with no
  regulator above them). This account supports the clause about no
  regulator above, in a different domain: the controllers are peers and
  the winner is the more reliable, not the one a higher system prefers. It
  sharpens a question [THEORY-056](THEORY-056.md) leaves open, whether a structure that
  computes arbitration counts as a "regulating system". This account says
  it does not, if it weighs only reliability. No relation is declared,
  since the domains differ.
- **[THEORY-tmpkujus](THEORY-tmpkujus.md) (the expected value of control).** The two give
  different reasons why strenuous concurrent demands should favour habit.
  Here the model's estimate becomes less reliable; there control is costly.
  Holding reliability fixed while varying cost would separate them. They
  are not declared rivals, because the EVC account is about the intensity
  of cognitive control and this one about which of two learners acts, and
  both may hold.
- **[THEORY-tmpgx68d](THEORY-tmpgx68d.md) (Ainslie).** Rejects the same reason-against-impulse
  picture, for controllers that differ in delay, not in method. Daw et al.'s
  controllers share their ends; Ainslie's differ in them by time. The
  pictures address different divisions and do not conflict.
- **[THEORY-045](THEORY-045.md)** (felt affect as the experience of regulatory state). The
  salt result is a case of the body's regulatory state instantly changing
  the value of a predictive cue. It is consistent with that account and does
  not test its claim about experience.
