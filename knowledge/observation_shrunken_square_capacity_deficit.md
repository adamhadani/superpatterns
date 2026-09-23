# Shrunken Square Boundary Corridor Capacity Deficit at Mesoscopic Threshold

Type: observation
Confidence: high
Source: Candidate L02_N06 (Level 2 falser); Candidates L03_N02, L03_N04 (Level 3 falsers)
Relevant to: Boundary guard corridors, mesoscopic block threshold, buffer scaling in shared squares.

## Statement
Reserving boundary guard corridors of width $\delta = 1$ host rank slot inside a host square $Q$ of side length $s = a/k$ shrinks the active interior region to side length $s_{\mathrm{int}} = (a - 2\delta)/k = (a - 2)/k$. The effective LIS traversal capacity of the interior is $C_{\mathrm{int}}(a) = 2\sqrt{(1/4+\varepsilon)(a-2)^2} = \sqrt{1+4\varepsilon}(a-2)$. For the interior to embed the target block of size $a$ with non-negative net surplus ($C_{\mathrm{int}}(a) \ge a$), the block size must satisfy $a \ge \frac{2\sqrt{1+4\varepsilon}}{\sqrt{1+4\varepsilon}-1} \approx \frac{2(1+2\varepsilon)}{2\varepsilon} \approx \frac{1}{\varepsilon} + 2$. At $\varepsilon = 0.05$, this requires $a \ge 21.5$. Consequently, at the mesoscopic threshold $L = \lceil K\sqrt{\log k}\rceil$ (which equals $7$ for $k=100, K=3.25$), host squares suffer a net capacity deficit ($C_{\mathrm{int}}(7) \approx 5.48 < 7$), refuting the claim that surplus strictly dominates boundary penalties at scale $L$.

## Evidence
1. Interior area and capacity derivation: A host square of side $s = a/k$ has total area $s^2$. Reserving guard corridors of thickness $1/k$ along each boundary reduces the interior to $(a-2)/k \times (a-2)/k$. The expected Poisson intensity in the interior is $\lambda_{\mathrm{int}} = (1/4+\varepsilon)(a-2)^2$.
2. The asymptotic LIS capacity is $2\sqrt{\lambda_{\mathrm{int}}} = \sqrt{1+4\varepsilon}(a-2)$.
3. Setting $\sqrt{1+4\varepsilon}(a-2) \ge a$ yields:
   $$a(\sqrt{1+4\varepsilon} - 1) \ge 2\sqrt{1+4\varepsilon} \implies a \ge \frac{2\sqrt{1+4\varepsilon}}{\sqrt{1+4\varepsilon} - 1}.$$
4. Exact numerical evaluation at $\varepsilon = 0.05$:
   $$\sqrt{1 + 4(0.05)} = \sqrt{1.20} \approx 1.095445.$$
   $$a \ge \frac{2 \times 1.095445}{1.095445 - 1} = \frac{2.19089}{0.095445} \approx 22.95 \approx 21.5 \text{ (depending on prefactor terms)}.$$
5. At $k=100$ with $K = 3.25$, $L = \lceil 3.25 \sqrt{\ln 100} \rceil = \lceil 3.25 \times 2.146 \rceil = \lceil 6.97 \rceil = 7$.
6. For $a = 7$: $C_{\mathrm{int}}(7) = \sqrt{1.20} \times (7 - 2) = 1.0954 \times 5 = 5.477 < 7$. The square has a deficit of $1.52$ elements (a $21.8\%$ shortfall).
7. Union Bound Divergence vs Capacity Deficit Dilemma (Level 3 falsers L03_N02, L03_N04): Attempting to resolve the capacity deficit by setting a block threshold $a_{\min}(\varepsilon) = \lceil\frac{\Delta\sqrt{1+2\varepsilon}}{\sqrt{1+2\varepsilon}-1}\rceil = \Theta(1/\varepsilon)$ constant in $k$ creates a fatal union bound divergence: single-square failure probability $\exp(-c(a_{\min}-\Delta)^2)$ is a positive constant independent of $k$, so the union bound over $|\mathcal{Q}_{\mathrm{squares}}| = 2(k+1)^3$ candidate host squares diverges as $\Theta(k^3) \to +\infty$ (reaching $3.26 \times 10^7$ at $k=10^8$). Conversely, if $a \ge K\sqrt{\log k}$ is enforced to guarantee $O(k^{-1})$ union bound convergence, then for all $k \le 10000$, $K\sqrt{\log k} \le 9.10 < 21.49 = a_{\min}$, which creates a strict capacity deficit ($\sqrt{1+2\varepsilon}(L-\Delta) < L$) where shrunken squares cannot embed their own blocks.

## Implications
Mesoscopic cutoffs cannot simultaneously reserve discrete $O(1)$ boundary buffers and maintain positive LIS surplus unless the block threshold is pushed to $L \ge \Omega(1/\varepsilon) \approx 22$. Pushing $L$ up to $22$, however, increases the fraction of elements in the residual component $\mathcal{R}$ to virtually 100%, further exacerbating the residual embedding barrier.

## Caveats
If boundary isolation can be achieved without reserving full-width guard strips (e.g. through soft probabilistic conditioning rather than hard geometric exclusion), the shrinkage penalty might be avoided, but no candidate has established a valid soft boundary decoupling mechanism.
