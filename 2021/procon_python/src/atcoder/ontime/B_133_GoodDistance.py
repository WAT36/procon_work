import math

l = list(map(int,input().split()))
N = l[0]
D = l[1]
x = []
for i in range(N):
    x.append(list(map(float,input().split())))

ans = 0
for i in range(N):
    for j in range(i+1,N):
        dist = 0
        for k in range(D):
            dist = dist + (x[j][k] - x[i][k])**2
        dist = math.sqrt(dist)
        if(dist.is_integer()):
            ans = ans + 1

print(ans)