---
status: Read
paper: LIT-tmptgfjj
title: 'Besley and Prat — Handcuffs for the grabbing hand'
version: 1
history:
- version: 1
  date: '2026-10-21'
  note: >-
    Read in full from the authors' working paper in LSE Research Online
    (eprint 3767; STICERD Political Economy and Public Policy Series PEPP/7,
    July 2005, the text dated 4 August 2005), text extracted with
    pdftotext. Greek letters were lost in extraction, so pages 8, 10, 29 and
    30 (the model, Proposition 1 and its proof) were also read as page
    images. Read: introduction, the baseline model with Propositions 1–2
    and Table 1, the four extensions (moral hazard, Proposition 3; entry,
    Proposition 4; endogenous monitoring, Lemma 5 and Proposition 6; access,
    Proposition 7), the conclusions, the appendix proofs, and the
    "Additional Material" on market segmentation (Propositions 8–11). The
    published AER version (2006) was not reached; the AEA's PDF link
    returned a web page. It was not compared, and proposition numbers there
    may differ.
date: '2026-10-21'
summary: >-
  A retrospective-voting model in which an incumbent can pay outlets to
  suppress verifiable bad news. Because one outlet reporting informs every
  voter, each outlet must be paid what it would earn as the only one to
  break the story, so the media are captured exactly when n·τa < r: the
  number of outlets, the transaction cost of transfers and audience revenue
  protect against capture, and the rent of office invites it. Capture ends
  turnover and lowers voter welfare without deceiving anyone: voters know
  silence is uninformative.
---
<!-- inactive-ok-file: CLAIM-tmpjo2zr CASE-tmp3uarw TERM-tmpe6jtq — Proposed, or a case filed with them; the entries filed in the same pull request that this reading bears on, cited as open -->

# NOTE-tmp01hhe: Besley and Prat — Handcuffs for the grabbing hand

## Contribution

It made media capture endogenous in a political agency model. Whether the
government silences the press is decided by a bargaining game, so the
features of the media market (how many outlets, how they are owned, how
much they earn from audiences) determine whether voters get the news, and
through that, corruption and turnover. It gives "independence" of the
media a precise sense: the difficulty, τ, of transferring resources from
the government to an outlet.

## Key insight

Plurality protects the press because news is non-rival. If one outlet
publishes, all voters learn. So silencing the press means silencing every
outlet, and each outlet's price is what it would earn as the only one to
break the story, a, not its share a/n. "If the government wants to buy out
all the media, it has to pay each of them as if it were a monopoly provider
of unbiased information." The cost of capture rises linearly in the number
of outlets while the benefit, the rent of office, does not.

## Assumptions

- **Two-period retrospective voting.** The incumbent is good with
  probability γ and gives voters 1, or bad and gives 0. A challenger is
  drawn from the same distribution. Voters do not observe their payoff
  before voting.
- **Hard news only.** If the incumbent is bad, all n outlets receive the
  same verifiable signal with probability q. "news cannot be fabricated",
  signals can only be bad, and only verifiable information is printed.
- **Audience revenue.** An outlet that reports news earns a/m when m
  outlets report it, and 0 otherwise. If at least one outlet reports, all
  voters are informed.
- **Transfers.** The incumbent sees the signal and makes simultaneous,
  private offers tᵢ ≥ 0. A transfer tᵢ costs her tᵢ and yields tᵢ/τ to the
  outlet, τ ∈ [0, ∞). She gets r − Σtᵢ if re-elected and −Σtᵢ if not.
  Footnote 7: the result survives if offers are observed by other outlets.
- **Equilibrium.** Pure-strategy perfect Bayesian equilibrium in which
  voters do not play weakly dominated strategies.

## Key results

- **Proposition 1.** If n < r/(τa), the media are captured: each outlet
  suppresses its signal for a bribe tᵢ = τa. If n ≥ r/(τa), each reports
  truthfully. The appendix proves this is the unique equilibrium of the
  class, with the incumbent indifferent at nτa = r. Re-derived in
  [THEORY-tmp6l5uw](../theory.d/THEORY-tmp6l5uw.md).
