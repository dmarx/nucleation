# LEAD-089: Northstar modelled with control only and with a will-organization, priced

The study behind the CASE filed for LEAD-089. QUESTION-056's test: model
Northstar (CASE-023) with control and metacontrol mechanisms alone, then with
a will-organization over them, and price the difference as CLAIM-174's test 4
does (does the model with a will-organization beat the model without one by
more than its Occam cost, CLAIM-154).

## Model (`model.py`)

Episodes decide which of three regimes becomes effective: routine
deployment, cautious verification, emergency suspension. Context: a
specialist's objection o, an incident signal r, a business-critical flag b.
Arrangement of authority a = (s, j, v), the case's own variants: an
objection suspends deployment (Northstar-A, CASE-003) or not (B); severity is
classified by the product team or by an independent reliability group
(CASE-002); senior management may override a freeze for a business-critical
release (CASE-002). Proposals and attitudes are the same under every
arrangement.

- **WO**, will-organization: maintained relations decide which proposal
  becomes effective (a severe classification takes precedence; jurisdiction
  over classification sets how readily a signal is classified severe;
  suspension by objection; the override). Four parameters (q0, q1, m, eps),
  uniform priors; evidence by 16-node Gauss-Legendre quadrature per
  dimension.
- **C0** controller blind to authority, P(y | x), Dirichlet; exact evidence.
- **C1** saturated metacontrol lookup, P(y | x, a), Dirichlet; exact.
- **C2** metacontrol gate: softmax over regimes, values linear in (1, x, a);
  14 weights, N(0, 2²) prior, Laplace evidence.
- **C3** C2 plus every pairwise product within x and between x and a; 38
  weights.
- **C4** gate saturated in x, each authority bit modulating each context
  separately; 64 weights.

The arrangement is an input to C1-C4, so they are control models that see
authority; what they lack is variables for the relations.

## Worlds (`model.world_table`)

- `governed`: the case as stipulated (the WO structure), true parameters
  drawn per seed: q0 ~ U(0.1, 0.6), q1 ~ U(0.6, 0.95), m ~ U(0, 0.4),
  eps ~ U(0.01, 0.1).
- `idle`: authority does nothing; P(y | x) drawn Dirichlet(1,1,1) per context
  (CLAIM-089's surviving case, CLAIM-482).
- `idiosyncratic`: authority matters, but not by these relations;
  P(y | x, a) Dirichlet per cell.
- `interacting`: the same relations, except that where the reliability group
  classifies it also takes objections over, so an objection no longer
  suspends by itself (s idle when j = 1). Seen only in combined arrangements.

Training: the baseline arrangement and each single change (000, 100, 010,
001), n episodes each, n in {30, 100, 300, 1000}; 20 seeds. Scores: log
evidence on the training data; log predictive per episode on 2,000 fresh
episodes per arrangement, under the training arrangements and under the four
unseen combined arrangements (110, 101, 011, 111). Regret is truth's log
predictive minus the model's, in nats per episode.

## Rerun

    python3 -I -m pytest -q test_model.py     # 8 tests, ~2 s
    python3 -I study.py                       # WO, C0-C3: 320 items, ~3 min
    python3 -I study.py c4                    # C4 on the same data, ~1 min
    python3 -I analyze.py                     # results/summary.json, summary_table.txt
    python3 -I asymptote.py                   # unlimited data, ~1 min

`study.py` appends one JSON line per item to `results/runs.jsonl`
(`runs_c4.jsonl` for C4) and skips items already written.

## Results (`results/summary_table.txt`, `results/asymptote.json`)

ln BF is WO's log evidence minus the best control-only model's, per seed
(median [min, max]); regret on the unseen arrangements is the mean over
seeds.

| World | n | ln BF, WO vs best control | WO wins | Regret, unseen: WO | C2 | C3 | C4 |
|---|---|---|---|---|---|---|---|
| governed | 30 | 17.1 [10.0, 22.2] | 20/20 | 0.015 | 0.264 | 0.197 | 0.214 |
| governed | 1000 | 61.3 [49.1, 70.7] | 20/20 | 0.001 | 0.102 | 0.046 | 0.032 |
| idle | 30 | -32.2 [-76.9, -0.9] | 0/20 | 0.422 | 0.212 | 0.177 | 0.122 |
| idle | 1000 | -1513.9 | 0/20 | 0.443 | 0.103 | 0.028 | 0.025 |
| idiosyncratic | 1000 | -1539.4 | 0/20 | 0.473 | 0.451 | 0.910 | 1.162 |
| interacting | 30 | 16.8 [10.3, 21.6] | 20/20 | 0.317 | 0.193 | 0.208 | 0.214 |
| interacting | 1000 | 66.4 [54.3, 81.6] | 20/20 | 0.294 | 0.197 | 0.292 | 0.236 |

With unlimited data (exact expected counts, 10^6 per training arrangement,
five seeds) the gates' regret on the unseen arrangements in the governed
world stays at 0.08-0.11 (C2), 0.022-0.034 (C3) and 0.009-0.018 (C4) nats
per episode, against WO's 0.0003-0.0009, which is the quadrature grid's
resolution. In the interacting world WO's is 0.19-0.40, worse than C2's
0.13-0.23.

## What it shows and does not

- In the world the case stipulates, the relations-structured model wins by
  more than its Occam cost at every size and seed, and it alone predicts
  combined interventions on authority never seen together. The gap to the
  control-only gates does not close with data: a log-additive gate cannot
  represent how the relations compose, and the products of two authority
  bits that would let it are never observed in training.
- The test has teeth: where authority is idle or idiosyncratic, WO loses by
  tens to thousands of nats.
- In-sample evidence does not catch a wrongly composed relation: in the
  interacting world WO wins the training evidence by 17-66 nats and
  predicts the unseen combined arrangements worse than the additive gate.
  Only the intervention test does.
- It is fictional data from the case's own stipulation. It shows what the
  structure buys if Northstar is as the paper says, not that any company is.
