# Reader notes: crutchfield2003 (LIT-3010)

Crutchfield & Feldman, "Regularities Unseen, Randomness Observed: Levels of
Entropy Convergence", arXiv cond-mat/0102181; Chaos 13(1):25-54 (2003),
DOI 10.1063/1.1530990 (DOI and pages from OpenAlex, 2026-11-22).

## Step 1: copies located (2026-11-22)

- https://arxiv.org/pdf/cond-mat/0102181 : arXiv preprint (v1, 9 Feb 2001,
  the only version; SFI Working Paper 01-02-012). Fetched, HTTP 200, PDF,
  535,715 bytes. Lawful (arXiv). READ.
- https://doi.org/10.1063/1.1530990 : publisher's version (AIP, Chaos).
  OpenAlex marks it not OA. Not attempted (paywalled; arXiv copy suffices).
- https://pubmed.ncbi.nlm.nih.gov/12675408 : abstract record, not OA. Not attempted.
- https://escholarship.org/uc/item/8kd123jv : submitted version per
  OpenAlex (institutional repository). Lawful kind; not attempted.
- https://econpapers.repec.org/RePEc:wop:safiwp:01-02-012 : SFI working
  paper catalogue entry. Not attempted.
- https://csc.ucdavis.edu/~cmg/papers/rurociso.pdf : guessed author-page
  address; HTTP 404. No copy there.

arXiv API and OpenAlex queried with no email address sent. No bot check met.

## Provenance

arXiv v1 PDF (35 pp.), text extracted with pdftotext. Read in full: §§I-VIII
(pp. 2-28), Table I-III, Appendix A (proofs of Props 1-8, Lemmas 1, 3), the
opening of Appendix B. Skimmed: the rest of Appendix B and Appendix C (proof
of Thm 1), the reference list. Figures read from captions only. Page numbers
below are the arXiv PDF's. The 2003 journal version (Chaos 13, 25-54) was
not seen; differences from v1 are unknown, and the record's "(2003)"
citation rests on a 2001 text.

## Summary

The paper treats the block entropy H(L) of a stationary discrete process and
takes discrete derivatives and "integrals" of it. Level 1: the entropy gain
hµ(L) = ΔH(L) = H[S_L | S^{L-1}], converging to the entropy rate hµ. Level 2:
the predictability gain Δ²H(L) ≤ 0 (so H is concave). Integrating each level's
excess over its limit gives total predictability G = log2|A| − hµ (= minus the
redundancy), excess entropy E = Σ[hµ(L) − hµ], and a new quantity, the
transient information T = Σ[E + hµL − H(L)]. E is shown equal to the
subextensive part of H(L), and to the past-future mutual information. T is
proved to equal the synchronization information of a block-Markov process up
to a term in R and hµ (Thm 1). Worked examples (IID coins, period-16 and
period-5, golden mean, RRXOR, even process, simple nondeterministic source,
Thue-Morse) and a review of infinitary cases (intermittent maps, CA rules,
texts, Ising models after Bialek-Nemenman-Tishby) follow. §VII shows that an
observer at finite L who ignores E overestimates hµ by E/L ("regularities
unseen ... converted to apparent randomness"), and one who assumes it is
synchronized underestimates hµ and E. §VIII classifies processes (periodic,
aperiodic, memoryless, finitary: Markov / deterministic HMM / nondeterministic
HMM, infinitary).

## Contribution

A synthesis of known quantities (hµ, G, E under its many names) into one
derivative/integral hierarchy, with one new quantity (T) and one new theorem
(T and synchronization). The authors say so: "much of our narrative ...
restates results and intuitions known to a number of researchers" (p. 3).

## Key results

1. **E as subextensive part.** Prop 7, p. 11: "The excess entropy is the
   subextensive part of H(L): E = lim_{L→∞}[H(L) − hµL]", so H(L) ~ E + hµL.
2. **E as past-future information.** Prop 8, p. 11: "The excess entropy is the
   mutual information between the left and right (past and future)
   semi-infinite halves of the chain", "when the limit exists"; read as "the
   amount of historical information stored in the present that is
   communicated to the future" (pp. 11-12), and "the cost of amnesia" (p. 12,
   credited to Dan Upper).
