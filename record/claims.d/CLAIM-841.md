---
number: 841
status: Proposed
formerly:
- CLAIM-tmpsr8r4
title: 'A power law or a scale-invariant law does not by itself indicate criticality: symmetry, flux, growth, coarsening, geometry and broad relaxation spectra each remove a characteristic scale without a tuned transition'
version: 4
history:
- version: 2
  date: '2026-11-22'
  note: >-
    Edited in place on 2026-11-22 after Broido and Clauset (LIT-2963)
    was read: the folded-in bullet "Many reported scale-free networks
    are not" is reworded to what the paper shows, a lack of statistical
    evidence, and marked as background to the thesis, since the paper
    never mentions criticality (ARG-tmp38kft). The thesis and status are
    unchanged.
- version: 3
  date: '2026-11-22'
  note: >-
    Edited in place on 2026-11-22 after Bak, Tang and Wiesenfeld
    (LIT-2992) was read (NOTE-tmpnl00y, THEORY-tmpehudh): the
    self-organized-criticality bullet under "What it does not say" now
    quotes the letter, and notes that it infers criticality from a
    straight log-log line. THEORY-tmpehudh corroborates the claim
    (ARG-tmp1zu0m). The thesis and status are unchanged.
- version: 4
  date: '2026-11-22'
  note: >-
    Edited in place on 2026-11-22 after Kardar, Parisi and Zhang
    (LIT-2978), Takeuchi and Sano (LIT-2982) and Toner and Tu (LIT-2970)
    were read, and Kosterlitz and Thouless (LIT-2969, Unfetched) and
    Mermin and Wagner (LIT-2985, Unavailable) through neighbours: the KPZ
    row scoped to d ≤ 2 and its "generically" to theory and simulation
    (ARG-tmp2xbl4); the flocking row's ΔN ∝ ⟨N⟩^φ replaced by the
    diverging structure factor the paper predicts (ARG-tmpdc2qe); the XY
    row rests on LIT-2969 with Kosterlitz (1974), not on Mermin–Wagner,
    and its phase is "critical" only in another sense (ARG-tmprfa3j). The
    readings join `grounds`. The thesis and status are unchanged.
