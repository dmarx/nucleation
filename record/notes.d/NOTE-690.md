---
number: 690
status: Read
formerly:
- NOTE-tmpbm8lu
paper: 'LIT-885'
title: 'Relevance in the Renormalization Group and in Information Theory'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read in full from the arXiv PDF of v1 (arXiv:2012.01447v1, 2 December
    2020, the only version; 16 pp.: main text pp. 1–4, references pp.
    5–6, Appendices A–F pp. 6–16), text extracted with pdftotext. Main
    text, all six appendices and the reference list read. The transfer-
    matrix reduction (Eqs. B1–B9) and the solution at the first transition
    (Eqs. C1–C11) followed step by step; the symmetry argument (Appendix
    D, Eqs. D1–D8) followed in outline, not re-derived; the Z4
    counterexample's entropies recomputed by hand and found correct
    (1.3296, 1.0986, 1.3689; 1.3296 > 1.3013). Two numbers checked
    independently by exact transfer-matrix computation for the paper's
    test system (critical 2D Ising, circumference 3, V of two slices, E of
    one, nine transfer steps between them): the squared second singular
    value of P(v,e)/√(P(v)P(e)) gives β_c = 146.34458, the paper's
    predicted value, and it equals (λ0/λ1)^18 to all printed digits; and
    over all 254 non-trivial binary partitions of E-facing boundary
    configurations, the one maximizing I(H;E) is the sign of r_v, at
    buffers of 1, 2 and 9 steps. Figures read as text only: the plots did
    not survive extraction, so their content is taken from captions and
    text. Read after LIT-878 (NOTE-681), LIT-873 (NOTE-674) and LIT-881
    (NOTE-682), to place it without repeating them. The published
    Physical Review Letters text was not read (the publisher returned HTTP
    403); it appeared six and a half months after v1, and differences
    cannot be ruled out.
date: '2026-10-09'
summary: >-
  Proves, for a short-range lattice model on a cylinder with block and
  environment as slabs separated by a buffer, that the information-
  bottleneck encoder at its first transition depends on the block only
  through the boundary weak value of the leading transfer-matrix
  eigenvector, which at large circumference is the lowest-dimension
  primary, with β_c = (λ0/λ1)^(2L_B); checked on a three-site Ising
  cylinder. It does not cover the planar block-in-a-shell geometry or
  the fixed-alphabet β → ∞ limit that RSMI uses, which [LIT-878](../literature.d/LIT-878.md) relies on.
---
<!-- inactive-ok-file: THEORY-194 THEORY-198 THEORY-197 THEORY-161 THEORY-017 THEORY-205 QUESTION-025 CLAIM-092 — Proposed or open; cited as accounts this reading underpins or is set beside, the account it produced, and the question and claim it does not answer -->

# NOTE-690: Relevance in the Renormalization Group and in Information Theory

## Contribution

The real-space mutual-information programme ([LIT-873](../literature.d/LIT-873.md), [LIT-881](../literature.d/LIT-881.md), [LIT-878](../literature.d/LIT-878.md))
chooses a block's coarse variable by what it shares with the distant
environment, and claims that the variables found are the RG-relevant
ones. Before this paper the claim rested on examples with known answers
and on 1D proofs. This paper gives the first derivation that ties the
information-theoretic optimum to RG scaling dimensions in a model that
is not one-dimensional: posing the problem as an information bottleneck
(IB) with the environment as relevance variable, it solves the IB
equations at their first transition in closed form, in terms of
transfer-matrix eigenvectors and eigenvalues, and so in terms of CFT data
when the circumference is large. It adds a result on when the optimal
encoder respects the data's symmetries.

## Key insight

Across a long buffer the joint law of block and environment is the
identity plus a sum of rank-one terms, one per transfer-matrix
eigenvector, each weighted by its eigenvalue ratio raised to the buffer
length. The IB's first transition is where the encoder first finds it
worth keeping anything, and what it keeps is the largest of those
terms: the slowest-decaying mode, which is the most relevant operator.
"Relevant in the sense of IB" is the leading singular direction of the
block–environment channel, and a transfer matrix makes that direction a
scaling operator.

## Assumptions

- **Geometry: a cylinder, with block and environment as slabs.** The
  system is an infinite cylinder of circumference L. V is a run of whole
  slices, E another, separated along the axis by L_B slices. Both span
  the full circumference; V's coupling to E passes through its single
  boundary slice ∂V_R. This is not the RSMI geometry of [LIT-873](../literature.d/LIT-873.md) and
  [LIT-878](../literature.d/LIT-878.md), in which a square block sits inside a buffer shell inside an
  environment shell.
