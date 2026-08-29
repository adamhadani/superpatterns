# bisect.py r h [-free] [reps] : C_1/2 = N_1/2 / k^2 by bisection on C, prints trace; appends to results.txt
import subprocess,sys
r=int(sys.argv[1]); h=int(sys.argv[2]); free='-free' in sys.argv; iid='-iid' in sys.argv
reps=int(sys.argv[3]) if len(sys.argv)>3 and sys.argv[3].isdigit() else 400
k=r*h; lo,hi=0.15,1.2; seed=7
trace=[]
for it in range(11):
    C=(lo+hi)/2; N=int(C*k*k)
    out=subprocess.run(['./tg',str(r),str(h),str(N),str(reps),str(seed)]+(['-free'] if free else [])+(['-iid'] if iid else []),capture_output=True,text=True).stdout.split()
    p=int(out[4])/reps; trace.append((round(C,4),p)); seed+=1
    if p<0.5: lo=C
    else: hi=C
res=f"{'free' if free else ('iid' if iid else 'fixed')} r={r} h={h} k={k} reps={reps} C_1/2={(lo+hi)/2:.4f} trace={trace}"
print(res); open('results.txt','a').write(res+'\n')
