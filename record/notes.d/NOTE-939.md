---
number: 939
status: Read
formerly:
- NOTE-tmpik4nc
paper: 'LIT-1166'
title: 'Massey — Causality, feedback and directed information'
version: 1
history:
- version: 1
  date: '2026-10-17'
  note: >-
    Read in full from the author's preprint in the ETH Zürich ISI archive
    (mass-1990-1.pdf), 6 pp.: abstract, Introduction, Discrete Channels,
    Directed Information, Causal Systems, Remarks, references [1]–[3].
    Nothing skipped. Extracted with pdftotext. I checked the proofs of
    Theorems 1–3, computed directed and mutual information for a binary
    symmetric channel with noiseless feedback, and checked by chain rule
    and numerically that directed information splits into transfer
    entropies plus instantaneous terms (script in the session scratchpad,
    checks/ay_massey.py). The proceedings version was not compared, and
    Marko (1973), the source of the idea, was not read.
date: '2026-10-17'
summary: >-
  The textbook DMC, P(y^N|x^N) = Π P(y_n|x_n), is the DMC used without
  feedback; the right definition is P(y_n|x^n y^{n−1}) = P(y_n|x_n).
  Directed information I(X^N→Y^N) = Σ I(X^n; Y_n | Y^{n−1}) is at most
  I(X^N;Y^N), equal without feedback (Theorem 1), and in a causal system
  bounds what the output says about the source (Theorem 3), so feedback
  cannot raise DMC capacity. Statistical dependence has no direction;
  directed information does.
---

# NOTE-939: Massey — Causality, feedback and directed information

## Contribution

Before this paper, the standard definition of a discrete memoryless
channel tacitly assumed no feedback, so the classic result that feedback
does not raise a DMC's capacity was, Massey says, "logically meaningless"
under it. After it, the DMC and "use without feedback" are separate
definitions, and a directed information quantity, from Marko (1973), gives
a two-line proof of the capacity result and a tighter bound than mutual
information when feedback is present.

## Key insight

Conditioning the output at time n on the whole input sequence X^N lets
later inputs, which feedback makes depend on earlier outputs, carry
information backwards. Conditioning only on the inputs up to n, X^n, and
summing over n keeps the direction of time. That sum is directed
information.

## Assumptions

- **Discrete time, finite alphabets** (p. 1).
- **A discrete channel** is a specification of P(y_n | x^n y^{n−1}) for all n
  (p. 1). Memoryless: P(y_n | x^n y^{n−1}) = P(y_n | x_n) (Eq. 1).
- **Use without feedback**: P(x_n | x^{n−1} y^{n−1}) = P(x_n | x^{n−1})
  (Eq. 2).
- **A causal system** (Eq. 8): for every source sequence u^K and every
  channel, P(y_n | x^n y^{n−1} u^K) = P(y_n | x^n y^{n−1}). Sources are fixed
  before transmission and reach a channel only through its inputs.

## Key results

- **Eqs. 3–5.** With no feedback, P(y^N|x^N) = Π P(y_n|x^n y^{n−1}) (Eq. 4),
  and with memorylessness the textbook Eq. 5. Noiseless feedback
  x_n = y_{n−1} makes Eq. 5 false: P(y^N|x^N) = 0 whenever x_n ≠ y_{n−1}.
- **Ash's "causality" relation (Eq. 6)** P(y_n|x^N y^{n−1}) = P(y_n|x^n
  y^{n−1}) rules out feedback, not acausality.
- **Eq. 7.** I(X^N→Y^N) = Σ_{n=1}^N I(X^n; Y_n | Y^{n−1}). Not symmetric.
- **Theorem 1.** I(X^N→Y^N) ≤ I(X^N;Y^N), equal without feedback.
  *Checked:* replacing X^n by X^N in each term gives the chain rule for
  I(X^N;Y^N); without feedback, Eq. 4 makes H(Y^N|X^N) = Σ H(Y_n|X^n
  Y^{n−1}).
- **Theorem 2.** For a DMC, I(X^N→Y^N) ≤ Σ I(X_n;Y_n), equal iff the Y_n are
  independent. *Checked:* by Eq. 1, I(X^N→Y^N) = H(Y^N) − Σ H(Y_n|X_n).
