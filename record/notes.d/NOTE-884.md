---
number: 884
status: Read
formerly:
- NOTE-tmpvgf21
paper: LIT-1069
title: Jones — Scaling scaling laws with board games
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: >-
    Read in full 2026-10-15 from the author's arXiv preprint, version 2 (the latest;
    v2 submitted 2021-04-15, v1 2021-04-07), fetched as https://arxiv.org/pdf/2104.03113v2
    (8 pp., IEEE two-column, with Appendices A–D). Text extracted with pdftotext,
    in raw and layout modes; the layout mode was used to read Tables I–IV, whose
    columns the raw mode scrambles, and the axis labels of Figs. 8 and 9 were read
    from the extraction, not from page images. Read: abstract, all five sections,
    all four appendices and the reference list; nothing skipped. v1 (https://arxiv.org/pdf/2104.03113v1)
    was also fetched and diffed word by word against v2: v2 changes the abstract's
    last sentence, adds related work (Hilton et al., Hernandez et al., pruning)
    and renumbers references; the methods, tables, figures and the train–test numbers
    are the same in both. Every quotation of the paper below was checked against
    the v2 extracted text by script, with whitespace normalised; one, where the
    extraction joins "test-time" across a line break as "testtime", matched with
    hyphens ignored. Quoted phrases from the record (the LIT entry, the QUESTION)
    were checked against those files.
date: '2026-10-15'
summary: >-
  Training AlphaZero on Hex at board sizes 3×3 to 9×9, the best Elo reachable for
  a given training compute follows one change-point curve across sizes: an incline
  of about 500 Elo per tenfold of training compute, with the compute for perfect
  play rising about 7× and the compute to leave random play about 4× per added board
  row, and fits on small boards predicting larger ones. On 9×9 only, train-time
  and test-time (tree-search) compute substitute at a fixed rate: at equal Elo,
  each 10× of train-time compute removes about 15× of test-time compute (fit: log
  test = −1.2·log train + 0.004·Elo + 29), down to a one-node search, over roughly
  1e14–1e16 FLOPS-seconds of training. The trade is an iso-performance curve for
  a single search; the paper never counts how many games or moves the trained agent
  will play, so it does not price amortization, and it does not state the unit of
  test-time compute. One game, small boards, Elo anchored to a perfect player, and
  no uncertainty on the fitted trade-off coefficients.
---
<!-- inactive-ok-file: CLAIM-295 — Proposed; open claims and accounts cited as open, nothing here rests on their being settled -->

# NOTE-884: Jones — Scaling scaling laws with board games

## Contribution

Scaling laws had been fitted in model size, data and compute with the problem held fixed. Jones scales the problem too: Hex boards from 3×3 to 9×9, about 200 AlphaZero models and 2,800 snapshots, rated by Elo with perfect play (MoHex) fixed at zero. The frontier of best Elo against training compute has the same shape at every size, and a fit to small boards predicts larger ones. As a side result, "suggested" by Jared Kaplan, it measures how train-time compute and test-time search compute substitute at equal performance.

## Key insight

The frontier is a parallel family: the same incline, shifted by a fixed factor of compute per board row, so problem size enters the law as a single additive term in log compute. And at a fixed performance level, compute spent in training and compute spent in search at play time are interchangeable along a straight line in log–log space. The author's account of why the rate is near one-for-one rather than steeply favouring search: "an optimization at test-time needs only optimise over one sample, while train-time compute meanwhile must optimise over the entire distribution of samples."

## Assumptions

- **One game, small boards.** Hex without the pie rule, sizes 3 to 9; 9×9 is the largest MoHex plays perfectly. Each evaluation pair plays black and white equally.
- **Compute is training FLOPS-seconds**, varied along three axes only: network depth, width (1 layer of 1 neuron to 8 of 1024, in powers of 2, capped per board size, Table II), and run length. Other hyperparameters fixed (Table I): 32k environments, batch 32k, buffer 2m samples, learning rate 1e-3, MCTS 64 nodes, c_puct 1/16.
- **Search size 64 nodes in training and in all main-result evaluation.** Only the train–test section varies test-time tree size, from 1 to 512 nodes.
- **Elo assumes transitivity.** League evaluation, 1,024 matches per pair of snapshots; Appendix B repeats the analysis against a single top agent (64k games each) and gets the same form with noisier, somewhat different parameters (Table IV).
- **A five-parameter change-point model**, chosen over linear (bad at the ends) and sigmoid (equally good MSE, harder to read) forms: plateau = m_boardsize·boardsize + c; incline = m_boardsize·boardsize + m_flops·log flop + c (separate coefficients); elo = incline.clamp(plateau, 0). Fitted with L-BFGS. The logarithm's base is not stated; the derived quantities make sense only for base 10.
- **A nonstandard AlphaZero** (Appendix A): small fully connected residual nets, all-GPU environment and search, regularized tree search after Grill et al. with a Newton step, large batches, a small replay buffer. The author does not claim it matches a conventional implementation; the check is that the best agents draw MoHex.
- **The train–test trade-off is measured on 9×9 snapshots only**, with Elo on the same perfect-play scale.

## Key results

- **Frontier parameters (Table III, league evaluation).** Plateau: m_boardsize −270, c 570. Incline: m_flops 510, m_boardsize −430, c −4400. (Top-agent evaluation, Table IV: plateau −330, 820; incline 600, −590, −4700.)
- **Derived quantities (§IV-A), as stated:**
  - "The slope of the incline is 500 Elo per order of magnitude increase in compute"; "you will need about 2× as much compute as your opponent to beat them 2/3 of the time."
  - "The minimum compute needed for perfect play increases 7× for each increment in board size."
  - "The minimum training compute needed to see any improvement over random play increases by 4× for each increment of board size."
  - "the distance between random play and perfect play increases by 500 Elo for each increment of board size", a property of the game, not the agent. About 2,000 Elo separates random from perfect play on 9×9.
- **Training time.** Perfect play on 9×9 takes "a little under 3 hours on a single RTX 2080 Ti"; time to reach −50 Elo is roughly exponential in board size (Fig. 3). Per-size compute caps (Table II) run from 1E+12 (3×3) to 1E+17 FLOPS-seconds (9×9). About 500 GPU-hours of training and 100 of evaluation in all.
- **Extrapolation (§IV-B, Fig. 7).** Frontiers fitted on boards up to size k predict larger boards; "The error in the predicted frontier (as measured by the residual variance) starts small and decays exponentially as more small boards are added to the fit." Residual variance falls from about 0.1 to about 0.003 on the figure's axis; no table of these errors is given.
- **Test-time compute alone (Fig. 8).** For a fixed 9×9 snapshot, Elo is sigmoid in test-time compute as the tree grows from 1 to 512 nodes; "larger tree searches at test time can substantially improve the performance of an agent."
- **The exchange rate (§IV-C, Fig. 9).** "the trade-off is linear in log-compute: for each additional 10× of train-time compute, about 15× of test-time compute can be eliminated, down to a floor of a single-node tree search." The fitted line printed on Fig. 9 is log(test) = −1.2·log(train) + 0.004·elo + 29. With base 10, a slope of −1.2 is 10^1.2 ≈ 16× less search per 10× more training, matching "about 15×"; in the introduction this is rounded to "a similar factor". Range: Fig. 9's axes run over train-time compute of about 1e14 to 1e16 FLOPS-seconds and test-time compute of about 1e6 to 1e9, for iso-Elo contours from −1500 to −250 (perfect play is 0). Each contour is "the minimum train-test compute required for a certain Elo on a 9 × 9 board". The floor ends the trade: below a one-node search no further training can replace search.
- **What the same fit implies (my arithmetic, not stated in the paper).** Holding training fixed, 10× more test-time compute buys 250 Elo (1/0.004). Holding test-time compute fixed, 10× more training buys 300 Elo (1.2/0.004), less than the 500 Elo per decade of the training frontier at a fixed 64-node search; the paper does not reconcile the two fits. No standard errors or confidence intervals are given for −1.2, 0.004 or 29.
- **Discussion.** The 2×-compute, 2/3-win regularity matches a toy model in which each player draws as many random numbers as it has compute and the highest wins; the author calls this possibly "serendipity". Performance is smooth in compute and board size, with no "spikes", which "could plausibly be a property unique to Hex". The author expected test-time compute to be "much ‘cheaper’ than train-time compute" and was "surprised that one could easily substitute for the other".

## Bearing on the record

**On [QUESTION-095](../questions.d/QUESTION-095.md): a measured exchange rate between work done before the request and work done at it, at fixed quality, with no term for reuse.**

- **What it supplies.** Training is the first strategy in the question's table, precompute and leave a result, with the result left in the weights; tree search at play time is work done when the request comes. Jones gives the iso-performance substitution between the two, about 15× (fitted 10^1.2 ≈ 16×) less search per 10× more training, over about two decades of training compute on one board, down to a one-node floor. That is a measured price for the computational part of the trade ([CLAIM-295](../claims.d/CLAIM-295.md)'s second component), which none of the cognitive readings attached to the question supplies.
- **What it does not supply: expected reuse.** The paper compares a one-off training budget with test-time compute without saying how many games or moves the trained agent will play, and does not say whether its test-time FLOPS-seconds are per move, per game or per evaluation. The magnitudes (1e6–1e9 against a forward pass of about 5e5 FLOPS-seconds for the 2×512 net in Appendix A) suggest per search, but that is inference. The phrase "amortized" does not occur. The LIT entry's framing, "compute spent once in training is amortized over every later query", is the record's reading; the paper's own explanation is the closest it comes: test-time search optimises "over one sample", training "over the entire distribution of samples". So the question's "expected reuse" term has to be added from outside: with N searches, total cost at fixed Elo is train + N·k·train^−1.2 on Jones's fit, and the cheapest training budget grows with N (my derivation, not the paper's). The paper does not make the trade a function of N; it gives the curve a reuse count would be applied to.
- **Query predictability.** Implicit and favourable: training and test draw positions from the same game, at the same board size, so the trained policy is never asked a question outside the distribution it was trained for. Nothing measures what happens when the later query shifts, which is the regime the question's Ballard case (input that cannot be precomputed) represents.
- **Retrieval cost.** Not separated. A one-node search is a single forward pass, so retrieval from the precomputed store is the floor of test-time compute; the paper treats it as the irreducible cost, not as a term to be traded.
- **Staleness and bias.** Not measured. Elo at fixed compute is the only quality term, and the trade is defined at equal Elo, so any systematic error the trained policy carries is folded into its rating. The paper's one mention of "staleness" is about replay-buffer samples during training (Appendix A), not about reused results.
- **Erosion of the alternative.** Absent. Search capability is a fixed algorithm here; nothing in the setup lets heavy training weaken the search, so Risko and Gilbert's term has no counterpart.
- **Fit to the four strategies.** It narrows the question rather than answering it: within one system, two of the regimes (precompute into a store; compute at the moment of use) lie on one smooth iso-performance curve with a constant log-log slope, which is the shape the owner's conjecture ("regimes of one trade") would predict for those two. It says nothing about maintained structure or defer-and-re-read, and the curve is measured on one game, one board size, with no reuse count.
- **What the LIT entry's summary gets right and wrong.** Right that it fits laws across board sizes and finds a train–test trade-off at a measured rate. "more training buys the same performance as more search" holds only down to the one-node floor and over the measured range; the abstract does not give the rate, and the entry's description of it as "the cleanest measured exchange rate between amortized (training) and per-query (search) compute" overstates "amortized", since the paper prices neither the number of queries nor a per-query unit.

## Limitations

- One game (Hex), boards 3×3 to 9×9; the trade-off on 9×9 only.
- A modified AlphaZero with small fully connected nets; whether the rates transfer to standard implementations, larger nets or other games is untested, and the author asks for that test twice.
- Elo is transitive by assumption; the top-agent check changes the fitted parameters by up to about 40% (e.g. m_boardsize on the incline −430 against −590).
- The change-point form is chosen for interpretability; the sigmoid fits as well.
- No uncertainty is reported on any fitted coefficient, and the test-time compute unit is not defined.
- Training and test-time compute are compared in the same FLOPS-seconds without hardware or latency costs, and without any count of the games the agent will play.
