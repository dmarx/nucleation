---
number: 813
status: Proposed
formerly:
- THEORY-tmpit8ng
promote_when: 'A result beyond the one-dimensional case where the NTK and the NNGP differ by more than a within-class rescaling. That could be a derivation for multi-dimensional or multi-class data, or a measurement of NC1, with a stated metric, on networks trained in a verified lazy regime (the tangent kernel measured to stay fixed) on real data. The measurement should show NC1 staying at its initial value while the same architecture, trained out of the lazy regime, collapses. The account is refuted by a lazy-regime network, kernel verified static, whose hidden features'' NC1 falls substantially below its value at initialization. More Gaussian-mixture simulations of NNGP against NTK cannot settle it, and neither can finite networks whose regime is not checked.'
title: 'Training a wide network in the lazy, kernel regime does not make its features more collapsed than at initialization, so neural collapse, where it occurs, is something only feature learning produces'
version: 2
history:
- version: 2
  date: '2026-11-20'
  note: >-
    A dated note: CLAIM-775 reads the lazy regime as a
    separation of rates between features and fit. No change of status or title.
tags:
- learning-theory
- representation-learning
date: '2026-10-20'
source:
- LIT-985
summary: >-
  The general reading that [THEORY-294](THEORY-294.md) held before the
  promotion audit narrowed it to the one-dimensional, zero-bias, two-class
  case it proves. Kothapalli and Tirer (2024),
  [LIT-985](../literature.d/LIT-985.md), read in
  [NOTE-774](../notes.d/NOTE-774.md), draw it as their conclusion: the lazy
  regime does not collapse anything, so the data-dependence of collapse has
  to come from a kernel that moves with the data. Beyond the solved case
  their support is simulation on two-class Gaussian data, where the NTK
  comes out less collapsed than the NNGP. Filed under
  [ADR-047](../decisions.d/ADR-047.md) v4 so the wide form stays a thesis
  evidence can confirm or reject.
extends:
- THEORY-294
answers:
- QUESTION-192
---
<!-- inactive-ok-file: THEORY-tmpcij35 — Proposed, Deferred or new; the readings of 2026-11-22 and the entries they bear on -->
<!-- inactive-ok-file: CLAIM-775 CLAIM-478 — Proposed; filed in the contribution of 2026-11-20 on μP, depth scaling and modular duality -->
<!-- inactive-ok-file: THEORY-tmp8sxta — Proposed, Deferred or new; the readings of 2026-11-22 (Wang, Wu and Fan; Yang, Steinhardt and Hu; Ansuini and colleagues; Cai and colleagues; Martínez-Sánchez and colleagues), their arguments, and the entries they bear on -->

# THEORY-813: Training a wide network in the lazy, kernel regime does not make its features more collapsed than at initialization, so neural collapse, where it occurs, is something only feature learning produces

## Source

Kothapalli and Tirer (2024), [LIT-985](../literature.d/LIT-985.md), read in [NOTE-774](../notes.d/NOTE-774.md): Theorem 5.1 (the solved case, claim C2) and Figures 2–3 (claim C3, "the NTK is not more collapsed than the NNGP in higher dimensions", moderate: Gaussian data, two classes, 10 draws).

## What is asserted, and by whom

The thesis is that lazy training never lowers within-class variability below its value at initialization, for wide networks in general and not only in the case where the tangent kernel is a within-class rescaling of the initialization kernel. Collapse is then a signature of feature learning. Kothapalli and Tirer state it as the moral of their analysis; the abstract states the higher-dimensional part as an empirical finding.

## What the record holds toward it

- [THEORY-294](THEORY-294.md) (Active): the exact result for one-dimensional data with the two classes on opposite sides of the origin and zero bias, where the equality is close to built in.
- The paper's Gaussian simulations in higher dimension, which find the NTK less collapsed than the NNGP, consistent with the thesis but not a test of lazy training of finite networks.

## What would confirm or reject it

A verified-lazy network on real data whose NC1 stays at its initial value while the same architecture, trained out of the lazy regime, collapses would confirm it; one whose NC1 falls well below its initial value with the kernel verified static would reject it. [QUESTION-192](../questions.d/QUESTION-192.md) asks the same thing as a question; this entry is the answer Kothapalli and Tirer propose.

## Note of 2026-11-19: Poole and colleagues, read
A parallel ([NOTE-2099](../notes.d/NOTE-2099.md)): Poole and colleagues' layerwise covariance recursion is, in substance, the kernel recursion of the infinite-width regime; they predate the name and do not make the identification.

## Note of 2026-11-20: the lazy regime as two levels

[CLAIM-775](../claims.d/CLAIM-775.md) reads the lazy, kernel regime this reading describes as a
separation of rates: the hidden features move by a vanishing amount while the
output is fit, so the features act as a slow level constraining the fast
readout, in the sense of [CLAIM-478](../claims.d/CLAIM-478.md) (version 5). Feature learning, which this
reading says alone produces neural collapse, is then what happens when the
hidden layers are not slower than the readout by a factor that grows with
width. A bearing of use; nothing here tests the reading.

## Note of 2026-11-22: Dandi and colleagues, read

Dandi and colleagues ([LIT-2983](../literature.d/LIT-2983.md), [NOTE-tmpdac0o](../notes.d/NOTE-tmpdac0o.md), [THEORY-tmpcij35](THEORY-tmpcij35.md)): **a
parallel.** Learned structure appears only off the kernel regime: after a
maximal-update step, not in random features. No relation.

## Note of 2026-11-22: Yang, Steinhardt and Hu, read

Yang, Steinhardt and Hu (LIT-2957, NOTE-tmpl260d, THEORY-tmp8sxta): **a parallel.**
Both concern the data's role in collapse. Yang and colleagues are the
feature-learning side: the residual variation is structured by the input,
against the unconstrained-feature model, which "completely ignores the role
of the input data". No kernel-regime comparison. A note, no relation.
