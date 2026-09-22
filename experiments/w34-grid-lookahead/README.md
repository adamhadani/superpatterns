# W34 — cross-strip lookahead and repaired grid reduction

The current [reduction](reduction.md) proves individual failure at most
k^(−A) for each fixed A>0, C>C_b^mix, min(r,h)≥log³k, and successive visits
to a strip separated by at least ηr for fixed η>0. The old fixed-window
H_b hypothesis did not imply this separation and is withdrawn.

W36 analytically proves C_b^mix→1/4. The repaired reduction therefore gives
simultaneous containment of all admissible tilted-grid shapes and their
dihedral images at (1/4+ε)k². It does not give simultaneous containment of
all row-permutation sequences satisfying the separation condition.

[proof.md](proof.md) retains the first-passage and scaling derivations;
`historical-proof.md` preserves the superseded application. `fpp.py`,
`check_dp.py` and `blocks.py` supply numerical investigations; finite-block
Monte Carlo constants in `results.md` are estimates, not interval bounds.
