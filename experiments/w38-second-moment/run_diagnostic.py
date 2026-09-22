#!/usr/bin/env python3
"""A bounded, single-process audit. Never overwrite previous raw outputs."""
from pathlib import Path
import json
import math
import subprocess
import time

HERE = Path(__file__).resolve().parent
OUT = HERE / "out" / "review-20260910"
OUT.mkdir(exist_ok=True)
BINARY = OUT / "diagnose_can"
subprocess.run(["cc", "-O3", "-std=c11", "-Wall", "-Wextra", str(HERE / "diagnose_can.c"), "-lm", "-o", str(BINARY)], check=True)
specs = [(k, c, 1000 if k == 6 else 400) for k in (6, 8) for c in (.22, .25, .27, .30, .40)]
specs.append((10, .25, 64))
for k, c, hosts in specs:
    n = math.floor(c * k * k + 1e-9)
    stem = f"k{k}_n{n}"
    raw, meta = OUT / (stem + ".csv"), OUT / (stem + ".json")
    if raw.exists():
        print(f"Preserving existing {raw.name}", flush=True)
        continue
    seed = 2026091000 + 100 * k + n
    start = time.monotonic()
    with raw.open("x") as output, (OUT / (stem + ".log")).open("x") as log:
        subprocess.run([str(BINARY), str(k), str(n), str(hosts), str(seed)], stdout=output, stderr=log, check=True)
    data = dict(k=k, n=n, requested_C=c, actual_C=n/(k*k), hosts=hosts, seed=seed,
                subsets_per_host=math.comb(n,k), seconds=time.monotonic()-start)
    meta.write_text(json.dumps(data, indent=2) + "\n")
    print(f"Completed {stem}: {hosts} hosts, {data['seconds']:.1f}s", flush=True)
