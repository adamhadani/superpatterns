# W24 — union-bound slack R(n,k) = E[M]/Pr(M>0) for random σ_n (log)

Date: 2026-08-29. Dir: experiments/w24-union-slack/. Machine shared (load ≈ 35 on 12 cores at start); I use ≤ 3 processes.

## Tooling
- mslack.c: adapted from w5-random/sp.c (bitset over k! mixed-radix codes, pruned DFS over k-subsets, random seeding).
  For each random σ_n it prints "M c1 c2 ..." (M = # missing k-patterns and their codes, codes only if M ≤ DUMPMAX=5000),
  then a summary line. Seeds: rng seeded by argument (two xorshift generators, one for σ, one for seeding subsets).
- Self-test (selftest.py + mslack_stdin): the *sets* of missing codes agree with a naive Python enumeration of all
  C(n,k) subsets (patlib.missing_bruteforce) on 30 perms (k=5,n=14), 10 (k=6,n=20), 3 (k=7,n=26): 0 mismatches.
  patlib.decode/encode roundtrip checked.
- Speed (this loaded machine): k=6 ~0.01 s/σ, k=7 ~0.035 s/σ, k=8 ~0.1–0.2 s/σ, k=9 ~1.5–2 s/σ.

## Runs
- 16:05 launched 3 queues (run_queue.sh queueA/B/C.txt): A = all k=6,7,8 points; B = k=9 n=49..62; C = k=9 n=64..72.
  Grid n from ≈0.6k² to ≈1.3k². Samples: ≥2000 (k≤8), more at high n; k=9: 300–2000 (cost).
  Extra large samples at n≈t(k): k=6 n=28 (30000), k=7 n=37 (20000), k=8 n=48 (6000) for pairwise correlations.
- 16:15 appended k=5 grid (n=15..32) to queue A for a 5th point in the k-fits.
- 16:25 k=6 done; analyze.py fixed (ln 0 guard). k=6: ln R ≈ 1.9 at t(6), ≈0.4 at n=k², →0 by n≈1.1k².
- 17:31 appended extra k=9 seeds (n=58,60,62; new n=66) to queue B.
- 17:50 k=6,7 complete; k=9 n=49..64 complete. Interim: ln R at t(k) = 1.93 (k=6), 2.59 (k=7), 3.95 (k=9) ≈ 0.30·ln k!.
  At n = k²: ln R ≈ 0.4–0.5 (k=6,7); R → 1 by n ≈ 1.1k² (but Pr(M>0) < 1e-3 there, few events).
  Pairwise: ρ(π, π∘adjacent transposition) ≈ 160–230 at t(7); dihedral images ρ ≈ 20–25; random pairs ρ ≈ 12–16 ≈ E[M²]/E[M]².
  Reverse/complement pairs of the identity: 0 co-misses in 20000 samples (ρ≈0) — LIS and LDS are *negatively* related at fixed n.
  Cluster analysis added: missing set = 2–4 components (k=7, n≈t) under adjacent transpositions; largest component ≈ 70% of M.
- 18:40 k=9 n=68: one σ with M=539 of 53 events; added 'R w/o max' column.
- 19:20 queue C done; started queue D (k=8 n=46,48,50 seed 12; k=9 n=60 seed 13).
