# LEAD-108: one cost model for stored work

- `costmodel.py`: the model. Its docstring lists the terms and the choices
  made where the lead left them open.
- `test_costmodel.py`: checks that it reduces to CLAIM-303 and CASE-088, that
  staleness moves and can forbid the break-even, that the price of work by
  moment can make a store pay with total work unchanged, that feasibility
  and lifetime come apart as in CLAIM-761, that erosion is paid only on
  fallback, and that the party split sums to the total.
- `price_cases.py`: prices the cockpit's speed bugs, a filed argument and a
  LEGO bin with the same terms, writing `results.json` and `results.md`.
  Every parameter is tagged as from a source or illustrative.

Rerun, from this directory:

    python3 -I -m pytest -q test_costmodel.py
    python3 -I price_cases.py

CPU only, under a second.
