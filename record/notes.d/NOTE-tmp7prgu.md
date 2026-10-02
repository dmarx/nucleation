---
status: Read
paper: LIT-tmpoej2u
title: 'Belousov-Zhabotinsky reaction'
version: 1
history:
- version: 1
  date: '2026-10-02'
  note: >-
    Read in full (Scholarpedia revision #91050, last modified 21 October
    2011: the four sections, the Oregonator reaction scheme as printed,
    the five figure captions and the 38 references). The figures themselves
    were not inspected. The article has been edited by others since its
    2007 acceptance, so not every sentence is certainly Zhabotinsky's; the
    page does not say which. The primary papers it cites (Belousov 1959,
    Zhabotinsky 1964, Zaikin & Zhabotinsky 1970, Field, Kőrös & Noyes 1972)
    were not read.
date: '2026-10-02'
summary: >-
  An authoritative short review. BZ: bromate oxidizes an organic reductant,
  catalysed by Ce, Fe(phen)₃ or other metal ions. Oscillation is a relaxation
  cycle: autocatalytic HBrO₂ oxidizes the catalyst, Br⁻ (made when Ce⁴⁺
  oxidizes bromomalonic acid) shuts the autocatalysis off. Phase resetting
  by Br⁻, Ag⁺ and Ce⁴⁺ confirms it. Closed: up to several thousand cycles.
  CSTR: indefinite oscillation, bursting, chaos. Unstirred: trigger waves,
  targets, spirals, scrolls; in microemulsion, Turing structures. The
  Oregonator is qualitative only.
---
<!-- inactive-ok-file: LIT-tmpd737a — Deferred, no lawful full text; Nicolis & Prigogine, cited only as the review's source for the far-from-equilibrium condition, not leaned on -->

# NOTE-tmp7prgu: Belousov-Zhabotinsky reaction

## Contribution

An encyclopedia review, so no new result. What it adds to the record is a
first-hand account, by one of the reaction's two eponyms, of:

- the history: Belousov's citric-acid/cerium system and Zhabotinsky's
  malonic-acid version;
- the core mechanism, the Oregonator and the Oregonator's known failures;
- the difference between closed and open-reactor dynamics;
- the wave phenomena first reported by Zaikin and Zhabotinsky in 1970.

## Key insight

BZ is an oscillator because a fast positive feedback (autocatalytic HBrO₂
production oxidizing the catalyst) is coupled to a slower negative feedback
(Br⁻ released as the oxidized catalyst is reduced by the organic substrate).
Each switches the other off at a threshold, which gives a relaxation limit
cycle. The same thresholds make the unstirred medium excitable, so a local
switch propagates as a trigger wave followed by a refractory zone. The rest
follows from that: annihilation of colliding waves, the fastest pacemaker
entraining the others, and spirals at broken fronts.

## Assumptions

What the review takes for granted:

- **Thermodynamics.** Oscillation needs the system "sufficiently far from
  the state of thermodynamic equilibrium", and detailed balance forbids it
  near equilibrium (both cited to Nicolis and Prigogine 1977, [LIT-tmpd737a](../literature.d/LIT-tmpd737a.md)).
- **Chemistry.**
  - Bromate is "the only irreplaceable initial reagent".
  - The catalyst may be Ce, Mn or complexes of Fe, Ru, Co, Cu, Cr, Ag, Ni
    and Os.
  - Many reductants work.
- **Models.** The Oregonator (Field and Noyes 1974) and Tyson's two-variable
  reductions are taken as qualitative models. The quantitative claims rest
  on later modified versions (Rovinsky and Zhabotinsky 1984; Nagy-Ungvarai
  et al. 1989).

## Key results

- **History.**
  - Belousov found oscillations with Ce³⁺/Ce⁴⁺ and citric acid, with
    frequency rising with temperature (Belousov 1959).
  - Zhabotinsky replaced citric acid with malonic acid and showed that the
    colour oscillation is the oscillation of [Ce⁴⁺]. He found that oxidation
    of Ce³⁺ by HBrO₃ is autocatalytic, that oscillation starts after
    bromomalonic acid accumulates, and that Br⁻ inhibits the autocatalysis
    (Zhabotinsky 1964a, b).
