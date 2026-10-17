---
status: Read
paper: 'LIT-tmps1x9k'
title: 'Lizier, Prokopenko and Zomaya — Local information transfer as a spatiotemporal filter'
version: 1
history:
- version: 1
  date: '2026-10-16'
  note: >-
    Read in full from arXiv 0809.3275v1 (19 Sep 2008), 12 pp., extracted
    with pdftotext: §§I–V, figure captions, references. Figures read from
    captions and prose; the plotted profiles were not seen. I checked the
    three worked local values against their stated probabilities, and
    rule 18's update table for the apparent/complete contrast. I did not
    compare the PRE version (Phys. Rev. E 77, 026110), which Crossref dates
    15 February 2008, before this arXiv posting.
date: '2026-10-16'
summary: >-
  Transfer entropy is the expectation of a local transfer entropy,
  t_{Y→X}(n+1, k, l) = log p(x_{n+1} | x⁽ᵏ⁾_n, y⁽ˡ⁾_n)/p(x_{n+1} | x⁽ᵏ⁾_n),
  defined at every point and possibly negative. Apparent transfer entropy
  conditions on the destination's past; complete transfer entropy also
  on its other causal parents. On elementary cellular automata, with
  k ≥ 6 (rule 110) and k = 16, local transfer entropy highlights gliders
  and domain walls as the dominant information-transfer structures; k = 1
  and local time-lagged mutual information do not. The averages carry
  none of this.
---

# NOTE-tmpr3ktj: Lizier, Prokopenko and Zomaya — Local information transfer as a spatiotemporal filter

## Contribution

Before this paper, transfer entropy was an average over a channel, and
the conjecture that particles in cellular automata carry information was
qualitative. After it, transfer entropy has a pointwise form that profiles
transfer into every spatiotemporal point, two named variants, apparent and
complete, and quantitative support for the particle conjecture in four
elementary CAs.

## Key insight

Any average of a log ratio is the mean of the log ratio at each
observation (Eqs. 6–9). The local value says, at one point, how much more
(or less) probable the destination's actual next state became once the
source was taken into account, given the destination's past.

## Assumptions

- **Stationary or homogeneous probabilities.** For CAs the distributions are
  pooled over every cell and time of a channel (§IV), 10 000 cells and 600
  steps after 30 transient steps, confirmed over at least 10 runs.
- **Plug-in estimates** of discrete probabilities. k is limited by sample
  size (§IV E).
- **The causal parents are known** for complete transfer entropy: in an ECA,
  the destination's neighbourhood (Eq. 13). "Complete transfer entropy can be
  constructed for any system by conditioning out all causal information
  contributors", which presupposes knowing them.
- **l = 1**, the source's single previous state, throughout the results.
- **Deterministic dynamics** for the nonnegativity of complete TE.

## Key results

- **Eq. 9** — T_{Y→X} = ⟨t_{Y→X}(n + 1, k, l)⟩. The same construction gives
  a local time-lagged mutual information (Eq. 10).
- **Eq. 12** — t(i, j, n + 1, l) = lim_{k→∞} t(i, j, n + 1, k, l). Finite k
  can attribute the destination's own past, routed through the source, to
  the source.
- **Eq. 14** — complete local TE tc conditions on the rest of the
  neighbourhood v_{i,j,n}. In deterministic systems tc ≥ 0. Its average
  can only fall with k; the apparent average can rise (Fig. 7).
- **Periodic domains** — for a temporally periodic domain of period p,
  k ≥ p − 1 suffices to give zero transfer there (§IV B). With gliders
  present no finite k is sufficient.
- **Rule 110** — with k = 1, neither local MI nor local TE separates
  gliders from the background (Fig. 2). With k = 6 both metrics highlight
  gliders in their direction of motion (Fig. 3); with k = 16, mostly the
  gliders' leading edges, and not the stationary "vertical" glider (Fig. 5).
  Small nonzero transfer persists in the domain, signalling that no glider
  is coming.
- **Worked values (Fig. 4).** tc = 4.7 bits where p = 1.0 against 0.038;
  0.057 bits in the domain where p = 1.0 against 0.96; apparent t = −2.05
  bits orthogonal to a glider where p = 0.038 against 0.16. *Checked:*
  log₂(1/0.038) = 4.72, log₂(1/0.96) = 0.059, log₂(0.038/0.16) = −2.07; the
  small differences are rounding in the quoted probabilities.
- **Rule 18** — domain walls highlighted, a single cell wide (Fig. 6). In
  the domain, complete TE is about 1 bit (0.96 to 1.04 by inspection) at
  alternate sites from both channels, where apparent TE is 0. *Checked:*
  rule 18 with centre cell 0 maps (L, R) to L ⊕ R, so either neighbour
  alone carries nothing about the next state and the two together
  determine it.
- **Rules 54, 146, 22** — gliders (54) and domain walls (146) confirmed;
  rule 22 shows transfer at many points with no coherent structure.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Transfer entropy is the average of a local transfer entropy, which can be negative | strong | Eqs. 6–9; an identity |
