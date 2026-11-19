---
status: Read
paper: LIT-tmp8sgre
title: 'Omidvar and others 2025 — Racetrack computing with a topological boundary ratchet'
version: 1
history:
- version: 1
  date: '2026-11-19'
  note: >-
    LIT records DOI 10.1103/jw9p-s3kk (Phys. Rev. Lett. 2026); publisher
    copy not tried. Found an arXiv version by the same authors via the arXiv
    API title search (export.arxiv.org, no email sent): arXiv 2509.01706,
    "Racetrack computing with a topological boundary ratchet", Omidvar,
    Bestler, Zahedi Fard, Zilberberg, Serra-Garcia. The API lists only v1
    (2025-09-01) and gives no journal_ref or DOI, so its identity with the
    PRL rests on the matching title and authors. URL read:
    https://arxiv.org/pdf/2509.01706v1, HTTP 200, PDF. Kind of copy: arXiv
    preprint, the authors' manuscript (step 5, arXiv). Fetched 2026-11-19;
    nothing stopped the fetch. Text extracted with pdftotext to dl/text.txt.
    Read: main text and Figs. 1–4; Appendix D opening; Appendix E (boundary-
    mode renormalization under a second domain) set-up and assumptions.
    Skipped: Appendices A–C (numerical methods, experimental methods, local
    bias), most of Appendix D's algebra; the Supplementary Information is
    not in the arXiv PDF. Doubt: v1 predates the PRL by six months and may
    differ from it. Verdict on the source's characterization ("information
    transport by a topological boundary ratchet in a metamaterial, without
    learning"): accurate. "Topological" refers to the excitation band
    polarization that produces the wall mode. The transport itself is
    instability-driven, and the authors say it is not Chern-number
    transport.
date: '2026-11-19'
---
<!-- inactive-ok-file: CLAIM-606 THEORY-1408 THEORY-1415 THEORY-1893 — Proposed; cited in this filing of 2026-11-19 -->
<!-- inactive-ok-file: LIT-tmp01nqp — Unfetched; cited in this filing of 2026-11-19 -->

# NOTE-tmp9n17l: Omidvar and others 2025 — Racetrack computing with a topological boundary ratchet

## Contribution

An experiment and model of a mechanical "racetrack memory" (arXiv 2509.01706 v1, 1 Sep 2025; published as Phys. Rev. Lett. 2026, DOI 10.1103/jw9p-s3kk, whose text was not read). The device is a chain of polymer beams. Strongly compressed main beams are bistable and store a bit as a buckling direction. Weakly compressed coupling beams link them. A cyclic compression pattern with a four-site period moves domain walls, and so stored bits, by one unit cell per cycle in a quantized way. The authors trace the motion to a ratchet. A boundary mode localized at the wall between two domains is softened by the opposite domain's "pressure" until it goes unstable, and the wall then hops. They distinguish this from Chern-number pumping. They also simulate NAND, NOT, buffer and half-adder circuits built from branched racetracks.

## Key results

- **Claim** (abstract): "digital information is encoded in buckling domains and transported in a quantized manner via cyclic loading." "neighboring domains act as different topological pumps for their Bogoliubov excitations, so their interface hosts topological boundary modes." "Cyclic loading renders these modes unstable through interdomain pressure, which in turn drives the motion of the domain wall."
- **Why not an ordinary pump** (p. 1): topological pumps "adiabatically move linear excitations, which are short-lived".
- **Observation** (Fig. 1): after a full cycle of the external compression pattern, the soliton is shifted by one unit cell. "If the static compressive displacements β1 and β2 are exchanged, the direction of propagation reverses".
- **Chern number not the mechanism** (p. 2–3): when the two modulations are tuned together as in the experiment, "the Bogoliubov bulk bands close during the pump cycle and the Chern number becomes ill-defined". The simulations identify "a so-called topological ratchet mechanism [27], where wall motion is triggered by instabilities rather than by Chern number transport."
- **Still topological, in a weaker sense** (p. 3): "Although distinct from a conventional topological pump, the ratchet mechanism remains topologically rooted." Boundary modes appear in the gaps "due to nonvanishing bulk polarization that develops as θ is varied."
- **Interface versus edge** (p. 3): "Unlike a vacuum edge, the opposing domain exerts an additional" pressure, and "this pressure softens the boundary-mode frequency until it becomes imaginary, at which point the wall shifts by two sites".
- **Measured softening** (Fig. 3): as the wall approaches the central beam, "we observe an additional peak in the spectrum, whose frequency goes to zero right before the domain wall advances." Principal component analysis shows that "the observed additional peak is indeed localized at the domain wall".
- **Logic, simulated only** (Fig. 4): a NAND gate and a half adder from tight-binding simulations. "Although these simulations are based on a tight-binding model, negative couplings and branching geometries can be physically implemented".
- **Use** (p. 5): "our metamaterial can operate on a continuous input stream of information", whereas earlier buckling computers needed resetting after each iteration.
- **Approximation in the boundary-mode derivation** (Appendix E): "We assume that the first domain is unaffected by the presence of the domain wall".

