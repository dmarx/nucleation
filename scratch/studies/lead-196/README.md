# LEAD-196 study files

`chesson_overlap.py` checks that Chesson's overlap ρ, sensitivity s and
average fitness κ for MacArthur's consumer-resource model (Chesson 2011,
Table 1) are, in CLAIM-369's notation with u_jl = c_jl √(v_l K_l / r_l),
b_l = √(v_l K_l r_l) and cost μ_j: ρ = the cosine of u_j and u_k,
s_j = ‖u_j‖, κ_j = (Uᵀb − μ)_j / ‖u_j‖; that his eq. (1) holds; and that
a rare species' growth against a lone resident is ‖u_i‖(κ_i − ρκ_j),
in the reduced form and in the full consumer-resource model while every
resource stays positive.

Rerun:

    python3 -I chesson_overlap.py
    python3 -I -m pytest -q -p no:cacheprovider test_chesson_overlap.py

(numpy, scipy, pytest; CPU, about a second.)
