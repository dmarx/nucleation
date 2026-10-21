---
status: Read
paper: LIT-tmpx95z2
title: 'Weatherall, O''Connor and Bruner — How to beat science and influence people'
version: 1
history:
- version: 1
  date: '2026-10-21'
  note: >-
    Read in full from arXiv:1801.01239v2 (20 August 2018), the authors'
    manuscript headed "Draft of August 21, 2018" and "PLEASE CITE THE
    PUBLISHED VERSION IF AVAILABLE!", text extracted with pdftotext. Read:
    the abstract, §§1–6, the footnotes and Appendix A's semi-analytic
    treatment. The figures were read from their captions and the text;
    their plotted values were not seen. The Greek ε was lost in extraction
    throughout (".5+." for .5 + ε) and is restored from context. Not
    compared with the BJPS version of 2020. The selective-sharing results
    were re-run in a re-implementation from the paper's description
    (THEORY-tmpnq01l), and the biased-production result re-derived
    (THEORY-tmpg79sv).
date: '2026-10-21'
summary: >-
  In Bala–Goyal network models with Bayesian policy makers who do not
  gather evidence, a propagandist who forwards only the real results of
  unbiased scientists that happen to favour the worse action, or who runs
  honest studies and publishes only the unfavourable ones, can leave policy
  makers near-certain of the false theory while the scientists converge on
  the true one. It works best when the problem is hard, studies are small,
  scientists are many and policy makers hear few of them. A journalist who
  reports one result for each side every round slows policy makers' learning
  and never helps it.
---
<!-- inactive-ok-file: CLAIM-tmpjo2zr CLAIM-342 THEORY-143 THEORY-146 THEORY-148 — Proposed; open claims and accounts this reading bears on, nothing here rests on them -->
<!-- inactive-ok-file: LIT-751 — Unavailable; the Holman–Bruner paper this one describes, cited as unread -->

# NOTE-tmp8rwaa: Weatherall, O'Connor and Bruner — How to beat science and influence people

## Contribution

It models the two prongs of the tobacco industry's strategy as Oreskes and
Conway describe it, "selective sharing" and "biased production", in an
epistemic network with a separate audience of policy makers, and shows that
neither prong needs fraud or biased methods to mislead the audience while
the scientists themselves get it right. It adds a non-malicious analogue,
"fair" journalism, and a semi-analytic account of the outcome as a
tug-of-war between science and propaganda.

## Key insight

What a Bayesian audience learns depends on the statistics of the evidence
it sees, not on whether each item is genuine. "The fact that each result
that is shared is, in some sense, 'real' ends up being irrelevant, because
it is the statistical properties of the total available evidence that
matter." An honest community working on a hard problem produces, by
chance, a steady supply of results that favour the wrong answer, and
whoever chooses which of them reach the audience controls what it
concludes.

## Assumptions

- **Inquiry:** a two-armed bandit. Action A succeeds with probability .5,
  known; B with .5 + ε (true) or .5 − ε, unknown. Scientists with credence
  above .5 in B play B, n times a round, and update by Bayes on their own
  and their network neighbours' results. Networks are cycles or complete
  graphs of K scientists.
- **Policy makers** gather no evidence, have initial credences uniform on
  (0, .5), listen to k scientists, and influence no one. They update by
  Bayes on everything they receive, treating each result as an unselected
  draw; they do not model the propagandist's selection.
- **Propagandist:** sees every scientist's result and reaches every policy
  maker. Under selective sharing it forwards the round's results that favour
  A, so that a policy maker may count a result twice (the authors also ran a
  version without double counting: "qualitatively similar" and weaker).
  Under biased production it spends its own pulls on B in studies of a
  chosen size and publishes only those favouring A.
- **Stopping and averaging:** a run stops when every scientist prefers A or
  every scientist's credence exceeds .99; results are averaged over runs in
  which the scientists reached the correct consensus (footnote 12, which
  says this dropped at most 10% of runs).
- Parameters (footnotes 11 and 24): K from 4 to 50, n from 1 to 1000, p_B
  from .51 to .7, k from 1 to all.

## Key results

