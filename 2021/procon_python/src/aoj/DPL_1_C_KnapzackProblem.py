n,w=map(int,input().split())
dp=[[0 for _ in range(w+1)] for _ in range(n+1)]
for i in range(1,n+1):
    vi,wi=map(int,input().split())
    for j in range(1,w+1):
        if(j<wi):
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=max(dp[i-1][j-wi]+vi,dp[i-1][j],dp[i][j-wi]+vi)
print(dp[n][w])