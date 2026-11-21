# Reader notes: LIT-tmp7sbn6, Dambre, Verstraeten, Schrauwen & Massar (2012)

## Copies located (2026-11-21)

1. https://www.nature.com/articles/srep00514 — publisher's open-access HTML
   (Scientific Reports, CC BY-NC-SA 3.0). Fetched, HTTP 200, no challenge.
   Used for the equation images only.
2. https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3400147/fullTextXML —
   Europe PMC full-text XML (PMC3400147, PMID 22816038, open access), the
   repository's documented API (ADR-101). Fetched, HTTP 200. Read in full;
   its equations are images, so the key ones were read from 3.
3. https://media.springernature.com/full/springer-static/image/art%3A10.1038%2Fsrep00514/MediaObjects/41598_2012_Article_BFsrep00514_Equ{2..10}_HTML.jpg
   — publisher's equation images (eqs 2–8, 10). Fetched, 200.
4. https://static-content.springer.com/esm/art%3A10.1038%2Fsrep00514/MediaObjects/41598_2012_BFsrep00514_MOESM1_ESM.pdf
   — the publisher's Supplementary Information (8 pp., dated 28 June 2012).
   Fetched, 200; read in full (proofs, centred definition, estimation).

No bot check, paywall or refusal met. Status should be read, not Unfetched
or Unavailable. Route for the text: Europe PMC's REST API (ADR-101); the
publisher's page and supplement were open too. No email address was sent.

## Provenance

Read: the whole main text (Introduction, Results, Discussion, figure
captions 1–4, the reference list where cited) from the Europe PMC XML;
eqs 4, 8 and 10 from the publisher's images; the Supplementary
Information in full (§1 proofs, §2 centred capacities, §3 estimation,
§3.4 the reaction-diffusion system). Skipped: the figures themselves
(captions only), eqs 11–17 (system equations, not needed), the Methods
details beyond what the text gives.

## Summary

For a dynamical system driven by i.i.d. input u(t) and observed through N
state variables x_i(t), the capacity to reconstruct a function z of past
inputs with a linear readout (no bias) is C[X,z] = 1 − min MSE/⟨z²⟩, the
squared cosine between z and its projection on the span of the x_i
(Def. 1; SI eq. 1.10). Capacities for orthogonal functions measure
independent things, and summed over any finite orthogonal set they are at
most N (Theorem 4). If the system has fading memory and its N variables
are linearly independent, the sum over a complete orthonormal basis of the
Hilbert space of fading-memory functions equals N (Theorem 7). Simulations
of a driven logistic map, a 50-node echo state network and a 2-D
Gray-Scott reaction-diffusion system (Legendre-product basis, uniform
input on [−1,1], T = 10⁶) show the total near N up to the undriven
system's edge of stability, a trade-off between linear memory and
nonlinearity as input scaling ι (or sampling period T_S) grows, and a loss
of usable capacity when unknown noise is a second input.

## Contribution

A normalized, implementation-independent measure of all the computation
(linear and nonlinear, short and long memory) a driven system does with a
linear readout, and the theorem that the total is fixed by the number of
independent observed variables. It generalizes Jaeger's (2002) linear
memory capacity (ref. 12) to a complete function basis.

## Key results

1. **Normalization** (Prop. 3): "the capacity is normalized according to:
   0 ≤ C_T[X,z] ≤ 1 … C_T = 1 if perfect reconstruction of z is possible".
2. **The bound** (Theorem 4, eq. 8): for orthogonal y_l with finite fourth
   moment, "in the limit of an infinite data set T → ∞, the sum of the
   capacities for these functions is bounded by the number N of output
   functions (independently of h, of the set Y_L, or of its size)". It
   needs neither fading memory nor linear independence; SI fn. 1: Prop. 3
   holds "also for dynamical systems that are not fading memory".
