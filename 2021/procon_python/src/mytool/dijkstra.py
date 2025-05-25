INF=float("inf")

#始点,頂点の数,辺(頂点ごとの隣接行列)
def dijkstra(start,v,e):
    pre=[-1 for _ in range(v)]
    x=set([i for i in range(v)])
    dist=[INF for _ in range(v)]

    dist[start]=0

    s=start
    while(len(x)>0):
        x.remove(s)

        min_x=-1
        min_dx=float("inf")
        for xi in x:
            if(dist[xi]>dist[s]+e[s][xi]):
                dist[xi]=dist[s]+e[s][xi]
                pre[xi]=s

            if(min_dx>dist[xi]):
                min_dx=dist[xi]
                min_x=xi

        s=min_x

    return dist,pre

edge=[[INF,2  ,5  ,6  ,INF],
      [2  ,INF,1  ,INF,9  ],
      [5  ,1  ,INF,INF,10 ],
      [6  ,INF,INF,INF,4  ],
      [INF,9  ,10 ,4  ,INF]]
print(dijkstra(0, 5, edge))