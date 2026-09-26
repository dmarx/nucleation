---
number: 76
status: Read
formerly:
- NOTE-tmpt46pj
paper: LIT-076
title: 'REST2 MD simulations of disordered proteins'
version: 2
history:
- version: 2
  date: '2026-09-25'
  note: >-
    Read in full (Full text of arXiv:2505.01860v1 (3 May 2025,
    physics.chem-ph), 30 pp.: Introduction, REST theory (Eqs. 1–9),
    Materials, Methods (preparation, equilibration, input generation,
    running, analysis), Conclusion, Notes 1–10, Figs. 1–4 and the 60-item
    bibliography (raw4/2505.01860.txt, extracted with PyMuPDF). v1 is the
    only version. The figures came through only as labels, so I relied on
    captions and prose; the chapter's text states no numerical results for
    the worked example. I also spot-checked the accompanying repository
    (github.com/paulrobustelli/IDP_REST_tutorial): the README,
    TUTORIAL_FILES/README.md, the starting PDB and prod.mdp. I checked these
    only to verify the example's sequence and run length, and did not audit
    the scripts.). Upgraded from `Skimmed` to `Read`: the claims table,
    assumptions and results are new, and the skim is corrected where the
    full text disagreed.
date: '2026-09-25'
summary: >-
  A how-to chapter for REST2 enhanced sampling of intrinsically disordered
  proteins in GROMACS 2022.5 with PLUMED 2.9.0, worked on the α-synuclein
  C-terminal fragment (residues 121–140) with the a99SB-disp force field
  and water. The example uses 10 replicas, a solute-temperature ladder
  from 300 K to 450 K, swap attempts every 1.6 ps, and a ≥ ~20 %
  acceptance target. Its load-bearing methodological point is that high
  swap acceptance "is not, in isolation, sufficient evidence of robust
  conformational sampling or convergence". Convergence has to be judged by
  comparing demultiplexed replicas' structural distributions, with
  blocking-analysis errors.
---

# NOTE-076: REST2 MD simulations of disordered proteins

## Contribution

The chapter packages a reproducible end-to-end protocol for Hamiltonian replica exchange with solute tempering (REST2) on IDPs. It covers theory (REST1 versus REST2 scaling, the exchange criterion), software versions, force-field choice, starting-structure construction, solvation with identical water counts across replicas, a two-barostat equilibration, scaled-topology generation with PLUMED partial_tempering, the mdrun invocation, demultiplexing, PBC correction, and convergence diagnostics. All inputs and analysis scripts are released. Nothing in it is new science; the contribution is operational.

## Key insight

In REST2 only the solute's own and solute–solvent energies enter the swap criterion (Eq. 8), so few replicas can span a wide effective temperature range. The price is that the ladder's upper rungs are unphysical Hamiltonians, where IDPs over-collapse. Replicas can then swap freely without ever rearranging the chain. Acceptance ratios and round-trip times therefore diagnose ladder mixing, not conformational sampling, and convergence has to be read from whether independent demultiplexed replicas sample the same conformational distributions.

## Assumptions

The chapter's premises, with its sources:
- **Replica exchange is valid sampling.** Metropolis swaps preserve detailed balance, so each rung samples its Boltzmann distribution; continuous-time dynamics is lost (pp. 3–4; Sugita & Okamoto 1999).
- **REST2 scaling (Eq. 5; Wang, Friesner & Berne 2011).** E_n = (β_n/β0)E_pp + √(β_n/β0)E_pw + E_ww at a common thermostat T0. The effective solute temperature follows from β_n/β0 = T0/T_n (Eq. 6).
- **Force field.** Many AMBER/CHARMM protein–water combinations are inaccurate for IDPs, and a99SB-disp "has been found to provide accurate descriptions of many IDPs" (p. 7; Robustelli et al. 2018). This is the authors' own force field.
- **Starting structures matter at practical run lengths.** Ensembles from 1–10 µs per replica "will usually retain some starting–structure dependence" (p. 10).
- **Rules of thumb.** These are stated, not derived:
  - a box length about 4× the IDP's R_g (citing ref. 48);
  - at least about 20 % swap acceptance;
  - PBC contacts under 2.0 nm in fewer than 1 % of frames;
  - maximise aggregate ns/day when choosing the replica count.

## Key results

