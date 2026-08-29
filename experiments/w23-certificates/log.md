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
