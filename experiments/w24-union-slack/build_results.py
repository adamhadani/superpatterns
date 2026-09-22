"""Assemble results.md from results_head.md, prose blocks, and sections of analysis.txt."""
import re
A = open('analysis.txt').read()
def section(start, end):
    i = A.index(start); j = A.index(end, i) if end else len(A); return A[i:j].rstrip() + '\n'
def block(k, n, task):
    key = f'**k={k}, n={n}**'
    i = A.index(key, A.index('### Task 3') if task == 3 else A.index('### Task 4'))
    j = A.find('\n**k=', i+1); j2 = A.find('\n### ', i+1)
    j = min(x for x in (j, j2, len(A)) if x > 0); return A[i:j].rstrip() + '\n'
out = [open('results_head.md').read()]
out.append(open('results_body.md').read())
out.append('\n\n## A. Task 1 — full tables\n\n' + section('### Task 1', '### Task 2'))
out.append('\n## B. Task 2 — fits (machine output)\n\n' + section('### Task 2', '### Task 3'))
out.append('\n## C. Task 3 — pairwise correlations at n ≈ t(k) and in the tail (selected points; all points in analysis.txt)\n\n')
out.append(A[A.index('### Task 3'):A.index('\n**k=', A.index('### Task 3'))] + '\n')
for k, n in [(5,19),(6,28),(7,37),(8,48),(8,52),(8,55),(9,60),(9,62),(9,64),(9,68)]:
    try: out.append('\n' + block(k, n, 3))
    except ValueError: pass
out.append('\n## D. Task 4 — structure of the missing patterns (selected points; all points in analysis.txt)\n\n')
for k, n in [(5,19),(6,28),(7,37),(7,44),(8,48),(8,55),(9,60),(9,64)]:
    try: out.append('\n' + block(k, n, 4))
    except ValueError: pass
open('results.md', 'w').write('\n'.join(out))
print('results.md written:', sum(len(x) for x in out), 'chars')