- **Core scheme** (Vavilin and Zaikin 1971):
  - HBrO₃ + HBrO₂ → 2BrO₂• + H₂O;
  - H⁺ + BrO₂• + Fe(phen)₃²⁺ → Fe(phen)₃³⁺ + HBrO₂;
  - HBrO₂ + H⁺ + Br⁻ → 2HOBr;
  - plus Br⁻ production as the oxidized catalyst oxidizes bromomalonic acid.
  Phase resetting (Fig. 1, Vavilin et al. 1973) supports it. Br⁻ or Ce⁴⁺
  injected while [Ce⁴⁺] is rising switches the system to the falling phase.
  Ag⁺, which removes Br⁻, switches it from falling to rising.
- **Oregonator.** Field, Kőrös and Noyes (1972) gave the detailed mechanism.
  The Oregonator (Field and Noyes 1974) has variables [HBrO₂], [Br⁻] and
  [Ce⁴⁺] and a stoichiometric factor standing for bromide production. It
  "properly models oscillations and excitability" but "is not a quantitative
  model": it leaves total catalyst out of its parameters, reproduces the
  waveform poorly, and misses the observed oscillatory domains. Taking
  reversibility of the catalyst reactions into account corrects these.
- **Closed systems.**
  - Oscillation occurs over large ellipsoidal domains of initial
    concentrations, spanning about three orders of magnitude in bromate and
    malonic acid and three to four in cerium.
  - Period-2 oscillation can arise as the reaction evolves.
  - Excitability and bistability lie outside the oscillatory domain.
    Bistability needs a source of Br⁻ other than the reactions of Ce⁴⁺.
  - A closed system "can generate up to several thousand oscillatory cycles".
- **Open systems.** In a CSTR "stationary oscillations can continue
  indefinitely". Bursting (Vavilin et al. 1968) and chaos (Schmitz et al.
  1977) were found, and the CSTR allows bifurcation sequences to be traced.
- **Waves.**
  - Zaikin and Zhabotinsky (1970) observed concentric trigger waves from
    point pacemakers in a thin unstirred ferroin-catalysed layer, forming
    target patterns.
  - Colliding waves annihilate because of their refractory zones, and the
    fastest pacemaker entrains the rest (Fig. 4).
  - Broken fronts curl into spirals (Zhabotinsky and Zaikin 1971; Winfree
    1972), and in thick layers into scroll waves (Winfree 1973).
  - With 1,4-cyclohexanedione, anomalous dispersion groups waves into
    packets.
  - In AOT microemulsion BZ shows Turing and short-wave instabilities and
    "produces Turing structures", standing waves, localized structures,
    inwardly moving waves and segmented waves (Vanag and Epstein 2001).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Before BZ, chemists generally attributed homogeneous oscillations to heterogeneity or error, misreading the near-equilibrium prohibition as general | historical assertion | Zhabotinsky 1991 (his own history) |
| C2 | The oscillation is driven by autocatalytic HBrO₂ inhibited by Br⁻, with Br⁻ regenerated from bromomalonic acid by the oxidized catalyst | strong | primary kinetics cited; phase-resetting experiments (Fig. 1) |
| C3 | The Oregonator models oscillation and excitability qualitatively but not quantitatively | strong | named defects; corrected models cited |
| C4 | A closed BZ system can run up to several thousand cycles | stated, uncited | §Basics |
| C5 | In a CSTR oscillation continues indefinitely, with bursting and chaos in some regimes | strong | cited experiments |
| C6 | Unstirred BZ supports target, spiral and scroll waves, which annihilate on collision | strong | Zaikin and Zhabotinsky 1970; Winfree 1972, 1973 |
| C7 | BZ in microemulsion produces Turing structures | moderate here (one cited group) | Vanag and Epstein 2001 |

## Concepts

- **BZ reaction**: "a family of oscillating chemical reactions" in which
  transition-metal ions catalyse oxidation of (usually organic) reductants
  by bromic acid in acidic water.
- **trigger wave**: a pulse of excitation followed by a refractory zone,
  propagating through an excitable or oscillatory medium.
