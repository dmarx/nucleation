---
number: 683
status: Read
formerly:
- NOTE-tmp7l8yg
paper: 'LIT-882'
title: 'An exact mapping between the Variational Renormalization Group and Deep Learning'
version: 2
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read in full from the arXiv PDF of v1, the only version
    (arXiv:1410.3831v1, 14 October 2014, 8 pp.), text extracted with
    pdftotext. Every section, both appendices and the reference list
    read. The derivation of Sections I and III (Eqs. 1–22) checked line
    by line, and the free-energy consequence noted under Limitations
    derived by me from Eqs. 4, 6, 7 and 18. Figures read from captions
    and text only; the receptive-field images did not survive
    extraction. The "SI Materials and Methods" and the Matlab file the
    appendix refers to are not part of the arXiv record and were not
    seen. For the dispute, the relevant passages of Koch-Janusz and
    Ringel (LIT-873, arXiv v2: main text p. 4 and the supplement's
    "Comparison with contrastive divergence trained RBMs", pp. 17–18)
    were re-read from the copy read for NOTE-674.
- version: 2
  date: '2026-10-09'
  note: >-
    Corrected: the free-energy point under Limitations was called "not in
    either paper". Lin, Tegmark & Rolnick's v2 appendix (LIT-887,
    read in NOTE-688) makes it in substance, and the authors conceded
    Eq. 8's "iff" as a typo in arXiv 1609.03541.
date: '2026-10-09'
summary: >-
  Identifies Kadanoff's variational RG kernel with an RBM energy by
  T = −E + H, so that the coarse-grained Hamiltonian is the RBM's
  hidden-marginal Hamiltonian for any parameters and an exact RG step is a
  perfect fit of the data. The identity is correct but definitional, and
  the paper concedes the approximate schemes differ; its evidence that
  trained networks do RG is qualitative. [LIT-873](../literature.d/LIT-873.md) is right that fitting
  the distribution need not give RG, though it does not engage the
  identity.
---
<!-- inactive-ok-file: THEORY-197 THEORY-194 THEORY-036 QUESTION-025 THEORY-185 — Proposed or open; cited as what this reading produced, the account it is set beside, a neighbour, and the question it does not answer -->

# NOTE-683: An exact mapping between the Variational Renormalization Group and Deep Learning

## Contribution

It writes Kadanoff's variational real-space RG and the restricted
Boltzmann machine in one notation and shows that, under the
identification T = −E + H of the RG kernel with the RBM energy, the
coarse-grained Hamiltonian of RG and the marginal Hamiltonian of the RBM's
hidden layer are the same function, and that Kadanoff's exactness
condition is the same as the RBM reproducing the data distribution
exactly. It adds a deep network that carries out decimation of the 1D
Ising chain by construction, and an observation that a stacked RBM trained
on near-critical 2D Ising samples has local receptive fields that grow
with depth. It was, as far as its references show, the first statement of
the RG–deep-learning correspondence in this form, and the paper later work
on the question answers to.

## Key insight

A coarse-graining that integrates out visible spins against a coupling
kernel and an RBM that marginalizes its visible layer are the same
operation written twice: once the kernel is defined as the RBM's energy
plus the data Hamiltonian, the two coarse Hamiltonians cannot differ. What
the identity leaves open is the thing RG is for: which kernel to choose.
RG chooses it to preserve the long-distance physics; an RBM chooses it to
reproduce the data. The two choices coincide only where both are exact.

## Assumptions

- **Binary spins, Boltzmann data.** P(v) = e^{−H(v)}/Z with temperature
  set to one; H is a general polynomial in the spins (Eq. 3).
