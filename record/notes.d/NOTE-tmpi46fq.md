---
status: Read
paper: LIT-tmp4kcgq
title: 'Anastassiou et al. — Ephaptic coupling of cortical neurons'
version: 1
history:
- version: 1
  date: '2026-11-03'
  note: >-
    Read at the owner's direction from the scan of the published article
    on gwern.net (licence not stated; the owner ruled under ADR-064).
    Text extracted with pypdf. Read: the abstract, introduction, results,
    discussion and online methods (pp. 217–223 and the methods page), and
    the reference list. Figures were read from their captions; the panels'
    numbers came through only in part. The supplementary material (17+
    figures and a supplementary discussion, on Nature's site) was not
    read, so every result the text sends there is the text's report.
date: '2026-11-03'
summary: >-
  In rat cortical slices with synapses blocked, LFP-sized extracellular
  fields applied by an electrode moved somatic membrane potential by less
  than 0.5 mV, undiminished to 100 Hz, and with spiking driven by current
  they shifted spike timing without changing spike counts. Phase locking
  was strongest for slow fields (significant from 0.74 mV/mm at 1 Hz) and
  needed fields nearly ten times larger at 30 Hz. Four nearby neurons were
  synchronized by one field. The authors read this as a consequence of
  Kirchhoff's laws and a threshold model.
---
<!-- inactive-ok-file: CLAIM-478 — Proposed, Open, Deferred, Unfetched, Unavailable or new; cited as open -->
<!-- inactive-ok-file: THEORY-tmp6xjgq — Proposed or new; readings this bears on -->

# NOTE-tmpi46fq: Anastassiou et al. — Ephaptic coupling of cortical neurons

## Contribution

A direct measurement of ephaptic coupling at the single soma under fields of
physiological size. Earlier work applied constant fields between parallel
plates and sampled the field with one electrode at least 50 µm away (p. 217).
Here a 12-pipette setup applied an oscillating current near a patched soma and
measured the extracellular potential at up to seven points around it, so the
field at the membrane was known (pp. 217–218).

## Key insight

A neuron's own field environment can set when it fires, even though the field
is far too weak to make it fire. A sub-millivolt periodic polarization moves
the moment a cell driven toward threshold crosses it, so the field defines
"temporal windows of enhanced excitability" shared by every cell in it (p.
222).

## Assumptions

- **Slices, synapses blocked.** Rat somatosensory cortex, 300 µm slices from
  14–18-day-old Wistar rats; AP5, gabazine or bicuculline, and CNQX block
  NMDA, GABA and AMPA receptors (methods). Gap junctions are argued away by
  age and the absence of spikelets (p. 218).
- **Applied fields.** I = I₀ sin(2πft) through one extracellular pipette 50–150
  µm from the soma, I₀ = 25–200 nA, chosen to give LFP-like amplitudes; at least
  25–50 times weaker than the current that triggers spikes directly (p. 218).
- **A point-source fit** to estimate the field from the recorded potentials (p.
  218).
- **Spiking driven by current.** A 9 s step gave 2–4 Hz firing; each condition
  was paired with a control just before it (p. 219).

## Key results

- **Field sizes.** At 1 Hz, I₀ = 25, 50, 100 and 200 nA gave fields of 0.74,
  1.49, 2.96 and 5.86 mV/mm and extracellular amplitudes of 0.07, 0.14, 0.28 and
  0.55 mV (mean, with large s.d.; p. 218), within the in vivo range (under 0.5
  mV and 5 mV/mm, p. 217).
- **Subthreshold entrainment** (n = 23). At I₀ = 100 nA the membrane potential
  oscillated by 0.16 mV at 1 Hz and 0.14 mV at 100 Hz, in anti-phase with the
  extracellular potential (165° and 179°), at every polarization tested (n = 17).
  Unlike intracellular injection, it is not attenuated by capacitive filtering
  (p. 218).
- **Spike timing** (n = 25). No significant change in spike number or rate.
  The population vector of spike phases grew with field strength, from 0.046 to
  0.145 at 1 Hz, with preferred direction about 241–266° (p. 219). Spike–field
  coherence rose with the field. At I₀ = 50 nA, P = 6.5 × 10⁻⁵ at 1 Hz, 0.019 at
  8 Hz, and above 0.05 at 30 Hz, where significance needed about 5.6 mV/mm
  (p. 220).
- **Synchrony.** Four neurons within 100 µm, all driven at once, clustered their
  spikes near 270° as the 1 Hz field grew, also in triplets and pairs (pp.
  220–221).
- **Mechanism.** Resonance is ruled out because the current drive produces far
  larger membrane fluctuations than the field. A threshold model explains it: if
  synaptic input takes 100 ms to reach a 10 mV threshold, a 0.5 mV ephaptic
  potential advances the spike by 5 ms (p. 222).
- **Relevance.** The coherence changes match the roughly 50% increase in
  hippocampal spike–theta coherence that predicts memory formation in humans,
  at fields of about 1 mV/mm (p. 222).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | LFP-sized fields alter the somatic membrane potential by under 0.5 mV, independent of synapses, up to 100 Hz | strong | direct measurement, n = 23 |
| C2 | Such fields phase-lock spikes without changing spike counts, most effectively at slow frequencies | strong | paired controls, n = 25, corrected tests |
| C3 | A common field synchronizes nearby neurons | moderate | quartets, triplets, pairs; individual-cell variation acknowledged |
| C4 | Endogenous brain activity can causally affect neural function through field effects in vivo | moderate | argued from matched amplitudes; the fields here are applied, not endogenous, and the preparation is a slice |

## Concepts

- **Ephaptic coupling.** Effects on membrane potential of voltage and field
  changes along the membrane, beyond synaptic coupling. The authors widen
  Arvanitaki's term, coined for juxtaposed elements (p. 217).
- **Spike–field coherence (SFC).** The spike-triggered-average spectrum
  normalized by the spike-triggered power, 0% for no phase relation and 100%
  for full locking (p. 219).

## Connections

- **Jennings 2026** ([LIT-tmpasemk](../literature.d/LIT-tmpasemk.md), p. 35) quotes p. 217's sentence that groups
  of cells change their electric environment, which feeds back onto all their
  members, and infers "that brain activity cannot be described simply through
  local interactions, as in a weak emergence account". The quotation is
  accurate. The inference is not the paper's, which calls the potentials "a
  simple consequence of Kirchhoffs' circuit laws" (p. 221). A field effect is a
  physical channel between neurons that is not a synapse. It is non-local in
  wiring, not irreducible.
- **[LIT-388](../literature.d/LIT-388.md)** ([NOTE-330](NOTE-330.md)), where ephaptic coupling is held as a hypothesis about
  sentience. The paper shows the mechanism exists at physiological size and
  says nothing about experience.
- **Marshall et al. 2006** (ref. 26), transcranial slow-oscillation stimulation
  during sleep, and **Rutishauser et al. 2010** (ref. 32), theta phase-locking
  and memory: the in vivo results it is compared with. Not held.

## Bearing on the record

- **[THEORY-tmp6xjgq](../theory.d/THEORY-tmp6xjgq.md)** (Jennings's contextual emergence). Its summary already
  says its neural evidence fits weak emergence. This reading confirms it for
  ephaptic coupling: the evidence is a field effect fully described by
  circuit physics, and the experiment applies the field from outside rather
  than showing the neurons' own field doing the constraining. It gives no
  support to the boundary condition's causal reading.
- **[CLAIM-334](../claims.d/CLAIM-334.md).** A field generated by a population and acting back on it is a
  candidate for macro-to-micro influence. But the field supervenes on the
  currents that produce it, so an intervention on it, as here, is an
  intervention by an electrode on a physical variable, not on a macro variable
  holding its base fixed. The claim stands.
- **[CLAIM-478](../claims.d/CLAIM-478.md).** A slow collective variable (the low-frequency field)
  constrains fast events (spike times) without setting them. The slow field
  works best, which is the claim's first half in a neural case, though the
  slowness here is imposed.
- **No instruction for machine-learning practice.**

## Limitations

- Slices from juvenile rats, synapses blocked, fields applied by one electrode,
  spiking driven by constant current. In vivo relevance is argued from matched
  amplitudes, not shown.
- Large spread in field sizes (s.d. near the mean, p. 218), so "LFP-like" is
  approximate.
- The supplementary figures and discussion, which carry the per-cell analyses
  and the threshold model, were not read.

## Open questions

- Do the fields neurons themselves generate entrain them in vivo, with
  synapses intact and the background noise of 0.2–0.4 mV intrinsic or more with
  synaptic activity (p. 221)?
- Does ephaptic entrainment bear on attention, which Jennings says would
  support her account ([LIT-tmpasemk](../literature.d/LIT-tmpasemk.md), p. 35)? The paper does not test it.
