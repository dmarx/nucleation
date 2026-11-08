---
number: 228
status: Proposed
formerly:
- CASE-tmpnlf5c
title: 'Reporting by total output against reporting that also records breaches of the hours cap: under self-scored regime selection the aggregate regime is always kept and records no violation while one occurs, and the adequate regime keeps itself only when the penalty on a recorded breach exceeds the convenience of breaching plus the cost of reporting'
version: 3
history:
- version: 2
  date: '2026-11-07'
  note: >-
    Its `illustrates` now points to SYNTHESIS-002, the synthesis
    CLAIM-624 was moved into (ADR-076), because it is about
    the current account and not its archived predecessor. The text is
    unchanged and still names the claim where it was written against it.
- version: 3
  date: '2026-11-08'
  note: >-
    The syntheses this pointed at returned to CLAIM at the decision that
    a SYNTHESIS is an account (ADR-084), so `illustrates` names
    CLAIM-624 for SYNTHESIS-002. No other change.
standing: fictional
kind: construction
tags:
- society-and-governance
- self-governance
- ethics
date: '2026-11-07'
line:
- distributed-agency
variant_of:
- CASE-110
illustrates:
- CLAIM-624
summary: >-
  A62 §4 of the second share of the exchange "Individuation, Possibility,
  and Disposition" (2026-11-06 to 07), extending [CASE-110](CASE-110.md)'s two workers
  with a convenience benefit κ for the over-cap allocation, a penalty λ
  on a recorded breach, an administrative cost c for adequate reporting,
  and regime selection by scores computed under the current regime. The
  reader reran it with exact rationals: the aggregate regime is always
  self-stable, with actual violation 1 and recorded violation 0, and the
  adequate regime is self-stable only when λ > κ + c, which A omits. So
  self-scoring makes both regimes self-confirming where λ > κ + c, and
  history decides. The construction is A's, corrected by the reader;
  adopting it is the owner's call.
---
<!-- inactive-ok-file: ADR-076 — filed from the same exchange, Proposed -->
<!-- inactive-ok-file: CLAIM-624 — filed from the same exchange, Proposed; the thesis this case illustrates -->
<!-- inactive-ok-file: CLAIM-445 — Proposed; the held reproductive form -->

# CASE-228: Reporting by total output against reporting that also records breaches of the hours cap: under self-scored regime selection the aggregate regime is always kept and records no violation while one occurs, and the adequate regime keeps itself only when the penalty on a recorded breach exceeds the convenience of breaching plus the cost of reporting

## The case

A, at A62 §4 of the exchange "Individuation, Possibility, and Disposition",
second share (https://chatgpt.com/share/6aeea2bc-d280-83e9-ac1f-f6772adf263c):
"We can extend Nucleation's worker-hours example into a small model."
[CASE-110](CASE-110.md)'s two workers produce 12 units, by a = (6, 6), within the
eight-hour cap, or b = (10, 2), past it. The institution's decision score
is

V_r(u) = 12 + κ·1[u = b] − λ·r·1[u = b], with λ > κ,

where r = 0 is aggregate reporting ("registers only total output") and
r = 1 is adequate reporting ("also registers violations of the
working-hours agreement"). Under r = 0, b is chosen; under r = 1, a is.

Reproduction: "the institution selects reporting systems by rewarding
managers for scores computed under the current scheme, while maintaining
more detailed reporting has an administrative cost." Call that cost c. A
regime is kept when its own score, net of c for r = 1, is at least the
alternative's scored under the current regime.

## What the rerun shows

The reader's script (exact rationals over a grid of κ, λ, c with λ > κ)
found:

- **The aggregate regime is always self-stable**: 12 + κ against 12 − c.
  At it, actual violation = 1 and recorded violation = 0, as A says.
- **The adequate regime is self-stable exactly when λ > κ + c**: 12 − c
  against 12 + κ − λ. All 1,800 grid cases off the tie matched; the 120
  mismatches are all at λ = κ + c, where the two scores are equal.
- Scoring both regimes independently under r = 1 also keeps r = 1 exactly
  when λ > κ + c. What self-scoring adds is that it **also** keeps r = 0.
- Δ_occlusion, with the violation indicator as loss (κ = 1, λ = 3), is
  E[L | do(r = 0)] − E[L | do(r = 1)] = 1.

**Correction (the reader's).** A's heading promises "two organizational
equilibria", and A writes: "If no independent commitment protects the
adequate reporting system, internal incentives may continually favor the
aggregate one." That is true from r = 0 always, but from r = 1 only when
c > λ − κ. Where λ > κ + c the adequate regime protects itself under the
same self-scoring, and there are two equilibria; where κ + c > λ the
aggregate regime is the only one.

So the construction shows bistability: history decides which regime an
institution is in, as in [CLAIM-463](../claims.d/CLAIM-463.md)'s hysteresis, and the regime is judged
by evidence that passes through it, the condition [CLAIM-342](../claims.d/CLAIM-342.md) names. A
one-off move to adequate reporting can sustain itself when λ > κ + c.

## What it cannot show

It is fictional, so it shows what is coherent, not what is common. A's
own hedge: "This is a **candidate self-maintaining harmful equilibrium**,
conditional on the specified governance and reproduction rules." The
reproduction is one comparison of scores, not a productive cycle, so it
does not show organizational closure ([TERM-070](../terms.d/TERM-070.md), [CLAIM-516](../claims.d/CLAIM-516.md)). Nor does it
show anything normative: that b is a wrong is stipulated by the cap. Its
form is held in [CLAIM-445](../claims.d/CLAIM-445.md)'s protective regime, which shifts the evidence
used to judge it.
