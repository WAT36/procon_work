import heapq

def int_minus(x):
    return -1 * int(x)

n,m=map(int,input().split())
a=list(map(int_minus,input().split()))
heapq.heapify(a)
for i in range(m):
    maxa=-1 * heapq.heappop(a)
    maxa = maxa // 2
    heapq.heappush(a, -1 * maxa)
print(-1 * sum(a))