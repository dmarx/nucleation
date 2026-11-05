---
status: Skimmed
paper: 'LIT-tmpwddcn'
title: 'Sobczak — Investigations of the DNA origami folding process (dissertation)'
version: 1
history:
- version: 1
  date: '2026-11-05'
  note: >-
    Read in part on 2026-11-05 from the PDF in TU München's institutional
    repository mediaTUM
    (https://mediatum.ub.tum.de/download/1415627/1415627.pdf, 172 pp.),
    found by web search; no obstacle met. Text extracted by pdftotext,
    which dropped mathematical symbols (inequality, degree and minus
    signs). Read in full: front matter, Chapter 1 (summary), §§2.4–2.5
    (the folding process), all of Chapter 3 (experiments, pp. 13–38), the
    §4.5 summary, §5.1.3 (temperature jumps), a §5.1.5 excerpt, §5.2's
    opening and §§5.2.2–5.2.5 (scaffold permutations, long staples, short
    staples), §5.3 (summary) and §§6.1–6.4.1. Skimmed or skipped: the
    model derivation (§§4.1–4.4), most of §§5.1–5.2.1, and Chapters 7–9
    (methods, code, parameters, designs). Figures are images, read only
    through their legends and recovered axis text; no gel or TEM image
    was seen. Hence Skimmed. Registered as a stand-in for the unread
    Sobczak et al. (2012), LIT-tmpg98v0.
date: '2026-11-05'
summary: >-
  Gel and SYBR Green assays show 3D DNA origami folding cooperatively in
  a structure-specific window of about 5 °C, foldable at constant
  temperature within it, and melting 5–10 °C higher within seconds while
  folding takes minutes to hours. Cooperativity spans connected
  subdomains; staple concentration and internal routing shift the window
  and the rate, routing by more than 100-fold at fixed shape and
  composition. A kinetic model, partly read, blames spurious short
  binding for low-temperature inhibition, and a short-domain design folds
  only when cooled fast to its folding temperature.
---
<!-- inactive-ok-file: LIT-tmpg98v0 THEORY-tmp500wn THEORY-1398 CLAIM-567 CLAIM-583 CLAIM-571 CLAIM-581 CLAIM-591 CLAIM-569 CLAIM-566 CLAIM-557 CLAIM-574 CLAIM-570 CLAIM-592 CLAIM-572 CLAIM-184 CLAIM-478 CLAIM-568 CLAIM-185 — Proposed, Unavailable, Skimmed or new; cited from the reading of Sobczak (2018) as open -->

# NOTE-tmpwxm2p: Sobczak — Investigations of the DNA origami folding process (dissertation)

## Contribution

It measures where on the temperature axis origami assembly happens and
finds a narrow, structure-specific window rather than the whole anneal.
It separates the forward and reverse transitions, by 5–10 °C and by
orders of magnitude in time. It shows that internal design, not final
shape or stability, sets the window and the rate. All of this is
temperature and time spent on one fixed target.

## Key insight

A folded origami is enormously favoured at low temperature, yet at most
temperatures it does not form on any laboratory timescale: above the
window the nucleation barrier is not crossed, below it spurious short
bindings bog the scaffold down. Folding is a narrow passage, and leaving
the folded state is not its reverse.

## Assumptions

- **Readout.** The fraction of scaffold in the leading gel band is
  "fully folded", and folded structures are stable during measurement
  (§3.5); liquid-nitrogen shock-freezing stops reactions without
  distorting them (§3.2.1).
- **Dye.** SYBR Green at a low dye-to-DNA ratio does not perturb
  folding, and subtracting a staple-only sample removes background, which
  the author calls not an accurate correction (§3.2.2).
- **Barrier.** A two-state picture with an entropic barrier (Eq. 3.3),
  valid only in a limited temperature window.
- **Model (Chapters 4–5).** A domain-level Gillespie model with spurious
  matches cut off below 4 nt; it omits strand displacement and helix
  electrostatics (§5.3).

## Key results

- **Narrow window (§3.3, p. 20; Figs 3.8–3.9).** In a slow anneal "the
  transition seems to occur in an extremely narrow temperature range of
  only a few degrees"; the SYBR Green assay puts nearly all base pairing
  within about 5 °C.
- **Cooperativity (§3.3, p. 22; Fig. 3.10).** Predicted whole-staple
  melting temperatures centre near 80 °C and single-domain ones near
  10 °C; their contraction into one sharp transition "implies a strong
  cooperativity".
- **Hysteresis (§3.3, p. 22; Fig. 3.11).** "We observe a significant
  hysteresis" of 5–10 °C between folding and unfolding, and "unfolding
  does not occur in the temperature range predicted by the melting
  temperatures of the full staple strand sequences".
- **Isothermal folding (§3.3, p. 25; Fig. 3.12).** It works "with the
  successful temperature ranges roughly corresponding to the lower half
  of the folding transition temperature range"; at 50 °C "most of the
  origamis are fully folded after just 2 hours", while a sample 6 °C
  higher showed "absolutely no folded origamis even after 48 hours". A
  short denaturation step first is still needed: "this step remains
  necessary to break up pre-existing secondary structures".
- **Slow in, fast out (§3.5, pp. 31–33; Figs 3.17–3.18).** Unfolding
  runs "on the order of seconds"; the gap of orders of magnitude implies
  "a large energetic barrier that needs to be overcome for folding",
  argued to be mostly entropic. At low temperature "the system behaves
  less and less like a two-state system".
- **Yield follows speed (§3.5, p. 31; Fig. 3.16).** Yields are higher
  where folding is faster, "with the highest yields occurring at the
  temperatures of fastest folding"; the §3.8 summary gives high yields
  approaching 100% at constant temperature.
- **Subdomains (§3.4, p. 27; Fig. 3.13).** A hinged two-domain object
  shows "two separate transitions instead of one for both processes";
  cooperativity extends "only to structurally connected subdomains", and
  "in folding, base pair formation precedes full structure formation,
  while in unfolding the collapse of the 3-dimensional structure precedes
  full base pair denaturation".
- **Concentrations (§3.6, pp. 33–35).** Higher staple concentration
  raises the folding temperature and rate; scaffold concentration has no
  effect.
- **Routing (§3.7, p. 36; Fig. 3.21).** Three routings of one brick shape
  with identical composition show "more than two orders of magnitude of
  variation between the mean folding times", with "the fast-folding
  Brick-fast design folding at significantly higher temperatures"; "The
  final structure stability is not predictive of the folding rate on its
  own" (p. 38). Permuting the scaffold sequence along a fixed routing
  changed nothing (§5.2.2, pp. 95–96).
- **The path matters (§5.2.4, pp. 99–101; Fig. 5.18).** A design of
  21-nt staples with three 7-nt domains barely folds in 20 h at 40 °C.
  When cooling from 65 °C to 40 °C was shortened by shock-freezing, "Both
  the folding yield and folding rate are significantly higher"; a sample
  cooled slowly over 25 min "does not show any folding whatsoever". The
  reason given: in between, the temperature is "low enough for some
  random match binding to occur but too high for the correct domains to
  form".
- **Arrest (§5.1.3, p. 84; §5.1.5, p. 87).** In simulation, a jump from
  50 °C to 25 °C gives "an arrested state where folding proceeds at an
  extremely reduced rate", and the text reports that "imperfectly folded
  structures do not fold at room temperature even after long waiting
  periods"; defects "are repaired only very slowly since all states
  including incorrect ones are more stable".
- **What traps are (§5.3, p. 104).** Not one trapping state: "the system
  gets lost in a sea of easily accessible incorrect states".
- **Driving force (§2.4, p. 10).** About 17,500 kT at 25 °C for about
  7,500 bases, yet folding "did not succeed until extreme, week-long
  assembly protocols were tried".

## Characterization

- **TEM (§3.1, p. 13)** tells folded from unfolded but "cannot elucidate
  details of the unfolded state", and because of uneven deposition "does
  not allow quantitative analysis of the folding process and folding
  yield".
- **Gel with a Cy5 staple (§§3.2.1, 3.5)** gives the folded fraction but
  not the state of intermediates; the split depends on a cutoff, and lanes
  need a ladder correction.
- **SYBR Green (§3.2.2)** reads base pairs, not structure; a more
  informative high dye concentration cannot be used "without risking
  perturbing the folding process" (p. 19).

## Concepts

- **Folding window**: the few degrees in which the object folds on
  laboratory timescales, usable isothermally.
- **Hysteresis**: unfolding at temperatures 5–10 °C above folding.
- **Random matches**: spurious short complementarities between staples
  and scaffold, which bind at low temperature and inhibit folding.
- **Mean folding time**: from the cumulative fraction-folded curve of a
  gel time series.
- **Cooling-path dependence**: whether a hold at one temperature folds
  depends on how the sample got there.

## Connections

It restates, from the stand-in's side, the 2012 Science paper
[LIT-tmpg98v0](../literature.d/LIT-tmpg98v0.md), which its Chapter 3 cites as ref. [2]: the narrow window,
constant-temperature folding, folding/unfolding hysteresis, subdomain
cooperativity (Fig. 3.13 is marked as adapted from it), and design and
staple-concentration shifts of the folding temperature. It does not
restate the paper's own numbers with certainty: the brick designs and
all of Chapters 4–5 (the kinetic model, the 42-helix-bundle variants,
shock-freeze cooling) may be later work, and the 2012 abstract calls
unfolding equilibrium where the thesis calls it "also an out of
equilibrium process, but less so". It extends the held DeLuca et al.
simulation ([LIT-2081](../literature.d/LIT-2081.md), [NOTE-1561](NOTE-1561.md), [THEORY-1398](../theory.d/THEORY-1398.md)) experimentally on
domain-wise folding and is in tension with it on traps: many accessible
wrong states, not global topological ones. It measures what Rothemund
(2006, [NOTE-tmp8kyp2](NOTE-tmp8kyp2.md)) did not, the window and the hysteresis his anneal
passed through. Wagenbauer, Wachauf and Dietz (2014), from the same
group, use the isothermal protocol and find it slightly less complete
than a ramp.

## Bearing on the record

- **[CLAIM-567](../claims.d/CLAIM-567.md) (feasible, reachable, reliably reachable).** Supports
  empirically: the folded state is vastly favoured, yet at 56 °C nothing
  forms in 48 h, and reliable reaching holds only in a few-degree band.
- **[CLAIM-583](../claims.d/CLAIM-583.md) (same complex, different reachability).** Supports in kind:
  same shape, base-pair count and composition, different routing, rates
  more than 100-fold apart. Routing differs, so it is not the same
  complex; same routing with permuted sequence changed nothing.
- **[CLAIM-571](../claims.d/CLAIM-571.md) (threshold need not equal the holding requirement).**
  Supports for the denaturation step: reaching the target needs about
  65 °C, while folding and holding happen near 40–50 °C, and for the
  short-domain design the path down decides whether a 40 °C hold folds.
  Temperature is a window, not a monotone budget, so a peak requirement
  fits only that step.
- **[CLAIM-581](../claims.d/CLAIM-581.md) (reversible peak costs).** Qualifies: folding and unfolding
  differ in temperature and timescale, so the reversibility premise does
  not hold here.
- **[CLAIM-591](../claims.d/CLAIM-591.md) (directed costs).** Supports: leaving the folded state takes
  5–10 °C more than entering it, and seconds against hours.
- **[CLAIM-569](../claims.d/CLAIM-569.md) (construct, maintain, transition).** Supports directly:
  within the hysteresis band a folded object persists but cannot be
  built. The brick at 56 °C is the example, if its melting lies above
  56 °C as the hysteresis implies; no melting temperature for it was
  found in the text read.
- **[CLAIM-566](../claims.d/CLAIM-566.md) (assemble, persist, regenerate).** Supports assembly and
  persistence as separate: defective folds persist unrepaired at room
  temperature (simulation and lab lore). Nothing on regeneration.
- **[CLAIM-557](../claims.d/CLAIM-557.md), [CLAIM-574](../claims.d/CLAIM-574.md), [CLAIM-570](../claims.d/CLAIM-570.md), [CLAIM-592](../claims.d/CLAIM-592.md) (observing budgets).**
  Illustrate them: TEM merges all unfolded states, the gel merges
  intermediates with a cutoff, SYBR Green counts base pairs, not
  structure. No ordering of probe costs is studied.
- **[CLAIM-572](../claims.d/CLAIM-572.md) (one shared budget).** Weak: a more informative dye readout
  perturbs the folding it observes.
- **[CLAIM-184](../claims.d/CLAIM-184.md) (anchors entrench).** Supports by analogy: early spurious
  bindings block correct structure, and a slow cooling path entrenches
  them.
- **[CLAIM-478](../claims.d/CLAIM-478.md) (scale separation makes constraints).** Supports modestly:
  spurious and dye binding equilibrate fast relative to folding, and the
  assay relies on that separation.
- **[QUESTION-380](../questions.d/QUESTION-380.md) (small compatible nucleus).** Bears: subdomains fold in
  turn, and the 2012 abstract speaks of nucleation-driven pathways;
  predicting a nucleus's effectiveness from design is what the unread
  model chapters attempt.
- **[QUESTION-374](../questions.d/QUESTION-374.md) (two budgets).** Weakly, through the dye that perturbs
  what it observes.
- **Missed by the first search.** [CLAIM-568](../claims.d/CLAIM-568.md) (four ways a transition
  fails): at 56 °C a path exists and is not followed on the timescale;
  the short-domain design is a path that cannot be reliably followed.
  [CLAIM-463](../claims.d/CLAIM-463.md) (restoring conditions need not restore a capacity): the
  hysteresis band is an empirical case, though that a melted object
  returned to the band stays unfolded is inferred, not measured.
  [CLAIM-185](../claims.d/CLAIM-185.md) (a nucleation threshold makes structure persist): by analogy
  only. [QUESTION-373](../questions.d/QUESTION-373.md) (who supplies the resource): the protocol supplies
  the denaturation heat and the choice of window.
- Filed: [THEORY-tmp500wn](../theory.d/THEORY-tmp500wn.md). No instruction for machine-learning practice.

## Limitations

- A thesis, not peer reviewed as a whole, and informally written.
- Mostly one brick family, plus a plate and a gear; magnesium was not
  varied in the sections read.
- Yields are gel-band fractions, and folding times hang on a cutoff.
- The arrested-state result is simulation plus tacit lab knowledge.
- Which Chapter 3 numbers appear in the 2012 paper is not known; only
  some figures and the dye assay are marked as adapted from it.
- The model derivation and the figures themselves were not read.
