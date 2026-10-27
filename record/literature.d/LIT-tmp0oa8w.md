---
status: Active
status_note: >-
  read 2026-10-27 (NOTE-tmp2597d) in full, from the authors' own copy
  of the ICML paper; worth reading for the beam sampler, which adds a
  uniform slice variable under each transition so that only finitely many
  state trajectories of the infinite HMM have positive probability, and
  then samples a whole trajectory exactly by forward filtering, backward
  sampling (THEORY-tmp7bmmi). The infinite factorial HMM's inference is
  built on it. Read it knowing that its case for faster mixing than Gibbs
  sampling rests on charts, synthetic data and one changepoint series
  judged by eye (THEORY-tmptl00j), and that one of its fixed
  hyperparameter settings was chosen from the samplers' own results.
title: 'Beam Sampling for the Infinite Hidden Markov Model'
version: 2
history:
- version: 1
  date: '2026-10-27'
  note: >-
    Filed, not read, at the owner's request of 2026-10-27 ("file the next
    readings"): the curation entry of 2026-10-27 02:06 lists it among the
    works the infinite factorial HMM names, and NOTE-1199 says the
    infinite factorial HMM's inference "follows the beam sampler for the
    infinite HMM". Checked on 2026-10-27 against Crossref and the PDF's
    header and footer: Jurgen Van Gael, Yunus Saatci, Yee Whye Teh and
    Zoubin Ghahramani, "Beam sampling for the infinite hidden Markov
    model", Proceedings of the 25th International Conference on Machine
    Learning (ICML '08), Helsinki, pp. 1088–1095, doi:10.1145/1390156.1390293.
    Crossref gives the year only (published-print and issued 2008) and the
    conference's dates as 5–9 July 2008, so `published:` is 2008-07-01,
    month precision (ADR-002; the earlier of the month and the opening
    day). It has no arXiv deposit. The summary follows the abstract.
- version: 2
  date: '2026-10-27'
  note: >-
    Read in full (NOTE-tmp2597d): §§1–6, the figure captions, the
    footnotes and the references, from the authors' PDF on the Cambridge
    Machine Learning Group's server, which is the ICML paper with its
    proceedings footer. Status Deferred → Active. THEORY-tmp7bmmi (Active)
    and THEORY-tmptl00j (Proposed) filed. The summary is checked against
    the reading and given the method's form.
tags:
- probabilistic-modeling
- mathematical-statistics
date: '2026-10-27'
published: '2008-07-01'
doi: '10.1145/1390156.1390293'
url: 'https://mlg.eng.cam.ac.uk/pub/pdf/VanSaaTehGha08.pdf'
first_author: 'Van Gael'
keywords:
- 'beam sampling'
- 'infinite hidden Markov model'
- 'HDP-HMM'
- 'slice sampling'
- 'forward filtering backward sampling'
implementations: []
summary: >-
  Van Gael, Saatci, Teh & Ghahramani (2008), ICML '08: 1088–1095. For the
  infinite hidden Markov model (the HDP-HMM), an auxiliary variable
  u_t ~ Uniform(0, π_{s_{t−1}s_t}) per time step leaves only finitely
  many trajectories with positive probability, so a whole state sequence
  can be resampled by dynamic programming without truncation. On
  synthetic data, a well-log changepoint series and character prediction
  in Alice in Wonderland, the beam sampler mixes in fewer iterations and
  is less sensitive to initialization and priors than the Gibbs sampler,
  at a cost per iteration close to O(TK) in practice.
---
<!-- inactive-ok-file: THEORY-tmptl00j — Proposed; the sampler comparison filed from this reading, cited as open -->

# LIT-tmp0oa8w: Beam Sampling for the Infinite Hidden Markov Model

Van Gael, J., Saatci, Y., Teh, Y. W. & Ghahramani, Z. (2008). Beam
sampling for the infinite hidden Markov model. In *Proceedings of the 25th
International Conference on Machine Learning* (ICML '08), pp. 1088–1095.
ACM. doi:10.1145/1390156.1390293.

Read in full on 2026-10-27 (NOTE-tmp2597d). Two accounts were drawn from
it: THEORY-tmp7bmmi and THEORY-tmptl00j.

## Why this is here

The owner asked on 2026-10-27 to "file the next readings". The infinite
factorial HMM (LIT-1577) samples each of its binary chains with a slice
variable and forward filtering, backward sampling, the scheme introduced
here for the infinite HMM. The record held the Markov IBP's prior and not
the inference that makes it usable; any fitting of a dynamic feature
model such as CASE-165's would need a sampler of this kind for its
per-feature chains.
