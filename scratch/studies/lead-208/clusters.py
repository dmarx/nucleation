"""Cluster dimensions: box counting of the largest geometric spin cluster."""
import numpy as np

from ising import geometric_bonds, label_clusters


def largest_cluster_masks(s):
    """Bool (B, L, L): the largest geometric (like-spin) cluster per replica."""
    br, bd = geometric_bonds(s)
    lab = label_clusters(br, bd)
    B = s.shape[0]
    out = np.zeros(s.shape, dtype=bool)
    for b in range(B):
        ids, counts = np.unique(lab[b], return_counts=True)
        out[b] = lab[b] == ids[np.argmax(counts)]
    return out


def box_counts(mask, eps_list):
    """Number of eps x eps boxes (aligned grid) that meet the set, per replica.

    mask: bool (B, L, L); each eps must divide L. Returns (B, len(eps_list)).
    """
    B, L, _ = mask.shape
    res = []
    for e in eps_list:
        blocks = mask.reshape(B, L // e, e, L // e, e).any(axis=(2, 4))
        res.append(blocks.sum(axis=(1, 2)))
    return np.stack(res, axis=1)
