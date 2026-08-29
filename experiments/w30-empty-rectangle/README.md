# W30 — empty rectangles vs missing k-patterns

Question: is the number of k-patterns "killed" by one empty axis-parallel rectangle of a random σ_n (n ≈ 0.75k²)
e^{O(k)}? Files:
- `erect.c` — sampler. `./erect K N SAMPLES SEED R` prints per σ: `M | σ | (a b c d area Kc)×R | Kany Kunion Krand | Kg×9 | h0..h9`
  where the R rectangles are the R largest *maximal* empty rectangles [a,b]×[c,d] (0-based positions × values),
  Kc = # missing patterns revived by a phantom point at the centre slot of the rectangle, Kany = revived by *some* point
  of rectangle 1, Kunion = revived by at least one of the R centre phantoms, Krand = revived by a phantom at a uniformly
  random slot, Kg = revived by each of 9 phantoms on a 3×3 grid, h_m = # missing patterns revived by exactly m of the 9.
- `verify.py K N S SEED R` — brute-force cross-check of every field (itertools); passes for k = 4, 5, 6.
- `analyze.py k,n ...` — all tables of results.md from `out/k{k}_n{n}_s*.txt` (+ `out/mu_small.txt`, μ(n) at small n).
- `witness_phantom.py` — deterministic test: sp(6)=17 witness + one point, K_x over all 324 slots (proof.md §4).
- `proof.md` (theory, tagged), `results.md` (tables + verdict), `log.md` (chronology, dead ends).

Rerun (≤3 cores; k=6 ≈ 1 min per 6000 σ, k=7 n=37 ≈ 2 s/σ under load, k=8 ≈ 1 min/σ):
```
cc -O3 -march=native -o erect erect.c && python3 verify.py 5 14 20 7 3
./erect 6 27 6000 101 8 > out/k6_n27_s101.txt ; ./erect 7 37 4000 201 8 > out/k7_n37_s201.txt
python3 analyze.py 6,27 6,28 7,37 > analysis.txt ; python3 witness_phantom.py
```
