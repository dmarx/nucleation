---
status: Active
title: 'Maintained connector shows ignition and collapse'
statement: >-
  With a supply multiplying its production terms, a maintained connector
  shows the ignition threshold, the collapse below a supply fold and the
  outage after which restoring the supply does not relight it, while
  supplied repair matched to the same state shows none of them; where the
  supply enters only the capacities' production, its fold is the damage fold
  relabelled
version: 2
history:
- version: 2
  date: '2026-11-25'
  note: >-
    Promoted to Active under the owner's delegation of 2026-11-24
    ("handle the fixes for the twelve ... use your best judgement"),
    as the status pass of 2026-11-24 and the reruns of 2026-11-25
    applied it to independently recomputed demonstrated claims and
    executed studies, in the recomputation pass of 2026-11-25
    (LEAD-tmpc0rqa). Rerun by a session other than the filer's: the
    filer's script
    scratch/manuscripts/governance-of-becoming/analysis/case189_supply_parameter.py
    prints its dated output of 2026-11-25 byte for byte, and an
    independent check written from the claim's and CASE-189's stated
    model, scratch/formal/case189_supply_check.py, reproduces every
    figure (s* = 0.6491 and 0.8528, 0.5914 = 1/(1 + d*) and 0.8280,
    outage limits 1.513 and 1.922, gaps 0.977 and 0.989, the control's
    3.337 and 2.13). ADR-057: its one ground, CASE-189, is Active; it
    rests on no claim; no objection targets it; nothing meets its
    defeated_if.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in
  scratch/manuscripts/governance-of-becoming/analysis/case189_supply_parameter.py
  whose correction, at the parameters run, removes the interior saddle
  with the supply on, turns the collapse below s* into a gradual decline,
  lets the supply restored after a long outage relight the connector, or
  gives the matched supplied repair a threshold, a fold or an outage
  limit. Or a showing that CASE-189's construction is misreproduced, so
  that the extension is of another system. Not defeated by the absence of
  a measured organization, since the claim is about the model, nor by an
  outside crew producing the same state-dependent terms, which the claim
  does not exclude.
tags:
- complex-systems
- individuation
date: '2026-11-25'
line:
- distributed-agency
grounds:
- CASE-189
corroborates:
- CLAIM-604
complements:
- CLAIM-521
summary: >-
  The assistant's computation for the manuscript governance-of-becoming,
  Article 1 (gap G1.2; item B17 of the audit of what was left out,
  2026-11-25), filed under write-manuscript step 6. [CASE-189](../cases.d/CASE-189.md)'s
  Construction 2 with a supply s multiplying its production terms shows
  all three of [CLAIM-604](CLAIM-604.md)'s signatures: an interior saddle with the supply
  on (from 0.9 of the saddle it goes out, from 1.1 it reaches c = 3.337),
  a supply fold below which it goes out rather than declines (s* = 0.649
  at d = 0 when the supply also feeds the connector), and an outage
  limit (about 1.5 time units) after which restoring the supply does not
  relight it. Supplied repair matched to the same kept state shows none.
  Where the supply enters only the capacities' production, the fold is
  [CASE-189](../cases.d/CASE-189.md)'s damage fold relabelled, s* = (1 + d)/(1 + d*) = 0.5914 at
  d = 0, so collapse in a supply and collapse in damage are one
  signature; at either fold the coupling's spectral gap stays near 0.98.
  Checked with python3 -I; the script reproduces [CASE-189](../cases.d/CASE-189.md)'s own figures
  first and prints "checks pass". The wording is the assistant's (Claude,
  in this session); adopting it is the owner's call.
---

<!-- inactive-ok-file: CLAIM-606 CASE-265 — cited with their standing; the claim it corroborates, the split it extends, the limits on what the signatures identify, and the nearest held construction -->

# CLAIM-tmpv6tw7: Maintained connector shows ignition and collapse

## The gap it fills

Article 1's G1.2 asks whether [CASE-189](../cases.d/CASE-189.md)'s maintained connector, a
construction filed for another purpose, shows [CLAIM-604](CLAIM-604.md)'s signatures of
maintained organization when a supply is put into it. [CASE-189](../cases.d/CASE-189.md) had no
supply parameter and no kept script. [CASE-265](../cases.d/CASE-265.md) has a supply, but it is a
different two-variable model with no supply fold or outage figures.

