# W4: alphabet [k+1] superpatterns and Gupta rosaries — log (2026-08-29)

## Tools
- `fkr_sat.py`  : exact f(k;r) via SAT (pysat/CaDiCaL 1.5.3 in ./venv). Encoding: one-hot letters x[i][l];
  for every target word t = s∘π (π∈S_k, s an increasing injection [k]→[r]) reachability vars
  R[i][j] ("t[:j] embeds in w[:i]") with R[i][j] → R[i-1][j] ∨ (R[i-1][j-1] ∧ x[i][t_j]);
  per π clause OR_s R_final. Symmetry break: w[0] ≤ ⌈r/2⌉ (complement). Witnesses re-verified by
  independent greedy checker `contains_all`.  Sanity: reproduces f(k;k)=7,12 (Newey) for k=3,4.
- `rosary_sat.py`: exact r(n) via SAT, same idea on the cyclic word (start j must carry π(1); embed
  π(2..n) in the next r−1 cyclic positions). Symmetry break: w[0]=1 and letters first appear in
  increasing order (relabeling + rotation). Witnesses re-verified by `is_rosary`.
- `roscheck.c` : fast C rosary checker (DFS over permutation prefixes carrying live start-set).
- `rossa.c`    : simulated annealing over cyclic words using roscheck.

## Runs / results (chronological)
### Part 1: f(k;r) (SAT, all UNSAT/SAT steps re-verified; witnesses verified by independent checker)
- f(2;3)=3   (232)              Miller bound 3  -> equality
- f(3;4)=6   (241323)           Miller bound 6  -> equality  (note f(3;4)=6 > sp(3)=5!)
- f(4;5)=10  (2435142314)       Miller bound 10 -> equality  (> sp(4)=9)
- f(5;6)=15  (n=13 UNSAT 19s, n=14 UNSAT 166s; Miller word 135642135642135 is a witness) -> equality (> sp(5)=13)
- f(6;7): n=17.. running (see below).
- Sanity: f(3;3)=7, f(4;4)=12 (Newey) reproduced.
- f(3;5)=5 (25314), f(3;6)=5, f(4;6)=9 (314625314), f(4;7)=9 (371426315): equal to sp(3), sp(4) already at r=k+2.
- f(5;7): n≤12 UNSAT (n=12 took 357s), n=13 running.  sp(5)=13.
Observation: f(k;k+1) = (k^2+k)/2 exactly for k<=5, strictly above sp(k) for k=3,4,5; one more letter (r=k+2) already recovers sp(k) for k=3,4.
Lower-bound heuristic for r=k+1: word over [k+1] with letter multiplicities r_1..r_{k+1} contains at most r_1...r_{k+1} * sum 1/r_l perms (EV survey),
which for n=(k^2+k)/2 - 1 is still >= k!, so the counting bound is NOT what forces equality; the SAT proofs are "structural".

### Part 2: rosaries r(n) (SAT exact; witnesses verified)
- r(2)=2 (12), r(3)=4 (1232), r(4)=8 (12341232), r(5)=12 (123432152435).  floor(n^2/2)= 2,4,8,12  -> equality for n=2..5.
- r(6): r=14,15 UNSAT (28s,146s); r=16 running. LZ give a 17-rosary, so r(6) in {16,17}.
- r(7) <= 24 = floor(49/2): SA found four 24-rosaries in seconds, e.g.
    1,7,6,5,3,4,1,2,5,6,7,4,3,2,1,5,4,3,7,6,1,5,2,4   (verified by python is_rosary)
  Structured 24-rosary: (1..7)(1,2,3,4)(7..1)(7..2)  [also X=1,2,4,3 works; only these 2 of 7^4 X's].
  r=23: SA (4 seeds, 3M iters) stuck at >=14 missing; SAT r=23 running (15M vars).  So r(7) in {?..24}; Gupta bound holds for n=7.
- r(9) <= 40 = floor(81/2): (1..9)^2 (1,2,3,4,5) (9..1) (9..2). Among increasing X of length 5 this is the ONLY one that works.
  (SA from LZ-minus-one-letter also found irregular 40-rosaries, e.g. (1..9)^2 (1,2,4,3,5)(9..1)(9..2).)
- r(11) <= 60 = floor(121/2): (1..11)^2 (1..6) (11..1)^2 (11..2), verified by roscheck (7s).
- n=13: (1..13)^3 (1..7) (13..1)^2 (13..2), length 84=floor(169/2): check running (~20 min).

CONJECTURAL CONSTRUCTION (odd n, m=(n-1)/2):  R_n = (1..n)^{floor(m/2)} (1..m+1) (n..1)^{ceil(m/2)-1} (n..2),
  length = floor(n^2/2). This is LZ's Theorem-2 word with the partial block (1..3k) resp. (1..3k+2) shortened to (1..2k+1) resp. (1..2k+2).
  Verified: n=5 (this is LZ's own n=5 word), 7, 9, 11.
  BUT LZ (Sec. 3) state it fails for n=21 (k=5) and give an explicit permutation for n=33; I re-verified their n=33 claim:
  pi=1,5,4,3,2,7,6,11,10,9,8,18,...,23,14,13,12,25,24,26,17,16,15,28,27,29,...,33 is NOT contained in (1..33)^8 (1..17)(33..1)^7(33..2)
  (but is in LZ's (1..24) version).  So R_n is NOT a proof route for all odd n; it is a small-n phenomenon (works n<=11, maybe 13).
  Proof status for odd n: OPEN. No general construction found; the natural modification of LZ provably fails at n=33.

### Further structured tests (n=7,9,11)
- n=7, word (1..7) X (7..1)(7..2), |X|=4, all 7^4 X: exactly 5 work: 1234, 1243, 1342, 1432, 2341.
- n=9, word (1..9)^2 X (9..1)(9..2), |X|=5, all 9^5 X (run killed ~70% through): found 12312, 12321, 12345, 12354, 12435, 12453, 12534, 12543, 13231 (+ possibly more with X[0]>1).
- n=11, word (1..11)^2 X (11..1)^2 (11..2), |X|=6: increasing X with X[0]<=5 fully enumerated -> only X=123456 works.
  Small-letter variants 123123 (518903 missing), 123412 (34716 missing), 123454, 123451, 123432, 123212: all FAIL.
  So the n=9 "small-letter" X's (12312 etc.) do not generalize; only the prefix-interval (1..(n+1)/2) survives to n=11, and that one dies at n=33 (LZ).
- n=13 checks (84-letter candidates) still running at time of writing: ros13.txt = (1..13)^3(1..7)(13..1)^2(13..2); ros13b.txt = (1..13)^3(1234)(123)(13..1)^2(13..2).

### Still running when the time-box ended (outputs in out_*.txt)
- fkr_sat.py 6 7 17  (f(6;7): is n=17..20 UNSAT?)  -> out_k6_r7.txt
- fkr_sat.py 5 7 (n=13)                             -> out_kplus23.txt
- rosary_sat.py 6 (r=16)                            -> out_ros6.txt   (r(6) in {16,17})
- rosary_sat.py 7 23 was killed (15M vars, too heavy); r(7) in [?,24], SA suggests 24.