role: thesis
warrant: demonstrated
defeated_if: >-
  A showing that one of the routes listed below needs a parameter tuned to
  a transition after all, for each route, so that the list is empty; or an
  argument that the evidence ordinarily offered for criticality (a power
  law in one observable) does in fact discriminate it from these routes.
  Not defeated by the remark that every scale-invariant state is a fixed
  point of some renormalization-group map: the claim concerns tuning to a
  transition, not the existence of a fixed point (see "What it does not
  say").
tags:
- complex-systems
- natural-sciences
- thermodynamics
date: '2026-11-21'
line:
- formal-apparatus
uses:
- TERM-142
- TERM-139
bears_on:
- QUESTION-508
grounds:
- THEORY-543
- THEORY-1085
- LIT-2978
- LIT-2982
- LIT-2969
- LIT-2985
- LIT-2970
- THEORY-tmpo3w5v
- THEORY-tmpmoyol
- THEORY-tmpdcfxq
- THEORY-tmpdfeto
- THEORY-tmpwdka8
- THEORY-tmpaojie
- THEORY-tmp1nvjs
- LIT-tmph3tia
complements:
- CLAIM-tmpvq33w
summary: >-
  A's, stated at A10 §6 ("Scale invariance is a mathematical property that
  can be produced by many different mechanisms. Criticality is one
  particularly important mechanism for generating it") and A23 §8 ("the
  word criticality is often used too broadly"), and built up over A24 §3,
  A26 §3–4, §6, §9 and A27 §6, §8 into a list of routes: broken continuous
  symmetry, a line of fixed points, nonequilibrium growth (KPZ), sustained
  flux, coarsening, cumulative advantage, geometric recursion, and broad
  relaxation spectra. The assistant adds what would show criticality
  instead, the three-state ring check of A24 §1, and two corrections. The
  wording is A's (the other assistant in the exchange "Rich Get Richer
  Power Laws", A10, A23, A24, A26, A27); adopting it is the owner's call.
---
<!-- inactive-ok-file: THEORY-tmp6jdas THEORY-tmpw4qgu THEORY-tmphcnj3 ARG-tmp38kft — Proposed; the readings of 2026-11-22 and the argument on this claim's network bullet -->
<!-- inactive-ok-file: LIT-tmpvmrkv — Deferred; the reply disputing Broido and Clauset, registered and unread -->
<!-- inactive-ok-file: TERM-139 CLAIM-846 — filed with this claim on 2026-11-21 -->
<!-- inactive-ok-file: LIT-2969 LIT-2985 LIT-tmph3tia — Unfetched, Unavailable or Deferred; Kosterlitz and Thouless and Mermin and Wagner, read through neighbours, and Kosterlitz (1974), registered -->
<!-- inactive-ok-file: THEORY-tmpo3w5v THEORY-tmpmoyol THEORY-tmpdcfxq THEORY-tmpdfeto THEORY-tmpwdka8 THEORY-tmpaojie THEORY-tmpqma2p THEORY-tmp1nvjs THEORY-tmp85ij4 NOTE-tmpcjw5n NOTE-tmpurjns ARG-tmp2xbl4 ARG-tmpdc2qe ARG-tmprfa3j CLAIM-tmpvq33w — Proposed, Skimmed or new; the readings of 2026-11-22, their arguments, and the claim filed beside this one -->
<!-- inactive-ok-file: THEORY-tmpehudh ARG-tmp1zu0m CLAIM-tmpfwwrf — Proposed or new; the reading of Bak, Tang and Wiesenfeld, the argument on this claim and the record's sandpile reproduction -->
<!-- inactive-ok-file: CLAIM-769 — Proposed; power-law relaxation from a spread of rates -->
<!-- inactive-ok-file: CLAIM-803 CLAIM-795 — filed from the same exchange on 2026-11-21, Proposed -->

# CLAIM-841: A power law or a scale-invariant law does not by itself indicate criticality: symmetry, flux, growth, coarsening, geometry and broad relaxation spectra each remove a characteristic scale without a tuned transition

## The routes

A27 §8's table, with the routes A adds in A10, A24 and A26. "Criticality"
here is a transition reached by tuning a control parameter
([TERM-139](../terms.d/TERM-139.md): a fixed point with relevant directions).

| Route | Why no intrinsic scale | Tuned? | Where |
|---|---|---|---|
| Criticality | correlation length diverges at a transition | yes | A6 §2, A8 §1 |
| Broken continuous symmetry | no θ² restoring term, so long-wavelength cost ∝ k²; transverse C(r) ∝ r^(−(d−2)) through the ordered phase | no | A27 §2–3 |
| Line of fixed points (2D XY) | marginal direction; vortex fugacity irrelevant on the fixed line; C(r) ∝ r^(−η(T)), η = T/2πρ_s, over a range of T | no | A12 §7, A27 §5; LIT-2969 with Kosterlitz (1974), LIT-tmph3tia, through THEORY-tmpwdka8, THEORY-tmpaojie |
| Nonequilibrium growth (KPZ) | W(L, t) = L^α F(t/L^z), α = ½, z = 3/2 in 1D, for any λ ≠ 0 in d ≤ 2; in experiment only where growth is local and disorder absent | no in d ≤ 2; above, a tuned threshold separates two scale-invariant phases | A24 §3; LIT-2978, LIT-2982; THEORY-tmpo3w5v, THEORY-tmpdcfxq, THEORY-tmpmoyol |
| Sustained flux (turbulence) | constant transfer rate across the inertial range | no | A23 §2 |
| Ordered active matter | density structure factor Cρ(q) diverging as q → 0 (q⊥^(−6/5) in 2D) through the ordered phase, at its own fixed point, not the transition's | no | A26 §4, A27 §7; THEORY-1085, LIT-2970, THEORY-tmpdfeto |
| Coarsening | L(t) ∝ t^(1/2) (nonconserved) or t^(1/3) (conserved), well below T_c | no | A26 §3 |
| Cumulative advantage | growth with attachment ∝ size | no | A1, A27 §8 |
| Geometric recursion | a fractal; Sierpiński D = log 3/log 2 = 1.585 | no | A10 §3 |
| Broad relaxation spectra | a superposition of exponentials over a wide spread of rates | no | A23 §7, A27 §8; [CLAIM-769](CLAIM-769.md) |
| Brownian motion | B(at) =d √a B(t) | no | A10 §6 |

The derivations A gives were rechecked: the BKT exponent from
⟨Δθ²⟩ = (T/πρ_s) ln r gives exp(−½⟨Δθ²⟩) = r^(−T/2πρ_s); the 2D
infrared integral ∫k^(d−3) dk diverges logarithmically (Mermin–Wagner,
LIT-2985, whose proof, by Gelfert and Nolting's outline, "ultimately
rests on the divergence of the integral" ∫d^Dk/k², THEORY-tmp1nvjs); an explicit field μ²θ² gives ξ = √ρ_s/μ; KPZ's z = α/β =
(½)/(⅓) = 3/2, so a tenfold length is 10^1.5 = 31.6-fold in time against
100-fold for diffusion (A24 §6); 1D directed percolation's
ν∥/ν⊥ = 1.7338/1.0969 = 1.581 (A24 §2). The Gaussian spin-wave route is
checked numerically in [CLAIM-846](CLAIM-846.md).

## A's further distinctions folded in

- **Structure is not scaling.** A Turing instability selects a band of
  wavenumbers and so a characteristic wavelength ℓ* = 2π/k* (A26 §2;
  [THEORY-543](../theory.d/THEORY-543.md)): "the emergence of structure and the emergence of scaling
  symmetry are two distinct phenomena." A26 §6 sorts the cases as scale
  selection (Turing), scale evolution (coarsening, whose dynamic scaling
  C(r, t) = F(r/L(t)) is "self-similar transformation, rather than a
  permanently scale-invariant state") and persistent multiscale
  organization (critical, turbulent, active). A26 §7 reads which case from
  the dispersion relation λ(k): negative everywhere, positive near some
  k* > 0, vanishing as k → 0, or positive over a broad band.
- **A histogram cannot name its mechanism** (A24 §1). Two processes can
  share a stationary distribution and differ in their currents. Checked: a
  three-state ring with rotation-symmetric rates 2 one way and 1 the other
  has stationary probabilities ⅓ each and a net current ⅓ on every edge;
  with equal rates the same distribution has none. "The same power-law
  distribution could be generated by an equilibrium critical system, a
  driven cascade, or an entirely different stochastic mechanism."
- **Order can be the reason for scale-free fluctuations** (A27 §10):
  "A particular kind of order can be the reason a system supports
  scale-free fluctuations"; and "A symmetry can protect scale-free
  fluctuations, and explicitly breaking that symmetry can introduce a
  characteristic scale" (A27 §6).
- **Many networks reported as scale free show little statistical
  evidence of it** (A10 §6, corrected on 2026-11-22), which A attributes
  to "rigorous studies", plainly Broido and Clauset ([LIT-2963](../literature.d/LIT-2963.md)). A said
  they "are not"; the paper shows a lack of evidence, many "may in fact
  be log-normal networks", and its verdict is disputed ([LIT-tmpvmrkv](../literature.d/LIT-tmpvmrkv.md)).
  The paper never mentions criticality, so this bullet is background to
  the thesis, not a ground of it ([ARG-tmp38kft](../arguments.d/ARG-tmp38kft.md)).

## What would show criticality instead

A12 §8: "A heavy-tailed distribution alone doesn't tell us whether a system
is critical. But a set of consistent scaling relationships—across event
sizes, system sizes, correlations, and control parameters—can provide much
stronger evidence." The discriminating observations are a cutoff that
grows as a control parameter is moved (and not only with system size), a
data collapse P(s, L) = s^(−τ) f(s/L^D) across sizes, and exponents that
satisfy the scaling relations among several observables. A24 §9 adds that
the cutoff behaves differently by route: near criticality it grows on
approach, in turbulence it is set by the injection and dissipation
scales, and a KPZ interface has universal scaling without power-law
tails at all. [LEAD-209](../leads.d/LEAD-209.md) proposes making this a protocol.

Two neighbours filed from the same exchange: [CLAIM-803](CLAIM-803.md) holds that a
power-law distribution does not identify its mechanism, and [CLAIM-795](CLAIM-795.md)
lists mechanisms with no positive feedback. This claim is narrower in one
way and wider in another: it concerns criticality in particular, and
scale-covariant laws (correlations, spectra, dynamic scaling) as well as
distributions.

## Corrections to A's turns

- A24 §5 is headed "Three ways nonequilibrium systems produce universal
  scaling" and its table has four rows (directed percolation, KPZ,
  turbulent cascade, self-organized criticality).
- A12 §8's third row, "Stable scale-free dynamics", is not defined beyond
  the BKT example and as written cannot be told from "critical scaling".
  This claim reads it as scaling with no tuned direction, which is the
  open part of [QUESTION-508](../questions.d/QUESTION-508.md).

## What it does not say

- That these routes are outside renormalization theory. In RG terms every
  scale-invariant law sits at or near some fixed point; the Goldstone
  phase and the XY phase are fixed points, and KPZ is a nonequilibrium
  one. What separates them from a critical point is that nothing has to be
  tuned to reach them. So "critical" in the broad sense of "at an RG fixed
  point" is not what this claim denies; it denies that a power law shows
  a tuned transition.
- That self-organized criticality is ruled out. It is a route that ends at
  a critical point without outside tuning (A24 §4; Bak, Tang and
  Wiesenfeld, [LIT-2992](../literature.d/LIT-2992.md): "an attractor reached by starting far from
  equilibrium", p. 381), and whether a given system takes it is
  [QUESTION-508](../questions.d/QUESTION-508.md). The founding letter is itself an instance of the
  inference this claim doubts: "The fact that the curve is linear over
  two decades indicates that the system is at a critical point" (p. 383).
  The finite-size cutoff it asserts, which the record reproduces
  ([CLAIM-tmpfwwrf](CLAIM-tmpfwwrf.md)), is the stronger of its two kinds of evidence, though
  by the list below it is one discriminating observation among several,
  not a proof.

## Change of 2026-11-22

The bullet "Many reported scale-free networks are not" now reads "Many
networks reported as scale free show little statistical evidence of it",
and is marked as background, not a ground ([ARG-tmp38kft](../arguments.d/ARG-tmp38kft.md)). Version 2.

## Note of 2026-11-22: Newman, read

Newman's review ([LIT-2976](../literature.d/LIT-2976.md), read in [NOTE-tmpa7yd2](../notes.d/NOTE-tmpa7yd2.md); the reading is
[THEORY-tmp6jdas](../theory.d/THEORY-tmp6jdas.md)) **supports the distributional half** of the thesis:
"most experimentally observed power laws are probably not the result of
phase transitions—a variety of other mechanisms produce power-law
behaviour as well" (§III.E, p. 12), and tuning "makes the divergence of
length-scales an unlikely explanation for generic power-law
distributions" (§IV.E, p. 19). It **leaves open** the routes listed here
(symmetry, a line of fixed points, KPZ, flux, coarsening), none of which
is in the review; its own routes (the Yule process, combinations of
exponentials, inverses, walks, highly optimized tolerance) touch only the
"cumulative advantage" and "broad relaxation" rows, loosely.
[THEORY-tmp6jdas](../theory.d/THEORY-tmp6jdas.md) `corroborates` the claim.

## Note of 2026-11-22: Clauset, Shalizi and Newman, read

A **parallel** ([LIT-2987](../literature.d/LIT-2987.md), [NOTE-tmphbwdu](../notes.d/NOTE-tmphbwdu.md), [THEORY-tmpw4qgu](../theory.d/THEORY-tmpw4qgu.md)). The power law
with an exponential cutoff is "clearly favored" for fires, flares and
earthquakes (p. 26), the classic self-organized-criticality cases, and the
pure power law is "firmly ruled out" for earthquakes (p. 23): the shape
offered as evidence of criticality often is not a pure power law at all.
No edge.

## Note of 2026-11-22: Broido and Clauset, read

**No bearing on the thesis; qualifies the folded-in bullet** ([LIT-2963](../literature.d/LIT-2963.md),
[NOTE-tmpleyjh](../notes.d/NOTE-tmpleyjh.md), [THEORY-tmphcnj3](../theory.d/THEORY-tmphcnj3.md); [ARG-tmp38kft](../arguments.d/ARG-tmp38kft.md), Rejected as a route). The
paper never mentions criticality or any route listed here; it doubts that
the power law is there at all, before any question of what it indicates.
It was never in `grounds`, and stays out. Status unchanged.

## Note of 2026-11-22: Bak, Tang and Wiesenfeld, read

Bak, Tang and Wiesenfeld ([LIT-2992](../literature.d/LIT-2992.md), read in full in [NOTE-tmpnl00y](../notes.d/NOTE-tmpnl00y.md); the
reading is [THEORY-tmpehudh](../theory.d/THEORY-tmpehudh.md)) **support the "What it does not say" bullet
on self-organized criticality**: "The critical point in the dynamical
systems studied here is an attractor reached by starting far from
equilibrium: The scaling properties of the attractor are insensitive to
the parameters of the model" (p. 381), and "There are no parameters since
a shift in K simply shifts z" (p. 382). [THEORY-tmpehudh](../theory.d/THEORY-tmpehudh.md) `corroborates`
the claim ([ARG-tmp1zu0m](../arguments.d/ARG-tmp1zu0m.md)).

**A historical contrast, not a defeater**, on two counts. The letter
infers criticality from the shape of one distribution: "The fact that the
curve is linear over two decades indicates that the system is at a
critical point with a scaling distribution of clusters" (p. 383), the
inference this claim's "What would show criticality instead" holds
insufficient; it backs it only with the finite-size remark, asserted
without data. And it proposes SOC as "the common underlying mechanism"
behind 1/f noise, fractals and turbulence (p. 381), where the table above
treats turbulence as a separate flux route. The letter offers a
conjecture and simulations, not an argument that the other routes fail,
so the thesis stands. Version 3.

## Change of 2026-11-22: the KPZ, flocking and XY rows, after reading

- **KPZ** (ARG-tmp2xbl4). "Generically" holds for d ≤ 2 only: there any
  λ ≠ 0 flows to the KPZ fixed point (Kardar, Parisi and Zhang, p. 891),
  but above two dimensions a small λ "is irrelevant, and an
  asymptotically ideal smooth surface is expected with z = 2" (p. 892),
  and "an intermediate fixed point, at g = g* ≃ d − 2" separates the two
  phases (Le Doussal, LIT-tmpvt8q4, p. 4): a tuned point between two
  scale-invariant phases, so the thesis stands. And in experiment untuned
  is not generic: "only two experiments among dozens directly found the
  KPZ exponents" (Takeuchi and Sano, p. 1), who credit their own success
  to "strictly local processes", intrinsic noise and no quenched disorder
  (p. 4).
- **Flocking** (ARG-tmpdc2qe). LIT-2970 is no longer cited for
  ΔN ∝ ⟨N⟩^φ, which it never writes: it predicts a density structure
  factor that diverges as q → 0, as q⊥^(−6/5) for q∥ ≪ q⊥ in two
  dimensions (eqs. 1.10–1.11). A's "some initially predicted exponents
  differ from those obtained in large-scale simulations" is not in it;
  it reports "good agreement" (p. 70).
- **XY** (ARG-tmprfa3j). The row rests on LIT-2969 with Kosterlitz (1974),
  LIT-tmph3tia, through its two neighbours, not on Mermin–Wagner, which
  "sheds no light on the question of whether quasi-long-range order can
  exist" (Halperin, THEORY-tmpqma2p). The neighbours call the low-T phase
  "critical" ("at all low-temperatures, the system is critical",
  Drouin-Touchette §2.2) in the sense of an infinite correlation length,
  not of a tuned transition, so the usage does not contradict this claim;
  and the transition that ends it is an essential singularity of ξ, not
  a power-law critical point (§3.4).

Version 4.

## Note of 2026-11-22: Kardar, Parisi and Zhang, read

Kardar, Parisi and Zhang (LIT-2978, read in full in NOTE-tmpf6isj; the
reading is THEORY-tmpo3w5v) **support the KPZ row for d ≤ 2 and the
bullet "A histogram cannot name its mechanism"**: in d = 1 the KPZ
interface has the linear interface's static exponent, and strip
simulations had read it as linear, "a result of a peculiarity of
one-dimensional interfaces" (p. 891); only z tells them apart.
THEORY-tmpo3w5v joins `grounds` (ARG-tmp2xbl4).

## Note of 2026-11-22: Takeuchi and Sano, read

Takeuchi and Sano (LIT-2982, read in full in NOTE-tmpbmox1; the reading
is THEORY-tmpmoyol) **support the KPZ row in experiment and qualify its
"generically"** (above). They also bear on A24 §9's "a KPZ interface has
universal scaling without power-law tails": the universal object is a
Tracy-Widom distribution, characterized by its cumulants, consistent with
A's remark. THEORY-tmpmoyol joins `grounds` (ARG-tmp2xbl4).

## Note of 2026-11-22: Toner and Tu (1998), read

Toner and Tu (LIT-2970, NOTE-tmpcjw5n; the reading is THEORY-tmpdfeto)
**support the flocking row's substance and the folded-in "explicitly
breaking that symmetry can introduce a characteristic scale"**: a compass
"will introduce a "mass"", after which "there are no interesting
fluctuations left at long distances and times" (p. 63). They **qualify
the XY row's reading of a fixed line**: their possible fixed line of
flocks, "somewhat reminiscent of that of the d = 2 equilibrium X − Y
model", is "not associated in any way with the absence of true long
ranged orientational order" (p. 52), so continuously varying exponents
need not mean quasi-long-range order. THEORY-tmpdfeto joins `grounds`
(ARG-tmpdc2qe).

## Note of 2026-11-22: Kosterlitz and Thouless, through two neighbours

LIT-2969 is Unfetched (the IOP copy behind a Cloudflare challenge).
Kosterlitz's Nobel lecture (LIT-tmp3k6np, NOTE-tmp0si2r, THEORY-tmpwdka8)
and Drouin-Touchette (LIT-tmp6hh1r, NOTE-tmpurjns, THEORY-tmpaojie)
**support the XY row** (ARG-tmprfa3j): the fugacity "becomes irrelevant"
on the fixed line (§3.3), nothing tuned through the phase.

## Note of 2026-11-22: Mermin and Wagner, through three neighbours

LIT-2985 is Unavailable. Halperin (LIT-tmp3zns2, THEORY-tmpqma2p),
Gelfert and Nolting (LIT-tmpbgf6y, THEORY-tmp1nvjs) and Nachtergaele
(LIT-tmp25uib, THEORY-tmp85ij4) **support the Goldstone row's no-tuning
point**: the divergence that excludes order holds at every T > 0, with no
parameter set. THEORY-tmp1nvjs joins `grounds` for the 2D logarithm. They
**scope the XY row's citation**, as above.

## Note of 2026-11-22: what three routes share

Read together, the KPZ, flocking and XY cases share a shape this claim
does not state: a symmetry or conservation law protecting a coupling or
forbidding a restoring term, and a perturbation (a compass, a finite
interaction range, d > 2 at weak coupling) that undoes it. The assistant
files it as CLAIM-tmpvq33w, which complements this one and bears on
QUESTION-508; it does not cover the flux, growth-by-attachment,
coarsening, recursion or relaxation routes.
