---
number: 103
status: Read
formerly:
- NOTE-tmp5mg89
paper: LIT-114
title: 'SEP — Philosophy of statistical mechanics'
version: 2
history:
- version: 2
  date: '2026-09-26'
  note: >-
    Read in full (full text of the Stanford Encyclopedia of Philosophy entry
    as served on plato.stanford.edu ("First published Tue Jan 10, 2023", no
    revision listed) — preamble, §§1–7 (all 23 subsections) and the
    bibliography, read end to end; the figure images and the "extended
    description" supplements for Figures 1–3 were not opened (the figures
    are schematic illustrations described in the text).). Upgraded from
    `Skimmed` to `Read`: the claims table, assumptions and results are new,
    and the skim is corrected where the full text disagreed.
date: '2026-09-26'
summary: >-
  The entry argues that statistical mechanics has no canonical formalism
  but three umbrellas — Boltzmannian SM, the Boltzmann Equation and
  Gibbsian SM — and that every live account of the approach to equilibrium
  (ergodic, typicality, Mentaculus, long-run residence time,
  coarse-graining, interventionist, epistemic) survives Loschmidt's and
  Zermelo's objections only by giving up strict irreversibility or adding
  something outside the isolated dynamics; it closes on the unresolved
  "schism" that physicists compute in GSM while philosophers explain in
  BSM.
---

# NOTE-103: SEP — Philosophy of statistical mechanics

## Contribution

A survey, not a new result. It reorganises the philosophy of SM around the fact that SM has "not yet found a generally accepted theoretical framework or a canonical formalism" (§2). So the philosophy has to classify approaches first and ask how they relate afterwards, rather than interpret one formalism, as the philosophy of quantum mechanics does starting from Hilbert space. For each umbrella (BSM, BE, GSM) the entry sets out the framework, the formal obstacle it meets and the proposed repairs, with the standard objections. It also argues two positions of its authors: equilibrium should be defined by long-run residence time (§4.7), and the BSM/GSM relation is the field's most pressing open question (§6.7).

## Key insight

Hamiltonian micro-dynamics is deterministic, measure-preserving and time-reversal invariant, and bounded systems recur. No account of thermodynamic behaviour can therefore deliver the strictly irreversible approach to equilibrium that thermodynamics describes. Every account in the entry either redefines the target, as "most of the time in equilibrium" or "overwhelmingly likely" (ergodic, typicality, Mentaculus, long-run residence), or brings in something the isolated dynamics lacks: a coarse-graining grid, an environment, an observer's knowledge, or a cosmological boundary condition. What each approach pays for irreversibility is the thing to compare.

## Assumptions

Premises the entry adopts or states as the common background:

- The mechanical background is classical, and foundational debate is conducted there. The quantum case is flagged as understudied (§3, §4.8).
- A system is a dynamical system (X, φ, μ). φ is deterministic, so trajectories do not intersect, and measure-preserving: μ(A) = μ(φ_t(A)), which Liouville's theorem gives for Hamiltonian systems (§3).
- BSM: macro-states supervene on micro-states, and the macro-regions X_M = {x : M(x) = M} partition X (§4.1). Boltzmann entropy is S_B(M_i) = k log μ(X_{M_i}).
- GSM: a density ρ on X evolves as ρ_t(x) = ρ_0(φ_{−t}(x)). Statistical equilibrium means stationarity. Observables are functions f : X → ℝ, and their phase averages are ⟨f⟩ = ∫ f ρ dx (§6.1).
- The authors decline to frame SM's aim as a reduction of thermodynamics, because both the notion of reduction and its success are contested (§1, returned to in §7.5).

## Key results

What the entry reports, with the formal facts it states:

