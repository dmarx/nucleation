"""LEAD-073: measure NOTE-746's F, G, M, N, Gamma and Gamma_q in a released model.

Usage (from the repository root; MODEL_DIR holds config.json, model.safetensors
and the tokenizer files, downloaded outside the repository):

    OMP_NUM_THREADS=2 python3 -I scratch/studies/lead-073/measure.py MODEL_DIR OUT.json

The tolerances are those of PREREG.md, fixed before the first real run.
"""
from __future__ import annotations

import json
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import geometry as geo  # noqa: E402
from relations import RELATIONS  # noqa: E402

PRIMARY_RTOL = 1e-3
RTOLS = (1e-2, 1e-3, 1e-4)
CTOL = 1e-3
LAM = 1e-2
TAU_V = 1e-2
PASS_WORST_OUT = 0.01


def ln_offset(gamma, beta) -> float:
    """sum_i beta_i / gamma_i. The final layer norm puts f in beta + diag(gamma) 1^perp,
    so span F is all of R^d (given generic normalized states) iff this is nonzero."""
    gamma = np.asarray(gamma, dtype=np.float64)
    beta = np.asarray(beta, dtype=np.float64)
    return float(np.sum(beta / gamma))


def _key(r: float) -> str:
    return f"{r:.0e}"


def _last(lm, ids):
    return lm.hidden(np.array([ids]))[0, -1].astype(np.float64)


def relation_vectors(lm, tok, bos, rel):
    """f(s) and f(s ^ q) for each (subject, reply) whose reply is one token."""
    subj, reply, Fs, Fsq = [], [], [], []
    for s, y in rel["pairs"]:
        yi = tok.encode(y)
        if len(yi) != 1:
            continue
        si = [bos] + tok.encode(s.strip())
        qi = tok.encode(rel["query"])
        Fs.append(_last(lm, si))
        Fsq.append(_last(lm, si + qi))
        subj.append(s)
        reply.append(yi[0])
    return subj, np.array(reply), np.array(Fs), np.array(Fsq)


def context_vectors(lm, bos, rng, n_random, len_random, n_sample, len_sample, V):
    """Context representations for F: random token strings and the model's own samples."""
    R = rng.integers(0, V, size=(n_random, len_random))
    R = np.concatenate([np.full((n_random, 1), bos), R], 1)
    fr = np.concatenate([lm.hidden(R[i:i + 8]).reshape(-1, lm.d) for i in range(0, n_random, 8)])
    S = lm.sample(np.full((n_sample, 1), bos), len_sample, rng) if n_sample else np.zeros((0, 1), int)
    fs = lm.hidden(S).reshape(-1, lm.d) if n_sample else np.zeros((0, lm.d))
    return fr.astype(np.float64), fs.astype(np.float64), S


