from collections import deque
n,u,v=map(int,input().split())
g=[set([]) for _ in range(n+1)]
for i in range(n-1):
    a,b=map(int,input().split())
    g[a].add(b)
    g[b].add(a)

leaf=[]
for i in range(1,n+1):
    if(len(g[i])==1):
        leaf.append(i)

d_u=[-1 for _ in range(n+1)]
d_v=[-1 for _ in range(n+1)]

def bfs(start,d):
    d[start]=0
    q=deque([start])

    while(len(q)>0):
        qi=q.popleft()
        di=d[qi]

        next_qi=g[qi]
        for i in next_qi:
            if(d[i]==-1):
                d[i]=di+1
                q.append(i)

    return d


d_u=bfs(u, d_u)
d_v=bfs(v, d_v)


if(u in leaf and list(g[u])[0]==v):
    print(0)
else:
    ans=0
    for li in leaf:
        if(d_u[li]<d_v[li]):
            ans=max(ans,d_v[li]-1)
    print(ans)
