# W1 search results (k-superpatterns by simulated annealing)

Tool: `sp.c` (this dir). Checker enumerates all k-subsets by DFS with O(1) incremental Lehmer-type rank
(popcount on a value bitmask), counts each k-pattern; SA moves = adjacent-position swaps and adjacent-value
swaps, updated incrementally (only subsets containing both swapped positions change). Energy = #missing + 0.4·#patterns realized exactly once.
Checker validated on: 25314 (k=3), 519472683 (k=4), Arnarson 17-perm (k=6), ζ_5..ζ_8 (Engen–Vatter) — all 0 missing;
Arnarson perm minus last entry has 42 missing 6-patterns; SA rediscovers length-17 6-superpatterns in 25k–600k moves.

All permutations below verified with `./sp -k K -c -p "..."` (0 missing).

## k=7

### n=24 (found in < 1 s each, essentially every chain, random start)
- 21 10 15 6 1 23 13 4 7 16 20 11 24 2 17 14 9 5 19 8 22 12 3 18   (seed 101, it 511)
- 11 3 23 17 6 13 21 4 10 16 7 24 19 14 1 9 22 5 12 18 15 2 8 20   (seed 110, start ζ_7 minus one entry)
- 12 17 7 24 19 1 15 4 10 22 13 6 18 3 20 8 16 5 23 11 14 2 21 9

### n=23 (found within ~1 min, 3 of 4 chains)
- 7 20 13 10 2 18 23 4 12 16 8 5 19 15 1 9 22 14 6 17 11 3 21   (seed 231, it 2242)
- 7 18 12 2 15 23 6 19 13 4 8 11 22 17 3 20 10 5 14 1 21 9 16   (seed 232)
- 10 16 2 22 6 11 19 15 5 21 12 1 9 18 4 13 23 7 17 3 14 20 8   (seed 234)

### n=22: NOT yet found (v1 SA, 12 chains × ~0.3M moves, 5 min each): best = 8 missing patterns (several chains at 8–9)
- best 8: 7 19 12 2 17 5 22 14 11 4 8 15 21 1 9 18 13 6 20 10 3 16   missing: 5462371, 5467312, 5617243, 1267543, 4356217, 5413267, 2134567, 1234567
- best 8: 18 12 2 7 15 21 5 19 13 8 1 11 16 22 9 4 17 6 14 20 3 10   missing: 2375641, 4567132, 2176543, 3217645, 6534217, 3456217, 3652417, 5342167
  (missing patterns are near-monotone / layered-ish: identity, 2134567, 2176543, ...)
- Symmetric subspaces: reverse-complement-fixed chains best 20–23; involution chains much worse (48–123). Symmetry restriction hurt here.

## k=8

### n=32 (found in seconds, random start, v1 SA)
- 9 30 23 16 3 19 6 26 14 31 4 21 12 29 7 11 17 25 5 20 28 1 13 22 27 18 32 10 2 15 8 24   (seed 321, it 1955)
- 13 26 3 31 11 16 23 8 20 12 30 6 18 27 7 1 21 29 15 4 9 22 32 19 2 14 24 10 28 5 17 25   (seed 322, it 675)

### n=31 (found in ~1 min)
- 25 21 11 4 27 8 17 19 1 13 31 5 23 16 26 10 6 29 15 20 28 3 9 14 24 2 12 30 18 7 22   (seed 311, it 3087)

### n=30 (found after 31k moves ≈ 10 min, weighted SA v2 `sp2`, seed 3001)
- 13 4 25 18 8 30 12 22 1 28 19 10 6 14 24 27 3 16 21 11 5 20 29 15 7 23 2 17 26 9
  Verified: 0 of 40320 8-patterns missing.

### n=29, 28: NOT found in the time box
- n=29: 2 chains × ~35k moves (10 min): best 12 missing.  n=28: 2 chains × 25k moves: best 61.
  (k=8 pair-move cost ≈ 5 ms at n=30; k=8 chains are ~20× slower than k=7 chains.)

## k=7, n=22: failed attempts summary (≈ 30 chains, ≈ 2 core-hours total)
- v1 SA (T 2→0.3 geometric cooling, LAM 0.3–0.4), 12 chains, 0.2–0.4M moves: best 8 (3 chains), 9, 10, 12, 17–18.
- v2 weighted SA (dynamic pattern weights + 10% transposition/insertion moves), 6 chains: best 7 (one chain), 8, 8, 10, 13, 14.
  best 7: 13 3 20 7 17 12 5 14 22 1 8 18 11 4 19 10 6 15 2 21 16 9   missing: 6723451, 7635412, 3127654, 7512346, 7123456, 5612347, 2134567
- fixed-temperature chains T∈{0.6,…,1.0}, 9 chains × 0.3M: best 12–27 (worse: high-T-then-cool schedule matters).
- seeded from the three n=23 solutions with one entry deleted, T=0.7: best 14–19.
- reverse-complement-symmetric subspace: best 20–23; involutions: best 48+.
Conclusion: n=22 for k=7 is either infeasible or needs a substantially better search; n=23 is easy (found in ≤ 40k moves).

## Structural observations
- Every solution found has LIS = LDS = k exactly (the minimum possible: must contain 12…k and k…21), i.e. its RSK shape sits in a k×k box; n ≈ k²/2 is around half the box.
- Ascending/descending run lengths are short (1–4) and irregular; the permutation plots look pseudo-random, with no zigzag/chessboard structure. Unlike ζ_k (Engen–Vatter) the solutions are not "word + tie-break" objects.
- Missing patterns in the best n=22 candidates are near-monotone (1234567, 2134567, 2176543, 1267543, …): the bottleneck at n=22 is having enough room for long monotone/layered patterns in a perm with LIS=LDS=7.
- sp(7) ≤ 23 and sp(8) ≤ 30 improve ⌈(k²+1)/2⌉ = 25, 33 by 2 and 3; with sp(6)=17 (−2), the sequence of savings vs the formula is 0,0,0,0,0,2,≥2,≥3.
