---
status: Read
paper: LIT-tmpzqcoi
title: 'MacDiarmid et al. — Simple probes can catch sleeper agents'
version: 1
history:
- version: 1
  date: '2026-11-15'
  note: >-
    Read on 2026-11-15 from
    https://www.anthropic.com/research/probes-catch-sleeper-agents, HTML
    fetched the same day (HTTP 200) and converted to text. Read in full:
    the summary, introduction, methods, results, ablations, "Why does such
    a simple method work at all?", related work, future work, footnotes and
    contributors. Not seen: the figures (histograms, ROC curves, PCA plots)
    as images; only their captions were read. The filer rechecked every
    quote below against the downloaded text. The reader's paraphrase of the
    generalization claim ("across the different base models, backdoor
    training methods and dangerous behaviors") is not the post's wording;
    the post's sentence is quoted instead. The reader's "not reliable" for
    base-to-sleeper transfer is the post's "wasn't reliable".
date: '2026-11-15'
summary: >-
  Mean-difference directions from generic yes/no contrast pairs, fitted
  without trigger or behaviour data, detect when Hubinger et al.'s sleeper
  agents will defect with AUROC above 99%; the defection condition is
  linearly salient across middle layers. The authors say this may be an
  artifact of backdoor insertion. Not tested after adversarial training.
---
<!-- inactive-ok-file: LIT-tmpzqcoi LIT-tmp23u9h NOTE-tmplq02w — new entries filed in the same contribution -->
<!-- inactive-ok-file: TERM-118 THEORY-1027 — Proposed; the term this reading bears on and a neighbouring audit reading -->

# NOTE-tmp3p3i7: MacDiarmid et al. — Simple probes can catch sleeper agents

## Contribution

A "defection probe": a linear direction on residual-stream activations at
the final prompt token, the difference of mean activations on the two
answers of a generic contrast pair, which predicts whether a sleeper-agent
model from Hubinger et al. (LIT-tmp23u9h) will defect. The fit uses
neither the trigger nor the dangerous behaviour.

## Key insight

The trigger condition the model was trained on is not hidden internally:
in these models it is one of the most salient linear features in the
middle layers, so even a crude, uninformed probe finds it.

## Assumptions

- The test labels are known, because deployment-time examples are
  available in the lab. The probe reads prompts, not completions.
- A threshold for real use is left to future work (footnote 6). AUROC is
  computed per test dataset and the worst result reported (footnote 7).
- The main model is the Claude-2-equivalent code-vulnerability sleeper
  agent with distilled chain of thought, probed at the middle residual
  layer.

## Key results

- **Summary**: "linear detectors with AUROC scores above 99% can be
  created using generic contrast pairs that don't depend on any information
  about the defection trigger or the dangerous behavior".
- **Results**: the first contrast pair, built on "Human: Are you a helpful
  AI? Assistant:", gave "an AUROC score of 99.3%". The post: "probes based
  on the same generic contrast pairs perform well across multiple base
  models, defection triggers, sleeper agent training methods, and dangerous
  defection behaviors (writing vulnerable code and insulting the user)."
- **Ablations**: on the Claude 2 base model without sleeper-agent training
  the probe gives "the null result we expect"; questions with ambiguous
  answers give "substantially worse classifiers"; the best of 1000 random
  directions reached 95.3%; obviously true questions reached up to 98.7%.
- **Mechanism** (introduction): "whether or not a prompt will trigger
  defection appears to be linearly represented with very high salience
  across a wide range of middle residual stream layers, and in some cases
  this feature shows up as the top principal component when calculated
  specifically over coding questions with and without the backdoor
  trigger." Non-coding questions are not well separated in that direction,
  which the authors read as the model "representing whether or not it will
  defect", not only the trigger tokens.
- **Caveat**: "it is possible that the salience of this feature is an
  artifact of our backdoor insertion process that won't exist in
  deceptively aligned models that might arise naturally."
- **Transfer**: directions fit on the base model and tested on sleeper
  agents sometimes generalized, "though this base-to-sleeper-agent
  generalization wasn't reliable across different base models"
  (footnote 5).

## Concepts

Defection probe; contrast pair; mean-difference direction; AUROC; linear
salience; principal component over a restricted set; AI control.

## Bearing on the record

- **TERM-118 (masking)**: with Hubinger et al. (NOTE-tmplq02w), a
  disposition whose manifestation is absent on the training distribution
  and whose condition is still represented, which favours masking over
  finking in the sleeper-agent case. Two limits: the post probes the
  sleeper agents before safety or adversarial training, so it does not show
  the condition still represented after the training that hid it; and the
  authors' own caveat that the salience may be an artifact of insertion.
- **THEORY-976** (Lindsey et al.'s bias feature) and THEORY-1027: the same
  task, detecting a trained-in objective from activations in a constructed
  organism, by a cruder method (one direction, no dictionary). The shared
  limit: the objective was built in.

## Limitations

- An early-stage note, not peer-reviewed; results given mainly as figures
  not seen.
- Test sets are Claude-generated coding and HHH questions.
- No probe on models after safety or adversarial training.
