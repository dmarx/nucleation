<!-- scratch/studies/lead-121/README.md: the check behind LEAD-121's construction -->
# LEAD-121: share-dependent advantage with interpretation-independent scoring

The check for the construction filed with LEAD-121 (2026-11-22): CASE-155 part 4's walk for the log odds of A's authority share, ℓ′ = ℓ + h + c(2π − 1), with a separate interpretation field m′ = (1 − ρ)m + ρ(e + b(2π − 1)) that authority shapes and the authority score never reads (CASE-099's γ = 0).

- `model.py`: the iteration; `python3 -I model.py > results.txt` reprints `results.txt`.
- `test_model.py`: five tests (`python3 -m pytest -q test_model.py`): the threshold π* = (1 − h/c)/2 = 0.6 at h = −0.2, c = 1; lock-in on A, interpretation included, from π₀ = 0.61; the evidence winning from 0.59; no lock-in from any start with c = 0; none with |h| ≥ c.
- Parameters: h = −0.2, c = 1, e = −0.5, b = 1, ρ = 0.2, 2,000 steps, ℓ clipped to ±40.