- **Short-range interactions and a real symmetric transfer matrix**, so
  that left and right eigenvectors coincide, P(∂V_R) = ⟨0|∂V_R⟩², and the
  r's are orthonormal under P. Not stated as an assumption, but used
  (Eq. B6 and the claim ⟨r²⟩ = 1).
- **A single most relevant operator**: ∆₂ > ∆₁ > 0, λ1 non-degenerate.
  Degenerate leading operators, such as the dimer model's pairs, are left
  to the symmetry appendix.
- **Large buffer**: terms of order (λ2/λ0)^(L_B) are dropped to reduce
  the IB equations to one variable (Eq. B9). The authors also write the
  condition as L_B ≫ L.
- **Near the first IB transition**: β = β_c,1 + t, small t, and for the
  closed form |H| = 2 with P(h) uniform.
- **For the CFT reading only**: L → ∞ with L_B/L → ∞, so that λ_i/λ_0 →
  exp(−2π∆_i/L) (Cardy). The authors stress that the transfer-matrix
  result does not need a CFT.
- **For the symmetry result** (Eq. D1): β < β_c,2; |H| large enough that
  one more symbol does not lower the IB Lagrangian; a second-order first
  transition; the crossing eigenvectors form an irreducible
  representation (no fine-tuning).

## Key results

- **Reduction** (Eqs. 3, B2–B5). With ε = (λ1/λ0)^(L_B),
  P(v|e) = P(v)[1 + ε r_v r_e] + O((λ2/λ0)^(L_B)),
  r_v = ⟨1|∂V_R⟩/⟨0|∂V_R⟩, r_e = ⟨∂E_L|1⟩/⟨∂E_L|0⟩; ⟨r_v⟩ = ⟨r_e⟩ = 0,
  ⟨r_v²⟩ = ⟨r_e²⟩ = 1. *Holds when:* the slab geometry above.
- **Reduced IB equation** (Eqs. 4, B9). To first order in ε,
  P(h|v) = P(h|r_v) ∝ P(h) exp(β ε² r_v ⟨r_v⟩_h). The encoder sees V only
  through r_v, and only through ∂V_R.
- **First transition** (Eqs. 5, C4–C5). β_c,1⁻¹ = ε² + o(ε²) →
  exp(−4π∆₁L_B/L) as L → ∞.
- **Encoder just above it** (Eqs. C6–C11). For h = ±1,
  P(h|r_v) = e^(h m r_v)/2cosh(m r_v), m = √(3(β − β_c)/(⟨r⁴⟩β_c)).
- **Numerical check** (Fig. 3, Appendix F). Critical 2D Ising, L = 3,
  |V| = 2 × 3, |E| = 1 × 3, L_B = 9, joint law computed exactly by the
  transfer matrix; iterative IB (forward and backward β scans to escape
  the saddle) gives 146.33999 < β_c < 146.34999 against 146.34458, and
  the encoder matches Eq. C6.
- **Symmetry** (Eqs. 6, D1–D8). Under the assumptions above, the optimal
  encoder satisfies P_β(h|v) = P_β(φ_s h|sv) for a permutation
  representation φ of S, possibly trivial; by continuity up to β_c,2.
  With |H| smaller than the needed representation it can fail: V = E =
  Z4, P(e|v) uniform on {v, v+1, v+2}, |H| = 2, β → ∞, the optimal
  partition {0}|{1,2,3} breaks Z4 (conditional entropy 1.3013 against
  1.3296 for both symmetric partitions); numerically, down to β_c,1.
- **RSMI as a limit** (main text p. 4). RSMI is "a β → ∞ limit of IB
  under the constraint of fixed |H|". Asserted, not analysed.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | In the slab geometry the block–environment law reduces to the boundary weak values of the leading transfer-matrix eigenvector, up to terms in (λ2/λ0)^(L_B) | strong | derivation, Eqs. B2–B6; exact, in fact (see Bearing) |
| C2 | Near the first IB transition the optimal encoder depends on V only through r_v, with β_c,1⁻¹ = ε² | strong in its setting | Eqs. B9, C1–C5; reproduced numerically, here and by the authors |
| C3 | At large circumference r_v is the most relevant (lowest-∆) primary, so IB relevance and RG relevance coincide | strong for the slab geometry and first transition; the general "equivalence" in the abstract is broader than this | Cardy's finite-size relation, cited |
| C4 | The closed-form encoder just above β_c,1 is a tanh of m r_v with m ∝ √(β − β_c) | moderate | perturbative expansion to third order (C10–C11); Fig. 3 agreement on one tiny system |
| C5 | RSMI is the β → ∞, fixed-|H| limit of IB, so the theorem underwrites RSMI | weak | asserted in one paragraph; the theorem is for the first transition, not β → ∞ |
| C6 | With a large enough alphabet and no fine-tuning, the IB encoder near β_c,1 carries a representation of the data's symmetry | moderate | Appendix D argument after Gedeon, Parker and Dimitrov; extension to all β conjectured |
| C7 | With too small an alphabet the encoder can break the symmetry | strong (by example) | Z4 example, checked by hand |
| C8 | The IB route can extract unknown symmetries and automate Ginzburg–Landau descriptions | weak | programme; a procedure sketched in Appendix E on a toy split-spin Ising model |