3. **Equality** (Theorem 7, eq. 10): with fading memory (Def. 6, after
   Boyd & Chua 1985), rank-N correlation matrix, finite fourth moments,
   T, T′ → ∞ and Y_L tending to a complete orthogonal set, the sum "tends
   towards the number N of output functions". Abstract: "bounded by the
   number of linearly independent state variables … equaling it if the
   system obeys the fading memory condition."
4. **Universality** (Introduction): "all dynamical systems, provided they
   obey the condition of having a fading memory and have linearly
   independent internal variables, have in principle the same total
   normalized capacity to process information." Discussion: "information
   is not lost inside these networks but merely transformed in various
   non-linear ways."
5. **Total capacity against the edge** (Fig. 1, "Total capacity"): "For
   very small input scaling, the capacity C_TOT remains close to N up to
   the bifurcation point of the undriven system and then drops off
   rapidly. As the input scaling increases, the loss of capacity becomes
   less abrupt, but its onset shifts to lower values." The drop below N
   is attributed partly to truncation (strongly nonlinear responses not
   captured by the polynomials kept) and partly to loss of fading memory.
6. **Memory–nonlinearity trade-off** (Fig. 3): "on one end of the scale
   they store the information but then are linear, while on the other end
   they immediately process the input in a highly non-linear way, but
   then have small linear memory." The parameter swept is input scaling ι
   (ESN at ρ = 0.95, logistic map at ρ = 2.5) and T_S, not distance from
   the edge.
7. **Noise** (§"Influence of noise"): noise is a second i.i.d. input v;
   "It is only over the full space that Theorem 7 holds and that the
   capacities will sum to N. However since v is unknown, the capacities
   which are measurable are those which depend only on u … these
   capacities will not sum to N." Usable capacity falls with lower SNR and
   with more nonlinearity (Fig. 4 left). Fig. 4 right: with K equal-power
   inputs, "for a strictly linear system … the capacity for a single input
   should equal N/K". SI §3.1 item 2: noise sources "can be thought of as
   additional inputs".
8. **Finite data** (SI §3.2): small capacities are overestimated by
   O(N/T); capacities below a χ²-based threshold are set to zero.
9. **Bias term** (SI §2): a centred version C′ (covariances) satisfies the
   same bound and equality (Corollaries 13, 14).

## Assumptions

i.i.d. stationary input from a fixed p(u) with separable L²(p); linear
readout of N observed variables, no bias (or the centred variant);
infinite data and washout; finite fourth moments; for equality, fading
memory (state a limit of functions of finitely many past inputs,
independent of initial condition) and full-rank state correlation; the
sum runs over a complete basis of functions of ALL inputs, noise included.
The paper says non-i.i.d. inputs make the basis "often not feasible" and
the bound "largely a theoretical insight" there (Discussion).

## Concepts

Capacity C[X,z]; Hilbert space of fading-memory functions; fading-memory
dynamical system; linear memory capacity L[C] and nonlinearity NL[C] as
summaries of the normalized capacity profile; Legendre-product basis;
noise as an unobserved input; relation to Wiener-series system modeling
(sum of capacities = how well a finite basis models the system).

## Verdict on the exchange's characterization

A15 §3 (as quoted in CLAIM-tmpask80): "under specified conditions, a
reservoir's total information-processing capacity is bounded by its
number of independent state variables. Different dynamical regimes can
redistribute that capacity between linear memory and nonlinear
transformations." **Accurate**, with three refinements. (a) The bound
(Thm 4) holds without fading memory; fading memory and linear
independence are the conditions for EQUALITY (Thm 7), and the quantity is
the number of observed variables N. The record's phrasing "bounded …
under fading memory" (brief; ARG-tmpubyzo "conditions (fading memory,
i.i.d. input)") runs the two together: bound needs i.i.d. input, finite
fourth moments, T → ∞; equality adds fading memory, rank N, a complete
basis, and that the basis covers every input including noise. (b) The
"regimes" that redistribute capacity in the paper are input scaling ι and
sampling period T_S, at fixed ρ near the edge; the paper does not report
the allocation as a function of distance from the edge. (c) Linear
readout is built into the measure; the paper's point is that the
reservoir itself does the nonlinear work.