- **pacemaker**: a point source emitting concentric waves; the fastest one
  entrains the medium.
- **CSTR**: continuous-flow stirred tank reactor, which keeps reagent
  concentrations fixed by inflow and outflow.

## Connections

- **Prigogine's Nobel lecture ([LIT-tmp452jw](../literature.d/LIT-tmp452jw.md)), read.** The lecture does not
  name BZ; its "chemical clock" is the Brusselator, a model with A and B
  "maintained constant". BZ in a CSTR is the experimental counterpart of that
  idealization. A closed BZ batch is not: there A and B run down, and the
  oscillation is a transient on the way to equilibrium. Both share the
  lecture's necessary condition, an autocatalytic step.
- **Turing ([LIT-tmptpgzu](../literature.d/LIT-tmptpgzu.md)), read.** BZ waves are the chemical travelling waves
  Turing's case (e) gestured at, but excitable and strongly non-linear, which
  his linear theory does not cover. The review's last paragraph records that
  BZ in microemulsion has since given stationary Turing structures.
- **Cross and Hohenberg ([LIT-tmpht8ga](../literature.d/LIT-tmpht8ga.md)), skimmed.** Their §X uses BZ and the
  Oregonator as the chemical example and says the same things: closed
  experiments "run down in finite time (typically less than 100 periods of
  oscillation)" for spatial patterns, and open gel reactors were the remedy.
  Their figure of under 100 periods for unstirred pattern experiments and
  the review's "several thousand" cycles for closed systems are not in
  conflict: the setups differ.
- **Nicolis and Prigogine ([LIT-tmpd737a](../literature.d/LIT-tmpd737a.md)), Deferred.** Cited by the review for
  the far-from-equilibrium condition on oscillation.

## Bearing on the record

- **[LIT-192](../literature.d/LIT-192.md) (demarcation).** BZ has rhythm, excitability, self-propagating
  signals and entrainment, which are properties often taken as marks of
  living organization. It has no closure of constraints and no
  self-maintenance: its organization is maintained by the experimenter's
  feed. That makes it the cleanest chemical foil for the
  candle-flame-versus-organism line Nahas and Sachs discuss ([NOTE-094](NOTE-094.md)). It
  shows that a criterion based on thermodynamics or dynamics alone does not
  separate organisms from non-organisms, so whatever separates them must be
  organizational.
- **[LIT-211](../literature.d/LIT-211.md) (the "Dissipative Self-Organizing Systems" cluster).** BZ in a CSTR
  satisfies definitions of that kind as well as an organism does. That is the
  standing objection to them, and [NOTE-109](NOTE-109.md) records that the cluster's
  definitions are "persister" criteria of the kind Baedke criticizes
  ([LIT-167](../literature.d/LIT-167.md)). BZ is a persister only while fed.
- **No THEORY is indicated by this reading alone. No ML instruction.**

## Limitations

- **A short review.** No derivations, and some statements (such as "several
  thousand" cycles) are uncited.
- **Authorship is mixed.** The page credits Zhabotinsky but lists later
  contributors and was modified in 2011.
- **Nothing on thermodynamics beyond the opening paragraph.** No entropy
  production, free-energy budget or stability analysis is given.

## Open questions

- How long does a closed BZ batch stay effectively at a quasi-steady state?
  That determines whether its patterns count as dissipative structures in
  Prigogine's steady-state sense or only as transients.
- Do the quantitative corrections to the Oregonator change any of its
  qualitative wave predictions?

## Corrections

- none to a seeded skim (there was no seed)
- **Request's candidates.** The request's alternative citation, Zaikin &
  Zhabotinsky (1970), Nature 225:535–537, is right; the issue is 5232 and the
  DOI 10.1038/225535b0. The first author is A. N. Zaikin. Nature prints the
  title in title case: "Concentration Wave Propagation in Two-dimensional
  Liquid-phase Self-oscillating System".
- **Discovery date.** Cross and Hohenberg (§X.A.1) date Belousov's discovery
  to 1951; the review cites its first publication, Belousov 1959. Both can be
  right; neither source reconciles them.
