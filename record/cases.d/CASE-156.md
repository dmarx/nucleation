---
number: 156
status: Active
formerly:
- CASE-tmpydmf8
title: 'A legibility filter as the ν of the meaning–authority–legibility model: in a safe world where 15% of raw cues are alarms, an admission rule P(admit | y, r) = σ(c + χry) with c = 0 and χr = 2 admits 88.1% of alarms and 11.9% of reassurances, so 56.6% of the admitted record is alarms with the world and the sensors unchanged; at symmetry the mean admitted evidence is χσ′(c)r to first order, so ν = η_m χ σ′(c); and r_t = λᵗr₀ + ε Σ λ^(t−1−j) a_j is an exponentially weighted history of authority'
version: 2
history:
- version: 2
  date: '2026-10-25'
  note: >-
    A dated note added: the U32 app's carried update rule, re-run,
    reproduces A22's reported numbers; lock-in needs χ above about 9.8, and
    the shortest correcting audit grows with χ. The case is unchanged.
standing: stipulated
kind: construction
tags:
- complex-systems
- self-governance
- epistemology
date: '2026-10-24'
line: distributed-agency
variant_of:
- CASE-124
illustrates:
- CLAIM-400
- CLAIM-448
summary: >-
  From the exchange of 2026-10-24 (workbench entry of 2026-10-24,
  U18–U19). The owner: "i think we already have a three variable system
  somewhere, where the third component is described as legibility", then
  "flesh this out further". A microfoundation for one of [CASE-124](CASE-124.md)'s
  abstract couplings: selective admission of evidence, checked when filed.
  It gives r an observational semantics and reads r as the memory of past
  authority. Selection-aware inference is the control that the pathology
  has to beat.
variants:
- CASE-tmpr1vuv
---

# CASE-156: A legibility filter as the ν of the meaning–authority–legibility model: in a safe world where 15% of raw cues are alarms, an admission rule P(admit | y, r) = σ(c + χry) with c = 0 and χr = 2 admits 88.1% of alarms and 11.9% of reassurances, so 56.6% of the admitted record is alarms with the world and the sensors unchanged; at symmetry the mean admitted evidence is χσ′(c)r to first order, so ν = η_m χ σ′(c); and r_t = λᵗr₀ + ε Σ λ^(t−1−j) a_j is an exponentially weighted history of authority

## The case

**The filter.** An objectively safe environment. An independent observer
emits cues y_t ∈ {−1, +1}, +1 an alarm, with 85% accuracy, so
P(y = +1 | safe) = 0.15. The governing regime decides whether a cue enters
the record: P(k = 1 | y, r) = σ(c + χ r y). At r = 0 alarms and
reassurances are admitted equally; for r > 0 alarms are favoured. With
c = 0 and χr = 2, σ(2) = 0.881 and σ(−2) = 0.119, and

    P(y = +1 | k = 1) = 0.15·0.881 / (0.15·0.881 + 0.85·0.119) ≈ 0.566.

Alarms go from 15% of the raw stream to 56.6% of the admitted record. The
world has not changed and the sensors are as accurate as before. An
evaluator who analyses the admitted record faithfully, without modelling
the admission rule, concludes that alarms are common.

**The microfoundation.** Write the admitted evidence v_t = k_t y_t (zero
when not admitted). At a symmetric point with equally frequent raw cues,

    E[v | r] = ½σ(c + χr) − ½σ(c − χr) = χσ′(c) r + O(r³).

With the meaning update m′ = tanh(αm + βa + η_m v), the mean dynamics have,
to first order, [CASE-124](CASE-124.md)'s ν = η_m χ σ′(c). The r → m coupling is then a
mechanism, selective admission, and not a stipulated influence. [CASE-124](CASE-124.md)'s
μ, the effect of r on scoring authority ([CLAIM-400](../claims.d/CLAIM-400.md)), is a different route
and is not produced by this filter: experts whose reports fit the official
categories scored higher with no better accuracy.

**Legibility as memory of authority.** Without inputs or nonlinearity,
r_{t+1} = λr_t + εa_t unrolls to r_t = λᵗr₀ + ε Σ_{j<t} λ^(t−1−j) a_j. A
once-dominant perspective leaves reporting conventions, attentional habits
and evaluative standards that keep operating after its authority has
faded. That is one more route of amortization ([CLAIM-358](../claims.d/CLAIM-358.md)'s note of
2026-10-23), adaptive while the settlement fits and self-protecting when
it blocks revision.

## What it can show

That filtering alone can turn a mostly reassuring stream into a mostly
alarming record; that one of [CASE-124](CASE-124.md)'s couplings has a concrete
mechanism; and why, at threshold, legibility acts like stronger coupling
([CLAIM-400](../claims.d/CLAIM-400.md)'s β_eff, δ_eff) while away from it r carries a memory of its
own.

## What it cannot show

- Lock-in. A statistically sophisticated evaluator that knows the
  admission probabilities can correct for the selection, so long as the
  cues remain identifiable and have nonzero admission probability. The
  pathology needs more than filtering: the selection unmodelled,
  unaudited, or protected against correction.
- That linear instability is lock-in. [CASE-124](CASE-124.md)'s witness
  (ρ(J₂) ≈ 0.724, ρ(J₃) ≈ 1.033) shows instability of the symmetric state.
  Lock-in also needs a persistent state, measured misalignment with the
  environment, and a maintaining path through r or a.

## The mean-field witness the exchange reported

At U22 the exchange reported a deterministic mean-field run: sensor 70%
correct, danger for 100 steps then safety for 500, a Jacobian at the
neutral point with entries (0.5, 0.1, 1.25; 0.5, 0.5, 0; 0, 0.5, 0.5) and
spectral radius about 1.203, a final lean r ≈ 0.225 with about 80.2% of
admitted cues alarms in the safe phase, and a correction threshold (one
step of independent evidence did not change the regime, three did). The
script was not provided and the run is not reproduced here. The record
holds it as reported, not checked.

## Note of 2026-10-25: the reported run, checked

At U32 of the exchange of 2026-10-24, continued, the mean-field model was
published as an interactive app, and its update rule was carried inline in
the share:

    m′ = tanh(0.5m + 0.1a + 0.5e),  a′ = tanh(0.5m + 0.5a + μr),
    r′ = tanh(εa + λr),  e = qσ(χr) − (1 − q)σ(−χr),

with χ = 10, λ = ε = 0.5, μ = 0, a 70% sensor, danger for 100 steps and
safety for 500. Transcribed and run, it reproduces every number A22
reported, which this case held as reported and not checked:

- the Jacobian at the neutral point is (0.5, 0.1, 1.25; 0.5, 0.5, 0;
  0, 0.5, 0.5), with spectral radius 1.2032;
- the final lean is r = 0.2248, at which 80.2% of admitted cues are alarms
  in the safe phase;
- the coupled run ends threat-leaning (m = +0.241), neutral reporting ends
  at m = −0.237, and with χ = 0 the coupled run ends at the neutral value;
- an audit of 1 or 2 steps of neutral reporting leaves the coupled run
  threat-leaning, and 3 steps send it to the safe attractor (m = −0.601).

Two further results. With these parameters, lock-in needs χ above about
9.8: at χ = 9 the coupled run turns to safety by itself (m = −0.597), and at
χ = 4 it ends at m = −0.513. And the shortest audit that corrects grows
with χ: 3 steps at χ = 10, 4 at 12 and 5 at 16. That is [CASE-155](CASE-155.md)'s
correction threshold in this model. That the app is the same script as
A22's is inferred from the matching numbers. The run is no longer only
reported. The case is unchanged.
