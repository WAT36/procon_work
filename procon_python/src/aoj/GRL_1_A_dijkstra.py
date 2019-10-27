import heapq
v,e,r=map(int,input().split())
INF=10**9
d=[INF for _ in range(v)]

edge=[[] for _ in range(v)]
for i in range(e):
    si,ti,di=map(int,input().split())
    edge[si].append([ti,di])

d[r]=0
q=[]
heapq.heapify(q)
heapq.heappush(q, [0,r])

while(len(q)>0):
    qi=heapq.heappop(q)
#    print(d)
#    print(qi)
    vi=qi[1]
    if(d[vi] >= qi[0]):
        for i in range(len(edge[vi])):
            ei = edge[vi][i]
#            print(ei)
            if(d[ei[0]] > d[vi] + ei[1]):
                d[ei[0]] = d[vi] + ei[1]
                heapq.heappush(q, [d[ei[0]],ei[0]])

for i in range(v):
    print(d[i] if d[i]!=INF else "INF")