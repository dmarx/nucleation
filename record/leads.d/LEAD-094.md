---
number: 94
status: Open
formerly:
- LEAD-tmpha13d
title: 'Read the dynamics batch on scale separation and localized structure, with Ott and Antonsen''s reduction as a candidate defeater'
version: 1
stage: idea
priority: high
method:
- reading
tags:
- complex-systems
- individuation
date: '2026-11-19'
line:
- distributed-agency
advances:
- CLAIM-478
- CLAIM-157
- QUESTION-281
- CLAIM-481
- CLAIM-405
summary: >-
  A central claim, a named defeater, and mostly free sources never tried.
  Named in [CLAIM-478](../claims.d/CLAIM-478.md). Filed by the backlog audit of 2026-11-19.
---
<!-- inactive-ok-file: CLAIM-1058 CLAIM-1088 ARG-220 THEORY-2291 THEORY-2300 THEORY-2292 THEORY-2301 THEORY-2298 THEORY-2288 THEORY-2279 — Proposed or new; filed for this lead on 2026-11-22 -->
<!-- inactive-ok-file: CLAIM-478 LIT-1638 LIT-1642 LIT-2254 LIT-2255 — Deferred, Proposed, Unfetched; cited in the backlog audit of 2026-11-19 -->

# LEAD-094: Read the dynamics batch on scale separation and localized structure, with Ott and Antonsen's reduction as a candidate defeater

## What it would do

Read Ott and Antonsen (2008, arXiv) first as the candidate defeater of
[CLAIM-478](../claims.d/CLAIM-478.md), then Fenichel and the never-tried arXiv works; Knobloch needs a
closed copy.

Where the record names it:

- [CLAIM-478](../claims.d/CLAIM-478.md): "A further candidate for defeater (a)."

## The works

- [LIT-2248](../literature.d/LIT-2248.md) (Deferred): Ott 2008, "Low Dimensional Behavior of Large
  Systems of Globally Coupled Oscillators"
- [LIT-1638](../literature.d/LIT-1638.md) (Unfetched): Fenichel 1979, "Geometric singular perturbation
  theory for ordinary differential equations"
- [LIT-1642](../literature.d/LIT-1642.md) (Unfetched): Knobloch 2015, "Spatial Localization in
  Dissipative Systems"
- [LIT-2231](../literature.d/LIT-2231.md) (Deferred): Schmietendorf 2026, "How causal is “circular
  causality”?"
- [LIT-2241](../literature.d/LIT-2241.md) (Deferred): Caprioglio 2024, "Emergence of metastability in
  frustrated oscillatory networks: the key role of hierarchical modularity"
- [LIT-2244](../literature.d/LIT-2244.md) (Deferred): Augustsson 2026, "Self-organizing Chimera States in
  Adaptive Networks"
- [LIT-2252](../literature.d/LIT-2252.md) (Deferred): Müller 2026, "Self-organization and circular
  causation as synergetic foundations of social interaction: a multilayer
  network perspective"
- [LIT-2254](../literature.d/LIT-2254.md) (Deferred): Yadav 2026, "Timescale-induced synchronization of
  contrarians in adaptive dynamical networks"
- [LIT-2255](../literature.d/LIT-2255.md) (Deferred): Haken 1975, "Cooperative phenomena in systems far
  from thermal equilibrium and in nonphysical systems"
- [LIT-2257](../literature.d/LIT-2257.md) (Deferred): Kaur 2026, "Using timescale as a state coordinate
  reveals the metastable geometry of behavior"
- [LIT-2266](../literature.d/LIT-2266.md) (Deferred): Hancock 2024, "Metastability demystified — the
  foundational past, the pragmatic present and the promising future"
- [LIT-2268](../literature.d/LIT-2268.md) (Deferred): Lee 2025, "Topological Flowscape Reveals State
  Transitions in Nonreciprocal Living Matter"

## What would count

An exact reduction that keeps what [CLAIM-478](../claims.d/CLAIM-478.md) says must be lost meets its
defeater (a).

## Note of 2026-11-22: the batch read, and the verdict filed as alternatives