What the chapter recommends and records:
- **Exchange criterion (Eq. 8).** Δ_{n,n+1} = (β_n − β_{n+1})[(E_pp(X_{n+1}) − E_pp(X_n)) + √β0/(√β_n + √β_{n+1})(E_pw(X_{n+1}) − E_pw(X_n))], and P_acc = min(1, e^{−Δ}). E_ww drops out, so REST2 needs far fewer replicas than tREMD.
- **Ladder.** Geometric, T_n = T0 exp[n log(T_high/T0)/N_r] (Eq. 7); the partial_tempering scaling factor is λ_n = T0/T_n.
- **Example set-up.**
  - Force field: a99SB-disp protein and water, CHARMM22 ions.
  - Box: 6.5 nm cubic, 8763 waters, 8 Na⁺.
  - Minimisation: steepest descent, up to 5000 steps, to F_max = 100 kJ mol⁻¹ nm⁻¹.
  - Heating: 1 ns NVT with V-rescale.
  - Equilibration: 1 ns NPT with the Berendsen barostat, flagged as fast but not producing correct kinetic-energy distributions, then 40 ns NPT with Parrinello–Rahman. Coupling constants 1 ps (temperature) and 5 ps (pressure).
  - Production: dt = 2 fs, -replex 800 (swaps every 1.6 ps), coordinates saved every 80 ps. Ten replicas (Fig. 2, Note 9) spanning 300–450 K solute temperature (Fig. 3c).
- **Starting structures.**
  - Use extended chains (φ = −180°, ψ = +180°) for 10–40-residue IDPs; for longer chains, collapse them in short vacuum simulations first.
  - Start prolines in ppII (Φ = −75°, Ψ = 145°) and keep all ω trans unless evidence says otherwise.
  - Seed experimentally known helices at φ = −57°, ψ = −47°.
  - Prefer different starting structures across replicas.
  - AlphaFold models or bound-state PDB structures can serve as seeds (Note 3).
- **Diagnostics.** Per demultiplexed replica: P(T0), mean effective solute temperature and round-trip time (Fig. 2). Across temperature replicas: a smooth temperature dependence of R_g, helicity and contacts, with higher solute T giving more compact states, more contacts and less secondary structure (Fig. 3). Across demultiplexed replicas: agreement within blocking errors (Fig. 4; Flyvbjerg–Petersen via pyblock).
- **Convergence verdict.** "Obtaining high acceptance rates on swap attempts is not, in isolation, sufficient evidence of robust conformational sampling or convergence. It is therefore essential to compare the distributions of conformations sampled in each demultiplexed replica" (p. 18). For IDPs over about 40 residues, some demultiplexed replicas "will occasionally become stuck".

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | REST2 swap acceptance is independent of water–water energy, so far fewer replicas are needed than in tREMD | strong | derivation, Eq. 8 (standard result, Wang et al. 2011) |
| C2 | The number of replicas tREMD needs "scales exponentially with the degrees of freedom" | weak (misstated) | assertion (p. 2), uncited. The standard result is that the replica count grows roughly as the square root of system size for a fixed temperature range; it is the swap acceptance at fixed spacing that falls exponentially. This is my note from general knowledge, not a correction the chapter makes |
| C3 | IDPs over-collapse at high solute temperature in REST2; REST3 and REHT mitigate this | moderate (secondary) | cited to refs 23–24; the chapter shows only a qualitative trend in its own example (Fig. 3) |
| C4 | High acceptance alone does not demonstrate convergence; compare demultiplexed-replica distributions | moderate | argument (pp. 17–18) with an example in Figs. 2–4; no failed-run counterexample is shown |
| C5 | A smooth temperature dependence of structural properties across rungs indicates meaningful sampling | weak | assertion (p. 17), a heuristic |
| C6 | a99SB-disp accurately describes many IDPs | moderate (secondary) | cited to the authors' own force-field paper (ref. 4) |
| C7 | Swap attempts every 1.6 ps with a ≥ ~20 % acceptance target and 1–10 µs per replica are reasonable defaults | weak | practitioner rule of thumb, uncited |
| C8 | Scaling the solute potential by 0.5 at T = 300 K is "effectively equivalent" to a separate 600 K solute thermostat | weak | holds exactly only for E_pp; E_pw is scaled by √(β_n/β0) (Eq. 5), so the equivalence is approximate. My note |

## Method

1. **Build.** Choose the starting structures, solvate each replica with an identical water and ion count (gmx solvate -maxsol), and neutralise.
2. **Equilibrate.** Minimise, heat under NVT, then run the Berendsen NPT and Parrinello–Rahman NPT stages. Every replica must reach the target pressure, since pressure mismatches stall swaps under NVT.
3. **Generate inputs.** Produce a unified processed.top without position restraints. Mark solute atom types with a trailing underscore (awk over the [atoms] lines). Run plumed partial_tempering λ_n for each rung, then grompp each replica with an empty plumed.dat.
4. **Run.** mpirun gmx mdrun -multi … -replex 800 -plumed plumed.dat, with equal resources per replica. Check acceptance early.
5. **Analyse.** Demultiplex with demux.fix.pl and trjcat -demux, striding the index to the output frequency. Apply PBC corrections (nojump → whole → mol). Compare temperature replicas and demultiplexed replicas with blocking-analysis errors. The final analysis is done on the unscaled 300 K replica.

## Concepts

