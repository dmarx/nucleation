---
number: 756
status: Read
formerly:
- NOTE-tmp0o608
paper: LIT-953
title: 'Varley — Flickering Emergences'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from the PubMed Central copy (PMC9858457, CC BY), fetched
    as JATS XML through the Europe PMC REST service after the MDPI PDF
    returned 403: every section (1–5), all five figure captions, the
    acknowledgements, the data statement and the reference list. The
    equations were rebuilt by eye from the flattened MathML. The figures
    themselves were not seen, only their captions; the per-transition
    values plotted in Figures 3–5 were therefore not checked. The
    supplementary figure (the replication with spinglass and leading
    eigenvector communities) was not fetched. The paper has no theorems
    and no appendix.
date: '2026-10-14'
summary: >-
  Information-theoretic emergence measures built on past–future mutual
  information are expected values, and their local (pointwise) values can
  be negative. In a four-node Boolean toy, a coarse-graining that is
  emergent on average maps about 53% of informative micro transitions to
  misinformative macro ones, and the whole-to-whole synergy atom is
  negative for 31.25% of macro transitions. In a connectome, misinformative
  edges fall mostly between communities. The paper argues the possibility
  is general to any excess-entropy measure; it shows instances, not a
  theorem.
---
<!-- inactive-ok-file: THEORY-268 — Proposed; the theory filed from this reading -->
<!-- inactive-ok-file: CLAIM-157 CLAIM-161 THEORY-222 THEORY-036 — Proposed; the answer, persistence test and accounts this reading bears on, open -->

# NOTE-756: Varley — Flickering Emergences

## Contribution

Two information-theoretic accounts of emergence, Hoel's coarse-graining
account and the integrated-information-decomposition (ΦID) account of
Mediano, Rosas and colleagues, both score a system by an expected value of
the mutual information between its past and its future. The paper takes
those scores apart transition by transition. It shows, in one toy system
for each framework and in one human connectome, that a system emergent on
average can have many particular transitions whose local value runs the
other way. It names this "flickering emergence" and argues that any
measure built on time-delayed mutual information admits it.

## Key insight

Mutual information is never negative, but its pointwise value is, whenever
a realised pair (x, y) is less likely under the coupling than under
independence. An emergence score that is an expectation of such values can
therefore be positive while some of the moments it averages are negative.
Then "the system is emergent" holds of the ensemble of transitions and
fails at those moments, which the paper glosses as the system briefly
being "more like a collection of 'parts'".

## Assumptions

- **Discrete, stationary, Markov dynamics.** Excess entropy is cut to one
  step, E(X) = I(X_{t−1}; X_t), and the system is given by a transition
  probability matrix.
- **Coarse-graining account:** effective information is computed with a
  maximum-entropy (uniform) distribution imposed on past states, as in
  Hoel et al.; the coarse-graining is fixed by the analyst (here a logical
  AND over pairs of nodes).
- **ΦID account:** a localisable double-redundancy function is assumed,
  Varley's I_τsx; the decomposition and its lattice of sixteen atoms
  (for two variables) are taken from Mediano et al. and not re-derived.
- **Network application:** a random walker on a structural connectivity
  matrix, with Infomap communities as macro-nodes.
- The general claim ("any approach based on excess entropy") is argued
  from localisability, not proved for each framework.

## Key results

- **Local mutual information (Eqs. 4–5).** i(x; y) = log P(x,y)/(P(x)P(y))
  = h(x) − h(x|y). It is negative when P(x,y) < P(x)P(y), "when a system
  is transiently breaking from its own average, long-term behaviour".
  *Holds:* for any joint distribution; I(X;Y) = E[i(x;y)] ≥ 0.
- **Local excess entropy (Eq. 8).** e(x) = i(x_{t−1}; x_t), negative when
  P(x_t | x_{t−1}) < P(x_t): "The past transiently ceases to inform of the
  future and instead misinforms."
