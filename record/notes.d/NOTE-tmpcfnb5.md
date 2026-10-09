---
status: Read
paper: 'LIT-tmpmigxa'
title: 'Semantic Communication: A Survey of Its Theoretical Development'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read in full from the Europe PMC JATS full text of the open-access
    article (PMC10888479, CC BY 4.0), converted to plain text with the
    MathML flattened: abstract, Sections 1–8 and the reference list. The
    eleven figures were not seen (the text describes them). The equations
    were read from the flattened MathML and checked against their
    surrounding prose.
date: '2026-10-09'
summary: >-
  Surveys semantic information theory around three Shannon analogues:
  semantic entropy (no agreed definition; logical-probability, task,
  knowledge and context variants), semantic rate–distortion (meaning as a
  latent state S behind the observation X, with dual distortions), and
  semantic channel capacity (definitions under which it can exceed
  Shannon capacity). It adds the information bottleneck, age of
  information, joint source–channel coding and LLMs as tools, and lists
  open problems. It catalogues rather than reconciles.
---

<!-- inactive-ok-file: THEORY-tmp3ijnj — Proposed; filed from this batch's readings, under test -->

# NOTE-tmpcfnb5: Semantic Communication: A Survey of Its Theoretical Development

## Contribution

A review of the theory, not the systems, of semantic communication, in the
order of Shannon's theory: what semantic entropy is, what rate–distortion
becomes when the thing to preserve is meaning, and what capacity means at
the semantic level. Its addition is the arrangement and the explicit
statement of what is unsettled; it proves nothing new.

## Key insight

Every formal version of "semantic" information in this literature buys
tractability by fixing what meaning is for a given purpose: a logical
model set, a knowledge base, a task, a utility weight, or a hidden state
with a known joint law with the observation. Once that is fixed, the
Shannon machinery applies almost unchanged; the open problems are all
about how to fix it.

## Assumptions

Not a theorem-bearing paper. Its working assumptions are that semantic
communication sits on top of digital communication (Section 2.2: symbols
still cross a physical channel), and that semantics is "tailored to
particular contexts" and tasks (Section 3.2).

## Key results

What the survey reports, with the forms it gives:

- **Semantic entropy** (Section 3). Carnap–Bar-Hillel: H_s(e) = −log m(e)
  (Eq. 2), with the paradox that a contradiction has infinite
  information. Bao et al.: m(e) = μ(W_e)/μ(W), the statistical mass of the
  sentence's models (Eq. 3). Chattopadhyay et al.: the least expected
  number of queries about X needed to solve task V (Eq. 4). Melamed: a
  translation entropy of a word, H(T|w) plus a null-link term (Eq. 5).
  Choi et al.: binary entropy of the probability that e holds given a
  knowledge base (Eq. 8). Kountouris and Pappas: a utility-weighted
  entropy −Σφ(x)P(x) log P(x) (Eq. 10).
- **Semantic rate–distortion** (Section 4.2). Liu et al.:
  R(D_s, D_a) = min I(X; Ŝ, X̂) subject to a semantic distortion bound
  E d̂_s(X, Ŝ) ≤ D_s and an appearance bound E d_a(X, X̂) ≤ D_a (Eqs.
  21–22), where S, the intrinsic state, is not observed. Guo et al.: two
  users with side information Y, R = min I(X₁, X₂; X̂₁, X̂₂, Ŝ | Y)
  (Eq. 23).
- **Semantic capacity** (Section 5.2). Bao et al.: C_s = sup over
  P(X|Z) of {I(X; Y) − H(Z|X) + mean H_S(Y)} (Eq. 25), so semantic
  capacity can be above or below Shannon capacity depending on encoder
  ambiguity H(Z|X) and receiver inference. Ma et al.: C_s = max I(X;Y)/α
  with α < 1 the fraction of messages that are semantically distinct
  (Eq. 26); a rate above C can have bit errors and no semantic errors.
- **Tools** (Section 6). Age of information Δ(t) = t − u(t) and the age
  of incorrect information (Eq. 32); the information bottleneck
  L = I(T;X) − βI(T;Y) (Eq. 39) and Barbarossa et al.'s noisy linear
  version (Eq. 40); deep JSCC; LLMs as knowledge bases.
- **Open problems** (Section 7): fundamental limits of semantic coding,
  the relation of semantic to engineering coding, capacity of semantic
  networks, and the effect of network topology.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | There is no agreed definition of semantic entropy or unified semantic information theory | strong (as a report of the field) | Sections 3, 7 |
