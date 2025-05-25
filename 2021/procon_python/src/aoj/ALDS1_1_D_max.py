n=int(input())
ans=-9999999999999
buy=int(input())
sell=buy
for i in range(1,n):
    buy=min(sell,buy)
    sell=int(input())
    if(ans < sell-buy):
        ans=sell-buy
print(ans)

