N,W = [int(i) for i in input().split()]

w = []
v = []

for i in range(N):
    a,b = [int(i) for i in input().split()]
    w.append(a)
    v.append(b)

dp_w = [[-1 for i in range(W+1)] for j in range(N+1)]
dp_w[0] = [0 for i in range(W+1)]
for i in range(N):
    for j in range(W+1):
        if(j < w[i]):
            dp_w[i+1][j] = dp_w[i][j]
        else:
            dp_w[i+1][j] = max(dp_w[i][j-w[i]] + v[i],dp_w[i][j])
print(dp_w[N][W])