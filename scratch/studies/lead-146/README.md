<!-- scratch/studies/lead-146/README.md: the materials of LEAD-146's draft preregistration -->
# LEAD-146: a draft preregistration of the discriminating fidelity study

Drafted on 2026-11-22 for LEAD-146. Nothing here is fixed; the owner fixes
the margins in CASE-055.

- `preregistration-draft.md`: the draft. Hypotheses, the strong contextual
  baseline, populations and sampling frames, the language pair, the rates
  assumed, the decision rule, the margin with its power, and the sixteen
  choices left to the owner, each with alternatives and a lean.
- `power.py`: a simulation of the study's main test, the held-out increment
  in R² of one predictor set over another, with cross-validation grouped by
  source item and a cluster bootstrap over items. Its docstring states the
  data-generating model; its `DEFAULTS` are the draft's assumed rates.
- `test_power.py`: five tests (`python3 -m pytest -q test_power.py`).
- `results.json`: the output: criterion reliability at J = 30 and 15, the
  calibration from latent to observed increment, and power at margins 0.01,
  0.02 and 0.05 over 40 to 480 items, with a size check at the margin and
  sensitivity to receivers, reliability and renderings per item.

Rerun: `python3 -I power.py results.json` (about ten minutes on four CPUs;
seeds are fixed, so the numbers reproduce).

Not modelled: judge random effects (judge noise is added per answer and not
removed, which is conservative), the composition test of QUESTION-074, and a
baseline with many more features than six.
