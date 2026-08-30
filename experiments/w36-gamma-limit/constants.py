"""W36: certified upper bounds for the W34/Theorem-18 constants from E K_n <= n + sqrt(2n) + 1/2 (proof.md Thm 3.3).
C_b <= (1/2 + 1/sqrt(2b) + 1/(4b))^2;  C_mix_b <= (1/2 + (sqrt(2b)+sqrt(2b+2)+1)/(2(2b+1)))^2."""
import math
print(" b        C_b_cert   Cmix_b_cert")
for b in (1, 2, 4, 8, 16, 32, 64, 128, 256, 10**3, 10**4, 10**5, 10**6, 10**7):
    cb = (0.5 + 1 / math.sqrt(2 * b) + 1 / (4 * b)) ** 2
    cm = (0.5 + (math.sqrt(2 * b) + math.sqrt(2 * b + 2) + 1) / (2 * (2 * b + 1))) ** 2
    print(f"{b:8d}  {cb:.4f}     {cm:.4f}")
