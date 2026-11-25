"""Mechanism check for the generic-symmetric divergence (LEAD-137).

Hypothesis: the informative-across-buffer direction u_info concentrates on R's
BORDER nodes (those with an edge to the buffer), whereas the gap-isolated block
mode u_block is the spread-out collective mode; so they diverge when the border
is a small heterogeneous subset (generic graph) and agree when every node is a
border node (lattice-like homogeneous slab). We measure, per item, the mass of
each unit vector on the border nodes and compare.

python3 -I mechanism.py
"""
import os
import sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import study as S


def border_mass(cfg):
    W, labels = S.build_system(cfg['K'], cfg['n'], cfg['p_in'], cfg['w_in'],
                               cfg['w_cross'], cfg['mode'], cfg['seed'],
                               cfg.get('homogeneous_border', False))
    A = S.scale_to_radius(W, cfg['rho'])
    Sigma = S.stationary_cov(A)
    idx_R, idx_B, idx_E = S.partition(labels, cfg['K'], cfg['buffer_width'])
    u_info, _, _ = S.info_direction(Sigma, idx_R, idx_E)
    u_block, _, _ = S.block_direction(A, idx_R)
    # border nodes of R: R-nodes with any coupling to the buffer community
    Rset = set(idx_R.tolist()); Bset = set(idx_B.tolist())
    border_local = []
    for li, g in enumerate(idx_R):
        if any((A[g, j] != 0 or A[j, g] != 0) for j in idx_B):
            border_local.append(li)
    border_local = np.array(border_local, int)
    m_info = float((u_info[border_local] ** 2).sum()) if border_local.size else 0.0
    m_block = float((u_block[border_local] ** 2).sum()) if border_local.size else 0.0
    frac_border = len(border_local) / len(idx_R)
    return m_info, m_block, frac_border, S.overlap(u_info, u_block)


base = dict(K=4, n=8, p_in=0.5, w_in=1.0, w_cross=0.1, rho=0.95, buffer_width=1)
for mode in ('symmetric', 'asymmetric'):
    for hb in (False, True):
        mi, mb, fb, ov = [], [], [], []
        for s in range(40):
            a, b, f, o = border_mass({**base, 'mode': mode,
                                      'homogeneous_border': hb, 'seed': s})
            mi.append(a); mb.append(b); fb.append(f); ov.append(o)
        print(f"mode={mode:10s} homog={hb!s:5s}  "
              f"frac_border={np.mean(fb):.2f}  "
              f"u_info border-mass={np.mean(mi):.2f}  "
              f"u_block border-mass={np.mean(mb):.2f}  "
              f"overlap={np.mean(ov):.3f}")
