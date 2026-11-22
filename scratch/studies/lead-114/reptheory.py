"""Recover a finite group's irreducibles from a Cayley table ALONE, with no
group name, no reference representation and no character table supplied.

Method (Peter-Weyl / Wedderburn, done numerically):

  * Functions on G = R^m carry the left-regular representation L(a) and the
    right-regular representation R(b); these commute.
  * The CENTRE of the group algebra -- operators commuting with every L and
    every R -- is spanned by the CLASS-SUM operators C_k = sum_{a in class k}
    L(a). There are (#conjugacy classes) of them, one per irreducible.
  * The class sums commute and are closed under transpose, hence form a
    commuting normal family: a generic Hermitian combination's eigenspaces are
    their joint eigenspaces = the ISOTYPIC BLOCKS V_rho, of dimension d_rho^2.
  * So #irreps = #blocks, d_rho = sqrt(dim V_rho), and the scalar by which C_k
    acts on V_rho is the central character omega_rho(k); the ordinary
    character is chi_rho(k) = omega_rho(k) * d_rho / |class k|.

Everything below takes only an integer Cayley table.
"""
import numpy as np


def identity_element(cayley):
    m = cayley.shape[0]
    ar = np.arange(m)
    for e in range(m):
        if np.array_equal(cayley[e], ar) and np.array_equal(cayley[:, e], ar):
            return e
    raise ValueError("no identity in table")


def inverses(cayley):
    m = cayley.shape[0]
    e = identity_element(cayley)
    inv = np.full(m, -1, dtype=np.int64)
    for g in range(m):
        h = int(np.where(cayley[g] == e)[0][0])
        inv[g] = h
    return inv, e


def conjugacy_classes(cayley):
    """Blind: partition elements by conjugacy using only the table."""
    m = cayley.shape[0]
    inv, _ = inverses(cayley)
    seen = [False] * m
    classes = []
    for g in range(m):
        if seen[g]:
            continue
        orbit = set()
        for x in range(m):
            # x g x^{-1}
            c = int(cayley[cayley[x, g], inv[x]])
            orbit.add(c)
        for c in orbit:
            seen[c] = True
        classes.append(sorted(orbit))
    return classes


def left_regular(cayley):
    """L[a] is m x m with L[a][x, y] = 1 iff a*y = x."""
    m = cayley.shape[0]
    L = np.zeros((m, m, m))
    for a in range(m):
        for y in range(m):
            L[a, cayley[a, y], y] = 1.0
    return L


def class_sum_operators(cayley, classes, L):
    return [sum(L[a] for a in cls) for cls in classes]


def _group_eigs(vals, tol):
    """Group sorted-by-value indices into clusters of near-equal values."""
    order = np.argsort(vals)
    groups = []
    cur = [order[0]]
    for i in order[1:]:
        if abs(vals[i] - vals[cur[-1]]) <= tol:
            cur.append(i)
        else:
            groups.append(cur)
            cur = [i]
    groups.append(cur)
    return groups


def isotypic_blocks(cayley, seed=0, tol=1e-6):
    """Return the isotypic blocks as orthonormal column bases (list of
    (m x dim) arrays) and the class list. No group supplied beyond `cayley`."""
    m = cayley.shape[0]
    classes = conjugacy_classes(cayley)
    L = left_regular(cayley)
    C = class_sum_operators(cayley, classes, L)
    rng = np.random.default_rng(seed)
    # Generic Hermitian element of the centre.
    A = sum((rng.standard_normal() + 1j * rng.standard_normal()) * Ck
            for Ck in C)
    Z = A + A.conj().T
    w, V = np.linalg.eigh(Z)          # ascending real eigenvalues
    groups = _group_eigs(w, tol * max(1.0, np.max(np.abs(w))))
    blocks = [V[:, g] for g in groups]
    return blocks, classes, C


def recover_irreps(cayley, seed=0, tol=1e-6):
    """Full blind recovery. Returns a dict with #irreps, dims, and the
    character table (rows=irreps, cols=classes)."""
    blocks, classes, C = isotypic_blocks(cayley, seed=seed, tol=tol)
    class_sizes = [len(c) for c in classes]
    dims = []
    char_rows = []
    cent_rows = []
    for B in blocks:
        bdim = B.shape[1]
        d = int(round(np.sqrt(bdim)))
        dims.append(d)
        omegas = []
        for Ck in C:
            # scalar by which C_k acts on this block: trace(B^H C_k B)/bdim
            scal = np.trace(B.conj().T @ Ck @ B) / bdim
            omegas.append(scal)
        omegas = np.array(omegas)
        cent_rows.append(omegas)
        chi = np.array([omegas[k] * d / class_sizes[k]
                        for k in range(len(classes))])
        char_rows.append(chi)
    dims = np.array(dims)
    order = np.argsort(dims, kind="stable")
    dims = dims[order]
    char = np.array(char_rows)[order]
    # Reorder the isotypic blocks to match the sorted dims/character rows, so
    # callers can align a per-irrep spectrum to dims[i] and character_table[i].
    blocks = [blocks[i] for i in order]
    # imaginary parts should be ~0 for real/quaternionic; keep real part but
    # report max imaginary for honesty.
    max_im = float(np.max(np.abs(char.imag))) if char.size else 0.0
    char_real = char.real
    # orthogonality residual: sum_k |class_k| chi(k) conj(chi'(k)) = |G| delta
    cs = np.array(class_sizes, dtype=float)
    G = char * cs[None, :]
    gram = G @ char.conj().T
    ortho_resid = float(np.max(np.abs(gram - cayley.shape[0] *
                                      np.eye(len(dims)))))
    return {
        "n_irreps": len(dims),
        "n_classes": len(classes),
        "class_sizes": class_sizes,
        "dims": dims.tolist(),
        "sum_d2": int(np.sum(dims ** 2)),
        "order_from_dims": int(np.sum(dims ** 2)),
        "character_table": np.round(char_real, 6).tolist(),
        "max_char_imag": max_im,
        "ortho_residual": ortho_resid,
        "blocks": blocks,          # orthonormal bases, index-aligned to G
        "classes": classes,
    }


def embedding_irrep_content(E, blocks):
    """Fraction of the embedding's squared Frobenius norm lying in each
    isotypic block. E is (m x d); its columns are functions on G in the same
    index order the blocks use. Returns a list aligned to `blocks` (which the
    caller orders), and the residual outside all blocks (should be ~0)."""
    total = np.sum(np.abs(E) ** 2)
    fracs = []
    for B in blocks:
        # projection of each column onto span(B): ||B B^H col||^2
        P = B @ B.conj().T
        proj = P @ E
        fracs.append(float(np.sum(np.abs(proj) ** 2) / total))
    captured = sum(fracs)
    return fracs, float(1.0 - captured)
