n,w=map(int,input().split())
dp=[[0 for _ in range(w+1)] for _ in range(n+1)]
for i in range(n):
    vi,wi=map(int,input().split())
    for j in range(w+1):
        if(j >= wi):
            dp[i+1][j] =max(dp[i][j-wi]+vi,dp[i][j])
        else:
            dp[i+1][j] =dp[i][j]
#    print(dp[i+1])
print(dp[n][w])