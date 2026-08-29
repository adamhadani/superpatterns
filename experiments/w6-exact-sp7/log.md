# W6: exact question "does a 7-superpattern of length 22 exist?" — log (2026-08-29)

## Status in one line
NOT settled. sp(7) ∈ {22, 23} remains open after this time-box. The exact SAT/CEGAR method built here is
validated on k=4,5 (reproduces sp(4)=9, sp(5)=13 with UNSAT certificates for n=8, n=12) but is far too slow
at (k,n)=(6,16) — a single CEGAR iteration takes minutes — so (7,22) is out of reach with this encoding.
Runs left going in the background (see "Still running").

## Method evaluation
### (B) DFS with per-pattern prefix pruning — rejected before coding
Building σ left-to-right by relative-order insertion, a prefix τ (length m, r = n−m to go) can be extended to a
solution only if every π ∈ S_k has a prefix π[:j] ⊂ τ with k−j ≤ r; in the insertion model value-gaps are
always available, so this is the *exact* per-pattern feasibility test, and it is weak: it bites only when
r ≤ k−2, i.e. at depth m ≥ n−k+2 = 17 for n=22. Number of prefixes of length 17 ≈ 17! ≈ 3.5·10^14, ÷8 for
symmetry — hopeless; the same estimate at (6,16) gives 12!/8 ≈ 6·10^7 nodes at depth 12 but then all
the fan-out (13·14·15·16) with weak pruning: feasible for k=6 but the scaling to k=7 is >10^6× worse.
Not pursued.

### (A) SAT + CEGAR — implemented: `spsat.py` (pysat/CaDiCaL 1.9.5, venv from work/w4)
Encoding ("lt"):
- order matrix lt[p][q] (p<q ⇒ "σ(p)<σ(q)"), C(n,2) vars, with transitivity (2·C(n,3) clauses) ⇒ exactly
  the total orders on positions = permutations. No permutation matrix is needed.
- per pattern π ∈ S_k: prefix-chain vars a[i][p] = "entry i sits at position ≤ p" (k·n vars, monotone chains,
  entry i+1 strictly right of entry i), and for each pair of pattern entries that are *consecutive in value*
  (k−1 pairs; transitivity supplies the rest) and each position pair (p,q): a-literals ⇒ lt literal.
  ≈ (k−1)·C(n,2) + 3kn clauses per pattern (≈1.5k clauses at n=22,k=7).
- CEGAR loop: start with the 2·2^(k−1) layered/co-layered patterns (`--init layered`) or additionally all
  patterns within 3 inversions of monotone (`--init near`); solve; decode σ from lt; run the C checker
  (`../w1-search/sp -k K -c -p ...`) to list missing patterns; add them all (or `--batch` of them); repeat.
  UNSAT ⇒ no k-superpattern of length n (under the stated symmetry assumption).
- Symmetry breaking (`--sym`): `first` = σ(1)<σ(n) (valid: complement flips it). `rc` = σ(1)<σ(n) AND
  pos(1)+pos(n) ≤ n+1 (valid: reverse-complement preserves the first condition and negates the second).
  NOTE: the combination "σ(1)<σ(n) and pos(1) in the left half" (`--sym both`) is NOT a valid symmetry
  reduction (complement moves the entry 1 to n); those runs were killed and are not used for any claim.
- Alternative encoding `--enc pv` (permutation matrix + position chains + value chains per pattern) was
  tried: k=5 n=12 did not finish in 10 min (vs 12 s for "lt"). Abandoned.
- Independent checker `check.py` (pure Python, enumerates all C(n,k) subsets) re-verifies every witness.

## Benchmarks (all on this machine, one core per run)
| k | n | init | sym | result | iterations / patterns in final instance | time |
|---|---|------|-----|--------|----------------------------------------|------|
| 4 | 8 | layered | none | UNSAT | 1 / 14 (layered patterns alone suffice!) | 0.0 s |
| 4 | 9 | layered | none | SAT 3 6 5 9 2 7 4 1 8 (verified 0 missing) | 1 / 14 | 0.0 s |
| 5 | 12 | layered | none | UNSAT | 14 / 80 | 12 s |
| 5 | 12 | layered | rc | UNSAT | 6 / 73 | 19 s |
| 5 | 12 | near | rc | UNSAT | 4 / 71 | 23 s |
| 5 | 12 | all 120 | rc | UNSAT | 1 / 120 | 20 s |
| 5 | 13 | layered | none | SAT 9 6 2 13 10 4 7 12 8 3 1 5 11 (verified) | 5 / 60 | 0.6 s |
| 5 | 13 | near | rc | SAT 3 10 6 13 4 8 11 9 1 5 12 2 7 (verified) | — | ~1 s |
| 6 | 16 | layered | none | it 1 (62 pats) 57 s; it 2 not finished after 15 min | — | running |
| 6 | 16 | layered | first | it 1: 272 s | — | running |
| 6 | 16 | layered | rc | it 1: 16 s; it 2 >10 min | — | running |
| 6 | 16 | near | rc | it 1 (~130 pats) >15 min | — | running |
| 6 | 16 | all 720 | rc | no answer after 15 min | — | running |
| 6 | 17 | layered | none | it 8: 278 pats, 2 missing at 564 s (SAT side, converging) | — | running |
| 7 | 22 | layered | first | it 1 (126 pats): 63 s, 977 missing | — | running |
| 7 | 22 | near | rc | it 1 (226 pats): 133 s, 389 missing | — | running |
| 7 | 23 | layered | none | it 3: 770 pats, 42 missing at 992 s | — | running |

