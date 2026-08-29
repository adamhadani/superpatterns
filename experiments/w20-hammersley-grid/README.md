# W20 — exact constant for tilted grids (Hammersley-grid): files

* proof.md — all statements, tagged PROVED / HEURISTIC / NUMERICAL / CONJECTURE, with full proofs.
* log.md — chronology, numerics tables, dead ends (marked DEAD END).
* tg.c — exact Pareto-front DP for tilted-grid containment (copied from W11, validated there against brute
  force); added option `-iid` (i.i.d. uniform colours = Poissonised strips, instead of the balanced colouring
  induced by rigid strips in N uniform points).  Compile: `gcc -O2 -o tg tg.c`.
  Usage: `./tg r h N reps seed [-free] [-beam B] [-tau eps] [-iid]`; output `r h N reps found notfound unknown`.
* bisect.py — `python3 bisect.py r h [reps] [-free] [-iid]`: C_{1/2} = N_{1/2}/k² by 11-step bisection on C
  (default 400 samples per step, seeds 7,8,…,17); appends one line with the full trace to results.txt.
  (Note: the file name shadows the stdlib module `bisect`; scripts importing numpy from this directory must
  strip the directory from sys.path, as mfrule.py does.)
* mf.py — mean-field Bellman recursion (proof.md Prop 4.3): `python3 mf.py [n_cells] [h_max]` prints C_mf(h).
  Outputs: mf400.out (n = 400), mf800.out (n = 800).
* mfrule.py — Monte Carlo of the h = 2 mean-field rule on the real FIXED model (no artificial fill):
  `python3 mfrule.py C r reps`.  Output runF.log.
* results.txt — all bisection results (model, r, h, k, reps, C_{1/2}, trace of (C, success fraction)).
* diag88.txt — exact FIXED 8×8 runs: lines `8 8 N 40 found notfound 0` (seed 5).
* run*.sh — the job lists that were run (runA: FIXED r = 2,3,4; runC: FIXED small h; runD: FREE r = 2;
  runE: -iid h = 1,2,3; runF: mfrule; runG: -iid r = 128,64; run88: FIXED 8×8).
