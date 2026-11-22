# LEAD-177: the forager ladder and a sensor network revising its correspondences

Constructions for QUESTION-285's strategy ("construct systems with identical
sensory correlations but different memory persistence, downstream use, and
adaptive capacities") and CASE-239's proposed study. numpy and scipy, CPU.

| file | what |
|---|---|
| `ladder.py` | the alarm-world rungs: R0 fail-safe relay (CASE-238), R1 tester (CASE-240), R2 four-probe diagnoser (CASE-242), R3 a diagnoser that revises its test schedule from its record of real fires |
| `forager.py` | CASE-239's forager: learner, frozen criterion, fixed self-set profile, designer's profile, oracle, plus a features-only freeze and two target-replacement controls (score, arbitrary); two learning rules (RLS, tabular) |
| `network.py` | a Robinson-style sensor network whose correspondences are fixed, revised by self-consistency, revised against a protected anchor, against a writable anchor, or against an anchor it may refuse |
| `study_*.py` | runners; each writes one JSON line per run to `results/*.jsonl` and resumes by skipping what is there |
| `analyze_forager.py` | the forager summary |
| `results/*_summary.md` | the tables the record cites |
| `test_*.py` | pytest |
| `smoke.py` | a quick look over a few seeds (not the study run) |

Rerun (about 5 minutes in all, one thread):

    export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
    python3 -I -m pytest -q scratch/studies/lead-177
    python3 -I scratch/studies/lead-177/study_ladder.py 100
    python3 -I scratch/studies/lead-177/study_forager.py 40
    python3 -I scratch/studies/lead-177/analyze_forager.py
    python3 -I scratch/studies/lead-177/study_network.py 40

Delete a `results/*.jsonl` to rerun it from scratch; otherwise the runner only
adds missing items.

Choices the lead left open, and why (also in the CASE):

- One world for the lower rungs (the owner's alarm chain), so that the four
  rungs read literally the same sensor channel; the forager has its own world
  because CASE-239 specifies one, and its arms share a patch stream and yield
  noise per seed (common random numbers).
- The forager enters any patch it does not warn about (predicted visit value
  below -0.5): the criterion of failure is predicted loss, as CASE-239 puts
  it, not an opportunity cost; the oracle uses the same rule with the truth.
- The learner's target is its own energy account per visit over a horizon of
  20 steps, including its share of upkeep above its resting rate; it knows
  its resting upkeep, not which patches raise it.
- A features-only freeze was added to separate CASE-239's arm 5 (which also
  freezes tau and the probe policy) into its parts.
- CASE-239's second defeater is read two ways and both are run: a matched
  surrogate (immediate intake, equal to the energy account in training) and an
  arbitrary score.
- R1 retests once on silence before registering (CASE-240's "additional
  interventions"); without it, 2 % readout error gave a false registration in
  68 of 100 runs.
