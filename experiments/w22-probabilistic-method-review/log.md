# W22 log — Alon–Spencer review (2026-08-29)

## What was done
1. Read context: `memory/SESSION-STATE.md`, `memory/NOTES.md` (results ledger), paper §Random and §Alon (Thms 5, 8–11,
   negative results (i)–(iii)).
2. Read the book (PDF page = book page + 18): TOC; Ch. 1–8 complete; 10.1–10.3; 15.7; Appendix A; all Probabilistic
   Lenses; index (no entries for "permutation", "increasing subsequence", "Hammersley", "Ulam"; the only LIS material is
   the Talagrand example on pp. 120–121 and Ex. 1.10 on p. 17).
3. Derived the orders of `μ` and `Δ` for the copy count at `N = Ck²` (heuristic `Δ_j/μ² ≈ c_j C(k,j)(k)_j/N^j`) and then a
   rigorous lower bound `Δ ≥ (1−o(1))μ²/C` for any family of cell-configuration events (Prop. B.1 in `review.md`),
   which caps every Ch. 8 inequality at exponent `C/2`.
4. Wrote `secmom.c` (exact `E X²` for the number of copies of `π` in a uniform permutation of length `n`, via
   `A_u = #{(ρ, I, J)}` brute force over `S_u`, `u ≤ 2k`) and ran it for `k = 4` (1234, 2143, 1324, 2413) and `k = 5`
   (12345, 21435, 25314, 31524), `n` up to `6k²`. ~20 s per `k = 5` pattern. Data in `secmom_k*.out`.
   Findings: `Δ_1/μ² = c_1 k²/n` with `c_1 = 1.37` (identity) vs `0.99` (25314); `c_j ≈ 1.3–1.5·j!` for the identity,
   `≈ 1–3` for random-like patterns; `E X²/μ²` at `C = 1`: 2.07 (identity) vs 1.29 (25314) for `k = 5`.
5. Wrote `review.md` (executive summary + per-technique sections with page references + dead ends + list of the book's
   random-permutation material).

## Main conclusions (details in review.md)
- Provably capped at `N = Ck²`: Janson/extended Janson/Suen/Brun (exponent `≤ C/2`), Talagrand (`≤ C/4` for
  disjoint-copy functionals; speed `k` at best), Azuma-type (`≤ C/2`), Kim–Vu (vacuous), LLL for the union (existence
  only, reduces to FKG).
- Worth pursuing: (1) certificate counting / entropy compression — for the identity it gives
  `Pr(LIS(Π_N) < k) ≤ e^{−N ln(C/e)}` (speed `N`) for `C > e` in three lines; proposal: antichain-cover certificates for
  periodic shuffles and block-grid patterns to remove the `poly(r)` in Thm 9's threshold; (2) measure the slack of the
  union bound `R = E[#missing]/Pr(#missing > 0)` at `k = 7–9`; (3) exact `c_j(π)` diagnostics for "identity hardest".

## Not done / caveats
- The heuristic `Δ_j/μ²` formula is stated for the label (Poisson) model; the rigorous cap (Prop. B.1) is in the cell
  model, which is the one where Janson applies. Both agree numerically at `k = 4, 5`.
- The identity certificate bound was derived, not simulated; its constant (`C > e`) is far from the truth (`1/4`) by
  design (non-canonical covers).
- No changes to the paper or to other experiment directories; nothing committed.
