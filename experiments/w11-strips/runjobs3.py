#!/usr/bin/env python3
# usage: runjobs3.py jobsfile P — lines "name<TAB>cmd" -> out2/name.txt (skipped if present); per-job timeout 1800 s
import sys,subprocess,os,concurrent.futures as cf
os.chdir('/Users/adamhadani/Development/math-proofs/superpatterns/work/w11-strips')
jobs=[l.rstrip('\n').split('\t') for l in open(sys.argv[1]) if '\t' in l]
def run(j):
    name,cmd=j; f=f'out2/{name}.txt'
    if os.path.exists(f) and os.path.getsize(f)>0: return
    try: out=subprocess.run(cmd,shell=True,capture_output=True,text=True,timeout=1800).stdout
    except subprocess.TimeoutExpired: out='TIMEOUT\n'
    open(f,'w').write(out)
with cf.ThreadPoolExecutor(int(sys.argv[2])) as ex: list(ex.map(run,jobs))
