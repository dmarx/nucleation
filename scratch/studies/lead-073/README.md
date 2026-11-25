# LEAD-073 study: M, N and Γ_q of NOTE-746 in GPT-2 small and Pythia-70m

Pure numpy on CPU (no torch, no transformers). The models are downloaded
from huggingface.co into a directory outside the repository; weights are
never committed.

## Files

- `lmnp.py`: safetensors reader, byte-level BPE tokenizer, GPT-2 and
  GPT-NeoX forward passes returning f(x) (final layer-norm output) and g.
- `geometry.py`: F, G, M, N, Γ, A_q, Γ_q, containment and visibility.
- `relations.py`: the three relations (city in country, country language,
  country capital).
- `measure.py`: the measurement; writes one JSON per model.
- `test_geometry.py`: pytest tests on constructed subspaces and tiny random
  models (Lemma 2's identity, the B.5 counterexample, recovery of a known
  affine map, causality of the forward passes, the final-layer-norm span).
- `PREREG.md`: tolerances fixed before the first real run.
- `results/`: the JSON outputs and `summary.md`.

## Rerun

    D=<scratch dir>; mkdir -p $D/gpt2 $D/pythia-70m
    for f in config.json vocab.json merges.txt model.safetensors; do
      curl -sSL -o $D/gpt2/$f https://huggingface.co/openai-community/gpt2/resolve/main/$f; done
    for f in config.json tokenizer.json model.safetensors; do
      curl -sSL -o $D/pythia-70m/$f https://huggingface.co/EleutherAI/pythia-70m/resolve/main/$f; done
    python3 -I -m pytest -q scratch/studies/lead-073
    OMP_NUM_THREADS=2 python3 -I scratch/studies/lead-073/measure.py $D/gpt2 scratch/studies/lead-073/results/gpt2.json
    OMP_NUM_THREADS=2 python3 -I scratch/studies/lead-073/measure.py $D/pythia-70m scratch/studies/lead-073/results/pythia-70m.json
    python3 -I scratch/studies/lead-073/summarize.py

Each model takes a few CPU minutes. Seed 73.
