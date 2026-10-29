---
status: Read
paper: LIT-1406
title: 'Seeley et al. — Stop signals provide cross inhibition in honeybee swarms'
version: 1
history:
- version: 1
  date: '2026-10-29'
  note: >-
    Read in full on 2026-10-29 from the copy on rangevoting.org
    (https://rangevoting.org/SeeleyVSHFMinhibit.pdf, 8 pages), read under
    the owner's ruling of 2026-10-29 that scholarly third-party copies
    count. It is the Science Express version of record: each page is
    footed "www.sciencexpress.org / 8 December 2011 / 10.1126/science.1210361"
    and "Downloaded from www.sciencemag.org on December 10, 2011"; title
    and six authors match Crossref; received 27 June 2011, accepted 21
    November 2011, published online 8 December 2011. It is not the print
    layout of Science 335, 108–111, which was not compared. Text extracted
    with pdftotext. Read: the abstract, the whole main text, the captions
    of Figs. 1–3, the 44 references and the acknowledgments. Figs. 1–3
    were read from captions and text; no number was taken from a chart.
    The supporting online material, which holds the methods, the
    statistical explanations and the models' equations, was not read. The
    chi-squared tests that can be rebuilt from counts in the text were
    recomputed (2026-10-29): χ²(1, 109) = 21.9 for 96 vs 13 return-phase
    contacts, and χ²(1, 112) = 16.03 for 26% of 38 vs 66% of 74, both
    reproduce; the implementation-phase χ²(1, 281) = 3.92 reproduces with
    128/148 and 103/133, which round to the stated 86% and 77%.
date: '2026-10-29'
summary: >-
  Nest-site scouts of honeybee swarms deliver stop signals, head-butts
  with a brief vibration, to scouts dancing for sites other than their
  own while the swarm is choosing (213 of 237 signals in two two-box
  swarms), and to all dancers once it has chosen. An ODE model, in the
  supplement, shows that above a critical rate of such cross inhibition
  a swarm facing two equal sites breaks deadlock and picks one at random,
  and picks the better when they differ enough.
---
<!-- inactive-ok-file: CLAIM-418 — Proposed; the claim this reading bears on, cited as open -->

# NOTE-tmpuj9lb: Seeley et al. — Stop signals provide cross inhibition in honeybee swarms

## Contribution

It finds in a honeybee swarm the cross inhibition between competing
evidence-accumulating populations that models of neural decision-making
assume. Scouts for one nest site send inhibitory stop signals mainly to
scouts dancing for the other, during the choice. A model built from the
observed behaviour shows why this matters: without it, a swarm choosing
between equal sites can stall in a stable deadlock.

## Key insight

A collective that chooses by accumulation to a threshold needs a way to
suppress the losing alternative, or equal options balance forever. The
bees' stop signal, already known from foraging, does that work when it
is aimed at rivals and given often enough. The same structure appears in
the Usher–McClelland leaky competing accumulator, so the paper presents
the swarm and the brain as two implementations of one decision scheme.

## Assumptions

- **Nest-site choice is a race to a quorum** between populations of
  scouts, each recruiting by waggle dances (refs. 6, 12).
- **A scout that stops dancing for a site soon stops visiting it**
  (refs. 22–23), so inhibition of dancing is inhibition of commitment.
- **The model's equations are mean-field ODEs** "rigorously derived from
  the individual-level interaction rules" observed; their form is in the
  supplement, not the main text.
- **Paint marks did not drive targeting**: stop signals were already
  given to unmarked dancers in the first five swarms.

## Key results

- **Stop signals in house-hunting.** On 2 of 5 swarms, 40 dancers filmed
  close up; 23 received 109 stop signals (4.7 ± 4.3 per signalled bee)
  from 40 bees. A signal lasts 0.21 ± 0.10 s; contact is 98% by the head.
  Signals came mostly in the return phase (96 vs 13 contacts; 73 and 36
  expected), and signalled dancers stopped 36 ± 22 s after signals began.
- **Signals end dances.** On 3 further swarms, 525 signals over 109
  dances were concentrated in the last deciles of circuits, also in long
  dances, which the authors take to show causation, not a common time
  trend.
- **Cross inhibition in the decision phase.** Two swarms on an island,
  two identical nest boxes, scouts painted pink or yellow by box. 98.4%
  of 1379 signals were attributed to a sender, and 94.5% of 1357 came
  from marked scouts. Dancers received 213 contra signals (from at least
  46 bees) and 24 ipsi (from at least 14), more contra than the marked
  proportions predict.
- **General inhibition in the implementation phase.** After worker piping
  began, contra (185) and ipsi (210) signals were in proportion to the
  marked scouts.
- **One-box control.** In the decision phase 26% of 38 dancers received
  signals with one box, against 66% of 74 with two; in the implementation
  phase 86% of 148 and 77% of 133, the one-box share being, if anything,
  higher (P = 0.05).
- **Models (Fig. 3, supplement).** (i) Direct switching between
  commitments (ref. 3), with any decay, deadlocks stably between equal
  sites. (ii) Indiscriminate stop signals deadlock too. (iii)
  Discriminate stop signals deadlock below a critical signalling rate;
  above it two stable consensus states appear and the swarm picks one at
  random; above a critical quality difference it converges on the
  better site.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Nest-site scouts use the stop signal and it ends dances | strong | 5 swarms; timing of 525 signals over 109 dances |
| C2 | In the decision phase scouts aim stop signals at dancers for the rival site | moderate | 2 swarms, one setup, χ² on pooled signals and on minimum signaller counts |
| C3 | After the choice, signals become general | moderate | same 2 swarms, plus 2 one-box swarms |
| C4 | Discriminate cross inhibition above a threshold breaks deadlock between equal sites | moderate, model | ODE analysis in the supplement, not read here |
| C5 | Swarm and brain converge on one decision scheme because it is reliable | weak | the authors' "It is tempting to think" |

## Concepts

- **Stop signal**: a vibrational pulse, about 150 ms at about 350 Hz in
  the foraging literature (0.21 s measured here), usually given by
  butting the head against a dancer.
- **Contra and ipsi signals**: from a scout marked for the other box, or
  for the same box, as the dancer.
- **Decision and implementation phases**: before and after the onset of
  worker piping, which marks a quorum reached.
- **Stable deadlock**: an attractor with equal commitment to two sites.

## Connections

The direct-switching model (i) is Marshall et al.'s (2009) optimal-decision
model for social insects; the Usher–McClelland model (2001) and Bogacz et
al. (2006) supply the neural side. The swarm's quorum mechanism is
Seeley and Visscher's (2004); the monograph is *Honeybee Democracy*
(2010). None of these is registered.

## Bearing on the record

- **[CASE-145](../cases.d/CASE-145.md), "Related evidence".** The case cites the paper for
  collective decisions "with no central controller by cross-inhibition of
  recruitment". The paper supports that, with two precisions: the
  inhibition is aimed at rivals only while the swarm is choosing, and is
  general once it has chosen; and that it is what breaks deadlock is a
  model result, holding only above a critical rate of signalling.
- **[CLAIM-418](../claims.d/CLAIM-418.md) and [CASE-108](../cases.d/CASE-108.md).** The LIT's "Why this is here"
  says the exchange cited it for these. Neither entry now cites it. The
  paper gives a case of a choice settled by mutual inhibition between
  advocates and not by an arbiter. It says nothing about adversarial or
  compromised members, which [CASE-108](../cases.d/CASE-108.md) is about.

No instruction for machine-learning practice; nothing for the anthology.

## Limitations

- **Few swarms.** The targeting result rests on two swarms with one
  island setup; the control on two more. Signals from the same bees are
  not independent, which the second test on minimum signaller counts
  only partly answers.
- **The model is not in the paper.** Its equations, parameters and the
  critical thresholds are in the supplement, and the main text gives
  them no values.
- **How scouts tell rival dancers apart is unknown**: dance decoding or
  odour, the authors say.
- **Overstatement.** The modelling results are called "conclusive";
  whether the swarms observed were near the critical signalling rate is
  not shown.
- **Errors.** None of substance found; the three tests rebuilt from the
  text's counts reproduce.

## Open questions

- Is the observed rate of stop signalling above the model's critical
  threshold, and by how much?