Carried out by a delegated lead worker on the branch
claude/lead-094-dynamics-batch; the progress file is
scratch/studies/lead-094/PROGRESS.md.

**Ott and Antonsen first.** The 2008 paper ([LIT-2248](../literature.d/LIT-2248.md), [NOTE-2385](../notes.d/NOTE-2385.md)) was
read in full, with its 2009 sequel registered and read as a supplement
([LIT-3163](../literature.d/LIT-3163.md), [NOTE-2378](../notes.d/NOTE-2378.md)), since the 2008 paper leaves open whether its
manifold attracts. The reduction is exact on an invariant manifold and
needs no small parameter; the sequel shows the manifold attracts the order
parameter whenever frequencies are spread, with no condition on rates. A
check ([CLAIM-1145](../claims.d/CLAIM-1145.md), scratch/studies/lead-094/oa_invariance.py) shows
the invariance needs coupling through the first harmonic alone.

**The verdict**, on "What would count" above, is filed as two alternatives
with the inference between them in [ARG-220](../arguments.d/ARG-220.md):

- [CLAIM-1058](../claims.d/CLAIM-1058.md) (leaned to): the reduction does not meet [CLAIM-478](../claims.d/CLAIM-478.md)'s
  defeater (a). Its persistence is an exact invariance, the limit of
  slowness, as [CLAIM-478](../claims.d/CLAIM-478.md)'s note of 2026-11-02 ruled for conservation laws,
  and the class is narrow; it is an instance of the non-necessity
  [CLAIM-478](../claims.d/CLAIM-478.md) already concedes. Caprioglio and Berthouze ([THEORY-2291](../theory.d/THEORY-2291.md))
  support it: off all-to-all coupling, their Ott–Antonsen-based reduction
  held only with a large spectral gap.
- [CLAIM-1088](../claims.d/CLAIM-1088.md): it meets (a) within first-harmonic oscillator
  populations, since the approach needs no faster rate and the
  off-manifold parts are averaged out rather than held by anything slower;
  [CLAIM-478](../claims.d/CLAIM-478.md) would then name invariant-manifold closure by phase mixing as a
  route on which rate differences do no work.

They part on how to read "slower or more persistent" in (a), and on what
counts as typical. Choosing is the owner's.

**The rest of the batch.** Read: Caprioglio and Berthouze ([LIT-2241](../literature.d/LIT-2241.md),
[THEORY-2291](../theory.d/THEORY-2291.md)), Augustsson and colleagues ([LIT-2244](../literature.d/LIT-2244.md), [THEORY-2300](../theory.d/THEORY-2300.md)),
Schmietendorf ([LIT-2231](../literature.d/LIT-2231.md), [THEORY-2292](../theory.d/THEORY-2292.md)). Skimmed: Kaur, Jain and Berman
([LIT-2257](../literature.d/LIT-2257.md), [THEORY-2301](../theory.d/THEORY-2301.md)), Lee and colleagues ([LIT-2268](../literature.d/LIT-2268.md),
[THEORY-2298](../theory.d/THEORY-2298.md)), Müller ([LIT-2252](../literature.d/LIT-2252.md), [THEORY-2288](../theory.d/THEORY-2288.md)), Hancock and
colleagues ([LIT-2266](../literature.d/LIT-2266.md), [THEORY-2279](../theory.d/THEORY-2279.md)). No lawful copy: Yadav and
colleagues ([LIT-2254](../literature.d/LIT-2254.md)) and Haken 1975 ([LIT-2255](../literature.d/LIT-2255.md)), now Unavailable. Blocked
again on 2026-11-22: Fenichel ([LIT-1638](../literature.d/LIT-1638.md), HTTP 403) and Knobloch ([LIT-1642](../literature.d/LIT-1642.md),
a Cloudflare challenge), still Unfetched.

**What remains.** The owner's choice between [CLAIM-1058](../claims.d/CLAIM-1058.md) and
[CLAIM-1088](../claims.d/CLAIM-1088.md); a copy of Fenichel, Knobloch, Haken or Yadav, if one can
be supplied; and the full reading of the skimmed works, if wanted. The
status and stage of this lead are unchanged.
