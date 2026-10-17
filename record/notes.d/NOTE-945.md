---
number: 945
status: Read
formerly:
- NOTE-tmpt2aw8
paper: 'LIT-1165'
title: 'James, Barnett and Crutchfield — Information flows? A critique of transfer entropies'
version: 1
history:
- version: 1
  date: '2026-10-17'
  note: >-
    Read in full from arXiv 1512.06479v2 (17 June 2016; SFI Working Paper
    16-01-001), 6 pp.: abstract, text, Figs. 1–2 from captions and prose,
    references [1]–[37]. Nothing skipped. PDF from arxiv.org, extracted
    with pdftotext; the I-diagram region values came through as stray
    numbers and were read from the prose. I recomputed both examples
    exactly, with lag-1 histories (both processes are first-order, so
    longer histories add nothing), and the Williams–Beer I_min PID of the
    first, with a script in the session scratchpad (te-checks/pid.py). I
    did not compare the PRL version.
date: '2026-10-17'
summary: >-
  Information flow from X to Y is information in Y attributable solely to
  X's past. Transfer entropy is not it. For Y_t = X_{t−1} ⊕ Y_{t−1} it is
  1 bit, but the bit is synergistic, carried by both pasts jointly
  (co-information −1). For Z_t = X_{t−1} ⊕ Y_{t−1} both transfer
  entropies are 0, and the causation entropies (conditional transfer
  entropies) are 1 bit each, again localizing a joint bit. By PID,
  transfer entropy is unique plus synergistic information; conditioning
  adds synergy, it does not only remove redundancy.
---

# NOTE-945: James, Barnett and Crutchfield — Information flows? A critique of transfer entropies

## Contribution

Before this Letter, transfer entropy was routinely read as information
flow, and its known weakness was the indirect path (X → Z → Y), which
causation entropy fixes by conditioning on Z. After it, the reading fails
for a different reason that conditioning cannot fix. Transfer entropy
assigns to one source information that only the joint past carries. A
measure built on conditional mutual information inherits the failure.

## Key insight

Conditioning is not subtraction. I[X : Y | Z] can exceed I[X : Y]. In a
partial information decomposition it equals X's unique information plus
the synergy of X and Z. So a transfer entropy is "how much better Y_t is
predicted when X's past is added to Y's", which is a fact about
prediction. It is not "how much of Y_t came from X".

## Assumptions

- **A definition of flow** as localized information: "information that is
  currently in Y, the 'cause' of which can be solely attributed to X's
  past" (p. 1). The critique is relative to this definition, which the
  authors align with Wiener and Granger's intuitions.
- **Stationary discrete processes**, with transfer entropy over full pasts,
  T_{X→Y} = I[Y_t : X_{0:t} | Y_{0:t}] (Eq. 1).
- **A PID exists** with I[X₁ : Y] = R + U₁ and I[X₁ : Y | X₂] = U₁ + S
  (Discussion). No particular redundancy measure is needed for the
  examples, since every proposed one gives XOR pure synergy.

## Key results

- **Two series (Fig. 1).** X_t, Y_0 i.i.d. fair bits, Y_t = X_{t−1} ⊕ Y_{t−1}.
  H[Y_t] = 1, I[Y_t : (X_{0:t}, Y_{0:t})] = 1, I[Y_t : Y_{0:t}] = 0,
  T_{X→Y} = 1, I[Y_t : X_{0:t}] = 0, I[Y_t : Y_{0:t} | X_{0:t}] = 1,
  co-information −1. *Checked exactly:* all six values; the I_min PID with
  target Y_t and sources X_{t−1}, Y_{t−1} gives R = U₁ = U₂ = 0, S = 1.
- **Three series (Fig. 2).** X, Y i.i.d. fair bits, Z_t = X_{t−1} ⊕ Y_{t−1}.
  T_{X→Z} = T_{Y→Z} = 0; I[Z_t : X_{0:t}] = I[Z_t : Y_{0:t}] =
  I[Z_t : Z_{0:t}] = 0; C_{X→Z|(Y,Z)} = C_{Y→Z|(X,Z)} = 1. *Checked
  exactly:* all seven.
- **Diagnosis.** T_{X→Y} = U(X past) + S(X past, Y past). "Only this
  unique information" is a candidate for flow, as Barrett (2015) and
  Williams and Beer (2011) proposed.
- **Directed information** (Massey) "is essentially a sum of transfer
  entropies and so inherits the same flaws". Ay and Polani's
  interventional flow and Granger causality are conjectured to fail for
  the same reason, conflating dyadic and polyadic relations.
- **Networks.** A transfer-entropy graph of the second example has no
  edges. A hypergraph is the suggested repair.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Transfer entropy can be positive with no information solely attributable to the source (overestimates flow) | strong | Example 1, exact; checked |
| C2 | Transfer entropy can be zero from each of two sources that jointly determine the target (underestimates influence) | strong | Example 2, exact; checked |
| C3 | Causation entropy fixes indirect paths but localizes joint information in the same way | strong | Example 2, exact; checked |
| C4 | Under PID, transfer entropy = unique + synergistic information | strong | from I[X₁:Y\|X₂] = U₁ + S, which holds for any PID satisfying the consistency equations |
| C5 | Unique information, if it could be measured, may be a measure of flow | weak | proposal; "no broadly accepted quantification of unique information" [19] |
| C6 | Directed information inherits the flaw | moderate | "essentially a sum of transfer entropies"; not shown here |
| C7 | Ay and Polani's interventional flow and Granger causality fail for the same reason | conjecture | stated as a conjecture (p. 4) |
| C8 | Similar failures arise in Gaussian systems, so the issue is widespread | weak | cited to Barrett (2015); no Gaussian example given |
| C9 | Modelling complex systems as graphs with transfer-entropy edges is "intrinsically flawed" | interpretive | from C2 and the dyadic structure of graphs |

