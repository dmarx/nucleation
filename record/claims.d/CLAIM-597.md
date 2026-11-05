---
number: 597
status: Proposed
formerly:
- CLAIM-tmps9wa1
title: 'Where every replacement part is supplied from outside, an organization can become independent of what founded it but never of what feeds it: with damage at rate d and supplied repair at rate ρs the intact fraction holds at ρs/(ρs + d), needs a supply growing as θ/(1 − θ) times the damage rate to hold a share θ, and decays as e^(−dt) once the supply stops, as DNA origami that self-heals from a strand pool and origami that replicates from supplied monomers both show'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the model: an intact fraction under first-order damage at
  rate d and repair at rate ρs proportional to an external supply that does
  not settle at ρs/(ρs + d), or that does not decay as e^(−dt) when s is set
  to zero; or a regenerating DNA nanostructure, or other system, whose
  replacement parts all come from outside and which nonetheless holds its
  intact share after the supply is withdrawn. Not defeated by systems that
  make some of their own parts, which the claim excludes.
tags:
- complex-systems
- natural-sciences
- mathematics
date: '2026-11-05'
line:
- readiness
- realizability
complements:
- CLAIM-566
- CLAIM-516
bears_on:
- QUESTION-398
- QUESTION-399
- QUESTION-090
summary: >-
  The assistant's, on the owner's invitation of 2026-11-05 to add readings
  and claims to the DNA origami filing. A's [QUESTION-398](../questions.d/QUESTION-398.md) asks when a
  partial organization becomes independent of the intervention that
  established it. Two readings separate formation from upkeep.
  Scheckenbach et al. 2021: folded origami regenerates from a pool of
  strands in solution. In serum, matching staples keep 76 % of structures
  intact over 11 days against 12 % without, but only at low damage rates,
  and the supply was never withdrawn. Zhou et al. 2021: in replicating
  origami the species that comes to dominate does so independent of the
  initial seed, yet every cycle needs fresh monomers, a thermal program
  and UV. In a one-line model with
  damage at d and supplied repair at ρs, the intact fraction is
  ρs/(ρs + d). Holding a share θ needs ρs = d·θ/(1 − θ), 9d for 90 % and 99d
  for 99 %, and withdrawal returns decay at the damage rate. Such
  regeneration is not closure: the turnover [CLAIM-516](CLAIM-516.md) excludes, basal
  external production, is exactly what these systems run on. The wording
  is the assistant's (Claude, in this session); adopting it is the
  owner's call.
---
<!-- inactive-ok-file: CLAIM-tmpoh07b CLAIM-tmpw4ai2 NOTE-tmp22pjn — new; readings and claims of the aid-dependency filing, cited as open -->
<!-- inactive-ok-file: CLAIM-566 LIT-2132 — Proposed, Skimmed or new; entries cited as open -->

# CLAIM-597: Where every replacement part is supplied from outside, an organization can become independent of what founded it but never of what feeds it: with damage at rate d and supplied repair at rate ρs the intact fraction holds at ρs/(ρs + d), needs a supply growing as θ/(1 − θ) times the damage rate to hold a share θ, and decays as e^(−dt) once the supply stops, as DNA origami that self-heals from a strand pool and origami that replicates from supplied monomers both show

## The claim

Let I be the intact fraction of a population of structures. Parts are
damaged at rate d, and damaged structures are repaired at rate ρs, where s
is the concentration of a supply that comes entirely from outside. Then

  dI/dt = −d I + ρ s (1 − I).

1. **Upkeep is bought, not acquired.** The intact fraction settles at
   I* = ρs/(ρs + d). Holding a share θ needs ρs = d·θ/(1 − θ): with d = 0.2
   and ρs = 1, I* = 0.833. The required supply is 9d for θ = 0.9 and 99d for
   θ = 0.99, so it grows without bound as θ → 1.
2. **Withdrawal returns decay.** With s = 0 after time 0, I(t) = I* e^{−dt}.
   From 0.833 that is 0.682 at t = 1, 0.307 at t = 5 and 0.113 at t = 10. In
   A's measure ([QUESTION-398](../questions.d/QUESTION-398.md)), the drop on withdrawal D never falls to
   zero for upkeep, however mature the structure.
3. **Formation and upkeep can come apart.** A population can become
   independent of what founded it, as when the composition replication
   reaches no longer depends on the founding seed, while staying fully
   dependent on what feeds it.

