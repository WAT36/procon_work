N = int(input())
h = list(map(int,input().split()))

mincost = [-1] * N
mincost[0] = 0
mincost[1] = abs(h[1] - h[0])

for i in range(2,N):
    a = mincost[i-2] + abs(h[i] - h[i-2])
    b = mincost[i-1] + abs(h[i] - h[i-1])
    mincost[i] = a if a < b else b

print(mincost[N-1])
