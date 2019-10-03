import numpy as np

N,K = [int(i) for i in input().split()]
h = np.array(list(map(int,input().split())))

dp = [10**4] * N
dp[0] = 0
dp[1] = abs(h[1] - h[0])
for i in range(2,N):
    k = max(0,i-K)
    dp[i] = min(dp[k:i] + np.abs(h[k:i] - h[i]))

print(dp[N-1])