- **Consequences.** Under capture, voters' expected utility is γ in both
  periods and turnover is zero ("voters are indifferent between the
  incumbent and the challenger but they vote for the incumbent"). Without
  capture, a bad incumbent is found out with probability q, turnover is
  q(1 − γ), and second-period welfare is γ + q(1 − γ)γ. Total audience
  revenue is qa when the media are free and 0 when captured.
- **Proposition 2.** Turnover, voter welfare and audience revenue are
  non-decreasing in q, n, a and τ. q acts only when the media are free;
  n, a and τ act through whether they are.
- **Table 1, suggestive only.** In 88 countries (Djankov et al. data), high
  state ownership of newspapers goes with 7.21 more years of a chief
  executive's tenure (s.e. 1.82) and 1.24 more on the ICRG corruption
  scale (s.e. 0.26). High ownership concentration goes with 5.46 years
  (1.78) and 1.16 (0.25). "While such evidence crude and cannot be
  interpreted causally, it is encouraging that these facts are consistent
  with Propositions 1 and 2."
- **Proposition 3, moral hazard.** With rent extraction y and detection
  probability Ψ(y)q, more media activity lowers rent and raises voter
  welfare, but its effect on turnover is ambiguous. Screening raises
  turnover, while discipline makes bad incumbents harder to catch.
  Turnover must rise in q near q = 0.
- **Proposition 4, free entry at cost c.** The media are free if the
  free-entry number of outlets, ⌊qa/c⌋, exceeds the number the incumbent is
  willing to buy, ⌊r/(τa)⌋. Barriers to entry therefore invite capture.
- **Lemma 5 and Proposition 6, chosen monitoring quality.** In equilibrium
  M = ⌊r/(τa)⌋ outlets choose the same high quality q̂(1) and are
  "potentially captured". The rest form a tail with quality q̂(i)
  decreasing in rank. A bad incumbent is removed with probability
  q̂(M + 1). Turnover and welfare rise with a and τ. The authors read the
  steep vertical differentiation of the US and UK press as a sign of a
  press "working for the audience rather than for the government".
- **Proposition 7, access instead of money.** If the government can only
  grant interviews worth Φ(m̂) to each of m̂ favoured outlets, with Φ
  decreasing, the media are captured iff Φ(n) > a.
- **Propositions 8–11, segmented audiences.** When a share 1 − φ of
  viewers read only their own outlet, the incumbent needs to silence only
  enough outlets to keep half the voters uninformed. The cost of capture
  rises in φ, τᵢ and aᵢ. It is strictly increasing in n when φ ≥ 1/2. For
  φ < 1/2 it is non-decreasing in n only once integer effects are set
  aside.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | In the baseline model the media are captured iff nτa < r, with each outlet paid τa | strong | Proposition 1 and its proof; re-derived in [THEORY-tmp6l5uw](../theory.d/THEORY-tmp6l5uw.md) |
| C2 | Capture lowers turnover and voter welfare | strong in the model | Propositions 1–2; with moral hazard, welfare holds and turnover becomes ambiguous (Proposition 3) |
| C3 | Plurality, high transaction costs (independent, dispersed or foreign ownership) and commercial audience revenue protect against capture | strong in the model, as comparative statics | Propositions 2, 4, 6, 7, 9 and 10 |
| C4 | State ownership and concentration of newspapers go with longer tenure and more corruption across countries | weak | Table 1, raw differences in means, "cannot be interpreted causally" |
| C5 | Formal press freedom is no guarantee of a press free from political interference | moderate | the model's equilibrium capture under no censorship; illustrated by Russia, Peru, Italy |

## Concepts

- **Captured**: "In situations where the media receives a transfer in
  exchange for silence we say that the media is captured, referring
  otherwise to the media being independent." A transaction, not a
  disposition.
- **Transaction cost τ**: how hard it is for the incumbent to move value to
  an outlet. Lowest for state-owned media, higher for widely held, foreign
  or independently owned media.
- **Commercial motive a**: the most an outlet can earn from audiences by
  reporting news.
- **Screening and discipline effects** of media activity, in the moral
  hazard extension.

## Connections

It builds on the agency models of Barro (1973) and Ferejohn (1986). It cites
McMillan and Zoido on Montesinos's payments to Peruvian media, Djankov et
al. on state ownership, and Gentzkow and Shapiro, Mullainathan and Shleifer
and Baron for media bias from sources other than capture. The record's
readings of Di Tella and Franceschelli ([LIT-tmpa8ani](../literature.d/LIT-tmpa8ani.md)) and Szeidl and
Szucs ([LIT-tmp6b6sj](../literature.d/LIT-tmp6b6sj.md)) take it as their model. Szeidl and Szucs equate their
δ, the government's ability to reward slant, with τ.

## Bearing on the record

- **[CLAIM-tmpjo2zr](../claims.d/CLAIM-tmpjo2zr.md), evidence route.** The model is a clean case of an
  evaluator governed through its evidence alone. The voters' decision rule
  is correct Bayesian updating throughout, and nothing is decided for them.
  Capture removes the evidence they would update on. In the captured
  equilibrium voters are not deceived: they know silence means nothing, and
  their posterior stays at the prior γ. That separates the evidence route
  from persuasion ([THEORY-404](../theory.d/THEORY-404.md)), where a receiver who knows the design is
  moved. Here the receiver is not moved; it is left at its prior, which is
  enough for the incumbent, since the tie goes to her.
- **[CLAIM-tmpjo2zr](../claims.d/CLAIM-tmpjo2zr.md), the loop between institutions.** The model has the
  press-as-evaluator structure of the claim's third part, with the
  evaluated party able to affect the evaluator's resources. But it is
  static. Capture is decided once by comparing nτa with r, and nothing
  feeds back from the outcome to the next period's n, τ, a or r, so it
  contains no amplification loop. The record's loop condition
  ([CLAIM-330](../claims.d/CLAIM-330.md)) has no counterpart here. The model supports the claim that
  formal independence (no censorship) does not make the evaluation
  independent. It does not support the claim's dynamic part.
- **[CASE-tmp3uarw](../cases.d/CASE-tmp3uarw.md), press variant.** The variant's "a newsroom whose
  conditions of production the evaluated party's decisions affect" is this
  model's outlet, with transfers as the channel. The case's sentence that
  Besley and Prat rest on an unread work can now be replaced: the model is
  read, it is static, and its mechanism is purchase of silence, not a drift
  in how the newsroom reads evidence.
- **[TERM-tmpe6jtq](../terms.d/TERM-tmpe6jtq.md).** Besley and Prat's "captured" is the purpose-relative,
  transactional sense the term set aside ("a decision bought outright is
  captured in it"). It is a single bargain, not a durable regime reproduced
  through the outlet's own processes, and it needs no outside standard,
  since suppression of a true verifiable signal is defined in the model. If
  the owner adopts the term as drafted, this paper's capture falls outside
  it. That is a reason to file the institutional sense as a narrower term,
  as the term's own body suggests.

No instruction for machine-learning practice; nothing for the anthology.

## Limitations

- **Hard, homogeneous news.** All outlets hold the same verifiable signal,
  which only a bad type generates. With soft news the authors expect a
  reputation game they do not solve. Di Tella and Franceschelli argue that
  with non-verifiable news partial bribing can pay, which the model rules
  out.
- **Indifferent voters.** In the captured equilibrium the posterior after
  silence equals the challenger's, so voters are exactly indifferent. That
  they re-elect is forced by the pure-strategy restriction (fn. 9). A
  mixed equilibrium with random voting exists and is called "analogous".
- **Static.** No dynamics of capture, entrenchment or reputation.
- **A notational slip in the working paper.** The appendix proof says an
  outlet "accepts tᵢ > a and rejects tᵢ < a", while the strategies and the
  proposition use τa. The conclusion, nτa against r, is consistent with
  τa. The published version was not checked.
- **Evidence.** Table 1 is raw differences in means across 88 countries.

## Open questions

- With soft or heterogeneous news, can an incumbent profitably buy some
  outlets and not others? That would break the all-or-nothing logic that
  makes plurality protective.
- What happens when capture today changes tomorrow's n, a or τ, for
  example by bankrupting critics or favouring friendly entrants? That is
  the dynamic the record's claim needs and the model omits. Szeidl and
  Szucs's endogenous ownership is one version.
