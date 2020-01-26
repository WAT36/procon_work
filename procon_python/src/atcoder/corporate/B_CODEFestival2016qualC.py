import heapq

k,t=map(int,input().split())
a=list(map(int,input().split()))
a=list(map(lambda x: -1*x,a))
heapq.heapify(a)

h=heapq.heappop(a)
h+=1
pre_h=h

while(len(a)>0):
    h=heapq.heappop(a)
    if(h==0):
        break
    else:
        h+=1
        heapq.heappush(a, pre_h)
        pre_h=h

print(-1*pre_h)