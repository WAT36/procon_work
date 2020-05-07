h,w=map(int,input().split())
s=[]
for i in range(h):
    s.append(list(input()))

dp=[[99999999 for i in range(w)] for i in range(h)]


if(s[0][0]=='#'):
    dp[0][0]=1
else:
    dp[0][0]=0

for i in range(h):
    for j in range(w):

        if(s[i][j-1] != s[i][j]):
            left = dp[i][j-1]+1
        else:
            left = dp[i][j-1]

        if(s[i-1][j] != s[i][j]):
            top = dp[i-1][j]+1
        else:
            top = dp[i-1][j]

        dp[i][j] = min(dp[i][j],left,top)

print((dp[h-1][w-1]+1)//2)