## Method

Write every distribution entering the IB equations (Tishby, Pereira and
Bialek's self-consistent equations, [LIT-338](../literature.d/LIT-338.md)) as matrix elements of powers
of the transfer matrix, eigendecompose T, and keep the leading term in
the buffer length. Linearize the reduced equation around the uniform
encoder to find where it loses stability, and expand to third order to
get the encoder above it. For symmetry, follow Parker, Gedeon and
Dimitrov's bifurcation analysis of the IB Hessian: its block structure
across symbols, the kernel at the transition, and the action of the
symmetry on the crossing eigenvectors.

## Concepts

- **relevance (IB)**: information a compression H of V keeps about the
  chosen relevance variable E; here E is the environment beyond a buffer.
- **relevance (RG)**: the ordering of operators by scaling dimension; the
  most relevant has the lowest ∆.
- **weak value r_v**: ⟨0|φ_∆₁|∂V_R⟩/⟨0|∂V_R⟩, the ratio of the leading
  excited to the ground transfer-matrix eigenvector on V's boundary
  slice. The paper says that for Ising it "is the overall magnetization on
  ∂V"; it is an odd, monotone function of it, not proportional (see
  Bearing).
- **IB transitions**: values of β where the optimal encoder changes
  non-analytically; each resolves one more feature by breaking the
  permutation symmetry among symbols.
- **gauge fixing**: the convention that symbols with proportional
  conditionals are made identical, so that the encoder below β_c,1 is
  uniform.

## Connections

It is the theoretical step between Koch-Janusz and Ringel's RSMI
principle ([LIT-873](../literature.d/LIT-873.md)) and its neural estimator ([LIT-878](../literature.d/LIT-878.md), cited here as in
preparation), beside Lenggenhager et al.'s factorization theorem
([LIT-881](../literature.d/LIT-881.md)). Its IB is Tishby, Pereira and Bialek's ([LIT-338](../literature.d/LIT-338.md), whose [NOTE-300](NOTE-300.md)
records that the IB phase transitions are cited out, not shown, there);
the transition analysis is Parker, Gedeon and Dimitrov's; the CFT
dictionary is Cardy's. It places itself among information-theoretic
readings of RG irreversibility (Zamolodchikov's c-theorem, Casini–Huerta,
Apenko, Machta et al., Bény and Osborne), none of them held here.

## Bearing on the record

- **[LIT-878](../literature.d/LIT-878.md) and [NOTE-681](NOTE-681.md): does the cited theorem hold?** In its own
  setting, yes, and more exactly than stated. In the slab geometry the
  Markov property along the cylinder makes P(v, e) = P(v)P(e) Σ_i ε_i
  r_v^(i) r_e^(i) exact, with ε_i = (λ_i/λ0)^(L_B) and the r^(i)
  orthonormal under P. The normalized channel's singular values are then
  exactly the ε_i, so the first transition is at β_c = (λ0/λ1)^(2L_B)
  with no o(ε²) correction, and the critical direction is exactly r_v.
  The paper's test value is reproduced this way to every printed digit
  (history). What [LIT-878](../literature.d/LIT-878.md) needs is more than that. Its filters live on a
  planar 8 × 8 block inside a buffer shell; its objective is RSMI at
  fixed |H|, not the IB near β_c,1; and its leading operators are
  degenerate pairs. None of these is the theorem's setting. "Proven in
  part" ([LIT-878](../literature.d/LIT-878.md)'s words) is accurate, and the part is the slab geometry
  at the first transition.