So sp(4)=9 and sp(5)=13 are re-proved exactly by this code (sanity check of the encoding/decoder, both
directions), but the cost jumps by >100× from (5,12) to (6,16): the (6,16) instance with only the 62 layered
patterns already needs minutes per solve, and the UNSAT proof of Pantone's result would need ~200–300
patterns and probably dozens of iterations. Extrapolating the (5,12)→(6,16) growth, (7,22) is many orders of
magnitude beyond this encoding on 12 cores. The `--init all` full encodings (1 M clauses at (6,16),
≈7.5 M clauses at (7,22)) are loadable but showed no sign of finishing either.

## What is proved (certified) in this work package
- Nothing new about sp(7). Re-proved: no 4-superpattern of length 8 (14 layered patterns already UNSAT —
  a cute fact: the layered 4-patterns alone force length ≥ 9), no 5-superpattern of length 12.
- Two new explicit 5-superpatterns of length 13 and a 4-superpattern of length 9 (verified twice).
- Validity caveat recorded: only `--sym none|first|rc` give sound UNSAT proofs.

## What is estimated (not proved)
- The encoding is the bottleneck, not the CEGAR loop: even the SAT direction ((6,17), (7,23)) crawls once
  ≥250 patterns are in the instance, while SA finds 23s in seconds. The hard core (SA's residual missing
  patterns at n=22: 1234567, 2134567, 7123456, 5612347, 2176543, …) is near-monotone, consistent with the
  (4,8) observation that layered patterns alone are already restrictive; at k=7 the layered+near-monotone
  set (226 patterns) is satisfiable at n=22 (389 missing in the model), so any UNSAT core must be larger.

## Ideas not executed (for a follow-up with more time)
1. Pattern-set UNSAT core hunting: at (6,16) find a *minimal* pattern subset that is UNSAT (with CaDiCaL
   assumptions); if the core at k=6 consists of layered/near-monotone patterns, the analogous k=7 family
   (~300 patterns) might be UNSAT at n=22 — a much smaller instance than full CEGAR.
2. Use the structural fact LIS=LDS=k: split (7,22) by the RSK shape / by pos(1), pos(22), σ(1), σ(22) into
   many small cubes ("cube-and-conquer") over 12 cores; each cube is still a (7,22)-sized instance, so this
   only helps if the per-cube time is hours, which the (6,16) timings do not support.
3. Better containment encoding: DP over positions with state = matched prefix length is exact for *words*
   (W4) but not for permutations; a correct DP needs value information. A "grid" encoding (positions AND
   values both chained, `--enc pv`) was strictly worse.

## Still running (output files in this directory; check with `tail -n1 *.txt`)
- k6n16_none.txt, k6n16_first.txt, k6n16_rc.txt, k6n16_rc_near.txt, k6n16_rc_all.txt — an "UNSAT" line in
  any of these is a (re)proof of sp(6)=17 by this method (sym first/rc are sound).
- k6n17.txt, k7n23.txt — SAT side; should end with a FOUND line (witnesses; verify with check.py).
- k7n22_first_s3.txt, k7n22_rc_near_s1.txt, k7n22_rc_near_s2.txt — the real question; "UNSAT" would prove
  sp(7)=23, "FOUND" would give a 22 (must be verified with `sp -k 7 -c -p` and `check.py 7 "..."`).

## Addendum: UNSAT-core hunting (`core.py`, selector literals + deletion-based minimisation)
- (4,8): minimal core of 14 patterns = exactly the layered + co-layered 4-patterns
  {1234,1243,1324,1432,2134,2143,2341,3214,3412,3421,4123,4231,4312,4321}: no permutation of length 8 with
  σ(1)<σ(8) contains all of these (so, by complement symmetry, no 8-perm contains all layered and
  co-layered 4-patterns).
- (5,12): first core 60 of 120 patterns after 188 s; minimisation running → core_k5n12.txt
  (ends with "MINIMAL CORE ...").  If the k=5 core is again (co-)layered/near-monotone, the k=6/k=7
  analogue (≈130/226 patterns, `--init near`) is the instance to attack first — but at (6,16) that instance
  already takes >15 min per solve here, and at (7,22) it is SAT (389 missing), so more patterns are needed.