## Assumptions

- A tight-binding model with on-site quartic nonlinearity and nearest-neighbour harmonic coupling (eq. 1). A standing (DC) compression makes the main beams bistable, and a cyclic (AC) compression sets the pump phase θ.
- Quasi-static driving: the system relaxes to equilibrium at each θ.
- Appendix E's boundary-mode renormalization keeps local nonlinearities at the boundary site, linearizes elsewhere, and treats the other domain as unaffected.
- The logic circuits are tight-binding simulations with negative couplings and local biases, not built devices.

## Concepts

- **Racetrack memory**: information stored in domains and moved along a track, here without magnetic fields or currents.
- **Bogoliubov excitations**: linear fluctuation modes about a domain's buckled state. Their bands can carry a Chern number when the two modulations are varied independently (Appendix D), but not along the experimental path.
- **Topological boundary ratchet**: directed, quantized wall motion driven by successive instabilities of a wall-localized mode, each hop advancing the effective pump phase by π.
- **Interdomain pressure**: the coupling term from the opposite domain that renormalizes and destabilizes the boundary mode. This is the difference between an interface and a vacuum edge.

## Bearing on the record

- [THEORY-1893](../theory.d/THEORY-1893.md): supports, with a different group, geometry and use. Bistability comes from buckling under a standing compression, and domain walls separate regions of opposite buckling, as in Zhang et al. Here the walls are moved, not static, and the bistability (and so the stored bit) exists only while the DC compression holds. It does not meet [THEORY-1893](../theory.d/THEORY-1893.md)'s promote_when: no kink–antikink lattice or stepwise count growth is tested.
- [THEORY-1408](../theory.d/THEORY-1408.md): qualifies its reach. The interface hosts localized boundary modes attributed to bulk polarization, but the transport is not index-protected. The authors say the Chern number is ill-defined on the experimental path and that motion is triggered by instability. The interface mode also differs from the vacuum-edge mode, because the neighbour's pressure destabilizes it. This is not a Kane–Lubensky zero-mode count, and it does not meet [THEORY-1408](../theory.d/THEORY-1408.md)'s promote_when.
- [QUESTION-tmp57ji2](../questions.d/QUESTION-tmp57ji2.md): a partial case of the back-action the question asks about. A mode bound at the wall goes soft, and its instability moves the wall: the hosted mode determines where the defect is. But the mode is the wall's own fluctuation mode, not a separate field, and it moves the wall rather than maintaining it. The wall's existence is maintained by the external DC compression. Leaves open the maintenance half.
- [QUESTION-378](../questions.d/QUESTION-378.md): supports the held point that coupling, not juxtaposition, creates new interface behaviour (Jules et al., [THEORY-1415](../theory.d/THEORY-1415.md)). The new interface behaviour (a soft mode, then a hop) arises from the pressure one domain exerts on the other. A vacuum edge of the same domain does not show it.
- [CLAIM-606](../claims.d/CLAIM-606.md): qualifies the use of "topological". The stored bit persists by bistability under a standing supply (the DC compression). The "topological" in the title refers to the excitation band polarization at the wall, not to a conserved charge of the wall. This is another case for the qualification already in the claim's note of 2026-11-15 (persistence only while a standing compression keeps the states degenerate).
- [LIT-tmp01nqp](../literature.d/LIT-tmp01nqp.md) (Iqbal and Welling, defects propagating information in deep networks, Unfetched): the comparison A15 drew. Here domain walls transport information along a track under an imposed cyclic load, with nothing learned.

## Limitations

- The text read is arXiv v1 (2025). The PRL version (2026) may differ, and the arXiv API lists no later version.
- Read: main text, Figs. 1–4, Appendix D's opening and Appendix E's derivation set-up. Skipped: Appendices A–C (numerical and experimental methods, controlling the local bias), most of Appendix D's algebra, the Supplementary Information (not in the arXiv PDF).
- One experimental device. The logic and the microfabrication layout are numerical or conceptual.
- The boundary-mode account rests on an approximation that treats the opposite domain as unaffected by the wall.
