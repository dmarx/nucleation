# LEAD-043: a toy-scale forgetting study (CASE-274's design, reduced)

numpy only, CPU. No torch on this machine, so the transformer and its
backward pass are written by hand (`tinytf.py`, checked against finite
differences in `test_tinytf.py`).

## Files

- `tinytf.py`: 2-layer transformer (d 64, 4 heads, MLP 256, no layer
  norm), loss with soft targets and signed weights, Adam.
- `probes.py`: linear and one-hidden-layer MLP probes.
- `study.py`: worlds, arms, readouts, relearning. One JSON line per
  (seed, arm); resumes by skipping lines already written.
- `analyze.py`: pools the JSON lines into `summary.json` and `summary.md`.
- `test_tinytf.py`, `test_study.py`: pytest.
- `results_a.jsonl` (seeds 0, 1), `results_b.jsonl` (seeds 2, 3).

## Rerun

    export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1
    python3 -I -m pytest -q -p no:cacheprovider --rootdir=. .
    python3 -I study.py results_a.jsonl CACHE_DIR 0 1
    python3 -I study.py results_b.jsonl CACHE_DIR 2 3
    python3 -I study.py results_c.jsonl CACHE_DIR 0 2 ascentA_early ascentAB_early
    cat results_a.jsonl results_b.jsonl results_c.jsonl > /tmp/all.jsonl
    python3 -I analyze.py /tmp/all.jsonl .

CACHE_DIR holds the pretrained weights (`pre_s{seed}_{world}.npz`); it is
not committed. About 30–40 minutes per process on a shared 4-core machine.

## Design in one paragraph

128 subjects × 4 relations, each fact a random object of 16. Three query
templates: A `[s, rA, Q]`, B `[rB, s, Q]`, C `[rC, Q, s]`. Pretraining:
the 64 old subjects' facts under A and B; C only for the 48 non-target
subjects. Targets: 16 subjects × relations 0 and 1 (32 facts). The twin
world differs only in the target facts' values; the twin starts from the
same initialization and trains on the same schedule. Arms: unlearn (KL to
uniform), ascent (negative cross-entropy) and overwrite (new values), each
at cue A only or at cues A and B, all with rehearsal of retained facts;
and newtask (64 new subjects, no rehearsal). Each arm trains to its
criterion and then as many steps again (at least 100). Readouts per
target fact, for each model against its own values and against the
twin's: argmax under each cue; the runner-up once the top answer is
removed; p(value) under A and repeated-sampling coverage 1 − (1 − p)^N;
logit lens and linear and MLP probes (fitted on retained facts) at each
residual stage; reverting each block's fine-tuning delta, singly and
from a block downward; and relearning half the targets, with the
held-out half watched.
