# LEAD-083: compensation and entrainment in closed modes that are not blocks

Three arms, one protocol (see the docstring of `study.py`):

- **A, a field excitation.** The kink of an overdamped φ⁴ lattice,
  spacing h = 1, 0.5, 0.25, on [−20, 20] with φ = ∓1 at the walls.
- **B, a collective mode.** Kuramoto partial synchrony: N = 200 phase
  oscillators, Gaussian frequency quantiles (σ = 1), uniform coupling
  K/N with K = 2.5. The form is the locked cluster.
- **C, a block control.** Two clusters of 50 oscillators, coupling 4/N
  inside and 0.1/N across, centre frequencies ∓1.5.

Measures: the block test of CLAIM-157 (spectral ρ = δ/ε, and the
entrywise ratio of inside to cross coupling); compensation κ, LIT-902's
jaw-load design (a sustained load on members S, the form's task variable
read with the other members free and frozen); entrainment, CLAIM-172's
timing sense (detune S, read the frequency shift of S and of the rest of
the form).

## Rerun

    python3 -m pytest -q test_study.py      # 6 tests
    python3 study.py A osc                  # about 15 minutes on 4 CPUs

`results.jsonl` is append-only, one line per item; a rerun skips the items
already there. Delete it to start over. `summarize.py` prints the tables
the CASE quotes.
