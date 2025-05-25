import numpy as np
n,m,x=map(int,input().split())
MAX=9999999999

c=[]
a=[]
for i in range(n):
    ca=list(map(int,input().split()))
    c.append(ca[0])
    a.append(ca[1:])

c=np.array(c)
a=np.array(a)

pat=2**n
ans=MAX
for i in range(pat):
    pat_i=bin(i)[2:].zfill(n)
    ai=np.array([0 for _ in range(m)])
    ansi=0

    for j in range(len(pat_i)):
        if(pat_i[j]=='1'):
            ansi+=c[j]
            ai+=a[j]

    if(min(ai)>=x):
        ans=min(ans,ansi)

if(ans!=MAX):
    print(ans)
else:
    print(-1)