3. **Finite-L estimators.** Eq. 60 E(L) = H(L) − L hµ(L); Eq. 61 E′(L) = the
   mutual information between the two halves of an L-block; Lemma 3, p. 13:
   "E′(L) ≤ E(L) ≤ E". E′(2T) is exactly TERM-141's I_pred(T) = 2H(T) − H(2T).
4. **Finitary vs infinitary.** Def. 1-2, p. 12: "A process is finitary if its
   excess entropy is finite"; Prop 9: for finitary processes hµ(L) − hµ <
   A/L; "For infinitary processes hµ(L) decays at or slower than 1/L"; an
   infinitary process "might scale as H(L) ∼ c1 + c2 log L + hµL".
5. **Closed forms.** Prop 10: period p gives E = log2 p. Prop 11: order-R
   Markov gives E = H(R) − Rhµ. Corollary 1 (exponential convergence):
   E ≈ (H(1) − hµ)/(1 − 2^−γ). Exponential decay is not proved in general:
   "there is not a direct proof of exponential decay for more general
   finitary processes" (p. 12); App. B argues it from transfer matrices.
6. **Transient information.** Thm 1, p. 14: for block-Markov processes the
   synchronization information S = T + ½R(R+1)hµ; "The transient information
   measures a structural property of the system — a property not captured by
   the excess entropy E." The three period-5 processes share E = log2 5 and
   have T = 4.073, 5.273, 4.873 bit-symbols (Table II, p. 16).
7. **Entropy rate does not fix structure.** Golden mean, RRXOR and even
   process all have hµ = 2/3, G = 1/3, and E ≈ 0.2516, 2, 0.902 bits
   (pp. 17-19).
8. **Information measures can understate structure.** Simple nondeterministic
   source: E ≈ 0.147, T ≈ 0.175, yet the optimal deterministic predictor has
   infinitely many states: "relying only on information theoretic quantities,
   one is misled as to the process's actual complexity" (p. 22).
9. **Infinitary with no randomness and no parameter.** Thue-Morse: hµ = 0,
   hµ(L) ∝ 1/L, "the excess entropy diverges; E(L) ∝ log2 L, indicating an
   infinite-memory process"; T(L) diverges linearly (p. 22). "There is no
   finite-state process that can generate the Thue-Morse sequence" (p. 21).
