# W27 — Comparison principle (identity vs every π) at n ≍ k²

Files
- proof.md    — statements (PROVED / HEURISTIC / NUMERICAL): §0 reformulation (what Alon needs; CP ⇒ Alon; block
                splitting), §1 CP(1) false at k=4 and the rate-form conjecture CP*, §2 Theorem 2.1 (speed-N tails for
                ⊕-sums of bounded blocks incl. (21)^{k/2}; closure under ⊕; relabelling identity), §3 numerics summary,
                §4 obstructions (grids, random π) and "CP above threshold suffices".
- results.md  — tables: ln Pr(π ⊄ σ_n) for all dihedral classes, k = 4,5,6,7, excess over the identity, crossovers.
- log.md      — chronological log incl. dead ends.
- avoid.c     — exact avoider counts by generating tree (own DFS containment; validated against OEIS).
- avoid2.c + bc_core.h — same, with W21's contain_bc solver core (bc_core.h = contain_bc.c lines 13–144 with a
                "virtual insertion" dominance table) and the SMC growth estimator:
                `./avoid2 exact PATTERN NMAX`  |  `./avoid2 smc PATTERN NMAX POP SEED` → lines "n  p  ln p".
- lis_exact.py — exact Pr(LIS(σ_n) < k) by hook-length sums (validation of the SMC on the identity).
- classes.py  — dihedral class representatives (classesK.txt: pattern, orbit size).
- run_smc.sh  — scan driver; smcK/ directories hold one file per class representative.
- analyze.py  — rankings, crossovers n_×(π), per-n excess tables.

Reproduce: `gcc -O2 -o avoid2 avoid2.c -lm; ./run_smc.sh 5 38 20000 1 smc5; python3 analyze.py 5 smc5 13,19,25,31,38`.