## The construction

`scratch/manuscripts/governance-of-becoming/analysis/case189_supply_parameter.py`
(deterministic RK4, run with `python3 -I`), output of 2026-11-25 beside
it. Step 0 reproduces [CASE-189](../cases.d/CASE-189.md)'s figures from the case text (Construction
1: 0.382 and 2.618; Construction 2's fold at c* = 1.1578, q* = 0.8545,
d* = 0.6908) and asserts them. The supply multiplies the production
terms: arm A in all three, arm B in the two capacity terms only; the
encounter term stays outside it. The control is supplied repair as in
[CLAIM-597](CLAIM-597.md), production s·K regardless of state, K matched to arm A's kept
state. At s = 1 both arms are [CASE-189](../cases.d/CASE-189.md) exactly. The sweep points,
outages (0.5 and 5 units), starts (0.9 and 1.1 of the saddle) and the
thresholds for "out" and "kept" were set before the run, and the
expectation was written in the script's docstring before it.

## Results (d = 0)

1. **Ignition threshold with the supply on**: below the saddle it goes
   out, above it reaches the kept state, in both arms.
2. **Collapse, not decline**: arm A's fold is s* = 0.6491 (0.8528 at
   d = 0.4); just above it the connector still holds c = 1.47, just
   below it goes out. Arm B's fold is s* = 0.5914 = 1/(1 + d*) to 1e-6
   (0.8280 at d = 0.4), at [CASE-189](../cases.d/CASE-189.md)'s (c*, q*).
3. **Outage**: after 0.5 units off it relights, after 5 it does not; the
   limit is about 1.51 units in arm A and 1.92 in arm B.
4. **Control**: no threshold (it reaches c = 3.337 from zero), a linear
   decline (c = 2.13 at s = 0.639, where arm A is already out), and full
   return after outages of 5 and 30 units.
5. **The coupling's spectral gap** at the supply fold is 0.977 (arm A)
   and 0.989 (arm B), so [CLAIM-521](CLAIM-521.md)'s split between coupling and
   maintenance holds at a supply fold too.

The expectation held, with one correction recorded in the output: s and
d enter arm B only as s/(1 + d) at the equilibria, not in the dynamics.

## What it does not say

- That the upkeep belongs to the organization: which terms are internal
  is stipulated, and an outside crew delivering the same state-dependent
  production gives the same equations ([CLAIM-522](CLAIM-522.md), [CLAIM-606](CLAIM-606.md)).
- Anything thermodynamic: the production terms are irreversible and
  unpaid.
- Anything beyond one fictional parameter set, or about a measured
  organization.

## Standing

Proposed. The computation has been run by its author and rerun once by
the filing session; no other session has checked it.


## Note of 2026-11-25: rerun by a session other than the filer's

Rerun on 2026-11-25 by the assistant, a session other than the filer's, in the recomputation pass of [LEAD-tmpc0rqa](../leads.d/LEAD-tmpc0rqa.md), at the owner's go-ahead of 2026-11-25 ("go ahead with the reruns"). Two checks. The filer's script, run with python3 -I, prints its dated output `case189_supply_parameter.2026-11-25.txt` byte for byte, ending "checks pass". An independent check, `scratch/formal/case189_supply_check.py` (numpy and scipy), written from this claim's and [CASE-189](../cases.d/CASE-189.md)'s stated model and not from the script, finds the folds from the symmetric equilibrium curves by bounded minimization, the outage limits by bisection and the gap as q c: kept state c = 3.3371 and saddle 0.5212 at s = 1; ignition from 1.1 and not 0.9 of the saddle in both arms; arm A's fold s* = 0.6491 (0.8528 at d = 0.4), with c = 1.466 at s* + 0.01 and extinction at s* − 0.01; arm B's 0.5914 = 1/(1 + d*) (0.8280); outage limits 1.513 and 1.922; gaps 0.9773 and 0.9894 at the folds; the control reaching 3.337 from zero, c = s K_c (2.13 at s = 0.639) and returning fully after a 30-unit outage. Everything reproduces. "Standing" above, that no other session had checked it, is out of date. Promoted in the same pass (history, version 2). The note is the assistant's (Claude, in this session).
