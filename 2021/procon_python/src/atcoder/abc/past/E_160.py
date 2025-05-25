import heapq
x,y,a,b,c=map(int,input().split())
p=list(map(int,input().split()))
p.sort()
p=p[-1*x:]
q=list(map(int,input().split()))
q.sort()
pq=p
pq.extend(q[-1*y:])
r=list(map(lambda x:-1*int(x),input().split()))
heapq.heapify(pq)
heapq.heapify(r)
while(len(r)>0):
    max_r=-1*heapq.heappop(r)
    min_pq=heapq.heappop(pq)
#    print(max_r,min_pq)
#    print(pq)
#    print(r)
    if(min_pq < max_r):
        heapq.heappush(pq,max_r)
    else:
        heapq.heappush(pq,min_pq)
        break
print(sum(pq))