The paper does not discuss criticality as a theme. Its one remark on the
edge is a Fig. 2 caption choosing ρ "close to the edge of stability, a
region in which the most useful processing often occurs", citing Langton
(1990), ref. 27: an assumption carried in, not a result.

## Bearing on the named codes

- **CLAIM-tmpd1shn** — **supports; the claim's main result is a case of
  Theorem 7 with the paper's noise model.** The scalar reservoir with
  |a| < 1 has fading memory and N = 1. Treat η as the paper's second
  input v: x lies in the span of the degree-1 functions u(t−1−k) and
  η(t−1−k), so over the full u⊗η basis the capacities sum to 1 at every
  a (Thm 7), the u-functions take s²/(s²+σ²) and the η-functions
  σ²/(s²+σ²). Independence from a is then immediate: the theorem's
  conditions hold throughout |a| < 1. At σ² = s² the u-share is 1/2 = N/K
  with K = 2, the paper's own linear benchmark (Fig. 4 right caption).
  The claim's "scalar case of the bound" is right but understates it: it
  is the equality case, not just the bound. Two details to align: the
  paper's capacity has no bias term (SI §2 gives the centred variant);
  with zero-mean u and η they coincide, so nothing changes. Gaussian u is
  within the theory (the paper names Hermite bases as an alternative). The
  readout-noise result s²/(s²+σ²+ρ(1−a²)) is not in the paper; it is
  consistent with it if ν is treated as a third i.i.d. input that enters
  only the observation (x+ν is then still a fading-memory function of the
  inputs, with total capacity 1 over the full basis). Nothing in the paper
  contradicts the lag-allocation optimum a² = k/(k+1); the paper has no
  such calculation.
- **CLAIM-tmpask80** — **supports strand 2, qualifies the thesis.**
  Supports "total capacity is bounded by the number of independent state
  variables" (Thm 4/7) and "different regimes redistribute it between
  linear memory and nonlinear transformations" (Fig. 3). Qualifies: (i)
  the paper shows total capacity CONSTANT (= N) throughout the
  fading-memory regime and FALLING past the edge (Fig. 1), so for this
  measure nearness to the edge cannot raise capacity and crossing it
  loses capacity — stronger than "does not raise every ability"; (ii) it
  does not show the allocation moving with distance from the transition,
  which strand 2 is used for; (iii) the edge here is the undriven
  system's loss of linear stability (ρ = 1 for the ESN, ρ = 3 for the
  logistic map), marginal stability, not a collective critical point, as
  CLAIM-tmpask80 already says of the scalar model. The defeated_if clause
  "a showing that the information-processing capacity of a reservoir with
  fading memory is not bounded by its number of independent state
  variables" is safe: Thm 4 bounds it for any system.
- **ARG-tmpubyzo** — **supports, and narrows its stated gap.** "What it
  does not show: Not the generality … That rests on Dambre and colleagues'
  bound … whose conditions (fading memory, i.i.d. input) the record has
  not checked." Checked: the generality holds for the TOTAL (every
  fading-memory system with N independent variables has total N, so
  "raises nothing in total" is general within that regime), not for how
  the allocation moves with distance from the edge, which the paper does
  not study. The scalar case is an instance of the theorem, not merely
  analogous. Conditions to state: i.i.d. input; linear readout; infinite
  data; fading memory and rank N for equality; noise counted as input.
- **QUESTION-tmp2hhlc** — **answers the first part, leaves the rest
  open.** "What would answer it … a capacity measure, its bound, and how
  the bound's allocation moves with distance from the transition."
  Measure and bound: given, for i.i.d.-driven systems with linear
  readout. Allocation against distance from the transition: not given
  (the paper sweeps ι and T_S at fixed ρ). Point 3 (environment): the
  paper's measure deliberately uses i.i.d. input "so that any measured
  structure will be due to the dynamical system itself", so it cannot
  speak to the value of multiscale memory for a correlated environment.
  Point 1 (which transition): the paper's edge is a stability edge of a
  deterministic map, not branching criticality.

