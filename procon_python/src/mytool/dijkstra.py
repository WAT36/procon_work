
#始点,頂点の数,辺(頂点ごとの隣接行列)
def dijkstra(start,v,e):
    pre=[-1 for _ in range(v)]
    x=set([])
    y=set([i for i in range(v)])
    dist=[float("inf") for _ in range(v)]

    dist[start]=0

    s=start
    while(len(y)>0):
        x.add(s)
        y.remove(s)

        min_y=-1
        min_dy=float("inf")
        for yi in y:
            if(dist[yi]>dist[s]+e[s][yi]):
                dist[yi]=dist[s]+e[s][yi]
                pre[yi]=s

            if(min_dy>dist[yi]):
                min_dy=dist[yi]
                min_y=yi

        s=min_y

    return dist,pre

#edge=[[0,2,5,6,0],[2,0,1,0,9],[5,1,0,0,10],[6,0,0,0,4],[0,9,10,4,0]]
#print(dijkstra(0, 5, edge))