## The molecular instances

- **Self-healing from a pool.** Scheckenbach et al. 2021 ([NOTE-1636](../notes.d/NOTE-1636.md)): labels exchange from
  a 5 nM pool, and missing staples are refilled where the damage exposes a
  toehold. In serum, matching staples at 22.5 nM each keep 76 % intact over
  11 days, against 12 % without and 56 % with non-matching DNA. "Self‐healing
  of DNA origami is thus limited to lower damage rates". Throughout, the
  repair pool is supplied, and it was never withdrawn.
- **Replication from supplied monomers.** Zhou et al. 2021 ([NOTE-1628](../notes.d/NOTE-1628.md)), standing
  in for He et al. 2017 ([LIT-2132](../literature.d/LIT-2132.md)): copies template further copies, at up to about 4 per
  cycle, and the faster-growing species comes to dominate "independent of
  the initial seed". So the population's outcome forgets its founder.
  Monomers are replenished each cycle, and the thermal program and UV
  crosslink are imposed from outside.

## What it adds

- **To [CLAIM-566](CLAIM-566.md).** Regeneration in DNA origami is real, and so is
  replication, but both are bought from outside, which is the claim's
  "without producing the constraints that would regenerate it". This
  corrects the filing's earlier statement that nothing in the origami read
  here repairs itself.
- **To [CLAIM-516](CLAIM-516.md).** [CLAIM-516](CLAIM-516.md) sets aside basal external production, and these
  systems persist under turnover only by it.
- **To readiness.** A capacity kept by standing supply has a cost that rises
  steeply with the share kept and with the damage rate. Like a reserve,
  that cost is easy to read as waste while it is working.

## What it does not say

- **That the linear model fits origami quantitatively.** Scheckenbach et al.'s
  limit at high damage rates involves non-specific protection by any DNA,
  which the model leaves out.
- **That no DNA system can make its own parts.** Such a system would fall
  outside the claim and would bear on [QUESTION-399](../questions.d/QUESTION-399.md).

## Note of 2026-11-05: the readings on aid dependency and self-sufficiency

Read at the owner's request to look to aid and development for theory on how aid-dependent organizations become self-sufficient; the works were chosen by the assistant.

- **Supported at the scale of a state.** Ostrom et al. ([NOTE-tmp22pjn](../notes.d/NOTE-tmp22pjn.md)) find Zambia's Kafue Gorge station maintained from outside since 1970, its operator "remains completely dependent on outside funds for the continued operation". Moss, Pettersson and van de Walle ([NOTE-tmpd45i4](../notes.d/NOTE-tmpd45i4.md)) count about three dozen countries that have received a tenth of GNI or more in aid for two decades. In the Kenya summary of the FANTA exit study ([NOTE-tmp46avq](../notes.d/NOTE-tmp46avq.md)), activities fed by project inputs until the end declined after exit, while savings groups, whose key was "lack of dependency on outside financing", held.
- **Qualified: the supply is not neutral.** The claim's repair term leaves the organization's own capacity alone. In every reading the supply lowers it. Recipients of assured help lose skill and effort, the Samaritan's dilemma (Ostrom et al.). Revenue machinery that is not used decays (Moore, [NOTE-tmpfngj0](../notes.d/NOTE-tmpfngj0.md)). Funding for form crowds out local effort (Andrews, Pritchett and Woolcock, [NOTE-tmpfpey1](../notes.d/NOTE-tmpfpey1.md)). States make some of their own parts, so they fall outside the claim's scope. [CLAIM-tmpoh07b](CLAIM-tmpoh07b.md) models that case: supply used before the organization's capacity lowers what capacity is kept, and Azam, Devarajan and O'Connell's 1999 model ([NOTE-tmpvgfdp](../notes.d/NOTE-tmpvgfdp.md)) already has the steady-state part.
- **Moved, not ended.** In the India summary ([NOTE-tmp9wlcj](../notes.d/NOTE-tmp9wlcj.md)) activities continued after exit where government programmes took them over, so the supply changed provider.
- **Self-maintaining upkeep.** [CLAIM-tmpw4ai2](CLAIM-tmpw4ai2.md) adds the other kind the record's dissipative structures separate: upkeep drawn in by the structure's own state, which escapes dependence on a provider but not on the flux, at the price of thresholds.

No status changes.
