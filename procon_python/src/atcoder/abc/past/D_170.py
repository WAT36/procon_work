import numpy as np
n=int(input())
a=sorted(list(map(int,input().split())))

dp=np.array([0 for _ in range(max(a)+1)])
for i in range(n):
    ai=a[i]
    if(dp[ai]>=2):
        continue

    j=1
    while(ai*j<=a[-1]):
        dp[ai*j]+=1
        j+=1

print(sum(dp[ai]==1 for ai in a))
