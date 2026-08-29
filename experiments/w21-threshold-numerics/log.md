# W21 threshold numerics — log

## Start
Read w16 proof.md §4, log.md, contain_mrv.c, contain_gen.c.  Machine load at start ≈ 19 (other agents + SAT job);
I will use ≤ 4–6 processes at a time.
Plan: new solver contain_bc.c = contain_mrv + 2D bounds consistency (position chain and rank chain propagate
min/max feasible position/value of every unplaced element to its neighbours, iterated to a fixpoint; O(k log n)
per pass via the dominance-count table), same cell-count prune, MRV branching.  Validate vs contain_gen (k ≤ 12)
and vs an LIS oracle for the identity; then thresholds for k = 20, 24, 28, 32.

## contain_bc.c written and validated
- 2-D bounds consistency (position chain + rank chain, binary searches on the dominance table) + cell-count prune
  + per-cell LIS/LDS prune (points of a gap cell must have LIS ≥ LIS(sub-pattern in the cell), same for LDS).
- validate.py: 56 000 per-sample comparisons vs contain_gen (k = 6..12, random π + identity, n around threshold):
  0 mismatches.  validate_lis.py: identity vs LIS oracle (lis_v.c, same RNG stream), 300 samples each at
  (k,n) = (20,135),(24,190),(28,255),(32,330): 0 mismatches.
- Speed (1 core, loaded machine): k=20 n=135: contain_mrv 85 s / 40 samples (id+1 rand); contain_bc 0.02 s.
  Identity is now trivial (LIS prune fires at the root).  Random π: k=24 n=185 ≈ 2 ms/sample; k=28 n=225 ≈ 12 ms;
  k=32 n=300 ≈ 50–90 ms/sample per pattern.  Before the LIS prune the identity cost 8 s/sample at k=28 (52 M nodes).
- Bug found and fixed while developing: the first version of the LIS prune applied it to singleton cells only
  (rep[] recorded the last element of the cell instead of the first); the bug was conservative (never wrong,
  only useless) and node counts exposed it.
- Patterns: pats.py; random.seed(100+k) then 8 shuffles — the first 4 coincide with W16's rand0..3.

## Sweeps launched (sweep.py, 2000 samples per point, seed 1000+n, all patterns on the same samples)
k=20: n = 100..165 step 5;  k=24: n = 145..215 step 5.
