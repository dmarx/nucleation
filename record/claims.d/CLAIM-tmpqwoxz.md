---
status: Proposed
title: 'A parameterization of a network allocates rates among its modules: it fixes the exponent with which each module''s rate of change scales with width or depth, so the lazy regime is the case where hidden modules are slower than the readout by a factor that grows with width and act as constraints on it, μP is the case where no module is slower by such a factor and the hidden layers form one level, and per-module allocation in the modular norm sets the rate differences directly'
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  Either of two results. (a) A reading of Yang and Hu (LIT-tmp9tr5w) or
  Chizat and colleagues (LIT-tmp67epj) that finds the kernel or lazy limit
  is not one in which hidden features change by a vanishing amount over
  the time in which the output is fit, so that it is not a separation of
  rates. (b) A reading of the modular norm (LIT-tmp4b6aq) that finds it
  does not apportion update sizes among modules by a free parameter, so
  that it sets no rate differences.
tags:
- learning-theory
- complex-systems
- anthology-candidate
date: '2026-11-20'
line:
- learned-structure
- distributed-agency
rests_on:
- CLAIM-478
- CLAIM-tmpy75jv
grounds:
- THEORY-813
- THEORY-2077
- LIT-tmp9tr5w
- LIT-tmp67epj
- LIT-tmp4b6aq
summary: >-
  The third link the owner asked for. The record's rate-difference claims
  ([CLAIM-478](CLAIM-478.md) version 5, [CLAIM-tmpy75jv](CLAIM-tmpy75jv.md)) say levels form where rates differ
  between groups by more than they vary within, and a slow level acts as a
  constraint on a fast one. Network parameterizations set exactly such
  exponents with width: the lazy limit, where hidden features barely move
  while the output is fit ([THEORY-813](../theory.d/THEORY-813.md); Chizat and colleagues), is a
  two-level hierarchy with frozen features as constraints; μP removes the
  width-growing differences. Rests on recollections of unread works until
  [LEAD-tmp8q1aw](../leads.d/LEAD-tmp8q1aw.md). The wording is the assistant's (Claude, in this session);
  adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-478 CLAIM-tmpy75jv LIT-tmp9tr5w LIT-tmp67epj LIT-tmp4b6aq LIT-tmpj34ir THEORY-813 THEORY-2077 CLAIM-tmpmugkp CLAIM-tmpxi826 — Proposed or Deferred; the claims this applies and the works it rests on until read -->

# CLAIM-tmpqwoxz: A parameterization of a network allocates rates among its modules: it fixes the exponent with which each module's rate of change scales with width or depth, so the lazy regime is the case where hidden modules are slower than the readout by a factor that grows with width and act as constraints on it, μP is the case where no module is slower by such a factor and the hidden layers form one level, and per-module allocation in the modular norm sets the rate differences directly

## The claim

The owner, 2026-11-20: "i bet we can connect this time scale separation to
depth scaling in the maximal update parameterization, which would give us a
path to connect our model to the modular duality program".

**Exponents with width are the ε^U form.** Yang and Hu ([LIT-tmp9tr5w](../literature.d/LIT-tmp9tr5w.md))
classify parameterizations by how each layer's initialization, multiplier and
learning rate scale with width n. Each choice fixes how fast each layer's
features change per step as a power of n. Write ε = 1/n: the layer rates are
ε^(U_l), the form of the record's rate-difference results ([CLAIM-tmpxi826](CLAIM-tmpxi826.md),
[CLAIM-tmpy75jv](CLAIM-tmpy75jv.md)), with one exponent per module.

**Lazy is a two-level hierarchy.** In the kernel or lazy limit the hidden
features move by a vanishing amount while the output is fit ([THEORY-813](../theory.d/THEORY-813.md);
Chizat and colleagues, [LIT-tmp67epj](../literature.d/LIT-tmp67epj.md), recalled). The hidden layers are slower
than the readout by a factor that grows with width. In [CLAIM-478](CLAIM-478.md)'s terms they
are a slow level acting as a constraint on the fast one: frozen random
features, with only the linearized model learning. [THEORY-2077](../theory.d/THEORY-2077.md) (Anguita and
colleagues) shows the same thing at finite size: the relative scale of the
layers' initialization places fine-tuning in regimes that trade reuse of
features against learning new ones.

**μP is one level.** μP sets every hidden layer's exponent so that its
features change at the same order as the others' as width grows: no module
is slower by a width-growing factor, so in width the hidden layers form one
level. The spectral condition ([LIT-tmpj34ir](../literature.d/LIT-tmpj34ir.md), recalled) states this as a
condition on each layer's update size in the spectral norm.

**The modular norm sets the allocation.** The modular norm ([LIT-tmp4b6aq](../literature.d/LIT-tmp4b6aq.md))
is defined recursively with the architecture and normalizes updates so that
learning rates transfer across width and depth (its abstract). The assistant
recalls that it carries a per-module mass apportioning the update among
modules; if so, the masses are the module rate exponents set by hand, and a
choice of masses is a choice of which modules form levels. Within a layer,
modular dualization equalizes rates across singular directions, which in a
linear network reverses and compresses the staged hierarchy of learning
([CLAIM-tmpmugkp](CLAIM-tmpmugkp.md)).

## What it does not say

- Not that the record's tree theorem applies to training. [CLAIM-tmpxi826](CLAIM-tmpxi826.md) is
  about a Markov chain moving among states; training is a flow over
  parameters. What carries over is the rate-difference claim, that slow
  modules constrain fast ones and levels form where differences between
  groups beat those within.
- Not that one parameterization is better. The claim is about the structure
  of the dynamics each one produces; which to use is the anthology's
  business ([ADR-048](../decisions.d/ADR-048.md)).
- The works it rests on are unread. Defeaters (a) and (b) are what reading
  them would test.
