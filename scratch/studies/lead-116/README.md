# LEAD-116: stochastic and factorial assembly scored by committor

Runs CASE-219 (stochastic assembly) and its factorial variant CASE-220,
extending CASE-216's four-state annealing toy, and scores intermediate partial
structures by the committor q(s) = Pr_s(tau_F < tau_K): the chance of reaching a
valid folded target F before a designated failure/trap set K.

## The model

A continuous-time Markov chain whose microstate is the SET of bonds currently
formed, a subset of {a, b, c, d}, plus one absorbing misfold sink K (16 subset
states + K = 17 states). Two alternative seams a, b (the "two routings" of
CASE-220) each nucleate the shared body c, d. Seam a completes to the valid fold
F_A = {a,c,d}, seam b to F_B = {b,c,d}; both are feasible. Two kinetic traps,
both from the DNA-origami readings:

- incompatible-seam trap (Dunn et al.): any state holding both seams misfolds,
  irreversibly, to K;
- unnucleated collapse (DeLuca et al.; Sobczak): a body bond forms only with a
  seam present to template it, and a seamless assembly collapses to K.

Committors are exact linear solves on the transient states
(Q_TT q_T + Q_TF 1 = 0, q = 1 on F, 0 on K). Occupancies and first-passage
probabilities use scipy matrix exponentials. Rates are invented constants (as
CASE-215's are); a temperature knob T scales the off-rates (melting), echoing
CASE-216. None is a DNA-origami measurement.

## Files

- `assembly_committor.py` — the model, the committor/occupancy solvers, the
  scenarios, and the checks. `python3 -I assembly_committor.py` writes
  `results.txt` and `results.json`.
- `test_assembly_committor.py` — 13 pytest tests (gambler's-ruin closed form,
  committor vs Monte Carlo, generator conservation, the harmonic equation, and
  one test per headline result). Run:
  `python3 -I -m pytest test_assembly_committor.py -q`.
- `results.txt`, `results.json` — the run's output.

## Rerun

    cd scratch/studies/lead-116
    OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 \
      NUMEXPR_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 -I assembly_committor.py
    OMP_NUM_THREADS=1 python3 -I -m pytest test_assembly_committor.py -q

Runs in about a second; everything is a 17x17 linear solve or matrix exponential.

## What it shows (see results.txt for the numbers)

- **CLAIM-599 from assembly dynamics.** q({a}) = q({b}) = 0.81 (each a
  productive nucleus, Delta = +0.62), but q({a,b}) = 0.04 (Delta = -0.15): two
  separately productive nuclei combine into a trap. V is non-monotone. CLAIM-599
  so far had only a stipulated numerical example; this is an instance from a
  dynamical assembly model.
- **CLAIM-567 / progress is not completion.** The committor does not track bond
  count: a 1-bond nucleus {a} has q = 0.81 while the 4-bond state {a,b,c,d} has
  q = 0.05 and {a,b} (2 bonds) has q = 0.04. Reachable is not reliably reached;
  an intermediate's future, not its progress, is what the committor measures.
- **CASE-220 factorial (2 routings x {uniform, targeted stabilisation}).**
  Targeted early stabilisation of the designed seam raises the committor
  (Delta_q_N > 0, a productive nucleus); stabilising both seams locks in the
  incompatible pair (Delta_q_N < 0, a trap). The routings are symmetric.
- **QUESTION-400.** At fixed total stock, moving the seam budget from a to b
  slides the realised share of F_A from 1.00 to 0.00 while the attainable set
  {F_A, F_B} is unchanged: allocation selects which form results. An even split
  across the two seams minimises the success committor (it maximises the
  double-seam trap); a seam-vs-body sweep has an interior optimum.
- **CLAIM-566.** A fold is reached (~0.20) far more often than it persists
  (survival ~0.05 by t=10), and survival falls with T (melting) and with time:
  assembling and persisting are distinct probabilities.
