from collections import deque
n,m=map(int,input().split())

q=deque([])

edge=[set([]) for _ in range(n+1)]
mark=[-1 for _ in range(n+1)]
used=[False for _ in range(n+1)]
for i in range(m):
    a,b=map(int,input().split())
    edge[a].add(b)
    edge[b].add(a)

q.append(1)
mark[1]=1
used[1]=True
while(len(q)>0):
    vi=q.popleft()
    ei=edge[vi]
    for eij in ei:
        if(used[eij]):
            continue
        else:
            mark[eij]=vi
            used[eij]=True
            q.append(eij)

print('Yes')
for i in range(2,len(mark)):
    print(mark[i])