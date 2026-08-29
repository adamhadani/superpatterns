# Witnesses and independent verification

`witnesses.txt` holds the explicit permutations behind Theorem 2 (sp(7) ≤ 23, sp(8) ≤ 30) and the structured
7-superpattern of length 24. One command re-checks all of them with a pure-Python brute force that shares no
code with the other two checkers:

```sh
python3 check_witness.py --test    # self-tests: sp(3)=5, sp(4)=9, ζ₅ (13), Arnarson's 17; damaged witnesses must fail
python3 check_witness.py --all     # every line of witnesses.txt; prints pattern counts and the file's SHA-256
```

Expected output (Python 3.14.7, macOS, 2026-08-29; ≈ 9 s CPU):

```
k=7 m=23 distinct patterns 5040/5040 (245157 subsets) -> OK
k=8 m=30 distinct patterns 40320/40320 (5852925 subsets) -> OK
k=7 m=24 distinct patterns 5040/5040 (346104 subsets) -> OK
sha256(witnesses.txt) = 42b52a6229ec8a6f2247a8798d08ffa1495c91f198cc99d8bd1de94e7e2be3e4
```

`sha256(check_witness.py) = cc6cecb98ef81849f59552e38e0fba3e7bb82426b545b7a5e908db55ff6e8864`

## Three independent checkers

| Checker | Language / method | Where |
|:--|:--|:--|
| Brute force | Python: enumerate all C(m,k) subsets, rank-standardise, count distinct patterns | `check_witness.py` (this folder) |
| DFS with pruning | C: depth-first embedding of each of the k! patterns (`sp -k 7 -c -p "..."`) | `../w1-search/sp.c` |
| Kernel-checked DFS | Lean 4: `checker_sound : checker k σ = true → IsSuperpattern k σ` proved; instances by `native_decide` | `../../formal-verification/lean/Superpatterns/{Checker,Certificates}.lean` |

The Python and C checkers use different standardisation code (rank sort vs. pairwise comparisons) and different
enumeration orders; the Lean checker's soundness is a theorem, so only Lean's `native_decide` evaluator is trusted
there (`#print axioms` in `Axioms.lean`).