- **Coarse-graining emergence (Eqs. 9–12).** Effectiveness
  F̄(X) = I(X_{t−1}^{Hmax}; X_t)/log N; emergence when
  log(F̄(X̃)/F̄(X)) > 0. The toy four-node Boolean network coarse-grained
  by AND over pairs gives log(F̄(X̃)/F̄(X)) ≈ 0.202.
- **Incongruous dynamics, coarse-graining (§3.1).** Defined as e(x̃) < 0
  while e(x) > 0. "≈52.73% of informative micro-scale edges map to
  misinformative macro-scale edges"; these are mostly low-probability
  transitions, which is why the average stays emergent. A random walk on
  the micro chain shows sign flips of e(x̃_t)/e(x_t) along the trajectory.
  The paper notes the normalisation by log N does not carry over locally,
  since local values are unbounded, so only signs are compared.
- **Network application (§3.1).** A Human Connectome Project structural
  matrix, Infomap macro-nodes: effectiveness ≈0.37 bit micro against
  ≈0.38 bit macro; ≈22.47% of informative micro edges map to
  misinformative macro edges. Informative edges were about as likely
  within communities (≈52.3%) as between (≈47.7%); misinformative edges
  were mostly between communities (≈80.4% against ≈19.6%). Replicated with
  spinglass and leading-eigenvector communities (supplement, not seen).
  *Holds:* one subject's matrix.
- **ΦID emergence (§§2.4.2, 3.2).** Temporal synergy is the atom
  {X1,X2}→{X1,X2}, "that portion of E(X) that is not disclosed by any
  simpler combination of elements". The toy macro system has
  Φ∂ ≈ 0.031 bit on average; 31.25% of its sixteen transitions have a
  negative local value of that atom. Two transitions ending in (0,0)
  have opposite-signed synergy, double-redundancy and "downward
  causation" atoms.
- **The general claim (§§1, 5).** Flickering is "an unavoidable
  consequence of any formal approach based on time-delayed mutual
  information" in the sense that the possibility is; the Conclusions say
  such approaches are "likely to display" it. Barnett and Seth's
  dynamical independence and Chang et al.'s information closure are
  expected to show it "barring an unexpected mathematical result", not
  shown.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Pointwise past–future mutual information can be negative while its expectation is positive | strong | standard identity, Eqs. 4–8 |
| C2 | A coarse-graining emergent on average can map most informative micro transitions to misinformative macro ones | moderate | one constructed toy (§3.1, Fig. 3) |
| C3 | The ΦID synergy atom can be positive on average and negative at particular transitions | moderate | the same toy at macro scale (§3.2, Fig. 5) |
| C4 | In a connectome, misinformative macro edges lie mostly between communities | weak | one subject, one walker model (§3.1, Fig. 4) |
| C5 | Every excess-entropy-based account of emergence admits flickering | weak | argued from localisability; two frameworks shown, two others conjectured |
| C6 | If integrated emergence is identified with a sense of self, the sense of self should flicker reportably | weak | a conditional raised in Discussion, not tested |

## Method

Take a transition probability matrix, compute local excess entropy for
every transition at micro and macro scale, and count sign mismatches.
For ΦID, solve the double-redundancy lattice locally for each transition
with I_τsx and Möbius inversion (Eq. 15), and read the sign of the
synergy atom. Run a random walk to show the sign changes over time.

## Concepts

- **Local (pointwise) mutual information** — i(x; y), the realised-pair
  term whose expectation is I(X; Y).
- **Misinformative transition** — one with e(x) < 0: knowing the past
  makes the realised future less expected than chance.
- **Incongruous dynamics** — a transition informative at one scale and
  misinformative at another (coarse-graining), or a negative local value
  of an atom whose expectation is positive (ΦID).
- **Flickering emergence** — the transient loss of an average emergent
  property at particular transitions, "like a candle sputtering".
