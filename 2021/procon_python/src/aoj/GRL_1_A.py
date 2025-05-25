#Bellman-Ford
v,e,r=map(int,input().split())
INF=10**9
edge=[]
d=[INF for _ in range(v)]

for i in range(e):
    edge.append(list(map(int,input().split())))

d[r]=0
while(True):
    update=False
    for i in range(len(edge)):
        ei=edge[i]
        if(d[ei[0]] != INF and d[ei[1]] > d[ei[0]] + ei[2]):
            d[ei[1]] = d[ei[0]] + ei[2]
            update=True
    if(not update):
        break

for i in range(len(d)):
    print(d[i] if d[i] != INF else "INF")