| C2 | The destination history should be k → ∞; small k misattributes self-influence to the source | moderate | §III B argument; Figs. 2, 3, 5, 7 |
| C3 | Gliders and domain walls are the dominant information-transfer agents in ECAs | moderate | rules 110, 54, 18, 146, by inspection of profiles |
| C4 | Apparent and complete TE can differ sharply, e.g. 0 against 1 bit in rule 18's domain | strong | §IV D; checked against the rule table |
| C5 | Local TE gives insight the averages cannot | moderate | Fig. 7 against Figs. 3–6 |
| C6 | The result "completes the establishment of transfer entropy as the appropriate measure for (predictive) information transfer" | weak | §V; a conclusion from one model class, later disputed ([LIT-tmpa6og3](../literature.d/LIT-tmpa6og3.md)) |

## Method

1. Pool every cell and time step of a channel j and estimate
   p(x_{i,n+1} | x⁽ᵏ⁾_{i,n}, x_{i−j,n}) and p(x_{i,n+1} | x⁽ᵏ⁾_{i,n}) by counting,
   with v_{i,j,n} added to both for the complete form.
2. Evaluate the log ratio at every point (Eqs. 11, 14).
3. Sum over channels j = −r…r for the summed profile (Eq. 15).

## Concepts

- **Local transfer entropy** — the log ratio at one observation (Eq. 9b).
- **Apparent transfer entropy** — conditioned only on the destination's
  past (Eq. 12).
- **Complete transfer entropy** — conditioned also on the destination's other
  causal information contributors (Eq. 14).
- **Non-traveling information** — the destination's own past influencing it
  through the source, "the trivial part of information transfer".
- **Self-information transfer** — j = 0, the destination's immediate past,
  conditioned on its earlier k values.

## Connections

- **Builds on** Schreiber (2000, [LIT-tmpz9o5z](../literature.d/LIT-tmpz9o5z.md)) for the measure and its k
  and l, and computational mechanics for domains and particles. It names
  Ay and Polani's perturbation-based information flow ([LIT-tmpq33qh](../literature.d/LIT-tmpq33qh.md)) as
  the causal alternative to compare against in future work.
- **[NOTE-788](NOTE-788.md)** defines TE_{x→y}(τ) = I(y_{t+τ}; x_t | y_t), a single
  destination value. By this paper that is the k = 1 setting that failed
  to find any structure in rule 110. Whether k = 1 suffices for an
  overdamped colloid pair, whose dynamics is close to first-order Markov,
  is a different question; the paper does not address continuous
  systems. My reading.
- **Synergy ([LIT-tmpa6og3](../literature.d/LIT-tmpa6og3.md), [LIT-tmpsbhb4](../literature.d/LIT-tmpsbhb4.md)).** Rule 18's domain is XOR. Apparent TE
  misses what the two neighbours determine jointly; complete TE assigns
  it in full to each source in turn, 1 bit from each channel, so the
  summed complete profile counts the same bit twice. That is the
  double-counting James, Barnett and Crutchfield attribute to conditioning
  on other sources. My inference from the rule table; the paper reads the
  contrast as a difference between complex and chaotic dynamics.
- **[THEORY-275](../theory.d/THEORY-275.md)** reads directional measures in a driven colloid pair. Local
  TE would show where in time the drive's information enters; [NOTE-788](NOTE-788.md)
  reports averages only.

## Bearing on the record

- Filed as [THEORY-tmp22xor](../theory.d/THEORY-tmp22xor.md).
- [TERM-tmpj9z04](../terms.d/TERM-tmpj9z04.md) should state the history length k and l, the
  apparent/complete distinction, and that the average is over a local
  quantity that can be negative.
- [CLAIM-tmpu9ivq](../claims.d/CLAIM-tmpu9ivq.md) can cite rule 18's domain as a worked case: TE conditioned
  on the destination alone reports 0, conditioned on the other parent
  reports 1 bit from each source, and neither number is a flow from one
  source.
- **For the Anthology of the SOTA:** no instruction for ML practice.

## Limitations

- All evidence is elementary CAs: binary, deterministic, with known causal
  parents and huge homogeneous samples. "Ready to be applied beyond CAs" is
  asserted.
- Profiles are judged by eye against expectations and other filters; no
  quantitative criterion of "highlighting".
- No significance testing of local values.
- k is limited by sample size and no limit is reached by k = 16 (Fig. 7),
  so the k → ∞ prescription is never met.
- Complete TE needs the causal parents, which outside a model are what one
  usually wants to learn.
- The closing claim that transfer entropy is established as the measure of
  information transfer is stronger than the evidence, and the paper itself
  notes that non-causal sources can make correlation look like transfer.

## Open questions

- Comparison with Ay and Polani's information flow, locally (the authors').
- Local measures of storage and modification (the authors', [39]).
- A criterion for k in stochastic, continuous systems.
