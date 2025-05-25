h,n=map(int,input().split())
ab=[]
for _ in range(n):
    ab.append(list(map(int,input().split())))
max_a=max([a for a,b in ab])
dp=[0 for _ in range(h+max_a)]

for i in range(1,len(dp)):
    dp[i]=min(dp[i-a]+b for a,b in ab)
print(min(dp[h:]))


#
# MAX_NUM=9999999999
# ab=[]
# for _ in range(n):
#     ab.append(list(map(int,input().split())))
# dp=[MAX_NUM for _ in range(h+1)]
# dp[0]=0
#
# for i in range(h):
#     if(dp[i]!=MAX_NUM):
#         for j in range(n):
#             a,b=ab[j]
#             ind = i+a if i+a<h else -1
#             dp[ind]=min(dp[ind],dp[i]+b)
# print(dp[-1])

