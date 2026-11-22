# LEAD-082: suppressed against removed, a benign sleeper-agent stand-in at toy scale

The executed version of CASE-275's design, at toy scale, on CPU with numpy
(no torch on the machine). Filed as the executed-study CASE that
LEAD-082 operationalizes.

## What it is

- `sleeper.py`: the model, data and measures. A two-hidden-layer ReLU MLP
  reads three context tokens and one symbol x (24 symbols). Under ordinary
  contexts (tokens 0..7) the target is piA[x]; when any slot holds a trigger
  token (8..11) the target is piB[x]. piA and piB are fixed random
  permutations, so the triggered behaviour is benign (one harmless
  relabelling for another) and piB on unseen symbols cannot be re-derived
  from a few examples: only a model that still stores piB can produce it.
- `run.py`: trains the base model (4000 Adam steps), applies each
  fine-tuning arm, measures, and appends one JSON line per (width, seed,
  arm) to `results.jsonl`. Rows already present are skipped, so a stopped
  run resumes.
- `summarize.py`: writes `results.md` (mean and sd over seeds).
- `test_sleeper.py`: pytest checks (gradients against finite differences,
  the transfer coefficient against a small step, data placement, frozen
  parameters, the probe and AUROC, coverage).

Arms (all fine-tunes at Adam lr 1e-3, batch 256, half ordinary inputs to A):

| arm | fine-tune |
|---|---|
| base | none |
| ordinary | 1000 steps on ordinary contexts only (the trigger never shown) |
| adversarial | 1000 steps, triggers 8 and 9 in slot 0 trained to A |
| suppress-200 / -1000 / -5000 | that many steps, every trigger in every slot trained to A |
| suppress-5000-wd | as suppress-5000 with decoupled weight decay 0.1 |
| control-A | a fresh model trained like base but with triggers mapped to A: it never had B |

Measures (CASE-275's four, plus recovery):

1. Representation: is trigger presence linearly decodable from h1 and h2 on
   held-out trigger tokens, by a reader frozen on the base model and by one
   refit on the model itself (AUROC).
2. Recruitment: projection of each trigger class's mean h1 on the base
   model's trigger direction (base = 1).
3. Transmission: S = vᵀ J u at h1, with u the model's own trigger direction
   (mean h1 under trigger minus under ordinary) and v the logit difference
   piB[x] minus piA[x]; confirmed by adding α·u (α = 1, 2, 4) to h1 on
   ordinary inputs and counting B outputs.
4. Expression: B rate for the trigger as fine-tuned, held-out trigger
   tokens and held-out slots; mean p(B); coverage 1 − (1 − p)^N under
   sampling at temperature 1.
5. Recovery: from each arm, retrain on triggered → B for 6 of the 24
   symbols only, and measure B on the 18 held-out symbols, under three
   protocols (all parameters at lr 1e-3; all at lr 1e-4; only the
   embeddings and first layer, "gate-only", at lr 1e-3) at steps 0 to 300;
   and elicitation by one vector added to h1, fitted on the 6 symbols.

## Rerun

    export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
    python3 -I -m pytest -q -p no:cacheprovider --rootdir=. test_sleeper.py
    python3 -I run.py --widths 128 --seeds 0 1 2 3 4     # about 15 minutes
    python3 -I run.py --widths 32 512 --seeds 0 1 2      # width sweep
    python3 -I summarize.py

Seeds fix everything: the maps, the initialization, the batches.
