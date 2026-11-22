# LEAD-040: Z2-symmetric recurrent lattices and the four partitions

A study for LEAD-040 (QUESTION-491): small recurrent networks with a Z2
symmetry, trained on a task whose answer depends on where the boundaries in
the input are; the four candidate partitions of the hidden field computed and
compared; walls moved by intervention; a closed wall pair compared with a wall
anchored by boundary conditions. numpy only, CPU.

## Files

- `z2rnn.py`: the lattice network (Z2-equivariant update, Z2-even readout),
  the task, hand-written backpropagation through time and Adam.
- `partitions.py`: the four partitions (walls, local causal-state coherent
  structures, local transfer entropy, operative sites by single-site Z2 flip)
  and the agreement measures.
- `experiments.py`: one item = one network: training, partitions on time
  slices 4, 8 (input phase) and 12, 16 (free phase), wall-moving interchange
  with a control window, closed against anchored walls.
- `run.py`: runs the ten items (six trained networks, four frozen random
  controls), appending one JSON line per network to `results.jsonl` and
  skipping ids already there. `params/` holds each network's weights.
- `summarize.py`: the tables in the CASE, from `results.jsonl`.
- `test_z2rnn.py`, `test_partitions.py`: pytest tests (gradient check,
  equivariance, transfer entropy on a copy process, causal states on fixed
  fields).
- `PROGRESS.md`: the run's progress and the choices made.

## Rerun

    cd scratch/studies/lead-040
    python3 -m pytest -q
    OPENBLAS_NUM_THREADS=1 python3 -I run.py      # about 1 minute per item
    python3 -I summarize.py

Delete `results.jsonl` to rerun from scratch. Seeds are fixed, so a rerun
reproduces the numbers up to floating-point differences.