def measure(lm, tok, bos, relations, rng, n_random=64, len_random=32, n_sample=24, len_sample=32,
            rtols=RTOLS, ctol=CTOL, lam=LAM, tau_v=TAU_V):
    t0 = time.time()
    Gm = lm.g.astype(np.float64)
    V, d = Gm.shape
    fr, fs, S = context_vectors(lm, bos, rng, n_random, len_random, n_sample, len_sample, V)
    rel_data = {name: relation_vectors(lm, tok, bos, rel) for name, rel in relations.items()}
    rel_f = [x for (_, _, a, b) in rel_data.values() for x in (a, b) if len(a)]
    Fm = np.concatenate([fr, fs] + rel_f)
    gam, beta = lm.ln_f()
    out = {"d": d, "V": V, "n_context_vectors": int(Fm.shape[0]),
           "n_random_vectors": int(fr.shape[0]), "n_sampled_vectors": int(fs.shape[0]),
           "ln_offset_sum_beta_over_gamma": ln_offset(gam, beta),
           "ln_hyperplane_residual": float(np.max(np.abs(((Fm - beta) / gam).mean(1)))),
           "settings": {"rtols": list(rtols), "ctol": ctol, "lam": lam, "tau_v": tau_v,
                        "pass_worst_out": PASS_WORST_OUT},
           "spans": {}, "relations": {}}
    _, sF = geo.span_basis(Fm, 1.0)
    _, sG = geo.pivot_span(Gm, 1.0)
    out["sv_F_rel"] = (sF / sF[0]).tolist()
    out["sv_G_rel"] = (sG / sG[0]).tolist()
    bases = {}
    for r in rtols:
        QF, _ = geo.span_basis(Fm, r)
        QG, _ = geo.pivot_span(Gm, r)
        QM, QN, cos = geo.m_and_n(QF, QG, ctol)
        QFr, _ = geo.span_basis(fr, r)
        QFs, _ = geo.span_basis(fs, r) if len(fs) else (np.zeros((d, 0)), None)
        bases[_key(r)] = (QF, QG, QM, QN)
        out["spans"][_key(r)] = {"dim_F": QF.shape[1], "dim_G": QG.shape[1], "dim_M": QM.shape[1],
                                 "dim_N": QN.shape[1], "dim_F_random_only": QFr.shape[1],
                                 "dim_F_sampled_only": QFs.shape[1],
                                 "min_principal_cos_F_G": float(cos.min()) if cos.size else None,
                                 "null_mean_out_of_M": 1 - QM.shape[1] / d}
    QFp, QGp, QMp, QNp = bases[_key(PRIMARY_RTOL)] if _key(PRIMARY_RTOL) in bases else bases[_key(rtols[0])]
    Wf, visf = geo.visibility(Gm, QFp)                       # F's directions by logit visibility
    Fu = Fm                                                   # uncentred: SIm(f)
    _, sv_gx, vt_gx = np.linalg.svd(Fu @ QGp, full_matrices=False)
    Wg, visg = QGp @ vt_gx.T, sv_gx / sv_gx[0]               # G's directions by context visibility
    out["visibility"] = {"F_by_logits_rel": visf.tolist(), "G_by_contexts_rel": visg.tolist(),
                         "n_F_below_tau": int(np.sum(visf < tau_v)), "n_G_below_tau": int(np.sum(visg < tau_v))}
    for name, (subj, rep, Fs, Fsq) in rel_data.items():
        if len(subj) < 4:
            out["relations"][name] = {"n_subjects": len(subj), "skipped": "too few single-token replies"}
            continue
        uniq = sorted(set(rep.tolist()))
        QGam = geo.reply_subspace(Gm, uniq)
        A, a = geo.fit_relation(Fs, Fsq, QGam, lam)
        r2, pred = geo.loo_r2(Fs, Fsq, QGam, lam)
        R = Gm[uniq]
        Rc = R - R.mean(0)
        model_logits = Fsq @ Rc.T
        pred_logits = (pred @ QGam.T) @ Rc.T
        truth = np.array([uniq.index(y) for y in rep])
        model_arg = model_logits.argmax(1)
        pred_arg = pred_logits.argmax(1)
        QGq = geo.gamma_q_basis(A)
        low_f = Wf[:, visf < tau_v]
        low_g = Wg[:, visg < tau_v]
        rel = {"n_subjects": len(subj), "n_replies": len(uniq), "dim_Gamma": QGam.shape[1],
               "dim_Gamma_q": QGq.shape[1], "loo_r2": r2,
               "model_acc_among_replies": float(np.mean(model_arg == truth)),
               "probe_faithfulness_loo": float(np.mean(pred_arg == model_arg)),
               "probe_acc_loo": float(np.mean(pred_arg == truth)),
               "chance": 1.0 / len(uniq),
               "Gamma_q_energy_in_low_visibility_F": 0.0 if low_f.shape[1] == 0
               else 1 - geo.energy_outside(A.T, low_f),
               "Gamma_in_low_visibility_G": 0.0 if low_g.shape[1] == 0
               else 1 - geo.energy_outside(QGam, low_g),
               "tests": {}}
        for r in rtols:
            QF, QG, QM, QN = bases[_key(r)]
            rel["tests"][_key(r)] = {
                "Gamma_in_N": geo.containment(QGam, QN),
                "Gamma_q_in_M": geo.containment(QGq, QM),
                "Gamma_q_in_F": geo.containment(QGq, QF),
                "A_energy_outside_M": geo.energy_outside(A.T, QM),
                "pass": bool(geo.containment(QGam, QN)["worst_out"] <= PASS_WORST_OUT
                             and geo.containment(QGq, QM)["worst_out"] <= PASS_WORST_OUT)}
        out["relations"][name] = rel
    out["seconds"] = time.time() - t0
    out["sampled_text_examples"] = []
    if hasattr(tok, "decode") and len(S):
        out["sampled_text_examples"] = [tok.decode(S[i, 1:]) for i in range(min(3, len(S)))]
    return out


def main(argv):
    import lmnp
    model_dir, out_path = argv[1], argv[2]
    lm, tok = lmnp.load_model(model_dir)
    bos = 50256 if lm.kind == "gpt2" else 0
    rng = np.random.default_rng(73)
    res = measure(lm, tok, bos, RELATIONS, rng)
    res["model_dir"] = os.path.basename(os.path.normpath(model_dir))
    with open(out_path, "w") as fh:
        json.dump(res, fh, indent=1)
    print(json.dumps({k: v for k, v in res.items() if k not in ("sv_F_rel", "sv_G_rel", "visibility")}, indent=1))


if __name__ == "__main__":
    main(sys.argv)