10. **Reported infinitary cases** (not the authors' results, p. 23): CA rules
    30/45 α ≈ 0.6, rule 120 α ≈ 1.0 (Grassberger); texts ("The Bible,
    Grimms' Tales, Moby Dick ...") hµ(L) − hµ ∼ L^α with α 0.4-0.6 [sign as
    printed; a decay, so L^−α is meant]; Beethoven α ≈ .75; Ising
    long-range α = 0.5 (Bialek et al.).
11. **Ignored memory becomes randomness.** Prop 13, p. 24: when synchronized,
    h′µ(L) − hµ = E/L: "E bits of memory are converted into additional,
    apparent randomness." Prop 15 and §VII C: assuming synchronization too
    early gives ĥµ ≤ hµ and a reduced apparent memory Ê ≤ E (pp. 25-26).
12. **Against disorder-based complexity.** p. 10: measures "based on
    multiplying G by hµ" (López-Ruiz et al.; Shiner et al.) "fail to capture
    structure or memory, since they are only a function of disorder hµ".
13. **Limits of the frame, by the authors.** p. 11: how memory "is organized
    cannot be done within the framework of information theory; a more
    structural approach based on the theory of computation must be used";
    p. 27: computational mechanics' ε-machine "captures all of a source's
    structure"; p. 27, on Bialek et al.: their result "holds in a slightly
    different context than ours", an observer learning a distribution by
    successive sampling rather than block histograms.

## Assumptions

Stationary process on a finite alphabet; observer knows block probabilities
exactly (no finite-sample estimation, explicitly set aside, p. 3); H(0) = 0,
hµ(0) = log2|A| as boundary conditions (G = −R turns on this); Thm 1 for
directly observed block-Markov processes only; exponential convergence for
finitary HMMs assumed/empirical, not proved; ergodicity not stated as an
assumption (the measure is shift-invariant). One dimension; higher-dimensional
E is ambiguous (p. 28).

## Concepts

block entropy H(L); entropy gain hµ(L); predictability gain Δ²H(L);
redundancy R and total predictability G; excess entropy E (aliases listed
p. 10: stored information, effective measure complexity, complexity,
predictive information, reduced Rényi entropy of order 1); transient
information T; synchronization information S; finitary / infinitary
processes; measure sofic process; nondeterministic HMM; weak Bernoulli
(finite E, citing del Junco and Rahe, p. 27).

## Verdict on the exchange's characterization

LIT-3010 and TERM-141 have A invoke the work for "excess entropy as the
measure of a process's stored structure". **Fair for "stored information",
overstated for "the measure of structure".** The paper calls E "one kind of
memory" (p. 12), "apparent memory", historical information communicated to
the future, and then shows E missing structure twice: T separates processes
with equal E (result 6), and the SNS has small E and an infinite-state
predictor (result 8). It assigns structure proper to computational mechanics
(result 13). TERM-141's own text attributes the regimes and the
random-vs-multiscale distinction to Bialek et al., not to this paper; the
paper does support the distinction in its own terms (hµ vs E; results 7, 11).
LIT-3010's summary ("excess entropy, transient information and Markov order")
is accurate, Markov order entering through Prop 11 and Thm 1.

## Bearing on the named codes

- **TERM-141** (predictive information / excess entropy). **Supports** the
  definition and the identities: E = lim[H(L) − hµL] (Prop 7) and E =
  I(past; future) (Prop 8); its finite-window quantity is the paper's E′(L)
  (Eq. 61), and Lemma 3 adds E′(L) ≤ E(L) ≤ E, a bound TERM-141 lacks.
  Supports "Not entropy": IID coins have E = 0 at any hµ (p. 15-16).
  **Qualifies** the regimes: logarithmic growth is not a sign of finitely
  many learned parameters; Thue-Morse is deterministic, has no parameter, and
  has E(L) ∝ log L from infinite-state, aperiodic structure (result 9).
  Logarithmic growth thus has at least two sources: the Bialek parameter case
  and aperiodic zero-entropy order. This belongs under TERM-141's condition 2
  ("infinitely many such quantities, or long memory") rather than condition 1,
  and it is an ergodic case. **Qualifies** "Not statistical complexity" only
  in passing: the paper does not compute Cμ but its SNS example (3 hidden
  states, infinitely many causal states, finite E) shows the bound E ≤ H of
  any generator's state (my remark, by data processing; not in the paper)
  can be tighter than one via causal states. **Leaves open** "Not a sign of
  criticality": the paper is silent on criticality except for reporting the
  Bialek Ising exponents.
- **THEORY-2151 / LIT-3008 / NOTE-2243** (Bialek, Nemenman, Tishby).
  **Parallel, with a stated contrast.** This paper treats E and Bialek's
  predictive information as the same quantity (alias list, p. 10), reports
  their Ising α values (p. 23), and says their parameter-count result "holds
  in a slightly different context" of sampling-based learning (p. 27). It
  corroborates NOTE-2243's identification of S₁ with excess entropy when
  finite; it does not take up the divergence-at-criticality assertion.
- **QUESTION-507** (computational capacity near transitions). **Background
  only.** The paper offers measures (E, T, G) a capacity study could use and
  the finitary/infinitary split; it says nothing on transitions, capacity or
  tasks. Its warning that finite-L estimates convert unseen memory into
  apparent randomness (Prop 13-15) bears on point 2 ("which measure") as a
  methodological caution for finite-window studies such as LIT-2980.
- **CLAIM-805** (criticality is not the maximum of complexity). **Supports**
  the separation of entropy, predictability and memory (results 7, 11, 12):
  equal hµ with unequal E; hµ·G "complexity" rejected because it is a
  function of disorder alone. Silent on criticality; its ref [48] (Feldman &
  Crutchfield, "Discovering noncritical organization", 1998) is the authors'
  work on the point and is not held (not read here).
- **CLAIM-849 / ARG-152 / ARG-154.** Background: same quantity; the paper's
  growth classes (finite, log, power-law hµ(L) decay) frame the regimes, but
  it has nothing on Fisher spectra. No bearing beyond TERM-141's.
- **QUESTION-517 / LEAD-208** (effective dimensions; 2D Ising). Background:
  the paper warns 2D excess entropies differ by definition ("unlike in one
  dimension where the various expressions for the excess entropy are
  equivalent, they yield different results when extended to two
  dimensions", p. 28). LEAD-208's "growth of predictive information" on a 2D
  lattice must pick a definition; this **qualifies** the lead's plan.
- **SYNTHESIS-119.** Background; no change suggested.

## Limitations

A synthesis paper; most results are restated. Exact block probabilities are
assumed, so nothing about estimation from data. Thm 1 only for observed
Markov chains, not HMMs. Exponential convergence for finitary HMMs not
proved. Many numbers (γ fits, E, T) are numerical estimates. The text-entropy
exponents and the Ising exponents are cited, not derived. One printed sign
slip (L^α for a decay, p. 23) and garbled indices in Eq. 53 as extracted.
Read from the 2001 preprint, not the 2003 journal text.

## Candidate THEORY

Sentence: "For a stationary process on a finite alphabet, the excess entropy
E, the summed excess of the finite-L entropy-rate estimates over the entropy
rate, equals both the subextensive part of the block entropy and the mutual
information between past and future; it is finite exactly when those
estimates fall faster than 1/L, and an observer who ignores it at block
length L overestimates the entropy rate by E/L, while E does not fix how hard
the process is to synchronize to, which the transient information measures
and for block-Markov processes equals the synchronization information up to
½R(R+1)hµ."

promote_when: a second reading (e.g. Shalizi & Crutchfield LIT-1126, or a
textbook treatment) confirms the identities E = lim[H(L) − hµL] = I(past;
future) and the E/L overestimate; and Thm 1 is checked on one example (e.g.
the golden mean process, R = 1: S = T + hµ).

## Recheck (search after reading)

Searched record/ for: Thue-Morse, golden mean, even process, effective
measure complexity, finitary, weak Bernoulli, López-Ruiz/Shiner, subextensive,
Grassberger, Ebeling, ε-machine, block entropy, Markov order, hidden Markov,
Feldman, Crutchfield. Held entries the first search missed:

- **NOTE-689 / LIT-888 / THEORY-784, THEORY-204** (Deriving neural scaling
  laws from language statistics). Its Hypothesis 1, H_n − H_∞ ≍ n^−γ, is
  this paper's power-law entropy convergence, and NOTE-689 already names
  "Crutchfield and Feldman's" form of Hilberg's hypothesis. With γ ≈ 0.27-0.33
  < 1, Prop 9 makes that token process infinitary (E diverges, as L^(1−γ));
  consistent with the paper's reported text exponents 0.4-0.6 (p. 23).
  **Parallel/supports** as to classification.
- **NOTE-1372 / LIT-1126** (Shalizi & Crutchfield, Computational mechanics):
  "Excess entropy is a lower bound on stored memory, not a measure of it"
  (its C5, Thm 5). **Parallel**: the same lesson as results 8 and 13, and
  the record's best second reading for the candidate THEORY.
- **NOTE-978 / THEORY-756** (thermodynamic depth of causal states): cites
  "Eq. (106) of Feldman and Crutchfield" for v < Cμ. Background; that Eq. is
  from another Feldman-Crutchfield paper, unidentified here (this one's
  equations stop near 105 and none is on Cμ).
- (NOTE-055 matched "Shiner" only as golden shiners, a false hit; the record
  holds no López-Ruiz/Shiner complexity measure.)
- **THEORY-748 / NOTE-970** (block entropies in turbulence): background;
  block entropies blind to reflection and time reversal, a limit this paper
  does not discuss.
- **NOTE-591** (Shannon 1948, block entropy G_N → H): background, the
  hµ = lim H(L)/L estimator the paper calls h′µ(L) and shows converges more
  slowly than hµ(L) (Lemma 1).

Not held and relevant: Feldman & Crutchfield 1998 "Discovering noncritical
organization" (ref [48]); Ebeling and Pöschel 1994 on literary English
(ref [37]); Grassberger 1986 "Toward a quantitative theory of
self-generated complexity" (ref [13]; no LIT title match).

## Neighbours

None needed; the work itself was read. No other work was read or quoted.
