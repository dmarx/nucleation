# scratch/formal/permutation_spectrum_check.py: shows that a Fourier spectrum taken over the row and column order of a
# weight matrix, as FREE-Merging takes one of each task update, is not a property of the network's function: permuting a
# hidden layer's units leaves a two-layer network's outputs unchanged and moves the spectrum's low-frequency share.
# Filed with the assistant's admission rule for CLAIM-tmpumro8 (2026-11-15). Run: python3 -I scratch/formal/permutation_spectrum_check.py
import numpy as np

rng = np.random.default_rng(0)
d_in, d_h, d_out, n = 16, 32, 8, 200
W1, W2 = rng.normal(size=(d_h, d_in)), rng.normal(size=(d_out, d_h))
dW1 = np.outer(np.cos(2 * np.pi * np.arange(d_h) / d_h), np.ones(d_in)) + 0.1 * rng.normal(size=(d_h, d_in))  # a smooth update
relu = lambda z: np.maximum(z, 0)
f = lambda A, B, X: B @ relu(A @ X)

X = rng.normal(size=(d_in, n))
P = np.eye(d_h)[rng.permutation(d_h)]
A, Ap = W1 + dW1, P @ (W1 + dW1)              # the fine-tuned layer, and the same with its hidden units permuted
B, Bp = W2, W2 @ P.T
assert np.allclose(f(A, B, X), f(Ap, Bp, X))  # same function

def low_share(M, k=3):
    """Share of the 2-D spectral energy at low frequency along the hidden-unit (row) axis, all column frequencies."""
    S = np.abs(np.fft.fft2(M)) ** 2
    return S[np.r_[0:k, -k + 1:0], :].sum() / S.sum()

before, after = low_share(dW1), low_share(P @ dW1)  # the update, in the two equivalent coordinate orders
print(f"low-frequency share of the update: {before:.3f} in one unit order, {after:.3f} in a permuted one")
assert before > 0.5 and after < 0.5 * before
# A quantity of the function is unchanged; e.g. the singular values of the update are permutation-invariant.
assert np.allclose(np.linalg.svd(dW1, compute_uv=False), np.linalg.svd(P @ dW1, compute_uv=False))
print("permutation spectrum check: all passed")
