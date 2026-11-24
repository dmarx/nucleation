---
status: Proposed
title: 'In a linear model of a representation''s cultural salience and its material or organizational realization, each decaying alone and each raising the other, the representation''s circulation amplifies its own realization exactly when the product of the two gains exceeds the product of the two decay rates, so hyperstitional efficacy is a property of the coupling between a representation and the activity that can realize it, not of the representation; it is the continuous-time form of the meaning–authority condition'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the stability condition (a case with α, β ≥ 0 and μ, ν > 0
  in which the zero state of ṁ = αr − μm, ṙ = βm − νr is unstable while
  αβ ≤ μν, or stable while αβ > μν); or, for the reading, a showing that
  representations whose circulation helped bring about what they say
  differ from those whose circulation did not in a property of the
  representation alone, with the gains of the activity that realizes them
  held fixed.
tags:
- complex-systems
- society-and-governance
- epistemology
date: '2026-11-24'
line:
- distributed-agency
- formal-apparatus
summary: >-
  A10 §4 of the exchange "Memes, Contracts, and Systemic Normativity"
  (ChatGPT, 2026-11-24), at the owner's U9 ("relate to hyperstition").
  [CLAIM-426](CLAIM-426.md)'s note of 2026-10-30 says the read sources (Land, Soros) give
  "no condition for telling which judgements' circulation helps make them
  true", and [NOTE-1378](../notes.d/NOTE-1378.md) finds Land's "favorable" circumstances left
  unstated. A10 gives a condition in a model: αβ > μν. The algebra and the
  mapping to [CLAIM-330](CLAIM-330.md) are checked with python3 -I. It is a condition on
  gains in a model, not a way to measure them. The wording is A's
  (ChatGPT, in the exchange 'Memes, Contracts, and Systemic Normativity');
  adopting it is the owner's call.
---

<!-- inactive-ok-file: CLAIM-426 CLAIM-tmpnws9d — Proposed; the held claim whose open item this narrows, and the gap fill filed with it -->

# CLAIM-tmpvic6m: In a linear model of a representation's cultural salience and its material or organizational realization, each decaying alone and each raising the other, the representation's circulation amplifies its own realization exactly when the product of the two gains exceeds the product of the two decay rates, so hyperstitional efficacy is a property of the coupling between a representation and the activity that can realize it, not of the representation; it is the continuous-time form of the meaning–authority condition

## The claim

A10 §4: "Consider a representation whose cultural salience is m, and
whose material or organizational realization is r." The model is
ṁ = αr − μm, ṙ = βm − νr, with α "the extent to which realization
reinforces cultural salience", β "the extent to which salience facilitates
realization", and μ, ν "decay or countervailing processes". "The feedback
loop becomes unstable around the zero equilibrium when αβ > μν." "Neither
cultural salience nor material realization need be independently
self-amplifying. Their coupling can produce amplification." And: "The
important observation is that hyperstitional efficacy is not a property of
m alone. It depends on the coupling between cultural expression and
realizable organizational activity." Land's favourable circumstances
"can therefore become an explicit object of investigation: receptivity,
resources, coordination mechanisms, feedback gains, maintenance processes
and competing constraints."

**The derivation.** The Jacobian is [[−μ, α], [β, −ν]], with trace
−(μ + ν) < 0 and determinant μν − αβ. A real 2×2 system with negative
trace has an eigenvalue with positive real part exactly when its
determinant is negative, so the zero state is unstable exactly when
αβ > μν. Checked with `python3 -I` on 100,000 random draws with
α, β ∈ [0, 2] and μ, ν ∈ (0, 2]: no mismatch.

**The mapping to [CLAIM-330](CLAIM-330.md).** The discrete map x_{t+1} = Ax corresponds to
ẋ = (A − I)x. With A = [[α′, β′], [γ′, δ′]], A − I has determinant
(1 − α′)(1 − δ′) − β′γ′, so μ = 1 − α′, ν = 1 − δ′ and [CLAIM-330](CLAIM-330.md)'s
β′γ′ > (1 − α′)(1 − δ′) becomes αβ > μν, under [CLAIM-330](CLAIM-330.md)'s conditions
(nonnegative entries, α′, δ′ < 1). A10's "continuous-time analogue" is
exact.

**A10's bounded version.** A10's interactive model adds saturation,
ṁ = αr(1 − m) − 0.5m, ṙ = βm(1 − r) − 0.5r, so μν = 0.25. Rerun as
A10 codes it: at αβ = 0.64 a seed (m, r) = (0.14, 0.015) settles at
0.375 each; at αβ = 0.24 and 0.09 it decays to zero; at αβ = 0.27 it
settles low, near 0.035 and 0.040. Started near saturation with
αβ = 0.225 or 0.24 it still decays: in this model there is no second
stable state below the threshold.

## What it does not say

- **Not that hyperstition is a mechanism the record lacked.** [CLAIM-426](CLAIM-426.md)
  already says Merton's self-fulfilling prophecy and the looping effects of
  [CLAIM-402](CLAIM-402.md) run "on the same circuit". The claim adds a condition, in a
  model, for when the circuit amplifies.
- **Not a way to tell, in a case, which judgements' circulation helps make
  them true.** The gains are not observed; the condition says what would
  have to be measured. [CLAIM-426](CLAIM-426.md)'s open question is narrowed, not
  answered.
- **Not that the realization lasts.** In this model realization is held up
  by circulation; when salience decays, so does realization. Persistence
  after circulation stops needs more ([CLAIM-tmpnws9d](CLAIM-tmpnws9d.md)).
- **Not a law of cultural evolution.** A10: "This construction
  demonstrates a possible mechanism, not an empirically established law of
  cultural evolution."
