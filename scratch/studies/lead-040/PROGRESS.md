# LEAD-040 progress

- Lead: LEAD-040 (advances QUESTION-491)
- Branch: claude/lead-040-z2-rnns
- Task: train small Z2-symmetric RNNs (numpy, CPU) on a task whose answer
  depends on boundaries in the input; compute the four candidate partitions
  of the hidden field (domain walls, local causal-state coherent structures,
  local transfer entropy concentrations, intervention-identified operative
  structures); move walls by intervention (interchange from a source input
  with the wall elsewhere, THEORY-2003 Remark 47), with a frozen random
  network control (THEORY-1002); compare a closed wall with an anchored one.
  File a CASE (executed-study), a CLAIM if warranted, dated notes on
  QUESTION-491 and LEAD-040.

## Done

- Step 1: checked whether held. Not held: no CASE, CLAIM or workbench cites
  QUESTION-491 with a result; CLAIM-763 only ranks the question; LEAD-092 and
  LEAD-118 are readings.

- Model, partitions, experiments and tests written (12 tests pass).
- First full run stopped (by PID) after one item to fix the wall
  definition; restarted 2026-11-22 from scratch (10 items, about a minute
  each, time limit 40 min), writing results.jsonl item by item.

- Full run done: results.jsonl holds all ten items; params/ holds weights.
  check_erasure.py / erasure.txt: where an erased anchored wall goes.
  Coordinator asked to resume; branch was already current, nothing lost.

## Next

- Summarize; write README; file CASE, CLAIM if warranted, notes on
  QUESTION-491 and LEAD-040, changelog fragment.

## Choices

- Lattice: 1D, N=32 sites, hidden d=4 (4 seeds) and d=8 (2 seeds); update
  tanh(Ws h_i + Wn(h_{i-1}+h_{i+1}) + u x_i), no bias, so Z2-equivariant.
- Task: noisy +-1 domain input (0-4 walls, domains >= 3) for 8 steps, then
  bulk input off for 12 steps with end sites clamped (boundary conditions);
  target m^2 (m = mean of input signs), read out as (mean a.h)^2 (Z2-even).
  Chosen so that moving a wall changes the answer (the lead's "what would
  count").
- Partitions on slices t=4, 8 (input phase), 12, 16 (free phase):
  walls = sign change of the order field; coherent structures = local
  causal state not a domain state (3-level field, past cone depth 2, future
  depth 2, domain = each future row uniform w.p. >= 0.9); local TE from
  both neighbours, history 2, > 0.5 bit; operative = flipping h_i -> -h_i
  moves the prediction by > 0.002.
- Interchange (THEORY-2003): move one wall by 2 sites by splicing the
  source run (same noise, wall moved) on the window, at t=4 and t=8;
  control window of equal width away from walls.
- Controls (THEORY-1002): frozen random networks (scale 0.5 and 1.5),
  readout trained only.
- Closed vs anchored: minority domain of length 1-8 vs single wall forced
  by opposite boundary inputs, run 200 free steps; shrink a pair by
  interchange; erase the anchored wall by writing a uniform state.
- Experiment E (spectrum around a wall) not attempted: outside the lead.
- Walls are defined by neighbour dot products h_i . h_{i+1} < 0, and the
  scalar field for causal states and TE uses a per-time leading direction:
  the first full item showed the trained network oscillating in the free
  phase (the bulk flips sign about every 6 steps), so a fixed axis saw the
  whole field pass through zero. Wall counts in the closed/anchored tests
  use interior bonds 3..N-3 (boundary layers at the clamped ends excluded).