- **Temporal synergy** (Mediano et al.'s "causal decoupling") — the
  {X1,X2}→{X1,X2} atom of ΦID.

## Connections

It builds on Hoel, Albantakis and Tononi's effective information
([LIT-1038](../literature.d/LIT-1038.md)), on the ΦID programme reviewed in [LIT-025](../literature.d/LIT-025.md), and on Lizier's
local information dynamics. Varley and Hoel's "emergence as the conversion
of information" ([LIT-027](../literature.d/LIT-027.md)) is cited as the observer-relative reading under
which flickering is only model failure. Klein and Hoel's network
coarse-graining supplies the connectome analysis. The Discussion argues a
"pragmatic pluralist" view, that the two frameworks are distinct valid
kinds of emergence.

## Bearing on the record

- **[QUESTION-035](../questions.d/QUESTION-035.md) (how long a combined form lasts).** The seed claim in
  [LIT-953](../literature.d/LIT-953.md) is confirmed: the paper does show emergence holding on average
  and failing at particular configurations. What it adds for the question
  is that a criterion of unity computed as an average over the dynamics
  gives no verdict about a particular moment. "How long does it last" then
  needs a window and a rule for how many misinformative moments end the
  form, which none of these measures supplies.
- **[CLAIM-157](../claims.d/CLAIM-157.md) (the block criterion and its duration clause).** "It lasts
  as long as that block persists" is stated over joint dynamics, which
  are estimated over an interval. Varley shows that for information
  measures the interval verdict and the moment verdict can differ in sign,
  so the duration clause inherits the same question of window. The
  network result also bears on the boundary clause: misinformative
  transitions concentrate on edges between communities, so the boundary of
  a block is where the macro description fails most often.
- **[CLAIM-161](../claims.d/CLAIM-161.md) (persistence as conserved coherence).** If the coherence
  measure is an information quantity, "approximately conserved along its
  own trajectory" must tolerate negative local values that average out.
  The paper does not discuss persistence, so this is the record's
  application, not the paper's claim.
- **[THEORY-222](../theory.d/THEORY-222.md) (causal emergence).** Complements it: the average
  effective-information gain [THEORY-222](../theory.d/THEORY-222.md) holds can coexist with most
  informative micro transitions becoming misinformative at the macro
  scale. Nothing in [THEORY-222](../theory.d/THEORY-222.md) cites this paper, and nothing there needs
  correcting.
- **[THEORY-036](../theory.d/THEORY-036.md).** Cites Varley and Hoel, not this paper; no bearing.
- **New THEORY.** [THEORY-268](../theory.d/THEORY-268.md) holds the claim no existing THEORY
  holds: emergence measured as an expectation is a property of the
  ensemble of transitions, not of each moment.
- No instruction for machine-learning practice; nothing for the
  anthology.

## Limitations

- One four-node toy, chosen to display the effect, carries both framework
  results; one structural connectome carries the network result.
- Whether a negative local value marks a change in the system or a
  fluctuation is left open: "it does not necessarily define why a
  particular moment breaks from the long-term behaviour".
- The local ΦID result depends on the choice of redundancy function
  (I_τsx); other redundancy functions are not tried.
- The general claim for every excess-entropy measure is argued, not
  proved, and two named frameworks are not computed.
- For a deterministic, invertible dynamics with a uniform state
  distribution every realised transition has e(x) = log N > 0, so
  flickering is possible in these frameworks, not guaranteed for every
  system; the paper does not state the conditions under which it must
  occur.

## Open questions

- What fraction of moments may be misinformative before a form is no
  longer one system, and is there a principled window?
- Do misinformative transitions cluster in time (a breakdown) or scatter
  (noise)? A test on a system with a known regime change, such as the
  flock that scatters or the fibrillating heart the paper names, would
  separate the two.
- Do the coarse-graining and ΦID measures flicker at the same moments on
  a shared system?
