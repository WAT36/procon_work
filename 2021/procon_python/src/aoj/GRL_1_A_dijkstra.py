#https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/1/GRL_1_A
import math
import heapq
V,E,r=map(int,input().split())
edge=[[] for _ in range(V)]     # edge[i] : 頂点iからの辺、edge[i][j]:[v,c] 頂点iから頂点vまでの辺、コストc
d=[math.inf for _ in range(V)]  #頂点sからの最短距離

for i in range(E):
    si,ti,di=map(int,input().split())
    edge[si].append([ti,di])
#    edge[ti].append([si,di]) #有向なのでここは無し

#優先度付きキュー
q=[]
heapq.heapify(q)

def dijkstra(start):
    d[start]=0 #初期値
    heapq.heappush(q, [0,start])

    while(len(q)!=0):
        #まだ使われてない頂点のうち距離が最小のものを探す。ない場合は終了
        di=heapq.heappop(q)
        distance=di[0]
        v=di[1]

        if(d[v] < distance):
            continue

        ei = edge[v]
        for i in range(len(ei)):
            e = ei[i]
            if(d[e[0]] > d[v]+e[1]):
                d[e[0]] = d[v]+e[1]
                heapq.heappush(q, [d[e[0]],e[0]])

dijkstra(r)
for i in range(len(d)):
    print(d[i] if d[i]!=math.inf else "INF")