- **Temperature replica.** All frames at one rung, e.g. the 300 K base replica.
- **Demultiplexed replica.** One continuous coordinate set followed as it diffuses through the ladder.
- **Round-trip time.** The mean time for a demultiplexed replica to go from the base rung to the top rung and back.
- **Effective solute temperature.** T0/λ_n for the scaled Hamiltonian; not a physical temperature.
- **REST1 / REST2 / REST3 / REHT.**
  - REST1: per-replica temperatures with scaled E_pw and E_ww (Eq. 3).
  - REST2: a common thermostat with scaled E_pp and E_pw (Eq. 5).
  - REST3: adds scaling of solute–solvent van der Waals interactions.
  - REHT: heats the solvent too, on a gentler ladder.

## Connections

The chapter implements Liu et al. 2005 (REST) and Wang et al. 2011 (REST2), through Bussi's 2014 GROMACS/PLUMED Hamiltonian replica exchange implementation. It situates REST2 against tREMD (Sugita & Okamoto; Hansmann) and the IDP-specific variants REHT (Appadurai et al. 2021) and REST3 (Zhang et al. 2023). Its force-field choice rests on Robustelli, Piana & Shaw 2018. As a sampling method it belongs to the replica-exchange / parallel-tempering MCMC family; the dossier's `probabilistic-modeling` tag reflects that and nothing more specific.

## Bearing on the record

This is a computational-chemistry methods tutorial. It carries **no instruction for machine-learning practice**, and the dossier is right that it is not an Anthology `biomolecular-modeling` document. Two narrow points could matter to a future ML reader:
- The convergence lesson (swap acceptance measures ladder mixing, not sampling) generalises to parallel tempering used anywhere, including tempered MCMC in probabilistic ML. The chapter does not make that link, and it is an informal argument here, not a measured result.
- If the record later takes up ML ensemble generators for IDPs (e.g. models trained on MD ensembles), this is the kind of protocol their reference ensembles come from. Its caveats then matter: at 1–10 µs per replica there is residual starting-structure dependence, and chains longer than 40 residues get stuck replicas.

## Limitations

- The chapter reports no quantitative outcome for its example: no acceptance ratios, R_g values or convergence statistics in the text, only figure panels. There is no comparison with tREMD, REST3, REHT or unbiased MD, so it cannot tell a reader which variant to prefer.
- The example is a short, highly charged, NMR-disordered 20-mer, the easy case. The chapter itself says convergence is harder above about 40 residues.
- The textual errors (sequence, GROMACS version, C2's scaling claim, typos in Note 9's awk and Note 1's install script) mean the repository should be treated as authoritative. Note 7 is also cited where the REST.top editing is actually described in Note 8.
- Its convergence criteria (smooth trends, demultiplexed agreement "within statistical sampling errors") are heuristics with no quantitative threshold.

## Open questions

- For IDPs over 40 residues, how much do REST3 or REHT reduce stuck demultiplexed replicas relative to REST2 at equal cost? A head-to-head on one construct with fixed GPU-hours would answer it.
- Is there a quantitative convergence criterion across demultiplexed replicas, e.g. a divergence between their R_g or contact distributions with a threshold, that would replace the visual comparison?
- How large is the residual starting-structure dependence at 1 µs per replica for this 20-mer? It could be measured with two independent REST2 runs from different seed sets.

## Corrections to the seeded skim

- **The printed sequence is not the simulated construct.** The chapter says it simulates "the last 20 residues of α–synuclein (residues 121–140)" and prints the sequence "DMPVDPDNEAYEMPSEEGYQDYEPEA" (p. 11). That string is 26 residues, α-syn 115–140. The repository's starting structure (TUTORIAL_FILES/initial_input_files/prot_only.pdb) holds the 20 residues DNEAYEMPSEEGYQDYEPEA, 121–140. So do the chapter's own processed.top excerpt (first residue ASP 121, Note 8) and its stated net charge of −8 with 8 Na⁺: by my count, 121–140 with free termini gives −8, whereas 115–140 would give −10. The extra "DMPVDP" prefix is an error in the text.
- **The venue is still unverified.** The dossier says the host book is not named, and after a full read that still holds. The text says "this chapter" throughout, and the repository README mentions "the Book Chapter" without naming it.
- **The tutorial run length comes from the repository, not the chapter.** The chapter gives only the generic "1–10 µs per replica" (p. 10). The repository's prod.mdp sets nsteps = 500,000,000 at dt = 2 fs, i.e. 1 µs per replica. The README estimates about 3 days on 10 NVIDIA A5500 GPUs or about 10 days on 2.
- **The GROMACS version differs between sections.** Materials says the tutorial used GROMACS 2022.5 (p. 7); the install script in Note 1 checks out GMX_version = 2024.3.
- The dossier's other points check out against the full text: the four-stage workflow, the REHT/REST3 remedies for IDP collapse, and the starting-structure advice.
