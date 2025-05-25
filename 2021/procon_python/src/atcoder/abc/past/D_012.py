INF=float('inf')
n,m=map(int,input().split())
d=[[INF for _ in range(n+1)] for _ in range(n+1)]

for i in range(1,n+1):
    d[i][i]=0

for i in range(m):
    a,b,t=map(int,input().split())
    d[a][b]=t
    d[b][a]=t


for a in range(n+1):
    for b in range(n+1):
        for c in range(n+1):
            d[b][c] = min(d[b][c],d[b][a]+d[a][c])

ans=INF
for i in range(1,n+1):
    ans=min(ans,max(d[i][1:]))
print(ans)