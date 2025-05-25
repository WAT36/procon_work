n,k=map(int,input().split())
p=list(map(int,input().split()))
max_p=max(p)
e=[-1 for _ in range(max_p+1)]


def calc_e(i):
    if(e[i]==-1):
        ei=(i+1)/2
        e[i]=ei
        return ei
    else:
        return e[i]

ans=0
for i in range(k):
    ans+=calc_e(p[i])

now_e=ans
for i in range(1,n-k+1):
    now_e-=calc_e(p[i-1])
    now_e+=calc_e(p[i+k-1])
    if(ans<now_e):
        ans=now_e
print(ans)