- **RBM energy** E(v, h) = Σ b_j h_j + Σ v_i w_ij h_j + Σ c_i v_i (Eq. 10;
  the sign convention is the paper's), joint p_λ = e^{−E}/Z_λ.
- **The identification** T(v, h) = −E(v, h) + H(v) (Eq. 18) is a
  definition, not a result. It makes T depend on the data Hamiltonian, so
  T is not a fixed functional form in λ applied across a family of
  Hamiltonians, as a Kadanoff kernel usually is.
- **Exact RG** is taken to mean Tr_h e^{T(v,h)} = 1 for every v (Eq. 9).
- **The 2D experiment.** Periodic 40 × 40 Ising lattice at J = 0.408
  (paramagnetic side); equilibrium Monte Carlo samples (20,000 in the
  text, 40,000 in Appendix A); four RBMs of 1600, 400, 100 and 25 units
  trained layer by layer by contrastive divergence for 200 epochs with
  an L1 penalty of 2 × 10⁻⁴, chosen "to ensure that one could not have
  all-to-all couplings"; no convolution.

## Key results

- **Eq. 21.** With T = −E + H, H^RG_λ(h) = H^RBM_λ(h) for every λ: the
  RBM's hidden marginal is of Boltzmann form with the RG Hamiltonian. The
  proof is two substitutions (Eqs. 19–20). The authors note it does not
  use the form of E, so it holds for any Boltzmann machine.
- **Eq. 22.** e^{T(v,h)} = p_λ(h|v) e^{H(v) − H^RBM_λ(v)}. Hence when
  Tr_h e^T = 1 for every v, the RBM's visible Hamiltonian is the data
  Hamiltonian, D_KL(P‖p_λ) = 0, and T is exactly the log of the
  conditional p_λ(h|v). (The converse also holds, up to an additive
  constant in E.)
- **Approximations differ** (end of Section III, the paper's own words):
  variational RG schemes "work at the level of the Hamiltonians and Free
  Energies", whereas RBMs minimize the KL divergence, so "the two
  approaches employ distinct variational approximation schemes for coarse
  graining".
- **1D Ising** (Fig. 2). Decimating every other spin gives
  tanh J^(n+1) = tanh² J^(n), flowing to the stable fixed point J = 0.
  Written as a layered network with interlayer weights J^(n), marginalizing
  a layer is one decimation. The authors note it "contains no information
  about half of the visible spins".
- **2D Ising** (Fig. 3). Effective receptive fields (products of the
  weight matrices, Appendix B) of the 100 middle and 25 top units are
  local blocks of roughly equal size within a layer, larger in higher
  layers; reconstructions from the top layer keep the samples'
  macroscopic domains, at a compression of 64.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Under T = −E + H, the RG coarse-grained Hamiltonian equals the RBM hidden-marginal Hamiltonian, for any parameters and any Boltzmann machine | strong (proof), but true by construction | Eqs. 18–21 |
| C2 | An exact variational RG step (Tr_h e^T = 1) is the same as an RBM fitting the data distribution exactly | strong (proof) | Eq. 22 |
| C3 | ΔF = 0 is equivalent to the exactness condition (Eq. 8) | not supported; false in general | Eq. 8 asserts "⟺"; see Limitations |
| C4 | There is a "one-to-one mapping" between RBM-based deep networks and variational RG | moderate as a correspondence of model classes; not as a correspondence of procedures | C1–C2, with the paper's own concession that the approximate schemes differ |
| C5 | A deep network can implement decimation of the 1D Ising chain | strong, by construction | Fig. 2, Eq. 24 |
| C6 | A stacked RBM trained on near-critical 2D Ising samples self-organizes into block-spin-like coarse-graining | weak | one temperature, one lattice size, qualitative receptive fields, locality encouraged by L1; Fig. 3 |
| C7 | Deep learning may be employing a generalized RG-like scheme | weak (hedged suggestion) | C1–C6 |

## Method

Section I reviews Kadanoff's variational RG: a kernel T_λ(v, h), the
coarse Hamiltonian from Eq. 6, the free energies F^v and F^h_λ, and the
choice of λ by minimizing ΔF = F^h_λ − F^v. Section II reviews RBMs,
their marginals and KL training, and stacking. Section III defines T by
Eq. 18 and derives Eqs. 19–22. Section IV gives the 1D construction
analytically and the 2D experiment numerically, using Hinton and
Salakhutdinov's stacked-RBM code (unsupervised phase only).

## Concepts

- **variational RG**: Kadanoff's real-space scheme in which hidden spins
  are coupled to physical spins through a parametrized kernel T_λ, and λ
  is chosen variationally; here, by minimizing ΔF.
- **exact RG transformation**: one with Tr_h e^{T(v,h)} = 1 for every
  configuration v, so that the partition function is preserved.
- **H^RG_λ, H^RBM_λ**: the coarse Hamiltonian defined by tracing out v
  against T, and the Hamiltonian of the RBM's hidden marginal p_λ(h).
- **effective receptive field**: r^(l) = r^(l−1) W^(l) with r^(1) = W^(1),
  the product of the weight matrices up to layer l; a measure of which
  visible spins a hidden unit is coupled to through the stack.

## Connections

It rests on Kadanoff's variational RG (Kadanoff, Houghton and Yalabik
1976; Efrati, Wang, Kolan and Kadanoff 2014, which reads tensor-network
methods as variational RG) and on Hinton's stacked RBMs and contrastive
divergence. Within this record its sequel in argument is Koch-Janusz and
Ringel ([LIT-873](../literature.d/LIT-873.md)), and the account produced from that reading is
[THEORY-194](../theory.d/THEORY-194.md). The third position, Lin, Tegmark and Rolnick's denial that
RG and unsupervised learning are related (arXiv:1608.08225), is not held.

## The dispute with [LIT-873](../literature.d/LIT-873.md), on both texts

**What [LIT-873](../literature.d/LIT-873.md) says.** Main text p. 4: its dimer filters "are orthogonal
to those obtained using Kullback-Leibler (KL) divergence", which "shows
that standard RBMs minimizing the KL-divergence do not generally perform
RG, thereby contradicting prior claims" (this paper). The supplement
(pp. 17–18): this paper "claims an 'exact' mapping"; "our theoretical
arguments, as well as explicit numerical results on dimer model disprove
the very general claims" of it; "a neural network is not specified
without the cost function", and this paper assumes the KL cost
explicitly. The evidence is one CD-trained RBM on fully packed dimers with
added decoupled spin pairs: with few hidden units it couples to the noise
pairs, with many it learns columnar rather than staggered dimer textures.

**What this paper claims, read exactly.** The proved content is C1 and
C2. The title says "exact mapping" and the discussion "one-to-one
mapping", but the interpretive claims are hedged: the mapping "suggests"
that deep networks implement "a generalized RG-like procedure", and the
2D result "suggests the DNN is self-organizing to implement block spin
renormalization". The paper does not state that every KL-trained RBM
performs RG, and at the end of Section III it says in terms that, short
of exactness, RG and RBM training "employ distinct variational
approximation schemes".

**Assessment.**

- **On the identity, this paper stands and [LIT-873](../literature.d/LIT-873.md) does not touch it.**
  Eqs. 18–22 are correct, and [LIT-873](../literature.d/LIT-873.md) neither disputes nor engages them.
  Its word "disprove" applies to the interpretation, not to the
  mathematics.
- **On what the identity shows, [LIT-873](../literature.d/LIT-873.md) is right, and for a reason this
  paper's own text supplies.** The identity holds for every λ, trained or
  not, good RG or bad, so it cannot by itself select a coarse-graining.
  The only point at which RG and RBM training provably coincide is the
  exact one, and an RBM with a restricted number of hidden units cannot
  match an arbitrary distribution exactly, as the paper notes citing Le
  Roux and Bengio (the bound it quotes is 2^N hidden units; a
  coarse-graining has fewer than N). Everywhere training actually operates, the two procedures
  optimize different things, which is [LIT-873](../literature.d/LIT-873.md)'s "the cost function
  decides" and this paper's "distinct variational approximation schemes".
  [LIT-873](../literature.d/LIT-873.md) adds what the concession lacked: a case where the difference
  changes which variables are kept, and an objective (mutual information
  with the environment beyond a buffer) that keeps the right ones.
- **The point is sharper than either paper says.** By my derivation from
  Eqs. 4, 6, 7 and 18 (reached independently; Lin, Tegmark and Rolnick's v2
  appendix, [LIT-887](../literature.d/LIT-887.md), makes the same point in substance): under the identification,
  F^h_λ = −log Z_λ, so ΔF = log Z − log Z_λ. Variational RG's own
  criterion, ΔF, then measures only the RBM's normalization; it vanishes
  for any λ once E is shifted by a constant, and carries no information
  about how well the RBM fits or coarse-grains. In general ΔF = 0 says
  only that ⟨Tr_h e^T⟩_P = 1, an average, so Eq. 8's "⟺" with the
  pointwise condition is wrong. The mapped variational RG therefore has
  no non-trivial approximate criterion of its own; the only criterion
  left on the RBM side is KL, which is the one [LIT-873](../literature.d/LIT-873.md) shows can keep the
  wrong variables.
- **On the evidence, [LIT-873](../literature.d/LIT-873.md)'s counterexample does not refute this
  paper's 2D observation, and does not need to.** The setups differ: one
  CD-trained RBM on noisy dimers there, an L1-penalized four-layer stack
  on clean Ising here. Clean Ising near T_c has no strongly patterned
  short-range noise to latch on to, and block-like receptive fields there
  are what local correlations and an L1 penalty set to forbid all-to-all
  couplings would give in any case; growing receptive fields follow from
  composing sparse local weight matrices. So this paper's 2D result was
  weak evidence for RG before [LIT-873](../literature.d/LIT-873.md) and is not contradicted by it;
  [LIT-873](../literature.d/LIT-873.md) shows the inference from it to "deep learning does RG" does not
  generalize.
- **Where [LIT-873](../literature.d/LIT-873.md) overreaches.** "Contradicting prior claims" and "very
  general claims" read this paper at its title and abstract rather than
  at its hedged conclusions and its own concession. Its counterexample is
  one dataset, one architecture and one training algorithm; it shows that
  distribution fitting need not give RG, not when it does ([NOTE-674](NOTE-674.md)'s C4
  and limitations already say so).
- **Verdict.** On the question actually in dispute, whether unsupervised
  training by distribution fitting performs RG, [LIT-873](../literature.d/LIT-873.md) is right and this
  paper gave no reason to think otherwise beyond a suggestive picture.
  On the exact correspondence of the two formalisms, this paper is right,
  and the correspondence is narrower than its title: exact as a
  re-parametrization and at the exact point, silent everywhere else.

## Bearing on the record

- **Produces [THEORY-197](../theory.d/THEORY-197.md)**: the correspondence is an identity of
  parametrizations whose only non-trivial content is the coincidence of
  the exact points; it does not make distribution-fitting training an RG
  step. It is the formal counterpart of [THEORY-194](../theory.d/THEORY-194.md), which holds the
  empirical side from [LIT-873](../literature.d/LIT-873.md).
- **[THEORY-194](../theory.d/THEORY-194.md).** This reading supports it on the point it shares with
  this paper (which objective decides) and adds the formal reason the
  fitted coarse-graining need not be the RG one: the identity is silent
  on which kernel to choose. It does not bear on [THEORY-194](../theory.d/THEORY-194.md)'s mutual
  information criterion.
- **[THEORY-036](../theory.d/THEORY-036.md) and [LIT-219](../literature.d/LIT-219.md), [LIT-150](../literature.d/LIT-150.md).** No bearing beyond what [NOTE-674](NOTE-674.md)
  says: this paper offers no criterion for which compression counts.
- **[QUESTION-025](../questions.d/QUESTION-025.md) and [THEORY-185](../theory.d/THEORY-185.md).** No bearing. The hierarchy is of spatial
  blocks; there are no attributes, co-occurrence statistics or lattices.
- **Anthology.** A theory of what deep networks learn, with no practice
  instruction; the anthology's `analysis-and-evaluation` topic, which
  takes theory, could hold it, hence `anthology-candidate` on the LIT.

## Limitations

- **The mapping is definitional.** T is defined so that Eq. 21 holds; the
  identity holds for untrained and badly trained networks alike, and T
  depends on the data Hamiltonian rather than being a fixed kernel form.
- **Eq. 8 overstates.** ΔF = 0 is equivalent to ⟨Tr_h e^T⟩_P = 1, not to
  Tr_h e^T = 1 for every v; and under Eq. 18 it reduces to Z_λ = Z (my
  derivation, above).
- **The 1D network is constructed from the known decimation**, not
  learned, and the paper does not write out its T or E to show it is an
  instance of Eqs. 18–22.
- **The 2D evidence is qualitative and single-condition.** One lattice
  size, one temperature on the paramagnetic side, no coarse couplings, no
  flow, no fixed point, no exponent; locality is encouraged by the L1
  penalty; no comparison with a known block-spin transformation beyond
  appearance.
- **Small errors.** The 2D critical coupling is given as J/k_BT = 0.4352;
  the exact value is ln(1 + √2)/2 ≈ 0.4407 (the experiment's 0.408 is on
  the paramagnetic side either way). The sample count is 20,000 in the
  text and 40,000 in Appendix A. The SI and Matlab file cited in the
  appendix are not on arXiv.
- **Never published in a journal**; arXiv v1 is the only version.

## Open questions

- When does minimizing KL with fewer hidden than visible units give an
  RG transformation, i.e. a coarse Hamiltonian that stays short-ranged and
  keeps the relevant operators? A characterization for a class of
  Hamiltonians would settle the scope of C4 and of [LIT-873](../literature.d/LIT-873.md)'s
  counterexample together.
- Does the stacked RBM of Fig. 3, run on the noisy dimer data of [LIT-873](../literature.d/LIT-873.md),
  also spend its units on the noise? That is the direct test of whether
  depth and the L1 penalty change [LIT-873](../literature.d/LIT-873.md)'s single-RBM result.
- Is there a non-trivial approximate criterion on the RG side, short of
  exactness, that the RBM parametrization preserves? Under Eq. 18 the
  free-energy criterion does not supply one.
