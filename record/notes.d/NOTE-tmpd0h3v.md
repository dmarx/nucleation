---
status: Read
paper: LIT-tmppqss3
title: 'Javed and White 2019 — Meta-Learning Representations for Continual Learning'
version: 1
history:
- version: 1
  date: '2026-11-19'
  note: >-
    URL read: https://arxiv.org/pdf/1905.12588 (15 pages; header "33rd
    Conference on Neural Information Processing Systems (NeurIPS 2019)").
    Javed and White. Kind of copy (step 5): arXiv preprint, the authors' own
    manuscript (the NeurIPS 2019 version). Lawful. Date: 2026-11-19. HTTP
    200, no bot check, no refusal. No email address sent. Text extracted
    with pdftotext to dl/text.txt; PDF in dl/paper.pdf. Read: abstract,
    §1-§6 in full (pp. 1-9). Skipped: appendices (algorithm 3,
    hyperparameters, Appendix C.1 on meta-learned initializations, which the
    main text cites but which was not read). Values in tables and figures
    read from captions and text.
date: '2026-11-19'
---
<!-- inactive-ok-file: CASE-tmphsr99 CLAIM-tmp5vg7p CLAIM-tmp8ljvp THEORY-1353 — Proposed; cited in this filing of 2026-11-19 -->

# NOTE-tmpd0h3v: Javed and White 2019 — Meta-Learning Representations for Continual Learning

## Contribution

Khurram Javed and Martha White propose OML (online-aware meta-learning). It meta-trains a deep representation network (RLN) so that a small prediction network (PLN) on top of it can learn from a correlated stream by plain online SGD, quickly and without overwriting what it learned earlier. The objective takes gradients through a sequence of online updates and then scores the result on all the data seen, so interference is part of the training signal. At meta-test time the representation is frozen, and only the PLN learns. On Incremental Sine Waves and Split-Omniglot (and mini-ImageNet), OML representations forget far less than pre-trained or sparse (SR-NN) ones. They turn out highly sparse with no dead neurons, and they make other continual-learning methods (EWC, MER, ER-Reservoir) work better.

## Key results

- The aim (abstract, p. 1): "we propose OML, an objective that directly minimizes catastrophic interference by learning representations that accelerate future learning and are robust to forgetting under online updates in continual learning".
- Separating forgetting from generalization (§4, p. 7): "Note that training accuracy is a meaningful metric in continual learning as it measures forgetting."
- Regression (§4, p. 7): "OML can learn new functions with a negligible increase in average MSE." The pre-training baseline "clearly suffers from interference".
- It is the online-awareness that helps, not representation quality alone (§4, p. 7): OML and MAML-Rep do equally well with IID training, so "the higher performance of OML is indeed because the representations are more suitable for incremental" learning.
- Faster learning, not only less interference (§5, p. 9): "OML outperforms even approximate IID sampling, suggesting it is not only mitigating interference but also making learning faster on new data."
- Sparsity without dead units (§4, p. 8): "OML produces the most sparse network, without any dead neurons."
- Meta-learning an initialization was not enough (§3, p. 4): "their work meta-learns a model initialization, an inductive bias we found insufficient for solving the catastrophic interference problem".
- The representation is fixed at test time (§4, p. 6): "The RLN is only updated with the meta-update and acts as a fixed feature extractor during the inner updates in the meta-learning objective and at evaluation time."
- Their open problem (§6, p. 9): "An important next step for this work is to demonstrate how to learn these representations online without a separate meta-training phase."

## Assumptions

- A meta-training distribution of continual-learning problems like those met at test time (held-out sine functions, held-out Omniglot characters).
- A split into a slow representation, meta-trained offline and then frozen, and a fast predictor learned online.
- Short trajectories (400 regression batches; 1,000 Omniglot images over 200 classes) and small networks.

## Concepts

- Continual Learning Prediction (CLP) problem: an unending stream of correlated samples whose targets depend only on the current input.
- RLN / PLN: the meta-learned representation network and the online prediction network.
- Instance sparsity, and dead neurons: few units active per input, and none inactive for all inputs.

## Bearing on the record

- [CLAIM-tmp8ljvp](../claims.d/CLAIM-tmp8ljvp.md): related, mostly on the forgetting side. OML trains a representation against forgetting and for fast later learning together, which is the claim's Not-new-as-an-objective point (meta-learning already targets future adaptability). It does not show continued training raising acquisition cost. The representation is frozen at test time, so new learning happens only in the small predictor, and the representation's own capacity to change is set to zero by design. That is an extreme case of the claim's Not-one-scalar bullet: retention and fast acquisition are secured together by giving up representational plasticity during deployment. The authors' open problem, learning the representation online, is where the claim's question would arise.
- [CLAIM-tmp5vg7p](../claims.d/CLAIM-tmp5vg7p.md): leaves open. There is no long-horizon training and no plasticity-restoring intervention. The authors' tentative remedy for online use, periodically re-optimizing the representation on a recent buffer, is a direct intervention on the representation, but it is not tested.
- [CASE-tmphsr99](../cases.d/CASE-tmphsr99.md): supports the case's adapter arm. The case reads a fresh small adapter doing much better than updating existing weights as a sign of a shortage of modifiable organization (A58). OML shows the converse design, a frozen representation and a learned head, working well when the representation was trained for it. A frozen-body-plus-head control should be read against how the representation was trained.
- [THEORY-1353](../theory.d/THEORY-1353.md): a small point of contact. OML's representation has no dead neurons, while Dohare et al. list dead units as a correlate of plasticity loss. OML does not study plasticity loss.

## Limitations

- Short streams and small benchmarks. There is no measure of plasticity over long training.
- An offline meta-training phase needs a distribution of tasks like the test tasks, the requirement Dohare et al. call unrealistic for lifelong learning.
- Both the Split-Omniglot and the regression objectives use approximations (truncated unrolling for Omniglot).
