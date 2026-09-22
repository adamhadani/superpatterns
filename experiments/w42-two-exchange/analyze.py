#!/usr/bin/env python3
"""Summarize exact census integers; no simulation or fitted constants."""
from fractions import Fraction
import json
from pathlib import Path

root = Path(__file__).parent
data = json.loads((root / 'exact-census.json').read_text())
lines = [
    '# Exact census summary', '',
    'All expectations average over an independent uniform target and uniform host.',
    'Ratios are computed as exact fractions and displayed rounded to six decimals.', '',
    '| k | n | E Y1 | E Y2 | R1 | R2 |',
    '|---|---|---|---|---|---|',
]
for cell in data:
    rows = cell['patterns']
    population = cell['hosts'] * len(rows)
    means = [Fraction(sum(r[f'y{d}'] for r in rows), population) for d in (1, 2)]
    ratios = [Fraction(sum(r[f'y{d}_squared'] for r in rows), population) / means[d-1]**2
              for d in (1, 2)]
    lines.append(f'| {cell["k"]} | {cell["n"]} | {means[0]} | {means[1]} | '
                 f'{float(ratios[0]):.6f} | {float(ratios[1]):.6f} |')
(root / 'summary.md').write_text('\n'.join(lines) + '\n')
print('\n'.join(lines))