- **Selective sharing (§3).** "under many scenarios we find that while the
  community of scientists converges on true beliefs about the world, the
  policy makers reach near certainty in the false belief." Policy makers
  are harder to deceive when they listen to more scientists (Fig. 2: cycle,
  K = 20, n = 10, p_B = .55), when ε is larger (Fig. 3), and when n is larger
  (Fig. 4: complete, K = 10, k = 9, p_B = .55; "For high enough n, the
  propagandist can do almost nothing"). With k fixed, more scientists
  "increases the total number of spurious results that the propagandist can
  then share with policy makers, often worsening policy maker belief".
- **Convergence time (§3, Fig. 5).** When the propagandist is winning on
  average, slow scientific consensus helps it; with p_B = .55 and n = 5 the
  complete network was better for policy makers, with p_B = .7 and n = 20 the
  cycle. "at least in some cases, maximizing convergence time is truth
  conducive for the scientists, but not for the public."
- **Biased production (§4).** More propagandist resources mislead more (Fig.
  6), and for fixed resources "it is always better for them to break their
  data up into the smallest possible chunks" (Fig. 7). Here, unlike under
  selective sharing, more scientists help the policy makers without
  exception.
- **Fair reporting (§5).** A journalist who shares one result favouring each
  theory every round, against one who shares two random results or all of
  them: "the Fairness Doctrine never improves the epistemic performance of
  the policy makers", and policy makers still tend to the truth whenever the
  scientists do, "but they do so much more slowly" (Fig. 9).
- **Appendix A.** B_{t+1} ≈ Y_P × Y_S × B_t, with
  Y_S = (1/(B_t + (1 − B_t)X))^{rk} and X = ((1 − 2ε)/(1 + 2ε))^{2nε}, r the
  fraction of scientists playing B, so Y_S > 1; and
  Y_P = (1/(B_t + (1 − B_t)X̃))^{rz}, z = P(x < n/2) × K the rate of spurious
  results, with X̃ = ((1 − 2ε)/(1 + 2ε))^{2Ẽ−n} built from the expected spurious
  result Ẽ < n/2, so X̃ > 1 and Y_P < 1. A linear fit Ẽ ≈ −.62 + .47n for small
  ε gives the exponent −.06n − 1.24.
- **Conclusion (§6).** Selective sharing is often more effective than
  biased production, "particularly when the scientific community is large
  and the problem at hand is difficult", and combines with Holman and
  Bruner's industrial selection. Remedies named: hearing more scientists,
  detecting propagandists statistically, adjusting the update for filtered
  evidence, and rewarding fewer, higher-powered studies.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Forwarding only real, unbiased results that favour the worse theory can drive a Bayesian audience to the false theory while the scientists converge on the true one | strong, within the model | simulations of §3 (Figs 2–5), averaged over 1,000 runs per setting; re-run here (THEORY-tmpnq01l) |
| C2 | The effect weakens with more scientists heard, larger ε and larger n, and with k fixed can strengthen with more scientists | strong, within the model | Figs 2–4 and the text; the last "not always" (footnote 19) |
| C3 | Under biased production the smallest studies serve the propagandist best | strong | Fig. 7; re-derived pathwise here (THEORY-tmpg79sv) |
| C4 | "Fair" reporting slows the audience's learning and never improves it | moderate | Fig. 9 over a representative set of parameters (footnote 29) |
| C5 | Selective sharing is often more effective than biased production | moderate | comparison of §3 and §4 in the conclusion, with cost and risk arguments that are outside the model |
| C6 | The Tobacco Strategy was an important causal factor in the delay of tobacco regulation | weak from the model | the model with Oreskes and Conway's history; the authors call the model "how-potentially" and say "modeling alone cannot establish that this did happen" |

## Concepts

- **Selective sharing:** promoting independently produced results that
  happen to favour one's position.
- **Biased production:** funding research and publishing only the results
  that favour one's position, without falsifying any.
- **Spurious result:** a study of B with fewer than n/2 successes, which
  favours A though B is better.
- **Policy maker:** an agent that updates on received evidence and gathers
  none.

## Connections

It extends Bala and Goyal (1998) and Zollman (2007; LIT-724) with an
audience, and contrasts itself with Holman and Bruner's intransigently
biased agent (2015; LIT-751, Unavailable), who "draws from a biased arm
relative to the other scientists" and acts on the scientists, not on an
audience. It points forward to Holman and Bruner's industrial selection
(2017; LIT-744), and cites Rosenstock, Bruner and O'Connor (LIT-733) for the
scope of the Zollman effect and O'Connor and Weatherall on polarization.

## Bearing on the record

- **CLAIM-tmpjo2zr.** It is the network-epistemology prior art for the
  claim's evidence route, and adds a third form beside THEORY-404 and
  THEORY-146. In THEORY-404 the receiver knows the sender's committed design
  and is still moved; in THEORY-146 funding changes which producers prosper;
  here every result is genuine and honestly produced, and the audience is
  moved because it updates on a selected sample as if it were not selected.
  So the claim's phrase "even if the regulator reasons correctly on the
  evidence it receives" holds here only in the sense that the policy makers
  apply Bayes' rule to the items received; the authors themselves name an
  update that models the filtering as a possible remedy. §5's fair journalist
  supports the claim's caveat that "ordinary editorial selection is
  unavoidable": a curator with no aim of misleading reproduces part of the
  propagandist's effect. The paper's audience does not feed back on the
  scientists, so it has nothing of the claim's interpretation–authority loop
  between institutions.
- **CLAIM-330.** A25's positioning, "alongside—not as a replacement for",
  fits: this paper's dynamics are an open-loop tug-of-war (Y_P × Y_S), with no
  coupling from the audience back to the evidence, which is what CLAIM-330's
  instability needs.
- **THEORY-143 and THEORY-148.** The Zollman effect concerns the community's
  own learning. With an outside audience and a propagandist, the slow
  consensus that sparse networks give can leave the audience worse off (Fig.
  5), and footnote 14 reports Holman and Bruner's finding that with a biased
  agent among the scientists it is best for them to be highly connected.
  THEORY-143's scope should say so; a candidate wording is in the batch
  report.
- **LIT-751.** This paper's footnotes 14, 18 and 23 describe that unread
  model: the biased agent draws from a biased arm and shares with
  scientists; high connectivity helps; and scientists who can ignore
  statistically unlikely data do better when n is large, because the biased
  agent is easier to detect. These are Weatherall et al.'s reports, not a
  reading.
- **CLAIM-342.** Hearing more scientists is the paper's main remedy: evidence
  that arrives without passing through the propagandist. That is
  CLAIM-342's anchor for a loop that selects its own evidence, in a case
  with no loop.
- **QUESTION-047.** The audience settles on a belief none of the scientists
  holds, through selection of their own outputs: a community-level mechanism
  of the kind the question asks for, with the community split into producers
  and an audience.

No instruction for machine-learning practice; nothing for the anthology.

## Limitations

- **Simulation only,** with a stylized bandit and a two-point hypothesis
  space. The authors call it "how-potentially" and say the model cannot
  establish the historical claim (C6).
- **Selection is invisible to the audience by assumption.** A policy maker
  that modelled the propagandist would discount its results; the authors
  name this and leave it to future work.
- **Averaging over successful runs** (footnote 12) conditions every figure
  on the scientists' converging to the truth.
- **Double counting** strengthens selective sharing; the version without it
  was run and only described.
- **Appendix A's sign slip.** It says "(2Ẽ − n) < 1, so X̃ > 1"; what makes
  X̃ > 1, with base (1 − 2ε)/(1 + 2ε) < 1, is 2Ẽ − n < 0, which Ẽ < n/2 gives.
  The appendix's product Y_P × Y_S treats sequential updates as independent
  factors, an approximation the authors flag for slowly changing B.
- **C5's cost and risk arguments** (industry science "can cost a great deal
  to produce ... and ultimately be disqualified") are outside the model.

## Open questions

- How much of the effect survives policy makers who know a propagandist is
  present and discount its results, or who weigh sources by their statistical
  track record?
- With feedback from the audience to the scientists' funding or attention,
  does the open-loop tug-of-war become CLAIM-330's kind of instability?
