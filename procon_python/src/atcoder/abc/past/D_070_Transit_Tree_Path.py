import sys
sys.setrecursionlimit(10**6)
n=int(input())
INF=9999999999
d=[INF for _ in range(n)]
g=[[] for _ in range(n)]


for i in range(n-1):
    a,b,c=map(int,input().split())
    g[a-1].append([b-1,c])
    g[b-1].append([a-1,c])

def dfs(v,p,dv):
    d[v]=dv
    for gi,c in g[v]:
        if(gi==p):
            continue
        dfs(gi,v,dv+c)

q,k=map(int,input().split())

dfs(k-1,-1,0)

for i in range(q):
    x,y=map(int,input().split())
    print(d[x-1]+d[y-1])