- **Closing part of the gap (my argument, not the paper's).** In the slab
  geometry the RSMI case follows at leading order. For a deterministic
  encoder, P(e|h) = P(e)[1 + Σ_i ε_i r_e^(i) ⟨r^(i)⟩_h], so
  I(H;E) = ½ Σ_i ε_i² Σ_h P(h)⟨r^(i)⟩_h² + O(ε³): to leading order RSMI
  maximizes the between-class variance of r_v, whose optimum over
  partitions of a scalar is a set of intervals in r_v (thresholds), with
  subleading operators entering only at order ε_2². The exhaustive check
  in the history found the sign of r_v optimal at every buffer tried, but
  at circumference 3 that is also the sign of the magnetization, so the
  check is weak. For the planar geometry, a CFT on an annulus maps
  conformally to a finite cylinder, which suggests the same structure
  with ε set by a ratio of radii; the paper does not argue this, and on a
  lattice block of eight sites the map is not exact. That is open.
- **Off criticality.** [NOTE-681](NOTE-681.md) asked what the formal status of the
  optimal filters is away from criticality. The transfer-matrix part of
  the theorem does not use criticality: at the first transition the
  encoder follows the leading excited eigenvector at any temperature. Only
  its reading as a scaling operator needs the critical point.
- **The magnetization remark.** For the paper's L = 3 Ising cylinder,
  r_v on the boundary slice takes the values ±1.086 at |m| = 3 and
  ±0.449 at |m| = 1, a ratio of 2.42, not 3; its P-weighted correlation
  with the magnetization is 0.999 at L = 3 and 0.994 at L = 9, while the
  transfer matrix's ∆₁ tends to 1/8. The sign agrees, so any binary
  threshold encoder is the same; the soft encoder of Eq. C6 is not
  exactly a function of the magnetization.
- **[THEORY-194](../theory.d/THEORY-194.md).** Its source list cites [LIT-873](../literature.d/LIT-873.md), [LIT-881](../literature.d/LIT-881.md) and [LIT-878](../literature.d/LIT-878.md) for
  the empirical claim, and its `promote_when` asks, among other things,
  for a proof for a class of local Hamiltonians in two or more
  dimensions. This paper is a proof about relevant operators, not about
  short-ranged effective Hamiltonians, and for slabs of a cylinder, not
  for blocks, so it does not meet that clause. It is the formal
  counterpart of [THEORY-194](../theory.d/THEORY-194.md)'s operator claim, filed as [THEORY-205](../theory.d/THEORY-205.md).
- **[THEORY-198](../theory.d/THEORY-198.md).** Different statement: [LIT-881](../literature.d/LIT-881.md) proves that full capture
  of the block's information keeps the Hamiltonian short-ranged; this
  paper says which single feature a minimal capture takes. They do not
  conflict, and neither implies the other.
- **[THEORY-197](../theory.d/THEORY-197.md).** Consistent: what a compression keeps is fixed by the
  relevance variable, not by fitting P(v); nothing here bears on the RBM
  identity.
- **[THEORY-161](../theory.d/THEORY-161.md) and [CLAIM-092](../claims.d/CLAIM-092.md).** Both pose meaning or translation as an
  information bottleneck. This paper is a fully worked case where the IB's
  first feature is the leading singular direction of the source–relevance
  channel, and where too small an alphabet breaks a symmetry of the data.
  That is an analogy for [CLAIM-092](../claims.d/CLAIM-092.md)'s context-indexed bottleneck, not
  evidence for it. My connection.
- **[THEORY-017](../theory.d/THEORY-017.md) and [QUESTION-025](../questions.d/QUESTION-025.md).** As in [NOTE-681](NOTE-681.md): the partition into
  block, buffer and environment is given before anything is learned, and
  with a degenerate leading operator the IB fixes a subspace and leaves
  the basis to symmetry (Appendix D's representation φ). No attributes,
  no co-occurrence matrix, no concept lattice: no direct bearing on
  [QUESTION-025](../questions.d/QUESTION-025.md).
- **Anthology.** No practice instruction; not an anthology candidate (see
  the LIT).

## Limitations

- **The abstract's "equivalence" is wider than the proof.** It says the
  two notions "are in fact equivalent in physical systems"; what is shown
  is that the first IB feature in the slab geometry is the leading
  transfer-matrix mode.
- **One transition.** Nothing is derived beyond β_c,1; whether later
  transitions add the next operators in order of dimension is implied by
  the corrections' ordering but not shown.
- **One tiny numerical test**, on a cylinder of circumference 3, where the
  CFT identification is not at stake.
- **Asserted links**: RSMI as a limit of IB; the Gaussian field theory's
  whole IB curve (cited to work in preparation); the symmetry result at
  all β (a conjecture).
- **Text inconsistencies.** Appendix C says Monte Carlo samples were fed
  to the IB solver; Appendix F says P(E, V) was computed exactly. The
  condition "the buffer to be much larger than ratio ∆₁/L" in Appendix B
  is garbled; elsewhere it is L_B ≫ L.

## Open questions

- Does the result hold for a block surrounded by a buffer shell, the
  geometry the algorithms use? A derivation via radial quantization, or
  an exact computation for a small planar block, would settle it.
- Do later IB transitions resolve operators in order of scaling
  dimension? A numerical IB scan on a cylinder with a known spectrum,
  through the second transition, would show it.
- With a degenerate leading operator (O(2), the dimer charges), which
  basis does a finite alphabet pick, and does it break the symmetry, as
  the Z4 example does?
