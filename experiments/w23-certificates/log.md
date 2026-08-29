# W23 — certificate counting for absence of block-grid / periodic patterns

## Plan
1. Prove Pr(LIS(Pi_N) < k) <= (e/C)^N at N = C k^2 via Dilworth covers; quantify loss vs true threshold C=1/4; try canonical covers.
2. Fixed-strip model: absence certificate for periodic word (12..r)^{k/r} and G(r,h); count certificates; derive speed and f(r).
3. Free model via union over strip boundaries.
4. Numerics vs w11 tg.c for r=2,3.
Record dead ends.

## Log
- [start] created dir; reading w22 review §A.1, §B.8, w11 proof §0-2,§4, paper notes.
- Read inputs. Key facts: w22 B.8 gives (k-1)^N/(floor(N/(k-1))!)^{k-1}; W11 Thm 2.2 threshold 8(r+1)ln(2er^2(r+1))k^2, speed N/(4r^2(r+1)); Prop 3.1 lower bound e^{-N/r} in fixed model; Thm 4.1 corner-greedy gives threshold pi/8 but speed only min(r,h). tg.c: `tg r h N reps seed [-free]`, output "r h N reps found exact_notfound unknown"; fixed model = equal strips height 1/r.
- Plan for step 2: fixed-strip absence certificate for (12..r)^m. Idea: in strip j the LIS-type structure is a chain; the merge-word condition is a *greedy* (leftmost) embedding — the greedy embedding of w into the point set is canonical: scan x-order, maintain per-strip "current height" ... Actually greedy: needed letter j at step t; pick leftmost point in strip j with y > last chosen in strip j and x > last chosen point overall. Absence <=> greedy fails. The greedy is a deterministic function of the point set; certificate = its trace. Count traces.

## Analysis (session 1, before writing proof.md)
### Step 1 (LIS)
- Dilworth certificate: sum over class sizes gives EXACT identity Pr(LIS<k) <= sum_n N!/prod(n_i!)^2 (n over compositions into k-1 parts). Max term at equal parts -> (e/C)^N e^{o(N)}.
- Compare DZ rate H(x) at x = 1/sqrt(C): H(x) = -1 + x^2/4 + 2ln(x/2) - (2+x^2/2) ln(2x^2/(4+x^2)); as x->0, H = -1 - 2 ln x + O(x^2) = ln C - 1 + O(1/C). So Dilworth rate ln(C/e) is asymptotically EXACT as C->inf; loss only near threshold (e vs 1/4).
- For FIXED k-1 = l and N->inf: bound sum_n N!/prod(n_i!)^2 = sum over compositions... vs Regev sum_{lambda_1<=l}(f^lambda)^2 ~ c l^{2N} N^{-(l^2-1)/2}: both l^{2N}/N! up to poly(N). For l=2: bound C(2N,N)/N!, truth Catalan_N/N!, ratio N+1 over sqrt(pi N) ~ sqrt(N). So the loss is polynomial for fixed k, exponential only when k ~ sqrt N.
- Canonical covers (patience piles): sum_a Pr(pile sequence = a) is tautologically exact; a per-a bound better than prod 1/n_i! requires the sandwich constraint top(a-1) < y < top(a), which is the RSK/Plancherel structure -> no elementary gain. DEAD END (documented).
### Step 2 (fixed strips, periodic word) -- key structural facts found
- Only the "diagonal" sub-column boxes (rc+j-1, j, b) enter Lemma 2.1: relevant area 1/r, total intensity N/r. Box grid n_0 = alpha m column groups, n_1 = beta m rows/strip: M = r n_0 n_1 relevant boxes, lambda = C/(alpha beta), tolerance B* = m^2(alpha beta - beta - r alpha), fraction f = B*/M = 1/r - 1/(r alpha) - 1/beta. Need beta > r alpha/(alpha-1): the Mirsky factor r is forced.
- Bound: Pr <= exp(-M D(f||e^{-lambda})) <= exp(-f M (lambda - ln(e/f))), f M lambda = f N/r. With beta = c r: speed (N/r^2)(1-1/alpha-1/c), threshold C > alpha c r ln(er/(1-1/alpha-1/c)). alpha=c=3: C > 9 r ln(3er), speed N/(3r^2). Improves W11 Thm 2.2 (24 r ln r, N/(4r^3)) by a factor r in speed.
- FLOOR for any deterministic box lemma: (i) the band-kill set (strip j bad on column band j) has relevant-box density exactly 1/r and blocks everything, so any lemma "B <= f M => chain" has f <= 1/r; (ii) Chernoff for Bin(M,p) is tight, so the bound is vacuous unless p = e^{-lambda} < f <= 1/r, i.e. lambda > ln r; (iii) lambda <= C (boxes at most area 1/k^2... relevant region area 1/r with >= r m^2 boxes). Hence C >= ln r is necessary for ANY deterministic-tolerance box argument: no r-independent threshold along this route (confirms W11 log 3.1 quantitatively; the remaining gap ln r vs r ln r is the Mirsky loss on product orders).
- Speed cap: Prop 3.1 gives Pr >= e^{-N/r} for ALL C, so the fixed-strip rate is <= 1/r uniformly in C: a bound of the form exp(-N(ln C - f(r))) is IMPOSSIBLE in the fixed model; ln C growth needs the free model.
- Why box method loses another factor r in speed: band-kill of the *relevant* boxes costs intensity N/r^2 (only diagonal sub-columns), whereas the true event costs N/r. Adding sub-columns doubles both |P| and the entropy: no gain (checked).
- Canonical/greedy certificates (accept column iff all strips skip <= K): blocked by a "wall" of K+1 bad boxes per column, linear cost -> speed k only. DEAD END. Molecule-level antichain covers in [n]^{r+1}: entropy n^r, hopeless for r >= 3. Level-function certificate via helical monotonicity ỹ: needs rm levels (entropy ln k per point) but only n = Ck/r points per class, bound exp(+N ln k/2): DEAD END.
- proof.md §0-§3 written. Numerics batch 1 (C=0.5..3, k=12..30, r=1..3, 1e5 reps): absence prob < 1e-5 already at C=0.75 for k>=18; only C=0.5 informative. Launched batch 2: C=0.3..0.7 step 0.05, 2e5 reps, k=12,18,24.
- Batch 2 done; §4 written (tables in proof.md). Rates: r=2,3 k-independent already at k=12..24 (speed N), ≈ 1/r × identity rate; all ≪ cap 1/r; Thm 2.1 regime (C > 50) not simulable.
- README finalized. Total CPU: 3 procs × ~5 min. Nothing committed.