## Concepts

- **Information flow** — information in Y_t solely attributable to X's
  past, "localized" (p. 1).
- **Influence** — any dependence of Y_t on X's past, localizable or not
  (implicit; the examples "make operational" the distinction).
- **Causation entropy** — I[Y_t : X_{0:t} | Y_{0:t}, Z_{0:t}], Sun and
  Bollt's conditional transfer entropy (Eq. 2).
- **Co-information** — the central atom of a three-variable I-diagram,
  negative under synergy.

## Connections

- **Schreiber (2000, [LIT-1177](../literature.d/LIT-1177.md))** introduced transfer entropy as a
  measure of information transfer. This is the critique of that
  reading, not of the quantity. The authors "do not object to the transfer
  entropy as a measure of the reduction in uncertainty about one time
  series given another".
- **Williams and Beer (2011, [LIT-1176](../literature.d/LIT-1176.md), [NOTE-942](NOTE-942.md)).** Example 1 is
  their d = 1 process, the controlled-NOT, with the roles renamed. They
  call its 1 bit "state-dependent transfer entropy". This paper calls it
  synergy that is not flow. Both papers give the same decomposition; they
  disagree on what to call its synergistic part. The observation is mine.
- **Barnett, Barrett and Seth (2009, [LIT-1171](../literature.d/LIT-1171.md))** is cited for the
  identification of transfer entropy with Granger causality. With
  [THEORY-641](../theory.d/THEORY-641.md) that makes transfer entropy a predictive quantity, which
  this paper accepts. It denies the step from prediction to flow.
- **[CLAIM-333](../claims.d/CLAIM-333.md)** concerns the step from Granger prediction to
  intervention, and this paper the step from prediction to localized
  flow. They are separate failures. In Example 1, intervening on X_{t−1}
  does change Y_t, so X has an interventional effect on Y. What fails is
  attributing the bit to X alone. My observation.
- **[THEORY-497](../theory.d/THEORY-497.md) and [NOTE-010](NOTE-010.md) (ΦID).** ΦID decomposes past→future
  information by source and target atoms, so it can separate what this
  paper says transfer entropy conflates. [NOTE-799](NOTE-799.md)'s open question, a ΦID
  of transfer entropy, is the direction this paper points to. My
  connection.
- **[THEORY-568](../theory.d/THEORY-568.md).** The vulnerability numerator's single-source terms
  I(X_j; Y | X_{−j}) are unique plus synergy in exactly this sense
  ([NOTE-053](NOTE-053.md)'s connection makes T_{Y→X} one of them).
- **[THEORY-257](../theory.d/THEORY-257.md) (dynamical independence)** is defined as zero transfer
  entropy from micro to macro. By Example 2, zero transfer entropy from
  each micro variable does not mean the micro history carries nothing;
  Barnett and Seth condition on the whole micro history at once, which
  avoids that case. My observation, unchecked against [NOTE-791](NOTE-791.md)'s
  details beyond its summary.
- **[THEORY-275](../theory.d/THEORY-275.md) / [NOTE-788](NOTE-788.md)** read transfer-entropy asymmetries in a
  Gaussian (Langevin) system as flow direction. This paper says such
  readings need the synergistic part separated; Barrett (2015) is cited
  for Gaussian cases. Not tested on that system.

## Bearing on the record

- Filed as [THEORY-707](../theory.d/THEORY-707.md). It is the main ground for [CLAIM-335](../claims.d/CLAIM-335.md).
- [NOTE-788](NOTE-788.md) and [THEORY-275](../theory.d/THEORY-275.md) speak of "information flow" and "backflow"
  between the colloids, the paper's own words. By this Letter that names
  the direction of predictive improvement, not localized flow. Nothing
  there rests on the stronger reading, and [THEORY-275](../theory.d/THEORY-275.md) already disclaims
  coupling architecture. [NOTE-122](NOTE-122.md) relays Barrett et al. calling transfer
  entropy "only a proxy" for inter-regional transfer, which agrees.
- **For the Anthology of the SOTA:** no instruction for ML practice.

## Limitations

- Both examples are deterministic XORs with uniform inputs, the case
  where every PID agrees. Away from it, how much of a transfer entropy is
  synergy depends on the redundancy measure, and the paper does not say
  which it would use.
- "Flow" is the authors' definition. A reader who means predictive
  improvement by "transfer" is not refuted, only renamed.
- The Gaussian claim (C8) and the directed-information and Ay–Polani
  claims (C6, C7) are cited or conjectured.
- The ε-transducer cure is pointed to, with its informational atoms "in
  preparation".

## Open questions

- A measure of unique information that the field accepts, and whether it
  then behaves as flow should, for instance additively along chains.
- Whether interventional flow (Ay and Polani, [LIT-1174](../literature.d/LIT-1174.md)) fails on
  Example 1. Intervening on X_{t−1} alone moves Y_t, so an interventional
  measure would credit X with the bit. Whether that is a failure depends on
  which definition of flow one keeps.