## Limitations

Theory only for i.i.d. input; capacity only with a linear readout;
asymptotic in T and T′; equality needs a complete basis, never reached
numerically, so C_TOT is a lower estimate truncated by threshold and by
polynomial degree (≤ 9); the drop past the edge in Fig. 1 mixes loss of
fading memory with truncation, which the paper does not separate; a
single ESN instance; no study of allocation against ρ; no treatment of
readout (observation) noise apart from noise-as-input; "capacity" weights
all orthogonal functions equally, so equal totals say nothing about
usefulness for a given task (the paper: "Some systems may carry out more
interesting computations than others").

## Candidate THEORY

Dambre and colleagues show that for a dynamical system driven by i.i.d.
input and read out linearly from N observed variables, the capacities to
reconstruct orthogonal functions of past inputs sum to at most N, and to
exactly N over a complete basis when the system has fading memory and its
N variables are linearly independent, so that such systems differ in how
they divide a fixed capacity among linear memory and nonlinear
computation, not in its total; unobserved noise, counted as a further
input, takes part of that total.

promote_when: the theorems (Theorem 4 and Theorem 7 with Supplementary
§1.4 and §1.6) are confirmed as stated, with their conditions, by a
second reading of the proofs or by an independent derivation or textbook
restatement of the result.

## Recheck (search of record/ after reading)

Terms searched: memory capacity, fading memory, echo state, reservoir
computing, Jaeger, Volterra, Wiener series, Ganguli, Langton, edge of
chaos, edge of stability, Legendre, Hermite, liquid state, Maass,
information processing capacity, short-term memory.

- **THEORY-1431** (origami reservoir, NOTE-1600, LIT-2026), already named
  in CLAIM-tmpask80's grounds: a physical reservoir with a trained linear
  readout. Parallel: the paper's measure would apply to it; the record
  has no capacity figure for it.
- **NOTE-1907 / LIT-2553** (Andrieu et al., provable state estimation
  with recurrent models), not found by the first search: discusses
  contraction and the echo state property, the condition that gives
  fading memory. Background for the equality condition.
- **CLAIM-tmpyy261** (chaos, criticality and scale cascades are distinct),
  not named in the citing entries: bears on QUESTION-tmp2hhlc point 1;
  the paper's edge is a stability edge, a third thing again.
- **NOTE-1988 / LIT-2642** (linear transformers as fast weight
  programmers, memory capacity bounded by dimension): parallel —
  another capacity bounded by state dimension; contrast in that its
  memory is written, not driven.
- **Ganguli, Huh & Sompolinsky (2008), "Memory traces in dynamical
  systems"**, ref. 15 of the paper: many Ganguli hits in record/ (e.g.
  LIT-862, LIT-864, LIT-877) but none for this PNAS paper — not held.
  Jaeger (2002) GMD report 152 (the linear memory capacity bound of
  which CLAIM-tmpd1shn's is the scalar case) — not held. White, Lee &
  Sompolinsky (2004) — not held. Boyd & Chua (1985) — not held.
- Edge-of-chaos hits (THEORY-2041, THEORY-2051, LIT-tmpkvpg4) are already
  cited by QUESTION-tmp2hhlc. "Edge of stability" hits (THEORY-184,
  LIT-861) are gradient-descent step-size results, unrelated.

## Neighbours

Not needed; the work itself was read. Supplement read: the paper's own
Supplementary Information (publisher's ESM, address 4 above), quoted
above (SI fn. 1, §2, §3.1, §3.2). It is part of the article, not a
separate work, so no separate LIT should be needed; the filer may decide
otherwise under ADR-114.
