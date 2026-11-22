<!-- scratch/studies/lead-167/README.md: the materials of LEAD-167's study -->
# LEAD-167: Bourrat's two individuality measures on a scaffolding model

The study filed as the CASE that carries out LEAD-167 (2026-11-22). Exact
computation, no sampling: every quantity is computed from the 256-state
transition matrix and its stationary distribution.

- `model.py`: the minimal ecological-scaffolding model (six binary cells in
  two patches, one external scaffold bit per patch, collective reproduction by
  recolonisation, an endogenisation parameter `lam`) and the common-input
  controls (symmetric and asymmetric). The docstring states the dynamics.
- `measures.py`: Krakauer et al.'s A*, A, nC; Bourrat 2024's Â by the
  adjustment route NOTE-027 gives (do-channel first, then its MI under a
  stated input distribution), its normalised form, C1, C2's variance profile,
  and I(E'; Ŝ).
- `coarse.py`: Bourrat 2023's δC on all 203 partitions of the cells, with
  and without conditioning on the environment (δC|E), in the point-prediction
  form (Bourrat's) and a distributional form (an extension, not his).
- `run.py`: the sweep over `lam`, the controls, an accuracy-plus-cost
  objective δC + κ·k (an extension), and a parameter sensitivity check;
  writes `results.json` and `summary.txt`.
- `test_lead167.py`: 9 tests, among them NOTE-027's XOR counterexample
  (A = 1 bit, Â = 0), Bourrat's Fig. 2 common cause (A* > 0, Â = 0), the
  exact lumpability of the patch partition given the environment, and the
  zero δC|E of the identity partition.

Rerun (about a minute on a CPU, numpy only):

    cd scratch/studies/lead-167
    python3 -m pytest -q -p no:cacheprovider test_lead167.py
    python3 -I run.py

Parameters: a = 0.3 (cell heredity), eps = 0.05 (noise), d = 0.05
(recolonisation), q_on = q_off = 0.2 (scaffold switching); the sensitivity
block varies a in {0.1, 0.3, 0.5} and d in {0, 0.05, 0.2}.
