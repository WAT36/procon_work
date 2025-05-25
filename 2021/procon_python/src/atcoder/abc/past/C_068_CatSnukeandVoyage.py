# -*- coding:utf-8 -*-

num = list(map(int,input().split()))
N = num[0]
M = num[1]

a = []
b = []

firstisland = []
islandlast = []

for i in range(M):
    num = list(map(int,input().split()))
    a.append(num[0])
    b.append(num[1])
    if (num[0] == 1):
        firstisland.append(num[1])
    if (num[1] == N):
        islandlast.append(num[0])

island = set(firstisland) & set(islandlast)

if (len(island) > 0):
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")

