---
status: Read
paper: 'LIT-1213'
title: 'Halpern and Moses — Knowledge and common knowledge in a distributed environment'
version: 1
history:
- version: 1
  date: '2026-10-29'
  note: >-
    Read in full on 2026-10-29 from the authors' arXiv deposit
    (https://arxiv.org/pdf/cs/0006009, v1 of 2 June 2000, 47 pages),
    text extracted with pdftotext. Its first footnote says it is
    "essentially identical to the version that appears in Journal of the
    ACM 37:3, 1990, pp. 549–587", a revised and expanded version of the
    PODC '84 paper; arXiv's comment says the paper is copyrighted by ACM.
    The JACM PDF itself was not reached (dl.acm.org returned a Cloudflare
    challenge on 2026-10-29) and the PODC '84 version was not read. Read:
    §§1–14, Appendix A (the fixed-point logic) and Appendix B (temporal
    imprecision, Proposition 13, Lemma 14, Proposition 15) and the
    references. The proofs of Proposition 4, Theorem 5, Corollary 6,
    Theorem 9, Proposition 10, Proposition 13 and Lemma 14 were followed
    step by step; Theorem 11 and Theorem 12 are stated with proofs left to
    the reader and were not checked.
date: '2026-10-29'
summary: >-
  Defines distributed, someone-, everyone- and common knowledge for
  processors in a system of runs, and shows that a guaranteed coordinated
  attack makes the attack common knowledge (Proposition 4), while over a
  channel that may lose any message nothing becomes common knowledge that
  would not be common knowledge with no messages delivered (Theorem 5), so
  no correct protocol ever attacks (Corollary 6). Temporal imprecision
  alone, uncertain start times and delivery times, makes common knowledge
  unattainable (Theorem 8). Weaker fixed-point variants (ε-, eventual and
  timestamped common knowledge) are attainable in many systems.
---
<!-- inactive-ok-file: LIT-1214 — Unfetched; named as the work this paper does not cite, nothing rests on its content -->

# NOTE-tmpi6s63: Halpern and Moses — Knowledge and common knowledge in a distributed environment

## Contribution

It gives a formal semantics for what a processor, and a group of
processors, knows in a distributed system: knowledge is truth at every
point of the system the processor cannot tell apart from the present one.
With that semantics it proves that guaranteed simultaneous coordination
requires common knowledge, that common knowledge cannot be gained over an
unreliable or asynchronous channel, and that in any system with some
uncertainty about timing it cannot be gained at all. It then defines
weaker states (ε-, eventual and timestamped common knowledge) that match
weaker coordination and can be attained.

## Key insight

Common knowledge requires every member's local state to change at the
same instant (Lemma 2), because it is a fixed point that any one
member's knowledge carries for all. Each delivered message adds at most
one level of "A knows that B knows", and a message that may be lost can
be removed from a run without its sender noticing, so induction on the
number of delivered messages carries any run back to the run with none.
Simultaneity, not communication, is what is missing.

## Assumptions

- **Model (§5).** A system is a set R of runs; a point is (r, t); each
  processor's history is its initial state and the messages it has sent
  and received, with clock readings if it has a clock. Protocols are
  deterministic functions of history.
- **Knowledge (§6).** View-based: K_i φ holds at (r, t) iff φ holds at
  every point where p_i has the same view. Under such interpretations K_i,
  D_G and C_G satisfy S5 (Proposition 1, proof in a companion paper). For
  the impossibility results any "knowledge interpretation" suffices:
  beliefs that are a function of history and are never false.
- **Communication not guaranteed (§8).** NG1: from any point some run with
  the same initial configuration and clocks delivers nothing more. NG2: if
  p_i receives nothing in (t′, t), some run extending (r, t′) looks the
  same to p_i up to t while no other processor receives anything in
  [t′, t). Theorem 5's proof uses NG2 only.
- **Temporal imprecision (App. B).** For every point and processor pair,
  some run shifts one processor's history by a small δ′ in time while the
  other's is unchanged. Proposition 15: bounded but uncertain delivery
  times on open intervals plus uncertain start times imply it.

## Key results

- **Proposition 4.** In any correct coordinated-attack protocol, whenever
  the generals attack it is common knowledge that both are attacking.
  Proof: ψ ⊃ Eψ is valid in R, then the induction rule.
- **Theorem 5.** If communication is not guaranteed and |G| ≥ 2, then
  (r, t) ⊨ C_G φ iff (r⁻, t) ⊨ C_G φ, where r⁻ has the same initial
  configuration and clocks and no messages received up to t. Induction
  on the number of messages received before t, using NG2 and Lemma 3.
- **Corollary 6.** Any correct coordinated-attack protocol guarantees that
  neither party ever attacks.
- **Theorem 7.** Theorem 5 holds for unbounded delivery times even if
  delivery is guaranteed.
- **Theorem 8 (with App. B).** With temporal imprecision, (r, t) ⊨ C_G φ
  iff (r, 0) ⊨ C_G φ: no fact becomes common knowledge that was not so at
  the start.
- **Theorem 9 and Proposition 10.** Over an unreliable channel, if
  ε-common (or eventual common) knowledge of φ never holds in the run with
  no messages, it never holds in any run with the same start; so no
  protocol guarantees that if one general attacks the other eventually
  will, unless neither ever attacks.
- **Theorem 11.** Asynchronous channels cannot give ε-common knowledge.
- **Theorem 12.** Timestamped common knowledge equals common knowledge
  with identical clocks, implies ε-common knowledge with clocks within ε,
  and eventual common knowledge if every clock reaches T.
- **R2–D2 example (§8).** With delivery taking 0 or ε, each level of
  "R2 knows that D2 knows" costs ε of time, so C sent(m) is never reached;
  with delivery exactly ε, or a global clock and a timestamp, it is
  reached at t_S + ε.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Guaranteed simultaneous coordinated action makes the action common knowledge | strong | Proposition 4; checked |
| C2 | Over a channel that can lose any message, communication cannot create common knowledge | strong | Theorem 5; checked |
| C3 | Hence no protocol guarantees coordinated attack in any run where an attack occurs | strong | Corollary 6; checked |
| C4 | Not even eventually coordinated attack can be guaranteed over such a channel | strong | Proposition 10 via Theorem 9; checked |
| C5 | Uncertain start and delivery times alone make common knowledge unattainable | strong | Theorem 8, Lemma 14, Proposition 15; checked except Proposition 15's sketch |
| C6 | Practical systems coordinate by attaining ε-, eventual or timestamped common knowledge instead | moderate | §§11–12 definitions and examples; an interpretive reading of practice |
| C7 | For actions needing common knowledge, no finite level E^k suffices | strong | coordinated attack attains E^k for any k when k messages arrive, yet cannot attack |

## Concepts

- **D_G φ (distributed knowledge)**: what someone holding all of G's views
  together would know.
- **E_G φ, E_G^k φ, C_G φ**: everyone knows; k nested levels; common
  knowledge, the greatest fixed point of X ≡ E_G(φ ∧ X).
- **ε-common knowledge C^ε**: the greatest fixed point with "everyone comes
  to know within some ε-interval containing now"; corresponds to actions
  within ε of each other.
- **Eventual common knowledge C^◇**: the same with "everyone at some time
  in the run"; corresponds to eventually coordinated actions.
- **Timestamped common knowledge C^T**: everyone knows at time T on their
  own clock.
- **Internal knowledge consistency (§13)**: an interpretation that may be
  false somewhere but that no processor's history can ever refute.

## Connections

It credits the coordinated attack problem to Gray (1978) and calls the
impossibility "a folk theorem of operating systems theory", citing
Gallager (1979) and Yemini and Cohen (1979) for proofs. It does not cite
Akkoyunlu, Ekanadham and Huber (1975), [LIT-1214](../literature.d/LIT-1214.md), which the record files
as the standard first source of the same problem. The muddy children
puzzle is taken from Barwise (1981). Aumann (1976) is cited for game
theory's use of common knowledge, without development.

## Bearing on the record

- **[CLAIM-346](../claims.d/CLAIM-346.md), case 3 (epistemic coordination alone).** The claim's
  argument ("remove the last delivered message ... repeat k times") is
  the informal induction of §4 and the formal one of Theorem 5. Two
  precisions from the reading. First, the claim's demand, "both act or
  neither does", with no simultaneity, is Proposition 10's eventual case,
  not Corollary 6's simultaneous one; both hold over a lossy channel, so
  the claim's construction is covered, but the right citation is
  Proposition 10 with Theorem 9. Second, the claim cites Akkoyunlu et al.
  (1975) beside this paper; this paper's own history of the result runs
  through Gray (1978), Gallager (1979) and Yemini and Cohen (1979), so
  the 1975 attribution rests on later usage, not on this paper.
- **Theorem 8 strengthens the obstruction.** Unreliable channels are not
  needed: any uncertainty in timing blocks common knowledge, and with it
  any guaranteed simultaneous action. The record's distributed-agency
  line can use ε- or eventual common knowledge where it means
  coordination that real organizations achieve.

No instruction for machine-learning practice; nothing for the anthology.

## Limitations

- Deterministic protocols throughout; probabilistic coordination is
  mentioned (a high-probability attack is achievable) and "left to the
  reader".
- "Communication not guaranteed" is defined by two weak conditions, not
  formalized fully; the authors say so.
- Proposition 1 and the S5 properties are proved in a companion paper,
  not here. Theorems 11 and 12 carry no proofs.
- **Errors and slips.** None of substance found. The reference [DRS90]
  is given as Journal of the ACM 34(7), 1990; JACM's 1990 volume is 37,
  so the volume number at least is wrong.

## Open questions

- Which organizational actions need common knowledge, and which only
  ε- or eventual common knowledge? The paper answers for agreement
  protocols, not for the record's operators.