- **Theorem 3.** In a causal system, I(U^K;Y^N) ≤ I(X^N→Y^N). *Checked:*
  conditioning on X_n can only lower H(Y_n|Y^{n−1}U^K), and Eq. 8 removes
  U^K.
- **Capacity.** Theorems 2 and 3 give that feedback cannot raise a DMC's
  capacity, in a causal system.

**A numerical check of Theorem 1 with feedback.** A binary symmetric
channel with crossover 0.1, x_1 uniform and x_n = y_{n−1}: for N = 2,
I(X;Y) = 1.000 bit and I(X→Y) = 0.531 = 1 − h(0.1); for N = 3, I(X;Y) =
1.469 and I(X→Y) = 0.531 again. Every input after the first is the previous
output, so only the first channel use carries new information. Mutual
information counts the fed-back copies; directed information does not.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | The usual DMC definition (Eq. 5) holds only for a DMC used without feedback | strong | Eqs. 1–5; exact |
| C2 | I(X^N→Y^N) ≤ I(X^N;Y^N), with equality without feedback | strong | Theorem 1; checked, and numerically with feedback |
| C3 | In a causal system I(U^K;Y^N) ≤ I(X^N→Y^N) | strong | Theorem 3; checked |
| C4 | Feedback does not increase DMC capacity | strong | Theorems 2–3; a classical result, re-proved |
| C5 | With feedback, directed information is the more useful quantity | moderate | follows from C2–C3 as a tighter bound; "whether [it] suffices as a basis for a genuine information theory of feedback systems remains … to be seen" |
| C6 | Statistical dependence, unlike causality, has no inherent direction | assertion | p. 2; the motivating remark |

## Concepts

- **Directed information I(X^N→Y^N)** — Eq. 7.
- **Use without feedback** — Eq. 2.
- **Causal system** — Eq. 8. A condition on how sources reach channels, not
  a notion of intervention.

## Connections

- **Builds on** Marko (1973) for the idea, Gallager (1968) for notation, and
  Ash (1965) as the source of the "causality" relation it criticises.
- **Transfer entropy and Granger causality.** By the chain rule,
  I(X^n; Y_n | Y^{n−1}) = I(X^{n−1}; Y_n | Y^{n−1}) + I(X_n; Y_n | X^{n−1}
  Y^{n−1}). The first term is the full-history transfer entropy from X to
  Y at time n; the second is instantaneous dependence given the joint past.
  So directed information is the sum of full-history transfer entropies
  plus the sum of instantaneous terms. *Checked* numerically on a random
  binary joint distribution with N = 3: 0.0590 + 0.1058 = 0.1648, the
  directed information. This is the record's derivation; Massey does not
  mention transfer entropy, which postdates the paper. In Geweke's terms
  ([LIT-1169](../literature.d/LIT-1169.md)), the first sum is feedback from X to Y and the second
  instantaneous feedback, and Granger causality ([TERM-058](../terms.d/TERM-058.md)) is the
  first part only. My inference.
- **[CLAIM-333](../claims.d/CLAIM-333.md)**'s counterexample is exactly a process where the first
  sum is zero and the second is not: directed information sees the
  within-step influence that transfer entropy and Granger causality miss.
  My inference.
- **Interventional notions.** Massey's "causal" (Eq. 8) is a factorization
  condition about where information may enter, not an intervention. Ay and
  Polani ([NOTE-946](NOTE-946.md)) and Eichler and Didelez ([NOTE-941](NOTE-941.md)) give
  interventional ones.

## Bearing on the record

- Filed as [THEORY-711](../theory.d/THEORY-711.md).
- For [TERM-057](../terms.d/TERM-057.md): directed information is not transfer entropy. It
  conditions on the current input and uses full histories. Transfer
  entropy with full histories is one of its two parts.
- **For the Anthology of the SOTA:** no instruction for ML practice.

## Limitations

- A short conference paper. The capacity result is classical; the
  contribution is the definitions and the two-line proofs.
- Finite alphabets and discrete time only.
- The paper does not say what directed information measures beyond being a
  bound; C5's closing sentence leaves that open.
- "Causal" is Massey's word for Eq. 8. Read as intervention, it would
  overstate the paper.

## Open questions

- Whether directed information "suffices as a basis for a genuine
  information theory of feedback systems" (Massey's own).
- When directed information equals an interventional quantity such as Ay
  and Polani's information flow. Not addressed in either paper.
