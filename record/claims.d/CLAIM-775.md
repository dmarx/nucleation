---
number: 775
status: Proposed
formerly:
- CLAIM-tmpqwoxz
title: 'A parameterization of a network allocates rates among its modules: it fixes the exponent with which each module''s effect on its output changes per step as a power of width or depth, so the kernel regime is the case where the hidden body is slower than the readout by a factor growing with width, its features and kernel fixed and acting as a constraint on the fitting, μP is the case where no part, readout included, is slower by such a factor, and the modular norm sets the ratios among modules by hand, with width exponents fixed by each module''s norm'
version: 2
history:
- version: 2
  date: '2026-11-21'
  note: >-
    Revised after the readings of 2026-11-21 of Yang and Hu, Chizat and
    colleagues, the spectral condition, the modular norm, Tensor Programs
    VI and modular duality. Defeaters (a) and (b) are not met. The title
    is restated where the readings correct it: μP removes the gap between
    body and readout, not differences among hidden layers (NTP's body is
    uniform too); the fixed hidden layers still contribute to the fit;
    masses set ratios, width exponents come from each module's norm.
    Grounds move from the unread works to the readings, and THEORY-212
    joins them. Previous title: "A parameterization of a network allocates
    rates among its modules: it fixes the exponent with which each
    module's rate of change scales with width or depth, so the lazy regime
    is the case where hidden modules are slower than the readout by a
    factor that grows with width and act as constraints on it, μP is the
    case where no module is slower by such a factor and the hidden layers
    form one level, and per-module allocation in the modular norm sets the
    rate differences directly".
role: thesis
warrant: interpretive
defeated_if: >-
  Either of two results. (a) A reading of Yang and Hu (LIT-2943) or
  Chizat and colleagues (LIT-2941) that finds the kernel or lazy limit
  is not one in which hidden features change by a vanishing amount over
  the time in which the output is fit, so that it is not a separation of
  rates. (b) A reading of the modular norm (LIT-2938) that finds it
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
- CLAIM-781
grounds:
- THEORY-813
- THEORY-2077
- THEORY-212
- THEORY-2133
- THEORY-2135
- THEORY-2138
- THEORY-2134
summary: >-
  The third link the owner asked for. The record's rate-difference claims
  ([CLAIM-478](CLAIM-478.md) version 5, [CLAIM-781](CLAIM-781.md)) say levels form where rates differ
  between groups by more than they vary within, and a slow level acts as a
  constraint on a fast one. Network parameterizations set exactly such
  exponents with width: the lazy limit, where hidden features barely move
  while the output is fit ([THEORY-813](../theory.d/THEORY-813.md); Chizat and colleagues), is a
  two-level hierarchy with frozen features as constraints; μP removes the
  width-growing differences. Version 2 rests on the readings of 2026-11-21, which correct it where
  noted: μP removes the gap between body and readout, not differences
  among hidden layers. The wording is the assistant's (Claude, in this session);
  adopting it is the owner's call.
---
<!-- inactive-ok-file: LIT-tmp4kae5 THEORY-tmpcij35 — Proposed, Deferred or new; the readings of 2026-11-22 and the entries they bear on -->
<!-- inactive-ok-file: THEORY-2133 THEORY-2135 THEORY-2138 THEORY-2134 THEORY-2139 THEORY-212 — Proposed; readings this claim now rests on -->
<!-- inactive-ok-file: CLAIM-478 CLAIM-781 THEORY-813 THEORY-2077 CLAIM-774 CLAIM-780 — Proposed or Deferred; the claims this applies and the works it rests on until read -->

# CLAIM-775: A parameterization of a network allocates rates among its modules: it fixes the exponent with which each module's effect on its output changes per step as a power of width or depth, so the kernel regime is the case where the hidden body is slower than the readout by a factor growing with width, its features and kernel fixed and acting as a constraint on the fitting, μP is the case where no part, readout included, is slower by such a factor, and the modular norm sets the ratios among modules by hand, with width exponents fixed by each module's norm

## The claim

The owner, 2026-11-20: "i bet we can connect this time scale separation to
depth scaling in the maximal update parameterization, which would give us a
path to connect our model to the modular duality program".

**Exponents with width are the ε^U form.** Yang and Hu ([THEORY-2133](../theory.d/THEORY-2133.md))
classify parameterizations by how each layer's initialization, multiplier and
learning rate scale with width n. Each layer's update changes its output by
Θ(n^(−r_l)) (their Proposition 5.3). Write ε = 1/n: the layer rates are
ε^(r_l), the form of the record's rate-difference results ([CLAIM-780](CLAIM-780.md),
[CLAIM-781](CLAIM-781.md)), with one exponent per module. The rate is of a layer's
effect on its output per step, not of its weights.