| C2 | Semantic rate–distortion is the most tractable of the three analogues, because semantic metrics already exist | moderate | Section 4, argued |
| C3 | Semantic channel capacity can exceed physical capacity when the system tolerates bit errors that do not change meaning | weak as stated: true under the definitions cited, which build it in | Section 5.2, Eqs. 25–26 |
| C4 | A general semantic capacity must be conditioned on task, knowledge, goals and timeliness | weak: the authors' proposal, not derived | Section 5.2 |
| C5 | The information bottleneck can give rise to human-like semantic categories | moderate, as reported from Zaslavsky et al. (arXiv 1808.03353) | Section 6.2 |

## Concepts

- **semantic information theory**: the mathematical theory of semantic
  communication and of representing semantics.
- **semantic noise**: a mismatch of meaning between sender and receiver,
  arising in the physical channel (a transmission error that changes a
  word) or in the semantic channel (a concept with no match in the target
  language; different background knowledge).
- **semantic channel capacity**: in most cited work, the capacity "at the
  semantic level", not the capacity of a separate semantic channel, which
  the authors say "does not really exist".
- **knowledge base**: the shared and private knowledge that lets encoder
  and decoder extract and interpret semantics; the feature the survey
  says most distinguishes semantic from conventional communication.

## Connections

Its three pillars rest on Carnap and Bar-Hillel (1952), Bao et al. (2011)
and Liu, Zhang and Poor (2021–2022). It cites Shannon ([LIT-764](../literature.d/LIT-764.md)), the
information bottleneck ([LIT-338](../literature.d/LIT-338.md)) and, for colour naming, Zaslavsky, Kemp,
Regier and Tishby's arXiv short paper (1808.03353) rather than the PNAS
paper held here as [LIT-tmpe6100](../literature.d/LIT-tmpe6100.md). It does not cite Blau and Michaeli's
rate–distortion–perception trade-off or anything built on it, so
Chai et al. ([LIT-tmpfnpwq](../literature.d/LIT-tmpfnpwq.md)) and Zhao et al. ([LIT-tmp2w545](../literature.d/LIT-tmp2w545.md)), which the
exchange named with it, are outside its map. Its definition of rate
distortion with a hidden semantic state is the one those two papers start
from.

## Bearing on the record

- **[CLAIM-tmpp8j04](../claims.d/CLAIM-tmpp8j04.md)** (task-sensitive information preservation is
  established in semantic and goal-oriented communication). The survey
  supports the general statement: task-oriented semantic entropy (Eq. 4),
  utility-weighted entropy (Eq. 10), rate–distortion with a hidden
  semantic state and side information (Eqs. 21–23), and the information
  bottleneck as task-relevant compression are all presented as existing
  work, and goal-oriented communication is named in the keywords. It does
  not support a stronger reading: it reports no theorem that ties
  preservation to a family of decision problems, and no treatment of
  distributions over interpretations. Those are in Zhao et al.
  ([LIT-tmp2w545](../literature.d/LIT-tmp2w545.md), [NOTE-tmpsmtp6](NOTE-tmpsmtp6.md)), not here.
- **Translation.** Two of its examples touch this record's translation
  line: Melamed's translation entropy of a word (Eq. 5) and the listing of
  "translation of one natural language into another language where some
  concepts … have no precise match" as semantic-channel noise. Both are
  mentioned, not developed.
- It is one of three sources of [THEORY-tmp3ijnj](../theory.d/THEORY-tmp3ijnj.md), the record's account of
  what the semantic rate–distortion frameworks formalise.
- **A misstated formula.** The information bottleneck is described as
  minimising I(T;X) "subject to the constraint that I(T;Y) does not exceed
  a predetermined threshold" (Section 6.2, Eq. 38, with
  {p(t|x): I(T;Y) ≤ D̂}). The bottleneck requires the relevant
  information to be at least the threshold; as written the minimum is
  trivially zero. The Lagrangian (Eq. 39) is the standard one.
- Nothing here is machine-learning practice; no anthology flag.

## Limitations

- A catalogue: the definitions of semantic entropy and capacity are set
  side by side without a comparison of what each implies.
- Coverage stops before rate–distortion–perception and before
  distributional (posterior-level) semantic distortion.
- Its answers to its own questions about capacity rest on definitions
  that make them true; the survey does not flag this.
- Equation 22 writes the semantic distortion as a function of X and Ŝ
  (d̂_s, the surrogate distortion of Liu et al.) without saying it is a
  surrogate for E d_s(S, Ŝ), and the text then calls S and Ŝ the
  "semantic understanding" and X and X̂ "their semantic representations",
  which blurs the hidden-state reading set out a paragraph earlier.

## Open questions

- Is there a semantic capacity that is not true by construction: one
  defined operationally, by a coding theorem for a stated semantic
  fidelity criterion, that can be compared with Shannon capacity? The
  survey asks this and leaves it open.
- How do the task-based definitions (Eq. 4, Eq. 10) relate to each other
  and to decision-theoretic comparison of information? The survey does
  not relate them.
