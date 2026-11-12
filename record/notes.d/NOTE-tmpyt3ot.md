---
status: Read
paper: LIT-tmpq8pi2
title: 'Freer and Nosratabadi (2022) — Revealed preference analysis under limited attention'
version: 1
history:
- version: 1
  date: '2026-11-12'
  note: >-
    Read on 2026-11-12 for the reading pass the owner asked for ("read the
    works you can reach"), from a reader's draft the filer verified against
    the downloaded text. Copy and extent: - Read:
    https://arxiv.org/pdf/2208.07659 (PDF, arXiv:2208.07659v3 [econ.TH], 13
    Oct 2023; title page dated October 16, 2023), text from pdftotext,
    2026-11-12. I read §§1–5 in full. I skipped the appendix proofs and the
    incomplete-data MIP construction in §3.2 beyond its opening. - arXiv
    API: first version 2022-08-16, last update 2023-10-13. No later arXiv
    version. The JEBO text may differ from v3. Outcome as the reader gave
    it: **Read**, from the authors' arXiv preprint (v3). The journal version
    of record (JEBO 246: 107568) was not read.
date: '2026-11-12'
summary: >-
  An observer wants to recover a decision-maker's welfare from her choices
  under limited attention. The standard choice-under-limited-attention model
  (Masatlioglu et al. 2012, "generic CLA") recovers almost nothing. Every
  choice set consistent with rationality can be read as the decision-maker
  attending only to what she chose. The authors add an "attention floor":
  the k-th order CLA, where she considers at least min(|B|, k) alternatives,
  which is equivalent to making at least k−1 comparisons. They characterize
  it on complete data (SARP_k plus WARP(LA_k), Theorem 1) and give a MIP
  test for incomplete data. They give an algorithm that recovers the
  revealed preference relation P*, the comparisons common to every
  rationalizing (preference, attention filter) pair. It handles "or"
  information. They apply it to Inoue and Shirai's (2018)
  intertemporal-bundle experiment (113 subjects, 10 alternatives, 20
  budgets).
---

# NOTE-tmpyt3ot: Freer and Nosratabadi (2022) — Revealed preference analysis under limited attention

## Contribution

It shows that welfare relevance under limited attention depends almost entirely on a minimal attention assumption, and that the assumption costs nearly nothing descriptively.

## Key results

- §1: under generic CLA, "We can not recover any preferences for 63% of the subjects in the standard model" (abstract), while the floor-2 model "reveals some preferences for all subjects".
- §1: the floor-2 model "allows us to recover one-third of the preferences that would be recovered under full attention" (abstract).
- §4.1, Table 2: pass rates are 1 (k=1), .99 (k=2) and .34 (k=8). The power of the test against random choice drops from .88–.96 to .35–.46 at k=2.
- §4.2: "if DM makes at least one comparison, then the theory is already powerful enough to recover 20% of potential comparison on average".
- §1: the rationale for the floor is that the minimal-attention reading "essentially, removes the act of comparison from the decision process".
- §5: two-stage models generate "or-logic", meaning revealed preferences of the form "x is better than y or z is better than w".

## Assumptions

A rational strict preference. Attention filters (removing an unattended item does not change choice). A uniform floor k across menus. Welfare is identified with that preference (model-based, not Bernheim–Rangel model-free). Lab data, one data set.

## Concepts

Attention filter; k-th order CLA; attention floor; revealed preference relation P* as the intersection over representations; multi-representation; descriptive power versus welfare relevance; predictive success index.

## Bearing on the record

**On the LIT's and the exchange's characterization.** A's summary ("tests whether limited-attention models help recover preferences from choices over restricted consideration sets") is broadly right but undersells the result. The paper's point is that the standard model does not help, and that a minimal comparison assumption restores much of the recovery.

- **[QUESTION-tmpuftum](../questions.d/QUESTION-tmpuftum.md)** (item 2, inferred demands): supports and sharpens it. What an observer can infer from behaviour depends on an assumption about attention that the behaviour cannot itself fix. Under the weakest assumption almost nothing is inferred, and the inferred relation is model-relative. This gives formal content to "behavioral observations are evidence about a demand, not automatically the demand itself". It does not address who fixes the attention set, so selective exposure shaped by an organization is left open.

- "limited attention", "consideration set" and "attention filter": nothing held. Not a duplicate: arXiv 2208.07659 and the DOI are found nowhere in record/.
- "revealed preference": [CLAIM-482](../claims.d/CLAIM-482.md) (an organization's aggregate revealed preference exists when winning moves never cycle and is fitted to one regime of authority) is a parallel. The preference revealed is relative to the model of the choosing process. [LIT-2096](../literature.d/LIT-2096.md) ("Rational Inefficiencies") and [NOTE-949](NOTE-949.md) (Slovic, the construction of preference) are also neighbours worth linking.

## Limitations

One lab data set. The floor is assumed, not observed. The proofs and the JEBO revisions were not read.