**The kernel regime is a two-level hierarchy.** A nontrivial stable
parametrization "is in kernel regime iff r > 0", which fixes all features and
feature kernels while the output changes by Θ(1) ([THEORY-2133](../theory.d/THEORY-2133.md)). In the
NTK parametrization every hidden layer is at ε^(1/2) and the readout at
Θ(1). In [CLAIM-478](CLAIM-478.md)'s terms the hidden body is a slow level whose fixed
kernel constrains the fast fitting. Two corrections from the readings: the
fixed hidden layers are not idle, since their vanishing changes still reach
the output through the initial readout; and the separation is proved only
over training times independent of width. Chizat and colleagues
([THEORY-2135](../theory.d/THEORY-2135.md)) give the same separation by a different route: scaling the
output by α makes the whole parameter vector and its tangent kernel move by
O(1/α) while the output is fit, readout included, so their two levels are
the output and the parameters, not hidden layers and readout. The per-layer
form at finite size is Dominé and colleagues' ([THEORY-212](../theory.d/THEORY-212.md)): unbalanced layer
scales put the larger layer near its initialization with a static kernel. [THEORY-2077](../theory.d/THEORY-2077.md) (Anguita and
colleagues) shows the same thing at finite size: the relative scale of the
layers' initialization places fine-tuning in regimes that trade reuse of
features against learning new ones.

**μP removes the gap.** μP is the unique stable parametrization with every
r_l = 0 and the readout updated and initialized maximally ([THEORY-2133](../theory.d/THEORY-2133.md)):
no part, readout included, is slower by a width-growing factor. Uniformity
among the hidden layers is not what it adds: parametrizations with a uniform
body form an edge from μP (r = 0) to NTP (r = ½). The spectral condition
([THEORY-2139](../theory.d/THEORY-2139.md)) states μP as spectral norms of weights and updates of order
√(fan-out/fan-in), "the unique maximal scaling"; equal order across layers is
what the maximal scaling gives, not what feature learning requires.

**Lazy within, learning across.** Under Depth-μP each two-layer block's
interior is in the kernel regime while the network learns features across
blocks ([THEORY-2134](../theory.d/THEORY-2134.md), §9.2): lazy and feature-learning dynamics at two
scales at once.

**The modular norm sets the allocation.** The modular norm ([THEORY-2138](../theory.d/THEORY-2138.md))
gives each module a mass that bounds its share of the output's change
(Proposition 3), forcing "individual layers to learn at specified, regulated
rates"; "Setting an atom's mass to zero has the effect of freezing its
weights", the limiting case of a slow module as constraint. Masses set
ratios among modules and their share with depth; width exponents come from
each atom's norm, √(d_out/d_in) for a linear layer. The paper aims at
balance and says nothing of levels. Within a layer,
modular dualization equalizes rates across singular directions, which in a
linear network reverses and compresses the staged hierarchy of learning
([CLAIM-774](CLAIM-774.md)).

## What it does not say

- Not that the record's tree theorem applies to training. [CLAIM-780](CLAIM-780.md) is
  about a Markov chain moving among states; training is a flow over
  parameters. What carries over is the rate-difference claim, that slow
  modules constrain fast ones and levels form where differences between
  groups beat those within.
- Not that one parameterization is better. The claim is about the structure
  of the dynamics each one produces; which to use is the anthology's
  business ([ADR-048](../decisions.d/ADR-048.md)).
- The readings of 2026-11-21 do not meet defeaters (a) or (b); both are
  stated for trained networks at width-independent times.

## Note of 2026-11-22: Dandi and colleagues, read

Dandi and colleagues ([LIT-2983](../literature.d/LIT-2983.md), [NOTE-tmpdac0o](../notes.d/NOTE-tmpdac0o.md), [THEORY-tmpcij35](../theory.d/THEORY-tmpcij35.md)):
**background.** The paper's regime is the maximal-update parametrization's
step size, η = Θ(d), against Moniri and colleagues' smaller steps
([LIT-tmp4kae5](../literature.d/LIT-tmp4kae5.md)), and the difference shows in the spectrum: finitely many
spikes beside the random-features bulk at smaller steps, a reshaped bulk at
the maximal one. A parametrization allocating rates thus also sets what
the learned spectrum looks like. A note, no relation.
