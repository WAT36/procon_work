n,m=map(int,input().split())
inf=float("inf")
d=[[inf for _ in range(n)] for _ in range(n)]
for i in range(n):
    d[i][i]=0

for i in range(m):
    a,b,t=map(int,input().split())
    d[a-1][b-1]=t
    d[b-1][a-1]=t

for a in range(n):
    for b in range(n):
        for c in range(n):
            d[b][c] = min(d[b][c],d[b][a]+d[a][c])

ans=inf
for i in range(n):
#    print(d[i])
    ans=min(ans,max(d[i]))
print(ans)