- **Combinatorial argument (§4.2).** Assume non-interacting particles, conserved energy and a one-particle grid parallel to the position and momentum axes. The distribution with the most arrangements is the discrete Maxwell–Boltzmann distribution n_i = α exp(−βE_i), and its macro-region is the largest. Lavis (2008) points out that "largest" does not mean "most of X": in some systems the non-equilibrium regions together are larger. The definition also ignores the dynamics, so it would give an equilibrium even if φ were the identity.
- **Two objections (§4.3).** Loschmidt's reversibility objection (1876) and Zermelo's recurrence objection (1896), the latter from Poincaré recurrence in bounded measure-preserving systems.
- **Ergodic approach (§4.4).** Ergodicity gives time-fractions equal to measure-fractions for almost all initial conditions. Its problems: many SM systems are not ergodic (solids, the Kac ring, anharmonic oscillators, the ideal gas); epsilon-ergodicity (Vranas 1998) helps only some systems; and there is the measure-zero problem (Sklar).
- **Typicality (§4.5).** The claim is that an atypical state "can simply not avoid" becoming typical. Frigg and Uffink object that this is unjustified without a dynamical assumption. Frigg & Werndl (2012) add one, and Lazarovici & Reichert (2015) deny it is needed.
- **Mentaculus (§4.6).** The statistical postulate alone makes a high-entropy past as likely as a high-entropy future. Albert conditionalizes on the Past-Hypothesis, defining I_t = φ_t(X_{M_p}) ∩ X_M, so that the probability of a high-entropy future is μ(I_t ∩ X_M⁺)/μ(I_t). The objections: Earman says the Past-Hypothesis is "not even false"; Winsberg says a low global entropy does not guarantee low entropy in subsystems. The status of the Past-Hypothesis is disputed: a fundamental law (Chen, Goldstein, Loewer), a regulative principle (Albert), a contingent fact that needs explaining (Price), or one that does not (Callender).
- **Long-run residence time (§4.7).** Macro-states are defined thermodynamically, and the equilibrium state is by definition the one the system occupies most of the time in the long run. That its macro-region is large then follows, for interacting systems too. An existence theorem (Werndl & Frigg, forthcoming-b) says equilibrium exists when X splits into invariant regions on which the motion is ergodic and the equilibrium macro-state is the largest on each. The entry states this intuitively; no formal statement is given.
- **Boltzmann Equation (§5).** The Stosszahlansatz gives N(v₁, v₂) = N² f_t(v₁) f_t(v₂) ‖v₂ − v₁‖ πD²Δt. From it come the Boltzmann equation and the H-theorem: dH/dt ≤ 0, with equality iff f is Maxwell–Boltzmann. Lanford's theorem says that in the Boltzmann–Grad limit, for most x, the Hamiltonian and Boltzmann evolutions stay close on [0, t*]. But t* is roughly two-fifths of the mean free time, "in the order of microseconds" for air, during which on average 40% of the molecules collide once. The source of irreversibility in the theorem is disputed (Lanford 1975 vs 1976/81; Cercignani; Valente and Uffink–Valente, who say there is none).
- **GSM obstacles (§6.2–6.3).** The textbook ergodic justification of phase averaging fails on three counts (Malament & Zabell 1980; Sklar): measurements are not infinite time averages; if they were, no change could be observed; and many systems are not ergodic. The fine-grained S_G = −k∫ρ log ρ dx is a constant of motion, and a non-stationary ρ can never become stationary.
- **GSM repairs (§§6.4–6.6).** *Coarse-graining:* needs the system to be mixing (stronger than ergodic), reaches only quasi-equilibrium, and does so only as t → ∞. Its empirical-indistinguishability premise is contested by the spin-echo experiment. *Interventionism:* there is no theorem that an arbitrary environment drives a system to equilibrium; it faces a regress up to the universe, which is blunted only if one denies that laws are universal (Cartwright). *Epistemic (Jaynes/MEP):* there is "no consensus on its significance, or even cogency". It ignores the dynamics, and its entropy under repeated measurement is either non-monotonic or depends on when measurements are made (Lavis & Milligan 1985). Its "most fundamental" problem is that kettles do not boil because of what we know.
- **BSM–GSM relation (§6.7).** The entry lists five positions: Lavis (2005) replaces binary equilibrium by "commonness"; Wallace (2020) makes GSM the more general framework with BSM a special case; Frigg & Werndl take BSM as fundamental and GSM as effective; Goldstein (2019) plays the difference down; Goldstein et al. (2020) find Boltzmann and Gibbs entropies agree to leading order in equilibrium.
- **Further issues (§7).** Probabilities: time-average, propensity and Humean-chance readings each have problems (§7.1). Maxwell's demon: Earman–Norton's dilemma against information-theoretic exorcisms, and Norton's verdict that the Landauer literature is "too fragile" to sustain general claims (§7.2). The Gibbs paradox and individuality (§7.3). SM outside physics: econophysics, population genetics, the free energy principle in biology (§7.4). Phase transitions need the thermodynamic limit: Batterman calls them emergent; Norton, Callender and Butterfield resist; Lavis, Kühn & Frigg and Yi hold that thermodynamics stays in place as an independent theory even if reduction succeeds (§7.5).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | SM has no generally accepted framework or canonical formalism, but most approaches fall under BSM, BE or GSM | informal argument | §2, the classification that organizes the entry |
| C2 | The combinatorial argument shows only that the equilibrium macro-region is the largest, not that it fills most of X, and it fails for interacting systems | informal argument, citing literature | §4.2 (Lavis 2008; Uffink 2007) |
| C3 | Ergodicity cannot explain the approach to equilibrium across the board, because paradigm SM systems, including the ideal gas, are not ergodic | assertion, citing literature | §4.4 (Uffink 1996b; Earman & Rédei 1996; Bricmont 2001) |
| C4 | Every BSM account (ergodic, typicality, Mentaculus, long-run residence) meets the Loschmidt and Zermelo objections only by dropping strict irreversibility | informal argument | stated separately in §§4.4–4.7; not argued as a general result |
| C5 | Long-run residence time gives a definition of equilibrium that holds for interacting systems, and a general existence criterion | assertion, citing the authors' own papers | §4.7 (Werndl & Frigg 2015a, 2015b, forthcoming-b); no proof in the entry |
| C6 | Lanford's theorem vindicates a statistical H-theorem, but only for t* ≈ 2/5 of the mean free time | assertion, citing literature | §5 (Lanford; Uffink & Valente 2015) |
| C7 | The fine-grained Gibbs entropy is constant, and a stationary ensemble cannot arise from a non-stationary one | stated as mathematical fact | §6.3; no proof given (they are standard consequences of Liouville's theorem) |
| C8 | The textbook ergodic justification of phase averaging fails | informal argument, citing literature | §6.2 (Malament & Zabell 1980; Sklar 1993) |
| C9 | Physicists work in GSM while philosophers explain in BSM, the two are not intertranslatable and sometimes not empirically equivalent, and this is pressing but understudied | assertion, citing literature | §6.7 (Anta 2021a; Wallace 2020; Werndl & Frigg 2020b) |
| C10 | Information-theoretic exorcisms of Maxwell's demon are not decisive | reported position | §7.2 (Earman & Norton 1998, 1999; Norton 2005, 2017), with replies by Bub, Bennett, Ladyman & Robertson noted but not adjudicated |
| C11 | Phase transitions in SM require the thermodynamic limit, and whether that means emergence or a failure of reduction is contested | reported debate | §7.5; the entry takes no side |

## Concepts

- **Macro-region X_M**: the set of micro-states that realize macro-state M; the macro-regions partition X (§4.1).
- **Boltzmann entropy**: S_B(M) = k log μ(X_M), a property of a macro-state.
- **Gibbs entropy**: S_G = −k∫ρ log ρ, a property of an ensemble or distribution; formally identical to Shannon entropy (§6.6).
- **Statistical equilibrium (Gibbs)**: stationarity of ρ, as opposed to an individual system being in equilibrium (§6.1).
- **Typicality**: holding in the "vast majority" of cases, measured by μ (§4.5).
- **Past-Hypothesis**: Albert's posit of a low-entropy initial macrocondition of the universe (§4.6).
- **Mentaculus**: the probability assignment generated by deterministic dynamics + Past-Hypothesis + statistical postulate (§4.6).
- **Long-run residence time equilibrium**: the macro-state the system occupies most of the time in the long run (§4.7).
- **Quasi-equilibrium**: a coarse-grained ρ̄ spread uniformly, replacing stationarity by uniformity (§6.4).
- **Interventionism**: environmental perturbations drive the approach to equilibrium (§6.5).
- **Stosszahlansatz**: independence of the velocities of colliding particles before collision (§5).

## Connections

Question about science: the entry addresses the **interpretation and structure of a scientific theory**, specifically which of SM's rival formalisms is *the* theory. It also covers explanation (what explains the approach to equilibrium), **reduction and emergence** (SM and thermodynamics, phase transitions, §7.5), and the interpretation of **probabilities in a deterministic theory** (§7.1). Its position is anti-canonical: SM is a plurality of frameworks. The authors lean towards defining equilibrium by thermodynamic behaviour, and towards BSM as fundamental with GSM as effective. The philosophy-of-science tag is plainly justified. It is close to the blurb's "the interpretation of physical theories" word for word.

Within the record:
- [LIT-150](../literature.d/LIT-150.md) and [LIT-141](../literature.d/LIT-141.md) (emergence): §7.5's phase-transition debate (Batterman vs Norton, Callender, Butterfield) is the standard physics test case for their claims about emergence. The entry takes no side.
- [LIT-082](../literature.d/LIT-082.md) (observational entropy unified with maximum-entropy principles): this is the constructive side of the coarse-graining and Jaynes/MEP threads of §6.4 and §6.6. The entry records that MEP's "cogency" is unsettled and that coarse-graining's empirical premise is contested by spin-echo. A reader of [LIT-082](../literature.d/LIT-082.md) should know both objections.
- [LIT-041](../literature.d/LIT-041.md) (work capacity of channels with memory) and [LIT-010](../literature.d/LIT-010.md) (quantum thermodynamics): both sit downstream of §7.2's Szilard/Landauer lineage. The entry's report of the Earman–Norton dilemma and Norton's "too fragile" verdict is the philosophical counterweight.
- [LIT-039](../literature.d/LIT-039.md) (rigorous renormalization group): bears on §6.2's "thermodynamic limit" research programme and on §7.5.
- [LIT-151](../literature.d/LIT-151.md) cites Wallace, whose "necessity of Gibbsian SM" (2020) is one of the §6.7 positions. The record does not hold that paper.

## Bearing on the record

For the nucleation record: this entry gives a reference map for any note on entropy, coarse-graining, typicality, the arrow of time or emergence in physics, and a reading of [LIT-082](../literature.d/LIT-082.md) should cite it for the standing objections to MEP and to coarse-graining. No THEORY document is supported or contradicted by it directly.

For ML practice: nothing. §6.6 (maximum entropy) and §7.4 (the free energy principle) touch ideas that ML borrows, but the entry says nothing about learning or inference in models. No anthology document should cite it for practice.

## Limitations

- The entry is classical only. Quantum SM is flagged as understudied and not treated (§3, §4.8).
- It explicitly excludes the direction of time and temporal asymmetry, which have their own SEP entry (§7).
- The authors describe their own account (§4.7) sympathetically and without a formal statement. Its existence theorem is cited as forthcoming, and its advantages are asserted rather than demonstrated in the entry.
- Several verdicts are reported rather than adjudicated (§7.2 on Maxwell's demon, §7.5 on reduction). A reader should not take the entry as settling them.
- The internal cross-reference slips noted in `corrections` are cosmetic.

## Open questions

- How are BSM and GSM related (§6.7)? What would close it is a theorem stating when Gibbsian phase averages equal Boltzmannian equilibrium values, of which Werndl & Frigg 2020b is a partial answer, and a principled choice among the five positions.
- Can BSM be formulated quantum-mechanically (§4.8)? Chen's "Wentaculus" and Goldstein et al. 2020 are early steps.
- Macro-states need a precise definition out of equilibrium, for example as local field variables (Frigg & Werndl, forthcoming-a).
- Under what conditions do environments drive systems to equilibrium (§6.5)?
- Is the Past-Hypothesis a law, a regulative principle, or a contingent fact, and does it need explaining (§4.6)?

## Corrections to the seeded skim

- The skim says §4 gives "five explanations of the approach to equilibrium" and then lists four. The full text has four accounts of the approach within BSM (ergodic §4.4, typicality §4.5, Mentaculus §4.6, long-run residence time §4.7); Boltzmann's combinatorial argument (§4.2) defines equilibrium and the entry says it "is silent about why and how systems approach equilibrium".
- The summary frames the field as "rival Boltzmannian and Gibbsian frameworks". The entry names three umbrellas: BSM, the Boltzmann Equation (BE, §5: Stosszahlansatz, H-theorem, Lanford's theorem) and GSM. The skim leaves §5 out entirely.
- The "schism" (§6.7) is the authors' framing, taken from Anta (2021a). It is not only a matter of practice versus explanation: the entry adds that in some contexts the two formalisms "do not even give empirically equivalent predictions" (Werndl & Frigg 2020b).
- The GSM remedies (§§6.4–6.6) answer two formal obstacles, not one: the constancy of the fine-grained Gibbs entropy, and the theorem that a distribution stationary at one time is stationary at all times, so an ensemble cannot evolve into statistical equilibrium (§6.3). The epistemic account's remedy is repeated measurement and conditionalization, not the Gibbs–Shannon identity itself.
- §4.8 lists four problems for BSM, not just closed systems: it deals only with closed systems; its macro-states are ill-defined out of equilibrium; it has no settled quantum version; and practitioners use GSM.
- The entry has some internal slips (not errors of substance). §4.2 sends the reader to §6.5 for coarse-graining, which is §6.4. §5 cites §4.3 for the Boltzmann entropy, which is defined in §4.1. §6.6 cites §6.1 for the problem with phase averages, which is argued in §6.2. The Ehrenfests' review is dated 1911 in the text and 1912 [1959] in the bibliography.
- The philosophy-of-science tag is justified, and philosophy-of-science should stay the primary topic. The secondary tags are weaker than they could be. `information-theory` is justifiably appropriate (§6.6 Gibbs–Shannon/MEP; §7.2 Szilard, Landauer and the entropy costs of computation) and `metaphysics` is too (laws of nature and the Past Hypothesis as a law, §§4.6, 6.5; emergence of phase transitions, §7.5). `probabilistic-modeling` is only marginally apt: the entry is about the interpretation of physical probabilities, not statistical modelling, and Jaynes's MEP is its one point of contact.
